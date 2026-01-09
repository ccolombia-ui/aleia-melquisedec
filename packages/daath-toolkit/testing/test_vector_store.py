"""
Tests for storage.vector_store module

Tests:
- Pinecone index creation/connection
- OpenAI embedding generation
- Artifact upsertion (insert/update)
- Domain-specific searching
- Instance-specific searching
- Namespace management
- Metadata filtering
- Artifact deletion
- Stats retrieval

Uses mocked Pinecone and OpenAI clients.
"""

import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from storage.vector_store import DomainAwareVectorStore


class TestDomainAwareVectorStore:
    """Test suite for DomainAwareVectorStore"""

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_initialization_creates_index_if_not_exists(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Initialization should create index if it doesn't exist"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        # Should call create_index
        mock_pinecone_client.create_index.assert_called_once()
        assert store.index_name == "test-index"

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_upsert_artifact_generates_embedding(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Upserting artifact should generate embedding and call Pinecone upsert"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        artifact_id = store.upsert_artifact(
            domain_id="DD-001",
            instance_id="I001",
            artifact_id="concept-crisp-dm",
            artifact_type="concept",
            text="CRISP-DM methodology",
        )

        # Should call OpenAI embeddings
        mock_openai_client.embeddings.create.assert_called_once()

        # Should call Pinecone upsert
        mock_pinecone_client.Index.return_value.upsert.assert_called_once()

        assert artifact_id == "concept-crisp-dm"

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_upsert_artifact_uses_correct_namespace(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Artifact should be inserted with correct namespace format"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        store.upsert_artifact(
            domain_id="DD-001",
            instance_id="I001",
            artifact_id="test-artifact",
            artifact_type="concept",
            text="Test text",
        )

        # Check that upsert was called with correct namespace
        call_args = mock_pinecone_client.Index.return_value.upsert.call_args
        assert call_args[1]["namespace"] == "DD-001.I001"

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_search_in_domain_queries_correct_namespace(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Searching in domain should query correct namespace"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        results = store.search_in_domain(query="data mining", domain_id="DD-001", top_k=5)

        # Should generate embedding for query
        mock_openai_client.embeddings.create.assert_called()

        # Should query Pinecone
        mock_pinecone_client.Index.return_value.query.assert_called_once()

        # Check results format
        assert len(results) == 1
        assert "id" in results[0]
        assert "score" in results[0]

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_search_in_instance_uses_specific_namespace(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Searching in instance should use domain.instance namespace"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        store.search_in_instance(
            query="test query", domain_id="DD-001", instance_id="I001", top_k=3
        )

        # Check namespace in query call
        call_args = mock_pinecone_client.Index.return_value.query.call_args
        assert call_args[1]["namespace"] == "DD-001.I001"

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_upsert_artifact_includes_metadata(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Upserting artifact should include provided metadata"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        custom_metadata = {"version": "1.0.0", "author": "HYPATIA"}

        store.upsert_artifact(
            domain_id="DD-001",
            instance_id="I001",
            artifact_id="test-artifact",
            artifact_type="concept",
            text="Test text",
            metadata=custom_metadata,
        )

        # Check metadata was passed to upsert
        call_args = mock_pinecone_client.Index.return_value.upsert.call_args
        vectors = call_args[1]["vectors"]
        metadata = vectors[0]["metadata"]

        assert metadata["version"] == "1.0.0"
        assert metadata["author"] == "HYPATIA"
        assert metadata["artifact_type"] == "concept"

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_delete_artifact_removes_from_namespace(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Deleting artifact should call Pinecone delete with correct namespace"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        store.delete_artifact(domain_id="DD-001", instance_id="I001", artifact_id="test-artifact")

        # Should call delete
        mock_pinecone_client.Index.return_value.delete.assert_called_once()
        call_args = mock_pinecone_client.Index.return_value.delete.call_args
        assert call_args[1]["namespace"] == "DD-001.I001"

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_get_domain_stats_returns_namespace_info(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Getting domain stats should return namespace statistics"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        stats = store.get_domain_stats(domain_id="DD-001")

        # Should call describe_index_stats
        mock_pinecone_client.Index.return_value.describe_index_stats.assert_called_once()

        assert "namespaces" in stats
        assert stats["total_vector_count"] == 10

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_search_with_metadata_filter(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Searching with metadata filter should pass filter to Pinecone"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        metadata_filter = {"artifact_type": "concept"}

        store.search_in_domain(
            query="test query", domain_id="DD-001", top_k=5, metadata_filter=metadata_filter
        )

        # Check that filter was passed
        call_args = mock_pinecone_client.Index.return_value.query.call_args
        assert call_args[1]["filter"] == metadata_filter

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_embedding_dimension_configurable(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Embedding dimension should be configurable"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index", dimension=3072)

        # Check that create_index was called with correct dimension
        call_args = mock_pinecone_client.create_index.call_args
        assert call_args[1]["dimension"] == 3072

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_empty_search_results_handled(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Empty search results should be handled gracefully"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        # Mock empty results
        mock_pinecone_client.Index.return_value.query.return_value = {"matches": []}

        store = DomainAwareVectorStore(index_name="test-index")

        results = store.search_in_domain(query="non-existent query", domain_id="DD-001", top_k=5)

        assert len(results) == 0

    @patch("storage.vector_store.Pinecone")
    @patch("storage.vector_store.OpenAI")
    def test_artifact_type_validation(
        self, mock_openai_class, mock_pinecone_class, mock_pinecone_client, mock_openai_client
    ):
        """Artifact type should be one of allowed types"""
        mock_pinecone_class.return_value = mock_pinecone_client
        mock_openai_class.return_value = mock_openai_client

        store = DomainAwareVectorStore(index_name="test-index")

        # Valid types
        valid_types = ["concept", "analysis", "output", "lesson"]

        for artifact_type in valid_types:
            store.upsert_artifact(
                domain_id="DD-001",
                instance_id="I001",
                artifact_id=f"test-{artifact_type}",
                artifact_type=artifact_type,
                text="Test text",
            )

        # Should have called upsert 4 times
        assert mock_pinecone_client.Index.return_value.upsert.call_count == 4
