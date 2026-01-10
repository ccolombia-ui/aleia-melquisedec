# PRAXIS: Meta-Framework Unificado v4.1.0

```yaml
---
id: "ADR-003-praxis-meta-framework"
version: "4.1.0"
date: "2026-01-09"
status: "DRAFT"
name: "PRAXIS"
acronym: "Problem-Research-Architecture-eXecution-Insight-Synthesis"
authors: ["MELQUISEDEC", "SALOMON", "COPILOT"]
supersedes: ["unified-research-template-design-v4.0.0.md"]
---
```

---

## 1. Filosofía Central

### 1.1 El Problema que Resolvemos

Los frameworks existentes (DSR, IMRAD, DDD, CDIO) son **mutuamente excluyentes** en su aplicación tradicional. Un investigador debe elegir UNO y perder las fortalezas de los otros.

**PRAXIS propone**: Un **meta-framework de composición** donde:
- Las **PHASES** son universales (estructura común)
- Los **LENTES** son configurables (metodologías como plugins)
- Los **ARTIFACTS** evolucionan (living documents)
- El sistema es **AUTOPOIÉTICO** (se mejora a sí mismo)

### 1.2 Principios Fundacionales

| Principio | Descripción |
|-----------|-------------|
| **Composición sobre Herencia** | No heredas de DSR, COMPONES con lentes DSR |
| **Living Documents** | Los steering docs EVOLUCIONAN en cada phase |
| **Lentes como Plugins** | Cada metodología es un "lente" activable |
| **Trazabilidad Total** | Cada cambio registrado en Neo4j |
| **Autopoiesis** | El sistema mejora sus propios templates |

---

## 2. Análisis de Metodologías Integradas

### 2.1 Metodologías Base

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        METODOLOGÍAS ANALIZADAS                          │
├─────────────┬─────────────┬─────────────┬─────────────┬─────────────────┤
│    DSR      │   IMRAD     │   Social    │    DDD      │      CDIO       │
│  (Design    │(Introduction│  Research   │  (Domain    │   (Conceive     │
│   Science)  │  Methods    │ (Abductive) │   Driven)   │    Design       │
│             │  Results    │             │             │   Implement     │
│             │ Discussion) │             │             │    Operate)     │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────────┤
│ 1. Problem  │ 1. Intro    │ 1. Observe  │ 1. Conceive │ 1. Conceive     │
│ 2. Design   │ 2. Methods  │ 2. Hypothe- │ 2. Model    │ 2. Design       │
│ 3. Build    │ 3. Results  │    size     │ 3. Implement│ 3. Implement    │
│ 4. Evaluate │ 4. Discuss  │ 3. Validate │ 4. Validate │ 4. Operate      │
│ 5. Lessons  │             │ 4. Theorize │             │                 │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────────┘
```

### 2.2 Patrón Emergente: Las 6 Phases Universales

Al analizar todas las metodologías, emerge un **patrón común**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                    PHASES UNIVERSALES (PRAXIS)                          │
├───────────────────┬────────────────────────────────────────────────────┤
│ 000-BOOTSTRAP     │ Inception: Crear estructura inicial                │
│ 010-PROBLEM       │ Definition: Definir qué resolver                   │
│ 020-CONCEIVE      │ Conceptualization: Modelar el dominio              │
│ 030-DESIGN        │ Architecture: Diseñar la solución                  │
│ 040-BUILD         │ Realization: Construir la solución                 │
│ 050-EVALUATE      │ Validation: Validar contra requisitos              │
│ 060-LESSONS       │ Reflection: Extraer aprendizajes                   │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 3. Sistema de Lentes (Methodology Plugins)

### 3.1 Concepto de Lente

Un **LENTE** es una forma de "ver" una phase. Cada lente aporta:
- **Preguntas específicas** que hacer
- **Artefactos específicos** a generar
- **Prompts específicos** para el agente

```yaml
# Ejemplo: Lente DSR-GAPS para phase 010-problem
lens:
  id: "dsr-gaps"
  methodology: "DSR"
  phase: "010-problem"

  questions:
    - "¿Qué problema existe en la práctica?"
    - "¿Qué soluciones actuales son insuficientes?"
    - "¿Cuál es el gap entre estado actual y deseado?"

  artifacts:
    - name: "gap-analysis.md"
      template: "dsr/gap-analysis.tpl.md"

  prompts:
    - ref: "@salomon/identify-gaps.v1"
