# Neo4j GraphRAG Retrievers - Usage Guide

**Phase**: Phase 2 Sprint 1 - R2.1 COMPLETE
**Date**: 2026-01-09
**Author**: SALOMON (Architect)
**Addresses**: GAP-8 (retrievers not installed), GAP-9 (functional examples missing)

---

## Overview

This package provides 4 retriever implementations based on the `neo4j-graphrag-python` library (v1.12.0), optimized for MELQUISEDEC architecture.

**Research Evidence**:
- R1.3: [hybrid-query-patterns.md](../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/neo4j-operations/hybrid-query-patterns.md) (900 lines, benchmarks)
- R1.1: [genai-stack-analysis.md](../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/genai-stack-analysis.md) (dual storage problem)
- R1.5: [validation-checkpoint.md](../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/validation-checkpoint.md) (gap analysis)

**Architecture**:
- **Unified storage**: Neo4j HNSW index (not Redis)
- **Embedding model**: Ollama qwen2.5:latest (1536 dimensions)
- **Vector index**: `melquisedec_embeddings`
- **Fulltext index**: `document_fulltext`

---

## Installation

```bash
# Install neo4j-graphrag-python
pip install neo4j-graphrag

# Install LlamaIndex Ollama embedder (if not already installed)
pip install llama-index-embeddings-ollama

# Verify Ollama is running
curl http://localhost:11434/api/tags
```

---

## Quick Start

### 1. Setup Neo4j Indexes

```cypher
-- Create vector index for semantic search
CREATE VECTOR INDEX melquisedec_embeddings IF NOT EXISTS
FOR (n:DocumentChunk)
ON n.embedding
OPTIONS {
  indexConfig: {
    `vector.dimensions`: 1536,              -- Ollama qwen2.5:latest
    `vector.similarity_function`: 'cosine',
    `vector.quantization.enabled`: true
  }
};

-- Create fulltext index for lexical search (hybrid retrievers)
CREATE FULLTEXT INDEX document_fulltext IF NOT EXISTS
FOR (n:DocumentChunk)
ON EACH [n.text];

-- Verify indexes
SHOW INDEXES YIELD name, type, state
WHERE name IN ['melquisedec_embeddings', 'document_fulltext']
RETURN name, type, state;
```

### 2. Initialize Driver and Embedder

```python
from neo4j import GraphDatabase
from llama_index.embeddings.ollama import OllamaEmbedding

# Neo4j connection
NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "password")

driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)

# Ollama embedder (same model used for indexing)
embedder = OllamaEmbedding(
    model_name="qwen2.5:latest",
    base_url="http://localhost:11434",
)
```

---

## Retriever Types

### 1. VectorRetriever (Basic Semantic Search)

**Performance**: ~50ms per query (from R1.3)

**Use Case**: Pure semantic similarity search without graph context.

```python
from packages.daath_toolkit.retrievers import MelquisedecVectorRetriever

retriever = MelquisedecVectorRetriever(
    driver=driver,
    embedder=embedder,
)

# Simple search
results = retriever.search(
    query_text="How to integrate LlamaIndex with Neo4j?",
    top_k=5
)

for result in results:
    print(f"Score: {result.score:.3f}")
    print(f"Text: {result.content[:200]}...")
    print("---")
```

**With Filters** (metadata filtering):

```python
# Filter by source document
filters = {
    "source": {"$eq": "llamaindex-deep-dive.md"}
}

results = retriever.search(
    query_text="retriever patterns",
    top_k=3,
    filters=filters
)
```

---

### 2. HybridRetriever (Vector + Full-Text)

**Performance**: ~80-100ms per query (from R1.3)

**Use Case**: Queries with both semantic and lexical requirements (e.g., technical terms).

```python
from packages.daath_toolkit.retrievers import MelquisedecHybridRetriever

retriever = MelquisedecHybridRetriever(
    driver=driver,
    embedder=embedder,
)

# Hybrid search (combines vector similarity and BM25 full-text)
results = retriever.search(
    query_text="Neo4j HNSW parameters tuning",
    top_k=5
)

# "HNSW" matched lexically + "tuning parameters" matched semantically
```

**Internal Algorithm**:
1. Vector search: HNSW k-ANN on embeddings
2. Full-text search: BM25 on text content
3. Fusion: Reciprocal Rank Fusion (RRF)
4. Final score: `(vecScore + ftScore) / 2.0`

---

### 3. VectorCypherRetriever (Vector + Graph Context)

**Performance**: ~100-120ms per query (from R1.3)

**Use Case**: Semantic search + graph relationships (e.g., enrich chunks with document/spec metadata).

