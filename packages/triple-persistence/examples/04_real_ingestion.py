"""
Ejemplo 4: Ingesta Real con research-autopoietic-template

Este ejemplo usa el pipeline completo (ingestion.py + retriever.py)
para ingestar documentos reales del proyecto research-autopoietic-template.

Requisitos:
1. Neo4j corriendo (docker-compose up neo4j)
2. Ollama corriendo con modelos descargados
3. Documentos en apps/research-autopoietic-template/
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from triple_persistence import (
    HybridRetriever,
    IngestionConfig,
    QueryRequest,
    TriplePersistencePipeline,
)


def main():
    print("=" * 70)
    print("🚀 Ejemplo 4: Ingesta Real - research-autopoietic-template")
    print("=" * 70)

    # Configuration
    config = IngestionConfig(
        project="research-autopoietic-template",
        paths=[
            str(
                Path(__file__).parent.parent.parent.parent
                / "apps"
                / "research-autopoietic-template"
                / "010-define"
            )
        ],
        neo4j_uri="bolt://localhost:7687",
        neo4j_user="neo4j",
        neo4j_password="password",
        ollama_base_url="http://localhost:11434",
        embedding_model="nomic-embed-text",
        embed_dim=768,
        chunk_size=512,
        chunk_overlap=50,
    )

    print(f"\n📋 Configuration:")
    print(f"   Project: {config.project}")
    print(f"   Path: {config.paths[0]}")
    print(f"   Neo4j: {config.neo4j_uri}")
    print(f"   Ollama: {config.ollama_base_url}")
    print(f"   Embedding Model: {config.embedding_model}")

    # Step 1: Ingestion
    print(f"\n{'=' * 70}")
    print("PASO 1: INGESTION PIPELINE")
    print("=" * 70)

    with TriplePersistencePipeline(config) as pipeline:
        # Ingest directory
        stats = pipeline.ingest_directory(config.paths[0])

        print(f"\n📊 Ingestion Stats:")
        print(f"   Documents: {stats['documents_processed']}")
        print(f"   Chunks: {stats['chunks_created']}")
        print(f"   Directory: {stats['directory']}")

        # Get the index for retrieval
        index = pipeline.vector_store.index

    # Step 2: Queries
    print(f"\n{'=' * 70}")
    print("PASO 2: HYBRID QUERIES")
    print("=" * 70)

    from neo4j import GraphDatabase

    driver = GraphDatabase.driver(config.neo4j_uri, auth=(config.neo4j_user, config.neo4j_password))

    retriever = HybridRetriever(index=index, neo4j_driver=driver, project=config.project)

    # Query 1: Semantic search
    queries = [
        "¿Qué son los templates autopoiéticos?",
        "Documentos sobre feedback empírico",
        "Atomics relacionados con investigación",
    ]

    for i, query_text in enumerate(queries, 1):
        print(f"\n{'─' * 70}")
        print(f"Query {i}: {query_text}")
        print("─" * 70)

        request = QueryRequest(query=query_text, top_k=3, include_graph=True)

        response = retriever.query(request)

        print(f"\n📊 Results: {response.total_results} documents")
        print(f"⏱️  Query time: {response.query_time_ms:.2f}ms")

        for j, result in enumerate(response.results, 1):
            print(f"\n   {j}. {result.document_path}")
            print(f"      Similarity: {result.similarity:.3f}")
            print(f"      Excerpt: {result.excerpt[:100]}...")
            if result.related_documents:
                print(f"      Related: {len(result.related_documents)} documents")

    # Step 3: Statistics
    print(f"\n{'=' * 70}")
    print("PASO 3: KNOWLEDGE BASE STATS")
    print("=" * 70)

    stats = retriever.get_stats()
    print(f"\n📊 Knowledge Base Statistics:")
    for key, value in stats.items():
        print(f"   {key.capitalize()}: {value}")

    driver.close()

    print(f"\n{'=' * 70}")
    print("✅ EJEMPLO COMPLETO")
    print("=" * 70)
    print(f"\n💡 Next steps:")
    print(f"   1. Open Neo4j Browser: http://localhost:7474")
    print(f"   2. Run query: MATCH (d:Document) RETURN d LIMIT 25")
    print(f"   3. Explore relationships: MATCH (d)-[r]-(n) RETURN d,r,n LIMIT 50")


if __name__ == "__main__":
    main()
