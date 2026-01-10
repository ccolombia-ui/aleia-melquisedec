# Unified Research Template Design v4.0.0

```yaml
---
id: "ADR-003-unified-template-system"
version: "4.0.0"
date: "2026-01-09"
status: "DRAFT"
authors: ["MELQUISEDEC", "COPILOT"]
supersedes: ["archive/templates/tasks.md"]
---
```

## Executive Summary

Este documento define la arquitectura del **Sistema de Templates Unificado** para crear apps de tipo:
- **Methodology**: Investigaciones académicas/técnicas
- **App**: Aplicaciones de software
- **Social-Project**: Proyectos de impacto social

### Principios de Diseño

| Principio | Descripción |
|-----------|-------------|
| **Composición** | Cada spec-type COMPONE artifacts, no los define inline |
| **Separación** | Steering ≠ Phases ≠ Artifacts ≠ Prompts |
| **Versionado** | Todo template tiene versión semántica y changelog |
| **Propagación** | Mejoras en `_templates/` se heredan automáticamente |
| **Minimalismo** | Solo crear lo necesario, carpetas on-demand |

---

## Gap Analysis: Estado Actual vs Deseado

### GAP-001: Template Monolítico
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Ubicación | `archive/templates/tasks.md` (1551 líneas) | Múltiples archivos modulares |
| Problema | Mezcla TODAS las phases en un archivo | Cada phase tiene su propio tasks.md |
| Impacto | Difícil de mantener, no componible | Modular, reutilizable |

### GAP-002: Formato Incompatible con spec-workflow-mcp
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Formato | `### X.Y. [Task Name]` con sub-items | `- [ ] X.Y. Task name` con indented items |
| Problema | Dashboard muestra 0 tasks | Tasks parseadas correctamente |
| Solución | Migrar a formato estándar spec-workflow-mcp |

### GAP-003: Metadata DAATH-ZEN Embebida
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Ubicación | Inline en cada task | Biblioteca de prompts versionados |
| Problema | No evolucionan, redundancia | Prompts como first-class citizens |
| Solución | Sistema `@prompt-ref` en tasks.md |

### GAP-004: Sin Separación Spec-Type vs Artifact
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Estructura | Todo junto | `spec-types/` + `artifacts/` separados |
| Problema | No se pueden reutilizar artifacts | Artifacts componibles |

### GAP-005: Checkpoints como Tasks
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Implementación | Tasks CK-01, CK-02 en tasks.md | Approval gates en spec-workflow |
| Problema | No bloquean siguiente phase | Gates bloquean hasta approval |

### GAP-006: Sin Versionado de Templates
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Cambios | Overwrite sin tracking | Versión semántica + changelog |
| Propagación | Manual | Automática a nuevos specs |

### GAP-007: Sin Índice de Artefactos
| Aspecto | Actual | Deseado |
|---------|--------|---------|
| Tracking | Ninguno | `outputs/index.yaml` con todos los artifacts |

---

## Arquitectura Propuesta

### Estructura de Directorios

```
_templates/                              # GLOBAL - Propagable
├── manifest.yaml                        # Índice global
│
├── spec-types/                          # Tipos de spec
│   ├── research-methodology/
│   │   ├── manifest.yaml                # Config: phases, artifacts, checkpoints
│   │   ├── steering/
│   │   │   ├── product.tpl.md
│   │   │   ├── tech.tpl.md
│   │   │   └── structure.tpl.md
│   │   └── phases/
│   │       ├── 000-bootstrap/
│   │       │   ├── tasks.tpl.md         # spec-workflow-mcp compatible
│   │       │   └── artifacts.yaml       # Qué artifacts genera
│   │       ├── 001-literature/
│   │       │   ├── tasks.tpl.md
│   │       │   └── artifacts.yaml
│   │       ├── 002-atomic/
│   │       ├── 003-workbook/
│   │       ├── 004-evaluate/
│   │       └── 005-outputs/
│   │
│   ├── app/                             # Template para apps de software
│   │   └── ...
│   │
│   └── social-project/                  # Template para proyectos sociales
│       └── ...
│
├── artifacts/                           # Tipos de artefacto (reutilizables)
│   ├── _schema.yaml                     # Validación JSON Schema
│   ├── book/
│   │   ├── metadata.tpl.yaml
│   │   ├── content.tpl.md
│   │   └── prompt.yaml
│   ├── paper/
│   ├── framework/
│   ├── notes/
│   ├── concept/
│   ├── spec/
│   └── dataset/
│
└── prompts/                             # Biblioteca de prompts versionados
    ├── _registry.yaml                   # Índice de prompts
    ├── melquisedec/
    │   └── init-structure.v1.yaml
    ├── hypatia/
    │   ├── search-sources.v2.yaml
    │   ├── document-source.v1.yaml
    │   └── atomize-concept.v2.yaml
    ├── salomon/
    │   ├── comparative-analysis.v1.yaml
    │   └── decision-matrix.v1.yaml
    ├── morpheus/
    │   └── generate-dataset.v1.yaml
    └── alma/
        ├── publish-artifact.v1.yaml
        └── create-index.v1.yaml
```

