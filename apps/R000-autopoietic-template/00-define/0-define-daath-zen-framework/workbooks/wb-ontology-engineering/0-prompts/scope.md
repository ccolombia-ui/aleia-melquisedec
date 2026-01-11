# Alcance: Investigación de Ingeniería Ontológica

## In Scope (Incluido ✅)

### Metodologías de Ingeniería Ontológica
- **METHONTOLOGY** (Fernández-López et al. 1997)
  - Fases: especificación, conceptualización, formalización, implementación, mantenimiento
  - Actividades de soporte: knowledge acquisition, integration, evaluation, documentation
- **NeOn Methodology** (Suárez-Figueroa et al. 2012)
  - 9 escenarios de desarrollo ontológico
  - Reutilización de recursos ontológicos (ORSD)
  - Collaborative ontology engineering
- **ISO 25964-1:2011**
  - Tesauros monolingües y multilingües
  - Interoperabilidad con ontologías
  - Estándares de mapeo semántico

### Estándares de Web Semántica (W3C)
- **OWL 2** (Web Ontology Language)
  - OWL 2 Full (máxima expresividad)
  - OWL 2 DL (Description Logic - decidible)
  - OWL 2 EL (Existential Logic - eficiente para razonamiento)
  - OWL 2 QL (Query Language - optimizado para consultas)
  - OWL 2 RL (Rule Language - basado en reglas)
- **RDF 1.1** (Resource Description Framework)
  - Modelo de tripletas (subject-predicate-object)
  - RDF Schema (vocabulario básico)
- **SPARQL 1.1**
  - Lenguaje de consulta para grafos RDF
  - Federación de queries
- **SWRL** (Semantic Web Rule Language)
  - Reglas de inferencia basadas en Horn clauses

### Herramientas de Modelado Ontológico
- **Protégé** (Stanford) - Editor visual de ontologías OWL
- **OntoGraf** (plugin Protégé) - Visualización de grafos ontológicos
- **WebVOWL** - Visualización interactiva de ontologías en web
- **Apache Jena** - Framework Java para RDF y OWL

### Reasoners OWL
- **HermiT** - Reasoner OWL 2 DL basado en hypertableau
- **Pellet** - Reasoner OWL 2 con soporte SWRL
- **ELK** - Reasoner OWL 2 EL altamente eficiente
- **Fact++** - Reasoner OWL DL optimizado

### Integración con Arquitectura ALEIA-MELQUISEDEC
- **Neo4j como Triple Store**
  - Modelado de tripletas RDF (subject-predicate-object)
  - Neosemantics (n10s) para importar/exportar RDF
  - Cypher queries para traversal semántico
- **Redis para Caché de Inferencias**
  - Caché de resultados de reasoners OWL
  - Índices de subsunción (class hierarchies)
  - TTL para invalidación de caché
- **Elasticsearch para Búsqueda Semántica**
  - Embeddings de conceptos ontológicos
  - Búsqueda por similitud semántica
  - Análisis de co-ocurrencias de conceptos

### Puentes Conceptuales con DDD
- Mapeo: **Bounded Context ↔ Ontology**
- Mapeo: **Entity/Value Object ↔ Class/Datatype Property**
- Mapeo: **Aggregate ↔ OWL Restriction**
- Mapeo: **Context Map ↔ Ontology Alignment**
- Mapeo: **Ubiquitous Language ↔ Controlled Vocabulary**
- Mapeo: **Repository ↔ SPARQL Endpoint**

---

## Out of Scope (Excluido ❌)

### Implementación Completa de Herramientas
- ❌ Desarrollo de editor ontológico custom (usar Protégé existente)
- ❌ Implementación de reasoner desde cero (usar HermiT/Pellet/ELK)
- ❌ IDE completo para ingeniería ontológica

### Aprendizaje Automático de Ontologías
- ❌ Ontology learning desde corpus de texto (NLP avanzado)
- ❌ Automatic ontology alignment con ML
- ❌ Concept drift detection automático
- ❌ Generación de ontologías por GPT/LLMs (fuera de alcance inicial)

