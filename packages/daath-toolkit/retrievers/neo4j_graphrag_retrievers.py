"""
Neo4j GraphRAG Retrievers Implementation (R2.1)

Wrappers around neo4j-graphrag-python (v1.12.0) retrievers with MELQUISEDEC-specific
configurations and patterns from R1.3 research findings.

**Research Evidence**:
- R1.3: hybrid-query-patterns.md (900 lines, 4 retriever patterns, benchmarks)
- VectorRetriever: 50ms baseline semantic search
- HybridRetriever: 80-100ms vector + BM25 full-text
- VectorCypherRetriever: 100-120ms vector + graph traversal
- HybridCypherRetriever: 120-150ms complete hybrid (vector + fulltext + graph)

**Architecture**:
- Unified storage: Neo4j HNSW index (not Redis)
- Embedding model: Ollama qwen2.5:latest (1536 dimensions)
- Index name: 'melquisedec_embeddings'
- Fulltext index: 'document_fulltext'

**Author**: SALOMON (Architect)
**Date**: 2026-01-09
**Phase**: Phase 2 Sprint 1 - Design & Architecture
**Addresses**: GAP-8 (retrievers not installed), GAP-9 (functional examples missing)
"""

from typing import Any, Optional

from neo4j import Driver
from neo4j_graphrag.retrievers import (
    HybridCypherRetriever,
    HybridRetriever,
    VectorCypherRetriever,
    VectorRetriever,
)

# Default MELQUISEDEC configuration (from R1.5 validation)
DEFAULT_INDEX_NAME = "melquisedec_embeddings"
DEFAULT_FULLTEXT_INDEX = "document_fulltext"
DEFAULT_EMBEDDING_DIMENSION = 1536  # Ollama qwen2.5:latest


class MelquisedecVectorRetriever:
    """
    Basic semantic search using Neo4j HNSW vector index.

    **Performance**: ~50ms per query (from R1.3 benchmarks)

    **Use Case**:
    - Pure semantic similarity search
    - No graph context needed
    - Fast retrieval for general queries

    **Example**:
        ```python
        from neo4j import GraphDatabase
        from llama_index.embeddings.ollama import OllamaEmbedding

        driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
        embedder = OllamaEmbedding(model_name="qwen2.5:latest")

        retriever = MelquisedecVectorRetriever(
            driver=driver,
            embedder=embedder
        )

        results = retriever.search(
            query_text="How to integrate LlamaIndex with Neo4j?",
            top_k=5
        )

        for result in results:
            print(f"Score: {result.score:.3f}")
            print(f"Text: {result.content[:200]}...")
        ```

    **Architecture Note**:
    This replaces genai-stack's dual-storage pattern (Neo4j + Redis) with
    unified storage in Neo4j. Latency improvement: 280-580ms → 50ms (5x faster).
    Evidence: R1.1 genai-stack-analysis.md
    """

    def __init__(
        self,
        driver: Driver,
        embedder: Any,
        index_name: str = DEFAULT_INDEX_NAME,
        return_properties: Optional[list[str]] = None,
    ):
        """
        Initialize VectorRetriever.

        Args:
            driver: Neo4j driver instance
            embedder: LlamaIndex embedder (e.g., OllamaEmbedding)
            index_name: Neo4j vector index name (default: 'melquisedec_embeddings')
            return_properties: Node properties to return (default: ['text', 'source', 'metadata'])
        """
        self.driver = driver
        self.embedder = embedder
        self.index_name = index_name

        if return_properties is None:
            return_properties = ["text", "source", "metadata"]

        self._retriever = VectorRetriever(
            driver=driver,
            index_name=index_name,
            embedder=embedder,
            return_properties=return_properties,
        )

    def search(
        self,
        query_text: str,
        top_k: int = 5,
        filters: Optional[dict[str, Any]] = None,
    ) -> list[Any]:
        """
        Perform semantic search.

        Args:
            query_text: Natural language query
            top_k: Number of results to return
            filters: Optional metadata filters (e.g., {"source": {"$eq": "spec.md"}})

        Returns:
            List of retrieval results with score and content
        """
        return self._retriever.search(
            query_text=query_text,
            top_k=top_k,
            filters=filters,
        )

    def get_search_results(
        self,
        query_vector: list[float],
        top_k: int = 5,
    ) -> list[Any]:
        """
        Search with pre-computed embedding vector.

        Args:
            query_vector: Embedding vector (1536 dimensions for qwen2.5)
            top_k: Number of results to return

        Returns:
            List of retrieval results
        """
        return self._retriever.get_search_results(
            query_vector=query_vector,
            top_k=top_k,
        )


