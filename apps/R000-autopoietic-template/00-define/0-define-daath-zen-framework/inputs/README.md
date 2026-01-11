# Inputs: SPEC-000 Investigation Daath-Zen Framework

## Overview

Este directorio centraliza **todos los inputs necesarios** para ejecutar SPEC-000: investigación académica para ampliar el dominio de conocimiento del proyecto ALEIA-Melquisedec.

**Propósito**: Proveer contexto completo (steering documents + foundational research + legacy analysis + baseline templates + code patterns) para que HYPATIA y SALOMON puedan ejecutar los 6 workbooks de investigación sin partir de cero.

**Principio de Organización**: Separación semántica por **propósito y mutabilidad**:
- **steering/**: Manifesto real (contexto inmutable del proyecto)
- **research/**: Investigación fundacional y análisis previos (evolución histórica)
- **baseline/**: Línea base de templates (punto de partida existente)

**Estructura**:
```
inputs/
├── README.md                          ← Este archivo (índice con claridad semántica)
├── steering/                          ← TRUE MANIFEST (contexto inmutable del proyecto)
│   ├── product.md                     → Qué construimos (visión, propuesta valor)
│   ├── tech.md                        → Cómo lo construimos (tech stack, arquitectura)
│   └── structure.md                   → Cómo lo organizamos (directorios, governance)
├── research/                          ← INVESTIGACIÓN (fundacional + histórica)
│   ├── preliminary/                   → Investigación fundacional crítica
│   │   ├── raw-manifiesto.md          → Manifiesto MELQUISEDEC completo (bridge concept)
│   │   ├── ANALISIS-APPROACH-ATOMICO.md → Propuesta metodología minimalista configurable
│   │   └── DIAGRAMAS-WORKFLOW-MCP.md  → Diagramas visuales completos (accessibility)
│   ├── legacy-proposals/              → Análisis históricos (contexto evolución)
│   │   ├── INVESTIGACION-BIDIRECCIONAL-template-spec-daath.md
│   │   ├── ANALISIS-PROPUESTA-spec-000-dominio-vivo.md
│   │   └── ANALISIS-PROFUNDO-academic-research-vs-imrad.md
│   └── code-analysis/                 → Análisis código spec-workflow-mcp
│       ├── mcp-server-architecture.md
│       ├── approval-system-flow.md
│       └── implementation-log-patterns.md
├── baseline/                          ← LÍNEA BASE (templates existentes antes de SPEC-000)
│   └── templates-daath-zen/           → 6 templates base (requirements, design, tasks, etc.)
│       ├── daath-zen-requirements.md
│       ├── daath-zen-design.md
│       ├── daath-zen-tasks.md
│       ├── daath-zen-product.md
│       ├── daath-zen-tech.md
│       └── daath-zen-structure.md
└── templates/                         ← TEMPLATES (generados por SPEC-000)
    ├── academic-research-template/    → Metodología Academic Research (5 folders)
    └── imrad-template/                → Metodología IMRAD (7 files)
```

---

## 1. Steering (True Manifest)

**Concepto**: El **true manifest** del proyecto - contexto inmutable que define QUÉ, CÓMO, y DÓNDE estamos construyendo.

### 1.1. product.md

**Propósito**: Define la visión del producto, propuesta de valor, y objetivos estratégicos.

**Contenido clave**:
- Visión del proyecto ALEIA-Melquisedec
- Propuesta de valor de daath-zen framework
- Objetivos de negocio y métricas de éxito

**Uso en SPEC-000**: SALOMON puede referenciar para entender el "por qué" detrás de las decisiones de arquitectura.

### 1.2. tech.md

**Propósito**: Define el tech stack, arquitectura técnica, y decisiones de implementación.

**Contenido clave**:
- Stack: Python 3.11+, TypeScript, Neo4j, RDF/JSON-LD
- MCP servers (spec-workflow-mcp, copilot-memory)
- Patrones: DDD, Event Sourcing, CQRS

**Uso en SPEC-000**: HYPATIA puede referenciar para entender constraints técnicos al analizar implementaciones.

### 1.3. structure.md

**Propósito**: Define la organización de directorios, governance, y flujos de trabajo.

**Contenido clave**:
- Estructura monorepo (apps/, packages/, docs/)
- Separación 00-define/ (workspace investigación) vs .spec-workflow/ (governance)
- Convenciones de nomenclatura y metadata

**Uso en SPEC-000**: Fundamento para entender dónde colocar artefactos y cómo navegar el proyecto.

---

## 2. Research (Foundational + Historical)

**Concepto**: Investigación fundacional crítica + análisis históricos que documentan la evolución del proyecto.

### 2.1. Research - Preliminary (Investigación Fundacional)

**Concepto**: Los 3 archivos **CRÍTICOS** que definen los cimientos conceptuales de daath-zen. Sin estos, SPEC-000 parte de cero.

#### 2.1.1. raw-manifiesto.md

**Autor**: Unknown (legacy foundational document)
**Fecha**: Unknown
**Líneas**: 17,142
**Versión**: v4.3.1

**Contenido**:
- **Bridge Concept**: Manifiesto MELQUISEDEC → daath-zen-root → spec-workflow-mcp
- Definición completa de daath-zen framework
- Sequence diagrams: Project initialization, workbook creation, artifact generation
- Metadata structures (Dublin Core, PROV-O, FOAF)

**Uso en SPEC-000**: Definición fundacional del "puente ejecutable" que SPEC-000 está investigando.

**Por qué es crítico**: Sin este archivo, no entendemos QUÉ es daath-zen ni CÓMO conecta el Manifiesto con spec-workflow-mcp.

#### 2.1.2. ANALISIS-APPROACH-ATOMICO.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-08
**Líneas**: 489

**Contenido**:
- Propuesta de enfoque **atómico vs monolítico**
- Principios Zettelkasten aplicados a documentación técnica
- Metodología issue-driven (1 issue = 1 PR = 1 cambio atómico)
- Métricas cuantificadas: +400% parallelization, -93.75% review time, +100% trackability

**Uso en SPEC-000**: Rationale para la arquitectura modular y configurable de daath-zen.

**Por qué es crítico**: Define la **filosofía minimalista** que permite customización sin rigidez.

#### 2.1.3. DIAGRAMAS-WORKFLOW-MCP.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-08
**Líneas**: 833

**Contenido**:
- Diagramas Mermaid v8.8.0 completos (workflows, estructuras, estados, arquitectura)
- 4 secciones:
  1. Workflows (main/sub/impl/steering)
  2. Structures (YAML relationships)
  3. States (spec lifecycle)
  4. Architecture (components)

**Uso en SPEC-000**: Visualizaciones críticas para "principiantes" (narrativa accessibility-first).

**Por qué es crítico**: "nuestra narrativa siempre es para principiantes" - los diagramas son **no negociables** para comprensión.

### 2.2. Research - Legacy Proposals (Análisis Históricos)

**Concepto**: Análisis previos que documentan propuestas, decisiones metodológicas, y contexto histórico para SPEC-000.

#### 2.2.1. INVESTIGACION-BIDIRECCIONAL-template-spec-daath.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-08
**Palabras**: ~15,000

**Contenido**:
- Investigación bidireccional: Templates DAATH-ZEN ↔ spec-workflow-mcp
- Análisis de plantillas compiladas (product.md, tech.md, structure.md)
- Propuesta de workbooks RBM (Result-Based Management)
- Sistema de herencia de templates

**Uso en SPEC-000**: Contexto histórico sobre cómo surgió el sistema de templates que estamos investigando.

#### 2.2.2. ANALISIS-PROPUESTA-spec-000-dominio-vivo.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-09
**Palabras**: ~8,000

**Contenido**:
- Propuesta de SPEC-000 como foundation specification
- Concepto de "dominio vivo" (evolución autopoiética del conocimiento)
- Workspaces: 00-define/ para investigación activa
- Separación entre investigación (00-define/), gobernanza (.spec-workflow/), y outputs (_melquisedec/domain/)

**Uso en SPEC-000**: Rationale histórico para la arquitectura de workspaces y concepto de dominio vivo.

#### 2.2.3. ANALISIS-PROFUNDO-academic-research-vs-imrad.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-10
**Palabras**: ~28,000

**Contenido**:
- **Parte 1**: Explicación "for dummies" de investigación académica
- **Parte 2-3**: Comparación Academic Research vs IMRAD
- **Parte 4-8**: Mejores prácticas, validación, metadata, ejemplos
- **Parte 9**: Gobernanza de artefactos (spec:issue, spec:owner, Pull Request system)

**Uso en SPEC-000**: Fundamento metodológico completo para los 6 workbooks.

### 2.3. Research - Code Analysis (Análisis de Código)

**Concepto**: Análisis del código spec-workflow-mcp para entender expectativas del dashboard y patrones de implementación.

#### 2.3.1. mcp-server-architecture.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-10

**Contenido**:
- Arquitectura del MCP server de spec-workflow
- Tools disponibles (get-project-setup-info, spec-workflow-guide, approvals, log-implementation, spec-status)
- Flujo completo: Idea → Requirements → Design → Tasks → Implementation

**Uso en SPEC-000**: HYPATIA puede analizar para entender qué artefactos espera el sistema.

#### 2.3.2. approval-system-flow.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-10

**Contenido**:
- Sistema de aprobaciones del dashboard
- Estados: pending → approved/rejected/needs-revision
- Workflow: request → status → delete

**Uso en SPEC-000**: SALOMON puede analizar para entender governance flow.

#### 2.3.3. implementation-log-patterns.md

**Autor**: GitHub Copilot (Claude Sonnet 4.5)
**Fecha**: 2026-01-10

**Contenido**:
- Patrones de implementation logs
- Artifacts esperados (apiEndpoints, components, functions, classes, integrations)
- Ejemplos de logs completos vs incompletos

**Uso en SPEC-000**: SALOMON puede analizar para crear validation strategies workbook.

---

## 3. Baseline (Línea Base)

**Concepto**: Templates existentes **antes de SPEC-000** - punto de partida para la investigación.

### 3.1. Templates Daath-Zen (6 variantes)

**Propósito**: Colección de templates base que se usan en el proyecto.

**Contenido**:
- `daath-zen-requirements.md`: Template para especificación de requisitos
- `daath-zen-design.md`: Template para decisiones de diseño (ADRs)
- `daath-zen-tasks.md`: Template para planificación de tareas
- `daath-zen-product.md`: Template para product thinking
- `daath-zen-tech.md`: Template para tech stack documentation
- `daath-zen-structure.md`: Template para estructura de proyecto

**Uso en SPEC-000**: SALOMON puede referenciar estos templates al analizar qué artefactos deberían generarse en los workbooks.

---

## 4. Templates (Generados por SPEC-000)

**Concepto**: Templates creados como resultado de Task-000-002 de SPEC-000.

### 4.1. Academic Research Template

**Estructura**: 5 folders (1-literature, 2-analysis, 3-atomics, 4-artifacts, 6-outputs)

**Metodología**: Systematic Literature Review (Kitchenham 2007) + Zettelkasten

**Uso**: Template para workbooks de exploración (ej: spec-workflow artifacts investigation).

### 4.2. IMRAD Template

**Estructura**: 7 files (01-introduction, 02-literature-review, 03-methodology, 04-results, 05-discussion, 06-conclusion, 07-references)

**Metodología**: IMRAD (Introduction, Methods, Results, Discussion)

**Uso**: Template para workbooks de síntesis (ej: DDD patterns, metadata governance).

---

## 5. Uso por Agentes

### 5.1. HYPATIA (Literature Review)

**Workbooks asignados**: Academic Research (3 workbooks)
- Spec-workflow artifacts investigation
- DDD patterns & bounded contexts
- Validation strategies & testing patterns

**Inputs críticos**:
1. Read `research/preliminary/raw-manifiesto.md` (bridge concept)
2. Read `research/preliminary/ANALISIS-APPROACH-ATOMICO.md` (atomic approach)
3. Read `research/preliminary/DIAGRAMAS-WORKFLOW-MCP.md` (workflow diagrams)
4. Read `research/legacy-proposals/ANALISIS-PROPUESTA-spec-000-dominio-vivo.md` (dominio vivo concept)
5. Read `research/code-analysis/mcp-server-architecture.md` (artifacts expected)
6. Read `baseline/templates-daath-zen/daath-zen-requirements.md` (baseline template)

**Workflow**:
1. Usar template `templates/academic-research-template/`
2. Referenciar preliminary research para conceptos fundacionales
3. Analizar code analysis para expectativas del sistema
4. Crear atomics (concept-*.md, pattern-*.md) en `3-atomics/`

### 5.2. SALOMON (Synthesis & Writing)

**Workbooks asignados**: IMRAD (3 workbooks)
- Requirements Specification Patterns
- Metadata & Dublin Core Governance
- Project Structure & Organization

**Inputs críticos**:
1. Read `research/preliminary/raw-manifiesto.md` (metadata structures)
2. Read `research/preliminary/DIAGRAMAS-WORKFLOW-MCP.md` (visualizations)
3. Read `research/legacy-proposals/ANALISIS-PROFUNDO-academic-research-vs-imrad.md` (methodology)
4. Read `steering/product.md` (product vision)
5. Read `steering/tech.md` (tech constraints)
6. Read `steering/structure.md` (governance)

**Workflow**:
1. Usar template `templates/imrad-template/`
2. Referenciar steering/ para contexto inmutable del proyecto
3. Sintetizar preliminary research en IMRAD sections
4. Incluir Mermaid diagrams (from DIAGRAMAS-WORKFLOW-MCP.md)

---

## 6. Relaciones con Documentación Formal

**Documentación Governance**:
- [SPEC-000 Requirements](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/requirements.md)
- [SPEC-000 Design](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/design.md)
- [SPEC-000 Tasks](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/tasks.md)

**Separación de Concerns**:
- **inputs/**: Source materials (steering + research + baseline)
- **.spec-workflow/specs/spec-000/**: Formal governance docs (requirements, design, tasks)
- **workbooks/**: Active research workspaces (6 workbooks en progreso)
- **_melquisedec/domain/**: Final knowledge outputs (atomics, embeddings, graphs)

---

## 7. Claridad Semántica

### Antes (manifest/)
- **Problema**: "Manifest" implica algo inmutable, pero contenía mezcla de steering + research + baseline
- **Confusión**: ¿Es un manifesto? ¿Es un input temporal? ¿Qué puedo modificar?

### Ahora (inputs/)
- **steering/**: **TRUE MANIFEST** - contexto inmutable del proyecto (product, tech, structure)
- **research/**: Investigación (preliminary foundational + legacy-proposals historical + code-analysis patterns)
- **baseline/**: Línea base de templates (punto de partida existente antes de SPEC-000)
- **templates/**: Templates generados por SPEC-000 (resultado de investigación)

### Beneficios
1. **Claridad conceptual**: steering/ = verdaderamente inmutable, research/ = evolución histórica
2. **Trazabilidad**: preliminary/ separa investigación fundacional de legacy-proposals/
3. **Accessibility**: preliminary/ incluye DIAGRAMAS críticos para "principiantes"
4. **Gobernanza**: Distinción clara entre inputs (inmutables/históricos) y outputs (generados por SPEC-000)

---

## 8. Próximos Pasos

1. ✅ **Task-000-002**: Templates creados (academic-research + imrad)
2. ⏳ **Task-000-003**: Crear validation tools (validate-imrad-structure.py, validate-academic-research.py, validate-metadata.py)
3. ⏳ **Task-000-004**: Ejecutar workbook "spec-workflow artifacts investigation" (HYPATIA)
4. ⏳ **Task-000-005**: Ejecutar workbook "DDD patterns" (HYPATIA)
5. ⏳ **Task-000-006**: Ejecutar workbook "validation strategies" (HYPATIA)
6. ⏳ **Task-000-007**: Ejecutar workbook "Requirements patterns" (SALOMON)
7. ⏳ **Task-000-008**: Ejecutar workbook "Metadata governance" (SALOMON)
8. ⏳ **Task-000-009**: Ejecutar workbook "Project structure" (SALOMON)

---

**Metadata**:
```yaml
'@context': '../../../context.jsonld'
'@type': 'InputsDirectory'
'@id': 'urn:melquisedec:spec:000:inputs'
dc:
  title: "Inputs Directory - SPEC-000 Investigation"
  creator: "MELQUISEDEC"
  date: "2026-01-11"
  subject: ["inputs", "steering", "research", "baseline", "templates"]
  description: "Directorio centralizado de inputs para SPEC-000 con separación semántica steering/research/baseline"
spec:
  issue: "SPEC-000"
  status: "active"
  version: "2.0.0"  # v2.0.0 = restructured from manifest/ to inputs/
```

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
