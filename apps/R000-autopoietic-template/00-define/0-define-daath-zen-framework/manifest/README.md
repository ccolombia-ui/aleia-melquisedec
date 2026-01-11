# Manifest: SPEC-000 Investigation Daath-Zen Framework

## Overview

Este directorio centraliza todos los inputs necesarios para ejecutar SPEC-000: investigación académica para ampliar el dominio de conocimiento del proyecto ALEIA-Melquisedec.

**Propósito**: Proveer contexto inicial (legacy analysis + templates + code patterns) para que HYPATIA y SALOMON puedan ejecutar los 6 workbooks de investigación sin partir de cero.

**Estructura**:
```
manifest/
├── README.md                          ← Este archivo (índice)
├── legacy-inputs/                     ← Análisis previos (contexto)
│   ├── INVESTIGACION-BIDIRECCIONAL-template-spec-daath.md
│   ├── ANALISIS-PROPUESTA-spec-000-dominio-vivo.md
│   └── ANALISIS-PROFUNDO-academic-research-vs-imrad.md
├── templates-daath-zen/               ← Templates base (6 variantes)
│   ├── daath-zen-requirements.md
│   ├── daath-zen-design.md
│   ├── daath-zen-tasks.md
│   ├── daath-zen-product.md
│   ├── daath-zen-tech.md
│   └── daath-zen-structure.md
└── code-analysis/                     ← Análisis de código spec-workflow-mcp
    ├── mcp-server-architecture.md
    ├── approval-system-flow.md
    └── implementation-log-patterns.md
```

---

## 1. Legacy Inputs

Análisis previos que documentan el contexto, propuestas, y decisiones metodológicas para SPEC-000.

### 1.1. INVESTIGACION-BIDIRECCIONAL-template-spec-daath.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-08
**Palabras**: ~15,000

**Contenido**:
- Investigación bidireccional: Templates DAATH-ZEN ↔ spec-workflow-mcp
- Análisis de plantillas compiladas (product.md, tech.md, structure.md)
- Propuesta de workbooks RBM (Result-Based Management)
- Sistema de herencia de templates

**Uso en SPEC-000**: Contexto sobre el sistema de templates que se está investigando.

---

### 1.2. ANALISIS-PROPUESTA-spec-000-dominio-vivo.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-09
**Palabras**: ~8,000

**Contenido**:
- Propuesta de SPEC-000 como foundation specification
- Concepto de "dominio vivo" (evolución autopoiética del conocimiento)
- Workspaces: 00-define/ para investigación activa
- Separación entre investigación (00-define/), gobernanza (.spec-workflow/), y outputs (_melquisedec/domain/)

**Uso en SPEC-000**: Rationale para la arquitectura de workspaces y concepto de dominio vivo.

---

### 1.3. ANALISIS-PROFUNDO-academic-research-vs-imrad.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-10
**Palabras**: ~28,000

**Contenido**:
- **Parte 1**: Explicación "for dummies" de investigación académica
- **Parte 2-3**: Comparación Academic Research vs IMRAD
- **Parte 4-8**: Mejores prácticas, validación, metadata, ejemplos
- **Parte 9**: Gobernanza de artefactos (spec:issue, spec:owner, Pull Request system)

**Uso en SPEC-000**: Fundamento metodológico completo para los 6 workbooks.

---

## 2. Templates DAATH-ZEN

Templates base que definen la estructura de los 6 tipos de artefactos (requirements, design, tasks, product, tech, structure). Estos templates sirven como referencia para entender qué estructura deben seguir los outputs de los workbooks.

### 2.1. daath-zen-requirements.md

**Propósito**: Template para documentos de requisitos
**Secciones**:
- Metadata (Dublin Core + spec extensions)
- Functional Requirements (REQ-XXX-01, REQ-XXX-02, ...)
- Non-Functional Requirements (Performance, Maintainability, Usability, Scalability)
- Acceptance Criteria
- Traceability Matrix

**Uso en SPEC-000**: SALOMON puede referenciar este template al escribir workbooks IMRAD sobre requirements.

---

### 2.2. daath-zen-design.md

**Propósito**: Template para documentos de diseño
**Secciones**:
- Metadata
- Overview
- Architecture Decision Records (ADRs)
- System Components Design
- Data Flow & Integration
- NFRs Design
- Risk Analysis & Mitigation
- Testing Strategy
- Traceability Matrix

**Uso en SPEC-000**: SALOMON puede referenciar al escribir sobre arquitectura.

---

### 2.3. daath-zen-tasks.md

**Propósito**: Template para planes de implementación
**Secciones**:
- Metadata
- Overview (estimación total, fases)
- Tasks (desglose con owner, files, requirements, estimación, prioridad, dependencies, subtasks, validation, success criteria)
- Milestones & Checkpoints
- Risk Management
- Success Metrics
- Traceability Matrix

**Uso en SPEC-000**: SALOMON puede referenciar al escribir sobre metodologías de planificación.

---

### 2.4. daath-zen-product.md

