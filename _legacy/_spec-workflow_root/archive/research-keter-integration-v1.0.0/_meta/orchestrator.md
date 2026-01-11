---
id: "research-keter-integration-v1.0.0-orchestrator"
version: "1.0.0"
principles:
  DRY: "No duplicar contenido - solo referenciar tasks.md"
  SSoT: "Single Source of Truth - tasks.md es la fuente única"
  SeparationOfConcerns: "Orchestrator gestiona flujo, no implementación"
  Idempotencia: "Ejecutar múltiples veces = mismo resultado"
  OutputTriple: "Analysis + Guidelines + Lessons (DAATH-ZEN core)"
  MultiRepo: "Spec en melquisedec, análisis incluye bereshit (keter)"
owners: ["Architecture Team"]
rostros: ["MELQUISEDEC", "MORPHEUS", "SALOMON", "ALMA"]
required_mcps: ["neo4j", "memory", "filesystem", "sequential-thinking", "grep-search"]
multi_repo: true
affected_repos: ["aleia-melquisedec", "aleia-bereshit"]
---

# DAATH-ZEN Issue Orchestrator: research-keter-integration-v1.0.0

Orchestrator para spec de **análisis arquitectónico multi-repositorio**. Este spec no implementa código sino que **crea guidelines y decisiones** sobre dónde vive cada componente en el ecosistema DAATH-ZEN.

**Naturaleza**: Strategic + Analysis (no deployment)
**Multi-Repo**: Spec en melquisedec, análisis incluye bereshit (keter como caso de estudio)

---

## FASE 0: CONTEXTO MULTI-REPO

**Repositorios Involucrados**:
```
[REPO:aleia-melquisedec]  → Donde vive este spec y deliverables
[REPO:aleia-bereshit]     → Donde está keter (sujeto de análisis)
```

**Convención de Logs**:
- Usar tags `[REPO:nombre]` en Implementation Logs
- Referencias cruzadas deben ser explícitas
- Deliverables solo se crean en melquisedec

**Acceso a Bereshit**:
- Usuario debe proporcionar información de keter (estructura, requirements, README)
- No ejecutamos cambios en bereshit (fuera de scope)
- Análisis es read-only desde perspectiva de bereshit

---

## FASE 1: PREPARACIÓN

**Cargar Contexto (por referencia)**:
- 📖 **Tasks (fuente única)**: [../tasks.md](../tasks.md) - 13 tasks en 5 fases
- 📋 **Requirements**: [../requirements.md](../requirements.md) - 5 user stories
- 🎨 **Design**: [../design.md](../design.md) - Decision tree + ComponentClassifier
- 🎯 **Success Metrics**: 7 deliverables, decision tree, keter decision clara

**Validaciones Pre-ejecución**:
- Verificar acceso a C:\proyectos\aleia-bereshit\apps\keter (o alternativa)
- Confirmar MCPs activos: neo4j, memory, filesystem, sequential-thinking, grep-search
- Crear estructura de directorios

**Directorios a Crear**:
```
research-keter-integration-v1.0.0/
├── Implementation Logs/
│   ├── analysis/          (análisis de keter)
│   └── session-*.md       (logs por sesión)
├── lessons-learned/       (lessons por task)
└── artifacts/             (outputs auxiliares)
```

---

## FASE 2: WORKFLOW POR SPRINTS

Este spec usa un enfoque de **sprints temáticos** en lugar de loop secuencial:

### Sprint 1: Discovery & Analysis (Tasks 1.1-1.3 + META-1, META-2)

**Goal**: Obtener y analizar información de keter
**Duration**: ~2 horas
**Critical Path**: META-1 → TASK-1.1 → TASK-1.2 → TASK-1.3

**Secuencia**:
1. **META-1**: Crear estructura de carpetas (5 min)
2. **TASK-1.1**: Gather Keter Information (30 min)
   - Solicitar al usuario: tree structure, requirements.txt/pyproject.toml, README
   - Guardar en `Implementation Logs/analysis/keter-raw-data.md`
   - Tag: `[REPO:aleia-bereshit] - Read-only access`
3. **TASK-1.2**: Analyze Keter Structure (45 min)
   - Aplicar framework de análisis (ComponentMetadata)
   - Generar scorecard multidimensional
   - Output: `Implementation Logs/analysis/keter-evaluation.md`
4. **TASK-1.3**: Apply Decision Tree to Keter (30 min)
   - Ejecutar decision tree paso a paso
   - Generar recomendación con confidence score
   - Output: `Implementation Logs/analysis/keter-decision.md`
5. **META-2**: Create Spec README (15 min)
   - Punto de entrada al spec
   - Links a requirements/design/tasks

