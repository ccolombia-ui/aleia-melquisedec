---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/requirements/REQ-004-lens-integration'
dc:title: 'REQ-004: Lens Integration - Lens Variants System'
dc:created: '2026-01-10'
version: '0.1.0'
status: 'draft'
result_type: 'intermediate'
associated_causes:
  - 'cause-004-lens-selection'
associated_features:
  - 'feat-lens-variants'
outputs:
  immediate: 'Lens templates and selection guide'
  intermediate: 'Validated lens selection for experiments'
  final: 'Lens-integrated templates used across specs'
generated_from: '_templates/daath-zen-patterns/daath-zen-req-template.md'
template_root: '_templates/daath-zen-patterns/template-configurable_daath-zen-root.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '320-380'
    rationale: 'Lens variants must be documented and referenced in templates.'
---

# REQ-004: Lens Integration - Lens Variants System

**Priority**: High
**Type**: Architecture
**Effort**: 12 hours

## 1. Problem Statement

Need to support multiple research and generation lenses (DSR, IMRAD, DDD) through template variants.

## 2. Summary

Provide a small set of lens templates and documentation that can be plugged into artifact templates and selected per-spec based on research objectives. This reduces ambiguity for authors and ensures outputs are comparable.

## 3. Deliverables & Owner

- Owner: MORPHEUS
- Deliverables:
  - Lens taxonomy document (`docs/guides/LENS-TAXONOMY.md`)
  - Two lens templates (DSR, IMRAD) in `_templates/daath-zen-patterns/`
  - Evaluation checklist to select lens per spec

## 4. Next Steps

- Define lens taxonomy and minimal example templates for DSR and IMRAD
- Provide evaluation criteria to select the appropriate lens for each spec
- Add examples to `_templates/daath-zen-patterns/`

---

*Generated via daath-zen-req-template (stub).*
