---
'@context': '../../../context.jsonld'
'@type': 'RequirementsSpecification'
'@id': 'urn:melquisedec:spec:000:requirements'
dc:
  title: "spec-000: Requirements - Investigation DAATH-ZEN & Domain Knowledge"
  creator: "MELQUISEDEC"
  date: "2026-01-10"
  subject: ["requirements", "functional-requirements", "investigation-spec"]
  description: "Requerimientos funcionales y no funcionales para spec-000 investigation"
  type: "RequirementsSpecification"
spec:
  issue: "spec-000-investigation-daath-zen"
  owner: "SALOMON"
  status: "draft"
  version: "0.1.0"
---

# Requirements: spec-000 Investigation DAATH-ZEN

## 1. Functional Requirements

### REQ-000-01: Workbooks de Investigación

#### REQ-000-01.01: Workbook Academic Research - spec-workflow Artifacts

**Tipo de Workbook**: Academic Research (Exploración)
**Ubicación**: `00-define/0-define-daath-zen-framework/workbooks/academic-research/spec-workflow-artifacts-investigation/`
**Metodología**: Systematic Literature Review (Kitchenham 2007) + Zettelkasten

**Descripción**:
Investigar qué artefactos espera el dashboard de spec-workflow-mcp mediante análisis sistemático del código fuente (implementation-log-manager.ts, server.ts).

**Estructura Requerida**:
```
spec-workflow-artifacts-investigation/
├── 1-literature/
│   ├── sources.yaml                    # PRISMA flow: ≥15 fuentes
│   ├── framework/spec-workflow-mcp/
│   │   ├── metadata.yaml               # Dublin Core
│   │   ├── content.md                  # Dashboard analysis ≥1000 palabras
│   │   └── citations.bib
│   ├── paper/hevner-2004-dsr/
│   └── book/evans-2003-ddd/
├── 2-analysis/
│   ├── dashboard-code-analysis.md      # AST parsing de dashboard
│   ├── rbm-to-artifacts-mapping.md     # Mapeo RBM → spec-workflow
│   ├── product-md-structure.md         # Análisis product.md esperado
│   ├── tech-md-structure.md            # Análisis tech.md esperado
│   └── recommendations.md              # Qué artefactos adoptar
├── 3-atomics/
│   ├── concept-product-md.md           # Qué es product.md
│   ├── concept-tech-md.md              # Qué es tech.md
│   ├── concept-structure-md.md         # Qué es structure.md
│   ├── concept-requirements-md.md      # Qué es requirements.md
│   └── concept-design-md.md            # Qué es design.md
├── 4-artifacts/
│   ├── test-product-compiler.py        # Test: Compilar product.md
│   ├── schema-product-md.json          # JSON Schema para product.md
│   └── contract-dashboard-parser.py    # Contract: Parser dashboard
└── 6-outputs/
    ├── index-spec-workflow-artifacts.md
    ├── cypher-artifacts-ingestion.cypher
    └── README.md                        # ALMA-generated overview
```

**Success Criteria**:
- [ ] ≥15 fuentes catalogadas en `1-literature/sources.yaml` (PRISMA flow completo)
- [ ] Metadata Dublin Core completa en cada fuente
- [ ] ≥8 contenidos-atómicos generados en `3-atomics/` (1 por artefacto spec-workflow)
- [ ] ≥3 artifacts ejecutables en `4-artifacts/` (tests passing)
- [ ] Cypher queries generadas en `6-outputs/` (Neo4j validated cuando se active)

**Documentos Modificados**:
- Workbook completo en `00-define/0-define-daath-zen-framework/workbooks/academic-research/spec-workflow-artifacts-investigation/`
- Contenidos-atómicos publicados en `_melquisedec/domain/markdown/concept-*.md` (al final)

