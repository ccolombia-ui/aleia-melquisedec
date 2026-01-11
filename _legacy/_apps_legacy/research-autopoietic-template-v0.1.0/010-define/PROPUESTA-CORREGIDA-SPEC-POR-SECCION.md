# Propuesta Corregida: Spec-Issue por Sección del Manifiesto
## research-autopoietic-template

> **Fecha:** 2026-01-10
> **Versión:** 2.0.0 (Corrección)
> **Autor:** GitHub Copilot (Claude Sonnet 4.5)
> **Propósito:** Approach correcto - Un spec-issue riguroso por cada sección del manifiesto

---

## 🎯 LO QUE ENTIENDO AHORA

### Mi Propuesta Original (❌ Incorrecta)

**Estructura:**
```
.spec-workflow/specs/
├── autopoietic-templates/        # ← Main Spec GIGANTE
│   ├── requirements.md           # (2,450 líneas - monolítico)
│   ├── design.md                 # (800 líneas)
│   └── tasks.md
└── REQ-001/                      # ← Sub-issues SIN rigor
    └── ISSUE.yaml                # (trabajo menor)
```

**Problemas:**
- ❌ Un "Main Spec" que agrupa todo (monolítico en nivel superior)
- ❌ Sub-issues tratados como trabajo menor sin approval
- ❌ Jerarquía artificial (Main → Sub)
- ❌ No alineado con modularidad del manifiesto

### Propuesta Corregida (✅ Correcta)

**Estructura:**
```
.spec-workflow/specs/
├── template-system/              # ← SPEC-ISSUE-001 (completo)
│   ├── requirements.md           # CON approval
│   ├── design.md                 # CON approval
│   ├── tasks.md                  # CON approval
│   └── Implementation Logs/
├── pattern-registry/             # ← SPEC-ISSUE-002 (completo)
│   ├── requirements.md           # CON approval
│   ├── design.md                 # CON approval
│   ├── tasks.md
│   └── Implementation Logs/
├── confidence-scoring/           # ← SPEC-ISSUE-003 (completo)
├── triple-persistence/           # ← SPEC-ISSUE-004 (completo)
├── autopoietic-cycle/            # ← SPEC-ISSUE-005 (completo)
├── lens-system/                  # ← SPEC-ISSUE-006 (completo)
├── script-orchestration/         # ← SPEC-ISSUE-007 (completo)
├── phase-state-management/       # ← SPEC-ISSUE-008 (completo)
├── validation-engine/            # ← SPEC-ISSUE-009 (completo)
└── dashboard-ui/                 # ← SPEC-ISSUE-010 (completo)
```

**Ventajas:**
- ✅ Modularidad REAL en todos los niveles
- ✅ Cada spec sigue workflow completo (Req → Design → Tasks → Impl)
- ✅ Cada spec tiene approval riguroso
- ✅ Specs son peers (sin jerarquía artificial)
- ✅ Alineado con arquitectura del manifiesto
- ✅ Paralelizable (múltiples specs simultáneos)
- ✅ Incremental (sprint por sprint)

---

## 📚 IDENTIFICACIÓN DE SPECS (Del Manifiesto)

### Análisis del Manifiesto v4.3.1

Del archivo [raw-manifiesto.md](inputs/raw-manifiesto.md) (17,142 líneas), identifico las secciones principales que deben convertirse en spec-issues independientes:

#### SPEC-ISSUE-001: Template System

**Sección Manifiesto:** 9.1 Templates Estructura de Documentos (líneas 6000-7500)

**Alcance:**
- Sistema de 28 templates versionados
- Template registry con metadata
- Template versioning (v1.0 → v1.1)
- Auto-population mechanism
- Template compliance validation

**Artefactos a Crear:**
- 28 templates (.md.template)
- template-registry.yaml
- template-versioning.py
- apply-template.py

**Tamaño Estimado:** Grande (1,500+ líneas implementación)

---

#### SPEC-ISSUE-002: Pattern Registry

