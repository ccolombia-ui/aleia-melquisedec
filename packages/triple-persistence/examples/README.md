# 🚀 Triple-Persistence Examples

Ejemplos simples para aprender Triple-Persistence paso a paso.

## 📚 Ejemplos Disponibles

### 01: Simple Ingestion
**Tiempo**: 5 minutos
**Archivo**: `01_simple_ingestion.py`

Aprende cómo funciona el pipeline de ingesta:
- Crear documentos con metadata
- Dividir en chunks (semantic chunking)
- Generar embeddings
- Almacenar en Neo4j (graph + vector)

```powershell
python examples/01_simple_ingestion.py
```

**Output esperado**:
```
✅ Documentos procesados: 1
✅ Chunks creados: 7
✅ Embeddings generados: 7
⏱️ Tiempo: 2.4s (simulado)
```

---

### 02: Vector Search
**Tiempo**: 5 minutos
**Archivo**: `02_vector_search.py`

Aprende cómo funciona la búsqueda semántica:
- Query → Embedding
- HNSW index (logarítmico, ultra-rápido)
- Cosine similarity scoring
- Top-K resultados

```powershell
python examples/02_vector_search.py
```

**Output esperado**:
```
🔍 Query: '¿Qué es triple-persistence?'
📊 Resultados: 3

1. Mi Primer Documento
   Similarity: 0.847
   Excerpt: Triple-Persistence es un sistema...
```

---

### 03: Graph Traversal
**Tiempo**: 5 minutos
**Archivo**: `03_graph_traversal.py`

Aprende cómo el grafo mejora los resultados:
- Hybrid retrieval (vector + graph)
- Enriquecer con relaciones ([:REFERENCES], [:TAGGED_WITH])
- Cypher queries avanzadas
- Performance trade-offs

```powershell
python examples/03_graph_traversal.py
```

**Output esperado**:
```
📄 PROPOSITO.md
   Similarity: 0.912
   🔗 Referencias:
      → README.md
      → REQ-001: Template System
```

---

## 🎓 Learning Path

**Orden recomendado**:

1. **Ejemplo 01** (Ingestion) - Entender el flujo de datos
2. **Ejemplo 02** (Vector Search) - Búsqueda semántica pura
3. **Ejemplo 03** (Graph Traversal) - Híbrido vector + graph

**Tiempo total**: 15-20 minutos

---

## 🔧 Requisitos

### Para ejemplos básicos (01-03)
✅ Solo Python 3.11+
✅ NO requiere Neo4j (simulados para aprendizaje)
✅ NO requiere Ollama

### Para producción (ingestion.py, retriever.py)
- Neo4j 5.26+ corriendo
- Ollama corriendo con modelos descargados
- Dependencias: `pip install -r requirements.txt`

---

## 🆚 Ejemplos vs Producción

| Característica | Ejemplos (01-03) | Producción (ingestion.py) |
|----------------|------------------|---------------------------|
| **Neo4j** | Simulado | Real (bolt://localhost:7687) |
| **Embeddings** | Fake arrays | Ollama (nomic-embed-text) |
| **Chunking** | Simple (párrafos) | Semántico (LlamaIndex) |
| **Performance** | Instant | 2-5 min (100 docs) |
| **Objetivo** | Aprendizaje | Producción |

---

## 💡 Próximos Pasos

Después de completar los 3 ejemplos:

1. ✅ Ver implementación real: `triple_persistence/ingestion.py`
2. ✅ Configurar Neo4j + Ollama (ver quickstart guide)
3. ✅ Ingestar research-autopoietic-template
4. ✅ Experimentar con queries propias

---

## 🐛 Troubleshooting

**Error: ModuleNotFoundError**
```powershell
# Instalar dependencies
pip install -r ../requirements.txt
```

**Error: numpy no instalado (ejemplo 02)**
```powershell
pip install numpy
```

**Quiero probar con Neo4j real**
```powershell
# Ver quickstart guide completo
cat ../../docs/guides/triple-persistence-quickstart.md
```

---

**Manual completo**: Ver `docs/guides/triple-persistence-quickstart.md`
