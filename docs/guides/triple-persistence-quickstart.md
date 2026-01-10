# 🚀 Triple-Persistence Quickstart Guide (Para Dummies)

**Fecha**: 2026-01-10
**Versión**: 1.0.0
**Audiencia**: Desarrolladores, investigadores sin experiencia en Neo4j/LLMs

---

## 📚 ¿Qué vas a aprender?

Este manual te enseña a usar **2 sistemas en paralelo**:

1. **GenAI Stack** (Laboratorio) - Para experimentar y aprender
2. **LlamaIndex MVP** (Producción) - Para tu investigación real

**Tiempo estimado**: 2-3 horas para setup completo

---

## 🎯 FASE 1: GenAI Stack (Laboratorio)

### ¿Qué es GenAI Stack?

Piensa en GenAI Stack como **un laboratorio pre-armado**:
- Neo4j (base de datos graph+vector)
- Ollama (LLMs locales)
- LangChain (framework RAG)
- 5 aplicaciones de ejemplo

**Objetivo**: Ver funcionando Neo4j + Ollama + Vector Search en **5 minutos**

---

### Paso 1.1: Prerrequisitos

Verifica que tienes instalado:

```powershell
# Docker Desktop
docker --version
# Debe mostrar: Docker version 24.x o superior

# Ollama (OPCIONAL - puedes usar contenedor Docker también)
ollama list
# Si está instalado, muestra modelos

# Git
git --version
```

**Si falta Docker Desktop**:
- Descargar: https://www.docker.com/products/docker-desktop/

**Ollama - TIENES 2 OPCIONES**:

**OPCIÓN A: TODO EN DOCKER (RECOMENDADO PARA EMPEZAR)**
- No necesitas instalar Ollama localmente
- Usa: `docker compose --profile linux up`
- Funciona en Windows/Mac gracias a Docker Desktop (WSL2/VM)

**OPCIÓN B: OLLAMA NATIVO (MEJOR RENDIMIENTO GPU)**
- Descargar: https://ollama.ai/download
- Mejor rendimiento con GPU local
- Usa: `docker compose up` (sin --profile)

---

### Paso 1.2: Instalar GenAI Stack

```powershell
# Ya está clonado en:
cd C:\proyectos\aleia-melquisedec\_lab\genai-stack

# Verificar archivos
lsIniciar GenAI Stack

**OPCIÓN A: TODO EN DOCKER (SIN OLLAMA LOCAL)**

```powershell
cd C:\proyectos\aleia-melquisedec\_lab\genai-stack

# Editar .env para usar Ollama en Docker
# Cambiar: OLLAMA_BASE_URL=http://llm:11434

# Iniciar con perfil Linux (incluye Ollama)
docker compose --profile linux up -d

# Esperar a que todo esté listo (2 minutos)
Start-Sleep -Seconds 120

# Verificar contenedores
docker ps
# Debes ver: database, llm, pull-model, bot, loader
```

**OPCIÓN B: OLLAMA NATIVO (SI YA LO INSTALASTE)**

```powershell
# Terminal 1: Iniciar Ollama
ollama serve

# Terminal 2: Descargar modelos
ollama pull qwen2.5:latest
ollama pull nomic-embed-text

# Terminal 3: Iniciar stack
cd C:\proyectos\aleia-melquisedec\_lab\genai-stack
docker compose up -d

# Verificar
docker ps
```

**Tiempo**:
- Primera vez: 2-3 minutos (descarga imágenes)
- Subsecuentes: 30 segundosC:\proyectos\aleia-melquisedec\_lab\genai-stack

# Iniciar servicios (Neo4j + apps)
docker-compose up -d database

# Esperar a que Neo4j esté listo (30 segundos)
Start-Sleep -Seconds 30

# Verificar que Neo4j está corriendo
docker ps
# Debes ver: genai-stack-database-1 (healthy)
```

**Puertos abiertos**:
- `7474`: Neo4j Browser (interfaz web)
- `7687`: Neo4j Bolt (conexión programática)

---

### Paso 1.4: Abrir Neo4j Browser

```powershell
# Abrir en navegador
start http://localhost:7474

# Credenciales (ya configuradas en .env)
# Usuario: neo4j
# Contraseña: password
```

**Prueba tu primera query Cypher**:

```cypher
// Ver qué nodos existen (debe estar vacío)
MATCH (n) RETURN n LIMIT 25;

// Crear nodo de prueba
CREATE (d:Document {title: "Mi primer documento", text: "Hola Neo4j!"});

// Ver el nodo creado
MATCH (d:Document) RETURN d;
```

**🎉 Si ves el nodo, Neo4j funciona correctamente!**

---