**Propósito**: Template para documentos de producto
**Secciones**:
- Metadata
- Vision & Strategy
- User Stories & Use Cases
- Feature Specifications
- Product Roadmap
- Success Metrics

**Uso en SPEC-000**: Referencia para entender product thinking.

---

### 2.5. daath-zen-tech.md

**Propósito**: Template para documentos técnicos
**Secciones**:
- Metadata
- Tech Stack
- Development Environment Setup
- Deployment Architecture
- CI/CD Pipeline
- Monitoring & Observability
- Security & Compliance

**Uso en SPEC-000**: Referencia para entender tech stack decisions.

---

### 2.6. daath-zen-structure.md

**Propósito**: Template para documentos de estructura
**Secciones**:
- Metadata
- Project Structure Overview
- Directory Organization
- File Naming Conventions
- Module Dependencies
- Configuration Management

**Uso en SPEC-000**: Referencia para entender project organization.

---

## 3. Code Analysis (spec-workflow-mcp)

Análisis del código fuente de spec-workflow-mcp para entender patrones de implementación actuales.

### 3.1. mcp-server-architecture.md

**Contenido**:
- Arquitectura del servidor MCP
- Tools disponibles (approvals, log-implementation, spec-status, spec-workflow-guide)
- Protocolo de comunicación (JSON-RPC)
- Gestión de estado (dashboard web)

**Uso en SPEC-000**: HYPATIA puede analizar patterns de implementación en DDD workbook.

---

### 3.2. approval-system-flow.md

**Contenido**:
- Flujo del sistema de aprobaciones
- Estados: pending → approved/rejected/needs-revision
- Formato de approval requests (filePath, category, type, title)
- Dashboard interface para review

**Uso en SPEC-000**: SALOMON puede analizar governance patterns en Metadata Governance workbook.

---

### 3.3. implementation-log-patterns.md

**Contenido**:
- Patrones de logging de implementación
- Formato de logs (task ID, status, artifacts created)
- Traceability entre tasks y outputs
- Metrics tracking (LOC, files created, tests passed)

**Uso en SPEC-000**: SALOMON puede analizar tracking patterns en Validation Strategies workbook.

---

## Usage Instructions

### For HYPATIA (Academic Research Agent)

**Before starting Task-000-004 (DDD Workbook)**:
1. Read `legacy-inputs/ANALISIS-PROFUNDO-academic-research-vs-imrad.md` Parte 2-3 (metodología)
2. Read `code-analysis/mcp-server-architecture.md` (código a analizar)
3. Reference `templates-daath-zen/daath-zen-design.md` (estructura de referencia)

**Before starting Task-000-005 (IMRAD Literature Workbook)**:
1. Read `legacy-inputs/ANALISIS-PROFUNDO-academic-research-vs-imrad.md` Parte 2-3 (metodología IMRAD)
2. Collect external IMRAD sources (Sollaci & Pereira 2004, scientific writing guides)

### For SALOMON (IMRAD Synthesizer Agent)

**Before starting Task-000-006 (Research Synthesis)**:
1. Read all atomics from HYPATIA workbooks (Task-000-004, Task-000-005)
2. Read `legacy-inputs/ANALISIS-PROPUESTA-spec-000-dominio-vivo.md` (dominio vivo concept)
3. Reference `templates-daath-zen/` for structure examples

**Before starting Task-000-007 (Metadata Governance)**:
1. Read `legacy-inputs/ANALISIS-PROFUNDO-academic-research-vs-imrad.md` Parte 9 (gobernanza)
2. Read `code-analysis/approval-system-flow.md` (governance patterns)

**Before starting Task-000-008 (Triple Persistence)**:
1. Read `legacy-inputs/ANALISIS-PROPUESTA-spec-000-dominio-vivo.md` (workspace separation)
2. Read Docker Compose files in repo root (Neo4j + Redis setup)

**Before starting Task-000-009 (Validation Strategies)**:
1. Read `code-analysis/implementation-log-patterns.md` (tracking patterns)
2. Read validation tool implementations (when available)

### For MORPHEUS (Atomics Curator)

**Before starting Task-000-010 (Cross-Workbook Validation)**:
1. Read all 6 workbooks README.md files (metadata)
2. Collect all atomics from `3-atomics/` folders
3. Run validation tools on each workbook

### For ALMA (Publisher & Validator)

**Before starting Task-000-011 (Publication)**:
1. Read `validation-report.md` from MORPHEUS (Task-000-010)
2. Verify 100% pass rate before copying to `_melquisedec/domain/`
3. Document manual copy process in `WORKSPACE-SETUP.md`

---

## References

- [SPEC-000 Requirements](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/requirements.md)
- [SPEC-000 Design](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/design.md)
- [SPEC-000 Tasks](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/tasks.md)
- [Workbooks Directory](../workbooks/)
- [Dublin Core Metadata Initiative](https://www.dublincore.org/)
- [ISO 15836:2009](https://www.iso.org/standard/52142.html) - Dublin Core Standard

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-01-11 | GitHub Copilot (Claude Sonnet 4.5) | Initial manifest README |

---

**End of Manifest README**
