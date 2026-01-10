"""
Unit tests for TriplePersistencePipeline

Uses mocks to test ingestion logic without requiring
Neo4j or Ollama to be running.
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, Mock, call, patch

import pytest
from triple_persistence.ingestion import TriplePersistencePipeline
from triple_persistence.models import Document, IngestionConfig


@pytest.fixture
def config():
    """Test configuration"""
    return IngestionConfig(
        project="test-project",
        paths=["tests/fixtures"],
        neo4j_uri="bolt://localhost:7687",
        neo4j_user="neo4j",
        neo4j_password="password",
        ollama_base_url="http://localhost:11434",
        embedding_model="nomic-embed-text",
        embed_dim=768,
    )


@pytest.fixture
def mock_neo4j_driver():
    """Mock Neo4j driver"""
    driver = Mock()
    session = Mock()
    driver.session.return_value.__enter__ = Mock(return_value=session)
    driver.session.return_value.__exit__ = Mock(return_value=None)
    return driver


@pytest.fixture
def mock_embedder():
    """Mock Ollama embedder"""
    embedder = Mock()
    embedder.model_name = "nomic-embed-text"
    return embedder


@pytest.fixture
def mock_vector_store():
    """Mock Neo4j vector store"""
    store = Mock()
    store.index_name = "test_embeddings"
    return store


class TestTriplePersistencePipeline:
    """Test TriplePersistencePipeline class"""

    @patch("triple_persistence.ingestion.GraphDatabase")
    @patch("triple_persistence.ingestion.OllamaEmbedding")
    @patch("triple_persistence.ingestion.Neo4jVectorStore")
    def test_init(
        self,
        mock_vector_store_class,
        mock_embedder_class,
        mock_graph_db,
        config,
        mock_neo4j_driver,
        mock_embedder,
    ):
        """Test pipeline initialization"""
        # Setup mocks
        mock_graph_db.driver.return_value = mock_neo4j_driver
        mock_embedder_class.return_value = mock_embedder
        mock_vector_store_class.return_value = Mock()

        # Initialize pipeline
        pipeline = TriplePersistencePipeline(config)

        # Assert
        assert pipeline.config == config
        assert pipeline.embedder == mock_embedder
        assert pipeline.neo4j_driver == mock_neo4j_driver
        mock_graph_db.driver.assert_called_once_with(
            config.neo4j_uri, auth=(config.neo4j_user, config.neo4j_password)
        )
        mock_embedder_class.assert_called_once()

    def test_extract_title(self, config):
        """Test title extraction from markdown"""
        with patch("triple_persistence.ingestion.GraphDatabase"), patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            pipeline = TriplePersistencePipeline(config)

            # Test with heading
            text = "# My Document Title\n\nSome content"
            title = pipeline._extract_title(text)
            assert title == "My Document Title"

            # Test without heading
            text = "Just some text without heading"
            title = pipeline._extract_title(text)
            assert title is None

            # Test with multiple headings
            text = "# First Title\n## Second Title"
            title = pipeline._extract_title(text)
            assert title == "First Title"

    def test_detect_document_type(self, config):
        """Test document type detection"""
        with patch("triple_persistence.ingestion.GraphDatabase"), patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            pipeline = TriplePersistencePipeline(config)

            # Test atomic
            path = Path("atomics/atomic-001.md")
            doc_type = pipeline._detect_document_type(path, "")
            assert doc_type == "atomic"

            # Test requirement
            path = Path("requirements/req-001.md")
            doc_type = pipeline._detect_document_type(path, "")
            assert doc_type == "requirement"

            # Test ADR
            path = Path("decisions/adr-001.md")
            doc_type = pipeline._detect_document_type(path, "")
            assert doc_type == "adr"

            # Test default
            path = Path("docs/readme.md")
            doc_type = pipeline._detect_document_type(path, "")
            assert doc_type == "document"

    def test_detect_rostro(self, config):
        """Test rostro detection"""
        with patch("triple_persistence.ingestion.GraphDatabase"), patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            pipeline = TriplePersistencePipeline(config)

            # Test MELQUISEDEC
            text = "This document is about MELQUISEDEC principles"
            rostro = pipeline._detect_rostro(text)
            assert rostro == "MELQUISEDEC"

            # Test HYPATIA
            text = "HYPATIA is the knowledge keeper"
            rostro = pipeline._detect_rostro(text)
            assert rostro == "HYPATIA"

            # Test no rostro
            text = "Just regular text"
            rostro = pipeline._detect_rostro(text)
            assert rostro is None

    def test_detect_phase(self, config):
        """Test phase detection from path"""
        with patch("triple_persistence.ingestion.GraphDatabase"), patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            pipeline = TriplePersistencePipeline(config)

            # Test 010-define
            path = Path("apps/project/010-define/doc.md")
            phase = pipeline._detect_phase(path)
            assert phase == "010-define"

            # Test 020-conceive
            path = Path("research/020-conceive/readme.md")
            phase = pipeline._detect_phase(path)
            assert phase == "020-conceive"

            # Test no phase
            path = Path("docs/readme.md")
            phase = pipeline._detect_phase(path)
            assert phase is None

    def test_extract_references(self, config):
        """Test wikilink extraction"""
        with patch("triple_persistence.ingestion.GraphDatabase"), patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            pipeline = TriplePersistencePipeline(config)

            # Test simple wikilinks
            text = "See [[Document A]] and [[Document B]]"
            refs = pipeline._extract_references(text)
            assert refs == ["Document A", "Document B"]

            # Test with aliases
            text = "See [[Document A|Link Text]]"
            refs = pipeline._extract_references(text)
            assert refs == ["Document A"]

            # Test no references
            text = "No references here"
            refs = pipeline._extract_references(text)
            assert refs == []

    def test_extract_tags(self, config):
        """Test hashtag extraction"""
        with patch("triple_persistence.ingestion.GraphDatabase"), patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            pipeline = TriplePersistencePipeline(config)

            # Test tags
            text = "This is #important and #urgent"
            tags = pipeline._extract_tags(text)
            assert set(tags) == {"important", "urgent"}

            # Test filtering markdown headers (numbers only)
            text = "# Heading\n#tag1 #tag2 #123"
            tags = pipeline._extract_tags(text)
            assert "tag1" in tags
            assert "tag2" in tags
            assert "123" not in tags  # Numbers filtered

    @patch("triple_persistence.ingestion.SimpleDirectoryReader")
    @patch("triple_persistence.ingestion.SemanticSplitterNodeParser")
    @patch("triple_persistence.ingestion.VectorStoreIndex")
    @patch("triple_persistence.ingestion.GraphDatabase")
    @patch("triple_persistence.ingestion.OllamaEmbedding")
    @patch("triple_persistence.ingestion.Neo4jVectorStore")
    def test_ingest_directory(
        self,
        mock_vector_store_class,
        mock_embedder_class,
        mock_graph_db,
        mock_index_class,
        mock_splitter_class,
        mock_reader_class,
        config,
    ):
        """Test directory ingestion"""
        # Setup mocks
        mock_driver = Mock()
        mock_session = Mock()
        mock_driver.session.return_value.__enter__ = Mock(return_value=mock_session)
        mock_driver.session.return_value.__exit__ = Mock(return_value=None)
        mock_graph_db.driver.return_value = mock_driver

        # Mock reader
        mock_doc = Mock()
        mock_doc.metadata = {"file_path": "/test/doc.md"}
        mock_doc.text = "# Test Document\n\nContent"
        mock_reader = Mock()
        mock_reader.load_data.return_value = [mock_doc]
        mock_reader_class.return_value = mock_reader

        # Mock splitter
        mock_node = Mock()
        mock_node.metadata = {"document_id": "test-id"}
        mock_splitter = Mock()
        mock_splitter.get_nodes_from_documents.return_value = [mock_node]
        mock_splitter_class.return_value = mock_splitter

        # Mock index
        mock_index = Mock()
        mock_index_class.return_value = mock_index

        # Initialize and run
        pipeline = TriplePersistencePipeline(config)
        stats = pipeline.ingest_directory("tests/fixtures")

        # Assert
        assert stats["documents_processed"] == 1
        assert stats["chunks_created"] == 1
        assert stats["project"] == "test-project"
        mock_reader_class.assert_called_once()
        mock_splitter_class.assert_called_once()
        mock_index_class.assert_called_once()

    def test_close(self, config):
        """Test pipeline cleanup"""
        with patch("triple_persistence.ingestion.GraphDatabase") as mock_graph_db, patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            mock_driver = Mock()
            mock_graph_db.driver.return_value = mock_driver

            pipeline = TriplePersistencePipeline(config)
            pipeline.close()

            mock_driver.close.assert_called_once()

    def test_context_manager(self, config):
        """Test pipeline as context manager"""
        with patch("triple_persistence.ingestion.GraphDatabase") as mock_graph_db, patch(
            "triple_persistence.ingestion.OllamaEmbedding"
        ), patch("triple_persistence.ingestion.Neo4jVectorStore"):
            mock_driver = Mock()
            mock_graph_db.driver.return_value = mock_driver

            with TriplePersistencePipeline(config) as pipeline:
                assert pipeline is not None

            # Should have closed driver
            mock_driver.close.assert_called_once()
