# DAATH-ZEN Pattern: Refactoring

```yaml
---
id: "daath-zen-refactoring"
version: "1.0.0"
status: "validated"
confidence: 0.85
date: "2026-01-08"
validated_in_specs:
  - "monorepo-improvements-v1.1.0"
  - "demo-fix-references"
  - "nucleo-reorganization" # (hipotético, ejemplo)
applies_to_domains:
  - "code-structure"
  - "package-management"
  - "reference-fixing"
  - "monorepo-organization"
---
```

---

## Patrón: Refactoring de Código/Estructura

### Cuándo Usar Este Patrón

Usa este patrón cuando necesites:

- ✅ Reorganizar estructura de directorios/paquetes
- ✅ Fix broken references (imports, links, configs)
- ✅ Migrar código entre ubicaciones
- ✅ Consolidar módulos dispersos
- ✅ Aplicar nuevas convenciones de naming
- ✅ Eliminar código duplicado

**NO uses este patrón para**:
- ❌ Implementar nuevas features (usa `daath-zen-feature`)
- ❌ Investigación pura (usa `daath-zen-research`)
- ❌ Bugfixes puntuales (hotfix directo)

---

## Requirements Template

### User Stories (Estándar)

#### US-1: Análisis de Estado Actual
**As a** developer  
**I want** to understand the current structure and identify issues  
**So that** I can plan refactoring safely

**Acceptance Criteria**:
- All files are catalogued
- References are mapped (imports, links, configs)
- Impact analysis is complete
- Risk assessment documented

#### US-2: Restructuring
**As a** developer  
**I want** to move/rename files and packages  
**So that** the structure follows the new conventions

**Acceptance Criteria**:
- Files moved to new locations
- Naming conventions applied
- Directory structure reflects architecture
- Git history preserved

#### US-3: Reference Fixing
**As a** developer  
**I want** to update all references to moved/renamed entities  
**So that** nothing breaks

**Acceptance Criteria**:
- All imports updated
- All markdown links fixed
- All config paths updated
- Zero broken references

#### US-4: Validation
**As a** developer  
**I want** to verify the refactoring didn't break anything  
**So that** I can merge with confidence

**Acceptance Criteria**:
- All tests pass
- No broken imports
- No broken links
- Documentation updated

---

## Tasks Template

### Estructura de Tareas (6 tareas estándar)

```markdown
# Tasks

## 1. Refactoring: {Brief Description}

- [ ] 1.1. Analyze current structure and identify issues
  - File: Repository root
  - _Requirements: US-1_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, grep-search, sequential-thinking]_
  - _Lesson: lessons-learned/task-1.1-analysis.md_
  - _Prompt: Role: MELQUISEDEC Classifier | Task: Scan all files, catalog structure, identify broken references (Python imports, markdown links, config paths), classify by type and severity, generate impact report | Restrictions: Read-only operations, no modifications | Success: Complete catalogue with severity levels, impact analysis, risk assessment_

- [ ] 1.2. Plan restructuring strategy
  - File: .spec-workflow/specs/{spec-name}/design.md
  - _Requirements: US-2_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[sequential-thinking, filesystem]_
  - _Lesson: lessons-learned/task-1.2-planning.md_
  - _Prompt: Role: SALOMON Analyzer | Task: Based on analysis, design new structure, plan move operations, identify dependencies, determine order of operations to minimize breakage | Restrictions: Consider git history preservation, minimize disruption | Success: Detailed migration plan with ordered steps, dependency graph, rollback strategy_

- [ ] 1.3. Move/rename files and directories
  - File: {List of files to move}
  - _Requirements: US-2_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, git]_
  - _Lesson: lessons-learned/task-1.3-move-files.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Execute move operations using git mv to preserve history, follow plan order, create new directories as needed, verify each move | Restrictions: Use git mv, not plain mv; preserve commit history | Success: All files moved, directory structure matches design, git history intact_

- [ ] 1.4. Fix Python imports
  - File: **/*.py
  - _Requirements: US-3_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-refactoring, python-env, grep-search]_
  - _Lesson: lessons-learned/task-1.4-fix-imports.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Update all Python import statements to reflect new locations, use python-refactoring MCP to detect unused imports, run pytest after each batch to catch errors early | Restrictions: Test after each batch, preserve relative imports where appropriate | Success: All imports resolve, no unused imports, pytest passes_

- [ ] 1.5. Fix markdown links and documentation
  - File: **/*.md, README.md
  - _Requirements: US-3_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, grep-search, markitdown]_
  - _Lesson: lessons-learned/task-1.5-fix-links.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Update all markdown internal links, convert absolute to relative where needed, update anchor links, fix image paths | Restrictions: Use workspace-relative paths, preserve external links | Success: All internal links work, no 404s, link checker passes_

- [ ] 1.6. Validate refactoring and cleanup
  - File: Repository root
  - _Requirements: US-4_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env, git]_
  - _Lesson: lessons-learned/task-1.6-validation.md_
  - _Prompt: Role: ALMA Publisher | Task: Run full test suite, execute link checker, verify imports, check for orphaned files, generate validation report | Restrictions: Zero tolerance for failures | Success: All tests pass, no broken references, validation report clean_

- [ ] 1.7. Generate lessons-learned summary
  - File: .spec-workflow/specs/{spec-name}/lessons-learned/summary.yaml
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking]_
  - _Lesson: N/A_
  - _Prompt: Role: ALMA Publisher | Task: Aggregate all lessons from tasks 1.1-1.6, identify refactoring patterns, calculate confidence scores, update daath-zen-refactoring pattern | Restrictions: Only validated lessons (confidence >= 0.70) | Success: summary.yaml created, patterns documented, daath-zen-refactoring updated_
```

---

## Design Template Sections

