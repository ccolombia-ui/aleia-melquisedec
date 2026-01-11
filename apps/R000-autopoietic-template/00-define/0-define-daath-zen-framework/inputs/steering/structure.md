---
'@context': '../../../context.jsonld'
'@type': 'ProjectStructure'
'@id': 'urn:melquisedec:spec:000:structure'
dc:
  title: "spec-000: Project Structure & File Organization"
  creator: "MELQUISEDEC"
  date: "2026-01-10"
  subject: ["project-structure", "file-organization", "workspace-layout"]
  description: "Estructura de directorios y organización de archivos para spec-000 investigation"
  type: "StructureSpecification"
spec:
  issue: "spec-000-investigation-daath-zen"
  owner: "ALMA"
  status: "draft"
  version: "0.1.0"
---

# Project Structure: spec-000 Investigation

## 1. Overview

spec-000 utiliza **workspace de investigación** en `00-define/` separado del **spec formal** en `.spec-workflow/specs/`.

### Principio de Separación

```
00-define/                          ← WORKSPACE (investigación activa)
.spec-workflow/specs/spec-000/      ← SPEC FORMAL (documentación governance)
_melquisedec/domain/                ← OUTPUTS FINALES (publicación consolidada)
```

**Razón**: Investigación es proceso vivo y cambiante. Spec formal es governance y tracking.

---

## 2. Workspace Structure (00-define/)

### 2.1 Ubicación Principal

```
apps/R000-autopoietic-template/00-define/0-define-daath-zen-framework/
```

**Naming convention**: `0-define-{topic}/`
- `0-define-daath-zen-framework/` → spec-000
- `0-define-ontologies-investigation/` → spec-XXX (futuro)
- `0-define-embeddings-benchmarking/` → spec-YYY (futuro)

---

### 2.2 Internal Structure

