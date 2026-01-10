"""
Ejemplo 1: Ingestar un solo documento Markdown

Objetivo: Entender cómo funciona el pipeline de ingesta
Tiempo: 5 minutos
Pre-requisitos: Neo4j corriendo, Ollama corriendo

Uso:
    python examples/01_simple_ingestion.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import hashlib
from datetime import datetime

from triple_persistence.models import Document, IngestionConfig


def create_sample_document():
    """Crea un documento de ejemplo para ingestar"""

    content = """# Mi Primer Documento con Triple-Persistence

Este es un documento de prueba para entender cómo funciona el sistema.

## ¿Qué es Triple-Persistence?

Triple-Persistence es un sistema que almacena documentos en tres capas:

1. **Markdown** (fuente de verdad): Archivos .md versionados con Git
2. **Graph** (relaciones): Neo4j almacena metadata y conexiones entre documentos
3. **Vector** (semántica): Embeddings para búsqueda semántica

## ¿Por qué Triple-Persistence?

- **Markdown**: Legible por humanos, versionable, portable
- **Graph**: Navegar relaciones (X referencia Y, X deriva de Z)
- **Vector**: Encontrar documentos similares semánticamente

## Ejemplo de Uso

Si tienes documentos de investigación, puedes:
1. Escribir en Markdown (tu editor favorito)
2. Ingestar con triple-persistence (1 comando)
3. Buscar semánticamente ("¿qué atomics hablan de templates?")
4. Navegar el grafo (ver referencias, dependencias)

## Conclusión

Triple-Persistence combina lo mejor de tres mundos: simplicidad de Markdown,
poder de grafos, y búsqueda semántica con LLMs.
"""

    # Crear objeto Document
    doc = Document(
        id="doc-ejemplo-001",
        path="examples/data/ejemplo.md",
        title="Mi Primer Documento",
        type="atomic",  # Puede ser: requirement, atomic, adr, lesson
        rostro="HYPATIA",  # Rostro MELQUISEDEC
        phase="020-conceive",  # Fase del proyecto
        created_at=datetime.now(),
        updated_at=datetime.now(),
        content_hash=hashlib.sha256(content.encode()).hexdigest(),
        text=content,
        metadata={
            "tags": ["tutorial", "triple-persistence", "quickstart"],
            "author": "Sistema",
            "version": "1.0.0",
        },
    )

    return doc


def simple_ingestion_example():
    """Ejemplo simplificado de ingesta (sin Neo4j real por ahora)"""

    print("=" * 60)
    print("🚀 Ejemplo 1: Simple Ingestion")
    print("=" * 60)
    print()

    # Paso 1: Crear documento de ejemplo
    print("📄 Paso 1: Creando documento de ejemplo...")
    doc = create_sample_document()
    print(f"   ✅ Documento creado: {doc.title}")
    print(f"   📝 Tipo: {doc.type}")
    print(f"   🎭 Rostro: {doc.rostro}")
    print(f"   📊 Tamaño: {len(doc.text)} caracteres")
    print()

    # Paso 2: Chunking (dividir en pedazos)
    print("✂️  Paso 2: Chunking (dividir en pedazos)...")
    # Chunking simple por párrafos (en producción usamos SemanticSplitterNodeParser)
    chunks = [p.strip() for p in doc.text.split("\n\n") if p.strip()]
    print(f"   ✅ {len(chunks)} chunks creados")
    print(f"   📏 Chunk sizes: {[len(c) for c in chunks[:3]]}... caracteres")
    print()

    # Paso 3: Simular embeddings (en producción usamos Ollama)
    print("🔢 Paso 3: Generando embeddings (simulado)...")
    # En producción: embeddings = ollama.embed_batch(chunks)
    embeddings = [[0.1, 0.2, 0.3] * 256 for _ in chunks]  # Fake 768-dim embeddings
    print(f"   ✅ {len(embeddings)} embeddings generados")
    print(f"   📐 Dimensión: {len(embeddings[0])} (768 en producción)")
    print()

    # Paso 4: Crear nodos en Neo4j (simulado)
    print("🗄️  Paso 4: Almacenando en Neo4j (simulado)...")
    print(f"   CREATE (:Document {{id: '{doc.id}', title: '{doc.title}'}})")
    for i, chunk in enumerate(chunks[:3]):
        print(f"   CREATE (:Chunk {{id: '{doc.id}-chunk-{i}', text: '{chunk[:50]}...'}})")
        print(f"   CREATE (:Document)-[:HAS_CHUNK]->(:Chunk)")
    print(f"   ... ({len(chunks)} chunks total)")
    print()

    # Paso 5: Resumen
    print("=" * 60)
    print("✅ INGESTION COMPLETADA")
    print("=" * 60)
    print(f"📊 Estadísticas:")
    print(f"   • Documentos procesados: 1")
    print(f"   • Chunks creados: {len(chunks)}")
    print(f"   • Embeddings generados: {len(embeddings)}")
    print(f"   • Nodos Neo4j (simulados): {1 + len(chunks)} nodos, {len(chunks)} relaciones")
    print()
    print("🎯 Próximos Pasos:")
    print("   1. Ejecutar con Neo4j real: Ver ingestion.py implementación completa")
    print("   2. Probar ejemplo 02: Vector Search")
    print("   3. Probar ejemplo 03: Graph Traversal")
    print()

    # Mostrar primer chunk para inspección
    print("📝 Primer chunk (para inspección):")
    print("-" * 60)
    print(chunks[0][:200] + "..." if len(chunks[0]) > 200 else chunks[0])
    print("-" * 60)
    print()


if __name__ == "__main__":
    simple_ingestion_example()

    print("💡 NOTA: Este es un ejemplo SIMPLIFICADO para aprendizaje.")
    print("   Para ingesta real con Neo4j, ver: triple_persistence/ingestion.py")