### Debe Incluir

1. **Current Structure Diagram**
   - Árbol de directorios actual
   - Mapa de dependencias

2. **Target Structure Diagram**
   - Árbol de directorios objetivo
   - Nuevas convenciones

3. **Migration Plan**
   - Orden de operaciones
   - Dependency graph
   - Risk mitigation

4. **Rollback Strategy**
   - Cómo revertir si falla
   - Checkpoints de seguridad

5. **Validation Strategy**
   - Tests a ejecutar
   - Link checkers
   - Import validators

---

## MCPs por Rostro (Estándar)

### MELQUISEDEC (Análisis)
**Base**: `neo4j`, `memory`  
**Especializados**: `filesystem`, `grep-search`, `sequential-thinking`

**Tareas típicas**:
- Análisis de estructura actual
- Catalogación de archivos
- Clasificación de referencias

### SALOMON (Planificación)
**Base**: `neo4j`, `memory`  
**Especializados**: `sequential-thinking`, `filesystem`

**Tareas típicas**:
- Diseño de estrategia
- Análisis de dependencias
- Planificación de orden de operaciones

### MORPHEUS (Ejecución)
**Base**: `neo4j`, `memory`  
**Especializados**: `filesystem`, `python-refactoring`, `python-env`, `git`, `grep-search`, `markitdown`

**Tareas típicas**:
- Move/rename files
- Fix imports
- Fix links
- Restructuring

### ALMA (Validación y Publicación)
**Base**: `neo4j`, `memory`  
**Especializados**: `filesystem`, `python-env`, `git`

**Tareas típicas**:
- Validation
- Test execution
- Report generation
- Lessons aggregation

---

## Lessons Comunes

### Lesson Pattern 1: Classification is Critical
**Confidence**: 0.90  
**Context**: En task 1.1 (análisis), subestimar la clasificación lleva a romper importaciones críticas.

**Best Practice**:
> Antes de mover nada, clasifica TODAS las referencias por:
> 1. Tipo (import, link, config)
> 2. Severidad (critical, high, medium, low)
> 3. Owner (qué módulo las usa)

### Lesson Pattern 2: Batch + Test
**Confidence**: 0.85  
**Context**: Mover todos los archivos de una vez y luego arreglar imports genera caos.

**Best Practice**:
> Divide en batches lógicos (por package/módulo). Después de cada batch:
> 1. Fix imports del batch
> 2. Run tests del batch
> 3. Commit
> 4. Next batch

### Lesson Pattern 3: Git MV, Not Plain MV
**Confidence**: 0.95  
**Context**: Usar `mv` en lugar de `git mv` rompe el history.

**Best Practice**:
> **SIEMPRE** usa `git mv` para preservar history. Esto es crítico para:
> - Git blame
> - Tracking authorship
> - Rollback capabilities

### Lesson Pattern 4: Relative Paths > Absolute
**Confidence**: 0.80  
**Context**: Absolute paths rompen cuando el repo se clona en diferentes rutas.

**Best Practice**:
> En markdown y configs, prefiere:
> - `../../docs/file.md` (relative)
> - NO `/home/user/project/docs/file.md` (absolute)

---

## Checklist de Calidad

### Pre-Refactoring
- [ ] Análisis completo de referencias
- [ ] Impact analysis documentado
- [ ] Rollback strategy definida
- [ ] Tests baseline ejecutados (todos pasan)

### Durante Refactoring
- [ ] Usar `git mv` para moves
- [ ] Test after each batch
- [ ] Commit after each successful batch
- [ ] Document blockers immediately

### Post-Refactoring
- [ ] All tests pass
- [ ] No broken imports
- [ ] No broken links (link checker)
- [ ] Documentation updated
- [ ] Lessons extracted

---

## Métricas de Éxito

| Métrica | Target | Descripción |
|---------|--------|-------------|
| **Zero Breakage** | 100% | No broken imports/links |
| **Test Pass Rate** | 100% | All tests pass |
| **Coverage Maintained** | >= baseline | No reduction in coverage |
| **Time to Complete** | < 5 days | Full refactoring cycle |
| **Rollback Success** | 100% | Can rollback cleanly if needed |

---

## Variaciones del Patrón

### Variación 1: Small Refactoring (< 10 files)
- Skip task 1.2 (planning)
- Combine 1.3 + 1.4 (move + fix in one step)
- Reduce to 4 tasks total

### Variación 2: Large Refactoring (> 100 files)
- Add task 1.2.5: Create migration scripts
- Split 1.4 into 1.4a (batch 1), 1.4b (batch 2), etc.
- Add intermediate validation tasks

### Variación 3: Python-Only Refactoring
- Skip 1.5 (markdown links)
- Focus 1.4 on imports only
- Add 1.4.5: Update pyproject.toml/setup.py

---

## Ejemplo Completo

Ver specs que usan este patrón:
- [monorepo-improvements-v1.1.0](../../.spec-workflow/specs/monorepo-improvements-v1.1.0/)
- [demo-fix-references](../../.spec-workflow/specs/demo-fix-references/)

---

## Evolución del Patrón

| Version | Date | Changes | Confidence |
|---------|------|---------|------------|
| 0.1.0 | 2026-01-06 | Initial proposal | 0.60 |
| 0.5.0 | 2026-01-07 | After 2 specs validated | 0.75 |
| 1.0.0 | 2026-01-08 | After 3+ specs, production-ready | 0.85 |
| 1.1.0 | TBD | Add Python-specific refinements | - |

---

## Referencias

- [Best Practices](../../.spec-workflow/steering/best-practices.md)
- [MCPs Recomendados](../../docs/manifiesto/03-workflow/04-mcps-recomendados.md)
- [Lesson Template](../_daath-template/lessons/lesson-template.md)