**Checkpoint**: ✅ Keter analizado, recomendación preliminar documentada

---

### Sprint 2: Architecture Documentation (Tasks 2.1-2.4)

**Goal**: Crear artefactos arquitectónicos reutilizables
**Duration**: ~2.5 horas
**Parallelizable**: Tasks 2.3 y 2.4 pueden hacerse después de 2.1

**Secuencia**:
1. **TASK-2.1**: Create ADR-002 Multi-Repo Strategy (1 hora) ⚡ CRITICAL
   - ADR completo con 5 secciones estándar
   - Basado en análisis de pensamiento complejo
   - Output: `docs/architecture/ADR-002-multi-repo-strategy.md`
   - Tag: `[REPO:aleia-melquisedec] - Create new ADR`
2. **TASK-2.2**: Create Component Placement Guidelines (1 hora)
   - Flowchart Mermaid del decision tree
   - Tabla de criterios y umbrales
   - 3 ejemplos aplicados (incluido keter)
   - FAQ con casos edge
   - Output: `docs/guides/component-placement-guidelines.md`
3. **TASK-2.3**: Create New Research Repo Template (1 hora)
   - Estructura completa con pyproject.toml, pre-commit, GitHub Actions
   - Output: `docs/guides/new-research-repo-template.md`
4. **TASK-2.4**: Create Multi-Repo Spec Workflow Guidelines (45 min)
   - Tracking conventions con tags `[REPO:...]`
   - 3 scenarios cubiertos
   - Output: `docs/guides/multi-repo-spec-workflow.md`

**Checkpoint**: ✅ 4 documentos guía creados y listos para uso futuro

---

### Sprint 3: Repository Cleanup (Tasks 3.1-3.2, 4.3)

**Goal**: Actualizar melquisedec con nuevas guidelines
**Duration**: ~1.5 horas
**Dependency**: Requiere TASK-2.1 completado

**Secuencia**:
1. **TASK-3.1**: Clarify apps/ Purpose in Melquisedec (30 min)
   - Decisión: Opción A (rename), B (keep + README), o C (remove)
   - Recomendación: Opción B (menor impacto)
   - Si rename: ejecutar `git mv apps/ examples/`
   - Actualizar README en la carpeta
2. **TASK-3.2**: Update ARQUITECTURA_MONOREPO.md (30 min)
   - Nueva sección: "Multi-Repository Strategy"
   - Referencia a ADR-002
   - Diagrama actualizado con repos externos
   - Output: Updated `docs/architecture/arquitectura-monorepo.md`
3. **TASK-4.3**: Update CONTRIBUTING.md (20 min)
   - Nueva sección "Where to Contribute"
   - Link a component placement guidelines
   - Output: Updated `CONTRIBUTING.md`

**Checkpoint**: ✅ Repo melquisedec actualizado con nueva arquitectura documentada

---

### Sprint 4: Decision & Finalization (Tasks 4.1-4.2, 5.1-5.3)

**Goal**: Decisión final sobre keter y cierre del spec
**Duration**: ~1.5 horas

**Secuencia**:
1. **TASK-4.1**: Document Keter Final Decision (30 min) ⚡ CRITICAL + User Approval
   - Decisión: A (mantener app), B (package), C (repo independiente), D (toolkit)
   - Rationale documentado
   - Action items específicos
   - Review date si procede
   - Output: `Implementation Logs/analysis/keter-decision.md` (actualizado)
   - **Requiere aprobación del usuario**
2. **TASK-4.2**: Create Implementation Roadmap (30 min) - Optional
   - Solo si decisión es B, C, o D
   - Fases: restructure → tests → package → publish
   - Nota: "Detailed implementation = future spec"
   - Output: `Implementation Logs/analysis/keter-implementation-roadmap.md`
3. **TASK-5.1**: Self-Validate Spec Multi-Repo Compliance (15 min)
   - Verificar tags `[MULTI-REPO: melquisedec, bereshit]`
   - Logs con convención `[REPO:...]`
   - Output: `Implementation Logs/validation-checklist.md`
4. **TASK-5.2**: Generate Summary & Changelog (20 min)
   - Executive summary en spec README
   - Entry en `CHANGELOG.md`
   - Links a deliverables
5. **TASK-5.3**: Create Spec Completion Report (15 min)
   - Todos los REQ-X validados
   - Deliverables checklist
   - Success criteria evaluados
   - Lessons learned capturados
   - Output: `Implementation Logs/completion-report.md`

**Checkpoint**: ✅ Spec completo, decisión tomada, métricas validadas

---

## FASE 3: IMPLEMENTATION-LOGS

