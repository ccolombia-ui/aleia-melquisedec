# LESSON-002: Arquitectura de Workbooks - De IMRAD Secuencial a Workbooks por Artefacto

**Fecha**: 2026-01-10
**Contexto**: SPEC-001 Phase 2 - Research Foundation
**Lesson ID**: LESSON-002
**Severity**: 🔴 CRÍTICA (cambio arquitectónico fundamental)

---

## 📋 Resumen Ejecutivo

**Error Detectado**: Propuse workbooks organizados por FASES IMRAD (01-introduction/, 02-methods/, etc.) cuando debían organizarse por **ARTEFACTOS** del spec-workflow (workbook-product-md/, workbook-requirements-md/, etc.).

**Impacto**: Esta confusión habría creado UN workbook gigante para toda la investigación en lugar de workbooks autocontenidos por cada artefacto, violando separation of concerns y el principio de bounded contexts de DDD.

**Corrección**: Reestructurar Phase 2 con 5 workbooks autocontenidos (uno por artefacto), cada uno con estructura epistemológica completa 1-6.

---

## 🔍 Problema Identificado

### Error Arquitectónico Original

**Lo que propuse** ❌:
```
_melquisedec/domain/workbooks/spec-001-prototype/
├── 01-introduction/            # Fase IMRAD como folder
│   ├── introduction.md
│   ├── literature/
│   └── atomic/
├── 02-methods/                 # Fase IMRAD como folder
└── ... (8 folders IMRAD)
```

**Problema**: Trataba SPEC-001 como UN SOLO paper IMRAD gigante, sin separación por artefacto.

### Arquitectura Correcta

**Lo correcto** ✅:
```
_melquisedec/domain/workbooks/spec-001-prototype/
├── workbook-product-md/              # UN workbook por ARTEFACTO
│   ├── 1-literature/                 # Fuentes primarias
│   │   ├── book/
│   │   ├── paper/
│   │   ├── framework/
│   │   └── library/
│   ├── 2-analysis/                   # Análisis + síntesis
│   │   ├── analysis-001-product-vision.md
│   │   └── discussion-stakeholders.md
│   ├── 3-atomics/                    # Conocimiento atomizado
│   │   └── concept-product-vision.json
│   ├── 4-artefact/                   # Tests, patterns, contracts
│   │   └── test-product-template.md
│   ├── 6-outputs/                    # Cypher, embeddings, índices
│   │   └── cypher-product-ontology.cypher
│   └── compiler/                     # Compilador del artefacto
│       ├── compile-product.py
│       └── templates/
│           └── product.md.j2
├── workbook-requirements-md/         # Estructura 1-6 completa
├── workbook-design-md/               # Estructura 1-6 completa
├── workbook-tasks-md/                # Estructura 1-6 completa
└── workbook-implementation-log-md/   # Estructura 1-6 completa
```

---

## 📚 Hallazgos de Investigación

### 1. IMRAD vs Scoping Review

**Investigación académica** (ArXiv papers + Brave Web Search):

