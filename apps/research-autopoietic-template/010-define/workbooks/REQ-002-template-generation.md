---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/requirements/REQ-002-template-generation'
dc:title: 'REQ-002: Create Base Template - Concept & Generation Tools'
dc:created: '2026-01-10'
version: '0.1.0'
status: 'draft'
result_type: 'intermediate'
associated_causes:
  - 'cause-002-template-consistency'
associated_features:
  - 'feat-template-generator'
outputs:
  immediate: 'artifact-templates/by-type/concept-tpl.md'
  intermediate: 'CLI generator capable of generating artifacts from template'
  final: 'Consistent KeterDoc artifact templates across repository'
generated_from: '_templates/daath-zen-patterns/daath-zen-req-template.md'
template_root: '_templates/daath-zen-patterns/template-configurable_daath-zen-root.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'Template creation and KeterDoc compliance.'
---

# REQ-002: Create Base Template - Concept & Generation Tools

**Priority**: Critical
**Type**: Template
**Effort**: 8 hours

## 1. Problem Statement

We require a base concept template and a generator CLI so that new artifacts can be produced consistently and with valid YAML-LD frontmatter.

## 2. Requirement Specification

FR-002.1: Create `artifact-templates/by-type/concept-tpl.md` with YAML-LD frontmatter and example content.

FR-002.2: Provide a CLI (or python script) to generate artifacts from DAATH-ZEN templates (see tools/generate_from_daath_template.py).

## 3. Acceptance Criteria

- AC-002.1: Template file exists and validates as YAML-LD
- AC-002.2: Generator script can produce a valid concept artifact file when invoked with minimal parameters

## 4. Implementation Guidance

Use `tools/generate_from_daath_template.py` as the baseline generator and add validations.

## 5. Dependencies and Constraints

Depends on: REQ-001 (context.jsonld)

## 6. Verification Plan

- Use JSON-LD Playground to validate generated concept artifact
- Run generator with example: `python tools/generate_from_daath_template.py _templates/daath-zen-patterns/daath-zen-req-template.md REQ-002=...`

---

*Generated via daath-zen-req-template (stub).*
