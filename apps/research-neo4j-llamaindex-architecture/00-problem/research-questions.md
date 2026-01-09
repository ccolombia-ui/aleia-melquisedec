# Research Questions (RQs)

> **DSR Phase**: Problem Identification
> **DAATH-ZEN Rostro**: HYPATIA (Researcher)
> **Status**: 🔴 IN PROGRESS

## 🎯 Research Questions Principales

### RQ1: Consistencia Transaccional Graph ↔ Vector Index

**Pregunta**: ¿Cómo mantienen consistencia transaccional proyectos existentes entre Graph y Vector Index en Neo4j?

**Hipótesis Inicial**: Usan transacciones Cypher nativas para atomicidad (CREATE node + CREATE vector index entry en misma transacción).

**Investigación Requerida**:
- Analizar código de `neo4j/genai-stack`
- Revisar implementación `LlamaIndex Neo4jVectorStore`
- Buscar error handling patterns (rollback, retry)

**Success Criteria**:
- [ ] ≥3 code examples de sincronización transaccional
- [ ] Identificar estrategias de error handling
- [ ] Contrastar hipótesis con evidencia

---

### RQ2: Patrones de Chunking Efectivos

**Pregunta**: ¿Cuáles son los patrones de chunking más efectivos en proyectos RAG production-ready?

**Hipótesis Inicial**: Semantic chunking > token-based chunking para calidad de retrieval.

**Investigación Requerida**:
- Comparar chunking strategies en LlamaIndex, Haystack, LangChain
- Analizar trade-offs: chunk size vs overlap vs semantic coherence
- Buscar benchmarks o case studies

**Success Criteria**:
- [ ] Matriz comparativa de chunking strategies (≥3)
- [ ] Recomendación basada en evidencia (chunk size, overlap, strategy)
- [ ] Code patterns extraídos (≥5)

---

### RQ3: Arquitectura de Software Robusta

**Pregunta**: ¿Qué arquitectura de software usan proyectos robustos (Hexagonal, Clean, Layered)?

**Hipótesis Inicial**: Hexagonal Architecture por dependency inversion y testability.

**Investigación Requerida**:
- Analizar estructura de `neo4j/genai-stack` (¿layered, modular, monolith?)
- Revisar arquitectura de LlamaIndex core (abstractions, interfaces)
- Buscar ADRs o design docs en proyectos open source

**Success Criteria**:
- [ ] ≥3 proyectos analizados con arquitectura documentada
- [ ] Identificar patterns: ports/adapters, dependency injection, abstractions
- [ ] Justificación para adoptar Hexagonal Architecture

---

### RQ4: Integración Embeddings Locales vs Cloud

**Pregunta**: ¿Cómo integran embeddings locales (Ollama) vs cloud (OpenAI) los frameworks?

**Hipótesis Inicial**: Adapter pattern con interface común (EmbeddingServicePort).

**Investigación Requerida**:
- Revisar LlamaIndex `BaseEmbedding` interface
- Analizar Ollama integration en genai-stack
- Comparar con OpenAI embeddings adapter

**Success Criteria**:
- [ ] Interface común identificada (method signatures)
- [ ] ≥2 adapters implementados (Ollama, OpenAI)
- [ ] Code patterns para switching entre providers

---

### RQ5: Estrategias de Testing

**Pregunta**: ¿Qué estrategias de testing usan proyectos maduros (testcontainers, mocks)?

**Hipótesis Inicial**: Testcontainers para integration tests (Neo4j), mocks para embeddings (deterministic).

**Investigación Requerida**:
- Buscar tests en `neo4j/genai-stack`
- Revisar testing approach en LlamaIndex
- Analizar fixtures y test helpers

**Success Criteria**:
- [ ] ≥3 testing patterns identificados
- [ ] Fixtures design documentado (Neo4j testcontainer, Ollama mock)
- [ ] Coverage strategy recomendada (unit/integration/E2E ratio)

---

## 📊 RQs Status Summary

| RQ | Status | Evidence Gathered | Hypothesis Validated? |
|----|--------|-------------------|----------------------|
| RQ1 | 🔴 Investigating | 0/3 examples | ⚪ Pending |
| RQ2 | ⚪ Pending | 0/3 strategies | ⚪ Pending |
| RQ3 | ⚪ Pending | 0/3 projects | ⚪ Pending |
| RQ4 | ⚪ Pending | 0/2 adapters | ⚪ Pending |
| RQ5 | ⚪ Pending | 0/3 patterns | ⚪ Pending |

---

**Última actualización**: 2026-01-08
**HYPATIA Researcher** - Phase 1: Problem Identification
