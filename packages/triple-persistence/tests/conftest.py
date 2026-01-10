"""Test configuration for pytest"""

import sys
from pathlib import Path

# Add package to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from unittest.mock import Mock

import pytest


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