```

### 3.2 Lentes Disponibles por Phase

```
┌──────────────────┬─────────────────────────────────────────────────────┐
│     PHASE        │              LENTES DISPONIBLES                     │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 000-bootstrap    │ [structure] - Universal, sin variantes              │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 010-problem      │ [dsr-gaps]      → Análisis de gaps                  │
│                  │ [imrad-questions] → Preguntas de investigación      │
│                  │ [social-abductive] → Hipótesis abductiva            │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 020-conceive     │ [ddd-domain]    → Bounded contexts, ubiquitous lang │
│                  │ [cdio-needs]    → Necesidades del sistema           │
│                  │ [imrad-methods] → Métodos de investigación          │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 030-design       │ [dsr-design]    → Diseño de artefacto               │
│                  │ [ddd-model]     → Modelo de dominio                 │
│                  │ [cdio-design]   → Arquitectura de sistema           │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 040-build        │ [dsr-build]     → Construir artefacto               │
│                  │ [cdio-implement]→ Implementar sistema               │
│                  │ [imrad-execute] → Ejecutar métodos                  │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 050-evaluate     │ [dsr-evaluate]  → Evaluar artefacto                 │
│                  │ [imrad-results] → Analizar resultados               │
│                  │ [cdio-operate]  → Validar operación                 │
├──────────────────┼─────────────────────────────────────────────────────┤
│ 060-lessons      │ [dsr-lessons]   → Contribuciones a conocimiento     │
│                  │ [imrad-discussion] → Discusión e implicaciones      │
│                  │ [social-theory] → Teorización emergente             │
└──────────────────┴─────────────────────────────────────────────────────┘
```

### 3.3 Configuración de Lentes por Tipo de Proyecto

```yaml
# _templates/spec-types/methodology/manifest.yaml
spec_type: "methodology"
default_lenses:
  010-problem: ["dsr-gaps", "imrad-questions"]
  020-conceive: ["imrad-methods"]
  030-design: ["dsr-design"]
  040-build: ["dsr-build", "imrad-execute"]
  050-evaluate: ["dsr-evaluate", "imrad-results"]
  060-lessons: ["dsr-lessons", "imrad-discussion"]

# _templates/spec-types/app/manifest.yaml
spec_type: "app"
default_lenses:
  010-problem: ["dsr-gaps"]
  020-conceive: ["ddd-domain", "cdio-needs"]
  030-design: ["ddd-model", "cdio-design"]
  040-build: ["cdio-implement"]
  050-evaluate: ["cdio-operate"]
  060-lessons: ["dsr-lessons"]

# _templates/spec-types/social-project/manifest.yaml
spec_type: "social-project"
default_lenses:
  010-problem: ["social-abductive", "dsr-gaps"]
  020-conceive: ["imrad-methods"]
  030-design: ["dsr-design"]
  040-build: ["dsr-build"]
  050-evaluate: ["imrad-results"]
  060-lessons: ["social-theory", "dsr-lessons"]