```python
from packages.daath_toolkit.retrievers import MelquisedecVectorCypherRetriever

# Custom Cypher query to add graph context
retrieval_query = """
MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
OPTIONAL MATCH (doc)-[:PART_OF_SPEC]->(spec:Spec)
OPTIONAL MATCH (doc)-[:BELONGS_TO]->(domain:Domain)
RETURN node.text AS text,
       doc.title AS documentTitle,
       spec.name AS specName,
       domain.name AS domainName,
       score
ORDER BY score DESC
"""

retriever = MelquisedecVectorCypherRetriever(
    driver=driver,
    embedder=embedder,
    retrieval_query=retrieval_query,
)

results = retriever.search(
    query_text="decision traceability patterns",
    top_k=3
)

for result in results:
    print(f"Document: {result.metadata['documentTitle']}")
    print(f"Spec: {result.metadata['specName']}")
    print(f"Domain: {result.metadata['domainName']}")
    print(f"Score: {result.score:.3f}")
    print("---")
```

**Standard MELQUISEDEC Query** (includes rostro, confidence, sequential context):

```python
from packages.daath_toolkit.retrievers import get_standard_melquisedec_retrieval_query

retrieval_query = get_standard_melquisedec_retrieval_query()

retriever = MelquisedecVectorCypherRetriever(
    driver=driver,
    embedder=embedder,
    retrieval_query=retrieval_query,
)

results = retriever.search("autopoiesis patterns", top_k=5)
```

---

### 4. HybridCypherRetriever (Complete Hybrid)

**Performance**: ~120-150ms per query (from R1.3)

**Use Case**: Most sophisticated retrieval - vector + full-text + graph + custom logic.

```python
from packages.daath_toolkit.retrievers import MelquisedecHybridCypherRetriever

# Filter SALOMON decisions with high confidence (Decision Traceability)
retrieval_query = """
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
"""

retriever = MelquisedecHybridCypherRetriever(
    driver=driver,
    embedder=embedder,
    retrieval_query=retrieval_query,
)

results = retriever.search(
    query_text="architecture decisions for RAG pipeline",
    top_k=5
)

for result in results:
    print(f"Decision: {result.metadata['title']}")
    print(f"Domain: {result.metadata['domain']}")
    print(f"Confidence: {result.metadata['confidence']:.2f}")
    print(f"Score: {result.score:.3f}")
    print("---")
```

---

## Factory Functions

### Decision Tracer Retriever (GAP-1 from R1.5)

Pre-configured retriever for decision traceability:

```python
from packages.daath_toolkit.retrievers import create_decision_tracer_retriever

# Retrieve SALOMON (architect) decisions with confidence > 0.85
retriever = create_decision_tracer_retriever(
    driver=driver,
    embedder=embedder,
    rostro="SALOMON",
    min_confidence=0.85,
    domain="architecture"  # Optional: filter by domain
)

results = retriever.search(
    query_text="RAG pipeline design decisions",
    top_k=5
)
```

**Supported Rostros**:
- `SALOMON`: Architect decisions (strategic, high-level)
- `HYPATIA`: Researcher insights (state-of-art, comparative analysis)
- `MELQUISEDEC`: Synthesis decisions (integration, orchestration)
- `MORPHEUS`: Deep analysis (technical deep-dives)
- `ALMA`: User-centric decisions (UX, simplicity)

---

## Advanced Patterns

### Graph-Constrained Vector Search

Limit search to specific subgraph (e.g., chunks within specs related to an issue):

```python
retrieval_query = """
// 1. Define scope via graph traversal
MATCH (issue:Issue {id: $issue_id})<-[:HAS_ISSUE]-(spec:Spec)
MATCH (spec)-[:CONTAINS_DOCUMENT]->(doc:Document)
MATCH (doc)-[:CONTAINS_CHUNK]->(node:DocumentChunk)

// 2. Vector search constrained to scope
WITH COLLECT(node) AS candidateChunks
CALL db.index.vector.queryNodes('melquisedec_embeddings', 10, $query_vector)
YIELD node, score
WHERE node IN candidateChunks

RETURN node.text AS text,
       doc.title AS documentTitle,
       spec.name AS specName,
       score
ORDER BY score DESC
"""

retriever = MelquisedecVectorCypherRetriever(
    driver=driver,
    embedder=embedder,
    retrieval_query=retrieval_query,
)

results = retriever.search(
    query_text="implementation details for issue",
    top_k=5,
    query_params={"issue_id": "ISSUE-123"}
)
```

### Sequential Context (Previous/Next Chunks)

```python
retrieval_query = """
MATCH (node)<-[:CONTAINS_CHUNK]-(doc:Document)
OPTIONAL MATCH (node)-[:NEXT_CHUNK]->(next:DocumentChunk)
OPTIONAL MATCH (prev:DocumentChunk)-[:NEXT_CHUNK]->(node)

RETURN node.text AS text,
       prev.text AS previousContext,
       next.text AS nextContext,
       doc.title AS documentTitle,
       score
ORDER BY score DESC
"""

retriever = MelquisedecVectorCypherRetriever(
    driver=driver,
    embedder=embedder,
    retrieval_query=retrieval_query,
)

results = retriever.search("specific implementation detail", top_k=3)

for result in results:
    print("Previous:", result.metadata['previousContext'][:100])
    print("Current:", result.content[:100])
    print("Next:", result.metadata['nextContext'][:100])
```

