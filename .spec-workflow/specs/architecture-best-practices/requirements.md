# Architecture Best Practices v1.0.0 - Requirements

## Overview

Este spec implementa arquitectura óptima para Triple Persistencia MELQUISEDEC basada en análisis profundo de 34 papers académicos, documentación oficial de Neo4j, y código de Obsidian Smart Connections. Resuelve 4 gaps críticos identificados (G1-G4) para establecer fundamentos sólidos antes de desarrollo.

**Premisa clave**: NO hay que migrar nada (no existe implementación previa), solo documentar y crear la arquitectura correcta desde el inicio.

---

## User Stories

### US-1: Como arquitecto, quiero que los vectores embeddings estén en Neo4j (no Redis)
- Para tener queries unificadas (graph + vectors en 1 query)
- Para eliminar complejidad de dual storage
- Para aprovechar Neo4j Vector Index nativo (HNSW)
- **Relacionado**: Gap G1

### US-2: Como desarrollador, quiero un pipeline documentado para procesar documentos
- Para entender cómo Markdown → Chunks → Embeddings → Storage
- Para debugging cuando embeddings no son correctos
- Para onboarding de nuevos contribuidores
- **Relacionado**: Gap G2

### US-3: Como desarrollador, quiero entender el schema de Autopoiesis en Neo4j
- Para consultar la evolución de domains y lessons
- Para extender el schema con nuevos nodos
- Para troubleshooting cuando queries fallan
- **Relacionado**: Gap G3

### US-4: Como architect, quiero benchmarks que validen la arquitectura
- Para tomar decisiones basadas en datos (no opiniones)
- Para comparar vs alternativas (Smart Connections)
- Para detectar regresiones de performance
- **Relacionado**: Gap G4

---

## Functional Requirements

### REQ-1: Neo4j Vector Index (Eliminar Redis para vectores)

**Objetivo**: Usar Neo4j 5.15.0+ native vector index en lugar de dual storage.