| Metodología | Propósito | Uso |
|-------------|-----------|-----|
| **IMRAD** | Reportar experimento empírico | "¿Cómo afecta X a Y?" (pregunta experimental) |
| **Scoping Review** (Arksey & O'Malley) | Mapear territorio de conocimiento | "¿Qué se conoce sobre X?" (descubrimiento de dominio) |

**Conclusión**: SPEC-001 NO es investigación empírica (no hay experimento). Es **descubrimiento de dominio** → **Scoping Review** es más apropiada que IMRAD puro.

### 2. Estructura Epistemológica 1-6

**Flujo de conocimiento**:
```
1-literature/    →  ENTRADA (fuentes primarias: books, papers, frameworks)
2-analysis/      →  PROCESO (análisis, notas, discusiones)
3-atomics/       →  EXTRACCIÓN (conceptos atomizados en JSON)
4-artefact/      →  VALIDACIÓN (tests, patterns, contracts)
6-outputs/       →  INGESTA (cypher para Neo4j, embeddings, índices)
compiler/        →  COMPILACIÓN (generate artifact final)
```

**Ventaja**: Cada workbook es un **bounded context** autogestionable que puede compilarse independientemente.

### 3. Fuentes Citadas

**Papers de ArXiv**:
- "Enhancing the role of academic librarians in conducting scoping reviews" (2021) - Bibliometric mapping
- "Student Explanation Strategies in Postsecondary Mathematics" (2025) - Scoping review framework
- "Nine Best Practices for Research Software Registries" (2020) - Documentation standards

**Web Sources**:
- Wikipedia IMRAD - "Direct reflection of the process of scientific discovery"
- NTNU Academic Writing - "IMRAD for empirical studies, Literature Review for domain discovery"
- SSRN paper - "Extended IMRAD (+ Literature Review + Theoretical Framework)"

---

## 🎯 Decisiones de Diseño

### ADR-008: Workbooks como Artefactos Autocontenidos

**Contexto**: Inicialmente propuse workbooks organizados por fase IMRAD (01-introduction/, 02-methods/).

**Decisión**: Un workbook por artefacto del spec-workflow (workbook-requirements-md/, workbook-design-md/, etc.).

**Razón**: 
- Cada artefacto (requirements.md, design.md, tasks.md, etc.) tiene su propio **dominio de conocimiento**
- Separation of concerns: literatura sobre requirements ≠ literatura sobre tasks
- Bounded contexts de DDD: cada workbook es un agregado autocontenido

**Estructura**: `1-literature/ → 2-analysis/ → 3-atomics/ → 4-artefact/ → 6-outputs/ → compiler/`

**Consecuencias**:
- ✅ Separation of concerns clara
- ✅ Autopoiesis: cada workbook evoluciona independientemente
- ✅ Traceability: Source → Analysis → Atomic → Artifact → Compiled Product
- ⚠️ Duplicación potencial de literatura común (mitigada con artefactos-conocimiento/)

### ADR-009: Scoping Review vs IMRAD

**Contexto**: SPEC-001 no es investigación empírica (no hay experimento).

**Decisión**: Usar **Scoping Review** (Arksey & O'Malley framework) en vez de IMRAD puro.

**Razón**: 
- Estamos **mapeando conocimiento existente** sobre artifacts, no reportando un experimento
- IMRAD = "¿Cómo funciona X?" (experimental)
- Scoping Review = "¿Qué se sabe sobre X?" (discovery)

**Framework Arksey & O'Malley**:
1. Identifying research question
2. Identifying relevant studies
3. Study selection
4. **Charting the data** (bibliometric mapping, science landscapes)
5. Collating, summarizing, reporting results

**Consecuencias**:
- ✅ Estructura flexible en 2-analysis/ (temática, cronológica, conceptual)
- ✅ Bibliometric mapping posible en 6-outputs/ (visualización de dominio)
- ✅ Alineado con la realidad: estamos descubriendo, no experimentando
- ⚠️ Menos estructura fija que IMRAD (requiere más decisiones de diseño)

### ADR-010: Estructura 1-6 Epistemológica

**Decisión**: Flujo Literature → Analysis → Atomics → Artifacts → Outputs → Compiled Product.

**Razón**: La estructura debe reflejar el **PROCESO DE DESCUBRIMIENTO** de conocimiento, no solo el formato de reporte.

**Consecuencias**:
- ✅ Cada workbook es autogestionable (tiene toda la pipeline completa)
- ✅ Compilable: compiler/ lee 1-3 y genera artifact
- ✅ Rastreable: Cada claim en artifact puede rastrearse a source en 1-literature/
- ✅ Validable: 4-artefact/ contiene tests para verificar claims

---

## 🔄 Acciones Correctivas

### Actualizaciones en requirements.md

**Cambio**: Reemplazar REQ-001-04 (8 workbooks IMRAD) con REQ-001-04 (5 workbooks por artefacto):

```diff
- REQ-001-04: SALOMÓN - IMRAD Investigation Workbooks
-   - 8 workbooks: 01-introduction ... 08-references
+ REQ-001-04: SALOMÓN - Domain Workbooks por Artefacto
+   - 5 workbooks: workbook-product-md/, workbook-requirements-md/, 
+                   workbook-design-md/, workbook-tasks-md/, 
+                   workbook-implementation-log-md/
+   - Cada uno con estructura 1-6 completa
+   - Metodología: Scoping Review (Arksey & O'Malley)
```

### Actualizaciones en tasks.md

**Problema**: Tasks no pueden usar sub-numeración (2.2.1, 2.2.2 prohibido en spec-workflow-mcp).

**Solución**: Reindexar Phase 2 tasks:
- Task 2.1: HYPATIA Knowledge Acquisition ✅ (sin cambios)
- Task 2.2: Create workbook-product-md/ (🆕 expandido)
- Task 2.3: Create workbook-requirements-md/ (🆕)
- Task 2.4: Create workbook-design-md/ (🆕)
- Task 2.5: Create workbook-tasks-md/ (🆕)
- Task 2.6: Create workbook-implementation-log-md/ (🆕)
- Task 2.7: RBM Mapping (antes era 2.3) ✅
- Task 2.8: Ontology (antes era 2.5) ✅
- Task 2.9: Template Updates (antes era 2.6) ✅

### Actualizaciones en design.md

**Agregar**:
- ADR-008: Workbooks como Artefactos Autocontenidos
- ADR-009: Scoping Review vs IMRAD
- ADR-010: Estructura 1-6 Epistemológica

---

## 💡 Lecciones Aprendidas

### 1. Investigación Académica Antes de Arquitectura

**Lección**: Antes de proponer una estructura, investigar metodologías académicas establecidas (IMRAD, Scoping Review, Systematic Review).

**Aplicación**: Usar ArXiv search + Brave Web Search para comprender diferencias entre metodologías y elegir la apropiada.

### 2. Bounded Contexts Aplican a Research También

**Lección**: Los principios de DDD (bounded contexts, aggregates) aplican no solo a código, sino también a **organización de conocimiento**.

**Aplicación**: Cada artefacto (requirements, design, tasks) es un **bounded context** con su propio dominio de conocimiento y vocabulario.

### 3. Autopoiesis Requiere Autocorrección

**Lección**: El sistema detectó su propio error (usuario señaló: "ESTO NO VA EN EL SPEC, ES EL PRODUCTO DEL SPEC").

**Aplicación**: La capacidad de autocorrección es fundamental para sistemas autopoiéticos. SmartThinking (5 pensamientos) facilitó análisis profundo.

### 4. Separación Epistemológica: Source vs Product

**Lección**: Clarificar la diferencia entre:
- **Source** (domain/workbooks/) = INVESTIGACIÓN (paper académico)
- **Product** (spec/) = APLICACIÓN (estándar técnico que CITA el paper)

**Aplicación**: Como ISO 21838 **cita** papers de BFO pero no los embebe completos.

---

## ✅ Criterios de Éxito

- [x] SmartThinking analysis completado (5 pensamientos, 91% confidence)
- [ ] requirements.md actualizado con REQ-001-04 correcto
- [ ] design.md actualizado con ADR-008, ADR-009, ADR-010
- [ ] tasks.md reindexado (2.2-2.9 sin sub-numeración prohibida)
- [ ] CHATLOG actualizado con análisis SmartThinking
- [ ] LESSON-002 creado documentando aprendizaje
- [ ] Commit: "refactor(spec-001): workbooks por artefacto + estructura 1-6 epistemológica"

---

## 📖 Referencias

**Académicas**:
- Arksey, H., & O'Malley, L. (2005). "Scoping studies: towards a methodological framework"
- Sollaci, L. B., & Pereira, M. G. (2004). "The introduction, methods, results, and discussion (IMRAD) structure"
- Kokol, P., et al. (2021). "Enhancing the role of academic librarians in conducting scoping reviews"

**Técnicas**:
- Evans, E. (2003). "Domain-Driven Design: Tackling Complexity in the Heart of Software"
- Vernon, V. (2013). "Implementing Domain-Driven Design"

**Web**:
- Wikipedia: IMRAD - https://en.wikipedia.org/wiki/IMRAD
- NTNU Academic Writing: IMRAD Structure - https://i.ntnu.no/en/academic-writing/imrad-structure
- SSRN: "Academic Article Structure beyond IMRAD" (2025)

---

**Status**: ✅ LESSON DOCUMENTED | AWAITING IMPLEMENTATION
