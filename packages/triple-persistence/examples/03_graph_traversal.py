"""
Ejemplo 3: Enriquecer resultados con Graph Traversal

Objetivo: Ver cómo el grafo mejora los resultados de vector search
Tiempo: 5 minutos
Pre-requisitos: Entender ejemplo 02 (vector search)

Uso:
    python examples/03_graph_traversal.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from triple_persistence.models import QueryResult


def graph_traversal_example():
    """Ejemplo de hybrid retrieval (vector + graph)"""

    print("=" * 60)
    print("🕸️  Ejemplo 3: Graph Traversal")
    print("=" * 60)
    print()

    # Paso 1: Vector Search (del ejemplo 02)
    print("🔍 Paso 1: Vector Search (del ejemplo anterior)...")
    query = "templates autopoiéticos con feedback empírico"

    # Resultado de vector search (top-1)
    initial_result = {
        "id": "doc-proposito",
        "title": "PROPOSITO.md",
        "similarity": 0.912,
        "text": "Templates autopoiéticos son estructuras que se auto-mejoran mediante feedback empírico...",
    }

    print(f"   ❓ Query: '{query}'")
    print(f"   ✅ Top resultado: {initial_result['title']}")
    print(f"   🎯 Similarity: {initial_result['similarity']:.3f}")
    print()

    # Paso 2: Explorar el grafo
    print("🕸️  Paso 2: Graph Traversal - Explorar relaciones...")
    print()

    # Simular grafo Neo4j
    graph = {
        "doc-proposito": {
            "references": ["doc-readme", "doc-req-001"],
            "tagged_with": ["autopoietic", "templates", "feedback"],
            "derived_from": ["doc-literature-review"],
        },
        "doc-readme": {
            "references": ["doc-proposito", "doc-design"],
            "tagged_with": ["overview", "quickstart"],
        },
        "doc-req-001": {"references": [], "tagged_with": ["requirements", "templates"]},
    }

    print("   🗂️  Relaciones encontradas para PROPOSITO.md:")
    print()
    print("   📖 [:REFERENCES] (documentos citados):")
    for ref_id in graph["doc-proposito"]["references"]:
        print(f"      → {ref_id}")
    print()
    print("   🏷️  [:TAGGED_WITH] (tags):")
    for tag in graph["doc-proposito"]["tagged_with"]:
        print(f"      → #{tag}")
    print()
    print("   🧬 [:DERIVED_FROM] (fuentes):")
    for source in graph["doc-proposito"]["derived_from"]:
        print(f"      → {source}")
    print()

    # Paso 3: Enriquecer resultado original
    print("🔄 Paso 3: Enriquecer resultado con información del grafo...")

    # Fetch full info for referenced docs
    referenced_docs = [
        {"id": "doc-readme", "title": "README.md", "excerpt": "Guía rápida del proyecto..."},
        {
            "id": "doc-req-001",
            "title": "REQ-001: Template System",
            "excerpt": "Requisitos del sistema de templates...",
        },
    ]

    enriched_result = QueryResult(
        document_id=initial_result["id"],
        document_title=initial_result["title"],
        similarity_score=initial_result["similarity"],
        excerpt=initial_result["text"],
        related_documents=[doc["title"] for doc in referenced_docs],
    )

    print()
    print("   ✅ Resultado enriquecido:")
    print(f"      📄 Documento: {enriched_result.document_title}")
    print(f"      🎯 Similarity: {enriched_result.similarity_score:.3f}")
    print(f"      📝 Excerpt: {enriched_result.excerpt[:60]}...")
    print(f"      🔗 Referencias ({len(enriched_result.related_documents)}):")
    for related in enriched_result.related_documents:
        print(f"         → {related}")
    print()

    # Paso 4: Comparación Vector-Only vs Hybrid
    print("=" * 60)
    print("🆚 VECTOR-ONLY vs HYBRID (Vector + Graph)")
    print("=" * 60)
    print()

    print("🔵 Vector-Only (Ejemplo 02):")
    print("   ✅ Encuentra: PROPOSITO.md (similarity 0.912)")
    print("   ❌ NO muestra: Referencias, tags, fuentes")
    print("   ❌ Usuario debe buscar manualmente documentos relacionados")
    print()

    print("🟢 Hybrid (Vector + Graph):")
    print("   ✅ Encuentra: PROPOSITO.md (similarity 0.912)")
    print("   ✅ PLUS: README.md, REQ-001 (referencias)")
    print("   ✅ PLUS: #autopoietic, #templates, #feedback (tags)")
    print("   ✅ PLUS: Literature Review (fuente origen)")
    print("   🎯 Usuario ve contexto completo en 1 query")
    print()

    # Paso 5: Use Cases
    print("=" * 60)
    print("🎯 USE CASES - ¿CUÁNDO USAR GRAPH TRAVERSAL?")
    print("=" * 60)
    print()

    print("✅ Usar Hybrid (Vector + Graph) cuando:")
    print("   • Necesitas contexto (qué documentos cita, qué lo cita)")
    print("   • Explorar relaciones (dependencias, derivaciones)")
    print("   • Encontrar documentos relacionados indirectamente")
    print("   • Research/investigación (conectar conceptos)")
    print()

    print("⚠️  Usar Vector-Only cuando:")
    print("   • Solo quieres similarity pura (top-k más similares)")
    print("   • Performance crítico (graph traversal añade latencia)")
    print("   • Documentos independientes (sin relaciones importantes)")
    print()

    # Paso 6: Cypher Query Real
    print("=" * 60)
    print("📝 CYPHER QUERY - HYBRID RETRIEVAL")
    print("=" * 60)
    print()
    print("```cypher")
    print("// 1. Vector Search")
    print("CALL db.index.vector.queryNodes(")
    print("  'triple_persistence_embeddings',")
    print("  10,  // top_k")
    print("  $query_embedding")
    print(") YIELD node AS doc, score")
    print()
    print("// 2. Graph Traversal - Enriquecer con relaciones")
    print("OPTIONAL MATCH (doc)-[:REFERENCES]->(ref)")
    print("OPTIONAL MATCH (doc)-[:TAGGED_WITH]->(tag)")
    print("OPTIONAL MATCH (doc)-[:DERIVED_FROM]->(source)")
    print()
    print("// 3. Agregar y retornar")
    print("RETURN")
    print("  doc.id AS document_id,")
    print("  doc.title AS document_title,")
    print("  score AS similarity,")
    print("  doc.text AS excerpt,")
    print("  collect(DISTINCT ref.title) AS references,")
    print("  collect(DISTINCT tag.name) AS tags,")
    print("  collect(DISTINCT source.title) AS sources")
    print("ORDER BY score DESC")
    print("LIMIT 5;")
    print("```")
    print()

    # Paso 7: Performance Considerations
    print("=" * 60)
    print("⚡ PERFORMANCE - Vector vs Hybrid")
    print("=" * 60)
    print()

    print("🔵 Vector-Only:")
    print("   • Latency: ~50ms (HNSW index ultra-rápido)")
    print("   • Throughput: 1000+ queries/sec")
    print("   • Usa: db.index.vector.queryNodes()")
    print()

    print("🟡 Hybrid (Vector + Graph):")
    print("   • Latency: ~150ms (+100ms por traversals)")
    print("   • Throughput: 300-500 queries/sec")
    print("   • Usa: OPTIONAL MATCH (doc)-[:REL]->(related)")
    print()

    print("💡 Optimización:")
    print("   • Limitar profundidad de traversal (1-2 hops max)")
    print("   • Crear índices en propiedades frecuentes")
    print("   • Cachear resultados para queries repetidas")
    print()

    # Paso 8: Resumen
    print("=" * 60)
    print("✅ GRAPH TRAVERSAL COMPLETADO")
    print("=" * 60)
    print()
    print("📚 Has aprendido:")
    print("   ✅ Diferencia Vector-Only vs Hybrid")
    print("   ✅ Cómo enriquecer resultados con relaciones")
    print("   ✅ Cypher queries para hybrid retrieval")
    print("   ✅ Trade-offs de performance")
    print()
    print("🎯 Próximos Pasos:")
    print("   1. Ver retriever.py para implementación completa")
    print("   2. Experimentar con research-autopoietic-template")
    print("   3. Ajustar top_k y traversal depth según tu caso")
    print()
    print("🏆 Recomendación:")
    print("   • Usa Hybrid por default (mejor contexto)")
    print("   • Usa Vector-Only solo si latencia es crítica")
    print()


if __name__ == "__main__":
    graph_traversal_example()

    print("💡 NOTA: Este es un ejemplo SIMPLIFICADO para aprendizaje.")
    print("   Para hybrid retrieval real con Neo4j, ver: triple_persistence/retriever.py")
