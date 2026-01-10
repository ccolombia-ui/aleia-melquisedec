# Dependency Audit Requirements

## Overview
Identificar y catalogar TODAS las dependencias hardcodeadas de Keter hacia módulos de aleia-bereshit (DAATH, YESOD, AYIN) para planificar la migración.

## User Stories
- As a developer, I want to know all hardcoded imports so that I can plan abstraction layers
- As an architect, I want to identify circular dependencies so that I can design clean interfaces
- As a tester, I want to map test coverage per dependency so that I can ensure no regressions

## Functional Requirements
- REQ-1: Catalog all Python imports from `daath`, `yesod`, `ayin` modules
- REQ-2: Catalog all configuration variables referencing aleia-bereshit paths
- REQ-3: Catalog all Supabase schema references with hardcoded names
- REQ-4: Catalog all template files with absolute paths
- REQ-5: Generate dependency graph in Mermaid format

## Non-Functional Requirements
- Completeness: 100% of dependencies must be identified
- Traceability: Each dependency linked to source file and line number
- Severity: Each dependency classified as P0/P1/P2

## Acceptance Criteria
- [ ] All imports from daath/yesod/ayin identified with file:line
- [ ] All hardcoded paths documented
- [ ] Dependency graph generated
- [ ] Severity classification complete
