# 📖 Cómo Analizar Documentos con Triple-Persistence

Esta guía te muestra cómo usar el sistema Triple-Persistence para analizar cualquier documento markdown de tu base de conocimiento.

## 🎯 Caso de Uso: raw-manifiesto.md

El archivo `raw-manifiesto.md` es un documento extenso (17K+ líneas) que contiene el diseño completo del meta-framework PRAXIS-RBM. Vamos a analizarlo usando Triple-Persistence.

---

## 📋 Tabla de Contenidos

1. [Pre-requisitos](#pre-requisitos)
2. [Paso 1: Iniciar el Stack](#paso-1-iniciar-el-stack)
3. [Paso 2: Ejecutar el Script de Análisis](#paso-2-ejecutar-el-script-de-análisis)
4. [Paso 3: Explorar en Neo4j Browser](#paso-3-explorar-en-neo4j-browser)
5. [Paso 4: Queries Avanzadas](#paso-4-queries-avanzadas)
6. [Paso 5: Exportar Resultados](#paso-5-exportar-resultados)
7. [Troubleshooting](#troubleshooting)

---

## Pre-requisitos

✅ **Software necesario:**
- Docker Desktop (Windows/Mac) o Docker Engine (Linux)
- Python 3.11+
- Git

✅ **Servicios corriendo:**
```powershell
# Iniciar el stack completo
docker-compose -f docker-compose.triple-persistence.yml up -d

# Verificar que todo está corriendo
docker-compose -f docker-compose.triple-persistence.yml ps
```

Deberías ver:
- ✅ neo4j (port 7474, 7687)
- ✅ ollama (port 11434)
- ✅ ollama-setup (completed)
- ✅ triple-persistence (port 8000)

---

## Paso 1: Iniciar el Stack

```powershell
# Navegar al proyecto
cd C:\proyectos\aleia-melquisedec

# Iniciar servicios
docker-compose -f docker-compose.triple-persistence.yml up -d

# Esperar a que Neo4j esté listo (30-60 segundos)
docker logs -f triple-persistence-neo4j-1

# Verificar Ollama tiene los modelos
docker exec -it triple-persistence-ollama-1 ollama list
```

Deberías ver:
```
NAME                    ID              SIZE
qwen2.5:latest         abc123...       4.7GB
nomic-embed-text:latest def456...       274MB
```

---

## Paso 2: Ejecutar el Script de Análisis

```powershell
# Navegar al paquete
cd packages\triple-persistence

# Activar entorno virtual (si existe)
.\.venv\Scripts\Activate.ps1

# Instalar dependencias (si no están)
pip install -r requirements.txt

# Ejecutar análisis del manifiesto
python examples\05_analyze_manifiesto.py
```

### ¿Qué hace el script?

1. **Ingesta el documento** (`raw-manifiesto.md`):
   - Lee el archivo markdown completo (17K líneas)
   - Extrae metadata del frontmatter (si existe)
   - Auto-detecta type, rostro, phase desde el path
   - Identifica [[wikilinks]] y #tags
   - Genera chunks semánticos usando embeddings
   - Almacena en Neo4j (nodos Document + Chunk)
   - Crea relaciones (REFERENCES, TAGGED_WITH, etc.)

2. **Crea índice vectorial**:
   - Embeddings con `nomic-embed-text` (768 dimensiones)
   - Índice HNSW en Neo4j para búsqueda rápida
   - Similitud por coseno

3. **Ejecuta queries de análisis**:
   - ¿Cuáles son los principios P1-P10?
   - ¿Cómo funciona PRAXIS-RBM?
   - ¿Qué son templates autopoiéticos?
   - ¿Cómo se estructura 010-050?
   - ¿Relación con spec-workflow-mcp?

4. **Genera estadísticas**:
   - Totales: documentos, chunks, tags, referencias
   - Distribución por tipo, rostro, fase
   - Tags más usados

5. **Muestra queries Cypher**:
   - Para exploración manual en Neo4j Browser

### Salida Esperada

```
============================================================
  🔬 ANÁLISIS DE raw-manifiesto.md
  Triple-Persistence System Demo
============================================================

============================================================
  1️⃣  Configuración
============================================================

✅ Configuración lista
   Proyecto: research-autopoietic-template
   Path: C:/proyectos/.../010-define/inputs/
   Neo4j: bolt://localhost:7687
   Ollama: http://localhost:11434

============================================================
  2️⃣  Ingesta del Documento
============================================================

📥 Iniciando pipeline de ingesta...
   Esto puede tomar 2-5 minutos dependiendo del tamaño del documento

✅ Ingesta completada!
   Documentos procesados: 1
   Chunks creados: 234
   Tags extraídos: 47
   Referencias: 23

📄 Metadata Extraída:
   Title: Unified Research Template Design v4.3.1
   Type: document
   Rostro: MELQUISEDEC
   Phase: 010-define
   Tags: #praxis, #rbm, #autopoiesis, #template, #melquisedec...
   References: 23 wikilinks

============================================================
  3️⃣  Análisis con Queries
============================================================

[... queries interactivas ...]

============================================================
  📊 Estadísticas de la Base de Conocimiento
============================================================

📈 Totales:
   Documentos: 1
   Chunks: 234
   Tags: 47
   Referencias: 23

[... más estadísticas ...]
```

---

## Paso 3: Explorar en Neo4j Browser

### 3.1 Abrir Neo4j Browser

```
URL: http://localhost:7474
User: neo4j
Password: password
```

### 3.2 Queries Básicas

**Ver el documento del manifiesto:**

```cypher
MATCH (d:Document {project: 'research-autopoietic-template'})
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN d.id, d.title, d.type, d.path
```

**Ver los primeros 10 chunks:**

```cypher
MATCH (d:Document)-[:HAS_CHUNK]->(c:Chunk)
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN d.title, c.text, c.embedding IS NOT NULL as has_embedding
LIMIT 10
```

**Ver referencias ([[wikilinks]]):**

```cypher
MATCH (d:Document)-[r:REFERENCES]->(target:Document)
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN d.title as from_doc, target.title as to_doc, type(r) as relationship
```

**Ver tags más usados:**

```cypher
MATCH (d:Document)-[:TAGGED_WITH]->(t:Tag)
WHERE d.project = 'research-autopoietic-template'
RETURN t.name, count(*) as usage
ORDER BY usage DESC
LIMIT 10
```

**Visualizar grafo completo (hasta 2 saltos):**

```cypher
MATCH path = (d:Document)-[:REFERENCES*1..2]-(related:Document)
WHERE d.path CONTAINS 'raw-manifiesto.md'
RETURN path
LIMIT 50
```

---

## Paso 4: Queries Avanzadas

### 4.1 Búsqueda por Concepto

```cypher
MATCH (d:Document)
WHERE d.project = 'research-autopoietic-template'
  AND (d.text CONTAINS 'MELQUISEDEC' OR d.text CONTAINS 'autopoiesis')
RETURN d.title, d.path, d.rostro
LIMIT 10
```

### 4.2 Documentos del Mismo Rostro

```cypher
MATCH (d:Document)-[:CREATED_BY]->(r:Rostro {name: 'MELQUISEDEC'})
RETURN d.title, d.path, d.type
```

### 4.3 Documentos de la Misma Fase

```cypher
MATCH (d:Document)-[:BELONGS_TO]->(p:Phase {name: '010-define'})
RETURN d.title, d.path, d.rostro
```

### 4.4 Documentos Relacionados por Tags

```cypher
MATCH (d1:Document)-[:TAGGED_WITH]->(t:Tag)<-[:TAGGED_WITH]-(d2:Document)
WHERE d1.path CONTAINS 'raw-manifiesto.md' AND d1 <> d2
RETURN d1.title as documento, collect(DISTINCT t.name) as tags_compartidos, d2.title as relacionado
```

### 4.5 Camino Más Corto Entre Documentos

```cypher
MATCH (d1:Document {path: '/path/to/raw-manifiesto.md'}),
      (d2:Document {path: '/path/to/otro-doc.md'}),
      path = shortestPath((d1)-[:REFERENCES*]-(d2))
RETURN path
```

---

## Paso 5: Exportar Resultados

### 5.1 Exportar a CSV (desde Neo4j Browser)

1. Ejecutar query
2. Click en botón "Download" (⬇️)
3. Seleccionar formato: CSV, JSON, or TXT

### 5.2 Exportar con Python

```python
from triple_persistence.retriever import HybridRetriever

# ... initialize retriever ...

# Query
request = QueryRequest(
    query="¿Qué son templates autopoiéticos?",
    top_k=10,
    include_graph=True
)
response = retriever.query(request)

# Export to JSON
import json
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(response.model_dump(), f, indent=2, ensure_ascii=False)

# Export to CSV
import csv
with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['document_id', 'path', 'similarity', 'excerpt'])
    for result in response.results:
        writer.writerow([
            result.document_id,
            result.document_path,
            result.similarity,
            result.excerpt[:100]
        ])
```

### 5.3 Exportar Grafo Completo

```cypher
// Export todos los nodos y relaciones
CALL apoc.export.json.all("knowledge-graph.json", {})

// Export solo el proyecto actual
CALL apoc.export.json.query(
  "MATCH (d:Document {project: 'research-autopoietic-template'})-[r]->(n) RETURN d, r, n",
  "project-graph.json",
  {}
)
```

---

## Troubleshooting

### ❌ Error: "Connection refused to Neo4j"

**Solución:**
```powershell
# Verificar que Neo4j está corriendo
docker ps | findstr neo4j

# Ver logs de Neo4j
docker logs triple-persistence-neo4j-1

# Reiniciar Neo4j
docker-compose -f docker-compose.triple-persistence.yml restart neo4j
```

### ❌ Error: "Ollama model not found"

**Solución:**
```powershell
# Verificar modelos instalados
docker exec -it triple-persistence-ollama-1 ollama list

# Si no están, descargarlos manualmente
docker exec -it triple-persistence-ollama-1 ollama pull nomic-embed-text
docker exec -it triple-persistence-ollama-1 ollama pull qwen2.5:latest
```

### ❌ Error: "File not found: raw-manifiesto.md"

**Solución:**
```python
# En el script, usar path absoluto
config = IngestionConfig(
    paths=[
        "C:/proyectos/aleia-melquisedec/apps/research-autopoietic-template/010-define/inputs/"
    ]
)
```

### ❌ Error: "Out of memory during ingestion"

**Solución:**
```yaml
# En docker-compose.triple-persistence.yml, aumentar memoria de Neo4j
environment:
  - NEO4J_server_memory_pagecache_size=2G  # Era 1G
  - NEO4J_server_memory_heap_max__size=4G  # Era 2G
```

### ⚠️ Ingesta muy lenta (>10 minutos)

**Causas posibles:**
1. Documento muy grande (>10K líneas)
2. Muchos chunks generados (>500)
3. Ollama en CPU (sin GPU)

**Soluciones:**
- Reducir `chunk_size` en config
- Usar GPU para Ollama (Docker GPU support)
- Procesar en batch más pequeño

---

## 🎯 Resumen del Flujo Completo

```
1. raw-manifiesto.md (17K líneas)
   ↓
2. Triple-Persistence Ingestion Pipeline
   ├── Read markdown
   ├── Extract metadata (frontmatter + auto-detect)
   ├── Chunk semánticamente (embeddings)
   ├── Store en Neo4j (nodes + relationships)
   └── Create vector index (HNSW)
   ↓
3. Neo4j Knowledge Graph
   ├── Document nodes (metadata)
   ├── Chunk nodes (embeddings)
   ├── Tag nodes (#tags)
   ├── Phase nodes (010-define, etc.)
   ├── Rostro nodes (MELQUISEDEC, etc.)
   └── Relationships (REFERENCES, TAGGED_WITH, etc.)
   ↓
4. Hybrid Retriever
   ├── Vector search (similarity)
   ├── Graph traversal (relationships)
   ├── Filtering (type, rostro, phase, tags)
   └── Score boosting (connections)
   ↓
5. Query Results
   ├── Ranked by similarity
   ├── Enriched with graph context
   ├── Metadata included
   └── Related documents listed
   ↓
6. Exploration & Export
   ├── Neo4j Browser (visual)
   ├── Cypher queries (analysis)
   ├── Python API (programmatic)
   └── Export (CSV, JSON, graph)
```

---

## 📚 Referencias

- [Triple-Persistence Quickstart](QUICKSTART-MVP.md)
- [Neo4j Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Manifiesto MELQUISEDEC](../../docs/manifiesto/README.md)

---

## 💡 Próximos Pasos

1. **Analizar más documentos:**
   - Ingerir toda la carpeta `010-define/`
   - Ingerir `020-conceive/`, `030-develop/`, etc.
   - Crear corpus completo del proyecto

2. **Crear dashboards:**
   - Visualizaciones de tags
   - Mapas de conceptos
   - Líneas de tiempo de evolución

3. **Integrar con RAG:**
   - Usar retriever para Q&A sobre el manifiesto
   - Generar summaries automáticos
   - Crear chatbot sobre el conocimiento

4. **Automatizar análisis:**
   - Pipeline CI/CD para ingesta automática
   - Notificaciones de nuevos documentos
   - Reports periódicos de estadísticas

---

**¿Preguntas? Consulta:**
- [QUICKSTART-MVP.md](QUICKSTART-MVP.md) - Guía de inicio rápido
- [README.md](README.md) - Documentación completa del paquete
- Issues en GitHub: [ccolombia-ui/aleia-melquisedec](https://github.com/ccolombia-ui/aleia-melquisedec)
