from unittest.mock import Mock

import pytest
from triple_persistence.models import QueryRequest, QueryResult
from triple_persistence.retriever import HybridRetriever


def test_vector_search_empty(mock_index, mock_neo4j_driver):
    mock_retriever = Mock()
    mock_retriever.retrieve.return_value = []
    mock_index.as_retriever.return_value = mock_retriever

    retriever = HybridRetriever(index=mock_index, neo4j_driver=mock_neo4j_driver, project="test")

    nodes = retriever._vector_search("nothing", top_k=5)
    assert nodes == []
    mock_index.as_retriever.assert_called_with(similarity_top_k=5)


def test_apply_filters_rostro_phase_tags(mock_index, mock_neo4j_driver):
    # Setup session responses for type/rostro/phase/tags
    mock_session = Mock()

    # For type check (not used here)
    # For rostro check: return count 1
    rostro_res = Mock()
    rostro_res.single.return_value = {"count": 1}

    phase_res = Mock()
    phase_res.single.return_value = {"count": 1}

    tag_res = Mock()
    tag_res.single.return_value = {"count": 1}

    # The sequence of calls will return these in order
    mock_session.run.side_effect = [rostro_res, phase_res, tag_res]
    mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

    results = [
        QueryResult(
            document_id="doc-001",
            document_path="/doc1.md",
            similarity=0.9,
            excerpt="x",
            related_documents=[],
            metadata={},
        )
    ]

    retriever = HybridRetriever(index=mock_index, neo4j_driver=mock_neo4j_driver, project="test")

    filtered = retriever._apply_filters(
        results, {"rostro": "MELQUISEDEC", "phase": "010-define", "tags": ["tag1"]}
    )
    assert len(filtered) == 1

    # Now simulate missing tag
    tag_res.single.return_value = {"count": 0}
    mock_session.run.side_effect = [rostro_res, phase_res, tag_res]
    filtered = retriever._apply_filters(
        results, {"rostro": "MELQUISEDEC", "phase": "010-define", "tags": ["tag1"]}
    )
    assert len(filtered) == 0


def test_get_document_context_not_found(mock_index, mock_neo4j_driver):
    mock_session = Mock()
    doc_result = Mock()
    doc_result.single.return_value = None
    mock_session.run.return_value = doc_result
    mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

    retriever = HybridRetriever(index=mock_index, neo4j_driver=mock_neo4j_driver, project="test")
    context = retriever.get_document_context("missing")
    assert context == {}


def test_enrich_with_graph_no_related(mock_index, mock_neo4j_driver):
    # Setup session to return empty list
    mock_session = Mock()
    mock_result = Mock()
    mock_result.data.return_value = []
    mock_session.run.return_value = mock_result
    mock_neo4j_driver.session.return_value.__enter__ = Mock(return_value=mock_session)

    results = [
        QueryResult(
            document_id="doc-001",
            document_path="/doc1.md",
            similarity=0.5,
            excerpt="x",
            related_documents=[],
            metadata={},
        )
    ]

    retriever = HybridRetriever(index=mock_index, neo4j_driver=mock_neo4j_driver, project="test")
    enriched = retriever._enrich_with_graph(results, max_related=5)
    assert enriched[0].related_documents == []
    assert pytest.approx(enriched[0].similarity, 0.0001) == 0.5
