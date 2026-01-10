# MVP: Triple-Persistence System (MD + Graph + Vector)

> **Version:** 0.1.0 MVP
> **Status:** Design
> **Target App:** research-autopoietic-template
> **Framework:** LlamaIndex + Neo4j 5.15+ + Ollama

---

## 1. Executive Summary

**Objetivo:** Sistema minimal para persistir conocimiento de investigación en 3 capas simultáneas:
1. **Markdown** (files): Source of truth, versionable, human-readable
2. **Graph** (Neo4j): Relationships, metadata, provenance
3. **Vector** (Neo4j HNSW): Semantic search, similarity, RAG

**Casos de uso inmediatos:**
- Ingestar documents de research-autopoietic-template (010-define/, 020-conceive/, etc.)
- Consultar "¿Qué atomics hablan de templates autopoiéticos?"
- Navegar grafo: `(Document)-[:REFERENCES]->(Atomic)-[:INFLUENCES]->(Decision)`

---

## 2. Arquitectura MVP

### 2.1 Stack Tecnológico

```yaml
Backend:
  - Python 3.11+
  - LlamaIndex 0.14.6 (Framework RAG)
  - Neo4j Python Driver 5.15+
  - llama-index-vector-stores-neo4jvector

LLM/Embeddings:
  - Ollama (local)
  - Model: qwen2.5:latest
  - Embeddings: nomic-embed-text (768 dim)

Database:
  - Neo4j 5.26 (Docker)
  - HNSW Vector Index
  - Graph + Vector unified storage

Infrastructure:
  - Docker Compose
  - Volume mounts: ./data/neo4j, ./data/markdown
```

### 2.2 Flujo de Datos

```
┌─────────────────┐
│ Markdown Files  │ (Source of Truth)
│ .md, .yaml, etc │
└────────┬────────┘
         │ 1. Scan & Parse
         ↓
┌─────────────────┐
│ LlamaIndex      │
│ SimpleDirectory │
│ Reader          │
└────────┬────────┘
         │ 2. Chunk (Semantic)
         ↓
┌─────────────────┐
│ Ollama Embedder │
│ nomic-embed-text│
│ (768 dimensions)│
└────────┬────────┘
         │ 3. Generate Embeddings
         ├───────────────┬──────────────┐
         ↓               ↓              ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Neo4j Graph  │  │ Neo4j Vector │  │ Markdown Copy│
│ (Nodes+Rels) │  │ (HNSW Index) │  │ (.melquisedec│
└──────────────┘  └──────────────┘  └──────────────┘
    Metadata         Semantic           Backup
    Provenance       Search             Versioning
```

### 2.3 Modelo de Datos (Neo4j)

```cypher
// Node Types
(:Document {
  id: string,           // Unique ID
  path: string,         // Relative path from project root
  title: string,
  type: string,         // "requirement", "atomic", "adr", etc.
  rostro: string,       // MELQUISEDEC, HYPATIA, etc.
  phase: string,        // "010-define", "020-conceive", etc.
  created_at: datetime,
  updated_at: datetime,
  content_hash: string, // SHA256 for change detection
  text: string          // Full text content (for BM25)
})

(:Chunk {
  id: string,
  document_id: string,
  chunk_index: int,
  text: string,         // Chunk content
  embedding: vector,    // 768-dim float array
  metadata: json        // Additional context
})

// Relationship Types
(:Document)-[:HAS_CHUNK]->(:Chunk)
(:Document)-[:REFERENCES]->(:Document)
(:Document)-[:TAGGED_WITH]->(:Tag)
(:Document)-[:BELONGS_TO]->(:Phase)
(:Document)-[:CREATED_BY]->(:Rostro)
```

---

## 3. MVP Components

### 3.1 Ingestion Pipeline

**File:** `packages/triple-persistence/ingestion.py`

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser

class TriplePersistencePipeline:
    def __init__(self, neo4j_uri, markdown_root):
        self.neo4j_uri = neo4j_uri
        self.markdown_root = markdown_root

        # Setup Ollama embeddings
        self.embedder = OllamaEmbedding(
            model_name="nomic-embed-text",
            base_url="http://localhost:11434"
        )

        # Setup Neo4j vector store
        self.vector_store = Neo4jVectorStore(
            username="neo4j",
            password="password",
            url=neo4j_uri,
            embed_dim=768,
            index_name="triple_persistence_embeddings",
            hybrid_search=True  # Enable BM25 + Vector
        )

    def ingest_directory(self, directory_path):
        """
        Ingest all markdown files from directory into triple-persistence.
        """
        # 1. Read markdown files
        documents = SimpleDirectoryReader(
            directory_path,
            file_extractor={".md": self._markdown_extractor}
        ).load_data()

        # 2. Semantic chunking
        splitter = SemanticSplitterNodeParser(
            embed_model=self.embedder,
            buffer_size=1  # Adjacent chunk context
        )
        nodes = splitter.get_nodes_from_documents(documents)

        # 3. Store in Neo4j (Graph + Vector)
        index = VectorStoreIndex(
            nodes,
            vector_store=self.vector_store,
            embed_model=self.embedder
        )

        # 4. Create graph relationships
        self._create_relationships(nodes)

        return index

    def _markdown_extractor(self, file_path):
        # Extract metadata from frontmatter
        pass

    def _create_relationships(self, nodes):
        # Create :REFERENCES, :TAGGED_WITH relationships
        pass
