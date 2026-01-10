"""
Unit tests for HybridRetriever

Uses mocks to test retrieval logic without requiring
Neo4j or LlamaIndex to be running.
"""

from time import time
from unittest.mock import MagicMock, Mock, patch

import pytest
from triple_persistence.models import QueryRequest, QueryResponse, QueryResult
from triple_persistence.retriever import HybridRetriever


@pytest.fixture
def mock_index():
    """Mock LlamaIndex VectorStoreIndex"""
    index = Mock()
    retriever = Mock()
    index.as_retriever.return_value = retriever

    # Mock query engine
    query_engine = Mock()
    index.as_query_engine.return_value = query_engine

    return index


@pytest.fixture
def mock_neo4j_driver():
    """Mock Neo4j driver"""
    driver = Mock()
    session = Mock()
    driver.session.return_value.__enter__ = Mock(return_value=session)
    driver.session.return_value.__exit__ = Mock(return_value=None)
    return driver


@pytest.fixture
def mock_nodes():
    """Mock NodeWithScore results"""
    node1 = Mock()
    node1.score = 0.95
    node1.node.metadata = {"document_id": "doc-001", "file_path": "/path/to/doc1.md"}
    node1.node.get_content.return_value = "Content of document 1"

    node2 = Mock()
    node2.score = 0.85
    node2.node.metadata = {"document_id": "doc-002", "file_path": "/path/to/doc2.md"}
    node2.node.get_content.return_value = "Content of document 2"

    return [node1, node2]