**Registrar por Sesión**:
```markdown
# Implementation Log: Session 01 - Discovery
**Date**: 2026-01-XX
**Sprint**: 1 (Discovery & Analysis)
**Tasks Completed**: META-1, TASK-1.1, TASK-1.2, TASK-1.3

## Summary
- [REPO:aleia-bereshit] Obtained keter structure via user-provided tree output
- Analyzed keter using ComponentMetadata framework
- Applied decision tree: Recommendation = [A/B/C/D]

## Files Created
- Implementation Logs/analysis/keter-raw-data.md
- Implementation Logs/analysis/keter-evaluation.md
- Implementation Logs/analysis/keter-decision.md

## Key Insights
- Keter maturity level: [Alpha/Beta/Stable]
- Reusability score: [0.0-1.0]
- Recommendation confidence: [0.0-1.0]

## Next Steps
- Sprint 2: Create architecture documents (ADR-002, guidelines)
```

**Convención Multi-Repo**:
- Usar `[REPO:nombre]` al inicio de cada acción que involucra repo externo
- Ejemplo: `[REPO:aleia-bereshit] - Read keter structure (read-only)`
- Ejemplo: `[REPO:aleia-melquisedec] - Created ADR-002`

---

## FASE 4: LECCIONES-APRENDIDAS

**Crear Lesson per Task** (no META tasks):
```markdown
# Lesson: TASK-1.2 - Analyze Keter Structure

**Confidence**: 0.85
**Tags**: [component-analysis, multi-repo, decision-tree]

## ✅ What Worked
- ComponentMetadata framework proporcionó estructura clara
- Scorecard multidimensional facilitó comparación objetiva

## ❌ What Didn't Work
- Análisis sin acceso directo al código requirió más iteraciones
- Dependencias externas no pudieron verificarse automáticamente

## 💡 Key Insights
- Análisis estructural puede hacerse con información parcial si se documenta
- Decision tree necesita umbrales configurables por contexto

## 🔄 Recommendations
- Crear script de análisis automatizado para futuros casos
- Definir threshold matrix en guidelines

## 📊 Cypher (Neo4j)
```cypher
CREATE (l:Lesson {
  task_id: "1.2",
  spec: "research-keter-integration-v1.0.0",
  confidence: 0.85,
  tags: ["component-analysis", "multi-repo", "decision-tree"],
  timestamp: datetime()
})
MERGE (s:Spec {name: "research-keter-integration-v1.0.0", type: "strategic-analysis"})
MERGE (s)-[:HAS_LESSON]->(l)

MERGE (r:Repository {name: "aleia-bereshit"})
MERGE (l)-[:ANALYZED_COMPONENT_FROM]->(r)
```
```

Archivo: `lessons-learned/task-1.2-analyze-keter.md`

**Agregación Final**: No hay task explícita, pero generar `lessons-learned/summary.yaml` al final:
```yaml
spec: research-keter-integration-v1.0.0
type: strategic-analysis
multi_repo: true
lessons_count: 11  # Excluyendo META tasks
avg_confidence: 0.82
key_patterns:
  - Multi-repo analysis without direct code access
  - Decision tree application to real-world components
  - Guidelines creation from specific case study
reusable_artifacts:
  - Component placement decision tree
  - ADR template for multi-repo strategies
  - Multi-repo spec workflow conventions
```

---

## FASE 5: PERSISTENCIA (NO APLICA DEPLOYMENT)

⚠️ **Importante**: Este spec es **análisis y documentación**, no deployment de código.

**Estrategia de Persistencia**:

### Opción 1: Manual Git Commit (Recomendado para specs analíticos)
```powershell
# Después de completar todos los sprints
git add .spec-workflow/specs/research-keter-integration-v1.0.0/
git add docs/architecture/ADR-002-multi-repo-strategy.md
git add docs/guides/component-placement-guidelines.md
git add docs/guides/new-research-repo-template.md
git add docs/guides/multi-repo-spec-workflow.md
git add docs/architecture/arquitectura-monorepo.md
git add CONTRIBUTING.md
git add CHANGELOG.md

git commit -m "spec: complete research-keter-integration-v1.0.0

- Created ADR-002 for multi-repo architecture strategy
- Added component placement guidelines with decision tree
- Documented new research repo template
- Clarified apps/ purpose in monorepo
- Analyzed keter: [Decision here]
- Updated ARQUITECTURA_MONOREPO.md and CONTRIBUTING.md

Refs: #[issue-number] (if tracked)
Tags: [MULTI-REPO: melquisedec, bereshit]"

git push origin main
```