---

## Especificaciones Detalladas

### 1. Manifest Global (`_templates/manifest.yaml`)

```yaml
# _templates/manifest.yaml
version: "4.0.0"
last_updated: "2026-01-09"

spec_types:
  - id: "research-methodology"
    version: "1.0.0"
    path: "spec-types/research-methodology/"
    description: "Template para investigaciones académicas/técnicas"

  - id: "app"
    version: "1.0.0"
    path: "spec-types/app/"
    description: "Template para aplicaciones de software"

  - id: "social-project"
    version: "1.0.0"
    path: "spec-types/social-project/"
    description: "Template para proyectos de impacto social"

artifacts:
  - id: "book"
    path: "artifacts/book/"
  - id: "paper"
    path: "artifacts/paper/"
  # ...

prompts:
  registry: "prompts/_registry.yaml"
```

### 2. Spec-Type Manifest (`spec-types/research-methodology/manifest.yaml`)

```yaml
# spec-types/research-methodology/manifest.yaml
id: "research-methodology"
version: "1.0.0"
name: "Research Methodology"
description: "Template para investigaciones usando DSR + DAATH-ZEN"

# Variables configurables al crear nueva research
parameters:
  - name: "research_name"
    type: "string"
    required: true
    pattern: "^[a-z0-9-]+$"

  - name: "research_full_name"
    type: "string"
    required: true

  - name: "research_type"
    type: "enum"
    values: ["methodology", "framework", "analysis", "case-study"]
    default: "methodology"

  - name: "min_sources"
    type: "integer"
    default: 10

  - name: "min_atomics"
    type: "integer"
    default: 20

# Steering documents
steering:
  - template: "steering/product.tpl.md"
    output: "steering/product.md"
  - template: "steering/tech.tpl.md"
    output: "steering/tech.md"
  - template: "steering/structure.tpl.md"
    output: "steering/structure.md"

# Phases (mapean a DSR)
phases:
  - id: "000-bootstrap"
    name: "Bootstrap"
    dsr_phase: "PROBLEM"
    spec_name: "bootstrap"
    artifacts: ["ISSUE.yaml", "README.md"]
    checkpoint: null

  - id: "001-literature"
    name: "Literature Review"
    dsr_phase: "PROBLEM → DESIGN"
    spec_name: "literature-review"
    artifacts: ["book/*", "paper/*", "framework/*", "notes/*"]
    checkpoint:
      id: "CK-LIT"
      criteria:
        min_sources: "{{min_sources}}"
        sources_documented: true
      require_approval: true

  - id: "002-atomic"
    name: "Knowledge Atomization"
    dsr_phase: "DESIGN"
    spec_name: "knowledge-atomization"
    artifacts: ["concept/*", "spec/*"]
    checkpoint:
      id: "CK-ATOMIC"
      criteria:
        min_atomics: "{{min_atomics}}"
        relationships_mapped: true
      require_approval: true

  - id: "003-workbook"
    name: "Analysis & Synthesis"
    dsr_phase: "BUILD"
    spec_name: "analysis-synthesis"
    artifacts: ["analysis/*", "notebook/*"]
    checkpoint:
      id: "CK-ANALYSIS"
      criteria:
        comparative_analysis: true
        synthesis_complete: true
      require_approval: false

  - id: "004-evaluate"
    name: "Evaluation"
    dsr_phase: "EVALUATE"
    spec_name: "evaluation"
    artifacts: ["evaluation/*", "metrics/*"]
    checkpoint:
      id: "CK-EVAL"
      criteria:
        evaluation_complete: true
      require_approval: true

  - id: "005-outputs"
    name: "Publish Outputs"
    dsr_phase: "LESSONS"
    spec_name: "publish-outputs"
    artifacts: ["index.yaml", "exports/*"]
    checkpoint:
      id: "CK-PUBLISH"
      criteria:
        index_created: true
        exports_ready: true
      require_approval: true
```

