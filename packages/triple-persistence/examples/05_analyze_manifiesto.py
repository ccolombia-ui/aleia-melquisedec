#!/usr/bin/env python3
"""
Example: Analyze raw-manifiesto.md with Triple-Persistence System

This script demonstrates how to:
1. Ingest the raw manifesto document
2. Extract metadata (title, type, rostro, phase, tags, references)
3. Query for key concepts
4. Explore relationships in the knowledge graph
5. Generate analysis reports

Document: research-autopoietic-template/010-define/inputs/raw-manifiesto.md
"""

import sys
from pathlib import Path
from typing import Dict, List

# Add package to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from triple_persistence.ingestion import TriplePersistencePipeline
from triple_persistence.models import IngestionConfig, QueryRequest
from triple_persistence.retriever import HybridRetriever


def print_section(title: str):
    """Print formatted section header"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def print_metadata(metadata: Dict):
    """Print document metadata"""
    print("📄 Metadata Extraída:")
    print(f"   Title: {metadata.get('title', 'N/A')}")
    print(f"   Type: {metadata.get('type', 'N/A')}")
    print(f"   Rostro: {metadata.get('rostro', 'N/A')}")
    print(f"   Phase: {metadata.get('phase', 'N/A')}")
    print(f"   Tags: {', '.join(metadata.get('tags', []))[:100]}")
    print(f"   References: {len(metadata.get('references', []))} wikilinks")


def execute_analysis_queries(retriever: HybridRetriever):
    """Execute queries to analyze the manifesto content"""

    queries = [
        {
            "title": "🔍 Principios del Manifiesto MELQUISEDEC",
            "query": "¿Cuáles son los principios P1-P10 del Manifiesto MELQUISEDEC?",
            "explanation": "Busca los 10 principios fundamentales del sistema",
        },
        {
            "title": "🏗️ Arquitectura PRAXIS-RBM",
            "query": "¿Cómo funciona la arquitectura PRAXIS-RBM?",
            "explanation": "Explora la estructura del meta-framework autopoiético",
        },
        {
            "title": "🔄 Templates Autopoiéticos",
            "query": "¿Qué son los templates autopoiéticos y cómo se implementan?",
            "explanation": "Entiende el concepto de autopoiesis aplicado a templates",
        },
        {
            "title": "📐 Estructura de Fases (010-050)",
            "query": "¿Cómo se organizan las fases 010-define hasta 050-conclude?",
            "explanation": "Mapea la estructura de carpetas del template",
        },
        {
            "title": "🌐 Relación con spec-workflow-mcp",
            "query": "¿Cómo se relaciona el manifiesto con spec-workflow-mcp?",
            "explanation": "Conecta conceptos con la herramienta de gestión",
        },
    ]

    for i, q in enumerate(queries, 1):
        print_section(f"{i}. {q['title']}")
        print(f"💭 Query: {q['query']}")
        print(f"📝 Objetivo: {q['explanation']}\n")

        # Execute query
        request = QueryRequest(
            query=q["query"], top_k=3, include_graph=True, filters={"type": "document"}
        )

        response = retriever.query(request)

        # Display results
        print(f"📊 Resultados: {response.total_results} documentos encontrados")
        print(f"⏱️  Tiempo: {response.query_time_ms:.2f}ms\n")

        for j, result in enumerate(response.results, 1):
            print(f"   {j}. {result.document_path}")
            print(f"      Similitud: {result.similarity:.2%}")
            print(f"      Contexto: {result.excerpt[:150]}...")
            if result.related_documents:
                print(f"      Relacionado con: {len(result.related_documents)} docs")
            print()

        if i < len(queries):
            input("   Presiona ENTER para continuar...")


def generate_cypher_queries():
    """Generate useful Cypher queries for Neo4j Browser exploration"""

    print_section("💡 Queries Cypher para Neo4j Browser")

    queries = [
        {
            "title": "Ver documento del manifiesto",
            "query": """
MATCH (d:Document {project: 'research-autopoietic-template'})
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN d.id, d.title, d.type, d.path
            """.strip(),
        },
        {
            "title": "Ver todos los chunks del manifiesto",
            "query": """
MATCH (d:Document)-[:HAS_CHUNK]->(c:Chunk)
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN d.title, c.text, c.embedding IS NOT NULL as has_embedding
LIMIT 10
            """.strip(),
        },
        {
            "title": "Explorar referencias ([[wikilinks]])",
            "query": """
MATCH (d:Document)-[r:REFERENCES]->(target:Document)
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN d.title as from_doc, target.title as to_doc, type(r) as relationship
            """.strip(),
        },
        {
            "title": "Ver tags más usados",
            "query": """
MATCH (d:Document)-[:TAGGED_WITH]->(t:Tag)
WHERE d.project = 'research-autopoietic-template'
RETURN t.name, count(*) as usage
ORDER BY usage DESC
LIMIT 10
            """.strip(),
        },
        {
            "title": "Grafo de conocimiento completo",
            "query": """
MATCH path = (d:Document)-[:REFERENCES*1..2]-(related:Document)
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN path
LIMIT 50
            """.strip(),
        },
        {
            "title": "Buscar por concepto clave",
            "query": """
MATCH (d:Document)
WHERE d.project = 'research-autopoietic-template'
  AND (d.text CONTAINS 'MELQUISEDEC' OR d.text CONTAINS 'autopoiesis')
