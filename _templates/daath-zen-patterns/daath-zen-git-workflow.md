# DAATH-ZEN Pattern: Git Workflow

```yaml
---
id: "daath-zen-git-workflow"
version: "1.0.0"
status: "validated"
confidence: 0.88
date: "2026-01-08"
validated_in_specs:
  - "git-push-workflow-v1.0.0"
applies_to_domains:
  - "git-operations"
  - "ci-cd"
  - "deployment"
  - "version-control"
---
```

---

## Patrón: Git Workflow Automation

### Cuándo Usar Este Patrón

Usa este patrón cuando necesites:

- ✅ Automatizar push workflows
- ✅ Crear PR workflows
- ✅ Gestionar releases
- ✅ Implementar branch strategies
- ✅ Pre-commit/pre-push validation
- ✅ Git hooks management

**NO uses este patrón para**:
- ❌ Code refactoring (usa `daath-zen-refactoring`)
- ❌ Feature implementation (usa `daath-zen-feature`)
- ❌ Solo git commands (hotfix directo)

---

## Requirements Template

### User Stories (Estándar)

#### US-1: Pre-Push Validation
**As a** developer  
**I want** automated validation before pushing  
**So that** I ensure code quality and prevent broken commits

**Acceptance Criteria**:
- Linters run automatically
- Tests execute on affected files
- Clear error messages
- Fast feedback (< 3min)

#### US-2: Structured Commits
**As a** team member  
**I want** consistent commit format  
**So that** we can track changes and generate changelogs

**Acceptance Criteria**:
- Conventional commits format
- Includes spec/task metadata
- Includes rostro/MCPs info
- Easy to parse

#### US-3: Branch Protection
**As a** maintainer  
**I want** branch validation  
**So that** we prevent accidental pushes to protected branches

**Acceptance Criteria**:
- Warns on main push
- Validates branch naming
- Checks upstream tracking
- Suggests corrections

#### US-4: Push Execution
**As a** developer  
**I want** reliable push with error handling  
**So that** conflicts are resolved cleanly

**Acceptance Criteria**:
- Handles auth errors
- Detects conflicts
- Provides retry suggestions
- Logs to Neo4j

---

## Tasks Template

### Estructura de Tareas (8-9 tareas estándar)