```
00-define/0-define-daath-zen-framework/
│
├── 0-context/                              # INPUTS (fuentes de investigación)
│   ├── legacy-research/
│   │   ├── INVESTIGACION-BIDIRECCIONAL-template-spec-daath.md
│   │   ├── ANALISIS-PROPUESTA-spec-000-dominio-vivo.md
│   │   ├── ANALISIS-PROFUNDO-academic-research-vs-imrad.md
│   │   └── SPEC-000-REFINEMENT-5-rostros.md
│   │
│   ├── templates/
│   │   ├── daath-zen-base.md               # 228 líneas
│   │   ├── daath-zen-minimalista.md        # 30 líneas
│   │   ├── daath-zen-configurable.md       # 45 líneas
│   │   ├── daath-zen-rbm.md                # 60 líneas
│   │   ├── daath-zen-keter-doc.md          # 80 líneas
│   │   └── daath-zen-full.md               # 228 líneas (backup)
│   │
│   ├── spec-workflow-code/
│   │   ├── dashboard-code-analysis.md      # Análisis de implementation-log-manager.ts
│   │   ├── server-endpoints.md             # Endpoints del dashboard
│   │   └── artifact-schemas/               # JSON Schemas esperados
│   │       ├── product-md.schema.json
│   │       ├── tech-md.schema.json
│   │       └── structure-md.schema.json
│   │
│   └── frameworks-research/
│       ├── schema-org-investigation.md
│       ├── foaf-ontology-analysis.md
│       ├── neo4j-gds-patterns.md
│       └── embedding-models-comparison.md
│
├── 1-steering/                             # STEERING DOCS (Governance)
│   ├── product.md                          # Product vision & success criteria
│   ├── tech.md                             # Technical architecture & pipeline
│   └── structure.md                        # This file (project structure)
│
├── workbooks/                              # INVESTIGACIÓN (workbooks activos)
│   │
│   ├── academic-research/                  # Tipo 1: Exploración de dominio
│   │   │
│   │   ├── spec-workflow-artifacts-investigation/
│   │   │   ├── 1-literature/
│   │   │   │   ├── sources.yaml            # PRISMA flow (≥15 fuentes)
│   │   │   │   ├── framework/
│   │   │   │   │   └── spec-workflow-mcp/
│   │   │   │   │       ├── metadata.yaml   # Dublin Core
│   │   │   │   │       ├── content.md      # Dashboard analysis
│   │   │   │   │       └── citations.bib
│   │   │   │   ├── paper/
│   │   │   │   │   └── hevner-2004-dsr/
│   │   │   │   └── book/
│   │   │   │       └── evans-2003-ddd/
│   │   │   │
│   │   │   ├── 2-analysis/
│   │   │   │   ├── dashboard-code-analysis.md
│   │   │   │   ├── rbm-to-artifacts-mapping.md
│   │   │   │   ├── product-md-structure.md
│   │   │   │   ├── tech-md-structure.md
│   │   │   │   └── recommendations.md
│   │   │   │
│   │   │   ├── 3-atomics/                  # Contenidos-atómicos (MORPHEUS)
│   │   │   │   ├── concept-product-md.md
│   │   │   │   ├── concept-tech-md.md
│   │   │   │   ├── concept-structure-md.md
│   │   │   │   ├── concept-requirements-md.md
│   │   │   │   └── concept-design-md.md
│   │   │   │
│   │   │   ├── 4-artifacts/                # Artifacts (tests, schemas)
│   │   │   │   ├── test-product-compiler.py
│   │   │   │   ├── schema-product-md.json
│   │   │   │   └── contract-dashboard-parser.py
│   │   │   │
│   │   │   └── 6-outputs/                  # Outputs para publicación
│   │   │       ├── index-spec-workflow-artifacts.md
│   │   │       ├── cypher-artifacts-ingestion.cypher
│   │   │       └── README.md               # ALMA-generated overview
│   │   │
│   │   └── opensource-ontologies-investigation/
│   │       ├── 1-literature/
│   │       │   ├── framework/
│   │       │   │   ├── schema-org/
│   │       │   │   ├── foaf-ontology/
│   │       │   │   ├── neo4j-gds/
│   │       │   │   └── dbpedia/
│   │       │   └── library/
│   │       │       ├── llamaindex/
│   │       │       └── langchain/
│   │       ├── 2-analysis/
│   │       ├── 3-atomics/
│   │       ├── 4-artifacts/
│   │       └── 6-outputs/
│   │
│   └── imrad-research/                     # Tipo 2: Análisis específico
│       │
│       ├── daath-zen-templates-analysis/
│       │   ├── 01-introduction.md          # Problema: 6 templates inconsistentes
│       │   ├── 02-methods.md               # Análisis comparativo línea-por-línea
│       │   ├── 03-results.md               # Tabla comparativa
│       │   ├── 04-analysis.md              # Patrones comunes
│       │   ├── 05-discussion.md            # Implicaciones
│       │   ├── 06-conclusion.md            # Decisión: template-base.yaml
│       │   └── 07-references.md            # Links a 6 templates
│       │
│       ├── genai-stack-documentation/
│       │   ├── 01-introduction.md
│       │   ├── 02-methods.md
│       │   ├── 03-results.md
│       │   ├── 04-analysis.md
│       │   ├── 05-discussion.md
│       │   ├── 06-conclusion.md
│       │   └── 07-references.md
│       │
│       ├── mcp-obsidian-integration/
│       │   └── [7 secciones IMRAD]
│       │
│       └── contenidos-atomicos-methodology/
│           └── [7 secciones IMRAD]
│
└── README.md                               # Overview del workspace
```

---

## 3. Spec Formal Structure (.spec-workflow/)

### 3.1 Ubicación

```
.spec-workflow/specs/spec-000-investigation-daath-zen/
```

---

### 3.2 Internal Structure

```
.spec-workflow/specs/spec-000-investigation-daath-zen/
│
├── 000-steering/                           # STEERING (Governance Docs)
│   ├── product.md                          # Product specification
│   ├── tech.md                             # Technical specification
│   └── structure.md                        # This file
│
├── 010-define/                             # DEFINE (Requirements & Design)
│   ├── requirements.md                     # Functional & non-functional requirements
│   ├── design.md                           # Architecture decisions (ADRs)
│   └── tasks.md                            # Execution plan (cronograma)
│
├── 020-build/                              # BUILD (Implementation tracking)
│   └── implementation-log.json             # MORPHEUS logs artifacts created
│
├── 030-validate/                           # VALIDATE (Quality assurance)
│   └── validation-results.json             # validate-*.py outputs
│
├── 040-review/                             # REVIEW (PR tracking)
│   ├── pending/
│   │   └── pr-XXX-to-000-YYY.md
│   ├── approved/
│   └── rejected/
│
├── 050-release/                            # RELEASE (Final outputs)
│   ├── release-notes.md
│   └── changelog.md
│
└── README.md                               # Spec overview & status
```