```

---

## 4. Living Documents: Evolución de Steering Docs

### 4.1 El Concepto de Living Document

Los steering docs **NO son estáticos**. Cada phase puede **CREAR o ACTUALIZAR** un documento específico:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    EVOLUCIÓN DE STEERING DOCS                           │
├──────────────────┬──────────────────────────────────────────────────────┤
│     PHASE        │           ARTIFACT AFECTADO                          │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 000-bootstrap    │ steering/structure.md      [CREATE v1.0.0]           │
│                  │ ↳ Define estructura inicial del proyecto             │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 010-problem      │ specs/X/problem.md         [CREATE v1.0.0]           │
│                  │ ↳ Define el problema a resolver                      │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 020-conceive     │ steering/tech.md           [UPDATE v1.0.0→v1.1.0]    │
│                  │ ↳ Agrega especificación de dominio (DDD)             │
│                  │ ↳ Bounded contexts, ubiquitous language              │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 030-design       │ steering/product.md        [UPDATE v1.0.0→v1.1.0]    │
│                  │ ↳ Agrega roadmap por épicas                          │
│                  │ specs/X/design.md          [CREATE v1.0.0]           │
│                  │ ↳ Arquitectura de la solución                        │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 040-build        │ specs/X/tasks.md           [CREATE v1.0.0]           │
│                  │ ↳ Tareas ejecutables (spec-workflow-mcp format)      │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 050-evaluate     │ specs/X/requirements.md    [VALIDATE]                │
│                  │ ↳ Contrastar implementación vs requisitos            │
│                  │ approvals/                 [CREATE]                  │
│                  │ ↳ Solicitar aprobaciones formales                    │
├──────────────────┼──────────────────────────────────────────────────────┤
│ 060-lessons      │ specs/X/lessons.md         [CREATE v1.0.0]           │
│                  │ ↳ Aprendizajes extraídos                             │
│                  │ steering/problem.md        [UPDATE]                  │
│                  │ ↳ Retroalimentación al problema original             │
│                  │ _meta/patterns/            [UPDATE]                  │
│                  │ ↳ Patrones emergentes para futuros specs             │
└──────────────────┴──────────────────────────────────────────────────────┘
```

### 4.2 Diagrama de Flujo de Evolución

```
                    000-bootstrap
                         │
                         ▼
              ┌─────────────────────┐
              │ structure.md v1.0.0 │ CREATE
              └─────────────────────┘
                         │
                         ▼
                    010-problem
                         │
                         ▼
              ┌─────────────────────┐
              │ problem.md v1.0.0   │ CREATE (nuevo artefacto)
              └─────────────────────┘
                         │
                         ▼
                    020-conceive
                         │
                         ▼
              ┌─────────────────────┐
              │ tech.md v1.1.0      │ UPDATE (agrega dominio DDD)
              └─────────────────────┘
                         │
                         ▼
                    030-design
                         │
              ┌─────────┴─────────┐
              ▼                   ▼
    ┌─────────────────┐  ┌─────────────────┐
    │product.md v1.1.0│  │ design.md v1.0.0│
    │  UPDATE         │  │  CREATE         │
    └─────────────────┘  └─────────────────┘
                         │
                         ▼
                    040-build
                         │
                         ▼
              ┌─────────────────────┐
              │ tasks.md v1.0.0     │ CREATE
              └─────────────────────┘
                         │
                         ▼
                    050-evaluate
                         │
              ┌─────────┴─────────┐
              ▼                   ▼
    ┌─────────────────┐  ┌─────────────────┐
    │requirements.md  │  │ approvals/      │
    │  VALIDATE       │  │  CREATE         │
    └─────────────────┘  └─────────────────┘
                         │
                         ▼
                    060-lessons
                         │
              ┌─────────┴─────────────────┐
              ▼                           ▼
    ┌─────────────────┐         ┌─────────────────┐
    │ lessons.md v1.0.0│        │ _meta/patterns/ │
    │  CREATE          │        │  UPDATE         │
    └─────────────────┘         └─────────────────┘
                                          │
                                          ▼
                                 ┌─────────────────┐
                                 │ AUTOPOIESIS:    │
                                 │ Templates       │
                                 │ mejorados para  │
                                 │ próximo spec    │
                                 └─────────────────┘
```

---

## 5. Estructura de Directorios

### 5.1 Templates Globales (`_templates/`)