### Paso 1.5: Iniciar Apps de Ejemplo

```powershell
cd C:\proyectos\aleia-melquisedec\_lab\genai-stack

# Iniciar chatbot de soporte
docker-compose up -d bot

# Esperar 30 segundos
Start-Sleep -Seconds 30

# Abrir chatbot
start http://localhost:8501
```

**Apps disponibles**:
- `8501`: Support Bot (chatbot con RAG)
- `8502`: Loader (carga datos StackOverflow)
- `8503`: PDF Bot (Q&A sobre PDFs)
- `8504`: API (REST API)
- `8505`: Frontend (UI Svelte)

---

### Paso 1.6: Experimentar con Datos

**Opción A: Cargar datos StackOverflow**

```powershell
# Iniciar loader
docker-compose up -d loader

# Ver logs (verás preguntas siendo ingestadas)
docker logs genai-stack-loader-1 -f
```

**Opción B: Subir tus propios PDFs**

```powershell
# Iniciar PDF bot
docker-compose up -d pdf_bot

# Abrir interfaz
start http://localhost:8503

# Subir PDF y hacer preguntas!
```

---

### Paso 1.7: Inspeccionar el Grafo

Vuelve a Neo4j Browser (`http://localhost:7474`) y ejecuta:

```cypher
// Contar nodos creados
MATCH (q:Question) RETURN count(q) AS total_questions;
MATCH (a:Answer) RETURN count(a) AS total_answers;

// Ver estructura del grafo
CALL db.schema.visualization();

// Ver embeddings (vectores)
MATCH (q:Question)
WHERE q.embedding IS NOT NULL
RETURN q.title, size(q.embedding) AS embedding_dimension
LIMIT 5;
```

**Debes ver**:
- Nodos `Question` y `Answer`
- Relaciones `[:ANSWERS]`, `[:TAGGED]`
- Embeddings como arrays de números

---

### Paso 1.9: Probar Vector Search

```cypher
// Buscar preguntas similares (vector search)
// NOTA: Esto requiere datos cargados primero

MATCH (q:Question)
CALL db.index.vector.queryNodes('stackoverflow', 5, q.embedding)
YIELD node, score
RETURN node.title AS similar_question, score
LIMIT 5;
```

**🎯 Objetivo cumplido**: Has visto Neo4j Vector Search funcionando!

---

### Paso 1.10: Detener GenAI Stack

Cuando termines de experimentar:

```powershell
cd C:\proyectos\aleia-melquisedec\_lab\genai-stack

# Detener servicios (mantiene datos)
docker-compose down

# Si quieres borrar datos y empezar de cero
docker-compose down -v
```

---

## 🏗️ FASE 2: LlamaIndex MVP (Producción)

### ¿Qué es LlamaIndex MVP?

Es **tu sistema personalizado** para research-autopoietic-template:
- Triple-Persistence (MD + Graph + Vector)
- Código limpio (Hexagonal Architecture)
- Tests automatizados
- Diseñado para documentos de investigación

**Objetivo**: Sistema production-ready en 1 semana

---

### Arquitectura LlamaIndex MVP

```
┌─────────────────────────────────────────────────────────────┐
│                    research-autopoietic-template            │
│  (010-define/, 020-conceive/, 030-design/, 040-build/)     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              TriplePersistencePipeline                      │
│  1. Leer Markdown → 2. Chunking → 3. Embeddings            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      Neo4j 5.26                             │
│  • Graph: (:Document)-[:HAS_CHUNK]->(:Chunk)               │
│  • Vector: HNSW index on Chunk.embedding (768 dim)         │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   HybridRetriever                           │
│  • Vector Search (top-k similar chunks)                     │
│  • Graph Traversal (enriquecer con metadata)               │
└─────────────────────────────────────────────────────────────┘
```

---

### Paso 2.1: Estructura del Package

```
packages/triple-persistence/
├── triple_persistence/
│   ├── __init__.py              ✅ YA CREADO
│   ├── models.py                ✅ YA CREADO (Pydantic schemas)
│   ├── ingestion.py             ⏳ POR CREAR
│   ├── retriever.py             ⏳ POR CREAR
│   ├── neo4j_client.py          ⏳ POR CREAR
│   ├── api.py                   ⏳ POR CREAR
│   └── cli.py                   ⏳ POR CREAR
├── examples/
│   ├── 01_simple_ingestion.py   ⏳ POR CREAR
│   ├── 02_vector_search.py      ⏳ POR CREAR
│   └── 03_graph_traversal.py    ⏳ POR CREAR
├── tests/
│   └── test_ingestion.py        ⏳ POR CREAR
├── docker-compose.yml           ⏳ POR CREAR
├── Dockerfile                   ⏳ POR CREAR
├── requirements.txt             ✅ YA CREADO
└── README.md                    ✅ YA CREADO
```

