# Tasks

## 1. Python Import Analysis

- [ ] 1.1. Scan DAATH imports in Python files
  - File: packages/keter/**/*.py
  - _Requirements: REQ-1_
  - _Phase: 02-BUILD_
  - _Prompt: Grep all `from daath` and `import daath` statements in packages/keter, document each import with file path and line number, classify by module (kg, utils, models)_

- [ ] 1.2. Scan YESOD imports for schema dependencies
  - File: packages/keter/**/*.py
  - _Requirements: REQ-1, REQ-3_
  - _Phase: 02-BUILD_
  - _Prompt: Grep all `from yesod` imports, identify schema dependencies, map to Supabase tables_

- [ ] 1.3. Scan AYIN imports for configuration patterns
  - File: packages/keter/**/*.py, .env*
  - _Requirements: REQ-1, REQ-2_
  - _Phase: 02-BUILD_
  - _Prompt: Grep all `from ayin` imports, identify configuration access patterns, document environment variables used_

## 2. Configuration Analysis

- [ ] 2.1. Environment variables audit
  - File: .env, .env.example, config/*.py
  - _Requirements: REQ-2_
  - _Phase: 02-BUILD_
  - _Prompt: List all env vars in .env files, identify hardcoded paths, map to AYIN config modules_

- [ ] 2.2. Supabase schema mapping
  - File: supabase/migrations/*.sql
  - _Requirements: REQ-3_
  - _Phase: 02-BUILD_
  - _Prompt: Document all 4 schemas (keter, templates, audit, public), list tables per schema, identify cross-schema references_

## 3. Template Analysis

- [ ] 3.1. Template path audit
  - File: packages/keter/templates/**/*
  - _Requirements: REQ-4_
  - _Phase: 02-BUILD_
  - _Prompt: List all 87 L0 templates, identify absolute vs relative paths, document template loader configuration_

## 4. Visualization

- [ ] 4.1. Generate dependency graph
  - File: 01-design/architecture/dependency-graph.mermaid
  - _Requirements: REQ-5_
  - _Phase: 03-EVALUATE_
  - _Prompt: Create Mermaid diagram of all dependencies, identify circular dependencies, highlight critical paths_