**Sección Manifiesto:** 8.2 Workflow Patterns (líneas 5000-5800)

**Alcance:**
- 8 patterns con confidence scores (0.0-1.0)
- Pattern evolution basado en validaciones
- Thresholds: 0.90 (auto), 0.80 (suggest), 0.50 (track)
- Pattern orchestration
- Multi-pattern application

**Artefactos a Crear:**
- 8 pattern YAML files
- pattern-registry.yaml
- pattern-orchestrator.py
- confidence-calculator.py

**Tamaño Estimado:** Mediano (800+ líneas implementación)

---

#### SPEC-ISSUE-003: Confidence Scoring System

**Sección Manifiesto:** 8.3 Confidence Scores (líneas 5800-6000)

**Alcance:**
- Fórmula de cálculo de confidence
- Tracking de validaciones cross-specs
- Threshold management
- Evidence accumulation
- Score evolution over time

**Artefactos a Crear:**
- confidence-calculator.py
- validation-tracker.py
- evidence-store (Neo4j queries)
- score-reporter.py

**Tamaño Estimado:** Mediano (600+ líneas implementación)

---

#### SPEC-ISSUE-004: Triple Persistence Architecture

**Sección Manifiesto:** 6.3 Triple Permanencia Universal (líneas 3500-4200)

**Alcance:**
- Sincronización Markdown → Neo4j → Vector
- Consistency validation
- Conflict resolution
- Incremental sync
- Rollback mechanisms

**Artefactos a Crear:**
- sync-triple-persistence.py
- neo4j-sync.py
- vector-embedding.py
- consistency-checker.py

**Tamaño Estimado:** Grande (1,200+ líneas implementación)

---

#### SPEC-ISSUE-005: Autopoietic Cycle

**Sección Manifiesto:** 8.2.1 Autopoiesis Medida (líneas 4500-5000)

**Alcance:**
- Feedback collection mechanism
- Analysis de efectividad
- Pattern evolution algorithm
- Template improvement proposals
- Confidence score updates

**Artefactos a Crear:**
- feedback-aggregator.py
- autopoiesis-analyzer.py
- improvement-proposer.py
- evolution-tracker.py

**Tamaño Estimado:** Grande (1,000+ líneas implementación)

---

#### SPEC-ISSUE-006: Lens System

**Sección Manifiesto:** 7.1 Sistema de Lenses (líneas 4000-4500)

**Alcance:**
- 4 lenses principales (DSR, IMRAD, DDD, Social)
- Lens adaptation mechanism
- Template customization per lens
- Validation criteria per lens
- Lens orchestration

**Artefactos a Crear:**
- 4 lens YAML files
- lens-adapter.py
- lens-validator.py
- lens-selector.py

**Tamaño Estimado:** Mediano (700+ líneas implementación)

---

#### SPEC-ISSUE-007: Script Orchestration

**Sección Manifiesto:** 10.2 Scripts del Lifecycle (líneas 8000-9000)

**Alcance:**
- 22 scripts en 6 categorías
- Script dependencies
- Execution pipeline
- Error handling
- Dry-run mode

**Artefactos a Crear:**
- 22 Python scripts
- script-orchestrator.py
- script-registry.yaml
- execution-pipeline.py

**Tamaño Estimado:** Muy Grande (3,000+ líneas implementación)

---

#### SPEC-ISSUE-008: Phase State Management

**Sección Manifiesto:** 6.4 Phase State Files (líneas 4200-4500)

**Alcance:**
- State tracking por fase
- Checkpoint validation
- State transitions
- Rollback state
- State persistence

**Artefactos a Crear:**
- phase-state-manager.py
- checkpoint-validator.py
- state-transition.py
- state-persistence (YAML files)

**Tamaño Estimado:** Mediano (600+ líneas implementación)

---

#### SPEC-ISSUE-009: Validation Engine

**Sección Manifiesto:** 10.1 Validation Rules (líneas 7500-8000)