RETURN d.title, d.path, d.rostro
LIMIT 10
            """.strip(),
        },
    ]

    for i, q in enumerate(queries, 1):
        print(f"{i}. {q['title']}")
        print(f"   {'-' * 55}")
        print(f"{q['query']}")
        print()

    print("💡 Cómo usar:")
    print("   1. Abrir Neo4j Browser: http://localhost:7474")
    print("   2. Copiar y pegar cualquier query de arriba")
    print("   3. Click en 'Run' (▶) o Ctrl+Enter")
    print("   4. Explorar resultados en forma de tabla o grafo")


def export_knowledge_base_stats(retriever: HybridRetriever):
    """Export knowledge base statistics"""

    print_section("📊 Estadísticas de la Base de Conocimiento")

    stats = retriever.get_stats()

    print("📈 Totales:")
    print(f"   Documentos: {stats.get('total_documents', 0)}")
    print(f"   Chunks: {stats.get('total_chunks', 0)}")
    print(f"   Tags: {stats.get('total_tags', 0)}")
    print(f"   Referencias: {stats.get('total_references', 0)}")

    if "by_type" in stats:
        print("\n📑 Por Tipo:")
        for doc_type, count in stats["by_type"].items():
            print(f"   {doc_type}: {count}")

    if "by_rostro" in stats:
        print("\n👤 Por Rostro:")
        for rostro, count in stats["by_rostro"].items():
            print(f"   {rostro}: {count}")

    if "by_phase" in stats:
        print("\n🔄 Por Fase:")
        for phase, count in stats["by_phase"].items():
            print(f"   {phase}: {count}")

    if "top_tags" in stats:
        print("\n🏷️  Tags Más Usados:")
        for tag, count in stats["top_tags"][:10]:
            print(f"   #{tag}: {count}")


def main():
    """Main analysis workflow"""

    print("\n" + "=" * 60)
    print("  🔬 ANÁLISIS DE raw-manifiesto.md")
    print("  Triple-Persistence System Demo")
    print("=" * 60)

    # Step 1: Configuration
    print_section("1️⃣  Configuración")

    config = IngestionConfig(
        project="research-autopoietic-template",
        paths=[
            "C:/proyectos/aleia-melquisedec/apps/research-autopoietic-template/010-define/inputs/"
        ],
        neo4j_uri="bolt://localhost:7687",
        neo4j_user="neo4j",
        neo4j_password="password",
        ollama_base_url="http://localhost:11434",
        embedding_model="nomic-embed-text",
        llm_model="qwen2.5:latest",
    )

    print("✅ Configuración lista")
    print(f"   Proyecto: {config.project}")
    print(f"   Path: {config.paths[0]}")
    print(f"   Neo4j: {config.neo4j_uri}")
    print(f"   Ollama: {config.ollama_base_url}")

    # Step 2: Ingestion
    print_section("2️⃣  Ingesta del Documento")

    print("📥 Iniciando pipeline de ingesta...")
    print("   Esto puede tomar 2-5 minutos dependiendo del tamaño del documento\n")

    try:
        with TriplePersistencePipeline(config) as pipeline:
            # Ingest directory
            result = pipeline.ingest_directory(config.paths[0])

            print("\n✅ Ingesta completada!")
            print(f"   Documentos procesados: {result['documents_processed']}")
            print(f"   Chunks creados: {result['chunks_created']}")
            print(f"   Tags extraídos: {result.get('tags_extracted', 0)}")
            print(f"   Referencias: {result.get('references_created', 0)}")

            # Show metadata
            if "metadata" in result:
                print()
                print_metadata(result["metadata"])

            # Step 3: Query Analysis
            print_section("3️⃣  Análisis con Queries")

            print("🔍 Ejecutando queries de análisis...")
            print("   Presiona ENTER después de cada resultado para continuar\n")

            retriever = HybridRetriever(
                index=pipeline.index, neo4j_driver=pipeline.neo4j_driver, project=config.project
            )

            execute_analysis_queries(retriever)

            # Step 4: Knowledge base stats
            export_knowledge_base_stats(retriever)

            # Step 5: Cypher queries
            generate_cypher_queries()

    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Asegúrate de que:")
        print("   1. Neo4j está corriendo (docker-compose up -d)")
        print("   2. Ollama está corriendo y tiene nomic-embed-text")
        print("   3. El path al documento es correcto")
        return 1

    # Final summary
    print_section("✅ Análisis Completado")

    print("📌 Próximos Pasos:\n")
    print("1. 🌐 Explora el grafo en Neo4j Browser:")
    print("   http://localhost:7474\n")

    print("2. 🔍 Ejecuta las queries Cypher de arriba\n")

    print("3. 📊 Revisa las estadísticas generadas\n")

    print("4. 🔗 Explora relaciones:")
    print("   • [[Wikilinks]] entre documentos")
    print("   • #Tags compartidos")
    print("   • Documentos del mismo rostro/fase\n")

    print("5. 💾 Exporta resultados:")
    print("   • CSV desde Neo4j Browser")
    print("   • JSON desde la API de retrieval")
    print("   • Visualizaciones de grafos\n")

    print("🎯 El documento raw-manifiesto.md está ahora:")
    print("   ✅ Indexado en Neo4j (grafo + vector)")
    print("   ✅ Chunkeado semánticamente")
    print("   ✅ Con metadata extraída")
    print("   ✅ Con relaciones mapeadas")
    print("   ✅ Listo para búsquedas híbridas\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
