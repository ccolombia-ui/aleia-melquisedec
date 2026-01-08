# Tasks

## 1. Mejoras de Estructura del Monorepo

- [x] 1.1. Fix all nucleo-investigacion references
  - File: *.md, *.py, docker-compose.yml
  - _Requirements: REQ-1_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking, grep-search]_
  - _Lesson: lessons-learned/task-1.1-fix-references.md_
  - _Prompt: Role: MELQUISEDEC Classifier | Task: Scan all files for 'nucleo-investigacion' references, classify by type (Python import, markdown link, Docker config), prioritize by impact | Restrictions: Don't break working imports, preserve git history | Success: All 23 references updated, no broken imports, validation passed_

- [x] 1.2. Move root documentation files to docs/
  - File: QUICK_REFERENCE.md, ESTRUCTURA_VISUAL.md, REORGANIZACION_COMPLETA.md
  - _Requirements: REQ-2_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, grep-search]_
  - _Lesson: lessons-learned/task-1.2-move-docs.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Move 3 root docs to docs/ preserving structure, update all internal relative links, verify no broken references | Restrictions: Maintain link integrity, update SUMMARY.md if exists | Success: Files moved, all links working, no 404s_

- [x] 1.3. Add pre-commit hooks
  - File: .pre-commit-config.yaml, package.json
  - _Requirements: REQ-3_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env]_
  - _Lesson: lessons-learned/task-1.3-precommit.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Configure pre-commit hooks for black, flake8, isort, mypy; add to package.json scripts | Restrictions: Use standard tools from Python ecosystem | Success: Hooks execute on commit, formatted correctly_

- [x] 1.4. Package discovery mechanism
  - File: packages/*/pyproject.toml, scripts/discover-packages.py
  - _Requirements: REQ-4_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-refactoring, sequential-thinking]_
  - _Lesson: lessons-learned/task-1.4-package-discovery.md_
  - _Prompt: Role: SALOMON Analyzer | Task: Create script to auto-discover packages by scanning pyproject.toml, support both pip and poetry, generate dependency graph | Restrictions: Support pip and poetry formats | Success: New packages auto-detected, graph generated_

- [~] 1.5. Add unit tests for validators **[DESCONTINUADO]**
  - File: packages/daath-toolkit/testing/*.py
  - _Requirements: REQ-5_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-refactoring, python-env]_
  - _Lesson: N/A - Descontinuado_
  - _Motivo: Esta tarea se resolverá como parte de la investigación de KETER (research-keter-integration-v1.0.0). El enfoque de testing será rediseñado desde la perspectiva de integración con KETER._
  - _Prompt: Role: MORPHEUS Designer | Task: Create pytest test suite for validators in daath-toolkit, aim for 80% coverage, use fixtures, mock external dependencies | Restrictions: 80% coverage minimum, follow pytest best practices | Success: Tests pass, coverage >= 80%, CI integration ready_

- [x] 1.6. Create cleanup post-reorganization script
  - File: tools/maintenance/cleanup_post_reorganization.py
  - _Requirements: REQ-6_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking, grep-search]_
  - _Lesson: lessons-learned/task-1.6-cleanup-script.md_
  - _Prompt: Role: MELQUISEDEC Classifier | Task: Script to identify orphaned files, broken symlinks, unused imports; classify by severity; dry-run by default | Restrictions: Dry-run by default, no destructive operations without --force | Success: Script identifies all issues, generates report with severity levels_

- [x] 1.7. Generate lessons-learned summary
  - File: .spec-workflow/specs/monorepo-improvements-v1.1.0/lessons-learned/summary.yaml
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: lessons-learned/summary.yaml (self-documenting)_
  - _Prompt: Role: ALMA Publisher | Task: Aggregate all lessons from tasks 1.1-1.6, extract patterns, calculate confidence scores, identify reusable patterns for future specs | Restrictions: Only include validated lessons | Success: summary.yaml created with aggregated insights, patterns documented_
  - _Nota: Task 1.5 marcada como descontinuada en summary (moved to Keter investigation)_