```

### 3.2 Retriever Híbrido

**File:** `packages/triple-persistence/retriever.py`

```python
class HybridRetriever:
    def __init__(self, index, neo4j_driver):
        self.index = index
        self.driver = neo4j_driver

    def query(self, query_text, top_k=10, include_graph=True):
        """
        Hybrid query: Vector similarity + Graph traversal
        """
        # 1. Vector search
        vector_results = self.index.as_query_engine().query(query_text)

        # 2. Graph enrichment (if enabled)
        if include_graph:
            enriched = self._enrich_with_graph(vector_results)
            return enriched

        return vector_results

    def _enrich_with_graph(self, results):
        # Add related documents via :REFERENCES
        # Add metadata via :TAGGED_WITH, :BELONGS_TO
        pass
```

### 3.3 Docker Compose Stack

**File:** `docker-compose.triple-persistence.yml`

```yaml
version: '3.8'

services:
  neo4j:
    image: neo4j:5.26
    ports:
      - "7474:7474"  # Browser
      - "7687:7687"  # Bolt
    environment:
      - NEO4J_AUTH=neo4j/password
      - NEO4J_PLUGINS=["apoc"]
      - NEO4J_dbms_memory_pagecache_size=1G
      - NEO4J_dbms_memory_heap_max__size=2G
    volumes:
      - ./data/neo4j:/data
    healthcheck:
      test: ["CMD", "cypher-shell", "-u", "neo4j", "-p", "password", "RETURN 1"]
      interval: 10s
      timeout: 5s
      retries: 5

  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ./data/ollama:/root/.ollama
    command: serve

  # Pull models on startup
  ollama-setup:
    image: ollama/ollama:latest
    depends_on:
      - ollama
    volumes:
      - ./data/ollama:/root/.ollama
    entrypoint: ["/bin/sh", "-c"]
    command:
      - |
        ollama pull qwen2.5:latest
        ollama pull nomic-embed-text
    restart: "no"

  # Triple Persistence Service
  triple-persistence:
    build:
      context: ./packages/triple-persistence
      dockerfile: Dockerfile
    depends_on:
      neo4j:
        condition: service_healthy
      ollama-setup:
        condition: service_completed_successfully
    environment:
      - NEO4J_URI=bolt://neo4j:7687
      - NEO4J_USER=neo4j
      - NEO4J_PASSWORD=password
      - OLLAMA_BASE_URL=http://ollama:11434
      - MARKDOWN_ROOT=/workspace/apps/research-autopoietic-template
    volumes:
      - ./apps:/workspace/apps
      - ./packages/triple-persistence:/app
    ports:
      - "8000:8000"  # FastAPI service
```

---

## 4. MVP Workflows

### 4.1 Workflow 1: Initial Ingestion

```bash
# 1. Start infrastructure
docker-compose -f docker-compose.triple-persistence.yml up -d

# 2. Ingest research-autopoietic-template
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "project": "research-autopoietic-template",
    "paths": [
      "010-define/",
      "020-conceive/",
      "030-design/"
    ]
  }'

# Expected output:
# {
#   "status": "success",
#   "documents_processed": 45,
#   "chunks_created": 523,
#   "graph_nodes": 45,
#   "graph_relationships": 89,
#   "processing_time": "2.3s"
# }
```

### 4.2 Workflow 2: Semantic Query

```bash
# Query: "¿Qué atomics hablan de templates autopoiéticos?"
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "templates autopoiéticos con feedback empírico",
    "top_k": 5,
    "include_graph": true
  }'

# Response:
# {
#   "results": [
#     {
#       "document": "020-conceive/02-atomics/atomic-005-template-feedback.md",
#       "similarity": 0.89,
#       "excerpt": "Los templates autopoiéticos evolucionan mediante...",
#       "related_documents": [
#         "010-define/requirements.md",
#         "030-design/adrs/ADR-001-autopoietic-design.md"
#       ]
#     }
#   ]
# }
```

### 4.3 Workflow 3: Graph Navigation

```bash
# Cypher query via Neo4j Browser (http://localhost:7474)
MATCH (d:Document {type: "atomic"})-[r:REFERENCES]->(ref:Document)
WHERE d.text CONTAINS "autopoietic"
RETURN d.title, collect(ref.title) AS references
```

---

## 5. Success Criteria (MVP)

| Criterio | Target | Medición |
|----------|--------|----------|
| **Ingestion Speed** | < 5 min para 100 docs | Time to ingest research-autopoietic-template |
| **Query Latency** | < 200ms (p95) | Vector + Graph query combined |
| **Recall** | > 80% @ top-10 | Manual evaluation con 20 queries test |
| **Graph Relationships** | > 50 created | Count of :REFERENCES, :TAGGED_WITH |
| **Storage** | < 500MB para 100 docs | Neo4j data folder size |
| **Markdown Backup** | 100% sync | All docs copied to .melquisedec/domain/ |

---

## 6. Non-Goals (Out of Scope for MVP)

❌ **NO incluir en MVP:**
- UI web (solo API REST)
- Authentication/Authorization
- Multi-user support
- Real-time sync (solo batch ingestion)
- Advanced graph algorithms (PageRank, Community Detection)
- Monitoring/Observability
- Production deployment (solo local Docker)
- Fine-tuning embeddings model

---

## 7. Next Steps

1. **Setup Python project** (`packages/triple-persistence/`)
2. **Implement ingestion pipeline** (SimpleDirectoryReader + Neo4jVectorStore)
3. **Create FastAPI service** (endpoints: /ingest, /query)
4. **Test with research-autopoietic-template**
5. **Document workflows** (README + examples)
6. **Validate success criteria** (benchmark tests)

---

## 8. Referencias

- **LlamaIndex Docs**: https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/
- **Neo4j Vector Index**: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- **Research Analysis**: `apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md`
- **Ollama Embeddings**: https://ollama.com/library/nomic-embed-text
