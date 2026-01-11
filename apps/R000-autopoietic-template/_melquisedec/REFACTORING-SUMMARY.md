# REFACTORIZACIÓN SPEC-001: Workbooks por Artefacto

**Fecha**: 2026-01-10
**Commit**: `refactor(spec-001): workbooks por artefacto + estructura 1-6 epistemológica`

---

## Cambios Principales

### 1. Arquitectura de Workbooks

**ANTES** ❌:
- Workbooks por fase IMRAD (01-introduction, 02-methods, 03-results...)
- Un solo workbook gigante para toda la investigación

**DESPUÉS** ✅:
- Workbooks por ARTEFACTO (workbook-product-md/, workbook-requirements-md/, etc.)
- 5 workbooks autocontenidos con estructura 1-6 cada uno

### 2. Estructura Interna (1-6 Epistemológica)

```
workbook-{artefacto}/
├── 1-literature/          # ENTRADA: book, paper, framework, library
├── 2-analysis/            # PROCESO: analysis-XXX.md, discussions
├── 3-atomics/             # EXTRACCIÓN: concept-XXX.json
├── 4-artefact/            # VALIDACIÓN: tests, patterns, contracts
├── 6-outputs/             # INGESTA: cypher, embeddings, índices
└── compiler/              # COMPILACIÓN: compile.py + templates
```

### 3. Metodología: Scoping Review

**Cambio**: De IMRAD puro → Scoping Review (Arksey & O'Malley)

**Razón**: SPEC-001 es descubrimiento de dominio, no experimento empírico.

---

## ADRs Agregados

- **ADR-008**: Workbooks como Artefactos Autocontenidos
- **ADR-009**: Scoping Review vs IMRAD
- **ADR-010**: Estructura 1-6 Epistemológica

---

## Tasks Reindexadas

**Phase 2 tasks**:
- 2.1: HYPATIA Knowledge Acquisition (sin cambios)
- 2.2: Create workbook-product-md/ (🆕)
- 2.3: Create workbook-requirements-md/ (🆕)
- 2.4: Create workbook-design-md/ (🆕)
- 2.5: Create workbook-tasks-md/ (🆕)
- 2.6: Create workbook-implementation-log-md/ (🆕)
- 2.7: RBM Mapping (antes 2.3)
- 2.8: Ontology (antes 2.5)
- 2.9: Template Updates (antes 2.6)

---

## Archivos Actualizados

- ✅ `LESSON-002-workbooks-arquitectura.md` (creado)
- ✅ `CHATLOG-2026-01-10_202500-spec-001-workbooks-refactor.md` (creado)
- ✅ `requirements.md` (REQ-001-04 actualizado - workbooks por artefacto)
- ✅ `design.md` (ADRs 008-010 agregados)
- ✅ `tasks.md` (Phase 2 reindexada 2.2-2.9, sin sub-numeración)

---

## Referencias

**SmartThinking Analysis**: 5 pensamientos, 91% confidence
**ArXiv Papers**: 3 papers sobre Scoping Review y metodologías
**Web Sources**: 10 sources (Wikipedia IMRAD, NTNU, SSRN)

---

**Status**: ✅ REFACTORING COMPLETE | Ready for Phase 2.2 implementation
