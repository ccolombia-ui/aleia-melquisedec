---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'TechArticle'
'@id': 'https://melquisedec.org/adr/ADR-005'
dc:title: 'ADR-005: DAATH-ZEN Configurable Templates (REQ artifacts)'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot'
version: '1.0.0'
status: 'accepted'
---

# ADR-005: DAATH-ZEN Configurable Templates (REQ artifacts)

## Status

**ACCEPTED** - 2026-01-10

## Context

We need a configurable, versioned template system for generating REQ-XXX artifacts that:
- Aligns with the KeterDoc / Manifesto standards
- Encodes result mapping (immediate, intermediate, final)
- Records associations between intermediate results and causes/features
- Is manageable across multiple template versions

Existing references:
- `_templates/_daath-template/` (output scaffolding)
- `_templates/daath-zen-patterns/` (patterns folder)

## Decision

Create:
1. `template-configurable_daath-zen-root.md` — root governance and validation policy for DAATH-ZEN templates.
2. `daath-zen-req-template.md` — a configurable requirement artifact template (placeholders, result mapping fields, manifesto coherence metadata).
3. Use `daath-zen-req-template.md` to generate REQ artifacts (example: `010-define/workbooks/REQ-001-context-validation.md`).

## Rationale

- Centralized root template enforces coherent policy (applies_to, versioning, manifesto coherence).
- Requirement artifacts need explicit `result_type` and `associated_causes`/`associated_features` to support RBM-GAC mapping and traceability.
- Generating artifacts from templates ensures consistent frontmatter for embeddings and Neo4j ingestion.

## Consequences

Positive:
- ✅ Consistency across REQ artifacts
- ✅ Easier validation and automation
- ✅ Clear traceability from requirement → intermediate results → final outcomes

Negative / Caveats:
- ⚠️ Template design requires careful review (multiple versions exist)
- ⚠️ Migration of existing templates may be necessary

## Implementation

- `[x]` Add `template-configurable_daath-zen-root.md` in `_templates/daath-zen-patterns/` (done)
- `[x]` Add `daath-zen-req-template.md` (done, version 0.1.0-experimental)
- `[x]` Generate `010-define/workbooks/REQ-001-context-validation.md` using the template (done)
- `[ ]` Review template with manifesto authors (HYPATIA) and select `stable` vs `experimental` variants
- `[ ]` Add validation scripts referenced in the root

## Notes

- Intermediate results must include `associated_causes` that connect to RBM-GAC causality chains; likewise, `associated_features` tie requirements to product features.
- Use `template_root` reference in every generated artifact to show which root governed the template.

---

**Decision Made By:** User (ccolombia-ui) + GitHub Copilot
**Date:** 2026-01-10
**Confidence:** 90% (pending template review)
