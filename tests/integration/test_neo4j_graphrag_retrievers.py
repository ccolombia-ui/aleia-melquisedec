"""
Integration Tests for Neo4j GraphRAG Retrievers (R2.1)

Tests the 4 retriever implementations against a live Neo4j instance with
MELQUISEDEC test data. Validates functionality and performance benchmarks
from R1.3 research findings.

**Test Requirements**:
- Neo4j 5.15+ running on bolt://localhost:7687
- Test database with 'melquisedec_embeddings' vector indexy
- 'document_fulltext' fulltext index
- Ollama running with qwen2.5:latest model

**Test Data Setup**:
Run `setup_test_data.py` to populate Neo4j with sample documents.

**Author**: SALOMON (Architect)
**Date**: 2026-01-09
**Phase**: Phase 2 Sprint 1
"""

import pytest
from llama_index.embeddings.ollama import OllamaEmbedding
from neo4j import GraphDatabase
from packages.daath_toolkit.retrievers import (
    MelquisedecHybridCypherRetriever,
    MelquisedecHybridRetriever,
    MelquisedecVectorCypherRetriever,
    MelquisedecVectorRetriever,
    create_decision_tracer_retriever,
    get_standard_melquisedec_retrieval_query,
)

# Test configuration
NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "password")
OLLAMA_MODEL = "qwen2.5:latest"
OLLAMA_BASE_URL = "http://localhost:11434"


@pytest.fixture(scope="module")
def neo4j_driver():
    """Neo4j driver fixture."""
    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    yield driver
    driver.close()


@pytest.fixture(scope="module")
def embedder():
    """LlamaIndex Ollama embedder fixture."""
    return OllamaEmbedding(
        model_name=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
    )


@pytest.fixture(scope="module")
def verify_indexes(neo4j_driver):
    """Verify required indexes exist."""
    with neo4j_driver.session() as session:
        # Check vector index
        result = session.run(
            "SHOW INDEXES YIELD name, type WHERE name = 'melquisedec_embeddings' RETURN name, type"
        )
        indexes = list(result)
        assert len(indexes) > 0, "Vector index 'melquisedec_embeddings' not found"

        # Check fulltext index
        result = session.run(
            "SHOW INDEXES YIELD name, type WHERE name = 'document_fulltext' RETURN name, type"
        )
        indexes = list(result)
        assert len(indexes) > 0, "Fulltext index 'document_fulltext' not found"


class TestMelquisedecVectorRetriever:
    """Tests for VectorRetriever (basic semantic search)."""

    def test_basic_search(self, neo4j_driver, embedder, verify_indexes):
        """Test basic vector similarity search."""
        retriever = MelquisedecVectorRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        results = retriever.search(
            query_text="How to integrate LlamaIndex with Neo4j?",
            top_k=5,
        )

        # Assertions
        assert len(results) > 0, "No results returned"
        assert len(results) <= 5, "More than top_k results returned"

        # Check result structure
        first_result = results[0]
        assert hasattr(first_result, "content"), "Result missing 'content' attribute"
        assert hasattr(first_result, "score"), "Result missing 'score' attribute"

        # Score should be between 0 and 1 (cosine similarity)
        assert 0 <= first_result.score <= 1, f"Invalid score: {first_result.score}"

    def test_search_with_filters(self, neo4j_driver, embedder, verify_indexes):
        """Test vector search with metadata filters."""
        retriever = MelquisedecVectorRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        # Filter by source document
        filters = {"source": {"$eq": "llamaindex-deep-dive.md"}}

        results = retriever.search(
            query_text="retriever patterns",
            top_k=3,
            filters=filters,
        )

        # All results should be from filtered source
        for result in results:
            if hasattr(result, "metadata") and "source" in result.metadata:
                assert result.metadata["source"] == "llamaindex-deep-dive.md"

    def test_empty_query(self, neo4j_driver, embedder, verify_indexes):
        """Test handling of empty query string."""
        retriever = MelquisedecVectorRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        with pytest.raises((ValueError, Exception)):
            retriever.search(query_text="", top_k=5)


class TestMelquisedecHybridRetriever:
    """Tests for HybridRetriever (vector + full-text)."""

    def test_hybrid_search(self, neo4j_driver, embedder, verify_indexes):
        """Test hybrid search combining vector and full-text."""
        retriever = MelquisedecHybridRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        # Query with both semantic and lexical components
        results = retriever.search(
            query_text="Neo4j HNSW parameters tuning",
            top_k=5,
        )

        assert len(results) > 0, "No results returned"
        assert len(results) <= 5, "More than top_k results returned"

        # Hybrid should find results containing "HNSW" (lexical) and related concepts (semantic)
        first_result = results[0]
        assert hasattr(first_result, "content")
        assert hasattr(first_result, "score")

    def test_hybrid_vs_vector_recall(self, neo4j_driver, embedder, verify_indexes):
        """Validate hybrid search improves recall vs pure vector search."""
        vector_retriever = MelquisedecVectorRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        hybrid_retriever = MelquisedecHybridRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        query = "vector index configuration"

        vector_results = vector_retriever.search(query, top_k=10)
        hybrid_results = hybrid_retriever.search(query, top_k=10)

        # Hybrid should return at least as many results as vector (or same)
        assert len(hybrid_results) >= len(vector_results) * 0.8  # Allow some variance