**Responsables**:
- **HYPATIA**: `1-literature/` (5 días)
- **SALOMON**: `2-analysis/` (3 días)
- **MORPHEUS**: `3-atomics/` + `4-artifacts/` (2 días)
- **ALMA**: `6-outputs/` + publicación a `_melquisedec/domain/` (1 día)

---

#### REQ-000-01.02: Workbook IMRAD - Templates DAATH-ZEN Analysis

**Tipo de Workbook**: IMRAD (Análisis Específico)
**Ubicación**: `00-define/0-define-daath-zen-framework/workbooks/imrad-research/daath-zen-templates-analysis/`
**Metodología**: IMRAD (Sollaci & Pereira 2004)

**Descripción**:
Analizar 6 versiones de templates DAATH-ZEN (14-228 líneas) mediante análisis comparativo línea-por-línea para identificar estructura unificada óptima.

**Estructura Requerida**:
```
daath-zen-templates-analysis/
├── 01-introduction.md      # Problema: 6 templates inconsistentes, hipótesis, objetivos
├── 02-methods.md           # Análisis comparativo línea-por-línea, extracción placeholders
├── 03-results.md           # Tabla comparativa (líneas, placeholders, metadata)
├── 04-analysis.md          # Patrones comunes, estructura unificada emergente
├── 05-discussion.md        # Implicaciones: template unificado reduce 70% código
├── 06-conclusion.md        # Decisión: Adoptar daath-zen-base.md, diseño template-base.yaml
└── 07-references.md        # Links a 6 templates analizados
```

**Success Criteria**:
- [ ] 7 secciones IMRAD completas (≥500 palabras cada una)
- [ ] Tabla comparativa de 6 templates en `03-results.md`
- [ ] Decisión fundamentada en `06-conclusion.md` (cita `03-results.md` y `04-analysis.md`)
- [ ] template-base.yaml diseñado (prototipo validado por MORPHEUS)

**Documentos Modificados**:
- Workbook completo en `00-define/0-define-daath-zen-framework/workbooks/imrad-research/daath-zen-templates-analysis/`
- Contenido atómico `template-base-design.md` en `_melquisedec/domain/markdown/` (al final)

**Responsables**:
- **SALOMON**: 7 secciones IMRAD (3 días)
- **MORPHEUS**: Validación de diseño (1 día)

---

#### REQ-000-01.03: Workbook Academic Research - Opensource Ontologies

**Tipo de Workbook**: Academic Research (Exploración)
**Ubicación**: `00-define/0-define-daath-zen-framework/workbooks/academic-research/opensource-ontologies-investigation/`
**Metodología**: Systematic Literature Review + Grounded Theory

**Descripción**:
Descubrir qué ontologías, frameworks y patterns opensource existen para grafos de conocimiento (Schema.org, FOAF, Neo4j GDS, etc.).

**Success Criteria**:
- [ ] ≥20 frameworks catalogados en `1-literature/framework/`
- [ ] ≥10 contenidos-atómicos en `3-atomics/` (conceptos clave de ontologías)
- [ ] ≥5 Cypher patterns en `4-artifacts/cypher-pattern-*.cypher`
- [ ] Recomendaciones en `2-analysis/recommendations.md` (qué adoptar para MELQUISEDEC)

**Responsables**:
- **HYPATIA**: `1-literature/` (4 días)
- **SALOMON**: `2-analysis/` (2 días)
- **MORPHEUS**: `3-atomics/` + `4-artifacts/` (2 días)
- **ALMA**: `6-outputs/` (1 día)

---

#### REQ-000-01.04: Workbook IMRAD - GenAI-stack Documentation

**Tipo de Workbook**: IMRAD (Documentación Arquitectura)
**Ubicación**: `00-define/0-define-daath-zen-framework/workbooks/imrad-research/genai-stack-documentation/`

**Descripción**:
Documentar arquitectura del prototipo GenAI-stack existente (_lab/genai-stack/) para identificar gaps y oportunidades de integración.

