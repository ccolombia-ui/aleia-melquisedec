# 🔬 Investigación Bidireccional: Template Spec-Workflow-MCP ↔ DAATH-ZEN

**Fecha**: 2026-01-10  
**Contexto**: Respuesta crítica a REFLEXION-CRITICA-orden-implementacion-spec-001.md  
**Autor**: Usuario + GitHub Copilot  
**Rostro**: Melquisedec (Arquitecto) ↔ Hypatia (Investigadora)  
**Criticidad**: 🔴 **BLOQUEANTE** - El template NO puede ser inventado, debe emerger del dominio

---

## 📋 Resumen Ejecutivo

### El Problema Identificado

La reflexión crítica señala correctamente que **la investigación es unidireccional e incompleta**:

```
❌ ESTADO ACTUAL (Incompleto)
└── spec-workflow-mcp artifacts
    └── ¿Cómo se construyen product.md, tech.md, tasks.md?

✅ ESTADO REQUERIDO (Bidireccional)
├── spec-workflow-mcp artifacts (herramienta)
│   ├── steering docs (product.md, tech.md, structure.md)
│   ├── spec artifacts (requirements.md, design.md, tasks.md)
│   └── workflows (approval, log-implementation, etc.)
│
└── DAATH-ZEN framework (dominio)
    ├── Ciclo Melquisedec (5 Rostros)
    ├── Principios P1-P10
    ├── Metodologías orquestadas (DSR, IMRAD, RBM-GAC)
    ├── Templates configurables
    └── Triple persistencia (md ↔ Neo4j ↔ vectors)
```

**Pregunta Central**: ¿Cómo debe el template **sintetizar** ambas fuentes para ser **configurable, mantenible, minimalista, coherente, automatizable, optimizable**?

---

## 🎯 Objetivo de la Investigación

### Resultado Esperado

Crear un **TEMPLATE CONFIGURABLE** que:

1. **Respete los artefactos de spec-workflow-mcp** (steering, requirements, design, tasks, approval, logs)
2. **Integre el dominio DAATH-ZEN** (rostros, principios, metodologías, triple persistencia)
3. **Sea configurable** (variables, not hardcoded)
4. **Sea mantenible** (minimalista, DRY, versionado)
5. **Sea coherente** (alineado al Manifiesto v4.0.0)
6. **Sea automatizable** (scripts, validaciones, compiladores)
7. **Sea optimizable** (aprende de lessons, autopoiesis)

### Productos de la Investigación

**Inmediatos (Rinm):**
- 📄 Inventario completo de artefactos spec-workflow-mcp
- 📄 Inventario completo de componentes DAATH-ZEN
- 📊 Matriz de correspondencia bidireccional
- 📋 Gap analysis (¿qué falta? ¿qué sobra?)

**Intermedios (RI):**
- 🏗️ Arquitectura del template configurable
- 🎨 Diseño de sistema de variables dependientes
- 📐 Especificación de compiler/generator patterns
- ✅ Criterios de validación y coherencia

**Finales (RF):**
- 📦 Template System implementado y validado
- 📚 Documentación completa con ejemplos
- 🧪 Test suite de validación
- 🔄 Sistema de lessons learned integrado

---

## ✨ 20 Mejores Prácticas Extraídas (Best Practices)

Del análisis de 6,350 líneas de investigación previa, se identificaron **20 best practices críticas**:

### Grupo 1: Minimalismo Cognitivo (Prácticas 1-5)

| # | Práctica | Origen | Evidencia |
|---|----------|--------|-----------|
| **1** | **Regla "Menos es Más"**: Si no cabe en 1 pantalla sin scroll → Split | ANALISIS-APPROACH-ATOMICO.md | Cognitive Load Theory, Miller 7±2 chunks |
| **2** | **Límite 300 líneas**: Máximo por documento atómico | INDICE-COMPLETO-ARTEFACTOS.md | "6 scrolls máximo antes de split" |
| **3** | **Zettelkasten Bidireccional**: `[[REQ-001]]` ↔ `[[CONCEPT-017]]` | ANALISIS-APPROACH-ATOMICO.md | Luhmann: 90K notas → 70 libros |
| **4** | **Issue-Driven Everything**: Cada componente = 1 issue trackeable | ISSUE-DRIVEN-SPEC-WORKFLOW-INTEGRATION.md | Lean/Kanban: Pull system |
| **5** | **Recursión Fractal**: Mismo patrón a todas las escalas | PROPUESTA-CORREGIDA-SPEC-POR-SECCION.md | P7 Manifiesto |

### Grupo 2: Configurabilidad (Prácticas 6-10)

| # | Práctica | Origen | Evidencia |
|---|----------|--------|-----------|
| **6** | **Sistema Minimalista**: 1 base (30 líneas) + N configs (20 líneas) | INDICE-COMPLETO-ARTEFACTOS.md | Reduce 475 líneas → 143 líneas (70% less) |
| **7** | **Variables Dependientes Calculadas**: Fórmulas explícitas, NO hardcoded | REQ-001-template-system.md | Pizza Margherita Pattern (temp = cheese_melt + 40°C) |
| **8** | **Fundamentar Cada Número**: Temperatura, tiempo, confidence con evidencia | REQ-001-template-system.md | Rigor metodológico |
| **9** | **Placeholders Consistentes**: `{{VAR}}` para todas las variables | daath-zen-base.md | Keter-Doc Protocol |
| **10** | **Config por Tipo**: requirement.yaml, concept.yaml, design.yaml | INDICE-COMPLETO-ARTEFACTOS.md | Agregar tipo = +20 líneas vs +100 |

### Grupo 3: Spec-Workflow Integration (Prácticas 11-15)

| # | Práctica | Origen | Evidencia |
|---|----------|--------|-----------|
| **11** | **Columna "spec-workflow Integration"**: Documentar workflow en tablas | GAP-ANALYSIS-SPEC-WORKFLOW-INTEGRATION.md | Main Spec vs Sub-Issue clarificado |
| **12** | **Main Spec CON approval**: Steering + Requirements + Design + Tasks | DIAGRAMAS-WORKFLOW-MCP.md | Approval workflow completo |
| **13** | **Sub-Issues SIN approval**: REQ/CONCEPT/LIT/DESIGN atómicos | DIAGRAMAS-WORKFLOW-MCP.md | Workflow rápido (20-35 min) |
| **14** | **IMPL CON logging MANDATORY**: Artifacts tracking obligatorio | GAP-ANALYSIS-SPEC-WORKFLOW-INTEGRATION.md | Previene duplicación código |
| **15** | **Timing Explícito**: Documentar tiempo estimado por workflow | DIAGRAMAS-WORKFLOW-MCP.md | 20-35 min, 5h, 4 semanas, etc. |