**Criterios de aceptación**:
1. ✅ Crear vector index en Neo4j con Cypher:
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
   }
   ```

2. ✅ Actualizar `docker-compose.yml`:
   - Mantener Neo4j con plugins APOC + GDS
   - Mantener Ollama para embeddings locales
   - **NO** incluir Redis para vector store (solo si se usa para otra cosa)

3. ✅ Documentar query pattern:
   ```cypher
   // Query híbrida: graph + vectors en 1 sola query
   MATCH (n:Spec)-[:HAS_ISSUE]->(i:Issue)
   CALL db.index.vector.queryNodes('melquisedec_embeddings', 5, $queryVector)
   YIELD node, score
   WHERE node = n
   RETURN i, score
   ORDER BY score DESC
   ```

**Validación**:
- `SHOW INDEXES` en Neo4j muestra vector index
- `docker ps` **no** muestra Redis container para vectores
- Query de ejemplo retorna resultados con scores

**Priority**: 🔴 **ALTA** - Fundamento arquitectónico

---

### REQ-2: Pipeline Formal de Procesamiento de Documentos

**Objetivo**: Implementar y documentar pipeline LlamaIndex + Semantic Chunking.

**Criterios de aceptación**:
1. ✅ Crear `packages/daath-toolkit/processors/document_pipeline.py` con clase `MELQUISEDECPipeline`:
   - **Fase 1**: Document Loading (SimpleDirectoryReader)
   - **Fase 2**: Statistical Analysis (language detection, complexity score)
   - **Fase 3**: Semantic Chunking (MarkdownNodeParser, 512 tokens, overlap 100)
   - **Fase 4**: Embedding (Ollama qwen3-embedding)
   - **Fase 5**: Storage (Neo4j Vector Index + Knowledge Graph)

2. ✅ Instalar dependencias:
   ```bash
   pip install llama-index llama-index-vector-stores-neo4j llama-index-embeddings-ollama
   ```

3. ✅ Crear documentación `docs/manifiesto/04-implementacion/06-pipeline-document-processing.md`:
   - Diagrama de fases
   - Código de ejemplo
   - Parámetros configurables (chunk_size, overlap, modelo embedding)
   - Troubleshooting común

4. ✅ Integrar con KnowledgeWriter (si existe):
   ```python
   class KnowledgeWriter:
       def __init__(self):
           self.pipeline = MELQUISEDECPipeline()
       
       def write_atomically(self, file_paths: List[str], metadata: Dict):
           index = self.pipeline.process_documents(file_paths, metadata)
           return index
   ```

**Validación**:
- Archivo `document_pipeline.py` existe y tiene clase completa
- Doc `06-pipeline-document-processing.md` tiene ≥400 líneas
- Tests básicos en `packages/daath-toolkit/testing/test_document_pipeline.py` pasan

**Priority**: 🔴 **ALTA** - Sin pipeline no hay consistencia

---

### REQ-3: Actualizar Configuración Docker (Sin Redis para vectores)

**Objetivo**: Actualizar `infrastructure/docker/docker-compose.yml` con configuración correcta.

**Criterios de aceptación**:
1. ✅ Mantener **solo** Neo4j + Ollama:
   ```yaml
   services:
     neo4j:
       image: neo4j:5.15-community
       # ... config con APOC + GDS
     
     ollama:
       image: ollama/ollama:latest
       # ... config
     
     # NO Redis para vectores (a menos que se use para cache/sessions)
   ```

2. ✅ Neo4j environment variables:
   - `NEO4J_PLUGINS=["apoc", "graph-data-science"]`
   - `NEO4J_dbms_memory_heap_max__size=2G` (suficiente para vectors)
   - `NEO4J_dbms_security_procedures_unrestricted=apoc.*,gds.*`

3. ✅ Actualizar `docs/manifiesto/04-implementacion/04-memoria-y-persistencia-triple.md`:
   - Remover referencias a Redis vector store
   - Actualizar diagrams (solo Neo4j + Ollama)
   - Actualizar código de ejemplo (sin redis_client)

**Validación**:
- `docker-compose up -d` inicia solo Neo4j + Ollama
- `docker ps | grep redis` retorna vacío (o Redis para otra cosa, no vectores)
- Doc `04-memoria-y-persistencia-triple.md` no menciona Redis para embeddings

**Priority**: 🟠 **MEDIA** - Dependencia de REQ-1

---

### REQ-4: Documentar Schema de Autopoiesis

**Objetivo**: Explicar el schema Neo4j existente (`tools/setup/neo4j_schema.py`).

**Criterios de aceptación**:
1. ✅ Crear ADR `docs/manifiesto/02-arquitectura/ADR-002-neo4j-unified-architecture.md`:
   - Context: Por qué usar Neo4j para graph + vectors
   - Decision: Arquitectura unificada (no dual storage)
   - Consequences: Ventajas (queries simples) y trade-offs (latencia ligeramente mayor)

2. ✅ Crear doc `docs/manifiesto/02-arquitectura/06-schema-autopoiesis.md`:
   - TL;DR del schema
   - Diagrama Mermaid de nodos y relaciones
   - Descripción de cada nodo: Domain, ResearchInstance, Lesson, PromptType, Output
   - Constraints e índices
   - Queries frecuentes con ejemplos
   - Uso desde Python (`neo4j_schema.py`)

3. ✅ Actualizar README principal con enlace al schema doc

**Validación**:
- Archivos ADR-002 y 06-schema-autopoiesis.md existen
- Doc tiene ≥600 líneas con diagrams + code
- README principal lista estos docs en sección "Arquitectura"

**Priority**: 🟡 **MEDIA** - Documentación importante pero no bloqueante

---

### REQ-5: Suite de Benchmarking

**Objetivo**: Crear framework para validar arquitectura vs alternativas.

**Criterios de aceptación**:
1. ✅ Crear dataset de test:
   ```python
   # packages/daath-toolkit/testing/fixtures/test_notes_100.json
   {
       "notes": [
           {
               "id": "note-001",
               "content": "...",
               "ground_truth_connections": ["note-045", "note-078"]
           },
           # ... 99 more
       ]
   }
   ```

2. ✅ Implementar `benchmark_vs_smart_connections.py`:
   - Clase `ConnectionsBenchmark`
   - Métricas: Precision@k, Recall@k, MRR (Mean Reciprocal Rank), Latency
   - Comparación: MELQUISEDEC (embeddings only) vs MELQUISEDEC (graph + embeddings) vs Smart Connections (baseline simulado)

3. ✅ Ejecutar benchmarks y documentar resultados:
   ```bash
   pytest packages/daath-toolkit/testing/benchmark_vs_smart_connections.py --benchmark
   ```

4. ✅ Crear doc `docs/manifiesto/04-implementacion/07-benchmark-results.md`:
   - Tabla de resultados
   - Interpretación (MELQUISEDEC graph+embeddings debe superar Smart Connections)
   - Gráficos (opcional)

**Validación**:
- Archivo `benchmark_vs_smart_connections.py` existe
- Dataset `test_notes_100.json` tiene 100 notas con ground truth
- Benchmark ejecuta en <5 minutos
- Doc con resultados muestra Precision@10 ≥ 0.75 para MELQUISEDEC

**Priority**: 🟢 **BAJA** - Validación útil pero no crítica

---

### REQ-6: Actualizar Documentos Existentes

**Objetivo**: Actualizar docs que referencian arquitectura antigua.

**Archivos a actualizar**:
1. ✅ `docs/manifiesto/04-implementacion/04-memoria-y-persistencia-triple.md`:
   - Remover secciones de Redis para vectores
   - Actualizar diagramas (solo Neo4j + Ollama)
   - Actualizar código Python (eliminar `redis_client.json()`)

2. ✅ `docs/manifiesto/04-implementacion/05-analisis-arquitectura-best-practices.md`:
   - Marcar G1 (Dual Vector Storage) como **RESUELTO**
   - Marcar G2 (Undocumented Pipeline) como **RESUELTO**
   - Agregar sección "Implementation Status" al final

3. ✅ `docs/guides/configuracion-completa.md` (si existe):
   - Actualizar pasos de setup (sin Redis para vectores)
   - Actualizar docker-compose commands

4. ✅ `docs/guides/quick-reference.md` (si existe):
   - Actualizar quick start (docker-compose con solo Neo4j + Ollama)

**Validación**:
- Grep search `grep -r "Redis.*vector\|vector.*Redis" docs/` retorna 0 resultados (excepto en contexto histórico)
- Docs mencionan "Neo4j Vector Index nativo"

**Priority**: 🟠 **MEDIA** - Evita confusión

---

## Non-Functional Requirements

### NFR-1: Performance
- Neo4j vector queries deben responder en <100ms para k=10
- Pipeline debe procesar 100 documentos en <2 minutos
- Benchmarks deben ejecutar en <5 minutos

### NFR-2: Maintainability
- Código debe tener docstrings completos (Google style)
- Pipeline debe ser extensible (fácil agregar nuevas fases)
- Configuración debe ser centralizada (no hardcoded)

### NFR-3: Documentación
- Cada doc debe tener TL;DR al inicio
- Diagramas Mermaid para arquitectura
- Code examples ejecutables (no pseudocódigo)

### NFR-4: Compatibility
- Python 3.11+
- Neo4j 5.15+
- LlamaIndex 0.10.0+

---

## Priority Order

1. **🔴 Alta**: REQ-1 (Neo4j vectors), REQ-2 (Pipeline), REQ-3 (Docker) - Fundamentos
2. **🟠 Media**: REQ-4 (Schema docs), REQ-6 (Update docs) - Documentación crítica
3. **🟢 Baja**: REQ-5 (Benchmarks) - Validación nice-to-have

---

## Success Criteria

- [ ] Todos los REQs 1-4 implementados y validados
- [ ] REQ-5 implementado (benchmarks) al menos con baseline
- [ ] REQ-6 completado (docs actualizados)
- [ ] Todos los NFRs cumplidos
- [ ] CHANGELOG.md actualizado con v1.0.0
- [ ] Dashboard spec-workflow muestra 100% completado

---

## Out of Scope

❌ **NO incluido en este spec**:
- Implementación de UI/dashboard (futuro spec)
- Integración con KETER (spec separado existente)
- Tests unitarios exhaustivos (solo benchmarks básicos)
- Performance tuning avanzado (solo configuración inicial)
- Multimodal embeddings (solo text por ahora)

---

## Dependencies

- **Spec previo**: `monorepo-improvements` (debe estar completo)
- **Docs existentes**: `05-analisis-arquitectura-best-practices.md` (referencia de investigación)
- **Código existente**: `tools/setup/neo4j_schema.py` (ya existe, no modificar)

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Neo4j vector index no rinde | ALTO | Benchmark early, comparar con Redis si es necesario |
| LlamaIndex breaking changes | MEDIO | Pin versiones en requirements.txt |
| Semantic chunking produce chunks muy grandes | MEDIO | Tuning de chunk_size (512, 768, 1024) |
| Benchmarks no son representativos | BAJO | Validar dataset con expertos |

---

**Versión**: 1.0.0
**Última actualización**: 2026-01-08
**Rostro autor**: SALOMON (Architect)