### 3. Phase Tasks Template (`phases/001-literature/tasks.tpl.md`)

```markdown
# Tasks: {{phase.name}}

> **Spec**: {{spec_name}}
> **Phase**: {{phase.id}} - {{phase.name}}
> **DSR**: {{phase.dsr_phase}}
> **Checkpoint**: {{phase.checkpoint.id | default("None")}}

---

## 1. Literature Search

- [ ] 1.1. Identify canonical sources
  - File: {{research_name}}/{{phase.id}}/sources.yaml
  - _Requirements: REQ-LIT-001_
  - _Prompt: @hypatia/search-sources.v2_
  - _Params: research_name="{{research_name}}", min_sources={{min_sources}}_

- [ ] 1.2. Document source content
  - File: {{research_name}}/{{phase.id}}/{type}/{id}/content.md
  - _Requirements: REQ-LIT-002_
  - _Prompt: @hypatia/document-source.v1_

## 2. Organization

- [ ] 2.1. Organize by type (book, paper, framework, notes)
  - File: {{research_name}}/{{phase.id}}/
  - _Requirements: REQ-LIT-003_
  - _Prompt: @melquisedec/organize-artifacts.v1_

## 3. Checkpoint: {{phase.checkpoint.id}}

- [ ] 3.1. Validate literature phase
  - File: {{research_name}}/.melquisedec/{{phase.checkpoint.id}}.yaml
  - _Requirements: CK-LIT_
  - _Prompt: @melquisedec/validate-checkpoint.v1_
  - _Params: checkpoint_id="{{phase.checkpoint.id}}", criteria={{phase.checkpoint.criteria | tojson}}_
```

### 4. Prompt Library (`prompts/hypatia/search-sources.v2.yaml`)

```yaml
# prompts/hypatia/search-sources.v2.yaml
id: "hypatia/search-sources"
version: "2.0.0"
rostro: "HYPATIA"
category: "research"
purpose: "Identificar fuentes canónicas para investigación"

# Parámetros que acepta el prompt
parameters:
  - name: "research_name"
    type: "string"
    required: true
    description: "Nombre de la investigación"

  - name: "min_sources"
    type: "integer"
    default: 10
    description: "Mínimo de fuentes a identificar"

  - name: "min_peer_reviewed"
    type: "integer"
    default: 5
    description: "Mínimo de fuentes peer-reviewed"

  - name: "domains"
    type: "array"
    default: []
    description: "Dominios de búsqueda"

# MCPs requeridos
mcps:
  base: ["neo4j", "memory"]
  specialized: ["brave-search", "arxiv", "context7"]

# MCP Workflow Strategy
workflow:
  thinking_mode: "none"  # search task, no deep thinking needed
  activation: ["activate_brave_search_tools", "activate_library_documentation_tools"]
  parallel: ["arxiv search", "brave-search", "context7"]
  sequential: ["aggregate", "deduplicate", "filter", "rank", "write"]
  error_handling: "If <5 sources, expand query with synonyms"

# El prompt ejecutable (Jinja2 template)
prompt: |
  Role: Investigadora HYPATIA
  Task: Identificar ≥{{min_sources}} fuentes canónicas para "{{research_name}}"

  Context:
  - Domains: {{domains | join(", ") | default("general")}}
  - Quality: ≥{{min_peer_reviewed}} peer-reviewed

  Search Strategy:
  1. PARALLEL: Execute simultaneously
     - arxiv: "{{research_name}}" + related academic terms
     - brave-search: "{{research_name}} frameworks best practices"
     - context7: resolve-library-id for known libraries

  2. SEQUENTIAL: Process results
     - Aggregate all results
     - Deduplicate by DOI/URL
     - Filter: peer-reviewed, recent (5 years), high-quality
     - Rank by relevance to research questions

  Output Format (sources.yaml):
  ```yaml
  sources:
    - id: "{type}-{slug}"
      type: "paper|book|framework|notes"
      title: "Title"
      authors: ["Author 1", "Author 2"]
      year: 2024
      doi: "10.1234/xxx"  # if available
      url: "https://..."
      peer_reviewed: true|false
      relevance: "high|medium|low"
      notes: "Why this source is relevant"
  ```

  Restrictions:
  - Prioritize peer-reviewed sources
  - Include DOI when available
  - Verify URLs are accessible
  - Document relevance rationale

# Criterios de éxito (validables)
success_criteria:
  - "sources.yaml created"
  - "≥{{min_sources}} sources identified"
  - "≥{{min_peer_reviewed}} peer-reviewed sources"
  - "All URLs verified accessible"
  - "Each source has relevance documented"

# Output esperado
output:
  file: "{{research_name}}/001-literature/sources.yaml"
  schema: "artifacts/_schemas/sources.schema.yaml"

# Changelog
changelog:
  - version: "2.0.0"
    date: "2026-01-09"
    changes:
      - "Added context7 for library documentation"
      - "Parallel search strategy"
      - "Enhanced output format with relevance field"
  - version: "1.0.0"
    date: "2026-01-01"
    changes:
      - "Initial version"
```

