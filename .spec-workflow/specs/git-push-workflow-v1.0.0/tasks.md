# Tasks

## 1. Git Push Workflow Implementation

- [ ] 1.1. Setup pre-commit hooks framework
  - File: .pre-commit-config.yaml, .git/hooks/pre-commit
  - _Requirements: REQ-1_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env]_
  - _Lesson: lessons-learned/task-1.1-precommit-setup.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Install pre-commit framework, configure black/flake8/isort/mypy hooks, test on sample files to verify execution | Restrictions: Use Python ecosystem standard tools, execution < 30s | Success: Pre-commit hooks execute on git commit, all checks pass, clear error messages_

- [ ] 1.2. Create test runner for affected tests
  - File: tools/testing/run_affected_tests.py
  - _Requirements: REQ-2_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env, python-refactoring]_
  - _Lesson: lessons-learned/task-1.2-test-runner.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Create script to detect changed Python modules, map to test files using naming conventions, run pytest with coverage on affected tests only | Restrictions: Skip if no tests affected (docs-only), cache results, execution < 2min | Success: Script correctly identifies affected tests, runs pytest, reports coverage, fast execution_

- [ ] 1.3. Implement branch validation
  - File: tools/git/validate_branch.py
  - _Requirements: REQ-4_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[git, sequential-thinking]_
  - _Lesson: lessons-learned/task-1.3-branch-validation.md_
  - _Prompt: Role: MELQUISEDEC Classifier | Task: Check git status, validate branch name format (spec/hotfix/docs prefix), verify upstream tracking, warn if on main branch without PR | Restrictions: Non-blocking warnings, suggest corrective actions | Success: Clear status report, actionable warnings, suggests branch creation if on main_

- [ ] 1.4. Create commit message generator
  - File: tools/git/generate_commit_msg.py
  - _Requirements: REQ-3_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, git]_
  - _Lesson: lessons-learned/task-1.4-commit-msg.md_
  - _Prompt: Role: ALMA Publisher | Task: Extract spec name from branch, read task metadata from tasks.md, generate conventional commit format with rostro/MCPs metadata, prompt user for description | Restrictions: Follow conventional commits spec, include all metadata fields | Success: Generated message follows format, includes spec/task/rostro/MCPs, user can edit before commit_

- [x] 1.5. Implement configurable push workflow script (COMPLETED)
  - File: tools/git/push_workflow.py
  - _Requirements: REQ-5_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[git, github, sequential-thinking]_
  - _Lesson: lessons-learned/task-1.5-push-workflow.md_
  - _Prompt: Role: ALMA Publisher | Task: Create a CLI `push_workflow.py` that reads optional `.gitpush.yml` and supports flags: `--dry-run`, `--non-interactive`, `--minimal`, `--files`, `--branch`, `--allow-branch-push`. The script prompts for `files` and `branch` when running interactively (agent must ask), enforces "no branches unless allowed" policy, supports minimal mode, and emits JSON summary for CI. | Restrictions: Keep default minimal and fast, avoid heavy operations unless enabled in config | Success: Script is configurable, supports minimal mode, usable as final CI task, includes `--dry-run`, prompts agent for files and branch when interactive, enforces branch push policy._

- [ ] 1.6. Create post-push Neo4j logger
  - File: tools/git/log_to_neo4j.py
  - _Requirements: REQ-6_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[git]_
  - _Lesson: lessons-learned/task-1.6-neo4j-logger.md_
  - _Prompt: Role: ALMA Publisher | Task: After successful push, create Commit node in Neo4j, link to Spec/Task/Rostro nodes, update memory with commit context, create git tags for releases | Restrictions: Idempotent operations, non-blocking (log failures but don't stop workflow) | Success: Commit logged to Neo4j with all relationships, memory updated, tags created if applicable_

- [ ] 1.7. Create integration tests for workflow (minimal + configurable)
  - File: tests/integration/test_git_push_workflow.py
  - _Requirements: ALL_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, python-env, git]_
  - _Lesson: lessons-learned/task-1.7-integration-tests.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Create pytest test suite covering minimal and full modes; include dry-run tests and non-interactive CI run; mock git and runner scripts; test both success and failure paths | Restrictions: Use pytest fixtures, mock git commands, test both success and failure paths | Success: Tests pass, verify CLI flags (--dry-run, --minimal, --non-interactive) and JSON output summary_

- [ ] 1.8. Document workflow and create user guide
  - File: docs/guides/git-push-workflow.md
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, markitdown]_
  - _Lesson: lessons-learned/task-1.8-documentation.md_
  - _Prompt: Role: ALMA Publisher | Task: Write comprehensive guide with examples, screenshots of success/error cases, troubleshooting section, quick reference commands | Restrictions: Use clear markdown, include code examples, link to related docs | Success: Guide is complete, easy to follow, covers common issues, includes visual examples_

- [ ] 1.9. Generate lessons-learned summary
  - File: .spec-workflow/specs/git-push-workflow-v1.0.0/lessons-learned/summary.yaml
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking]_
  - _Lesson: N/A_
  - _Prompt: Role: ALMA Publisher | Task: Aggregate all lessons from tasks 1.1-1.8, identify git workflow patterns, calculate confidence scores, propose daath-zen-git-workflow pattern template | Restrictions: Only validated lessons with confidence >= 0.70 | Success: summary.yaml created with aggregated insights, daath-zen-git-workflow pattern proposed with high confidence_