```
_templates/
├── manifest.yaml                        # Índice global
│
├── spec-types/                          # Tipos de spec (methodology, app, social)
│   ├── methodology/
│   │   ├── manifest.yaml                # Config: lentes default, phases
│   │   └── README.md
│   ├── app/
│   └── social-project/
│
├── phases/                              # Templates por phase
│   ├── 000-bootstrap/
│   │   ├── tasks.tpl.md                 # Tasks para esta phase
│   │   ├── artifacts.yaml               # Qué genera
│   │   └── structure.tpl.md             # Template del steering doc
│   │
│   ├── 010-problem/
│   │   ├── tasks.tpl.md
│   │   ├── artifacts.yaml
│   │   ├── problem.tpl.md               # Template nuevo artefacto
│   │   └── lenses/                      # Templates por lente
│   │       ├── dsr-gaps.tpl.md
│   │       ├── imrad-questions.tpl.md
│   │       └── social-abductive.tpl.md
│   │
│   ├── 020-conceive/
│   │   ├── tasks.tpl.md
│   │   ├── tech-update.tpl.md           # Update para tech.md
│   │   └── lenses/
│   │       ├── ddd-domain.tpl.md
│   │       └── cdio-needs.tpl.md
│   │
│   ├── 030-design/
│   ├── 040-build/
│   ├── 050-evaluate/
│   └── 060-lessons/
│
├── artifacts/                           # Tipos de artefacto
│   ├── book/, paper/, concept/, spec/, dataset/
│   └── _schemas/                        # JSON Schemas de validación
│
└── prompts/                             # Biblioteca de prompts versionados
    ├── _registry.yaml
    ├── melquisedec/
    ├── hypatia/
    ├── salomon/
    ├── morpheus/
    └── alma/
```

### 5.2 Proyecto Generado (`apps/research-X/`)

```
apps/research-X/
├── .spec-workflow/                      # spec-workflow-mcp
│   ├── config.toml
│   ├── steering/
│   │   ├── structure.md                 # 000-bootstrap CREATE
│   │   ├── tech.md                      # 020-conceive UPDATE
│   │   └── product.md                   # 030-design UPDATE
│   │
│   ├── specs/
│   │   └── main/                        # Spec principal
│   │       ├── problem.md               # 010-problem CREATE (NUEVO)
│   │       ├── requirements.md          # 050-evaluate VALIDATE
│   │       ├── design.md                # 030-design CREATE
│   │       ├── tasks.md                 # 040-build CREATE
│   │       └── lessons.md               # 060-lessons CREATE (NUEVO)
│   │
│   ├── phases/                          # Estado de cada phase
│   │   ├── 000-bootstrap.yaml
│   │   ├── 010-problem.yaml
│   │   ├── 020-conceive.yaml
│   │   ├── 030-design.yaml
│   │   ├── 040-build.yaml
│   │   ├── 050-evaluate.yaml
│   │   └── 060-lessons.yaml
│   │
│   └── approvals/
│
├── 000-bootstrap/                       # Working directory por phase
├── 010-problem/
├── 020-conceive/
├── 030-design/
├── 040-build/
├── 050-evaluate/
├── 060-lessons/
│   └── index.yaml                       # Índice de outputs
│
├── .melquisedec/                        # Metadata DAATH-ZEN
│   └── checkpoints/
│
└── README.md
```

---

## 6. Especificaciones Detalladas

### 6.1 Phase State File (`phases/010-problem.yaml`)

```yaml
# .spec-workflow/phases/010-problem.yaml
id: "010-problem"
name: "Problem Definition"
status: "completed"  # pending | in-progress | completed | blocked
started_at: "2026-01-09T10:00:00Z"
completed_at: "2026-01-09T12:30:00Z"

# Lentes activados para esta phase
active_lenses:
  - id: "dsr-gaps"
    status: "completed"
  - id: "imrad-questions"
    status: "completed"

# Artefactos generados
artifacts_generated:
  - path: "specs/main/problem.md"
    version: "1.0.0"
    action: "create"
  - path: "010-problem/gap-analysis.md"
    version: "1.0.0"
    action: "create"
  - path: "010-problem/research-questions.md"
    version: "1.0.0"
    action: "create"

# Checkpoint
checkpoint:
  id: "CK-PROBLEM"
  status: "passed"
  validated_at: "2026-01-09T12:25:00Z"
  criteria:
    problem_defined: true
    gaps_identified: true
    questions_formulated: true

# Trazabilidad
neo4j_ref: "phase:010-problem:research-X"
```