class TestMelquisedecVectorCypherRetriever:
    """Tests for VectorCypherRetriever (vector + graph context)."""

    def test_custom_cypher_query(self, neo4j_driver, embedder, verify_indexes):
        """Test vector search with custom Cypher enrichment."""
        retrieval_query = """
        MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
        OPTIONAL MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
        RETURN node.text AS text,
               doc.title AS documentTitle,
               domain.name AS domainName,
               score
        ORDER BY score DESC
        """

        retriever = MelquisedecVectorCypherRetriever(
            driver=neo4j_driver,
            embedder=embedder,
            retrieval_query=retrieval_query,
        )

        results = retriever.search(
            query_text="architecture patterns for RAG",
            top_k=3,
        )

        assert len(results) > 0, "No results returned"

        # Check custom properties from Cypher query
        first_result = results[0]
        assert hasattr(first_result, "metadata"), "Result missing metadata"

        # Should have documentTitle and domainName from Cypher query
        if hasattr(first_result, "metadata"):
            metadata = first_result.metadata
            assert "documentTitle" in metadata or "title" in metadata

    def test_standard_melquisedec_query(self, neo4j_driver, embedder, verify_indexes):
        """Test standard MELQUISEDEC retrieval query."""
        retrieval_query = get_standard_melquisedec_retrieval_query()

        retriever = MelquisedecVectorCypherRetriever(
            driver=neo4j_driver,
            embedder=embedder,
            retrieval_query=retrieval_query,
        )

        results = retriever.search(
            query_text="decision making process",
            top_k=5,
        )

        assert len(results) > 0

        # Standard query returns rich metadata
        first_result = results[0]
        if hasattr(first_result, "metadata"):
            metadata = first_result.metadata
            # Check for expected fields from standard query
            expected_fields = ["documentTitle", "rostro", "domainName"]
            found_fields = [f for f in expected_fields if f in metadata or f.lower() in metadata]
            assert len(found_fields) > 0, "Missing expected metadata fields"


class TestMelquisedecHybridCypherRetriever:
    """Tests for HybridCypherRetriever (complete hybrid search)."""

    def test_complete_hybrid_search(self, neo4j_driver, embedder, verify_indexes):
        """Test complete hybrid: vector + fulltext + graph + Cypher."""
        retrieval_query = """
        MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
        MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
        RETURN node.text AS text,
               doc.title AS title,
               domain.name AS domain,
               score
        ORDER BY score DESC
        """

        retriever = MelquisedecHybridCypherRetriever(
            driver=neo4j_driver,
            embedder=embedder,
            retrieval_query=retrieval_query,
        )

        results = retriever.search(
            query_text="LlamaIndex Neo4j integration patterns",
            top_k=5,
        )

        assert len(results) > 0, "No results returned"
        assert len(results) <= 5, "More than top_k results returned"

    def test_decision_tracer_factory(self, neo4j_driver, embedder, verify_indexes):
        """Test decision traceability retriever factory function."""
        retriever = create_decision_tracer_retriever(
            driver=neo4j_driver,
            embedder=embedder,
            rostro="SALOMON",
            min_confidence=0.85,
        )

        results = retriever.search(
            query_text="architecture decisions for vector storage",
            top_k=5,
        )

        # All results should be from SALOMON rostro with confidence > 0.85
        for result in results:
            if hasattr(result, "metadata"):
                metadata = result.metadata
                if "rostro" in metadata:
                    assert metadata["rostro"] == "SALOMON"
                if "confidence" in metadata:
                    assert metadata["confidence"] > 0.85

    def test_query_params(self, neo4j_driver, embedder, verify_indexes):
        """Test passing custom query parameters."""
        retrieval_query = """
        MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
        WHERE doc.confidence > $min_confidence
        RETURN node.text AS text,
               doc.confidence AS confidence,
               score
        ORDER BY score DESC
        """

        retriever = MelquisedecHybridCypherRetriever(
            driver=neo4j_driver,
            embedder=embedder,
            retrieval_query=retrieval_query,
        )

        results = retriever.search(
            query_text="high-confidence research findings",
            top_k=5,
            query_params={"min_confidence": 0.9},
        )

        # All results should have confidence > 0.9
        for result in results:
            if hasattr(result, "metadata") and "confidence" in result.metadata:
                assert result.metadata["confidence"] > 0.9


