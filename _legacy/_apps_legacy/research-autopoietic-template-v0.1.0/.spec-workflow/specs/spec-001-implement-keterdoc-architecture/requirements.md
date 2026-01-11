# Requisitos: spec-001-implement-keterdoc-architecture

## 📋 Resumen de Requisitos

**Propósito**: Definir requisitos detallados para la implementación de la arquitectura KeterDoc siguiendo la metodología RBM-GAC (Gestión Basada en Resultados - Metas, Actividades, Contexto).

**Fuente**: Derivado de lesson-001-keterdoc-architecture-gap.md y 3212 líneas de documentación del manifiesto.

**Estructura**: 7 fases × múltiples requisitos por fase = 52 requisitos totales

---

## Índice de Requisitos (Hub-note)

Los requisitos detallados han sido migrados a `010-define/workbooks/` como archivos atómicos REQ-XXX.md siguiendo el patrón de plantillas configurables DAATH-ZEN.

| ID | Título | Prioridad | Estado | Ruta |
|----|--------|-----------|--------|------|
| [REQ-001](workbooks/REQ-001-context-validation.md) | Definir Vocabulario YAML-LD @context | Crítico | Borrador | workbooks/REQ-001-context-validation.md |
| [REQ-002](workbooks/REQ-002-template-generation.md) | Crear Plantilla Base - Concepto y Generador | Crítico | Borrador | workbooks/REQ-002-template-generation.md |
| [REQ-003](workbooks/REQ-003-metadata-enrichment.md) | Enriquecimiento de Metadatos para Embeddings y Grafos | Alto | Borrador | workbooks/REQ-003-metadata-enrichment.md |
| [REQ-004](workbooks/REQ-004-lens-integration.md) | Integración de Lentes - Sistema de Variantes | Alto | Borrador | workbooks/REQ-004-lens-integration.md |
| [REQ-005](workbooks/REQ-005-lesson-tpl.md) | Crear Plantilla Base - Lección Aprendida | Crítico | Borrador | workbooks/REQ-005-lesson-tpl.md |
| [REQ-006](workbooks/REQ-006-output-tpl.md) | Crear Plantilla Base - Artefacto de Salida | Alto | Borrador | workbooks/REQ-006-output-tpl.md |
| [REQ-007](workbooks/REQ-007-implementation-logs.md) | Registros de Implementación y Lista de Validación | Alto | Borrador | workbooks/REQ-007-implementation-logs.md |
| [REQ-008](workbooks/REQ-008-lens-variants.md) | Variantes de Lentes - Guía Práctica | Medio | Borrador | workbooks/REQ-008-lens-variants.md |
| [REQ-009](workbooks/REQ-009-validation-scripts.md) | Scripts de Validación para Plantillas y Frontmatter | Alto | Borrador | workbooks/REQ-009-validation-scripts.md |
| [REQ-010](workbooks/REQ-010-neo4j-integration.md) | Integración Neo4j - Ingestión y mapeo RDF | Alto | Borrador | workbooks/REQ-010-neo4j-integration.md |
| [REQ-011](workbooks/REQ-011-create-ddd-lens-variants-6-templates.md) | Create DDD Lens Variants (6 templates) | Alto | Borrador | workbooks/REQ-011-create-ddd-lens-variants-6-templates.md |
| [REQ-012](workbooks/REQ-012-create-social-lens-variants-6-templates.md) | Create Social Lens Variants (6 templates) | Medio | Borrador | workbooks/REQ-012-create-social-lens-variants-6-templates.md |
| [REQ-013](workbooks/REQ-013-document-lens-selection-guide.md) | Document Lens Selection Guide | Alto | Borrador | workbooks/REQ-013-document-lens-selection-guide.md |
| [REQ-014](workbooks/REQ-014-define-artifact-workflow-mapping.md) | Define Artifact-Workflow Mapping | Crítico | Borrador | workbooks/REQ-014-define-artifact-workflow-mapping.md |
| [REQ-015](workbooks/REQ-015-create-pattern---output-triple-pattern-000.md) | Create Pattern - Output Triple (PATTERN-000) | Crítico | Borrador | workbooks/REQ-015-create-pattern---output-triple-pattern-000.md |
| [REQ-016](workbooks/REQ-016-create-patterns-001-009-9-patterns.md) | Create Patterns 001-009 (9 patterns) | Alto | Borrador | workbooks/REQ-016-create-patterns-001-009-9-patterns.md |
| [REQ-017](workbooks/REQ-017-document-pattern-system.md) | Document Pattern System | Alto | Borrador | workbooks/REQ-017-document-pattern-system.md |
| [REQ-018](workbooks/REQ-018-script---convert-issue.yaml-to-issue.md.md) | Script - Convert ISSUE.yaml to ISSUE.md | Crítico | Borrador | workbooks/REQ-018-script---convert-issue.yaml-to-issue.md.md |
| [REQ-019](workbooks/REQ-019-script---generate-artifact-from-template.md) | Script - Generate Artifact from Template | Crítico | Borrador | workbooks/REQ-019-script---generate-artifact-from-template.md |
| [REQ-020](workbooks/REQ-020-script---validate-keterdoc-compliance.md) | Script - Validate KeterDoc Compliance | Crítico | Borrador | workbooks/REQ-020-script---validate-keterdoc-compliance.md |
| [REQ-021](workbooks/REQ-021-script---extract-seci-relationships.md) | Script - Extract SECI Relationships | Alto | Borrador | workbooks/REQ-021-script---extract-seci-relationships.md |
| [REQ-022](workbooks/REQ-022-test-suite-for-all-tools.md) | Test Suite for All Tools | Alto | Borrador | workbooks/REQ-022-test-suite-for-all-tools.md |
| [REQ-023](workbooks/REQ-023-script---yaml-ld-to-rdf-triples.md) | Script - YAML-LD to RDF Triples | Crítico | Borrador | workbooks/REQ-023-script---yaml-ld-to-rdf-triples.md |
| [REQ-024](workbooks/REQ-024-script---import-rdf-triples-to-neo4j.md) | Script - Import RDF Triples to Neo4j | Crítico | Borrador | workbooks/REQ-024-script---import-rdf-triples-to-neo4j.md |
| [REQ-025](workbooks/REQ-025-create-semantic-query-examples.md) | Create Semantic Query Examples | Alto | Borrador | workbooks/REQ-025-create-semantic-query-examples.md |
| [REQ-026](workbooks/REQ-026-document-neo4j-integration-guide.md) | Document Neo4j Integration Guide | Alto | Borrador | workbooks/REQ-026-document-neo4j-integration-guide.md |
| [REQ-027](workbooks/REQ-027-backup-current-template.md) | Backup Current Template | Crítico | Borrador | workbooks/REQ-027-backup-current-template.md |
| [REQ-028](workbooks/REQ-028-migrate-issue.yaml-to-issue.md.md) | Migrate ISSUE.yaml to ISSUE.md | Crítico | Borrador | workbooks/REQ-028-migrate-issue.yaml-to-issue.md.md |
| [REQ-029](workbooks/REQ-029-migrate-existing-artifacts.md) | Migrate Existing Artifacts | Alto | Borrador | workbooks/REQ-029-migrate-existing-artifacts.md |
| [REQ-030](workbooks/REQ-030-test-obsidian-integration.md) | Test Obsidian Integration | Alto | Borrador | workbooks/REQ-030-test-obsidian-integration.md |
| [REQ-031](workbooks/REQ-031-test-spec-workflow-mcp-integration.md) | Test spec-workflow-mcp Integration | Alto | Borrador | workbooks/REQ-031-test-spec-workflow-mcp-integration.md |
| [REQ-032](workbooks/REQ-032-generate-neo4j-knowledge-graph.md) | Generate Neo4j Knowledge Graph | Alto | Borrador | workbooks/REQ-032-generate-neo4j-knowledge-graph.md |
| [REQ-033](workbooks/REQ-033-run-full-validation-suite.md) | Run Full Validation Suite | Crítico | Borrador | workbooks/REQ-033-run-full-validation-suite.md |
| [REQ-034](workbooks/REQ-034-extract-lesson-002-migration-validation.md) | Extract lesson-002-migration-validation | Alto | Borrador | workbooks/REQ-034-extract-lesson-002-migration-validation.md |
| [REQ-035](workbooks/REQ-035-create-module-01-fundamentos-specs-4-specs.md) | Create Module 01-fundamentos Specs (4 specs) | Alto | Borrador | workbooks/REQ-035-create-module-01-fundamentos-specs-4-specs.md |
| [REQ-036](workbooks/REQ-036-create-module-02-arquitectura-specs-5-specs.md) | Create Module 02-arquitectura Specs (5 specs) | Alto | Borrador | workbooks/REQ-036-create-module-02-arquitectura-specs-5-specs.md |
| [REQ-037](workbooks/REQ-037-create-module-03-workflow-specs-4-specs.md) | Create Module 03-workflow Specs (4 specs) | Alto | Borrador | workbooks/REQ-037-create-module-03-workflow-specs-4-specs.md |
| [REQ-038](workbooks/REQ-038-create-module-04-implementacion-specs-3-specs.md) | Create Module 04-implementacion Specs (3 specs) | Medio | Borrador | workbooks/REQ-038-create-module-04-implementacion-specs-3-specs.md |
| [REQ-039](workbooks/REQ-039-create-module-05-casos-estudio-specs-2-specs.md) | Create Module 05-casos-estudio Specs (2 specs) | Bajo | Borrador | workbooks/REQ-039-create-module-05-casos-estudio-specs-2-specs.md |
| [REQ-040](workbooks/REQ-040-create-module-06-referencias-specs-1-spec.md) | Create Module 06-referencias Specs (1 spec) | Bajo | Borrador | workbooks/REQ-040-create-module-06-referencias-specs-1-spec.md |
| [REQ-041](workbooks/REQ-041-create-master-index-spec-021.md) | Create Master Index (spec-021) | Crítico | Borrador | workbooks/REQ-041-create-master-index-spec-021.md |
| [REQ-042](workbooks/REQ-042-generate-implementation-status-tracker.md) | Generate Implementation Status Tracker | Alto | Borrador | workbooks/REQ-042-generate-implementation-status-tracker.md |
| [REQ-043](workbooks/REQ-043-validate-complete-system-coherence.md) | Validate Complete System Coherence | Crítico | Borrador | workbooks/REQ-043-validate-complete-system-coherence.md |
| [REQ-044](workbooks/REQ-044-extract-lesson-003-manifesto-coherence.md) | Extract lesson-003-manifesto-coherence | Alto | Borrador | workbooks/REQ-044-extract-lesson-003-manifesto-coherence.md |
| [REQ-045](workbooks/REQ-045-crear-especificaciones-módulo-03-workflow-4-specs.md) | Crear Especificaciones Módulo 03-workflow (4 specs) | Alto | Borrador | workbooks/REQ-045-crear-especificaciones-módulo-03-workflow-4-specs.md |
| [REQ-046](workbooks/REQ-046-crear-especificaciones-módulo-04-implementacion-3-.md) | Crear Especificaciones Módulo 04-implementacion (3 specs) | Medio | Borrador | workbooks/REQ-046-crear-especificaciones-módulo-04-implementacion-3-.md |
| [REQ-047](workbooks/REQ-047-crear-especificaciones-módulo-05-casos-estudio-2-s.md) | Crear Especificaciones Módulo 05-casos-estudio (2 specs) | Bajo | Borrador | workbooks/REQ-047-crear-especificaciones-módulo-05-casos-estudio-2-s.md |
| [REQ-048](workbooks/REQ-048-crear-especificación-módulo-06-referencias-1-spec.md) | Crear Especificación Módulo 06-referencias (1 spec) | Bajo | Borrador | workbooks/REQ-048-crear-especificación-módulo-06-referencias-1-spec.md |
| [REQ-049](workbooks/REQ-049-crear-índice-maestro-spec-021.md) | Crear Índice Maestro (spec-021) | Crítico | Borrador | workbooks/REQ-049-crear-índice-maestro-spec-021.md |
| [REQ-050](workbooks/REQ-050-generar-rastreador-de-estado-de-implementación.md) | Generar Rastreador de Estado de Implementación | Alto | Borrador | workbooks/REQ-050-generar-rastreador-de-estado-de-implementación.md |
| [REQ-051](workbooks/REQ-051-validar-coherencia-completa-del-sistema.md) | Validar Coherencia Completa del Sistema | Crítico | Borrador | workbooks/REQ-051-validar-coherencia-completa-del-sistema.md |
| [REQ-052](workbooks/REQ-052-extraer-lesson-003-manifesto-coherence.md) | Extraer lesson-003-manifesto-coherence | Alto | Borrador | workbooks/REQ-052-extraer-lesson-003-manifesto-coherence.md |