### 6.2 Problem.md Template (Nuevo Artefacto)

```markdown
<!-- _templates/phases/010-problem/problem.tpl.md -->
# Problem Definition: {{spec_name}}

```yaml
---
id: "problem-{{spec_name}}"
version: "1.0.0"
created: "{{current_date}}"
phase: "010-problem"
lenses_applied: {{active_lenses | tojson}}
---
```

## 1. Problem Statement

{{problem_statement}}

{% if 'dsr-gaps' in active_lenses %}
## 2. Gap Analysis (DSR Lens)

### 2.1 Current State
{{current_state}}

### 2.2 Desired State
{{desired_state}}

### 2.3 Identified Gaps

| Gap ID | Description | Impact | Priority |
|--------|-------------|--------|----------|
{% for gap in gaps %}
| GAP-{{loop.index}} | {{gap.description}} | {{gap.impact}} | {{gap.priority}} |
{% endfor %}
{% endif %}

{% if 'imrad-questions' in active_lenses %}
## 3. Research Questions (IMRAD Lens)

### 3.1 Primary Research Question
> **RQ1**: {{primary_question}}

### 3.2 Secondary Questions
{% for rq in secondary_questions %}
> **RQ{{loop.index + 1}}**: {{rq}}
{% endfor %}

### 3.3 Hypotheses (if applicable)
{% for h in hypotheses %}
- **H{{loop.index}}**: {{h}}
{% endfor %}
{% endif %}

{% if 'social-abductive' in active_lenses %}
## 4. Abductive Hypothesis (Social Research Lens)

### 4.1 Observations
{{observations}}

### 4.2 Surprising Facts
{{surprising_facts}}

### 4.3 Abductive Hypothesis
> If {{hypothesis}}, then the surprising facts would be explained because {{explanation}}.
{% endif %}

## 5. Scope & Boundaries

### 5.1 In Scope
{% for item in in_scope %}
- {{item}}
{% endfor %}

### 5.2 Out of Scope
{% for item in out_scope %}
- {{item}}
{% endfor %}

## 6. Success Criteria

| Criterion | Metric | Target |
|-----------|--------|--------|
{% for c in success_criteria %}
| {{c.name}} | {{c.metric}} | {{c.target}} |
{% endfor %}

---

## Next Phase

**→ 020-conceive**: Con el problema definido, proceder a conceptualizar la solución usando lentes [{{next_lenses | join(', ')}}].
```

### 6.3 Tech.md Update Template (020-conceive)

```markdown
<!-- _templates/phases/020-conceive/tech-update.tpl.md -->
<!-- APPEND to existing steering/tech.md -->

---

## Domain Specification (Updated in 020-conceive)

```yaml
updated: "{{current_date}}"
phase: "020-conceive"
lenses: {{active_lenses | tojson}}
```

{% if 'ddd-domain' in active_lenses %}
### Domain Model (DDD Lens)

#### Bounded Contexts

```mermaid
graph TB
    subgraph "{{domain_name}}"
    {% for bc in bounded_contexts %}
        {{bc.id}}["{{bc.name}}"]
    {% endfor %}
    {% for rel in context_relations %}
        {{rel.source}} -->|{{rel.type}}| {{rel.target}}
    {% endfor %}
    end