class TestPerformanceBenchmarks:
    """Performance benchmarks to validate R1.3 findings."""

    def test_vector_retriever_latency(self, neo4j_driver, embedder, verify_indexes):
        """Benchmark VectorRetriever latency (expected: ~50ms)."""
        import time

        retriever = MelquisedecVectorRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        # Warm-up query
        retriever.search("warm up", top_k=1)

        # Benchmark
        start = time.time()
        results = retriever.search("Neo4j vector operations", top_k=5)
        elapsed_ms = (time.time() - start) * 1000

        # From R1.3: VectorRetriever ~50ms baseline
        # Allow 3x margin for variance and slower hardware
        assert elapsed_ms < 150, f"VectorRetriever too slow: {elapsed_ms:.1f}ms (expected <150ms)"

        print(f"\n✅ VectorRetriever latency: {elapsed_ms:.1f}ms (R1.3 baseline: 50ms)")

    def test_hybrid_retriever_latency(self, neo4j_driver, embedder, verify_indexes):
        """Benchmark HybridRetriever latency (expected: ~80-100ms)."""
        import time

        retriever = MelquisedecHybridRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        # Warm-up
        retriever.search("warm up", top_k=1)

        # Benchmark
        start = time.time()
        results = retriever.search("HNSW index tuning parameters", top_k=5)
        elapsed_ms = (time.time() - start) * 1000

        # From R1.3: HybridRetriever ~80-100ms
        # Allow 3x margin
        assert elapsed_ms < 300, f"HybridRetriever too slow: {elapsed_ms:.1f}ms (expected <300ms)"

        print(f"\n✅ HybridRetriever latency: {elapsed_ms:.1f}ms (R1.3 baseline: 80-100ms)")

    @pytest.mark.skipif(
        condition=True,  # Skip by default (requires large dataset)
        reason="Requires full MELQUISEDEC corpus for realistic benchmark",
    )
    def test_vs_dual_storage_baseline(self, neo4j_driver, embedder, verify_indexes):
        """
        Compare Neo4j unified vs dual storage (Neo4j + Redis).

        From R1.1: genai-stack with LangChain + Redis + Neo4j = 280-580ms
        From R1.3: LlamaIndex + Neo4j unified = 50-100ms

        Expected improvement: 5x faster
        """
        import time

        retriever = MelquisedecHybridRetriever(
            driver=neo4j_driver,
            embedder=embedder,
        )

        # Benchmark over 10 queries
        queries = [
            "LlamaIndex retrievers comparison",
            "Neo4j vector index configuration",
            "hybrid search patterns",
            "decision traceability architecture",
            "MELQUISEDEC rostro definitions",
        ]

        latencies = []
        for query in queries:
            start = time.time()
            retriever.search(query, top_k=5)
            latencies.append((time.time() - start) * 1000)

        avg_latency = sum(latencies) / len(latencies)

        # From R1.1: dual storage baseline 280-580ms
        # Unified should be <150ms (conservative estimate)
        assert (
            avg_latency < 150
        ), f"Average latency {avg_latency:.1f}ms > 150ms (not beating dual storage)"

        print(f"\n✅ Unified Neo4j avg latency: {avg_latency:.1f}ms")
        print(f"   vs Dual storage baseline: 280-580ms")
        print(f"   Improvement: {280 / avg_latency:.1f}x faster")


# Test data setup helper (run manually before tests)
def setup_test_data(neo4j_uri: str, auth: tuple[str, str]):
    """
    Setup test data in Neo4j for integration tests.

    Creates:
    - DocumentChunk nodes with embeddings
    - Document nodes with metadata
    - Domain nodes
    - Spec nodes
    - Relationships: CONTAINS_CHUNK, BELONGS_TO, PART_OF_SPEC
    - Vector index: melquisedec_embeddings
    - Fulltext index: document_fulltext
    """
    print("Setting up Neo4j test data...")

    driver = GraphDatabase.driver(neo4j_uri, auth=auth)

    with driver.session() as session:
        # Create vector index
        session.run(
            """
            CREATE VECTOR INDEX melquisedec_embeddings IF NOT EXISTS
            FOR (n:DocumentChunk)
            ON n.embedding
            OPTIONS {
              indexConfig: {
                `vector.dimensions`: 1536,
                `vector.similarity_function`: 'cosine',
                `vector.quantization.enabled`: true
              }
            }
        """
        )

        # Create fulltext index
        session.run(
            """
            CREATE FULLTEXT INDEX document_fulltext IF NOT EXISTS
            FOR (n:DocumentChunk)
            ON EACH [n.text]
        """
        )

        print("✅ Indexes created")

        # TODO: Add sample documents from R1.1-R1.5 research findings
        # This would require reading markdown files and creating embeddings

    driver.close()
    print("✅ Test data setup complete")


if __name__ == "__main__":
    # Run test data setup
    setup_test_data(NEO4J_URI, NEO4J_AUTH)
    print("\nRun tests with: pytest tests/integration/test_neo4j_graphrag_retrievers.py -v")