```markdown
# Tasks

## 1. {Git Workflow Type} Implementation

- [ ] 1.1. Setup pre-commit/pre-push hooks
  - File: .git/hooks/, .pre-commit-config.yaml
  - _Requirements: US-1_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env, git]_
  - _Lesson: lessons-learned/task-1.1-hooks-setup.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Install pre-commit framework, configure linters (black, flake8, isort, mypy), test execution, ensure < 30s runtime | Restrictions: Use Python ecosystem tools, fast-fail on errors | Success: Hooks execute, all checks pass, clear errors_

- [ ] 1.2. Create test runner
  - File: tools/testing/run_affected_tests.py
  - _Requirements: US-1_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env, python-refactoring]_
  - _Lesson: lessons-learned/task-1.2-test-runner.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Detect changed modules, map to tests, run pytest with coverage on affected only | Restrictions: Skip if docs-only, cache results, < 2min | Success: Correct test detection, pytest runs, coverage reported_

- [ ] 1.3. Implement branch validation
  - File: tools/git/validate_branch.py
  - _Requirements: US-3_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[git, sequential-thinking]_
  - _Lesson: lessons-learned/task-1.3-branch-validation.md_
  - _Prompt: Role: MELQUISEDEC Classifier | Task: Check git status, validate branch name format, verify upstream, warn on main | Restrictions: Non-blocking warnings, actionable suggestions | Success: Clear status, helpful warnings, suggests fixes_

- [ ] 1.4. Create commit message generator/validator
  - File: tools/git/commit_msg_generator.py
  - _Requirements: US-2_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, git]_
  - _Lesson: lessons-learned/task-1.4-commit-msg.md_
  - _Prompt: Role: ALMA Publisher | Task: Extract spec from branch, read task metadata, generate conventional format with rostro/MCPs, allow user edit | Restrictions: Follow conventional commits, include all metadata | Success: Proper format, all metadata, user-editable_

- [ ] 1.5. Implement main workflow script
  - File: tools/git/{workflow_name}.py
  - _Requirements: US-1, US-4_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[git, github, sequential-thinking]_
  - _Lesson: lessons-learned/task-1.5-workflow-script.md_
  - _Prompt: Role: ALMA Publisher | Task: Orchestrate full workflow (pre-commit, tests, branch validate, commit, push), handle errors, support --dry-run | Restrictions: Clear progress, rollback on critical failures | Success: All stages execute, push succeeds, errors handled gracefully_

- [ ] 1.6. Create post-push actions
  - File: tools/git/post_push_actions.py
  - _Requirements: US-4_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[git, github]_
  - _Lesson: lessons-learned/task-1.6-post-push.md_
  - _Prompt: Role: ALMA Publisher | Task: After push, log commit to Neo4j, create git tags if release, update memory context | Restrictions: Idempotent, non-blocking (log failures don't stop workflow) | Success: Commit logged with relationships, tags created, memory updated_

- [ ] 1.7. Create integration tests
  - File: tests/integration/test_{workflow_name}.py
  - _Requirements: ALL_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env, git]_
  - _Lesson: lessons-learned/task-1.7-integration-tests.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Pytest suite simulating full workflow with mock git, test error scenarios, verify Neo4j logging | Restrictions: Use fixtures, mock git commands, test success and failures | Success: Tests pass, all stages covered, error scenarios handled_

- [ ] 1.8. Document workflow
  - File: docs/guides/{workflow_name}.md
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, markitdown]_
  - _Lesson: lessons-learned/task-1.8-documentation.md_
  - _Prompt: Role: ALMA Publisher | Task: Write comprehensive guide with examples, error screenshots, troubleshooting, quick reference | Restrictions: Clear markdown, code examples, visual aids | Success: Complete guide, easy to follow, covers issues_

- [ ] 1.9. Generate lessons-learned summary
  - File: .spec-workflow/specs/{spec-name}/lessons-learned/summary.yaml
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking]_
  - _Lesson: N/A_
  - _Prompt: Role: ALMA Publisher | Task: Aggregate lessons from tasks 1.1-1.8, identify git workflow patterns, calculate confidence, update daath-zen-git-workflow | Restrictions: Only validated lessons (>= 0.70 confidence) | Success: summary.yaml created, patterns documented, pattern updated_
```

---

## Design Template Sections

### Debe Incluir

1. **Workflow Diagram**
   - Stages del workflow
   - Decision points
   - Error handling paths

2. **Component Design**
   - Scripts y su responsabilidad
   - MCPs usados por componente
   - Interfaces entre componentes

3. **Error Handling**
   - Tipos de errores
   - Recovery strategies
   - User guidance

4. **Configuration**
   - .pre-commit-config.yaml
   - pyproject.toml (pytest)
   - Git hooks scripts

5. **Performance**
   - Time budgets por stage
   - Optimization strategies
   - Caching mechanisms

---

## MCPs por Rostro (Estándar)

### MELQUISEDEC (Branch Validation)
**Base**: `neo4j`, `memory`  
**Especializados**: `git`, `sequential-thinking`

**Tareas típicas**:
- Branch validation
- Status checks
- Classification of changes

### MORPHEUS (Pre-commit, Testing)
**Base**: `neo4j`, `memory`  
**Especializados**: `filesystem`, `python-env`, `python-refactoring`, `git`

**Tareas típicas**:
- Hook setup
- Test runner creation
- Integration testing

### ALMA (Commit, Push, Post-Push)
**Base**: `neo4j`, `memory`  
**Especializados**: `filesystem`, `git`, `github`, `sequential-thinking`

**Tareas típicas**:
- Commit message generation
- Push execution
- Post-push logging
- Documentation

---

## Lessons Comunes

### Lesson Pattern 1: Fast Feedback is Critical
**Confidence**: 0.90  
**Context**: Pre-commit hooks que tardan >1min frustran developers y se deshabilitan.