class MelquisedecHybridRetriever:
    """
    Hybrid search combining vector similarity (HNSW) and full-text search (BM25).

    **Performance**: ~80-100ms per query (from R1.3 benchmarks)

    **Use Case**:
    - Queries with both semantic and lexical requirements
    - Technical terms or exact keywords important
    - Balanced precision/recall

    **Example**:
        ```python
        retriever = MelquisedecHybridRetriever(
            driver=driver,
            embedder=embedder
        )

        # Query combines semantic ("parameters tuning") and lexical ("HNSW")
        results = retriever.search(
            query_text="Neo4j HNSW parameters tuning",
            top_k=5
        )
        ```

    **Internal Algorithm**:
    - Vector search: CALL db.index.vector.queryNodes()
    - Full-text search: CALL db.index.fulltext.queryNodes()
    - Fusion: Reciprocal Rank Fusion (RRF)
    - Formula: finalScore = (vecScore + ftScore) / 2.0

    **Requirements**:
    - Vector index: 'melquisedec_embeddings' must exist
    - Fulltext index: 'document_fulltext' must exist

    To create fulltext index:
        ```cypher
        CREATE FULLTEXT INDEX document_fulltext IF NOT EXISTS
        FOR (n:DocumentChunk)
        ON EACH [n.text];
        ```
    """

    def __init__(
        self,
        driver: Driver,
        embedder: Any,
        vector_index_name: str = DEFAULT_INDEX_NAME,
        fulltext_index_name: str = DEFAULT_FULLTEXT_INDEX,
        return_properties: Optional[list[str]] = None,
    ):
        """
        Initialize HybridRetriever.

        Args:
            driver: Neo4j driver instance
            embedder: LlamaIndex embedder
            vector_index_name: Vector index name (default: 'melquisedec_embeddings')
            fulltext_index_name: Fulltext index name (default: 'document_fulltext')
            return_properties: Node properties to return
        """
        self.driver = driver
        self.embedder = embedder
        self.vector_index_name = vector_index_name
        self.fulltext_index_name = fulltext_index_name

        if return_properties is None:
            return_properties = ["text", "source", "metadata"]

        self._retriever = HybridRetriever(
            driver=driver,
            vector_index_name=vector_index_name,
            fulltext_index_name=fulltext_index_name,
            embedder=embedder,
            return_properties=return_properties,
        )

    def search(
        self,
        query_text: str,
        top_k: int = 5,
    ) -> list[Any]:
        """
        Perform hybrid search (vector + full-text).

        Args:
            query_text: Natural language query
            top_k: Number of results to return

        Returns:
            List of retrieval results ranked by RRF score
        """
        return self._retriever.search(
            query_text=query_text,
            top_k=top_k,
        )