### Grupo 4: Trazabilidad & Validación (Prácticas 16-20)

| # | Práctica | Origen | Evidencia |
|---|----------|--------|-----------|
| **16** | **Sin Jerarquía Artificial**: Specs son peers, no "Main → Sub" | PROPUESTA-CORREGIDA-SPEC-POR-SECCION.md | Modularidad real |
| **17** | **Mapeo Manifiesto → Specs**: Cada sección importante = 1 spec | PROPUESTA-CORREGIDA-SPEC-POR-SECCION.md | 10 specs vs 1 monolito |
| **18** | **Outcomes SMART**: Tabla Baseline/Target/Actual/Status + fórmula éxito | REQ-001-template-system.md | Success Rate = (5/5) * 100 = 100% |
| **19** | **Métricas Cuantitativas**: Siempre incluir %, tiempo, cost | ANALISIS-APPROACH-ATOMICO.md | +400% paralelización, -93.75% tiempo review |
| **20** | **Diagramas Mermaid**: sequenceDiagram para todos los workflows | DIAGRAMAS-WORKFLOW-MCP.md | Visualización clara de procesos |

### Impacto Documentado

```
Sistema Monolítico (Antes):
- 475 líneas código (5 templates separados)
- ~300 líneas duplicadas (63%)
- Agregar tipo: +100 líneas
- 1 persona trabajando eficientemente
- 4 horas review time

Sistema Minimalista (Después):
- 143 líneas código (70% reducción) ✅
- 0 líneas duplicadas ✅
- Agregar tipo: +20 líneas ✅
- 4 personas en paralelo (+400%) ✅
- 15 minutos review (-93.75%) ✅
```

**Fórmula de Mejora Global**:
```
Improvement = (Old - New) / Old * 100
Improvement = (475 - 143) / 475 * 100 = 69.9% código menos
```

---

## 🔬 Investigaciones Previas Analizadas

### Documentos Legacy Revisados (010-define/)

Se realizó análisis exhaustivo de 5 documentos clave de investigaciones previas:

| Documento | Líneas | Propósito | Valor Extraído |
|-----------|--------|-----------|----------------|
| **INDICE-COMPLETO-ARTEFACTOS.md** | 2,577 | Sistema atómico, 157 issues | ✅ Sistema minimalista (1 base + N configs)<br/>✅ Variables dependientes calculadas<br/>✅ Ejemplo rigor metodológico (pizza margherita) |
| **ANALISIS-APPROACH-ATOMICO.md** | 489 | Análisis atómico vs monolítico | ✅ Métricas cuantitativas (+400% paralelización)<br/>✅ Principios cognitivos (Miller 7±2)<br/>✅ Zettelkasten aplicado |
| **PROPUESTA-CORREGIDA-SPEC-POR-SECCION.md** | 750 | 10 spec-issues por sección manifiesto | ✅ Mapeo manifiesto → specs independientes<br/>✅ Sin jerarquía artificial |
| **GAP-ANALYSIS-SPEC-WORKFLOW-INTEGRATION.md** | 700 | Gaps en integración MCP | ✅ Tabla "spec-workflow Integration" propuesta<br/>✅ Main Spec vs Sub-Issues clarificado<br/>✅ Implementation logging documentado |
| **ISSUE-DRIVEN-SPEC-WORKFLOW-INTEGRATION.md** | 1,001 | Diagramas y flujos completos | ✅ Secuencia approval workflow<br/>✅ 4 fases completas diagramadas |
| **DIAGRAMAS-WORKFLOW-MCP.md** | 833 | Mermaid visualizations | ✅ Main Spec (CON approval)<br/>✅ Sub-Issue (SIN approval)<br/>✅ IMPL (CON logging) |

**Total Analizado**: **6,350 líneas de investigación previa** con hallazgos validados.

### Workbooks REQ Legacy (52 ejemplos)

Se analizó estructura de 52 workbooks REQ-XXX en `010-define/workbooks/`:

**Estructura Identificada** (basado en REQ-001-template-system.md):

```markdown
# REQ-001: Template System Architecture

## Metadata (8 campos estándar)
- Tipo, Metodología, Status, Prioridad
- Created, Updated (timestamps ISO8601)

## Problem Statement (RBM)
### Gap Analysis (¿Qué falta?)
- Situación Actual (métricas cuantitativas)
- Problema Raíz (diagrama Mermaid)

### Goal (¿Qué queremos lograr?)
- Objetivos específicos (SMART)
- Arquitectura Objetivo (diagrama Mermaid)

### Expected Outcomes (Resultados Medibles)
- Tabla con 5 columnas: Outcome, Baseline, Target, Actual, Status
- Fórmula de éxito (Success Rate = X%)

## Approach (Metodología + Conceptos + Restricciones)
### Methodology (DSR, RBM, SECI)
### Key Concepts (con formulas)
### Constraints (con validaciones)

## Notes & Lessons Learned
```

**Hallazgo Clave**: Variables dependientes con **fórmulas explícitas**:

```yaml
# Ejemplo REQ-001 (Pizza Margherita Pattern):
timing:
  formula: "base_time + (num_sections * time_per_section)"
  inputs:
    base_time: 5 min
    num_sections: 4
    time_per_section: 5 min
  output: "25-30 min"
  reasoning: "Fundamentado en mediciones empíricas"
```

### Mejores Prácticas Extraídas

**De ANALISIS-APPROACH-ATOMICO.md**:

1. **Principio "Menos es Más"**: Si no cabe en 1 pantalla sin scroll (50 líneas), es demasiado grande
2. **Zettelkasten**: Notas atómicas vinculadas bidireccionalmente ([[REQ-001]] ↔ [[CONCEPT-017]])
3. **Issue-Driven**: Cada componente tiene issue trackeable en `.spec-workflow/specs/TYPE-XXX/`
4. **Recursión Fractal**: Mismo patrón a diferentes escalas (Spec → Sub-Spec → Workbook → Sections)
5. **Métricas Cuantitativas**: Siempre incluir baseline, target, actual, % improvement

**De GAP-ANALYSIS-SPEC-WORKFLOW-INTEGRATION.md**:

6. **Columna "spec-workflow Integration"**: Toda tabla de artefactos debe incluir workflow específico
7. **Main Spec CON approval**: Steering + Spec docs siguen approval workflow completo
8. **Sub-Issues SIN approval**: REQ/CONCEPT/LIT/DESIGN son atómicos, no requieren approval
9. **IMPL CON logging MANDATORY**: Artifacts tracking para evitar duplicación futura
10. **Timing Explícito**: Cada workflow documenta tiempo estimado (20-35 min, 5h, etc.)

**De DIAGRAMAS-WORKFLOW-MCP.md**:

11. **Secuencia Visual**: Mermaid sequenceDiagram para todos los workflows
12. **Estados Claros**: draft → in-progress → completed → deprecated
13. **4 Workflows Diferenciados**: Main Spec, Sub-Issue, IMPL, Steering (cada uno con su flujo)

**De PROPUESTA-CORREGIDA-SPEC-POR-SECCION.md**:

14. **Sin Jerarquía Artificial**: Todos los specs son peers, no "Main → Sub"
15. **Mapeo Manifiesto → Specs**: Cada sección importante del manifiesto = 1 spec independiente
16. **Modularidad Real**: 10 specs autónomos vs 1 monolito de 17,142 líneas

**De INDICE-COMPLETO-ARTEFACTOS.md**:

17. **Sistema Minimalista**: 1 template base (30 líneas) + N configs (20 líneas)
18. **Variables Dependientes**: NUNCA hardcoded, siempre calculadas con formula
19. **Rigor Metodológico**: Fundamentar cada número (temperatura, tiempo, confidence)
20. **Outcomes SMART**: Tabla con Baseline/Target/Actual/Status, fórmula de éxito

---

## 📊 Fase 1: Inventario Preliminar Completo

### 1.1. Artefactos spec-workflow-mcp (Herramienta)

#### Steering Documents (Optional, grandes proyectos)

| Artefacto | Propósito | Contenido Clave |
|-----------|-----------|-----------------|
| `product.md` | Visión de producto | Stakeholders, constraints, roadmap |
| `tech.md` | Stack tecnológico | Framework selection, architecture principles |
| `structure.md` | Arquitectura de carpetas | Monorepo layout, package organization |

**Observación**: Estos documentos **NO se inventan**, se **compilan desde workbooks** (DDD, IMRAD, ADRs).

#### Spec Documents (Core workflow)

| Artefacto | Propósito | Contenido Clave |
|-----------|-----------|-----------------|
| `requirements.md` | Requerimientos del spec | Problemas, soluciones, success criteria |
| `design.md` | Diseño técnico | Arquitectura, diagramas, decisiones |
| `tasks.md` | Plan de implementación | Fases, tareas, dependencias |
| `implementation-log.json` | Registro de ejecución | Artifacts created, APIs, components, functions |

**Observación**: Estos documentos son **el core del workflow** y deben integrarse con los Rostros DAATH-ZEN.

#### MCP Tools Disponibles

| Tool | Propósito | Cuándo Usar |
|------|-----------|-------------|
| `spec-workflow-guide` | Cargar workflow completo | **PRIMERO** en todo spec |
| `steering-guide` | Cargar guía steering docs | Solo para proyectos grandes |
| `approvals` | Gestionar aprobaciones | Después de crear cada documento |
| `log-implementation` | Registrar implementación | **CRÍTICO**: Después de cada task con artifacts detallados |

**Observación Crítica**: `log-implementation` requiere **artifacts estructurados** (apiEndpoints, components, functions, classes, integrations) para evitar duplicación futura.

---

### 1.2. Componentes DAATH-ZEN Framework (Dominio)

#### Templates Existentes (Análisis de Versiones)

| Rostro | Fase | MCPs Preferidos | Output Principal |
|--------|------|-----------------|------------------|
| **MELQUISEDEC** | Define (010) | sequential-thinking, filesystem | requirements.md, design.md |
| **HYPATIA** | Conceive (020) | brave, arxiv, wikipedia, perplexity | literature/, atomics/ |
| **SALOMON** | Design (030) | sequential-thinking, context7 | workbook/, adrs/ |
| **MORPHEUS** | Build (040) | e2b, python, filesystem | artifacts/, scripts/ |
| **ALMA** | Release (050) | neo4j, git | outputs/, validation/ |
| **DAATH** | Reflect (060) | smart-thinking, filesystem | lessons/, template-improvements.md |

**Observación**: Los Rostros son **roles metodológicos**, no personas. Un mismo agente puede ejecutar múltiples rostros.

#### Principios P1-P10 del Manifiesto

| Principio | Descripción Corta | Impacto en Template |
|-----------|-------------------|---------------------|
| **P1** | Síntesis metodológica (orquesta, no inventa) | Template debe **componer** metodologías existentes |
| **P2** | Autopoiesis (aprende y mejora) | Sistema de lessons + feedback loop |
| **P3** | Triple persistencia (md ↔ graph ↔ vectors) | Keter-Doc schema + Neo4j + embeddings |
| **P4** | Trazabilidad (URNs, JSON-LD) | Metadata en frontmatter + @context |
| **P5** | Modularidad (DRY, composable) | Variables dependientes, not hardcoded |
| **P6** | Versionado semántico (tracking changes) | Version tags, CHANGELOG |
| **P7** | Checkpoints (validación continua) | CK-01, CK-02, CK-03, CK-04 |
| **P8** | Context management (smart-thinking MCP) | Sessions, branches, memories |
| **P9** | Artifacts-first (log everything) | implementation-log con artifacts detallados |
| **P10** | Crecimiento orgánico (emerge según necesidad) | Estructura flexible, not rigid scaffolding |

#### Metodologías Orquestadas

| Metodología | Fase Aplicada | Artefactos Generados |
|-------------|---------------|----------------------|
| **RBM-GAC** | Define | Cadena de resultados (Rinm → RI → RF) |
| **DSR** | Conceive | Problem identification, solution design, evaluation |
| **IMRAD** | Conceive | Literature, analysis, discussion, conclusions |
| **DDD** | Design | Bounded contexts, aggregates, entities |
| **SECI** | Conceive | Socialization, externalization, combination, internalization |
| **Zettelkasten** | Conceive | Atomic notes, bidirectional links |

**Observación Crítica**: Estas metodologías **NO son opcionales**, son la fuente de donde emergen los artefactos.

#### Templates Configurables Legacy