---

## 4. Final Outputs Structure (_melquisedec/)

### 4.1 Domain Knowledge Base

```
apps/R000-autopoietic-template/_melquisedec/domain/
│
├── markdown/                               # Contenidos-atómicos consolidados
│   ├── concept-product-md.md
│   ├── concept-tech-md.md
│   ├── concept-structure-md.md
│   ├── template-base-design.md
│   ├── schema-org-core-concepts.md
│   ├── foaf-relationship-types.md
│   └── [...31 atomics total]
│
├── cypher/                                 # Cypher queries (futuro Neo4j)
│   ├── nodes.cypher
│   ├── relationships.cypher
│   └── constraints.cypher
│
├── embeddings/                             # Vector embeddings (futuro)
│   ├── concept-product-md.npy              # (768,) float32 array
│   ├── concept-tech-md.npy
│   └── [...]
│
├── ontologies/                             # OWL/Turtle ontologies (futuro)
│   └── melquisedec-domain-v1.0.ttl
│
└── README.md                               # ALMA-generated index
```

---

### 4.2 Context (General)

```
apps/R000-autopoietic-template/_melquisedec/context/
│
├── frameworks/                             # Frameworks catalogados
│   ├── ddd-evans-2003.md
│   ├── imrad-sollaci-2004.md
│   ├── schema-org.md
│   └── foaf-ontology.md
│
├── concepts/                               # Conceptos fundamentales
│   ├── bounded-context.md
│   ├── ubiquitous-language.md
│   └── aggregate-root.md
│
└── README.md
```

---

## 5. Flujo de Archivos (File Flow)

### 5.1 Inputs → Workbooks

```
0-context/templates/daath-zen-base.md
          ↓
workbooks/imrad-research/daath-zen-templates-analysis/02-methods.md
          ↓
workbooks/imrad-research/daath-zen-templates-analysis/03-results.md
```

---

### 5.2 Workbooks → Atomics

```
workbooks/academic-research/spec-workflow-artifacts-investigation/2-analysis/product-md-structure.md
          ↓ (MORPHEUS extrae)
workbooks/academic-research/spec-workflow-artifacts-investigation/3-atomics/concept-product-md.md
```

---

### 5.3 Atomics → Domain

```
workbooks/academic-research/.../3-atomics/concept-product-md.md
          ↓ (ALMA consolida)
_melquisedec/domain/markdown/concept-product-md.md
          ↓ (Futuro: Triple Persistence)
_melquisedec/domain/cypher/concept-product-md.cypher
_melquisedec/domain/embeddings/concept-product-md.npy
```

---

## 6. Naming Conventions

### 6.1 Workbooks

**Academic Research**:
- Format: `{topic}-investigation/`
- Example: `spec-workflow-artifacts-investigation/`

**IMRAD Research**:
- Format: `{topic}-analysis/` o `{topic}-design/`
- Example: `daath-zen-templates-analysis/`

---

### 6.2 Contenidos-Atómicos

**Concepts**:
- Format: `concept-{name}.md`
- Example: `concept-product-md.md`

**Designs**:
- Format: `design-{name}.md` o `{name}-design.md`
- Example: `template-base-design.md`

**Patterns**:
- Format: `pattern-{name}.md`
- Example: `pattern-cypher-ingestion.md`

---

### 6.3 Artifacts

**Tests**:
- Format: `test-{component}.py`
- Example: `test-product-compiler.py`

**Schemas**:
- Format: `schema-{artifact}.json`
- Example: `schema-product-md.json`

**Cypher**:
- Format: `{purpose}.cypher` o `cypher-{purpose}.cypher`
- Example: `nodes.cypher`, `cypher-artifacts-ingestion.cypher`

---

## 7. File Metadata Standards

### 7.1 YAML Frontmatter (Required)