```

#### Ubiquitous Language

| Term | Definition | Context |
|------|------------|---------|
{% for term in ubiquitous_language %}
| {{term.name}} | {{term.definition}} | {{term.context}} |
{% endfor %}

#### Aggregates

{% for agg in aggregates %}
##### {{agg.name}}
- **Root Entity**: {{agg.root}}
- **Invariants**: {{agg.invariants | join(', ')}}
- **Events**: {{agg.events | join(', ')}}
{% endfor %}
{% endif %}

{% if 'cdio-needs' in active_lenses %}
### System Needs (CDIO Lens)

#### Functional Requirements
{% for req in functional_requirements %}
- **FR-{{loop.index}}**: {{req}}
{% endfor %}

#### Non-Functional Requirements
{% for req in non_functional_requirements %}
- **NFR-{{loop.index}}**: {{req}}
{% endfor %}

#### Constraints
{% for constraint in constraints %}
- {{constraint}}
{% endfor %}
{% endif %}
```

### 6.4 Tasks.tpl.md Format (spec-workflow-mcp compatible)

```markdown
<!-- _templates/phases/040-build/tasks.tpl.md -->
# Tasks: {{phase.name}}

> **Spec**: {{spec_name}}
> **Phase**: {{phase.id}}
> **Lenses**: {{active_lenses | join(', ')}}

---

## 1. Implementation Tasks

{% for task in tasks %}
- [ ] {{loop.index}}.{{task.sub_index}}. {{task.title}}
  - File: {{task.file}}
  - _Requirements: {{task.requirements | join(', ')}}_
  - _Prompt: @{{task.rostro | lower}}/{{task.prompt_ref}}_
  - _Params: {{task.params | dictsort | map('join', '=') | join(', ')}}_

{% endfor %}

## 2. Checkpoint

- [ ] {{tasks | length + 1}}.1. Validate phase completion
  - File: .spec-workflow/phases/{{phase.id}}.yaml
  - _Requirements: CK-{{phase.id | upper}}_
  - _Prompt: @melquisedec/validate-checkpoint.v1_
```

---

## 7. Flujo de Ejecución

### 7.1 Crear Nuevo Proyecto

```bash
# Comando conceptual
praxis create \
  --type methodology \
  --name "neo4j-llamaindex" \
  --lenses "dsr,imrad" \
  --output "apps/research-neo4j-llamaindex"
```

### 7.2 Secuencia de Phases

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         FLUJO DE EJECUCIÓN                              │
└─────────────────────────────────────────────────────────────────────────┘

