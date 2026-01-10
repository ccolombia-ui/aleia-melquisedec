---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/requirements/REQ-009-validation-scripts'
dc:title: 'REQ-009: Validation Scripts for Template & Frontmatter'
dc:created: '2026-01-10'
version: '0.1.0'
status: 'draft'
result_type: 'immediate'
associated_causes:
  - 'cause-009-validation-automation'
associated_features:
  - 'feat-validation-scripts'
outputs:
  immediate: 'tools/validate-frontmatter.py'
  intermediate: 'CI job for frontmatter validation'
  final: 'Automated validation in CI for all generated artifacts'
generated_from: '_templates/daath-zen-patterns/daath-zen-req-template.md'
template_root: '_templates/daath-zen-patterns/template-configurable_daath-zen-root.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'Validation scripts required to ensure KeterDoc compliance.'
---

# REQ-009: Validation Scripts for Template & Frontmatter

**Priority**: High
**Type**: Tooling
**Effort**: 10 hours

## 1. Problem Statement

Add scripts to validate YAML-LD frontmatter, JSON-LD expansion, and required fields automatically in CI.

---

*Generated via daath-zen-req-template (stub).*