**Minimum Required Fields**:
```yaml
---
# Dublin Core
dc:
  title: "..."
  creator: "spec-000-investigation-daath-zen"
  date: "2026-01-10"
  type: "..."

# Spec-Workflow
spec:
  issue: "spec-000-investigation-daath-zen"
  owner: "MORPHEUS"  # HYPATIA | SALOMON | MORPHEUS | ALMA
  status: "draft"    # draft | stable | deprecated
  version: "1.0.0"

# Keter-Doc Protocol
'@context': '../../../context.jsonld'
'@type': '...'
'@id': '...'
---
```

---

### 7.2 Obsidian Compatibility

**Wikilinks**:
```markdown
Related: [[concept-tech-md]]
Depends on: [[template-base-design]]
Referenced by: (Backlinks auto-populated)
```

**Tags**:
```markdown
#workbook #spec-000 #imrad #academic-research
```

---

## 8. Version Control Strategy

### 8.1 Git Structure

```
.git/
├── hooks/
│   └── pre-commit                          # Run validate-metadata.py
├── lfs/                                    # Git LFS for large files
│   └── objects/
│       └── embeddings/*.npy                # Track embeddings with LFS
└── [standard git files]
```

---

### 8.2 .gitignore

```gitignore
# Python
__pycache__/
*.pyc
.venv/

# Neo4j (local data, no commit)
_melquisedec/domain/neo4j-data/
_melquisedec/domain/neo4j-logs/

# Ollama (models cache, no commit)
_melquisedec/domain/ollama-models/

# Obsidian (user-specific)
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# IDE
.vscode/settings.json  # Keep tasks.json, launch.json
.idea/
```

---

### 8.3 Git LFS (Large Files)

```bash
# .gitattributes
_melquisedec/domain/embeddings/*.npy filter=lfs diff=lfs merge=lfs -text
_melquisedec/domain/neo4j-data/**/* filter=lfs diff=lfs merge=lfs -text
```

---

## 9. Directory Creation Commands

### 9.1 Initial Setup

```bash
# Workspace de investigación
mkdir -p apps/R000-autopoietic-template/00-define/0-define-daath-zen-framework/{0-context,1-steering,workbooks/{academic-research,imrad-research}}

# Spec formal
mkdir -p .spec-workflow/specs/spec-000-investigation-daath-zen/{000-steering,010-define,020-build,030-validate,040-review,050-release}

# Outputs finales
mkdir -p apps/R000-autopoietic-template/_melquisedec/{domain/{markdown,cypher,embeddings,ontologies},context/{frameworks,concepts}}
```

---

### 9.2 Workbook Creation Template

```bash
# Academic Research workbook
mkdir -p "00-define/0-define-daath-zen-framework/workbooks/academic-research/{name}-investigation/{1-literature/{framework,paper,book},2-analysis,3-atomics,4-artifacts,6-outputs}"

# IMRAD workbook
mkdir -p "00-define/0-define-daath-zen-framework/workbooks/imrad-research/{name}-analysis"
cd "00-define/0-define-daath-zen-framework/workbooks/imrad-research/{name}-analysis"
touch 01-introduction.md 02-methods.md 03-results.md 04-analysis.md 05-discussion.md 06-conclusion.md 07-references.md
```

---

## 10. Access Patterns

### 10.1 Development Workflow

**Investigadores (HYPATIA + SALOMON)**:
- Trabajan en: `00-define/0-define-daath-zen-framework/workbooks/`
- Leen inputs de: `0-context/`
- No tocan: `_melquisedec/domain/` directamente

**Extractor (MORPHEUS)**:
- Lee: `workbooks/{type}/{name}/2-analysis/`, `workbooks/{type}/{name}/05-discussion/`
- Escribe: `workbooks/{type}/{name}/3-atomics/`, `workbooks/{type}/{name}/4-artifacts/`
- No toca: `_melquisedec/domain/` aún

**Publicador (ALMA)**:
- Lee: `workbooks/{type}/{name}/3-atomics/`, `workbooks/{type}/{name}/6-outputs/`
- Escribe: `_melquisedec/domain/markdown/`, `_melquisedec/context/`
- Ejecuta: `sync-all.sh` (futuro: triple persistence)

---

### 10.2 Read-Only vs Write Access