### Opción 2: Usar git-push-workflow (Si hay .gitpush.yml)
```yaml
# .spec-workflow/specs/research-keter-integration-v1.0.0/_meta/.gitpush.yml
stages:
  pre_commit: false
  tests: false
  branch_validate: false
  commit: true
  push: true
files:
  - ".spec-workflow/specs/research-keter-integration-v1.0.0/**"
  - "docs/architecture/ADR-002-multi-repo-strategy.md"
  - "docs/guides/component-placement-guidelines.md"
  - "docs/guides/new-research-repo-template.md"
  - "docs/guides/multi-repo-spec-workflow.md"
  - "docs/architecture/arquitectura-monorepo.md"
  - "CONTRIBUTING.md"
  - "CHANGELOG.md"
branch: main
allow_branch_push: false
non_interactive: true
commit_message: "spec: complete research-keter-integration-v1.0.0 (analysis + guidelines)"
dry_run: false
failure_mode: fail_fast
```

```bash
python tools/git/push_workflow.py --config .spec-workflow/specs/research-keter-integration-v1.0.0/_meta/.gitpush.yml --non-interactive
```

**Neo4j Nodes**:
```bash
# Después de push exitoso, ejecutar cypher desde lessons
cat lessons-learned/task-*.md | grep -A 30 "## 📊 Cypher" | neo4j-shell
```

**Archive Spec** (Post-completion):
```bash
# Crear tag
git tag -a research-keter-v1.0.0 -m "Multi-repo architecture strategy completed"
git push origin research-keter-v1.0.0

# Archive (opcional, si se considera cerrado permanentemente)
# mv .spec-workflow/specs/research-keter-integration-v1.0.0 \
#    .spec-workflow/archive/specs/research-keter-integration-v1.0.0
```

---

## FASE 6: POST-SPEC ACTIONS

### Si Keter Decision = B (Convert to Package)
- Crear nuevo spec: `keter-to-package-v1.0.0`
- Scope: Restructure, add tests, create pyproject.toml, publish to PyPI

### Si Keter Decision = C (Independent Repo)
- Crear nuevo repo: `aleia-keter`
- Aplicar new-research-repo-template.md
- Migrar código de bereshit

### Si Keter Decision = D (Integrate into Toolkit)
- Crear issue en melquisedec: "Integrate keter functionality into daath-toolkit"
- Scope: Extract reusable parts, add to toolkit packages

### Independientemente de la Decisión
- **Socializar guidelines**: Compartir ADR-002 y placement guidelines con equipo
- **Review en 3 meses**: Evaluar si las decisiones fueron correctas
- **Aplicar a otros casos**: Usar decision tree para evaluar otros componentes

---

## 📊 Success Criteria (Validación Final)

Antes de marcar el spec como completo, verificar:

- ✅ **7 deliverables creados**:
  1. ADR-002: Multi-Repository Architecture Strategy
  2. Component Placement Guidelines
  3. New Research Repo Template
  4. Multi-Repo Spec Workflow Guidelines
  5. Keter Evaluation
  6. Keter Decision
  7. Implementation Roadmap (if applicable)

- ✅ **Decision tree aplicable**: Puede usarse para casos futuros sin ambigüedad
- ✅ **Keter decision clara**: Opción A/B/C/D seleccionada con rationale
- ✅ **0 ambiguity sobre placement**: Criterios documentados y ejemplificados
- ✅ **Spec self-compliant**: Usa sus propias guidelines multi-repo
- ✅ **11 lessons captured**: Uno por task (excluyendo META)
- ✅ **CHANGELOG.md updated**: Entry con fecha y links

---

## 📚 Referencias

- **Tasks (fuente única)**: [../tasks.md](../tasks.md)
- **Requirements**: [../requirements.md](../requirements.md)
- **Design**: [../design.md](../design.md)
- **Dependency Graph**: Ver tasks.md sección "Dependency Graph"
- **Multi-Repo Context**: Este spec se gestiona en melquisedec pero analiza código en bereshit

---

## 🎯 Quick Start

**Comando para Usuario** (obtener info de keter):
```powershell
# Cambiar a directorio de keter
cd C:\proyectos\aleia-bereshit\apps\keter

# Obtener estructura
tree /F > keter-structure.txt
Get-Content keter-structure.txt

# Obtener dependencies
Get-Content requirements.txt
# O si usa pyproject.toml
Get-Content pyproject.toml

# Obtener descripción
Get-Content README.md
```

**Primera Tarea**: META-1 (crear estructura) + TASK-1.1 (solicitar info de keter al usuario)

---

_Orchestrator multi-repo: 350 líneas de claridad arquitectónica. Analysis-first, guidelines-driven, decision-focused._
