# Preguntas de Investigación: Ingeniería Ontológica

## P1: ¿Cuáles son los fundamentos de la ingeniería ontológica? [CRÍTICA]

**Subpreguntas:**
- P1.1: ¿Cómo se define formalmente una "ontología" en la literatura? (Gruber 1993, ISO 25964-1)
- P1.2: ¿Cuáles son los componentes esenciales de una ontología? (clases, propiedades, axiomas, instancias)
- P1.3: ¿Cómo se diferencian las ontologías de las taxonomías y tesauros?
- P1.4: ¿Qué son los niveles de compromiso ontológico? (conceptual, lógico, implementacional)

**Importancia:** CRÍTICA - Fundamento para todas las preguntas posteriores. Sin comprender qué es una ontología, no podemos aplicar metodologías ontológicas.

**Horas Estimadas:** 6 horas
- 2h: Leer ISO 25964-1 (secciones relevantes)
- 2h: Leer Gruber 1993 + Noy & McGuinness 2001
- 2h: Extraer 4-5 atómicos (ontology, class, property, axiom, instance)

**Fuentes Necesarias:**
- ISO 25964-1:2011 (Thesauri and interoperability)
- Gruber, T. (1993): "A Translation Approach to Portable Ontology Specifications"
- Noy, N. & McGuinness, D. (2001): "Ontology Development 101"
- W3C OWL 2 Primer (2012) - Sección "Ontologies"

**Entregables:**
- `1-literature/iso-25964-1-thesauri.md`
- `1-literature/gruber-1993-ontology-definition.md`
- `1-literature/noy-mcguinness-2001-ontology-101.md`
- `3-atomics/atomic-001-ontology.md`
- `3-atomics/atomic-002-class.md`
- `3-atomics/atomic-003-property.md`
- `3-atomics/atomic-004-axiom.md`

---

## P2: ¿Qué metodologías existen para desarrollar ontologías? [ALTA]

**Subpreguntas:**
- P2.1: ¿Cuáles son las fases de METHONTOLOGY? (especificación, conceptualización, formalización, implementación, mantenimiento)
- P2.2: ¿Qué es la metodología NeOn y cuándo usarla? (9 escenarios de desarrollo)
- P2.3: ¿Cómo se comparan estas metodologías? (fortalezas, debilidades, casos de uso)
- P2.4: ¿Qué guías prácticas existen? (Noy & McGuinness 101 steps)

**Importancia:** ALTA - Necesitamos metodología sistemática para construir ontologías en ALEIA-MELQUISEDEC, no solo conceptos teóricos.

**Horas Estimadas:** 4 horas
- 2h: Leer Fernández-López 1997 (METHONTOLOGY)
- 1h: Revisar NeOn Methodology (escenarios principales)
- 1h: Extraer 2-3 atómicos metodológicos

**Fuentes Necesarias:**
- Fernández-López, M. et al. (1997): "METHONTOLOGY: From Ontological Art Towards Ontological Engineering"
- Suárez-Figueroa, M.C. et al. (2012): "The NeOn Methodology for Ontology Engineering" (capítulo de handbook)
- Noy & McGuinness (2001) - Sección "Steps in Ontology Development"

**Entregables:**
- `1-literature/fernandez-lopez-1997-methontology.md`
- `1-literature/neon-methodology-overview.md`
- `3-atomics/atomic-005-methontology.md`
- `3-atomics/atomic-006-neon-methodology.md`
- `3-steps/step-001-specification-phase.md`
- `3-steps/step-002-conceptualization-phase.md`
- `3-steps/step-003-formalization-phase.md`

---

## P3: ¿Qué estándares de Web Semántica son relevantes? [CRÍTICA]

**Subpreguntas:**
- P3.1: ¿Qué es OWL 2 y qué perfiles tiene? (Full, DL, EL, QL, RL)
- P3.2: ¿Cómo se relacionan RDF, RDFS y OWL? (niveles de expresividad)
- P3.3: ¿Qué es SPARQL y cómo se usa para consultar ontologías?
- P3.4: ¿Qué son las Description Logics y por qué importan?

**Importancia:** CRÍTICA - Sin estándares W3C, no podemos interoperar con herramientas semánticas ni garantizar consistencia.