class TestHybridRetriever:
    """Test HybridRetriever class"""

    def test_init(self, mock_index, mock_neo4j_driver):
        """Test retriever initialization"""
        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test-project"
        )

        assert retriever.index == mock_index
        assert retriever.driver == mock_neo4j_driver
        assert retriever.project == "test-project"
        mock_index.as_query_engine.assert_called_once()

    def test_vector_search(self, mock_index, mock_neo4j_driver, mock_nodes):
        """Test vector similarity search"""
        # Setup
        mock_retriever = Mock()
        mock_retriever.retrieve.return_value = mock_nodes
        mock_index.as_retriever.return_value = mock_retriever

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        results = retriever._vector_search("test query", top_k=10)

        # Assert
        assert results == mock_nodes
        mock_index.as_retriever.assert_called_with(similarity_top_k=10)
        mock_retriever.retrieve.assert_called_once_with("test query")

    def test_group_by_document(self, mock_index, mock_neo4j_driver, mock_nodes):
        """Test grouping chunks by document"""
        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        results = retriever._group_by_document(mock_nodes)

        # Assert
        assert len(results) == 2
        assert results[0].document_id == "doc-001"
        assert results[0].similarity == 0.95
        assert results[1].document_id == "doc-002"
        assert results[1].similarity == 0.85

    def test_group_by_document_keeps_highest_score(self, mock_index, mock_neo4j_driver):
        """Test that grouping keeps the highest score per document"""
        # Create nodes with same document_id but different scores
        node1 = Mock()
        node1.score = 0.95
        node1.node.metadata = {"document_id": "doc-001", "file_path": "/doc.md"}
        node1.node.get_content.return_value = "Content 1"

        node2 = Mock()
        node2.score = 0.85
        node2.node.metadata = {"document_id": "doc-001", "file_path": "/doc.md"}
        node2.node.get_content.return_value = "Content 2"

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        results = retriever._group_by_document([node1, node2])

        # Assert - should only have one result with highest score
        assert len(results) == 1
        assert results[0].similarity == 0.95
        assert results[0].excerpt == "Content 1"

    def test_enrich_with_graph(self, mock_index, mock_neo4j_driver):
        """Test graph enrichment"""
        # Setup session mock
        mock_session = Mock()
        mock_result = Mock()
        mock_result.data.return_value = [
            {"id": "doc-002", "path": "/doc2.md", "title": "Doc 2"},
            {"id": "doc-003", "path": "/doc3.md", "title": "Doc 3"},
        ]
        mock_session.run.return_value = mock_result
        mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

        # Create test results
        results = [
            QueryResult(
                document_id="doc-001",
                document_path="/doc1.md",
                similarity=0.95,
                excerpt="Content 1",
            )
        ]

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        enriched = retriever._enrich_with_graph(results, max_related=5)

        # Assert
        assert len(enriched) == 1
        assert len(enriched[0].related_documents) == 2
        assert "doc-002" in enriched[0].related_documents
        assert "doc-003" in enriched[0].related_documents
        # Score should be boosted
        assert enriched[0].similarity > 0.95

    def test_apply_filters_type(self, mock_index, mock_neo4j_driver):
        """Test filtering by document type"""
        # Setup
        mock_session = Mock()
        mock_result = Mock()
        mock_result.single.return_value = {"type": "atomic"}
        mock_session.run.return_value = mock_result
        mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

        results = [
            QueryResult(
                document_id="doc-001", document_path="/doc1.md", similarity=0.95, excerpt="Content"
            )
        ]

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute - filter matches
        filtered = retriever._apply_filters(results, {"type": "atomic"})
        assert len(filtered) == 1

        # Execute - filter doesn't match
        mock_result.single.return_value = {"type": "requirement"}
        filtered = retriever._apply_filters(results, {"type": "atomic"})
        assert len(filtered) == 0

    def test_query_full_flow(self, mock_index, mock_neo4j_driver, mock_nodes):
        """Test complete query flow"""
        # Setup
        mock_retriever = Mock()
        mock_retriever.retrieve.return_value = mock_nodes
        mock_index.as_retriever.return_value = mock_retriever

        mock_session = Mock()
        mock_session.run.return_value.data.return_value = []
        mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        request = QueryRequest(query="test query", top_k=2, include_graph=False)
        response = retriever.query(request)

        # Assert
        assert isinstance(response, QueryResponse)
        assert response.total_results == 2
        assert response.query_time_ms > 0
        assert len(response.results) == 2
        assert response.results[0].similarity >= response.results[1].similarity

    def test_query_with_graph_enrichment(self, mock_index, mock_neo4j_driver, mock_nodes):
        """Test query with graph enrichment enabled"""
        # Setup
        mock_retriever = Mock()
        mock_retriever.retrieve.return_value = mock_nodes
        mock_index.as_retriever.return_value = mock_retriever

        mock_session = Mock()
        mock_result = Mock()
        mock_result.data.return_value = [{"id": "doc-003", "path": "/doc3.md", "title": "Doc 3"}]
        mock_session.run.return_value = mock_result
        mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        request = QueryRequest(query="test query", top_k=2, include_graph=True)
        response = retriever.query(request)

        # Assert
        assert response.total_results == 2
        # Should have related documents
        for result in response.results:
            assert len(result.related_documents) > 0

    def test_get_document_context(self, mock_index, mock_neo4j_driver):
        """Test getting full document context"""
        # Setup
        mock_session = Mock()

        # Mock document query
        doc_result = Mock()
        doc_result.single.return_value = {
            "d": {"id": "doc-001", "title": "Test Doc", "path": "/doc.md"}
        }

        # Mock relationships query
        rel_result = Mock()
        rel_result.single.return_value = {
            "references": [{"id": "doc-002", "title": "Doc 2"}],
            "referenced_by": [],
            "tags": ["tag1", "tag2"],
            "phase": "010-define",
            "rostro": "MELQUISEDEC",
        }

        mock_session.run.side_effect = [doc_result, rel_result]
        mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        context = retriever.get_document_context("doc-001")

        # Assert
        assert "document" in context
        assert context["document"]["id"] == "doc-001"
        assert len(context["references"]) == 1
        assert len(context["tags"]) == 2
        assert context["phase"] == "010-define"
        assert context["rostro"] == "MELQUISEDEC"

    def test_get_stats(self, mock_index, mock_neo4j_driver):
        """Test knowledge base statistics"""
        # Setup
        mock_session = Mock()
        mock_result = Mock()
        mock_result.single.return_value = {
            "documents": 10,
            "chunks": 50,
            "tags": 5,
            "phases": 3,
            "rostros": 2,
            "references": 15,
        }
        mock_session.run.return_value = mock_result
        mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

        retriever = HybridRetriever(
            index=mock_index, neo4j_driver=mock_neo4j_driver, project="test"
        )

        # Execute
        stats = retriever.get_stats()

        # Assert
        assert stats["documents"] == 10
        assert stats["chunks"] == 50
        assert stats["tags"] == 5
        assert stats["phases"] == 3
        assert stats["rostros"] == 2
        assert stats["references"] == 15
