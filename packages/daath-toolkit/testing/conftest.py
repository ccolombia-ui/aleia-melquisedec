"""
Pytest configuration and shared fixtures for daath-toolkit tests

Provides:
- Temporary research directories with valid/invalid structures
- Mock Pinecone clients
- Mock OpenAI clients
- Sample PROPOSITO.md files
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from unittest.mock import Mock, MagicMock
from datetime import datetime


@pytest.fixture
def temp_research_dir():
    """Creates a temporary research directory for testing"""
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    # Cleanup
    if temp_dir.exists():
        shutil.rmtree(temp_dir)


@pytest.fixture
def valid_proposito_content():
    """Returns valid PROPOSITO.md content"""
    return """---
id: DD-001-semantic-search
version: 1.0.0
created: 2024-01-15T10:00:00Z
status: active
purpose: |
  Investigar técnicas de búsqueda semántica
  para mejorar recuperación de información
initiated_by: HYPATIA
tags: [semantic-search, embeddings, rag]
---

# Propósito de la Investigación

Este documento describe el propósito y alcance de DD-001.

## Objetivos

1. Identificar mejores prácticas de semantic search
2. Evaluar modelos de embeddings
3. Diseñar arquitectura RAG
"""


@pytest.fixture
def invalid_proposito_content():
    """Returns PROPOSITO.md with missing fields"""
    return """---
id: DD-001-incomplete
status: active
---

# Missing required fields
"""


@pytest.fixture
def proposito_without_yaml():
    """Returns PROPOSITO.md without YAML frontmatter"""
    return """# Investigación sin Metadata

Este documento no tiene frontmatter YAML.
"""


@pytest.fixture
def valid_research_structure(temp_research_dir, valid_proposito_content):
    """Creates a complete valid research structure"""
    research_path = temp_research_dir / "DD-001-semantic-search"
    research_path.mkdir()

    # PROPOSITO.md
    (research_path / "PROPOSITO.md").write_text(valid_proposito_content, encoding='utf-8')

    # Valid folders with content
    folders = ['0-inbox', '1-literature', '2-atomic', '3-workbook', '4-dataset', '5-outputs', '_daath']
    for folder in folders:
        folder_path = research_path / folder
        folder_path.mkdir()
        # Add dummy file to make folder non-empty
        (folder_path / "README.md").write_text(f"# {folder}", encoding='utf-8')

    return research_path


@pytest.fixture
def invalid_research_structure(temp_research_dir):
    """Creates an invalid research structure (missing PROPOSITO.md)"""
    research_path = temp_research_dir / "DD-002-invalid"
    research_path.mkdir()

    # Create some random folders
    (research_path / "random-folder").mkdir()
    (research_path / "another-folder").mkdir()

    return research_path


@pytest.fixture
def mock_pinecone_client():
    """Mock Pinecone client"""
    mock_pc = Mock()

    # Mock list_indexes
    mock_indexes = Mock()
    mock_indexes.names.return_value = []
    mock_pc.list_indexes.return_value = mock_indexes

    # Mock create_index
    mock_pc.create_index.return_value = None

    # Mock Index
    mock_index = MagicMock()
    mock_index.upsert.return_value = {"upserted_count": 1}
    mock_index.query.return_value = {
        "matches": [
            {
                "id": "test-id-1",
                "score": 0.95,
                "metadata": {"artifact_type": "concept"}
            }
        ]
    }
    mock_index.delete.return_value = None
    mock_index.describe_index_stats.return_value = {
        "namespaces": {
            "DD-001.global": {"vector_count": 10}
        },
        "total_vector_count": 10
    }

    mock_pc.Index.return_value = mock_index

    return mock_pc


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client"""
    mock_client = Mock()

    # Mock embeddings.create
    mock_embedding_response = Mock()
    mock_embedding_response.data = [
        Mock(embedding=[0.1] * 1536)  # Embedding de 1536 dimensiones
    ]
    mock_client.embeddings.create.return_value = mock_embedding_response

    return mock_client


@pytest.fixture
def sample_chatlog_metadata():
    """Sample metadata for chatlog"""
    return {
        "instance_id": "DD-001-I001",
        "domain_id": "DD-001",
        "started_at": "2024-01-15T10:00:00Z",
        "status": "success",
        "prompts_used": {
            "HYPATIA": "v1.0.0",
            "SALOMON": "v1.0.0"
        },
        "checkpoints": [
            {
                "rostro": "HYPATIA",
                "name": "citations-filtered",
                "passed": True,
                "timestamp": "2024-01-15T10:15:00Z"
            }
        ],
        "potential_lessons": []
    }


@pytest.fixture
def temp_output_dir(temp_research_dir):
    """Creates a temporary output directory for chatlog testing"""
    output_path = temp_research_dir / "5-outputs" / "DD-001-semantic-search"
    output_path.mkdir(parents=True)
    return output_path
