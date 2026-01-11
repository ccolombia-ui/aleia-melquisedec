# Hypothesis Document

> **DSR Phase**: Problem Identification
> **DAATH-ZEN Rostro**: HYPATIA (Researcher)
> **Version**: v1.0.0 (Initial)
> **Status**: 🔴 TO BE VALIDATED

## 🧪 Hipótesis Central

**La adopción de Neo4j 5.15+ Vector Index unificado (graph + vectors) con LlamaIndex y Ollama embeddings locales, usando arquitectura Hexagonal + DDD, resultará en una solución RAG robusta, testeable y mantenible para MELQUISEDEC, superior a arquitecturas multi-vector-store (Redis/Pinecone) en términos de consistencia transaccional, simplicidad operacional y costo total de propiedad.**

## 🔍 Hipótesis Específicas por RQ

### H1: Consistencia Transaccional (RQ1)

**Hipótesis**: Neo4j permite mantener consistencia ACID entre operaciones de grafo y vector index usando transacciones Cypher nativas, eliminando necesidad de sistemas externos (Redis) y sus problemas de eventual consistency.

**Predicción**:
- Encontraremos código en `neo4j/genai-stack` que demuestra transacciones atómicas CREATE node + CREATE vector entry
- LlamaIndex `Neo4jVectorStore` usará session contexts para garantizar ACID
- Error handling será rollback automático (sin compensating transactions)

**Validación**:
- [ ] ≥3 code examples de transacciones atómicas encontrados
- [ ] Documentación Neo4j confirma ACID guarantees para vector index
- [ ] Comparativa con Redis (eventual consistency) muestra ventaja Neo4j

---

### H2: Chunking Strategies (RQ2)

**Hipótesis**: Semantic chunking (basado en estructura del documento) supera token-based chunking en calidad de retrieval para documentos técnicos (Markdown, code), pero token-based es suficiente para textos planos.

**Predicción**:
- LlamaIndex usará `SentenceSplitter` o `SemanticChunker` por defecto
- Proyectos production-ready tendrán chunk sizes entre 256-1024 tokens con overlap 10-20%
- Metadata preservation será crítico (source, section, category)

**Validación**:
- [ ] Matriz comparativa de ≥3 chunking strategies documentada
- [ ] Benchmarks o case studies encontrados (si existen)
- [ ] Recomendación clara para MELQUISEDEC (estrategia + params)

---

### H3: Arquitectura de Software (RQ3)

**Hipótesis**: Proyectos robustos adoptarán Hexagonal Architecture o Clean Architecture para separar concerns (domain logic vs infrastructure) y facilitar testing.

**Predicción**:
- `neo4j/genai-stack` tendrá estructura layered (backend/services/adapters)
- LlamaIndex core usará abstractions (`BaseVectorStore`, `BaseEmbedding`)
- Dependency injection será patrón común

**Validación**:
- [ ] ≥2 proyectos con arquitectura formal documentada
- [ ] Identificación de ports (interfaces) y adapters (implementations)
- [ ] ADR o design doc justificando arquitectura encontrado

---

### H4: Embeddings Locales vs Cloud (RQ4)

**Hipótesis**: Frameworks maduros abstraerán embedding service detrás de interface común, permitiendo switching entre Ollama (local), OpenAI (cloud), y otros providers sin cambiar domain logic.

**Predicción**:
- LlamaIndex tendrá `BaseEmbedding` interface con métodos: `embed_text()`, `embed_batch()`
- Ollama adapter implementará interface con client HTTP hacia `localhost:11434`
- Configuración será inyectable (env vars, config file)

**Validación**:
- [ ] Interface común `BaseEmbedding` documentada
- [ ] ≥2 adapters implementados (Ollama, OpenAI) analizados
- [ ] Code pattern para switching providers extraído

---

### H5: Testing Strategies (RQ5)

**Hipótesis**: Proyectos maduros usarán testcontainers para integration tests (Neo4j) y mocks deterministas para embeddings, siguiendo test pyramid (70% unit, 20% integration, 10% E2E).

**Predicción**:
- Tests integration usarán `testcontainers-python` con Neo4j image
- Embeddings serán mockeados con vectors deterministas (np.random.seed)
- Coverage target será ≥80% con SonarQube o similar

**Validación**:
- [ ] ≥3 testing patterns identificados en proyectos analizados
- [ ] Fixtures design documentado (testcontainer, mocks)
- [ ] Coverage strategy recomendada basada en evidencia

---

## 🎯 Criterios de Validación General

Para considerar la hipótesis central **VALIDADA**, se requiere:

1. **Evidence-Based**: ≥4 frameworks/proyectos analizados con depth analysis (no solo README)
2. **Code Patterns**: ≥20 code snippets extraídos y ejecutables
3. **Comparative Analysis**: Matriz comparativa completa con recommendation justificada
4. **RQs Answered**: ≥4 de 5 RQs respondidas con evidencia sólida
5. **Hypothesis Adjusted**: Si evidencia contradice hipótesis, ajustar y documentar

---

## 🔄 Versiones de la Hipótesis

| Version | Date | Status | Changes |
|---------|------|--------|---------|
| v1.0.0 | 2026-01-08 | 🔴 Initial | Hipótesis inicial basada en conocimiento previo |
| v1.1.0 | TBD | ⚪ Pending | Ajustes post R1.1-R1.4 (evidencia de genai-stack, LlamaIndex) |
| v2.0.0 | TBD | ⚪ Pending | Validación final post MELQUISEDEC (R1.5) |

---

**Última actualización**: 2026-01-08
**HYPATIA Researcher** - Hipótesis inicial, pendiente validación con evidencia
