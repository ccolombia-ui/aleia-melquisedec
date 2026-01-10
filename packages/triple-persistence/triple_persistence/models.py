"""Pydantic models for triple-persistence"""
from datetime import datetime
from typing import Any, Dict, List, Optional

# Provide a lightweight fallback for pydantic.BaseModel and Field when
# pydantic is not available (e.g., CI or Python versions without wheels).
try:
    from pydantic import BaseModel, Field
except Exception:
    from dataclasses import field as _dc_field

    def Field(*args, **kwargs):
        # Support default_factory and default keywords used in models
        if "default_factory" in kwargs:
            return _dc_field(default_factory=kwargs["default_factory"])
        if "default" in kwargs:
            return _dc_field(default=kwargs["default"])
        return _dc_field(default=None)

    class BaseModel:
        """Minimal BaseModel shim usable in tests and simple contexts."""

        def __init__(self, **data):
            for k, v in data.items():
                setattr(self, k, v)

        def model_dump(self):
            return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

        def dict(self):
            return self.model_dump()


class Document(BaseModel):
    """Document metadata"""

    id: str
    path: str
    title: str
    type: str  # "requirement", "atomic", "adr", etc.
    rostro: Optional[str] = None  # MELQUISEDEC, HYPATIA, etc.
    phase: Optional[str] = None  # "010-define", etc.
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    content_hash: str
    text: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Chunk(BaseModel):
    """Text chunk with embedding"""

    id: str
    document_id: str
    chunk_index: int
    text: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class IngestionConfig(BaseModel):
    """Configuration for ingestion pipeline"""

    project: str
    paths: List[str]
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    ollama_base_url: str = "http://localhost:11434"
    embedding_model: str = "nomic-embed-text"
    embed_dim: int = 768
    chunk_size: int = 512
    chunk_overlap: int = 50


class QueryRequest(BaseModel):
    """Query request"""

    query: str
    top_k: int = 10
    include_graph: bool = True
    filters: Optional[Dict[str, Any]] = None


class QueryResult(BaseModel):
    """Single query result"""

    document_id: str
    document_path: str
    similarity: float
    excerpt: str
    related_documents: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class QueryResponse(BaseModel):
    """Query response with results"""

    results: List[QueryResult]
    query_time_ms: float
    total_results: int