**Success Criteria**:
- [ ] Diagrama arquitectura en `03-results.md` (7 servicios Docker)
- [ ] Gaps identificados en `04-analysis.md` (falta MD ingestion)
- [ ] Propuesta integración en `05-discussion.md` (con triple-persistence)
- [ ] Spec formal para spec-002 en `06-conclusion.md`

**Responsables**:
- **SALOMON**: 7 secciones IMRAD (2 días)
- **MORPHEUS**: Validación técnica (0.5 días)

---

#### REQ-000-01.05: Workbook IMRAD - MCP-Obsidian Integration

**Tipo de Workbook**: IMRAD (Diseño Integración)
**Ubicación**: `00-define/0-define-daath-zen-framework/workbooks/imrad-research/mcp-obsidian-integration/`

**Descripción**:
Diseñar integración entre MCP-Obsidian y workbooks para gestión de dominio con Obsidian (graph view, backlinks, Kanban).

**Success Criteria**:
- [ ] Diagrama integración en `03-results.md`
- [ ] Estrategia sincronización en `04-analysis.md`
- [ ] ALMA como orquestador en `05-discussion.md`
- [ ] Pipeline ALMA definido en `06-conclusion.md`

**Responsables**:
- **SALOMON**: 7 secciones IMRAD (2 días)
- **ALMA**: Validación (0.5 días)

---

#### REQ-000-01.06: Workbook IMRAD - Contenidos-Atómicos Methodology

**Tipo de Workbook**: IMRAD (Metodología Design)
**Ubicación**: `00-define/0-define-daath-zen-framework/workbooks/imrad-research/contenidos-atomicos-methodology/`

**Descripción**:
Definir metodología estandarizada para contenidos-atómicos basada en Zettelkasten, con templates y automatización MORPHEUS.

**Success Criteria**:
- [ ] Template para atomic content en `03-results.md`
- [ ] Relación con triple persistence en `04-analysis.md`
- [ ] MORPHEUS automatizado en `05-discussion.md`
- [ ] Metodología estandarizada en `06-conclusion.md`

**Responsables**:
- **SALOMON**: 7 secciones IMRAD (2 días)
- **MORPHEUS**: Validación (0.5 días)

---

### REQ-000-02: Metadata Standards

#### REQ-000-02.01: Dublin Core Obligatorio

**Descripción**:
Todo archivo markdown en workbooks/ debe tener YAML frontmatter con Dublin Core completo.

**Campos Requeridos**:
```yaml
---
dc:
  title: "..."                              # REQUIRED
  creator: "spec-000-investigation-daath-zen"  # REQUIRED
  date: "2026-01-10"                        # REQUIRED
  subject: [...]                            # REQUIRED
  description: "..."                        # REQUIRED
  type: "..."                               # REQUIRED
  format: "text/markdown"                   # REQUIRED
  identifier: "..."                         # REQUIRED (atomic-000-001, workbook-000-001)
  language: "es"                            # REQUIRED

spec:
  issue: "spec-000-investigation-daath-zen" # REQUIRED
  owner: "MORPHEUS"                         # REQUIRED (HYPATIA|SALOMON|MORPHEUS|ALMA)
  status: "draft"                           # REQUIRED (draft|stable|deprecated)
  version: "1.0.0"                          # REQUIRED (semver)

'@context': '../../../context.jsonld'      # REQUIRED (Keter-Doc Protocol)
'@type': 'ContentoAtomic'                  # REQUIRED
'@id': 'atomic-000-001'                    # REQUIRED
---
```

**Validation**:
```bash
python tools/validate-metadata.py 00-define/0-define-daath-zen-framework/workbooks/
# Expected: 100% pass rate
```

---

#### REQ-000-02.02: Ownership & Governance

**Descripción**:
Todo contenido-atómico debe especificar owner (spec que lo creó y mantiene).