**Best Practice**:
> Mantén pre-commit < 30s:
> 1. Run linters en paralelo
> 2. Cache resultados
> 3. Solo check archivos staged
> 4. Skip tests en pre-commit (déjalos para pre-push)

### Lesson Pattern 2: Clear Error Messages
**Confidence**: 0.85  
**Context**: Errores crípticos como "push failed" no ayudan.

**Best Practice**:
> Cada error debe incluir:
> 1. **Qué falló** (específico)
> 2. **Por qué falló** (causa raíz)
> 3. **Cómo arreglarlo** (comando exacto)
> Ejemplo: "❌ Push failed: No upstream branch. Run: `git push -u origin main`"

### Lesson Pattern 3: Dry-Run Mode
**Confidence**: 0.88  
**Context**: Developers tienen miedo de romper cosas, no ejecutan workflows.

**Best Practice**:
> **SIEMPRE** incluye `--dry-run` flag que:
> 1. Simula operaciones
> 2. Muestra lo que haría
> 3. No ejecuta git commands destructivos
> Genera confianza y permite testing seguro.

### Lesson Pattern 4: Metadata in Commits
**Confidence**: 0.92  
**Context**: Sin metadata, imposible rastrear qué rostro/MCP produjo cambios.

**Best Practice**:
> Formato de commit:
> ```
> type(spec): task-id description
> 
> Spec: name-vX.Y.Z
> Task: X.Y
> Rostro: NAME
> MCPs: list
> Lesson: file or N/A
> ```
> Esto permite:
> - Trazabilidad en Neo4j
> - Changelog automático
> - Análisis de efectividad por rostro

---

## Checklist de Calidad

### Pre-Implementation
- [ ] Workflow diagram completo
- [ ] Error scenarios identificados
- [ ] Performance budgets definidos
- [ ] MCPs listados por stage

### Durante Implementation
- [ ] Cada stage < time budget
- [ ] Errors con actionable messages
- [ ] --dry-run implementado
- [ ] Tests cubriendo happy + error paths

### Post-Implementation
- [ ] Integration tests pass
- [ ] Documentation completa
- [ ] Users pueden ejecutar workflow
- [ ] Lessons extracted con alta confianza

---

## Métricas de Éxito

| Métrica | Target | Descripción |
|---------|--------|-------------|
| **Pre-commit Time** | < 30s | Tiempo de hooks |
| **Test Time** | < 2min | Tiempo de tests afectados |
| **Total Workflow** | < 3min | Pre-commit + test + push |
| **Error Rate** | < 5% | % de workflows fallidos |
| **User Adoption** | > 90% | % devs usando workflow |

---

## Variaciones del Patrón

### Variación 1: Simple Push (sin PR)
- Tasks: 5 (skip PR creation)
- Focus: commit + push + log

### Variación 2: PR Workflow
- Tasks: 10+ (add PR creation, review request)
- Focus: commit + push + create PR + request reviews

### Variación 3: Release Workflow
- Tasks: 12+ (add versioning, changelog, tagging)
- Focus: commit + push + version bump + tag + publish

---

## Ejemplo Completo

Ver spec que usa este patrón:
- [git-push-workflow-v1.0.0](../../.spec-workflow/specs/git-push-workflow-v1.0.0/)

---

## Evolución del Patrón

| Version | Date | Changes | Confidence |
|---------|------|---------|------------|
| 0.1.0 | 2026-01-08 | Initial proposal from git-push spec | 0.75 |
| 1.0.0 | 2026-01-08 | Validated, production-ready | 0.88 |
| 1.1.0 | TBD | Add PR workflow variant | - |
| 1.2.0 | TBD | Add release workflow variant | - |

---

## Referencias

- [Best Practices](../../.spec-workflow/_meta/best-practices.md)
- [MCPs Recomendados](../../docs/manifiesto/03-workflow/04-mcps-recomendados.md)
- [Git Push Workflow Spec](../../.spec-workflow/specs/git-push-workflow-v1.0.0/)
