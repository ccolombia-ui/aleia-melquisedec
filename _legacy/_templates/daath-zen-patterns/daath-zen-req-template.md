---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'RequirementArtifactTemplate'
'@id': 'https://melquisedec.org/templates/daath-zen-req'
dc:title: 'daath-zen-req-template'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot'
version: '0.1.0-experimental'
status: 'draft'
template_root: 'template-configurable_daath-zen-root.md'
applies_to: 'daath-zen-req-v{MAJOR.MINOR.PATCH}'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'Requirement artifact must include KeterDoc metadata and result_type mapping.'

# Template configuration (placeholders)
# Use in generation tools to replace {{PLACEHOLDERS}}

# Required metadata fields
# - result_type: immediate | intermediate | final
# - associated_causes: [list of IDs or descriptions]
# - associated_features: [list of feature IDs]
# - outputs: immediate_result | intermediate_result | final_result  (free text / link to artifacts)

---

# REQ-{{REQ_ID}}: {{REQ_TITLE}}

**Generated From:** `{{TEMPLATE_PATH}}` (use `template_configurable_daath-zen-root` as root)

**Metadata**:

- result_type: {{result_type}}  # immediate | intermediate | final
- associated_causes: {{associated_causes}}  # e.g., cause-001
- associated_features: {{associated_features}}  # e.g., feat-auth, feat-search
- outputs:
  - immediate: {{outputs.immediate}}
  - intermediate: {{outputs.intermediate}}
  - final: {{outputs.final}}
- validation: TODO (link to validation script)

---

## 1. Problem Statement

{{PROBLEM_STATEMENT}}

## 2. Requirement Specification

### 2.1 Functional Requirements

- FR-{{REQ_ID}}.1: {{FR_DESCRIPTION}}

### 2.2 Non-Functional Requirements

- NFR-{{REQ_ID}}.1: {{NFR_DESCRIPTION}}

## 3. Acceptance Criteria

- AC-{{REQ_ID}}.1: {{AC_DESCRIPTION}}

## 4. Implementation Guidance

{{IMPLEMENTATION_GUIDANCE}}

## 5. Dependencies and Constraints

- Depends on: {{DEPENDENCIES}}

## 6. Verification Plan

- Test Cases: {{TEST_CASES}}

---

# Notes about result mapping and features

- Result mapping should explicitly declare which outputs are "immediate" (direct deliverables), which are "intermediate" (contribute to final results and are tied to causes/features), and which are "final" (user-facing or business outcomes).
- Use `associated_causes` to connect intermediate results to causal chains in RBM-GAC.
- Use `associated_features` to link requirements to product features.

# Versioning guidance

- Update `version` in frontmatter when template changes semantics
- Use `applies_to` to indicate domain and template stability (stable/experimental)

---

*This file is a configurable template. For final artifacts, fill placeholders and validate frontmatter against `template-configurable_daath-zen-root.md`.*