---

### Paso 2.2: Ejemplo Simple 1 - Ingestion

**Archivo**: `examples/01_simple_ingestion.py`

```python
"""
Ejemplo 1: Ingestar un solo documento Markdown

Objetivo: Entender cómo funciona el pipeline de ingesta
Tiempo: 5 minutos
"""

from triple_persistence.ingestion import TriplePersistencePipeline
from triple_persistence.models import IngestionConfig

# Configuración
config = IngestionConfig(
    project="mi-primer-test",
    paths=["./data/ejemplo.md"],
    neo4j_uri="bolt://localhost:7687",
    neo4j_username="neo4j",
    neo4j_password="password",
    ollama_base_url="http://localhost:11434",
    embedding_model="nomic-embed-text",
    chunk_size=256  # Chunks pequeños para este ejemplo
)

# Pipeline
pipeline = TriplePersistencePipeline(config)

# Ingestar
result = pipeline.ingest_directory(config.paths[0])

# Resultados
print(f"✅ Documentos procesados: {result['documents_processed']}")
print(f"✅ Chunks creados: {result['chunks_created']}")
print(f"✅ Embeddings generados: {result['embeddings_generated']}")
print(f"⏱️ Tiempo: {result['processing_time_seconds']}s")
```

**Ejecutar**:

```powershell
cd C:\proyectos\aleia-melquisedec\packages\triple-persistence

# Crear archivo de ejemplo
New-Item -ItemType Directory -Path "data" -Force
@"
# Mi Primer Documento

Este es un documento de prueba para triple-persistence.

## Sección 1
Contenido de la sección 1 con información relevante.

## Sección 2
Más contenido para generar chunks y embeddings.
"@ | Out-File -FilePath "data\ejemplo.md" -Encoding utf8

# Ejecutar ejemplo
python examples/01_simple_ingestion.py
```

**Output esperado**:
```
✅ Documentos procesados: 1
✅ Chunks creados: 3
✅ Embeddings generados: 3
⏱️ Tiempo: 2.4s
```

---

### Paso 2.3: Ejemplo Simple 2 - Vector Search

**Archivo**: `examples/02_vector_search.py`

```python
"""
Ejemplo 2: Buscar documentos con vector search

Objetivo: Ver cómo funciona la búsqueda semántica
Tiempo: 3 minutos
"""

from triple_persistence.retriever import HybridRetriever
from triple_persistence.models import QueryRequest

# Configuración
retriever = HybridRetriever(
    neo4j_uri="bolt://localhost:7687",
    neo4j_username="neo4j",
    neo4j_password="password",
    ollama_base_url="http://localhost:11434"
)

# Query
request = QueryRequest(
    query="¿Qué es triple-persistence?",
    top_k=3,
    include_graph=False  # Solo vector search
)

# Buscar
results = retriever.query(request)

# Mostrar resultados
print(f"🔍 Query: {request.query}")
print(f"📊 Resultados: {len(results.results)}\n")

for i, result in enumerate(results.results, 1):
    print(f"{i}. {result.document_title}")
    print(f"   Similarity: {result.similarity_score:.3f}")
    print(f"   Excerpt: {result.excerpt[:100]}...")
    print()
```

**Output esperado**:
```
🔍 Query: ¿Qué es triple-persistence?
📊 Resultados: 3

1. Mi Primer Documento
   Similarity: 0.847
   Excerpt: Este es un documento de prueba para triple-persistence...

2. ...
```

---

### Paso 2.4: Ejemplo Simple 3 - Graph Traversal

**Archivo**: `examples/03_graph_traversal.py`

```python
"""
Ejemplo 3: Enriquecer resultados con graph traversal

Objetivo: Ver cómo el grafo mejora los resultados
Tiempo: 5 minutos
"""

from triple_persistence.retriever import HybridRetriever
from triple_persistence.models import QueryRequest

# Configuración
retriever = HybridRetriever(
    neo4j_uri="bolt://localhost:7687",
    neo4j_username="neo4j",
    neo4j_password="password"
)

# Query con graph enrichment
request = QueryRequest(
    query="templates autopoiéticos",
    top_k=5,
    include_graph=True  # ← Activa graph traversal
)

# Buscar
results = retriever.query(request)

# Mostrar resultados enriquecidos
for result in results.results:
    print(f"📄 {result.document_title}")
    print(f"   Similarity: {result.similarity_score:.3f}")

    # Documentos relacionados (via graph)
    if result.related_documents:
        print(f"   🔗 Referencias:")
        for related in result.related_documents:
            print(f"      - {related}")
    print()
```