| Role | Read | Write |
|------|------|-------|
| **HYPATIA** | `0-context/`, `workbooks/` | `workbooks/{type}/{name}/1-literature/` |
| **SALOMON** | `0-context/`, `workbooks/` | `workbooks/{type}/{name}/2-analysis/`, IMRAD sections |
| **MORPHEUS** | `workbooks/` | `workbooks/{type}/{name}/3-atomics/`, `workbooks/{type}/{name}/4-artifacts/` |
| **ALMA** | `workbooks/` | `_melquisedec/domain/`, `_melquisedec/context/`, `workbooks/{type}/{name}/6-outputs/` |

---

## 11. Obsidian Vault Configuration

### 11.1 Vault Root

**Option A** (Recommended): Vault = `00-define/0-define-daath-zen-framework/`
- Pros: Investigadores trabajan dentro del vault
- Cons: Outputs finales fuera del vault

**Option B**: Vault = `apps/R000-autopoietic-template/`
- Pros: Todo visible (workbooks + domain)
- Cons: Muchos archivos no-workbooks visibles

---

### 11.2 Graph View Filters

```json
{
  "search": "path:workbooks/ OR path:_melquisedec/domain/",
  "showTags": true,
  "hideUnresolved": false,
  "colorGroups": [
    {
      "query": "path:workbooks/academic-research/",
      "color": {"r": 255, "g": 195, "b": 0}
    },
    {
      "query": "path:workbooks/imrad-research/",
      "color": {"r": 0, "g": 176, "b": 255}
    },
    {
      "query": "path:_melquisedec/domain/",
      "color": {"r": 76, "g": 175, "b": 80}
    }
  ]
}
```

---

## 12. Cleanup & Maintenance

### 12.1 Temporary Files

```bash
# Remove temp files after publishing
find workbooks/ -name "*.tmp" -delete
find workbooks/ -name ".DS_Store" -delete
```

---

### 12.2 Archive Completed Workbooks

```bash
# After ALMA publishes to _melquisedec/domain/
# Archive workbooks to historical record
tar -czf "archived-workbooks-spec-000-$(date +%Y%m%d).tar.gz" workbooks/
mv "archived-workbooks-spec-000-*.tar.gz" ../archived/
```

---

## 13. Future Enhancements

### 13.1 Triple Persistence Active

Cuando se active Neo4j + Ollama:

```
_melquisedec/domain/
├── markdown/           # SOURCE OF TRUTH (no cambia)
├── cypher/             # Generated (sync-all.sh)
├── embeddings/         # Generated (sync-all.sh)
├── neo4j-data/         # Neo4j database files
└── ollama-models/      # Ollama models cache
```

---

### 13.2 Multi-Spec Workspaces

```
00-define/
├── 0-define-daath-zen-framework/       # spec-000
├── 0-define-ontologies-research/       # spec-002
└── 0-define-embeddings-benchmarking/   # spec-005
```

Cada workspace independiente, outputs consolidados en `_melquisedec/domain/`.

---

## 14. Related Documents

- **Product Specification**: [product.md](./product.md)
- **Technical Specification**: [tech.md](./tech.md)
- **Requirements**: [../010-define/requirements.md](../010-define/requirements.md)
- **Design Decisions**: [../010-define/design.md](../010-define/design.md)
- **Tasks & Timeline**: [../010-define/tasks.md](../010-define/tasks.md)

---

## 15. Summary of Key Paths

| Component | Path | Purpose |
|-----------|------|---------|
| **Workspace** | `00-define/0-define-daath-zen-framework/` | Investigación activa |
| **Inputs** | `00-define/.../0-context/` | Fuentes de investigación |
| **Steering** | `00-define/.../1-steering/` | Governance docs |
| **Workbooks** | `00-define/.../workbooks/` | IMRAD + Academic Research |
| **Spec Formal** | `.spec-workflow/specs/spec-000/` | Requirements, design, tasks |
| **Domain Final** | `_melquisedec/domain/markdown/` | Contenidos-atómicos consolidados |
| **Context Final** | `_melquisedec/context/` | Frameworks, concepts |

---

**Version History**:
- v0.1.0 (2026-01-10): Initial structure con workspace 00-define/ corregido