**Horas Estimadas:** 4 horas
- 2h: Leer W3C OWL 2 Primer (secciones core)
- 1h: Revisar RDF 1.1 Primer
- 1h: Extraer 3-4 atómicos sobre estándares

**Fuentes Necesarias:**
- W3C OWL 2 Web Ontology Language Primer (2012)
- W3C RDF 1.1 Primer (2014)
- W3C SPARQL 1.1 Query Language (2013)
- Baader, F. et al. (2003): "The Description Logic Handbook" (capítulos introductorios)

**Entregables:**
- `1-literature/w3c-owl2-primer.md`
- `1-literature/w3c-rdf-primer.md`
- `3-atomics/atomic-007-owl-2.md`
- `3-atomics/atomic-008-rdf.md`
- `3-atomics/atomic-009-description-logic.md`
- `3-atomics/atomic-010-sparql.md`

---

## P4: ¿Cómo funciona el razonamiento ontológico? [MEDIA]

**Subpreguntas:**
- P4.1: ¿Qué es un reasoner OWL y qué tipos hay? (HermiT, Pellet, ELK)
- P4.2: ¿Qué inferencias puede realizar un reasoner? (subsunción, instanciación, satisfiabilidad)
- P4.3: ¿Cuáles son las limitaciones computacionales? (decidibilidad, complejidad)
- P4.4: ¿Cómo se integran reasoners con Neo4j?

**Importancia:** MEDIA - Importante para validación y enriquecimiento automático, pero no es bloqueante para versión inicial.

**Horas Estimadas:** 3 horas
- 1h: Leer sobre reasoners OWL (comparativa)
- 1h: Revisar tipos de inferencias (papers, OWL 2 Primer)
- 1h: Extraer 2 atómicos sobre razonamiento

**Fuentes Necesarias:**
- Shearer, R. et al. (2008): "HermiT: A Highly-Efficient OWL Reasoner"
- Sirin, E. et al. (2007): "Pellet: A Practical OWL-DL Reasoner"
- Kazakov, Y. et al. (2014): "The Incredible ELK" (OWL EL reasoner)
- OWL 2 Primer - Sección "Reasoning"

**Entregables:**
- `1-literature/owl-reasoners-comparison.md`
- `3-atomics/atomic-011-reasoning.md`
- `3-atomics/atomic-012-reasoner.md`

---

## P5: ¿Cómo se mapean conceptos DDD a ontologías? [ALTA]

**Subpreguntas:**
- P5.1: ¿Bounded Context equivale a Ontology?
- P5.2: ¿Entity/Value Object corresponden a Class/Datatype Property?
- P5.3: ¿Aggregates se modelan como OWL Restrictions?
- P5.4: ¿Context Map equivale a Ontology Alignment/Merging?
- P5.5: ¿Ubiquitous Language es vocabulario controlado (tesauro)?

**Importancia:** ALTA - Puente esencial entre prácticas DDD existentes en ALEIA y fundamentos ontológicos formales.

**Horas Estimadas:** 4 horas
- 2h: Revisar patrones DDD (Evans 2003, Vernon 2013)
- 1h: Analizar equivalencias conceptuales
- 1h: Crear matriz de mapeo

**Fuentes Necesarias:**
- Evans, E. (2003): "Domain-Driven Design: Tackling Complexity..." (capítulos Strategic Design)
- Vernon, V. (2013): "Implementing Domain-Driven Design" (capítulos sobre Bounded Contexts)
- Allemang & Hendler (2011): "Semantic Web for the Working Ontologist" (sección sobre domain modeling)

**Entregables:**
- `1-literature/evans-2003-ddd-strategic.md`
- `5-analysis-connection/mapping-ddd-to-ontology.md`
- `5-analysis-connection/matrix-equivalences-ddd-owl.md`

---

## P6: ¿Cómo se integran ontologías con Triple Persistencia? [ALTA]

**Subpreguntas:**
- P6.1: ¿Neo4j puede actuar como triple store? (subject-predicate-object)
- P6.2: ¿Cómo se modela OWL 2 en Neo4j? (nodos Class, relaciones rdfs:subClassOf)
- P6.3: ¿Redis puede cachear inferencias ontológicas?
- P6.4: ¿Elasticsearch puede indexar embeddings semánticos de conceptos?
- P6.5: ¿Qué herramientas existen para convertir OWL → Neo4j?