class MelquisedecVectorCypherRetriever:
    """
    Vector search with custom Cypher query for graph traversal context.

    **Performance**: ~100-120ms per query (from R1.3 benchmarks)

    **Use Case**:
    - Semantic search + graph relationships
    - Need context from connected nodes (e.g., Document → Spec → Domain)
    - Custom business logic in retrieval

    **Example**:
        ```python
        # Custom Cypher to enrich chunks with document metadata
        retrieval_query = \"\"\"
        MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
        OPTIONAL MATCH (doc)-[:PART_OF_SPEC]->(spec:Spec)
        OPTIONAL MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
        RETURN node.text AS text,
               doc.title AS documentTitle,
               spec.name AS specName,
               domain.name AS domainName,
               score
        ORDER BY score DESC
        \"\"\"

        retriever = MelquisedecVectorCypherRetriever(
            driver=driver,
            embedder=embedder,
            retrieval_query=retrieval_query
        )

        results = retriever.search(
            query_text="decision traceability patterns",
            top_k=3
        )
        ```

    **Cypher Query Requirements**:
    - Variables available: `node` (matched chunk), `score` (similarity score)
    - Must RETURN at minimum: node content and score
    - Can traverse graph: MATCH, OPTIONAL MATCH, WITH, etc.
    - ORDER BY and LIMIT handled by retriever (don't include in query)

    **Advanced Pattern** (from R1.3):
    Graph-constrained vector search - limit search to specific subgraph:
        ```cypher
        // Scope: chunks within specs related to an issue
        MATCH (issue:Issue {id: $issue_id})<-[:HAS_ISSUE]-(spec:Spec)
        MATCH (spec)-[:CONTAINS_DOCUMENT]->(doc:Document)
        MATCH (doc)-[:CONTAINS_CHUNK]->(node:DocumentChunk)
        WHERE node IN $candidate_nodes  // Provided by vector search
        RETURN node.text AS text, score
        ```
    """

    def __init__(
        self,
        driver: Driver,
        embedder: Any,
        retrieval_query: str,
        index_name: str = DEFAULT_INDEX_NAME,
    ):
        """
        Initialize VectorCypherRetriever with custom Cypher query.

        Args:
            driver: Neo4j driver instance
            embedder: LlamaIndex embedder
            retrieval_query: Custom Cypher query for retrieval logic
            index_name: Vector index name (default: 'melquisedec_embeddings')
        """
        self.driver = driver
        self.embedder = embedder
        self.retrieval_query = retrieval_query
        self.index_name = index_name

        self._retriever = VectorCypherRetriever(
            driver=driver,
            index_name=index_name,
            retrieval_query=retrieval_query,
            embedder=embedder,
        )

    def search(
        self,
        query_text: str,
        top_k: int = 5,
        query_params: Optional[dict[str, Any]] = None,
    ) -> list[Any]:
        """
        Perform vector search with custom Cypher enrichment.

        Args:
            query_text: Natural language query
            top_k: Number of results to return
            query_params: Additional Cypher parameters (e.g., {"issue_id": "ISSUE-123"})

        Returns:
            List of retrieval results with custom properties from Cypher query
        """
        return self._retriever.search(
            query_text=query_text,
            top_k=top_k,
            query_params=query_params or {},
        )


class MelquisedecHybridCypherRetriever:
    """
    Complete hybrid search: vector + full-text + graph traversal + custom Cypher.

    **Performance**: ~120-150ms per query (from R1.3 benchmarks)

    **Use Case**:
    - Most sophisticated retrieval needs
    - Semantic + lexical + structural requirements
    - Complex business logic (e.g., confidence thresholds, rostro filtering)

    **Example** (Decision Traceability - from R1.5 GAP-1):
        ```python
        # Filter SALOMON (architect) decisions with high confidence
        retrieval_query = \"\"\"
        MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
        MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
        WHERE doc.rostro = 'SALOMON'
          AND doc.confidence > 0.85
        RETURN node.text AS text,
               doc.title AS title,
               domain.name AS domain,
               doc.confidence AS confidence,
               score
        ORDER BY score DESC, doc.confidence DESC
        \"\"\"

        retriever = MelquisedecHybridCypherRetriever(
            driver=driver,
            embedder=embedder,
            retrieval_query=retrieval_query
        )

        results = retriever.search(
            query_text="architecture decisions for RAG pipeline",
            top_k=5
        )

        for result in results:
            print(f"Decision: {result.metadata['title']}")
            print(f"Domain: {result.metadata['domain']}")
            print(f"Confidence: {result.metadata['confidence']}")
        ```

    **Best Practices** (from R1.3 Section 5):
    1. Use filters on indexed properties (rostro, confidence, domain)
    2. Avoid deep graph traversal (>3 hops) - latency increases
    3. LIMIT candidate nodes before vector search if possible
    4. Test query performance with PROFILE/EXPLAIN

    **Comparison to Alternatives**:
    - vs genai-stack (LangChain + Redis + Neo4j): 280-580ms → 120-150ms (2-4x faster)
    - vs LlamaIndex alone (no graph): Same speed but +graph relationships
    - Trade-off: 3x slower than VectorRetriever, but 10x more context
    """

    def __init__(
        self,
        driver: Driver,
        embedder: Any,
        retrieval_query: str,
        vector_index_name: str = DEFAULT_INDEX_NAME,
        fulltext_index_name: str = DEFAULT_FULLTEXT_INDEX,
    ):
        """
        Initialize HybridCypherRetriever with custom Cypher query.

        Args:
            driver: Neo4j driver instance
            embedder: LlamaIndex embedder
            retrieval_query: Custom Cypher query for retrieval logic
            vector_index_name: Vector index name
            fulltext_index_name: Fulltext index name
        """
        self.driver = driver
        self.embedder = embedder
        self.retrieval_query = retrieval_query
        self.vector_index_name = vector_index_name
        self.fulltext_index_name = fulltext_index_name

        self._retriever = HybridCypherRetriever(
            driver=driver,
            vector_index_name=vector_index_name,
            fulltext_index_name=fulltext_index_name,
            retrieval_query=retrieval_query,
            embedder=embedder,
        )

    def search(
        self,
        query_text: str,
        top_k: int = 5,
        query_params: Optional[dict[str, Any]] = None,
    ) -> list[Any]:
        """
        Perform complete hybrid search (vector + fulltext + graph + Cypher).

        Args:
            query_text: Natural language query
            top_k: Number of results to return
            query_params: Additional Cypher parameters

        Returns:
            List of retrieval results with custom properties from Cypher query
        """
        return self._retriever.search(
            query_text=query_text,
            top_k=top_k,
            query_params=query_params or {},
        )