> **Note:** ✅ COMPLETADO: 52/52 requerimientos generados (Phase 1-7 completa). Todos en español con formato YAML-LD + KeterDoc.

## Next Steps and Migration Plan

- [ ] Migrate REQ-011..REQ-020 this week (owner: MORPHEUS)
- [ ] Add validation scripts (`tools/validate-frontmatter.py`) and integrate into CI (owner: SALOMON)
- [ ] Request HYPATIA review for the DAATH-ZEN templates (see `review/HYPATIA-REVIEW.md`) and mark templates `stable` or `experimental`
- [ ] Run JSON-LD validation for REQ-001..REQ-010 examples and record results in `Implementation Logs/`

---

## Phase 1: Fundamentos (Weeks 1-2)

### REQ-001: Define YAML-LD @context Vocabulary

**Priority**: Crítico
**Type**: Architecture
**Effort**: 16 hours

**Description**:
Create `context.jsonld` file defining semantic web vocabulary for MELQUISEDEC system.

**Acceptance Criteria**:
- [ ] File: `context.jsonld` created in project root
- [ ] Defines namespaces: dc (Dublin Core), seci (SECI Model), mel (MELQUISEDEC)
- [ ] Maps KeterDoc fields: id, is_a, version, permalink
- [ ] Validates in JSON-LD Playground (https://json-ld.org/playground/)
- [ ] Includes @vocab for default namespace
- [ ] Documents usage with 3 complete examples
- [ ] Artifact generated from `daath-zen-req-template` and saved as `010-define/workbooks/REQ-001-context-validation.md` (includes `template_root: template-configurable_daath-zen-root.md`)

**Dependencies**: None
**Validation Method**: JSON-LD Playground validation + RDF triple generation test

---

### REQ-002: Create Base Template - Concept

**Priority**: Crítico
**Type**: Template
**Effort**: 8 hours

**Description**:
Create artifact-templates/by-type/concept-tpl.md following KeterDoc standard.

**Acceptance Criteria**:
- [ ] File: `artifact-templates/by-type/concept-tpl.md`
- [ ] YAML-LD frontmatter with @context, @type, @id
- [ ] KeterDoc metadata: id, is_a, version, dc, seci
- [ ] Body sections: Definition, Context, Relationships, Examples, References
- [ ] Includes filled example with actual data
- [ ] README.md explains usage with CLI: `generate-artifact-from-template.py concept`

**Dependencies**: REQ-001 (needs @context)
**Validation Method**: Template renders successfully with test data

---

### REQ-003: Create Base Template - Analysis

**Priority**: Alto
**Type**: Template
**Effort**: 8 hours

**Description**:
Create artifact-templates/by-type/analysis-tpl.md for analytical artifacts.

**Acceptance Criteria**:
- [ ] File: `artifact-templates/by-type/analysis-tpl.md`
- [ ] YAML-LD + KeterDoc frontmatter (same as REQ-002)
- [ ] Body sections: Objective, Data, Methods, Findings, Implications, Limitations
- [ ] Includes filled example (e.g., "Analysis of YAML vs YAML-LD")
- [ ] Documented usage

**Dependencies**: REQ-001
**Validation Method**: Template validation script

---

### REQ-004: Create Base Template - Decision

**Priority**: Alto
**Type**: Template
**Effort**: 8 hours

**Description**:
Create artifact-templates/by-type/decision-tpl.md for architectural decisions (ADR-style).

**Acceptance Criteria**:
- [ ] File: `artifact-templates/by-type/decision-tpl.md`
- [ ] YAML-LD + KeterDoc frontmatter
- [ ] Body sections: Context, Decision, Consequences, Alternatives Considered, Status
- [ ] Includes example (e.g., "ADR-003: Migrate YAML to YAML-LD")
- [ ] Documented usage

**Dependencies**: REQ-001
**Validation Method**: Template validation script

---

### REQ-005: Create Base Template - Experiment

**Priority**: Medio
**Type**: Template
**Effort**: 8 hours

**Description**:
Create artifact-templates/by-type/experiment-tpl.md for empirical experiments.

**Acceptance Criteria**:
- [ ] File: `artifact-templates/by-type/experiment-tpl.md`
- [ ] YAML-LD + KeterDoc frontmatter
- [ ] Body sections: Hypothesis, Methodology, Setup, Results, Analysis, Conclusions
- [ ] Includes example experiment
- [ ] Documented usage

**Dependencies**: REQ-001
**Validation Method**: Template validation script

---

### REQ-006: Create Base Template - Output

**Priority**: Alto
**Type**: Template
**Effort**: 8 hours

**Description**:
Create artifact-templates/by-type/output-tpl.md for deliverable outputs (papers, tools, datasets).

**Acceptance Criteria**:
- [ ] File: `artifact-templates/by-type/output-tpl.md`
- [ ] YAML-LD + KeterDoc frontmatter
- [ ] Body sections: Description, Purpose, Usage, Technical Details, Outputs, Links
- [ ] Includes example (e.g., "Tool: validate-keterdoc-compliance.py")
- [ ] Documented usage

**Dependencies**: REQ-001
**Validation Method**: Template validation script

---

### REQ-007: Create Base Template - Lesson

**Priority**: Crítico
**Type**: Template
**Effort**: 8 hours

**Description**:
Create artifact-templates/by-type/lesson-tpl.md for lessons learned (autopoiesis system).

**Acceptance Criteria**:
- [ ] File: `artifact-templates/by-type/lesson-tpl.md`
- [ ] YAML-LD + KeterDoc frontmatter
- [ ] Body sections: Executive Summary, Context, Gap Details, Solution Applied, Migration Plan, Validation, Confidence Evolution
- [ ] Includes example (lesson-001 as template)
- [ ] Documented usage with confidence scoring guide

**Dependencies**: REQ-001
**Validation Method**: lesson-001.md validates against this template

---

### REQ-008: Document Template Usage Guide

**Priority**: Alto
**Type**: Documentation
**Effort**: 8 hours

**Description**:
Create docs/guides/KETERDOC-QUICKSTART.md explaining KeterDoc system usage.

**Acceptance Criteria**:
- [ ] File: `docs/guides/KETERDOC-QUICKSTART.md`
- [ ] Sections: What is KeterDoc, Why YAML-LD, Template Structure, Quick Start, Examples
- [ ] Includes CLI commands for generating artifacts
- [ ] Shows SECI model usage (derives_from, informs)
- [ ] Links to manifesto documentation
- [ ] 3 complete end-to-end examples

**Dependencies**: REQ-002 through REQ-007
**Validation Method**: Developer follows guide and creates artifact successfully

---

## Phase 2: Lens Integration (Weeks 3-4)

### REQ-009: Create DSR Lens Variants (6 templates)

**Priority**: Alto
**Type**: Template
**Effort**: 24 hours

**Description**:
Create Design Science Research lens variants for 6 base templates.

**Acceptance Criteria**:
- [ ] Folder: `artifact-templates/by-lens/dsr/`
- [ ] 6 files: concept-dsr-tpl.md, analysis-dsr-tpl.md, decision-dsr-tpl.md, experiment-dsr-tpl.md, output-dsr-tpl.md, lesson-dsr-tpl.md
- [ ] Each template adapted for DSR:
  - Concept: Includes "Design Requirements" section
  - Analysis: Includes "Design Space Analysis"
  - Experiment: Includes "Artifact Evaluation"
- [ ] All templates inherit base structure + add DSR-specific sections
- [ ] README.md explains DSR lens philosophy

**Dependencies**: REQ-002 through REQ-007
**Validation Method**: Compare against base templates, verify DSR additions

---

### REQ-010: Create IMRAD Lens Variants (6 templates)

**Priority**: Alto
**Type**: Template
**Effort**: 24 hours

**Description**:
Create IMRAD (Introduction, Methods, Results, And Discussion) lens variants.

**Acceptance Criteria**:
- [ ] Folder: `artifact-templates/by-lens/imrad/`
- [ ] 6 files: concept-imrad-tpl.md, analysis-imrad-tpl.md, etc.
- [ ] Each template adapted for IMRAD scientific structure:
  - Concept: Includes "Literature Context" section
  - Analysis: Strict Methods → Results → Discussion format
  - Experiment: Full IMRAD structure with Introduction
- [ ] README.md explains IMRAD lens philosophy

**Dependencies**: REQ-002 through REQ-007
**Validation Method**: Verify IMRAD structure compliance

---

### REQ-011: Create DDD Lens Variants (6 templates)

**Priority**: Alto
**Type**: Template
**Effort**: 24 hours

**Description**:
Create Domain-Driven Design lens variants for software-focused research.

**Acceptance Criteria**:
- [ ] Folder: `artifact-templates/by-lens/ddd/`
- [ ] 6 files: concept-ddd-tpl.md, analysis-ddd-tpl.md, etc.
- [ ] Each template adapted for DDD:
  - Concept: Includes "Ubiquitous Language" and "Bounded Context"
  - Analysis: Includes "Domain Model" section
  - Decision: Includes "Strategic Design Impact"
- [ ] README.md explains DDD lens philosophy

**Dependencies**: REQ-002 through REQ-007
**Validation Method**: Verify DDD strategic/tactical patterns included

---

### REQ-012: Create Social Lens Variants (6 templates)

**Priority**: Medio
**Type**: Template
**Effort**: 24 hours

**Description**:
Create Social Science lens variants for qualitative research.

**Acceptance Criteria**:
- [ ] Folder: `artifact-templates/by-lens/social/`
- [ ] 6 files: concept-social-tpl.md, analysis-social-tpl.md, etc.
- [ ] Each template adapted for Social Science:
  - Concept: Includes "Social Context" and "Stakeholder Perspectives"
  - Analysis: Includes "Qualitative Coding" section
  - Experiment: Includes "Participant Demographics"
- [ ] README.md explains Social lens philosophy

**Dependencies**: REQ-002 through REQ-007
**Validation Method**: Verify social science methods included

---

### REQ-013: Document Lens Selection Guide

**Priority**: Alto
**Type**: Documentation
**Effort**: 8 hours

**Description**:
Create docs/guides/LENS-SELECTION-GUIDE.md to help choose appropriate lens.

**Acceptance Criteria**:
- [ ] File: `docs/guides/LENS-SELECTION-GUIDE.md`
- [ ] Decision matrix: Project Type → Recommended Lens
- [ ] Examples: "Building a tool? Use DSR", "Quantitative study? Use IMRAD"
- [ ] Comparison table showing differences between lenses
- [ ] Can combine lenses (e.g., DSR+DDD for software artifacts)
- [ ] Links to manifesto's lens documentation

**Dependencies**: REQ-009 through REQ-012
**Validation Method**: Developers can select correct lens for their project type

---

## Phase 3: Workflow-Pattern System (Week 5)

### REQ-014: Define Artifact-Workflow Mapping

**Priority**: Crítico
**Type**: Configuration
**Effort**: 8 hours

**Description**:
Create config/artifact-workflows.yaml mapping artifact types to workflow patterns.

**Acceptance Criteria**:
- [ ] File: `config/artifact-workflows.yaml`
- [ ] Maps 28+ artifact types to patterns (e.g., concept → PATTERN-003-Conceptualize)
- [ ] Includes lens overrides (e.g., concept + DSR → PATTERN-003-DSR variant)
- [ ] Documents confidence score initialization (0.50 for new patterns)
- [ ] Version tracking (patterns can evolve v1.0.0 → v1.1.0)

**Dependencies**: REQ-002 through REQ-007
**Validation Method**: All artifact types have assigned pattern

---

### REQ-015: Create Pattern - Output Triple (PATTERN-000)

**Priority**: Crítico
**Type**: Configuration
**Effort**: 4 hours

**Description**:
Create patterns/PATTERN-000-output-triple.yaml for foundational Output Triple workflow.

**Acceptance Criteria**:
- [ ] File: `patterns/PATTERN-000-output-triple.yaml`
- [ ] Structure:
  ```yaml
  pattern:
    id: 'PATTERN-000-output-triple'
    version: '1.0.0'
    confidence: 0.90  # Alto confidence - documented in manifesto
    description: 'Write to Markdown + Neo4j + Vector Store simultaneously'
    steps:
      - name: 'Write Markdown file'
      - name: 'Generate RDF triples'
      - name: 'Import to Neo4j'
      - name: 'Generate embeddings'
      - name: 'Store in vector DB'
    validation_criteria:
      - 'All 3 outputs present'
      - 'Neo4j relationships match SECI model'
    lens_applicability: ['DSR', 'IMRAD', 'DDD', 'Social']
  ```

**Dependencies**: None
**Validation Method**: Pattern file validates against JSON Schema

---

### REQ-016 through REQ-024: Create Patterns 001-009

**Priority**: Alto
**Type**: Configuration
**Effort**: 36 hours (4 hours × 9 patterns)

**Description**:
Create 9 additional workflow patterns for different artifact types.

**Patterns**:
- PATTERN-001: Literature Review
- PATTERN-002: Atomization (paper → concepts)
- PATTERN-003: Conceptualize
- PATTERN-004: Analyze
- PATTERN-005: Decide (ADR)
- PATTERN-006: Experiment
- PATTERN-007: Problem-RBM-GAC (this spec uses it)
- PATTERN-008: Output-Production
- PATTERN-009: Lesson-Extraction

**Acceptance Criteria** (for each):
- [ ] File: `patterns/PATTERN-00X-{name}.yaml`
- [ ] Contains: id, version, confidence, description, steps, validation_criteria, lens_applicability
- [ ] Confidence initialized (0.50 for new, 0.80-0.90 for documented patterns)
- [ ] At least 3 steps defined
- [ ] At least 2 validation criteria

**Dependencies**: REQ-015
**Validation Method**: All 10 patterns validate, cover 28+ artifact types

---

### REQ-025: Document Pattern System

**Priority**: Alto
**Type**: Documentation
**Effort**: 8 hours

**Description**:
Create docs/guides/PATTERN-SYSTEM.md explaining workflow pattern usage and evolution.

**Acceptance Criteria**:
- [ ] File: `docs/guides/PATTERN-SYSTEM.md`
- [ ] Sections: What are Patterns, How Confidence Scores Work, Pattern Evolution, Creating Custom Patterns
- [ ] Explains autopoiesis: lessons → pattern updates → confidence increases
- [ ] Shows example: PATTERN-003 v1.0.0 (confidence 0.50) → v1.1.0 (confidence 0.85)
- [ ] Links to manifesto/02-arquitectura/05-autopoiesis-system.md

**Dependencies**: REQ-014 through REQ-024
**Validation Method**: Developers understand how to use and evolve patterns

---

## Phase 4: Migration Tools (Week 6)

### REQ-026: Script - Convert ISSUE.yaml to ISSUE.md

**Priority**: Crítico
**Type**: Tool
**Effort**: 12 hours

**Description**:
Create tools/keterdoc/convert-issue-yaml-to-md.py for automated migration.

**Acceptance Criteria**:
- [ ] File: `tools/keterdoc/convert-issue-yaml-to-md.py`
- [ ] Reads ISSUE.yaml, outputs ISSUE.md with YAML-LD frontmatter
- [ ] Preserves all data (problem, gap, goal → Markdown sections)
- [ ] Adds KeterDoc metadata (id, is_a, dc, seci)
- [ ] CLI: `convert-issue-yaml-to-md.py --input ISSUE.yaml --output ISSUE.md --dry-run`
- [ ] Includes validation: warns if required fields missing
- [ ] Unit tests: 5 test cases (complete YAML, partial, invalid, etc.)

**Dependencies**: REQ-001
**Validation Method**: Converts 5 test ISSUE.yaml files successfully

---

### REQ-027: Script - Generate Artifact from Template

**Priority**: Crítico
**Type**: Tool
**Effort**: 12 hours

**Description**:
Create tools/keterdoc/generate-artifact-from-template.py for quick artifact creation.

**Acceptance Criteria**:
- [ ] File: `tools/keterdoc/generate-artifact-from-template.py`
- [ ] CLI: `generate-artifact-from-template.py concept "Graph Databases" --lens dsr --output 020-conceive/02-atomics/concept-graph-databases.md`
- [ ] Automatically:
  - Selects template (by-lens if lens specified, else by-type)
  - Generates unique id
  - Populates dc.date with current date
  - Creates file in specified output path
- [ ] Interactive mode: prompts for missing values
- [ ] Validation: checks KeterDoc compliance before writing
- [ ] Unit tests: 8 test cases (all combinations: type × lens)

**Dependencies**: REQ-002 through REQ-012
**Validation Method**: Generates 10 test artifacts successfully

---

### REQ-028: Script - Validate KeterDoc Compliance

**Priority**: Crítico
**Type**: Tool
**Effort**: 12 hours

**Description**:
Create tools/keterdoc/validate-keterdoc-compliance.py for CI/CD validation.

**Acceptance Criteria**:
- [ ] File: `tools/keterdoc/validate-keterdoc-compliance.py`
- [ ] CLI: `validate-keterdoc-compliance.py --path apps/research-autopoietic-template/ --recursive`
- [ ] Validates:
  - YAML-LD frontmatter present (@context, @type, @id)
  - KeterDoc fields present (id, is_a, version, dc, seci)
  - dc.date format (ISO 8601)
  - seci.derives_from paths exist
  - artifact_template reference valid
- [ ] Output: JSON report with pass/fail + detailed errors
- [ ] Exit code 0 (pass) or 1 (fail) for CI/CD
- [ ] Unit tests: 10 test cases (valid, missing fields, invalid dates, etc.)

**Dependencies**: REQ-001, REQ-002
**Validation Method**: Validates 20 test artifacts, catches all intentional errors

---

### REQ-029: Script - Extract SECI Relationships

**Priority**: Alto
**Type**: Tool
**Effort**: 8 hours

**Description**:
Create tools/keterdoc/extract-seci-relationships.py to build dependency graph.

**Acceptance Criteria**:
- [ ] File: `tools/keterdoc/extract-seci-relationships.py`
- [ ] CLI: `extract-seci-relationships.py --path apps/ --output seci-graph.json`
- [ ] Parses all artifacts, extracts seci.derives_from and seci.informs
- [ ] Outputs graph JSON: nodes (artifacts) + edges (relationships)
- [ ] Detects cycles: warns if circular dependencies found
- [ ] Generates Mermaid diagram: `--format mermaid` option
- [ ] Unit tests: 5 test cases (simple graph, cycles, orphaned nodes)

**Dependencies**: REQ-001, REQ-002
**Validation Method**: Generates graph from 50 test artifacts

---

### REQ-030: Test Suite for All Tools

**Priority**: Alto
**Type**: Testing
**Effort**: 8 hours

**Description**:
Create tests/keterdoc/ with comprehensive unit tests for all 4 scripts.

**Acceptance Criteria**:
- [ ] Folder: `tests/keterdoc/`
- [ ] Files: test_convert.py, test_generate.py, test_validate.py, test_extract.py
- [ ] Coverage: >80% line coverage for all scripts
- [ ] Uses pytest framework
- [ ] Fixtures: test data in tests/keterdoc/fixtures/
- [ ] CI/CD integration: runs on every commit
- [ ] Test report: HTML coverage report generated

**Dependencies**: REQ-026 through REQ-029
**Validation Method**: All tests pass, coverage >80%

---

## Phase 5: Neo4j Integration (Week 7)

### REQ-031: Script - YAML-LD to RDF Triples

**Priority**: Crítico
**Type**: Tool
**Effort**: 16 hours

**Description**:
Create tools/neo4j/yaml-ld-to-rdf-triples.py to convert YAML-LD to RDF.

**Acceptance Criteria**:
- [ ] File: `tools/neo4j/yaml-ld-to-rdf-triples.py`
- [ ] Uses rdflib library for RDF generation
- [ ] CLI: `yaml-ld-to-rdf-triples.py --input concept.md --output concept.ttl --format turtle`
- [ ] Supports formats: turtle, n-triples, json-ld, xml
- [ ] Batch mode: processes entire directory
- [ ] Validates @context against context.jsonld
- [ ] Generates triples for:
  - dc fields (dc:title, dc:creator, dc:date, etc.)
  - seci relationships (mel:derivesFrom, mel:informs)
  - artifact typing (mel:is_a)
- [ ] Unit tests: 10 test cases (simple, complex, invalid)

**Dependencies**: REQ-001, REQ-002
**Validation Method**: Generates valid RDF triples for 20 test artifacts

---

### REQ-032: Script - Import RDF Triples to Neo4j

**Priority**: Crítico
**Type**: Tool
**Effort**: 16 hours

**Description**:
Create tools/neo4j/import-rdf-to-neo4j.py for RDF → Neo4j import.

**Acceptance Criteria**:
- [ ] File: `tools/neo4j/import-rdf-to-neo4j.py`
- [ ] CLI: `import-rdf-to-neo4j.py --input concept.ttl --neo4j-uri bolt://localhost:7687`
- [ ] Uses neosemantics (n10s) plugin for RDF import
- [ ] Creates nodes: (:Concept {id, title, version})
- [ ] Creates relationships: (:Concept)-[:DERIVES_FROM]->(:Paper)
- [ ] Batch import: processes directory of .ttl files
- [ ] Performance: imports 1000 artifacts in <5 minutes
- [ ] Dry-run mode: shows Cypher queries without executing
- [ ] Unit tests: 8 test cases (simple, batch, error handling)

**Dependencies**: REQ-031
**Validation Method**: Imports 100 test artifacts to Neo4j successfully

---

### REQ-033: Create Semantic Query Examples

**Priority**: Alto
**Type**: Documentation
**Effort**: 8 hours

**Description**:
Create tools/neo4j/semantic-queries/ with 10 example Cypher queries.

**Acceptance Criteria**:
- [ ] Folder: `tools/neo4j/semantic-queries/`
- [ ] 10 files: query-01-concept-lineage.cypher, query-02-knowledge-flow.cypher, etc.
- [ ] Queries:
  1. Find all concepts derived from specific paper
  2. Show knowledge flow (paper → concept → analysis → decision)
  3. Find orphaned concepts (no derives_from)
  4. Count artifacts by type and lens
  5. Find concepts used in multiple outputs
  6. Show rostro collaboration (artifacts by creator)
  7. Find patterns with confidence >0.80
  8. Show temporal evolution (artifacts by date)
  9. Find circular dependencies (cycles)
  10. Generate trazabilidad report for specific output
- [ ] Each query includes: description, example usage, expected output
- [ ] README.md with query explanations

**Dependencies**: REQ-032
**Validation Method**: All 10 queries run successfully on test data

---

### REQ-034: Document Neo4j Integration Guide

**Priority**: Alto
**Type**: Documentation
**Effort**: 8 hours

**Description**:
Create docs/guides/NEO4J-INTEGRATION.md explaining complete Neo4j workflow.

**Acceptance Criteria**:
- [ ] File: `docs/guides/NEO4J-INTEGRATION.md`
- [ ] Sections: Setup Neo4j, Install neosemantics, Generate RDF, Import Triples, Query Examples
- [ ] Includes docker-compose.yml for Neo4j setup
- [ ] Screenshots: Neo4j Browser showing knowledge graph
- [ ] Troubleshooting section: common errors and fixes
- [ ] Links to manifesto/02-arquitectura/04-sincronizacion-knowledge.md

**Dependencies**: REQ-031 through REQ-033
**Validation Method**: Developer follows guide and imports data successfully

---

## Phase 6: Pilot Migration (Week 8)

### REQ-035: Backup Current Template

**Priority**: Crítico
**Type**: Safety
**Effort**: 2 hours

**Description**:
Create complete backup of research-autopoietic-template before migration.

**Acceptance Criteria**:
- [ ] Backup: `apps/research-autopoietic-template.backup-YYYYMMDD/`
- [ ] Includes all files (ISSUE.yaml, artifacts, configs)
- [ ] Documented rollback procedure
- [ ] Git tag: `pre-keterdoc-migration`

**Dependencies**: None
**Validation Method**: Backup directory complete, can restore if needed

---

### REQ-036: Migrate ISSUE.yaml to ISSUE.md

**Priority**: Crítico
**Type**: Migration
**Effort**: 4 hours

**Description**:
Convert research-autopoietic-template/ISSUE.yaml → ISSUE.md.

**Acceptance Criteria**:
- [ ] File: `research-autopoietic-template/ISSUE.md` (NEW)
- [ ] Contains YAML-LD frontmatter with KeterDoc metadata
- [ ] All ISSUE.yaml data preserved in Markdown body
- [ ] Validation: passes validate-keterdoc-compliance.py
- [ ] ISSUE.yaml renamed to ISSUE.yaml.deprecated (not deleted)

**Dependencies**: REQ-026, REQ-028, REQ-035
**Validation Method**: ISSUE.md validates, spec-workflow-mcp reads it successfully

---

### REQ-037: Migrate Existing Artifacts

**Priority**: Alto
**Type**: Migration
**Effort**: 16 hours

**Description**:
Convert 20+ existing artifacts to new templates.

**Acceptance Criteria**:
- [ ] Migrate: 020-conceive/02-atomics/ (10+ concept files)
- [ ] Migrate: 030-design/03-analyses/ (5+ analysis files)
- [ ] Migrate: 030-design/04-decisions/ (5+ decision files)
- [ ] All artifacts have YAML-LD frontmatter
- [ ] All artifacts pass validation
- [ ] seci.derives_from populated (e.g., concept → paper in 010-define)
- [ ] Generate migration report (successes, manual interventions needed)

**Dependencies**: REQ-027, REQ-028, REQ-036
**Validation Method**: All migrated artifacts validate, seci relationships correct

---

### REQ-038: Test Obsidian Integration

**Priority**: Alto
**Type**: Testing
**Effort**: 4 hours

**Description**:
Verify ISSUE.md and artifacts work natively in Obsidian.

**Acceptance Criteria**:
- [ ] Open research-autopoietic-template in Obsidian
- [ ] ISSUE.md displays correctly (frontmatter + body)
- [ ] Artifacts display correctly
- [ ] Graph view shows links between artifacts
- [ ] YAML-LD frontmatter parseable by Obsidian plugins
- [ ] Can edit and save without corruption
- [ ] Wikilinks work: [[concept-graph-databases]]

**Dependencies**: REQ-036, REQ-037
**Validation Method**: Obsidian user verifies all features work

---

### REQ-039: Test spec-workflow-mcp Integration

**Priority**: Alto
**Type**: Testing
**Effort**: 4 hours

**Description**:
Verify spec-workflow-mcp processes ISSUE.md correctly.

**Acceptance Criteria**:
- [ ] spec-workflow-mcp reads ISSUE.md
- [ ] Generates requirements.md from ISSUE.md
- [ ] Generates tasks.md from requirements.md
- [ ] Respects workflow_pattern field
- [ ] No errors or warnings during processing

**Dependencies**: REQ-036
**Validation Method**: spec-workflow-mcp generates all expected files

---

### REQ-040: Generate Neo4j Knowledge Graph

**Priority**: Alto
**Type**: Testing
**Effort**: 4 hours

**Description**:
Import all migrated artifacts to Neo4j and verify relationships.

**Acceptance Criteria**:
- [ ] All artifacts converted to RDF (yaml-ld-to-rdf-triples.py)
- [ ] All RDF imported to Neo4j (import-rdf-to-neo4j.py)
- [ ] Neo4j Browser shows:
  - 20+ nodes (concepts, analyses, decisions)
  - DERIVES_FROM relationships visible
  - INFORMS relationships visible
- [ ] Sample query works: "Show all concepts derived from paper X"
- [ ] Performance: query response time <1 second

**Dependencies**: REQ-031, REQ-032, REQ-037
**Validation Method**: Neo4j graph visualizer shows complete knowledge tree

---

### REQ-041: Run Full Validation Suite

**Priority**: Crítico
**Type**: Testing
**Effort**: 4 hours

**Description**:
Execute all validation scripts on migrated project.

**Acceptance Criteria**:
- [ ] validate-keterdoc-compliance.py: 100% pass rate
- [ ] extract-seci-relationships.py: no cycles detected
- [ ] All unit tests pass (tests/keterdoc/)
- [ ] All semantic queries return expected results
- [ ] Validation report generated (JSON + HTML)

**Dependencies**: REQ-028, REQ-029, REQ-030, REQ-037
**Validation Method**: All checkpoints pass, zero errors

---

### REQ-042: Extract lesson-002-migration-validation

**Priority**: Alto
**Type**: Autopoiesis
**Effort**: 8 hours

**Description**:
Document lessons learned from pilot migration.

**Acceptance Criteria**:
- [ ] File: `060-reflect/lessons/lesson-002-migration-validation.md`
- [ ] YAML-LD + KeterDoc frontmatter (using lesson-tpl.md)
- [ ] seci.derives_from: chatlog of migration session
- [ ] Sections:
  - What worked well
  - What didn't work (manual interventions needed)
  - Adjustments made to templates/tools
  - Confidence score (0.00-1.00)
  - Recommendations for future migrations
- [ ] Updates pattern confidence scores (e.g., PATTERN-007 confidence 0.50 → 0.75)

**Dependencies**: REQ-036 through REQ-041
**Validation Method**: Lesson validates, confidence score justified

---

## Phase 7: Manifesto-Wide Specs + Index Coherence (Weeks 9-10) 🆕

### REQ-043: Create Module 01-fundamentos Specs (4 specs)

**Priority**: Alto
**Type**: Specification
**Effort**: 32 hours (8 hours × 4 specs)

**Description**:
Create implementation specs for manifesto module 01-fundamentos.

**Specs**:
1. **spec-002**: Visual identity for "Qué es MELQUISEDEC"
   - Interactive diagram showing 10 Sefirot
   - Rostros assignment to Sefirot
   - SVG + interactive web component

2. **spec-003**: Interactive Árbol de la Vida diagram
   - Neo4j graph visualizer
   - Shows 3 columns, 22 paths
   - Links to manifesto documentation

3. **spec-004**: 5 Rostros assignment automation
   - CLI tool: assign-rostro.py
   - Rules: task type → rostro mapping
   - Validation: ensures all rostros balanced

4. **spec-005**: P1-P10 compliance checker
   - Script: check-principios.py
   - Validates project against 10 principles
   - Generates compliance report (0-100%)

**Acceptance Criteria** (for each):
- [ ] Folder: `.spec-workflow/specs/spec-00X/`
- [ ] Files: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md
- [ ] ISSUE.md uses YAML-LD + KeterDoc format (like spec-001)
- [ ] Links to manifesto/01-fundamentos/ sections

**Dependencies**: REQ-001 through REQ-042 (Phase 1-6 complete)
**Validation Method**: All 4 specs created, follow template structure

---

### REQ-044: Create Module 02-arquitectura Specs (5 specs)

**Priority**: Alto
**Type**: Specification
**Effort**: 40 hours (8 hours × 5 specs)

**Description**:
Create implementation specs for manifesto module 02-arquitectura.

**Specs**:
1. **spec-006**: Research Instance structure validator
2. **spec-007**: Sistema de Checkpoints automation (CK-01 to CK-05)
3. **spec-008**: KnowledgeWriter API + Reconciliador deployment
4. **spec-009**: Autopoiesis system (chatlog + lessons) - EXTENDS current
5. **spec-010**: KeterDoc validation suite - EXTENDS spec-001

**Acceptance Criteria**: Same as REQ-043

**Dependencies**: REQ-043
**Validation Method**: All 5 specs created

---

### REQ-045: Create Module 03-workflow Specs (4 specs)

**Priority**: Alto
**Type**: Specification
**Effort**: 32 hours

**Description**:
Create implementation specs for manifesto module 03-workflow.

**Specs**:
1. **spec-011**: Kanban board integration (Trello/Jira/GitHub Projects)
2. **spec-012**: Trazabilidad graph visualizer (Neo4j Browser extension)
3. **spec-013**: Versionamiento automation (semantic versioning)
4. **spec-014**: MCPs integration guide (all 15 MCPs documented)

**Acceptance Criteria**: Same as REQ-043

**Dependencies**: REQ-044
**Validation Method**: All 4 specs created

---

### REQ-046: Create Module 04-implementacion Specs (3 specs)

**Priority**: Medio
**Type**: Specification
**Effort**: 24 hours

**Description**:
Create implementation specs for manifesto module 04-implementacion.

**Specs**:
1. **spec-015**: Flujo-completo wizard (CLI guided walkthrough)
2. **spec-016**: Lessons-learned extraction automation (AI-powered)
3. **spec-017**: Interactive checklist validator (web app)

**Acceptance Criteria**: Same as REQ-043

**Dependencies**: REQ-045
**Validation Method**: All 3 specs created

---

### REQ-047: Create Module 05-casos-estudio Specs (2 specs)

**Priority**: Bajo
**Type**: Documentation
**Effort**: 16 hours

**Description**:
Create documentation specs for manifesto module 05-casos-estudio.

**Specs**:
1. **spec-018**: CASO-01-DDD complete documentation
2. **spec-019**: CASO-02-PROMPTS-DINAMICOS complete documentation

**Acceptance Criteria**: Same as REQ-043

**Dependencies**: REQ-046
**Validation Method**: All 2 specs created

---

### REQ-048: Create Module 06-referencias Specs (1 spec)

**Priority**: Bajo
**Type**: Tool
**Effort**: 8 hours

**Description**:
Create tool spec for manifesto module 06-referencias.

**Specs**:
1. **spec-020**: Glosario kabalístico with search (searchable glossary)

**Acceptance Criteria**: Same as REQ-043

**Dependencies**: REQ-047
**Validation Method**: spec-020 created

---

### REQ-049: Create Master Index (spec-021) 🎯 CRITICAL

**Priority**: Crítico
**Type**: Documentation + Architecture
**Effort**: 16 hours

**Description**:
Rebuild docs/manifiesto/00-master-index.md with results chain and conceptualization map.

**Acceptance Criteria**:
- [ ] Folder: `.spec-workflow/specs/spec-021-master-index-coherence/`
- [ ] Files: ISSUE.md (YAML-LD + KeterDoc), requirements.md, design.md
- [ ] Deliverable: `docs/manifiesto/00-master-index.md` (NEW)
- [ ] Sections:
  - **Results Chain**: Mermaid diagram showing spec dependencies (spec-001 → spec-002 → ...)
  - **Conceptualization Map**: Visual showing how all 21 specs form complete system
  - **Implementation Status**: Table (module, specs, status, completion %)
  - **Product Vision**: Narrative connecting manifesto → implementation → product
- [ ] Deliverable: `docs/manifiesto/00-conceptualization-map.mermaid`
- [ ] Validation: All 20 previous specs referenced, no orphaned specs

**Dependencies**: REQ-043 through REQ-048
**Validation Method**: Master index shows complete system coherence, conceptualization map visualizes interconnections

---

### REQ-050: Generate Implementation Status Tracker

**Priority**: Alto
**Type**: Documentation
**Effort**: 8 hours

**Description**:
Create docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md for tracking.

**Acceptance Criteria**:
- [ ] File: `docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md`
- [ ] Table: Module | Specs | Status | Completion % | Next Actions
- [ ] Progress bars (visual)
- [ ] Links to each spec's ISSUE.md
- [ ] Auto-generated from spec folders (script: generate-status.py)
- [ ] CI/CD: updates automatically on spec changes

**Dependencies**: REQ-043 through REQ-049
**Validation Method**: Status document accurate, updates automatically

---

### REQ-051: Validate Complete System Coherence

**Priority**: Crítico
**Type**: Testing
**Effort**: 8 hours

**Description**:
Run comprehensive validation across all 21 specs and 6 modules.

**Acceptance Criteria**:
- [ ] All 21 specs created (spec-001 through spec-021)
- [ ] All specs use YAML-LD + KeterDoc format
- [ ] All specs link to manifesto sections (seci.source)
- [ ] No orphaned documentation (every manifesto section → spec)
- [ ] Master index shows complete results chain
- [ ] Conceptualization map visualizes system
- [ ] Implementation status tracker accurate

**Dependencies**: REQ-049, REQ-050
**Validation Method**: Coherence validation script passes 100%

---

### REQ-052: Extract lesson-003-manifesto-coherence

**Priority**: Alto
**Type**: Autopoiesis
**Effort**: 8 hours

**Description**:
Document lessons learned from Phase 7 (manifesto-wide implementation).

**Acceptance Criteria**:
- [ ] File: `060-reflect/lessons/lesson-003-manifesto-coherence.md`
- [ ] YAML-LD + KeterDoc frontmatter
- [ ] seci.derives_from: chatlog of Phase 7 sessions
- [ ] Sections:
  - How master index improves system understanding
  - Challenges creating 21 specs
  - Value of conceptualization map
  - Recommendations for maintaining coherence
  - Confidence score evolution (spec-001 0.95 → spec-021 0.98)
- [ ] Updates MELQUISEDEC system confidence (overall 0.00 → 0.90)

**Dependencies**: REQ-051
**Validation Method**: Lesson validates, system confidence justified

---

## 📊 Summary

**Total Requirements**: 52
**Total Effort**: 400 hours (10 weeks)

**By Phase**:
- Phase 1: 8 requirements, 64 hours
- Phase 2: 5 requirements, 88 hours
- Phase 3: 12 requirements, 56 hours
- Phase 4: 5 requirements, 52 hours
- Phase 5: 4 requirements, 48 hours
- Phase 6: 8 requirements, 46 hours
- Phase 7: 10 requirements, 80 hours

**Crítico Path**:
REQ-001 (@context) → REQ-002-007 (templates) → REQ-009-012 (lens variants) → REQ-014-024 (patterns) → REQ-026-030 (tools) → REQ-031-034 (Neo4j) → REQ-035-042 (pilot) → REQ-043-048 (module specs) → **REQ-049 (master index)** → REQ-051 (validation)

**Success**: All 52 requirements met, system coherence validated, autopoiesis active.