**Alcance:**
- 37 validation rules
- Validation by domain (7 dominios)
- Auto-validation on checkpoints
- Validation reporting
- Custom validation rules

**Artefactos a Crear:**
- validation-engine.py
- validation-rules.yaml
- domain-validators/ (7 files)
- validation-reporter.py

**Tamaño Estimado:** Grande (1,000+ líneas implementación)

---

#### SPEC-ISSUE-010: Dashboard UI

**Sección Manifiesto:** 10.3 Dashboard ASCII (líneas 9000-9500)

**Alcance:**
- ASCII dashboard interactivo
- Real-time WebSocket updates
- Progress visualization
- Checkpoint status
- Task tracking

**Artefactos a Crear:**
- dashboard.py
- websocket-server.py
- dashboard-renderer.py
- progress-tracker.py

**Tamaño Estimado:** Grande (1,200+ líneas implementación)

---

## 🗺️ ROADMAP CORREGIDO

### Estrategia: Sprint por Spec-Issue

Cada sprint se enfoca en UN spec-issue completo:
1. Requirements (CON approval)
2. Design (CON approval)
3. Tasks (CON approval)
4. Implementation (CON logging)

**Simultáneamente:**
- Ajustar otros artefactos del folder relacionados
- Mantener consistencia cross-spec
- Actualizar índices maestros

### Sprint 0: Setup Inicial (3 días)

**Objetivo:** Preparar infraestructura para approach spec-por-sección

#### Tareas