### 5. Artifact Template (`artifacts/concept/`)

```yaml
# artifacts/concept/metadata.tpl.yaml
id: "concept-{{slug}}"
is_a: "concept/{{category}}"
version: "1.0.0"
created: "{{current_date}}"

# Dublin Core
dc:
  title: "{{title}}"
  creator: "{{rostro}}"
  date: "{{current_date}}"
  source: "{{source_id}}"
  subject: {{tags | tojson}}
  description: "{{description}}"
  type: "concept"
  format: "text/markdown"
  language: "{{language | default('es')}}"

# HKM Extensions
hkm:
  atomic: true
  max_words: 500
  source_ref: "{{source_id}}"
  related: {{related | default([]) | tojson}}

# DAATH-ZEN
daath:
  rostro: "{{rostro}}"
  phase: "002-atomic"
  checkpoint: "CK-ATOMIC"
```

```markdown
<!-- artifacts/concept/content.tpl.md -->
# {{title}}

## Definition

{{definition}}

## Context

{{context}}

## Examples

{{examples}}

## Related Concepts

{% for rel in related %}
- [[{{rel.id}}]] - {{rel.relationship}}
{% endfor %}

---

**Source**: {{source_id}}
**Created**: {{current_date}}
**Rostro**: {{rostro}}
```

### 6. Outputs Index (`005-outputs/index.yaml`)

```yaml
# apps/research-{name}/005-outputs/index.yaml
id: "outputs-index"
research: "{{research_name}}"
version: "{{version}}"
generated: "{{current_date}}"

# Resumen de artefactos generados
summary:
  total_artifacts: {{artifacts | length}}
  by_phase:
    001-literature: {{artifacts | selectattr("phase", "equalto", "001-literature") | list | length}}
    002-atomic: {{artifacts | selectattr("phase", "equalto", "002-atomic") | list | length}}
    003-workbook: {{artifacts | selectattr("phase", "equalto", "003-workbook") | list | length}}
    004-evaluate: {{artifacts | selectattr("phase", "equalto", "004-evaluate") | list | length}}

# Lista de artefactos
artifacts:
  # Phase 001-literature
  - id: "sources"
    type: "sources-list"
    phase: "001-literature"
    path: "001-literature/sources.yaml"
    count: {{sources_count}}

  # Papers documentados
  {% for paper in papers %}
  - id: "{{paper.id}}"
    type: "paper"
    phase: "001-literature"
    path: "001-literature/paper/{{paper.id}}/"
    title: "{{paper.title}}"
  {% endfor %}

  # Concepts atomizados
  {% for concept in concepts %}
  - id: "{{concept.id}}"
    type: "concept"
    phase: "002-atomic"
    path: "002-atomic/concepts/{{concept.id}}.md"
    title: "{{concept.title}}"
    source: "{{concept.source}}"
  {% endfor %}

# Exports disponibles
exports:
  - id: "graph-ready"
    format: "yaml-ld"
    path: "exports/graph-ready/"
    description: "Neo4j-ready YAML files"

  - id: "report"
    format: "pdf"
    path: "exports/report.pdf"
    description: "Final research report"

# Métricas
metrics:
  sources: {{sources_count}}
  atomics: {{concepts | length}}
  relationships: {{relationships_count}}
  coverage: "{{coverage_percentage}}%"
```