# Utility function for creating standard MELQUISEDEC retrieval query
def get_standard_melquisedec_retrieval_query() -> str:
    """
    Standard Cypher retrieval query for MELQUISEDEC architecture.

    Returns enriched context:
    - Document metadata (title, rostro, confidence)
    - Spec information (name, version, status)
    - Domain classification
    - Sequential chunk context (previous/next chunks)

    Use with VectorCypherRetriever or HybridCypherRetriever.

    Returns:
        Cypher query string
    """
    return """
    MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
    OPTIONAL MATCH (doc)-[:PART_OF_SPEC]->(spec:Spec)
    OPTIONAL MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
    OPTIONAL MATCH (node)-[:NEXT_CHUNK]->(next:DocumentChunk)
    OPTIONAL MATCH (prev:DocumentChunk)-[:NEXT_CHUNK]->(node)

    RETURN node.text AS text,
           doc.title AS documentTitle,
           doc.rostro AS rostro,
           doc.confidence AS confidence,
           spec.name AS specName,
           spec.version AS specVersion,
           domain.name AS domainName,
           prev.text AS previousContext,
           next.text AS nextContext,
           score
    ORDER BY score DESC
    """


# Example: Quick setup function for common use case
def create_decision_tracer_retriever(
    driver: Driver,
    embedder: Any,
    rostro: str = "SALOMON",
    min_confidence: float = 0.85,
    domain: Optional[str] = None,
) -> MelquisedecHybridCypherRetriever:
    """
    Factory function for decision traceability retriever (addresses GAP-1 from R1.5).

    Filters decisions by:
    - Rostro (default: SALOMON - architect decisions)
    - Minimum confidence (default: 0.85 - high-quality only)
    - Optional domain filter

    Args:
        driver: Neo4j driver instance
        embedder: LlamaIndex embedder
        rostro: Rostro filter (SALOMON, HYPATIA, MELQUISEDEC, etc.)
        min_confidence: Minimum confidence threshold (0.0-1.0)
        domain: Optional domain name filter

    Returns:
        Configured HybridCypherRetriever for decision traceability

    Example:
        ```python
        retriever = create_decision_tracer_retriever(
            driver=driver,
            embedder=embedder,
            rostro="SALOMON",
            min_confidence=0.85,
            domain="architecture"
        )

        results = retriever.search("RAG pipeline design decisions", top_k=5)
        ```
    """
    domain_filter = f"AND domain.name = '{domain}'" if domain else ""

    retrieval_query = f"""
    MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
    MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
    WHERE doc.rostro = '{rostro}'
      AND doc.confidence > {min_confidence}
      {domain_filter}
    RETURN node.text AS text,
           doc.title AS title,
           domain.name AS domain,
           doc.confidence AS confidence,
           doc.created_date AS createdDate,
           score
    ORDER BY score DESC, doc.confidence DESC
    """

    return MelquisedecHybridCypherRetriever(
        driver=driver,
        embedder=embedder,
        retrieval_query=retrieval_query,
    )