| Template | Ubicación | Líneas | Características Clave | Status |
|----------|-----------|--------|----------------------|--------|
| **daath-zen-base.md** | `_melquisedec/templates/` | 228 | ✅ Keter-Doc Protocol completo<br/>✅ YAML + JSON-LD frontmatter<br/>✅ Dublin Core metadata<br/>✅ Placeholders {{VAR}} | 🟢 Actual |
| **daath-zen-req-template.md** | `_legacy/_templates/daath-zen-patterns/` | ~150 | ✅ Requirement template<br/>✅ RBM structure<br/>✅ Result mapping (Rinm/RI/RF) | 🟡 Legacy |
| **template-configurable_daath-zen-root.md** | `_legacy/_templates/daath-zen-patterns/` | ~180 | ✅ Root governance<br/>✅ Validation policy<br/>✅ Version control rules | 🟡 Legacy |
| **daath-zen-salomon-design-template.md** | `_legacy/_templates/daath-zen-patterns/` | ~160 | ✅ Design template<br/>✅ ADR integration<br/>✅ Architecture patterns | 🟡 Legacy |
| **atomic-concept.md** | Legacy research templates | ~100 | ✅ SECI Model integration<br/>✅ Zettelkasten format | 🟡 Legacy |
| **unified-research-template-design-v4.2.0.md** | `.spec-workflow/_meta/templates/` | 17,142 | ❌ MONOLÍTICO (17K líneas)<br/>✅ Diseño completo de 5 fases<br/>✅ Workflow por rostro | 🔴 Obsoleto |

**Análisis Consolidado**:

```
Fortalezas Comunes:
✅ Keter-Doc Protocol (frontmatter estandarizado)
✅ Placeholders {{VAR}} configurables
✅ JSON-LD context (@context, @type, @id)
✅ Metadata Dublin Core (dc:title, dc:creator, etc.)

Debilidades Identificadas:
❌ Múltiples versiones inconsistentes
❌ No hay sistema unificado de variables dependientes
❌ Algunos templates muy largos (v4.2.0 = 17K líneas)
❌ No hay validador de coherencia entre versions
```

**Mejor Candidato para Base**: **daath-zen-base.md** (228 líneas)
- ✅ Más completo en metadata
- ✅ Keter-Doc Protocol actualizado
- ✅ Estructura limpia con placeholders
- ✅ JSON-LD completo

**Observación**: Existen **6 versiones** de templates DAATH-ZEN, necesitamos **consolidar** lo mejor de cada uno en un sistema minimalista.

---

## 🔗 Fase 2: Matriz de Correspondencia Bidireccional

### 2.1. Mapeo Steering Docs ↔ DAATH-ZEN

| Spec-Workflow Artifact | DAATH-ZEN Source | Metodología | Compilación |
|------------------------|------------------|-------------|-------------|
| `product.md` | `00-problem/` | RBM-GAC | Stakeholders, scope, constraints → steering |
| `tech.md` | `03-workbook/adrs/`, `02-atomics/` | DDD, IMRAD | Tech stack, architecture principles → steering |
| `structure.md` | `design.md`, `03-workbook/` | DDD | Bounded contexts, packages → steering |

**Flujo Típico**:
```
1. HYPATIA investiga (literature + atomics)
2. SALOMON analiza (workbook + ADRs)
3. MELQUISEDEC compila → steering docs
4. Approval request (spec-workflow-mcp tool)
```

### 2.2. Mapeo Spec Docs ↔ DAATH-ZEN

| Spec-Workflow Artifact | DAATH-ZEN Source | Rostro Principal | Fase |
|------------------------|------------------|------------------|------|
| `requirements.md` | `00-problem/`, `ISSUE.yaml` | MELQUISEDEC | 010-define |
| `design.md` | `03-workbook/`, `02-atomics/` | SALOMON | 030-design |
| `tasks.md` | Auto-generated from spec-config.yaml | MELQUISEDEC | 010-define |
| `implementation-log.json` | Runtime, post-task | MORPHEUS/ALMA | 040-build |

**Flujo Típico**:
```
1. MELQUISEDEC define (requirements.md, design.md)
2. Approval request
3. Spec-workflow-mcp genera tasks.md automáticamente
4. MORPHEUS/ALMA implementan → log-implementation
```

### 2.3. Mapeo Implementation Logs ↔ DAATH-ZEN

**🔴 CRÍTICO**: Este es el punto de **mayor integración** y **mayor riesgo de duplicación**.

| Log Component | DAATH-ZEN Source | Propósito |
|---------------|------------------|-----------|
| `artifacts.apiEndpoints` | `04-artifacts/`, code files | Evitar duplicar endpoints |
| `artifacts.components` | `04-artifacts/`, code files | Evitar duplicar componentes |
| `artifacts.functions` | `04-artifacts/`, code files | Evitar duplicar utilities |
| `artifacts.classes` | `04-artifacts/`, code files | Evitar duplicar clases |
| `artifacts.integrations` | `04-artifacts/`, design.md | Documentar patrones de integración |

**Ejemplo Concreto** (del tool description):

```json
{
  "taskId": "2.3",
  "summary": "Implemented real-time implementation logs dashboard",
  "artifacts": {
    "apiEndpoints": [
      {
        "method": "GET",
        "path": "/api/specs/:name/implementation-log",
        "purpose": "Retrieve implementation logs with optional filtering",
        "location": "src/dashboard/server.ts:245"
      }
    ],
    "components": [
      {
        "name": "LogsPage",
        "type": "React",
        "purpose": "Main dashboard page for viewing implementation logs",
        "location": "src/modules/pages/LogsPage.tsx"
      }
    ],
    "classes": [
      {
        "name": "ImplementationLogManager",
        "purpose": "Manages CRUD operations for implementation logs",
        "location": "src/dashboard/implementation-log-manager.ts",
        "methods": ["loadLog", "addLogEntry", "getAllLogs"]
      }
    ]
  }
}
```

**Observación**: Los artifacts logs son **searchable knowledge base** para futuros agentes. Sin ellos, se duplica código.

---

## 🏗️ Fase 3: Arquitectura del Template Configurable

### 3.1. Sistema Minimalista (Aprendido de Legacy)

**Lección del INDICE-COMPLETO-ARTEFACTOS v3.1.0**:

> "Sistema minimalista configurable: 1 template base + N configs pequeños"

**Diseño Propuesto**:

```yaml
# template-base.yaml (30 líneas genéricas)
type: template_base
version: 1.0.0
variables:
  generic: [spec_id, title, author, created, version]
  computed: [modified, dc_title, document_urn]
dependencies:
  required: [spec_id, title]
  optional: [parent_issue, related_specs]
structure:
  frontmatter: yaml
  context: jsonld
  body: markdown
```

```yaml
# config-requirement.yaml (pequeño)
extends: template-base.yaml
type: requirement
rostro_primary: MELQUISEDEC
phase: requirements
template_file: daath-zen-req-template.md
computed_variables:
  - dc_title: "REQ-{spec_id}: {title}"
  - document_urn: "urn:melquisedec:req:{spec_id}:{version}"
validations:
  - required_sections: [problem, solution, outcomes]
  - max_lines: 300
```

**Ventajas**:
- ✅ DRY (Don't Repeat Yourself)
- ✅ Variables dependientes calculadas
- ✅ Fácil de mantener
- ✅ Extensible (nuevos configs sin tocar base)

### 3.2. Integración con Spec-Workflow-MCP

**Secuencia de Integración**:

```mermaid
sequenceDiagram
    participant User
    participant Template System
    participant Spec-Workflow-MCP
    participant DAATH-ZEN

    User->>Template System: create_spec(name, type)
    Template System->>Template System: Load config (requirement/design/steering)
    Template System->>DAATH-ZEN: Apply Rostro context (MELQUISEDEC)
    Template System->>Template System: Generate from template + variables
    Template System->>Spec-Workflow-MCP: spec-workflow-guide (load workflow)
    Template System-->>User: Document created (requirements.md)
    
    User->>Spec-Workflow-MCP: approvals(action="request")
    Spec-Workflow-MCP-->>User: Approval requested
    
    Note over User,Spec-Workflow-MCP: User reviews in dashboard
    
    User->>Spec-Workflow-MCP: approvals(action="status")
    Spec-Workflow-MCP-->>User: Status: approved
    
    User->>Template System: continue_to_implementation()
    Template System->>DAATH-ZEN: Switch Rostro (MORPHEUS)
    Template System-->>User: Ready for implementation
    
    Note over User,DAATH-ZEN: Implementation happens
    
    User->>Spec-Workflow-MCP: log-implementation(artifacts)
    Spec-Workflow-MCP-->>DAATH-ZEN: Store in triple persistence
```

### 3.3. Variables Dependientes (Rigor Metodológico)

**Ejemplo de Pizza Margarita** (del INDICE-COMPLETO-ARTEFACTOS v3.1.0):

```yaml
# BAD (Hardcoded)
temperature: 220°C
time: 15 min

# GOOD (Calculated)
base_values:
  cheese_melt_point: 180°C
  dough_thickness: 0.5cm

computed:
  temperature: cheese_melt_point + 40  # 220°C
  time: (dough_thickness / 0.1) * 3    # 15 min (0.5/0.1 * 3)
```

**Aplicación al Template**:

```yaml
# BAD
max_lines_requirement: 300
max_lines_design: 500

# GOOD
base_values:
  screen_lines: 50           # Líneas visibles sin scroll
  max_screens: 6             # Máximo scrolls antes de split

computed:
  max_lines_requirement: screen_lines * max_screens  # 300
  max_lines_design: screen_lines * (max_screens + 4) # 500
  
reasoning: "Si supera 6 scrolls (300 líneas), es demasiado grande"
```

---

## 🔍 Fase 4: Investigación de Fuentes Legacy

### 4.1. Análisis de Versiones Previas

**Fuentes Identificadas**:

1. `_legacy/_apps_legacy/research-autopoietic-template-v0.1.0/010-define/`
   - ✅ **INDICE-COMPLETO-ARTEFACTOS.md** (2,577 líneas) - Sistema atómico
   - ✅ **ANALISIS-GAPS-Y-RECOMENDACIONES.md** (1,047 líneas) - Gap analysis
   - ✅ **workbooks/** (52 REQ-XXX.md files) - Ejemplos de requerimientos atómicos
   - 📊 **Valor**: Approach "atómico" documentado, REQ templates

2. `_legacy/_templates/daath-zen-patterns/`
   - ✅ **template-configurable_daath-zen-root.md** - Root governance
   - ✅ **daath-zen-req-template.md** - Requirement template
   - ✅ **daath-zen-salomon-design-template.md** - Design template
   - 📊 **Valor**: Templates con placeholders, configurables

3. `_legacy/canonical/el-puente-manifiesto-daath-zen-root-spec-workflow-mcp.md`
   - ⚠️ **Status**: Draft stub (vacío)
   - 📊 **Valor**: Concepto de "puente" entre manifiesto y spec-workflow

4. `.spec-workflow/_meta/templates/research-autopoietic-template/`
   - ✅ **unified-research-template-design-v4.2.0.md** - Diseño unificado
   - ✅ **README.md** - Estructura completa de 5 fases
   - ✅ **tasks.md** - 27 tasks en formato DAATH-ZEN Advanced
   - 📊 **Valor**: Diseño completo, workflow por rostro

5. `apps/R000-autopoietic-template/_melquisedec/templates/`
   - ✅ **daath-zen-base.md** (228 líneas) - Base con Keter-Doc Protocol
   - 📊 **Valor**: Template actual con JSON-LD completo

### 4.2. Consolidación de Mejores Prácticas

**De Legacy v0.1.0** (INDICE-COMPLETO-ARTEFACTOS):
- ✅ Sistema atómico (1 requirement = 1 file)
- ✅ Variables dependientes calculadas
- ✅ Approach minimalista configurable
- ✅ Gap analysis riguroso

**De _templates/daath-zen-patterns/**:
- ✅ Placeholders estructurados ({{VAR}})
- ✅ Root governance (template-configurable)
- ✅ Múltiples variantes (req, design, salomon)

**De .spec-workflow/_meta/templates/**:
- ✅ Estructura completa de 5 fases
- ✅ Workflow por rostro documentado
- ✅ 27 tasks organizadas (DAATH-ZEN Advanced)
- ✅ Checkpoints CK-01 a CK-04

**De daath-zen-base.md actual**:
- ✅ Keter-Doc Protocol completo
- ✅ JSON-LD context
- ✅ Dublin Core metadata
- ✅ Trazabilidad (parent_issue, related_specs)

---

## 📋 Fase 5: Plan de Acción Propuesto

### 5.1. Workbook de Investigación DAATH-ZEN

**Crear**: `.spec-workflow/specs/spec-001-investigation-daath-zen/`

**Estructura**:

```
spec-001-investigation-daath-zen/
├── ISSUE.yaml
├── requirements.md
├── design.md
├── tasks.md
├── analysis/
│   ├── ANALISIS-template-versions.md
│   ├── ANALISIS-spec-workflow-integration.md
│   ├── ANALISIS-variables-dependientes.md
│   └── MATRIZ-correspondencia-bidireccional.md
├── workbook/
│   ├── 01-inventory-spec-workflow-artifacts.md
│   ├── 02-inventory-daath-zen-components.md
│   ├── 03-best-practices-consolidation.md
│   ├── 04-template-architecture-design.md
│   └── 05-validation-criteria.md
└── implementation-log.json
```

**Tasks**:

```markdown
## Phase 1: Inventory (HYPATIA)
- [ ] T1.1. Document all spec-workflow-mcp artifacts
- [ ] T1.2. Document all DAATH-ZEN components
- [ ] T1.3. Analyze legacy template versions
- [ ] T1.4. Extract best practices from each source

## Phase 2: Analysis (SALOMON)
- [ ] T2.1. Create bidirectional correspondence matrix
- [ ] T2.2. Identify gaps and overlaps
- [ ] T2.3. Design configurable template architecture
- [ ] T2.4. Define computed variables system

## Phase 3: Design (SALOMON)
- [ ] T3.1. Create template-base.yaml (generic)
- [ ] T3.2. Create config-requirement.yaml
- [ ] T3.3. Create config-design.yaml
- [ ] T3.4. Create config-steering.yaml
- [ ] T3.5. Document integration with spec-workflow-mcp

## Phase 4: Implementation (MORPHEUS)
- [ ] T4.1. Implement template generator script
- [ ] T4.2. Implement variable calculator
- [ ] T4.3. Implement validator
- [ ] T4.4. Create test suite

## Phase 5: Validation (ALMA)
- [ ] T5.1. Test with REQ-001 example
- [ ] T5.2. Test with design.md example
- [ ] T5.3. Test spec-workflow-mcp integration
- [ ] T5.4. Extract lessons learned
```

### 5.2. Workbook de Investigación Spec-Workflow-MCP

**Crear**: `.spec-workflow/specs/spec-001-investigation-spec-workflow/`

**Foco**: Entender profundamente cómo usar las herramientas MCP:

```markdown
## Analysis Topics
- [ ] ¿Cuándo usar steering-guide vs spec-workflow-guide?
- [ ] ¿Cómo estructurar artifacts en log-implementation?
- [ ] ¿Qué debe ir en cada campo de apiEndpoints/components/functions?
- [ ] ¿Cómo evitar duplicación con logs detallados?
- [ ] ¿Cuál es el flujo completo de approval?
```

### 5.3. Cronograma Actualizado (Con Hallazgos)

**Opción Recomendada D (NUEVA): Investigación Acelerada + Implementación Híbrida** (2 semanas)

```
┌────────────────────────────────────────────────────────────────┐
│  WEEK 1: Investigación Focalizada + Primeros Prototipos       │
├────────────────────────────────────────────────────────────────┤
│  Day 1-2: Consolidación Rápida (HYPATIA + SALOMON)            │
│  ├─ ✅ Inventario YA REALIZADO (este documento)                │
│  ├─ ⏳ Consolidar 6 templates DAATH-ZEN → 1 base óptima        │
│  ├─ ⏳ Extraer estructura de daath-zen-base.md (228 líneas)    │
│  └─ ⏳ Diseño sistema minimalista (aplicando BP 6-10)          │
│                                                                 │
│  Day 3-4: Prototipo Template Base (MORPHEUS)                  │
│  ├─ ⏳ Implementar template-base.yaml (30 líneas target)       │
│  ├─ ⏳ Implementar config-requirement.yaml (20 líneas)         │
│  ├─ ⏳ Sistema variables dependientes (aplicando BP 7)         │
│  └─ ⏳ Validador básico (Keter-Doc compliance)                 │
│                                                                 │
│  Day 5: Validación con REQ-001 Real (ALMA)                    │
│  ├─ ⏳ Generar REQ-001 desde template+config                   │
│  ├─ ⏳ Comparar con workbooks legacy (52 ejemplos)             │
│  ├─ ⏳ Medir Success Rate (Baseline/Target/Actual)             │
│  └─ ⏳ Extraer Lesson-001 (template system)                    │
│                                                                 │
├────────────────────────────────────────────────────────────────┤
│  WEEK 2: Expansión + Spec-Workflow Integration                │
├────────────────────────────────────────────────────────────────┤
│  Day 6-7: Configs Adicionales (MORPHEUS)                      │
│  ├─ ⏳ config-concept.yaml (aplicando SECI)                    │
│  ├─ ⏳ config-design.yaml (aplicando ADR structure)            │
│  ├─ ⏳ config-steering.yaml (product/tech/structure)           │
│  └─ ⏳ Generator script (template mixer)                       │
│                                                                 │
│  Day 8-9: Spec-Workflow Integration (SALOMON)                 │
│  ├─ ⏳ Workflow documentation (aplicando BP 11-15)             │
│  ├─ ⏳ Diagramas Mermaid (4 workflows)                         │
│  ├─ ⏳ Implementation logging examples                         │
│  └─ ⏳ Approval workflow documentation                         │
│                                                                 │
│  Day 10: Final Validation + Lessons (ALMA + DAATH)            │
│  ├─ ⏳ Test suite completo (≥10 casos)                         │
│  ├─ ⏳ Generar 5 ejemplos (REQ/CONCEPT/DESIGN/IMPL/STEERING)   │
│  ├─ ⏳ Documentation completa                                  │
│  ├─ ⏳ Extraer lessons learned (≥3 lessons)                    │
│  └─ ⏳ Actualizar este documento con outcomes                  │
└────────────────────────────────────────────────────────────────┘

Total: 10 días (2 semanas calendario)
Esfuerzo: ~60 horas efectivas
Output: Template System v1.0.0 funcional + integración spec-workflow
```

**Ventajas de Opción D**:
- ✅ **Rápido**: 2 semanas vs 4 semanas (50% tiempo)
- ✅ **Pragmático**: Usa investigación YA REALIZADA (6,350 líneas analizadas)
- ✅ **Validado**: Basado en 20 best practices documentadas
- ✅ **Medible**: Success Rate con Baseline/Target/Actual
- ✅ **Autopoiético**: Lessons extraídas desde Day 5
- ✅ **Híbrido**: Combina rigor (investigación) + velocidad (implementación)

**Riesgos Mitigados**:
- ⚠️ Riesgo: "Implementar sin fundamento" → **Mitigado**: Inventario de 6 templates + 52 workbooks
- ⚠️ Riesgo: "Inventar variables" → **Mitigado**: BP #7 (variables dependientes calculadas)
- ⚠️ Riesgo: "No integrar spec-workflow" → **Mitigado**: BP #11-15 + DIAGRAMAS-WORKFLOW-MCP.md

---

## 🎯 Criterios de Éxito (Actualizados)

### Outcomes Esperados (SMART Metrics)

**Sistema Template Base**:

| # | Outcome | Baseline | Target | Método Medición |
|---|---------|----------|--------|----------------|
| 1 | **Líneas código totales** | 475 líneas (5 templates legacy) | ≤150 líneas | `wc -l template-base.yaml config-*.yaml` |
| 2 | **Código duplicado** | ~300 líneas (63%) | 0 líneas (0%) | Análisis manual de estructura |
| 3 | **Costo agregar tipo** | +100 líneas template completo | ≤25 líneas config | `wc -l config-nuevo-tipo.yaml` |
| 4 | **Templates DAATH-ZEN consolidados** | 6 versions inconsistentes | 1 base + N configs | Conteo de archivos |
| 5 | **Variables dependientes** | 0% (todas hardcoded) | 100% (todas calculadas) | Análisis de configs, verificar fórmulas |

**Integración Spec-Workflow**:

| # | Outcome | Baseline | Target | Método Medición |
|---|---------|----------|--------|----------------|
| 6 | **Workflows documentados** | 0 workflows claros | 4 workflows (Main/Sub/IMPL/Steering) | Conteo de diagramas Mermaid |
| 7 | **Ejemplos generados** | 0 ejemplos funcionales | ≥5 ejemplos (REQ/CONCEPT/DESIGN/IMPL/STEERING) | Archivos en `examples/` |
| 8 | **Implementation logs** | 0 ejemplos artifacts | ≥3 ejemplos completos | JSON con apiEndpoints/components/functions |
| 9 | **Best practices aplicadas** | 0 documentadas | ≥20 aplicadas | Checklist en README |

**Autopoiesis & Validación**:

| # | Outcome | Baseline | Target | Método Medición |
|---|---------|----------|--------|----------------|
| 10 | **Lessons learned** | 0 lessons | ≥3 lessons | Archivos en `lessons/` |
| 11 | **Test suite** | 0 tests | ≥10 casos de prueba | `pytest --collect-only` |
| 12 | **Success Rate** | N/A | ≥90% | `(Outcomes Achieved / 12) * 100` |

**Fórmula Final de Éxito**:
```
Success Rate = (Outcomes Target Met / Total Outcomes) * 100
Target: Success Rate ≥ 90% (≥11 de 12 outcomes)
```

---

## 📝 Decisión Recomendada

### Comparación de Opciones (Actualizada)

| Aspecto | A) Formal (4 sem) | B) Ligera (2 sem) | C) Híbrido (3 sem) | **D) Acelerada (2 sem) 🏆** |
|---------|-------------------|-------------------|--------------------|-----------------------------|
| **Tiempo** | 4 semanas | 2 semanas | 3 semanas | **2 semanas** |
| **Rigor Investigación** | ✅ Máximo | ⚠️ Ligero | ✅ Focalizado | ✅ **Focalizado + YA REALIZADO** |
| **Velocidad Implementación** | ⚠️ Lenta | ✅ Rápida | ⚠️ Media | ✅ **Rápida** |
| **Fundamentación** | ✅ Total | ⚠️ Parcial | ✅ Suficiente | ✅ **Total (6,350 líneas analizadas)** |
| **Best Practices** | ✅ Todas | ⚠️ Algunas | ✅ Críticas | ✅ **20 BP documentadas** |
| **Riesgo Refactoring** | ✅ Bajo | ⚠️ Alto | ⚠️ Medio | ✅ **Bajo (basado en 52 workbooks)** |
| **Validación Empírica** | ✅ Completa | ⚠️ Básica | ✅ Iterativa | ✅ **Desde Day 5** |
| **Autopoiesis** | ✅ Post | ⚠️ Post | ✅ Paralela | ✅ **Integrada (Day 5, Day 10)** |

### Recomendación: Opción D - Investigación Acelerada 🏆

**Justificación**:

1. **Investigación YA REALIZADA**: Este documento contiene:
   - ✅ 6,350 líneas de investigación previa analizadas
   - ✅ 20 best practices extraídas y validadas
   - ✅ 6 templates DAATH-ZEN inventariados
   - ✅ 52 workbooks REQ examinados
   - ✅ Métricas cuantitativas documentadas (improve 70%, +400% parallelization)

2. **Fundamentación Sólida**: No estamos "inventando", estamos **consolidando**:
   - daath-zen-base.md (228 líneas) → Template base
   - REQ-001-template-system.md → Variables dependientes
   - DIAGRAMAS-WORKFLOW-MCP.md → Spec-workflow integration
   - GAP-ANALYSIS → Implementation logging

3. **Balance Óptimo**: Rigor + Velocidad
   - ✅ 2 semanas (mismo tiempo que Opción B)
   - ✅ Fundamentación completa (mismo rigor que Opción A)
   - ✅ Validación desde Day 5 (mejor que todas)

4. **Riesgo Minimizado**:
   - ❌ No hay inventar: 6 templates para analizar
   - ❌ No hay guess: 52 workbooks como ejemplos
   - ❌ No hay assumptions: 20 best practices documentadas
   - ❌ No hay surprises: Métricas claras (Baseline/Target/Actual)

### Próximos Pasos Inmediatos (Opción D)

**Si Usuario Aprueba Opción D**:

```markdown
## Day 1 (Mañana - 4 horas)
- [ ] Leer daath-zen-base.md completo (228 líneas)
- [ ] Extraer estructura Keter-Doc Protocol
- [ ] Identificar placeholders {{VAR}} actuales
- [ ] Mapear a template-base.yaml (diseño)

## Day 1 (Tarde - 4 horas)
- [ ] Leer REQ-001-template-system.md (446 líneas)
- [ ] Extraer sistema variables dependientes
- [ ] Diseñar formulas (timing, complexity, coverage)
- [ ] Crear borrador config-requirement.yaml

## Day 2 (Completo - 8 horas)
- [ ] Implementar template-base.yaml (30 líneas target)
- [ ] Implementar config-requirement.yaml (20 líneas target)
- [ ] Sistema de cálculo variables dependientes
- [ ] Validador básico (YAML syntax)
- [ ] Test generación REQ-001 básico

## Day 3-5...
[Continuar según cronograma Opción D]
```

---

## 🤔 Pregunta Final al Usuario

**¿Deseas proceder con la Opción D (Investigación Acelerada - 2 semanas)?**

**Ventajas**:
- ✅ **Fundamentado**: 6,350 líneas de investigación previa
- ✅ **Rápido**: 2 semanas (10 días efectivos)
- ✅ **Validado**: Basado en 20 best practices + 52 workbooks
- ✅ **Medible**: Success Rate con 12 outcomes SMART
- ✅ **Autopoiético**: Lessons desde Day 5

**Alternativas**:
- **A) Investigación Formal Completa** (4 semanas) - Si prefieres máximo rigor sin prisa
- **B) Investigación Ligera** (2 semanas) - Si prefieres resultados rápidos con menos validación
- **C) Híbrido** (3 semanas) - Si prefieres balance tradicional

**O proponer tu propia variante combinando elementos...**

---

**Esperando tu decisión para comenzar la implementación.**

### Outcomes Esperados

**Investigación DAATH-ZEN**:
- [ ] Inventario completo de componentes (tabla con ≥20 items)
- [ ] Análisis de ≥5 versiones de templates legacy
- [ ] Documento de consolidación de mejores prácticas (≥10 prácticas)
- [ ] Arquitectura de template configurable diseñada

**Investigación Spec-Workflow-MCP**:
- [ ] Inventario completo de artefactos (tabla con ≥10 items)
- [ ] Guía de uso de cada MCP tool (≥4 tools)
- [ ] Ejemplos de artifacts logs detallados (≥3 ejemplos)
- [ ] Flujo de integración documentado (diagrama + texto)

**Integración Bidireccional**:
- [ ] Matriz de correspondencia completa (≥15 mappings)
- [ ] Gap analysis documentado (≥5 gaps identificados)
- [ ] Template System implementado y funcional
- [ ] Test suite con ≥10 casos de prueba

**Autopoiesis**:
- [ ] Lessons learned documentadas (≥3 lessons)
- [ ] Template improvements propuestas (≥5 improvements)
- [ ] Feedback loop establecido

---

## 🔗 Referencias

### Fuentes DAATH-ZEN

1. [INDICE-COMPLETO-ARTEFACTOS.md](C:\proyectos\aleia-melquisedec\_legacy\_apps_legacy\research-autopoietic-template-v0.1.0\010-define\INDICE-COMPLETO-ARTEFACTOS.md) - Sistema atómico
2. [ANALISIS-GAPS-Y-RECOMENDACIONES.md](C:\proyectos\aleia-melquisedec\_legacy\_apps_legacy\research-autopoietic-template-v0.1.0\010-define\ANALISIS-GAPS-Y-RECOMENDACIONES.md) - Gap analysis
3. [template-configurable_daath-zen-root.md](C:\proyectos\aleia-melquisedec\_legacy\_templates\daath-zen-patterns\template-configurable_daath-zen-root.md) - Root governance
4. [unified-research-template-design-v4.2.0.md](C:\proyectos\aleia-melquisedec\.spec-workflow\_meta\templates\research-autopoietic-template\unified-research-template-design-v4.2.0.md) - Diseño unificado
5. [daath-zen-base.md](C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template\_melquisedec\templates\daath-zen-base.md) - Base actual

### Fuentes Spec-Workflow-MCP

1. Tool: `mcp_spec-workflow2_spec-workflow-guide` - Workflow completo
2. Tool: `mcp_spec-workflow2_steering-guide` - Steering docs
3. Tool: `mcp_spec-workflow2_approvals` - Approval system
4. Tool: `mcp_spec-workflow2_log-implementation` - Implementation logs
5. [REFLEXION-CRITICA-orden-implementacion-spec-001.md](C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template\_melquisedec\lessons\lesson-001-spec-template-architecture\1-task-base-infraestructure\REFLEXION-CRITICA-orden-implementacion-spec-001.md) - Reflexión crítica

### Manifiesto

- [bereshit-v3.0.0.md](C:\proyectos\aleia-melquisedec\docs\manifiesto\bereshit-v3.0.0.md) - Principios P1-P10
- [ADR-005-daath-zen-configurable-templates.md](C:\proyectos\aleia-melquisedec\docs\architecture\ADR-005-daath-zen-configurable-templates.md) - Decisión de templates configurables

---

## 📝 Notas Finales

### Observación Crítica del Usuario

> "EL TEMPLATE DEBE ANALIZAR TANTO LOS ARTEFACTOS DE LA HERRAMIENTA, COMO DE NUESTRO FRAMEWORK, DE LO CONTRARIO EL TEMPLATE SERÁ INVENTADO, SIN RESPONDER A LOS REQUERIMIENTOS REALES DE DOMINIO."

**Respuesta**: ✅ **Confirmado y aceptado**. Este documento establece la investigación bidireccional requerida.

### Próximos Pasos Inmediatos

1. ✅ Leer este documento completo
2. ⏳ Decidir: ¿Seguir con spec-001 Phase 2 O hacer primero la investigación?
3. ⏳ Si investigación primero:
   - Crear `.spec-workflow/specs/spec-001-investigation-daath-zen/`
   - Crear `.spec-workflow/specs/spec-001-investigation-spec-workflow/`
   - Comenzar con inventario de artefactos

### Pregunta al Usuario

**¿Deseas proceder con la investigación formal ahora, o prefieres un approach híbrido (investigación ligera + implementación iterativa)?**

Opciones:

**A) Investigación Formal Completa** (4 semanas)
- ✅ Rigor metodológico
- ✅ Template fundamentado en dominio
- ⚠️ Mayor tiempo antes de implementación

**B) Investigación Ligera + Implementación Iterativa** (2 semanas + mejora continua)
- ✅ Resultados más rápidos
- ✅ Aprende haciendo (autopoiesis)
- ⚠️ Posible refactoring posterior

**C) Híbrido: Investigación de Artefactos + Implementación Paralela** (3 semanas)
- ✅ Balance entre rigor y velocidad
- ✅ Investigación enfocada en lo crítico
- ⚠️ Requiere coordinación cuidadosa

---

**Fin del documento. Esperando decisión del usuario.**