[START]
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 000-BOOTSTRAP                                                           │
│ ───────────────                                                         │
│ • Crear estructura de directorios                                       │
│ • Generar steering/structure.md v1.0.0                                  │
│ • Inicializar .spec-workflow/                                           │
│ • Checkpoint: CK-BOOTSTRAP (auto-pass)                                  │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 010-PROBLEM                                                             │
│ ────────────                                                            │
│ • Activar lentes: [dsr-gaps, imrad-questions]                          │
│ • Ejecutar prompts de cada lente                                        │
│ • Generar specs/main/problem.md v1.0.0                                  │
│ • Checkpoint: CK-PROBLEM (requiere approval)                            │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼ [Approval Gate]
┌─────────────────────────────────────────────────────────────────────────┐
│ 020-CONCEIVE                                                            │
│ ─────────────                                                           │
│ • Activar lentes: [ddd-domain] o [imrad-methods]                       │
│ • Modelar dominio o métodos de investigación                            │
│ • ACTUALIZAR steering/tech.md v1.0.0 → v1.1.0                          │
│ • Checkpoint: CK-CONCEIVE                                               │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 030-DESIGN                                                              │
│ ───────────                                                             │
│ • Activar lentes: [dsr-design]                                         │
│ • Diseñar arquitectura de solución                                      │
│ • ACTUALIZAR steering/product.md (roadmap, epics)                       │
│ • Generar specs/main/design.md v1.0.0                                   │
│ • Checkpoint: CK-DESIGN (requiere approval)                             │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼ [Approval Gate]
┌─────────────────────────────────────────────────────────────────────────┐
│ 040-BUILD                                                               │
│ ──────────                                                              │
│ • Activar lentes: [cdio-implement]                                     │
│ • Generar specs/main/tasks.md v1.0.0                                    │
│ • Ejecutar tareas (spec-workflow-mcp)                                   │
│ • Checkpoint: CK-BUILD (por cada task completada)                       │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 050-EVALUATE                                                            │
│ ─────────────                                                           │
│ • Activar lentes: [dsr-evaluate, imrad-results]                        │
│ • Contrastar implementación vs requirements                             │
│ • VALIDAR specs/main/requirements.md                                    │
│ • Crear approval requests                                               │
│ • Checkpoint: CK-EVALUATE (requiere approval final)                     │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼ [Approval Gate]
┌─────────────────────────────────────────────────────────────────────────┐
│ 060-LESSONS                                                             │
│ ────────────                                                            │
│ • Activar lentes: [dsr-lessons, imrad-discussion]                      │
│ • Extraer aprendizajes                                                  │
│ • Generar specs/main/lessons.md v1.0.0                                  │
│ • ACTUALIZAR _meta/patterns/ (autopoiesis)                              │
│ • Generar 060-lessons/index.yaml (índice de outputs)                    │
│ • Checkpoint: CK-LESSONS (cierre)                                       │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ▼
[END → Autopoiesis: Templates mejorados para próximo spec]
```

---

## 8. Integración con DAATH-ZEN

### 8.1 Mapeo Rostros → Phases

| Phase | Rostro Principal | MCPs Base | MCPs Especializados |
|-------|-----------------|-----------|---------------------|
| 000-bootstrap | MELQUISEDEC | neo4j, memory | filesystem |
| 010-problem | SALOMON | neo4j, memory | sequential-thinking, perplexity |
| 020-conceive | HYPATIA | neo4j, memory | brave-search, context7, arxiv |
| 030-design | MORPHEUS | neo4j, memory | sequential-thinking, filesystem |
| 040-build | MORPHEUS | neo4j, memory | filesystem, python-env, git |
| 050-evaluate | SALOMON | neo4j, memory | sequential-thinking |
| 060-lessons | ALMA | neo4j, memory | git, github, filesystem |

### 8.2 Output Triple por Phase

Cada phase genera el **Output Triple** de DAATH-ZEN:

1. **Cypher**: Registro en Neo4j
   ```cypher
   CREATE (p:Phase {id: "010-problem", spec: "research-X", status: "completed"})
   CREATE (p)-[:GENERATED]->(a:Artifact {path: "specs/main/problem.md"})
   CREATE (p)-[:USED_LENS]->(l:Lens {id: "dsr-gaps"})
   ```

2. **Markdown**: Artefactos generados (problem.md, design.md, etc.)

3. **Lesson**: Aprendizajes destilados en 060-lessons

---

## 9. Autopoiesis: El Sistema que Mejora a Sí Mismo

### 9.1 Flujo de Autopoiesis

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CICLO AUTOPOIÉTICO                              │
└─────────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────┐
                    │   060-lessons       │
                    │   (Spec actual)     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Extraer patrones    │
                    │ - ¿Qué funcionó?    │
                    │ - ¿Qué falló?       │
                    │ - ¿Qué mejorar?     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ _meta/patterns/     │
                    │ pattern-XXX.yaml    │
                    │ confidence: 0.75    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │ Si confidence ≥ 0.80│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ _templates/         │
                    │ UPDATE prompts      │
                    │ UPDATE templates    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Próximo spec        │
                    │ hereda mejoras      │
                    └─────────────────────┘
```

### 9.2 Pattern File Format