### Benchmarking Exhaustivo
- ❌ Performance testing exhaustivo de reasoners (solo comparativa básica)
- ❌ Scalability tests con millones de tripletas
- ❌ Benchmarks OWLAPI vs Jena vs RDF4J (solo overview)

### Otras Capas de Persistencia
- ❌ Bases de datos relacionales (PostgreSQL, MySQL)
- ❌ Bases de datos documentales (MongoDB, CouchDB)
- ❌ Bases de datos columnares (Cassandra, HBase)

### Ontologías de Dominio Específico Externas
- ❌ Ontologías médicas (SNOMED CT, UMLS)
- ❌ Ontologías financieras (FIBO)
- ❌ Ontologías geoespaciales (GeoNames)
- ❌ Ontologías científicas (ChEBI, Gene Ontology)

**Justificación:** ALEIA-MELQUISEDEC es de propósito general para gestión del conocimiento. Ontologías de dominio específico pueden integrarse posteriormente mediante owl:imports.

### Lenguajes de Ontologías Alternativos
- ❌ KIF (Knowledge Interchange Format) - obsoleto
- ❌ CycL (Cyc Knowledge Base) - propietario
- ❌ OKBC (Open Knowledge Base Connectivity) - descontinuado

**Justificación:** OWL 2 es estándar W3C maduro y ampliamente adoptado.

---

## Assumptions (Supuestos)

### Conocimiento Previo
1. **Lector tiene familiaridad con Domain-Driven Design** (Bounded Context, Entities, Aggregates)
2. **Lector entiende bases de grafos** (nodos, relaciones, traversal)
3. **Lector conoce sintaxis básica de Neo4j Cypher**
4. **Lector comprende arquitectura Triple Persistencia** (Neo4j + Redis + Elasticsearch)

### Tecnología
5. **Neo4j 5.x es target platform** (soporte para neosemantics)
6. **Redis 7.x es target platform** (soporte para RediSearch y RedisGraph si es necesario)
7. **Elasticsearch 8.x es target platform** (soporte para vector search)

### Estándares
8. **OWL 2 DL es el perfil target** (balance expresividad/decidibilidad)
9. **RDF 1.1 es el formato de serialización** (Turtle, JSON-LD, RDF/XML)
10. **SPARQL 1.1 es el lenguaje de consulta** (aunque se usará Cypher en Neo4j)

### Proceso
11. **Metodología METHONTOLOGY es baseline** (NeOn como complemento)
12. **Protégé es herramienta de modelado** (editor visual estándar)
13. **HermiT es reasoner por defecto** (OWL 2 DL completo)

---

## Constraints (Restricciones)

### Tiempo
1. **Duración total: 6 días (48 horas efectivas)**
   - No se pueden extender plazos sin aprobación
   - Buffer de 4 horas incluido para imprevistos

### Recursos
2. **8-10 fuentes académicas máximo** (limitación de tiempo de lectura)
3. **No acceso a papers pagados** (solo open access y estándares públicos)
4. **Sin presupuesto para herramientas comerciales** (solo open source)

### Alcance Técnico
5. **No implementación de código funcional** (solo especificaciones y modelos)
6. **No migración de datos existentes** (solo diseño de arquitectura)
7. **No integración con sistemas legacy externos**

### Idioma
8. **Contenido del workbook en español** (metadata, preguntas, atómicos, síntesis)
9. **Fuentes primarias en inglés** (estándares ISO, W3C en inglés original)
10. **SPECIFICATION.yaml en inglés** (estándar técnico internacional)

---

## Dependencies (Dependencias)

### Conocimiento Previo Requerido
- ✅ **LESSON-000-004**: Baseline Analysis (metodologías validadas)
- ✅ **LESSON-000-005**: Template Migration Strategy (estructura workbook)
- ✅ **Workbook DDD** (Task-000-005) - Para mapeo conceptual DDD ↔ Ontology
- ⏳ **Workbook IMRAD** (Tasks 000-006 a 000-010) - Opcional, para formato publicación

### Herramientas Disponibles
- ✅ **Neo4j Desktop** instalado (con neosemantics plugin)
- ✅ **Python 3.11+** con bibliotecas (rdflib, owlready2)
- ✅ **Validation scripts** (validate-academic-research.py, validate-metadata.py)