---

## Performance Benchmarks

From R1.3 research findings (measured on MELQUISEDEC corpus):

| Retriever | Latency | Use Case | Trade-off |
|-----------|---------|----------|-----------|
| VectorRetriever | **50ms** | Fast semantic search | No graph context |
| HybridRetriever | **80-100ms** | Semantic + lexical | +60% latency, +20% recall |
| VectorCypherRetriever | **100-120ms** | Semantic + graph | +100% latency, +graph relationships |
| HybridCypherRetriever | **120-150ms** | Complete hybrid | +140% latency, best context |

**Comparison to Dual Storage** (from R1.1):
- genai-stack (LangChain + Redis + Neo4j): **280-580ms**
- Neo4j unified (LlamaIndex + Neo4j): **50-150ms**
- **Improvement**: 2-5x faster ✅

---

## Testing

Run integration tests:

```bash
# Ensure Neo4j running on localhost:7687
# Ensure Ollama running on localhost:11434

# Run all tests
pytest tests/integration/test_neo4j_graphrag_retrievers.py -v

# Run specific test class
pytest tests/integration/test_neo4j_graphrag_retrievers.py::TestMelquisedecVectorRetriever -v

# Run performance benchmarks
pytest tests/integration/test_neo4j_graphrag_retrievers.py::TestPerformanceBenchmarks -v
```

**Setup Test Data** (first time):

```python
from tests.integration.test_neo4j_graphrag_retrievers import setup_test_data

setup_test_data(
    neo4j_uri="bolt://localhost:7687",
    auth=("neo4j", "password")
)
```

---

## Troubleshooting

### Error: "Index 'melquisedec_embeddings' not found"

Create vector index:

```cypher
CREATE VECTOR INDEX melquisedec_embeddings IF NOT EXISTS
FOR (n:DocumentChunk)
ON n.embedding
OPTIONS {
  indexConfig: {
    `vector.dimensions`: 1536,
    `vector.similarity_function`: 'cosine',
    `vector.quantization.enabled`: true
  }
};
```

### Error: "Index 'document_fulltext' not found" (HybridRetrievers only)

Create fulltext index:

```cypher
CREATE FULLTEXT INDEX document_fulltext IF NOT EXISTS
FOR (n:DocumentChunk)
ON EACH [n.text];
```

### Error: "Ollama connection refused"

Start Ollama:

```bash
ollama serve

# In another terminal, verify model exists
ollama list | grep qwen2.5

# If not installed
ollama pull qwen2.5:latest
```

### Slow Query Performance (>200ms)

Check:
1. **HNSW parameters**: Increase `m` or `ef_construction` (see R1.3 Section 2.2)
2. **Graph depth**: Limit Cypher traversal to <3 hops
3. **Candidate nodes**: Use pre-filtering to reduce search space

```cypher
-- Profile query to identify bottleneck
PROFILE [your cypher query]
```

---

## Migration from genai-stack (Dual Storage)

If migrating from genai-stack (LangChain + Redis + Neo4j):

**Old Architecture** (R1.1):
```
Query → LangChain → Redis (vector) → Neo4j (graph) → Merge
Latency: 280-580ms
```

**New Architecture** (R1.3):
```
Query → LlamaIndex → Neo4j HNSW (vector + graph unified)
Latency: 50-150ms (2-5x faster)
```

**Migration Steps**:
1. Create `melquisedec_embeddings` HNSW index in Neo4j
2. Re-embed documents with `OllamaEmbedding(model_name="qwen2.5:latest")`
3. Store embeddings in Neo4j: `DocumentChunk.embedding` property
4. Replace LangChain retrievers with DAATH retrievers
5. Remove Redis dependency

**Evidence**: R1.1 Section 4 (dual storage problem), R1.3 Section 5 (unified solution).

---

## Next Steps (Phase 2 Sprint 1)

- ✅ R2.1: Neo4j GraphRAG Retrievers COMPLETE
- ⏭️ R2.2: DecisionTracerRetriever Custom (inherit VectorCypherRetriever)
- ⏭️ R2.3: Benchmarking Suite (validate R1.3 performance claims)

---

## References

- R1.3: [Hybrid Query Patterns](../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/neo4j-operations/hybrid-query-patterns.md) (900 lines)
- R1.1: [genai-stack Analysis](../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/genai-stack-analysis.md)
- R1.5: [Validation Checkpoint](../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/validation-checkpoint.md)
- Neo4j Docs: [Vector Index](https://neo4j.com/docs/cypher-manual/current/indexes-for-vector-search/)
- neo4j-graphrag-python: [GitHub](https://github.com/neo4j/neo4j-graphrag-python)