```yaml
# _meta/patterns/pattern-001-dsr-gap-structure.yaml
id: "pattern-001"
name: "DSR Gap Analysis Structure"
version: "1.0.0"
confidence: 0.85
validated_in:
  - "research-neo4j-llamaindex"
  - "research-keter-migration"
  - "research-mcp-toolkit"

observation: |
  El análisis de gaps es más efectivo cuando incluye:
  1. Estado actual con evidencia
  2. Estado deseado con métricas
  3. Gaps priorizados por impacto

recommendation: |
  Actualizar template dsr-gaps.tpl.md para incluir:
  - Campo obligatorio "evidence" en current_state
  - Campo obligatorio "metrics" en desired_state
  - Priorización automática por impacto × urgencia

affected_templates:
  - path: "phases/010-problem/lenses/dsr-gaps.tpl.md"
    action: "update"
    changes:
      - "Add evidence field"
      - "Add metrics field"
      - "Add auto-prioritization"

changelog:
  - date: "2026-01-09"
    action: "created"
    from_spec: "research-keter-migration"
```

---

## 10. Migración desde Sistema Actual

### 10.1 Archivos a Transformar

| Archivo Actual | Acción | Nuevo Destino |
|----------------|--------|---------------|
| `_meta/best-practices.md` | SPLIT | `_templates/prompts/` (por rostro) |
| `_meta/GUIA_RAPIDA.md` | TRANSFORM | `_templates/README.md` |
| `_meta/RESUMEN_SISTEMA_COMPLETO.md` | SUPERSEDE | Este documento |
| `archive/templates/tasks.md` | DECOMPOSE | `_templates/phases/*/tasks.tpl.md` |
| `apps/00-template/` | EVOLVE | `_templates/spec-types/` |
| `_templates/_daath-template/` | INTEGRATE | `_templates/artifacts/` |

### 10.2 Plan de Implementación

1. **Phase 1**: Crear estructura `_templates/` base
2. **Phase 2**: Migrar prompts a biblioteca versionada
3. **Phase 3**: Crear spec-types (methodology, app, social-project)
4. **Phase 4**: Crear lentes por methodology
5. **Phase 5**: Implementar living documents
6. **Phase 6**: Implementar autopoiesis

---

## 11. Resumen Ejecutivo

### Lo que PRAXIS v4.1.0 logra:

| Aspecto | Antes | Después |
|---------|-------|---------|
| Metodologías | Elige UNA | COMPONE múltiples (lentes) |
| Steering docs | Estáticos | Living documents que evolucionan |
| Templates | Monolítico (1551 líneas) | Modulares por phase + lente |
| Prompts | Embebidos en tasks | Biblioteca versionada |
| Fases | Solo DSR | Universal (6 phases) + lentes |
| Artefactos spec | Solo 3 (req, design, tasks) | 5 (+ problem.md, lessons.md) |
| Autopoiesis | Manual | Automática con confidence scores |

### Diferencia clave vs v4.0.0:

> **v4.0.0**: Phases = DSR phases, artifacts separados
>
> **v4.1.0**: Phases = Meta-framework universal, LENTES como plugins de metodología, LIVING DOCUMENTS que evolucionan con cada phase

---

## Referencias

- [spec-workflow-mcp Documentation](https://github.com/pimzino/spec-workflow-mcp)
- [DAATH-ZEN Manifiesto](../manifiesto/bereshit-v3.0.0.md)
- [DSR Methodology - Hevner et al.](https://www.jstor.org/stable/25148625)
- [IMRAD Structure](https://en.wikipedia.org/wiki/IMRAD)
- [Domain-Driven Design - Eric Evans](https://domainlanguage.com/ddd/)
- [CDIO Syllabus](http://www.cdio.org/)

---

```yaml
---
changelog:
  - version: "4.1.0"
    date: "2026-01-09"
    changes:
      - "Introducción del concepto LENTES como plugins de metodología"
      - "Living Documents que evolucionan en cada phase"
      - "Nuevo artefacto problem.md antes de requirements"
      - "Nuevo artefacto lessons.md para cierre"
      - "Phase state files en .spec-workflow/phases/"
      - "Integración explícita con múltiples metodologías"
      - "Sistema de autopoiesis con confidence scores"
  - version: "4.0.0"
    date: "2026-01-09"
    changes:
      - "Versión inicial con separación spec-types/artifacts/prompts"
---
```