**Output esperado**:
```
📄 PROPOSITO.md
   Similarity: 0.912
   🔗 Referencias:
      - README.md
      - 010-define/requirements.md

📄 README.md
   Similarity: 0.854
   🔗 Referencias:
      - PROPOSITO.md
```

---

## 🔄 Comparación: GenAI Stack vs LlamaIndex MVP

| Característica | GenAI Stack | LlamaIndex MVP |
|----------------|-------------|----------------|
| **Setup** | 5 min | 1 semana |
| **Apps Incluidas** | 5 (bot, loader, PDF, API, UI) | Solo API |
| **Framework** | LangChain | LlamaIndex |
| **Tests** | ❌ No | ✅ pytest |
| **Arquitectura** | Scripts | Hexagonal |
| **Docs** | Para StackOverflow Q&A | Para research docs |
| **Producción** | ⚠️ Demo-grade | ✅ Production-ready |
| **Customizable** | ⚠️ Hardcoded | ✅ Config-driven |
| **Aprendizaje** | ⚡ Inmediato | 📚 Progresivo |

---

## 🎓 Learning Path (Ruta de Aprendizaje)

### Día 1: GenAI Stack
- ✅ Instalar y configurar
- ✅ Ver Neo4j Browser funcionando
- ✅ Probar chatbot de ejemplo
- ✅ Inspeccionar Cypher queries

### Día 2-3: LlamaIndex Basics
- ⏳ Ejecutar ejemplo 01 (ingestion)
- ⏳ Ejecutar ejemplo 02 (vector search)
- ⏳ Ejecutar ejemplo 03 (graph traversal)
- ⏳ Modificar parámetros y experimentar

### Día 4-5: Implementación
- ⏳ Completar ingestion.py
- ⏳ Completar retriever.py
- ⏳ Crear tests

### Día 6-7: Integración
- ⏳ Ingestar research-autopoietic-template
- ⏳ Validar success criteria
- ⏳ Documentar workflows

---

## 🐛 Troubleshooting (Problemas Comunes)

### Problema 1: Neo4j no inicia

```powershell
# Verificar logs
docker logs genai-stack-database-1

# Error común: Puerto 7687 ocupado
# Solución: Detener Neo4j existente
Get-Process | Where-Object {$_.ProcessName -like "*neo4j*"} | Stop-Process
```

### Problema 2: Ollama no conecta

```powershell
# Verificar Ollama corriendo
ollama list

# Si no responde, reiniciar
# En Windows: Restart Ollama desde system tray

# Verificar puerto
Test-NetConnection -ComputerName localhost -Port 11434
```

### Problema 3: Embeddings muy lentos

```bash
# Solución 1: Usar modelo más pequeño
EMBEDDING_MODEL=all-minilm-l6-v2  # 384 dim vs 768

# Solución 2: Batch processing
chunk_size=128  # Chunks más pequeños
```

### Problema 4: Docker "out of memory"

```powershell
# Aumentar RAM en Docker Desktop
# Settings → Resources → Memory → 8GB mínimo
```

---

## 📚 Recursos Adicionales

### Documentación Oficial
- GenAI Stack: https://github.com/docker/genai-stack
- LlamaIndex: https://docs.llamaindex.ai
- Neo4j Vector: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/
- Ollama: https://ollama.ai/library

### Tutoriales Recomendados
1. Neo4j Cypher Basics: https://neo4j.com/graphacademy/
2. LlamaIndex Tutorials: https://docs.llamaindex.ai/en/stable/getting_started/
3. RAG Architecture: https://www.youtube.com/watch?v=T-D1OfcDW1M

### Papers Relevantes
- GraphRAG (Microsoft Research, 2024)
- Neo4j Vector Index (Neo4j Labs, 2023)

---

## 🎯 Success Criteria

**Has completado exitosamente el quickstart si**:

✅ GenAI Stack:
- [ ] Neo4j Browser abierto y funcionando
- [ ] Chatbot cargando y respondiendo queries
- [ ] Vector search retornando resultados

✅ LlamaIndex MVP:
- [ ] Ejemplo 01 ejecutado correctamente
- [ ] Ejemplo 02 retornando similarity > 0.7
- [ ] Ejemplo 03 mostrando related_documents

✅ Comprensión:
- [ ] Entiendes diferencia entre Graph y Vector
- [ ] Sabes cuándo usar GenAI Stack vs LlamaIndex MVP
- [ ] Puedes explicar Triple-Persistence a un colega

---

**Próximos Pasos**: Ver `mvp-triple-persistence.md` para arquitectura completa

**Ayuda**: Si te atascas, revisar Troubleshooting o consultar documentación oficial