**Pull Request System**:
- Specs posteriores NO pueden modificar atomics de spec-000 directamente
- Deben crear PR en `.spec-workflow/specs/spec-000/pull-requests/pending/`
- MORPHEUS (owner) revisa y aprueba/rechaza
- Si aprobado: versión bump + changelog en metadata

**Ejemplo PR**:
```yaml
# pull-requests/pending/pr-003-to-000-product-md-schema.md
pr:
  id: "pr-003-to-000-001"
  from: "spec-003"
  to: "spec-000"
  target: "_melquisedec/domain/markdown/concept-product-md.md"
  type: "enhancement"
  status: "pending"
```

---

### REQ-000-03: Triple Persistence (Solución Temporal)

#### REQ-000-03.01: Publicación Manual a _melquisedec/domain/

**Descripción**:
Hasta activar Neo4j + Ollama, contenidos-atómicos se publican manualmente:

```bash
# ALMA ejecuta al finalizar workbooks
cp 00-define/.../workbooks/academic-research/.../3-atomics/*.md \
   _melquisedec/domain/markdown/

cp 00-define/.../workbooks/imrad-research/.../06-conclusion.md \
   _melquisedec/domain/markdown/{workbook-name}-conclusion.md
```

**Success Criteria**:
- [ ] ≥31 archivos en `_melquisedec/domain/markdown/`
- [ ] Todos con metadata completa (Dublin Core + spec:issue)
- [ ] `_melquisedec/domain/README.md` generado por ALMA (índice)

---

#### REQ-000-03.02: Preparación para Triple Persistence

**Descripción**:
Aunque no se active aún, preparar estructura:

```
_melquisedec/domain/
├── markdown/           # SOURCE OF TRUTH (manual por ahora)
├── cypher/             # Placeholder (vacío)
├── embeddings/         # Placeholder (vacío)
└── ontologies/         # Placeholder (vacío)
```

**Rationale**:
Cuando se active triple persistence (spec-002+), estructura ya existe.

---

### REQ-000-04: Validation & Quality

#### REQ-000-04.01: IMRAD Structure Validation

**Tool**: `python tools/validate-imrad-structure.py`

**Checks**:
- [ ] 7 archivos existen (01-07)
- [ ] Cada archivo ≥500 palabras
- [ ] Metadata YAML presente
- [ ] References section cita al menos 3 fuentes

**Exit Code**:
- `0`: Pass
- `1`: Fail (detalle en stderr)

---

#### REQ-000-04.02: Academic Research Validation

**Tool**: `python tools/validate-academic-research.py`

**Checks**:
- [ ] 5 folders existen (1-literature, 2-analysis, 3-atomics, 4-artifacts, 6-outputs)
- [ ] `1-literature/sources.yaml` con PRISMA flow
- [ ] ≥8 atomics en `3-atomics/`
- [ ] README.md en `6-outputs/`

---

#### REQ-000-04.03: Metadata Validation

**Tool**: `python tools/validate-metadata.py`

**Checks**:
- [ ] Dublin Core: 9 campos requeridos presentes
- [ ] `spec:issue` presente y válido
- [ ] `spec:owner` es uno de: HYPATIA, SALOMON, MORPHEUS, ALMA
- [ ] `spec:version` es semver válido
- [ ] `@context` apunta a `context.jsonld`

---

## 2. Non-Functional Requirements

### NFR-000-01: Performance

**NFR-000-01.01: Workbook Creation Time**
- Target: ≤18 días (3.5 semanas) para 6 workbooks
- Measured: Fecha inicio → fecha último commit workbooks/

**NFR-000-01.02: Validation Time**
- Target: < 5 minutos para validar todos los workbooks
- Measured: `time bash tools/validate-all.sh`

---

### NFR-000-02: Maintainability

**NFR-000-02.01: Documentation Coverage**
- Target: 100% workbooks con README.md
- Measured: `find workbooks/ -name README.md | wc -l` == 6

**NFR-000-02.02: Metadata Coverage**
- Target: 100% archivos .md con metadata
- Measured: `validate-metadata.py` pass rate