---

## Flujo de Uso

### Crear Nueva Research

```bash
# 1. Ejecutar comando de creación
create-research \
  --type methodology \
  --name "neo4j-llamaindex-architecture" \
  --full-name "Neo4j + LlamaIndex Architecture Best Practices"

# 2. El sistema:
#    a. Lee _templates/spec-types/research-methodology/manifest.yaml
#    b. Crea apps/research-neo4j-llamaindex-architecture/
#    c. Crea .spec-workflow/ con steering docs procesados
#    d. Crea specs/ por cada phase
#    e. Registra en dashboard
```

### Estructura Generada

```
apps/research-neo4j-llamaindex-architecture/
├── .spec-workflow/
│   ├── config.toml
│   ├── steering/
│   │   ├── product.md          # Procesado desde product.tpl.md
│   │   ├── tech.md
│   │   └── structure.md
│   └── specs/
│       ├── bootstrap/
│       │   ├── requirements.md
│       │   ├── design.md
│       │   └── tasks.md        # Parseado correctamente
│       ├── literature-review/
│       ├── knowledge-atomization/
│       ├── analysis-synthesis/
│       ├── evaluation/
│       └── publish-outputs/
├── 000-bootstrap/
├── 001-literature/
├── 002-atomic/
├── 003-workbook/
├── 004-evaluate/
├── 005-outputs/
│   └── index.yaml              # Generado al final
├── .melquisedec/
│   └── checkpoints/
└── README.md
```

### Ejecutar una Task

```markdown
# En specs/literature-review/tasks.md

- [ ] 1.1. Identify canonical sources
  - File: 001-literature/sources.yaml
  - _Requirements: REQ-LIT-001_
  - _Prompt: @hypatia/search-sources.v2_
  - _Params: research_name="neo4j-llamaindex-architecture", min_sources=15_
```

**El agente**:
1. Lee el prompt desde `_templates/prompts/hypatia/search-sources.v2.yaml`
2. Sustituye parámetros
3. Ejecuta con MCPs especificados
4. Valida success_criteria
5. Escribe output

---

## Migración desde Sistema Actual

### Archivos a Deprecar

| Archivo Actual | Acción | Reemplazo |
|----------------|--------|-----------|
| `_meta/best-practices.md` | ARCHIVE | `_templates/prompts/` |
| `_meta/GUIA_RAPIDA.md` | ARCHIVE | `_templates/README.md` |
| `_meta/RESUMEN_SISTEMA_COMPLETO.md` | ARCHIVE | Este documento |
| `archive/templates/tasks.md` (1551 líneas) | ARCHIVE | `_templates/spec-types/` |

### Plan de Migración

1. **Phase 1**: Crear estructura `_templates/` (este diseño)
2. **Phase 2**: Migrar prompts a biblioteca versionada
3. **Phase 3**: Crear spec-types para methodology, app, social-project
4. **Phase 4**: Actualizar `mcp.json` con script de creación
5. **Phase 5**: Deprecar archivos legacy

---

## Compatibilidad con spec-workflow-mcp

### Formato de Tasks (CRÍTICO)

```markdown
# ✅ CORRECTO - spec-workflow-mcp parsea esto
- [ ] 1.1. Task title here
  - File: path/to/file
  - _Requirements: REQ-001_
  - _Prompt: @rostro/prompt-name.v1_

# ❌ INCORRECTO - 0 tasks detectadas
### 1.1. Task title here
- [ ] Sub-item
- [ ] Sub-item
```

### Checkpoints como Approval Gates

```markdown
# En tasks.md - última task de la phase
- [ ] 3.1. Validate checkpoint CK-LIT
  - File: .melquisedec/CK-LIT.yaml
  - _Requirements: CHECKPOINT_
  - _Prompt: @melquisedec/validate-checkpoint.v1_

# Luego en spec-workflow dashboard:
# → Request approval para CK-LIT
# → Usuario aprueba
# → Siguiente phase se desbloquea
```

---

## Changelog

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 4.0.0 | 2026-01-09 | Diseño inicial unificado |

---

## Referencias

- [spec-workflow-mcp Documentation](https://github.com/pimzino/spec-workflow-mcp)
- [DAATH-ZEN Manifiesto](../manifiesto/bereshit-v3.0.0.md)
- [DSR Methodology](../manifiesto/02-arquitectura/)