### Infraestructura
- ✅ **Git repository** configurado (branch feature/spec-001-implementation)
- ✅ **MCP servers** activos (memory, neo4j, filesystem)

---

## Success Criteria (Criterios de Éxito)

### Cuantitativos
1. **8-10 fuentes documentadas** en `1-literature/`
   - Al menos 3 estándares primarios (ISO 25964-1, W3C OWL 2, W3C RDF 1.1)
   - Al menos 2 papers seminales (Gruber 1993, Fernández-López 1997)
   - Al menos 3 libros/capítulos de referencia
2. **12+ conceptos atómicos** en `3-atomics/`
   - Nomenclatura correcta: `atomic-XXX-{concepto}.md`
   - Cada atómico: 150-300 palabras
   - Cada atómico: 2-3 ejemplos (incluyendo contexto ALEIA)
3. **4-5 temas analizados** en `2-analysis/`
   - Cada tema referencia 2-3+ fuentes
   - Análisis comparativo incluido
4. **5-7 pasos metodológicos** en `3-steps/`
   - Cada paso: metadata completa, prerequisites, procedure, deliverables, validation
5. **3-5 diagramas Mermaid** en `4-canvas/`
   - workflow-overview.md
   - concept-map.md
   - step-dependencies.md
   - (opcionales: data-flow.md, timeline-gantt.md)
6. **1-2 mappings DDD ↔ Ontology** en `5-analysis-connection/`
   - mapping-ddd-to-ontology.md
   - matrix-equivalences-ddd-owl.md
7. **SPECIFICATION.yaml completo** (400-600 líneas) en `6-outputs/`
   - Todas las secciones presentes
   - Valid YAML (yamllint sin errores)
   - Todos los conceptos cross-referenciados
8. **ROADMAP.md** con plan 3 fases en `6-outputs/`
9. **Literatura review final** (2000-3000 palabras) en `6-outputs/`

### Cualitativos
10. **Todas las preguntas P1-P7 respondidas** con evidencia de fuentes
11. **Mapeo DDD ↔ Ontology justificado** con ejemplos ALEIA
12. **Validaciones pasadas** (validate-academic-research.py, validate-metadata.py)
13. **Cross-referencias completas** (atomics ↔ sources ↔ themes ↔ steps)
14. **Diagramas renders correctamente** en Markdown preview
15. **Documentación clara y accionable** (un desarrollador puede implementar siguiendo SPECIFICATION.yaml)

---

## Risks and Mitigations (Riesgos y Mitigaciones)

### Riesgo 1: Fuentes no accesibles (papers pagados)
**Probabilidad:** MEDIA
**Impacto:** ALTO
**Mitigación:** Priorizar estándares públicos (ISO accesible vía universidades, W3C gratis), usar ResearchGate/arXiv para preprints, contactar autores para PDFs.

### Riesgo 2: Complejidad de OWL 2 DL excede tiempo disponible
**Probabilidad:** MEDIA
**Impacto:** MEDIO
**Mitigación:** Enfocarse en OWL 2 Primer (tutorial), no leer especificación formal completa. Extraer conceptos esenciales solo.

### Riesgo 3: Neo4j neosemantics no soporta OWL 2 completo
**Probabilidad:** ALTA (conocida - n10s soporta RDF/RDFS, OWL básico)
**Impacto:** MEDIO
**Mitigación:** Documentar limitaciones claramente. Proponer arquitectura híbrida (Neo4j + Apache Jena para razonamiento OWL 2).

### Riesgo 4: Mapeo DDD ↔ Ontology ambiguo en algunos patrones
**Probabilidad:** MEDIA
**Impacto:** MEDIO
**Mitigación:** Documentar ambigüedades explícitamente. Proponer múltiples opciones cuando no hay mapeo 1:1. Incluir ejemplos concretos de ALEIA.

---

**Mantenido por:** HYPATIA (Research Lead)
**Revisado por:** MORPHEUS (Validation)
**Aprobado por:** Usuario (2026-01-11)
**Versión:** 1.0
**Última Actualización:** 2026-01-11