---

### NFR-000-03: Usability

**NFR-000-03.01: Obsidian Compatibility**
- Requirement: Todos los wikilinks [[]] válidos
- Measured: Obsidian graph view muestra conexiones

**NFR-000-03.02: Search Functionality**
- Requirement: Grep search encuentra conceptos
- Example: `grep -r "product.md" workbooks/` retorna ≥3 matches

---

### NFR-000-04: Scalability

**NFR-000-04.01: Future Specs**
- Requirement: Estructura soporta spec-001+
- Example: spec-001 puede referenciar atomics de spec-000 con [[concept-*]]

**NFR-000-04.02: Triple Persistence Ready**
- Requirement: Cuando se active Neo4j, sync debe ser automático
- Example: `sync-all.sh` funciona sin cambios en workbooks/

---

## 3. Constraints

### CON-000-01: No External APIs
- Rationale: Local-first approach
- Impact: No cloud embeddings, no external ontology APIs

### CON-000-02: No Database Until spec-002
- Rationale: Incremental complexity
- Impact: Manual copy a `_melquisedec/domain/`

### CON-000-03: Git Repository Size
- Rationale: Keep repo < 1GB
- Impact: No large embeddings committed (use Git LFS if needed)

---

## 4. Assumptions

### ASS-000-01: Legacy Research Available
- Assumption: `_melquisedec/lessons/lesson-001.../` contiene 4 documentos análisis previo
- Validation: Files exist (checked)

### ASS-000-02: 6 Templates Exist
- Assumption: 6 versiones templates DAATH-ZEN disponibles en `00-define/.../manifest/templates/`
- Validation: Count files

### ASS-000-03: spec-workflow Code Available
- Assumption: Dashboard code en `_legacy/` o repo externo accesible
- Validation: Code review posible

---

## 5. Dependencies

### DEP-000-01: Prerequisites
- [x] Keter-Doc Protocol v1.0.0 (`context.jsonld` existe)
- [ ] Python 3.11+ instalado
- [ ] Git instalado
- [ ] Obsidian (opcional, para visualización)

### DEP-000-02: External Specs
- None (spec-000 es foundation, no depende de otros specs)

---

## 6. Acceptance Criteria (Global)

### AC-000-01: Workbooks Complete
- [ ] 6 workbooks completados (2 Academic + 4 IMRAD)
- [ ] Todos con metadata completa
- [ ] Validation tools pasan 100%

### AC-000-02: Knowledge Base Populated
- [ ] ≥31 contenidos-atómicos en `_melquisedec/domain/markdown/`
- [ ] README.md índice generado por ALMA
- [ ] Todos los atomics con `spec:issue = spec-000`

### AC-000-03: Documentation Complete
- [ ] requirements.md (este archivo)
- [ ] design.md (ADRs)
- [ ] tasks.md (cronograma)

### AC-000-04: Quality Validated
- [ ] `validate-imrad-structure.py` pass
- [ ] `validate-academic-research.py` pass
- [ ] `validate-metadata.py` pass (100% coverage)

---

## 7. Traceability Matrix

| Requirement | Design Decision | Task | Validation |
|-------------|-----------------|------|------------|
| REQ-000-01.01 (Workbook 1) | ADR-001 (Academic vs IMRAD) | Task 2.1 | validate-academic-research.py |
| REQ-000-01.02 (Workbook 2) | ADR-001 | Task 2.2 | validate-imrad-structure.py |
| REQ-000-02.01 (Dublin Core) | ADR-003 (Metadata Standard) | Task 3.1 | validate-metadata.py |
| REQ-000-03.01 (Manual Publish) | ADR-005 (Triple Persistence Defer) | Task 4.1 | Manual check |

---

**Version History**:
- v0.1.0 (2026-01-10): Initial requirements basado en ANALISIS-PROPUESTA + ANALISIS-PROFUNDO