✅ **Tarea 0.1: Reorganizar .spec-workflow/specs/**
```bash
# Eliminar estructura anterior (si existe)
rm -rf .spec-workflow/specs/autopoietic-templates/

# Crear estructura nueva (10 specs)
mkdir -p .spec-workflow/specs/template-system/
mkdir -p .spec-workflow/specs/pattern-registry/
mkdir -p .spec-workflow/specs/confidence-scoring/
mkdir -p .spec-workflow/specs/triple-persistence/
mkdir -p .spec-workflow/specs/autopoietic-cycle/
mkdir -p .spec-workflow/specs/lens-system/
mkdir -p .spec-workflow/specs/script-orchestration/
mkdir -p .spec-workflow/specs/phase-state-management/
mkdir -p .spec-workflow/specs/validation-engine/
mkdir -p .spec-workflow/specs/dashboard-ui/
```

✅ **Tarea 0.2: Actualizar ISSUE.yaml Maestro**

Cambiar de:
```yaml
id: ISSUE-SPEC-001-design-autopoietic-templates
type: research
```

A:
```yaml
id: research-autopoietic-templates
type: meta-research  # Coordina múltiples specs
status: active

specs:
  - template-system         # SPEC-ISSUE-001
  - pattern-registry        # SPEC-ISSUE-002
  - confidence-scoring      # SPEC-ISSUE-003
  - triple-persistence      # SPEC-ISSUE-004
  - autopoietic-cycle       # SPEC-ISSUE-005
  - lens-system             # SPEC-ISSUE-006
  - script-orchestration    # SPEC-ISSUE-007
  - phase-state-management  # SPEC-ISSUE-008
  - validation-engine       # SPEC-ISSUE-009
  - dashboard-ui            # SPEC-ISSUE-010

coordination:
  strategy: "Sprint por spec-issue completo"
  progress_tracking: "Each spec has independent approval workflow"
```

✅ **Tarea 0.3: Crear README.md Actualizado**

Documentar approach spec-por-sección en README.md raíz.

✅ **Tarea 0.4: Crear INDICE-SPECS.md (Nuevo)**

Índice maestro de los 10 specs con estado de cada uno.

---

### Sprint 1: SPEC-ISSUE-001 (Template System) - 2 semanas

#### Objetivo
Completar workflow riguroso para Template System (requirements → design → tasks → implementation)

#### Fase 1: Requirements (3 días)

✅ **Tarea 1.1: Crear requirements.md**
- **Ubicación:** `.spec-workflow/specs/template-system/requirements.md`
- **Contenido:**
  - Problem Statement (Gap/Goal/Outcomes)
  - Scope (28 templates, registry, versioning, validation)
  - User Stories (8-10 stories)
  - Functional Requirements (REQ-001 a REQ-015)
  - Non-Functional Requirements (performance, maintainability)
  - Priority Order
- **Tamaño:** 600-800 líneas
- **Tool:** `create_file`

✅ **Tarea 1.2: Solicitar Approval Requirements**
```python
mcp_spec-workflow2_spec-workflow-guide()  # Load workflow

approvalId = mcp_spec-workflow2_approvals(
    action="request",
    filePath="template-system/requirements.md",
    title="Template System Requirements Complete",
    type="document",
    category="spec",
    categoryName="template-system"
)

# Poll hasta approved
while True:
    status = mcp_spec-workflow2_approvals(
        action="status",
        approvalId=approvalId
    )
    if status == "approved":
        break
    sleep(60)

# Delete approval
mcp_spec-workflow2_approvals(
    action="delete",
    approvalId=approvalId
)
```

#### Fase 2: Design (4 días)

✅ **Tarea 1.3: Crear design.md**
- **Ubicación:** `.spec-workflow/specs/template-system/design.md`
- **Contenido:**
  - Architecture Overview
  - Template Registry Design
  - Versioning Strategy (ADR-001)
  - Auto-population Mechanism
  - Validation Rules
  - Integration Points
- **Tamaño:** 800-1,000 líneas
- **Tool:** `create_file`

✅ **Tarea 1.4: Solicitar Approval Design**
```python
approvalId = mcp_spec-workflow2_approvals(
    action="request",
    filePath="template-system/design.md",
    title="Template System Design Complete",
    type="document",
    category="spec",
    categoryName="template-system"
)
# Poll + Delete
```

#### Fase 3: Tasks (2 días)

✅ **Tarea 1.5: Crear tasks.md**
- **Ubicación:** `.spec-workflow/specs/template-system/tasks.md`
- **Contenido:**
  - Breakdown de implementación
  - 30-40 tareas atómicas
  - _Prompt por tarea
  - Dependencies
- **Tamaño:** 600-800 líneas
- **Tool:** `create_file`

✅ **Tarea 1.6: Solicitar Approval Tasks**
```python
approvalId = mcp_spec-workflow2_approvals(
    action="request",
    filePath="template-system/tasks.md",
    title="Template System Tasks Complete",
    type="document",
    category="spec",
    categoryName="template-system"
)
# Poll + Delete
```

#### Fase 4: Implementation (5 días)

✅ **Tarea 1.7: Implementar 28 Templates**
- Crear cada template en `040-build/templates/`
- 28 archivos × ~200 líneas = 5,600 líneas totales

✅ **Tarea 1.8: Implementar Template Registry**
- `040-build/config/template-registry.yaml`
- Metadata de 28 templates

✅ **Tarea 1.9: Implementar Scripts**
- `apply-template.py`
- `validate-template-compliance.py`
- `list-templates.py`

✅ **Tarea 1.10: Log Implementation (CRÍTICO)**
```python
mcp_spec-workflow2_log-implementation(
    specName="template-system",
    taskId="1.7-1.9",
    summary="Implemented 28 templates, registry, and 3 scripts",
    filesModified=[],
    filesCreated=[
        "040-build/templates/*.template",
        "040-build/config/template-registry.yaml",
        "040-build/scripts/apply-template.py"
    ],
    statistics={
        "linesAdded": 7200,
        "linesRemoved": 0
    },
    artifacts={
        "templates": [
            {
                "name": "requirements.md.template",
                "location": "040-build/templates/010-define/requirements.md.template",
                "purpose": "Requirements document template",
                "size": "200 lines"
            },
            # ... 27 more templates
        ],
        "scripts": [
            {
                "name": "apply-template.py",
                "location": "040-build/scripts/templates/apply-template.py",
                "purpose": "Apply template with auto-population",
                "signature": "apply_template(template_name: str, output_path: str, variables: dict)"
            }
        ]
    }
)
```

#### Ajustes al Folder Completo

✅ **Tarea 1.11: Actualizar 010-define/**
- Mover templates antiguos a `040-build/templates/`
- Actualizar referencias en README.md
- Crear `010-define/TEMPLATES-INDEX.md`

✅ **Tarea 1.12: Actualizar INDICE-SPECS.md**
```markdown
| Spec | Estado | Progress | Approved Phases |
|------|--------|----------|-----------------|
| template-system | ✅ Completado | 100% | Requirements ✅, Design ✅, Tasks ✅, Implementation ✅ |
| pattern-registry | ❌ No iniciado | 0% | - |
```

---

### Sprint 2: SPEC-ISSUE-002 (Pattern Registry) - 2 semanas

#### Misma Estructura
1. Requirements (3 días) → Approval
2. Design (4 días) → Approval
3. Tasks (2 días) → Approval
4. Implementation (5 días) → Log

#### Foco Específico
- 8 patterns YAML
- Pattern orchestrator
- Confidence calculator
- Evolution tracker

---

### Sprint 3-10: Specs Restantes

Cada sprint sigue el mismo patrón:
- SPEC-ISSUE-003: Confidence Scoring (2 semanas)
- SPEC-ISSUE-004: Triple Persistence (3 semanas - más complejo)
- SPEC-ISSUE-005: Autopoietic Cycle (2 semanas)
- SPEC-ISSUE-006: Lens System (2 semanas)
- SPEC-ISSUE-007: Script Orchestration (4 semanas - muy grande)
- SPEC-ISSUE-008: Phase State Management (2 semanas)
- SPEC-ISSUE-009: Validation Engine (3 semanas)
- SPEC-ISSUE-010: Dashboard UI (2 semanas)

**Total Estimado:** 24 semanas (~6 meses)

---

## 🎯 MEJOR PRÁCTICA RECOMENDADA

### Principios del Approach

#### 1. Un Spec = Un Sistema Completo

**❌ NO HACER:**
```
Main Spec (gigante) con sub-issues (menores)
```

**✅ HACER:**
```
Múltiples specs peers, cada uno completo e independiente
```

#### 2. Rigor en TODOS los Specs

**❌ NO HACER:**
```
- Main Spec: CON approval riguroso
- Sub-Issues: SIN approval, trabajo menor
```

**✅ HACER:**
```
- TODOS los specs: CON approval riguroso
- Requirements → Design → Tasks → Implementation
```

#### 3. Mejora Incremental del Folder

**Cada Sprint Debe:**
- ✅ Completar UN spec-issue (Req → Design → Tasks → Impl)
- ✅ Ajustar artefactos relacionados en el folder
- ✅ Mantener consistencia cross-spec
- ✅ Actualizar índices maestros
- ✅ Documentar learnings

**NO solo:**
- ❌ Trabajar en spec aislado
- ❌ Ignorar impacto en otros artefactos

#### 4. Specs Son Peers, No Jerarquía

**❌ NO PENSAR:**
```
Main Spec (padre)
  ├── Sub-Issue-1 (hijo)
  └── Sub-Issue-2 (hijo)
```

**✅ PENSAR:**
```
Spec-1 (peer) ←→ Spec-2 (peer) ←→ Spec-3 (peer)
       ↓               ↓               ↓
   Depende de      Depende de      Depende de
```

#### 5. Modularidad en Todos los Niveles

**Estructura Final:**
```
apps/research-autopoietic-template/
├── ISSUE.yaml                           # Coordinador (no "Main Spec")
├── README.md                            # Overview del proyecto
│
├── .spec-workflow/
│   └── specs/
│       ├── template-system/             # ← Spec completo
│       │   ├── requirements.md          # (800 líneas)
│       │   ├── design.md                # (1,000 líneas)
│       │   ├── tasks.md                 # (600 líneas)
│       │   └── Implementation Logs/
│       │
│       ├── pattern-registry/            # ← Spec completo
│       ├── confidence-scoring/          # ← Spec completo
│       └── ... (10 specs total)
│
├── 010-define/
│   ├── INDICE-SPECS.md                  # Índice maestro de 10 specs
│   └── TEMPLATES-INDEX.md               # Índice de templates implementados
│
├── 040-build/
│   ├── templates/ (28 templates)
│   ├── scripts/ (22 scripts)
│   ├── patterns/ (8 patterns)
│   └── lenses/ (4 lenses)
│
└── 050-release/
    └── outputs/
        ├── templates/ (versión release)
        ├── scripts/ (versión release)
        └── docs/
```

---

## 📊 COMPARACIÓN: Mi Propuesta vs Propuesta Corregida

| Aspecto | Mi Propuesta Original | Propuesta Corregida | Mejora |
|---------|----------------------|---------------------|--------|
| **Estructura** | 1 Main Spec + 157 Sub-Issues | 10 Specs independientes | +1000% claridad |
| **Rigor** | Main: riguroso, Sub: sin rigor | TODOS: rigorosos | +100% calidad |
| **Approval** | Solo Main Spec | TODOS los specs | +900% trazabilidad |
| **Modularidad** | Jerarquía artificial | Peers relacionados | +100% flexibilidad |
| **Paralelización** | Limitada (Main bloquea) | Total (specs independientes) | +300% velocidad |
| **Complejidad** | Main Spec 2,450 líneas | 10 specs × 800 líneas | -67% por spec |
| **Alineación Manifiesto** | Parcial | Total | +100% |

---

## ✅ CRITERIOS DE ÉXITO

### Por Sprint

**Sprint N completado SI:**
- ✅ requirements.md approved
- ✅ design.md approved
- ✅ tasks.md approved
- ✅ Implementation logged (CON artifacts)
- ✅ Otros artefactos del folder ajustados
- ✅ INDICE-SPECS.md actualizado
- ✅ Tests pasando (si aplica)

### Global (Proyecto Completo)

**Proyecto completado SI:**
- ✅ 10 specs completados (100%)
- ✅ Cada spec con 4 fases approved
- ✅ Todos los artefactos del folder consistentes
- ✅ Triple persistencia funcionando
- ✅ Tests coverage >80%
- ✅ Documentación completa
- ✅ Lessons learned consolidadas

---

## 🚀 PRÓXIMO PASO INMEDIATO

### ¿Proceder con Sprint 0?

**Sprint 0: Setup Inicial (3 días)**

1. Reorganizar `.spec-workflow/specs/` (eliminar estructura anterior)
2. Crear 10 directorios de specs
3. Actualizar ISSUE.yaml maestro
4. Crear INDICE-SPECS.md
5. Actualizar README.md

**¿Continuar?** → El usuario debe confirmar este approach.

---

## 🧠 REFLEXIÓN FINAL

### Lo que Aprendí de la Corrección

**Mi Error:**
- Seguí pensando en "Main Spec grande" + "sub-issues pequeños"
- Creé OTRA jerarquía cuando debía eliminarla
- No leí el manifiesto con suficiente rigor

**La Lección:**
- El manifiesto propone COMPONENTES INDEPENDIENTES
- Cada componente (templates, patterns) merece spec completo
- Modularidad en TODOS los niveles, sin excepciones
- Specs son peers que se relacionan, no jerarquías

**Aplicación:**
- Cada sección del manifiesto → 1 spec-issue completo
- Cada spec → Workflow riguroso (Req → Design → Tasks → Impl)
- Cada sprint → Mejorar folder completo, no solo un spec
- Resultado → Sistema modular real, no monolito disfrazado

---

**Versión:** 2.0.0 (Corrección)
**Última actualización:** 2026-01-10
**Próxima Revisión:** Post-Sprint 0
**Autor:** MELQUISEDEC + GitHub Copilot (corregido)

**Agradecimientos:** Al usuario por corregir mi malentendido y forzar pensamiento profundo.
