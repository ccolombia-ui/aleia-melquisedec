"""
Ejemplo 2: Buscar documentos con Vector Search

Objetivo: Entender cómo funciona la búsqueda semántica
Tiempo: 5 minutos
Pre-requisitos: Datos ingestados (ejecutar ejemplo 01 primero)

Uso:
    python examples/02_vector_search.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from triple_persistence.models import QueryRequest, QueryResponse, QueryResult


def simulate_vector_similarity(query_embedding, doc_embeddings):
    """Simula similarity score usando cosine similarity"""
    # En producción, Neo4j hace esto con HNSW index

    # Normalize vectors
    query_norm = query_embedding / np.linalg.norm(query_embedding)

    similarities = []
    for doc_emb in doc_embeddings:
        doc_norm = doc_emb / np.linalg.norm(doc_emb)
        similarity = np.dot(query_norm, doc_norm)
        similarities.append(similarity)

    return similarities


def vector_search_example():
    """Ejemplo de vector search (simulado)"""

    print("=" * 60)
    print("🔍 Ejemplo 2: Vector Search")
    print("=" * 60)
    print()

    # Paso 1: Query del usuario
    query_text = "¿Qué es triple-persistence y cómo funciona?"
    print(f"❓ Query: '{query_text}'")
    print()

    # Paso 2: Convertir query a embedding
    print("🔢 Paso 1: Convertir query a embedding...")
    # En producción: query_embedding = ollama.embed(query_text)
    query_embedding = np.random.rand(768)  # Fake 768-dim embedding
    print(f"   ✅ Embedding generado: {len(query_embedding)} dimensiones")
    print(f"   📊 Primeros valores: {query_embedding[:5]}")
    print()

    # Paso 3: Documentos de ejemplo (simulados)
    print("📚 Paso 2: Documentos en la base de datos (simulados)...")
    docs = [
        {
            "id": "doc-001",
            "title": "Mi Primer Documento",
            "text": "Triple-Persistence es un sistema que almacena documentos en tres capas: Markdown, Graph, Vector.",
            "embedding": np.random.rand(768),
        },
        {
            "id": "doc-002",
            "title": "Guía de Neo4j",
            "text": "Neo4j es una base de datos de grafos que permite almacenar y consultar relaciones entre entidades.",
            "embedding": np.random.rand(768),
        },
        {
            "id": "doc-003",
            "title": "Tutorial de Embeddings",
            "text": "Los embeddings son representaciones vectoriales de texto que capturan similitud semántica.",
            "embedding": np.random.rand(768),
        },
        {
            "id": "doc-004",
            "title": "Research Autopoietic Template",
            "text": "Templates autopoiéticos son estructuras que se auto-mejoran mediante feedback empírico.",
            "embedding": np.random.rand(768),
        },
    ]
    print(f"   ✅ {len(docs)} documentos disponibles")
    print()

    # Paso 4: Vector Search (similarity scoring)
    print("🎯 Paso 3: Calculando similarity scores...")
    doc_embeddings = [d["embedding"] for d in docs]
    similarities = simulate_vector_similarity(query_embedding, doc_embeddings)

    # Combinar docs con similarities
    for doc, sim in zip(docs, similarities):
        doc["similarity"] = sim

    # Ordenar por similarity (descendente)
    docs_sorted = sorted(docs, key=lambda x: x["similarity"], reverse=True)
    print(f"   ✅ Similarity scores calculados")
    print()

    # Paso 5: Top-K resultados
    top_k = 3
    print(f"🏆 Paso 4: Top-{top_k} Resultados:")
    print()

    results = []
    for i, doc in enumerate(docs_sorted[:top_k], 1):
        result = QueryResult(
            document_id=doc["id"],
            document_title=doc["title"],
            similarity_score=float(doc["similarity"]),
            excerpt=doc["text"][:100] + "..." if len(doc["text"]) > 100 else doc["text"],
            related_documents=[],  # Sin graph traversal en este ejemplo
        )
        results.append(result)

        print(f"   {i}. {doc['title']}")
        print(f"      🎯 Similarity: {doc['similarity']:.3f}")
        print(f"      📝 Excerpt: {doc['text'][:80]}...")
        print()

    # Crear QueryResponse
    response = QueryResponse(
        results=results, query_time_ms=45, total_results=len(docs_sorted)  # Simulado
    )

    # Paso 6: Explicación del algoritmo
    print("=" * 60)
    print("🧠 ¿CÓMO FUNCIONA VECTOR SEARCH?")
    print("=" * 60)
    print()
    print("1️⃣ Query → Embedding:")
    print("   Tu pregunta se convierte en un vector de 768 números")
    print("   Ejemplo: 'triple-persistence' → [0.12, -0.34, 0.56, ...]")
    print()
    print("2️⃣ Buscar documentos similares:")
    print("   Neo4j usa HNSW index (rápido, logarítmico)")
    print("   Compara el vector query con todos los document embeddings")
    print()
    print("3️⃣ Similarity Score (Cosine Similarity):")
    print("   • 1.0 = Idéntico (mismo significado)")
    print("   • 0.8-0.9 = Muy similar")
    print("   • 0.6-0.8 = Relacionado")
    print("   • < 0.6 = Poco relacionado")
    print()
    print("4️⃣ Ordenar por Score:")
    print("   Top-K resultados (más similares primero)")
    print()

    # Comparación con búsqueda tradicional
    print("=" * 60)
    print("🆚 VECTOR SEARCH vs BÚSQUEDA TRADICIONAL")
    print("=" * 60)
    print()
    print("❓ Query: '¿Qué es triple-persistence?'")
    print()
    print("🔴 Búsqueda tradicional (keyword):")
    print("   • Busca palabras exactas: 'triple', 'persistence'")
    print("   • NO encuentra: 'sistema de tres capas' (misma idea, palabras diferentes)")
    print("   • MISS: Sinónimos, paráfrasis")
    print()
    print("🟢 Vector Search (semántica):")
    print("   • Entiende el SIGNIFICADO")
    print("   • Encuentra: 'triple-persistence', 'sistema de tres capas', 'arquitectura triple'")
    print("   • HIT: Conceptos relacionados aunque usen palabras diferentes")
    print()

    # Mostrar Cypher query equivalente
    print("=" * 60)
    print("📝 CYPHER QUERY EQUIVALENTE (Neo4j)")
    print("=" * 60)
    print()
    print("```cypher")
    print("// Vector Search en Neo4j")
    print(f"CALL db.index.vector.queryNodes(")
    print(f"  'triple_persistence_embeddings',  // Index name")
    print(f"  {top_k},                           // top_k")
    print(f"  $query_embedding                   // Query vector")
    print(f")")
    print(f"YIELD node, score")
    print(f"RETURN ")
    print(f"  node.id AS document_id,")
    print(f"  node.title AS document_title,")
    print(f"  score AS similarity,")
    print(f"  node.text AS text")
    print(f"ORDER BY score DESC")
    print(f"LIMIT {top_k};")
    print("```")
    print()

    print("✅ Vector Search completado!")
    print()
    print("🎯 Próximos Pasos:")
    print("   1. Probar ejemplo 03: Graph Traversal (enriquecer con relaciones)")
    print("   2. Ver retriever.py para implementación completa")
    print("   3. Ingestar tus propios documentos y experimentar")
    print()


if __name__ == "__main__":
    # Check numpy disponible
    try:
        import numpy as np
    except ImportError:
        print("❌ ERROR: numpy no instalado")
        print("   Instalar con: pip install numpy")
        sys.exit(1)

    vector_search_example()

    print("💡 NOTA: Este es un ejemplo SIMPLIFICADO para aprendizaje.")
    print("   Para vector search real con Neo4j, ver: triple_persistence/retriever.py")