**Importancia:** ALTA - Implementación práctica en arquitectura existente de ALEIA.

**Horas Estimadas:** 5 horas
- 2h: Investigar Neo4j como RDF store (neosemantics, APOC)
- 1h: Revisar caché de inferencias en Redis
- 1h: Explorar embeddings semánticos
- 1h: Documentar pipeline de integración

**Fuentes Necesarias:**
- Neo4j Neosemantics (n10s) documentation
- Barrasa, J. (2020): "Knowledge Graphs: Data in Context for Responsive Businesses"
- Papers sobre RDF storage en graph databases
- Documentación de Apache Jena (framework RDF/OWL)

**Entregables:**
- `1-literature/neo4j-neosemantics-rdf.md`
- `1-literature/knowledge-graphs-barrasa.md`
- `4-canvas/workflow-owl-to-neo4j.md`
- `4-canvas/diagram-triple-persistence-integration.md`
- `3-steps/step-005-implement-neo4j-ontology.md`

---

## P7: ¿Cómo se evoluciona y mantiene una ontología? [MEDIA]

**Subpreguntas:**
- P7.1: ¿Qué estrategias de versionado existen? (backward-compatible changes)
- P7.2: ¿Cómo se migrdan datos ante cambios ontológicos?
- P7.3: ¿Qué testing se aplica a ontologías? (unit tests, consistency checks)
- P7.4: ¿Cómo se documenta una ontología? (annotations, comments, examples)

**Importancia:** MEDIA - Crucial para mantenimiento a largo plazo, pero no bloqueante para versión inicial.

**Horas Estimadas:** 2 horas
- 1h: Revisar best practices de versionado (papers)
- 1h: Documentar estrategias de migración y testing

**Fuentes Necesarias:**
- Hartung, M. et al. (2013): "Schema and Ontology Matching" (capítulo sobre evolution)
- Noy, N. et al. (2006): "Ontology Versioning and Change Detection on the Web"
- OWL 2 Primer - Sección "Annotations"

**Entregables:**
- `1-literature/ontology-evolution-best-practices.md`
- `3-steps/step-006-maintain-and-evolve.md`

---

## Estrategia de Ejecución

### Priorización por Criticidad

**Día 1 (8h):**
- P1: Fundamentos (6h) → 4 fuentes, 4 atómicos
- P3: Estándares Web Semántica - Inicio (2h) → 1 fuente

**Día 2 (8h):**
- P3: Estándares - Completar (2h) → 2 fuentes, 4 atómicos
- P2: Metodologías (4h) → 2 fuentes, 3 atómicos, 3 steps
- P5: Puentes DDD - Inicio (2h) → 1 fuente

**Día 3 (8h):**
- P5: Puentes DDD - Completar (2h) → 2 mappings
- P6: Triple Persistencia (5h) → 2 fuentes, 2 diagramas, 1 step
- P4: Razonamiento - Inicio (1h)

**Día 4 (8h):**
- P4: Razonamiento - Completar (2h) → 1 fuente, 2 atómicos
- P7: Evolución (2h) → 1 fuente, 1 step
- Síntesis (4h) → 4-artifacts/synthesis-ontology-engineering.md

**Día 5-6 (16h):**
- Crear SPECIFICATION.yaml (6h)
- Crear ROADMAP.md (1h)
- Crear literatura review final (4h)
- Validar workbook (2h)
- Buffer / ajustes (3h)

### Horas Totales Estimadas

| Pregunta | Horas | Prioridad | Día |
|----------|-------|-----------|-----|
| P1 | 6h | CRÍTICA | 1 |
| P3 | 4h | CRÍTICA | 1-2 |
| P2 | 4h | ALTA | 2 |
| P5 | 4h | ALTA | 2-3 |
| P6 | 5h | ALTA | 3 |
| P4 | 3h | MEDIA | 3-4 |
| P7 | 2h | MEDIA | 4 |
| **Subtotal Investigación** | **28h** | | **Días 1-4** |
| Síntesis + SPEC + Review | 16h | | Días 4-6 |
| Validación + Buffer | 4h | | Día 6 |
| **TOTAL** | **48h** | | **6 días** |

---

**Mantenido por:** HYPATIA (Research Lead)
**Validado por:** MORPHEUS
**Última Actualización:** 2026-01-11
