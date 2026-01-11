# HYPATIA Review Checklist — spec-001-implement-keterdoc-architecture

**Purpose:** Provide a compact checklist and instructions for HYPATIA (manifesto authors) to review DAATH-ZEN templates and REQ artifacts.

**Intro:** This document is intentionally concise: it lists exactly what to validate, how to report, and the expected outcome of the review. Aim for concrete suggestions and clear approval (stable) or comments (experimental).

**Files to review:**
- `_templates/daath-zen-patterns/template-configurable_daath-zen-root.md`
- `_templates/daath-zen-patterns/daath-zen-req-template.md` (v0.1.0-experimental)
- `apps/research-autopoietic-template/010-define/workbooks/REQ-001-context-validation.md`
- `apps/research-autopoietic-template/010-define/workbooks/REQ-002-template-generation.md` .. `REQ-010-*.md`
- `docs/architecture/ADR-005-daath-zen-configurable-templates.md`

## Review Tasks

1. Manifesto Coherence
   - Confirm `manifesto_coherence` references (file + lines) are correct for the template fields
   - Suggest updated line ranges where necessary

2. Metadata & Validation
   - Check required frontmatter fields: `@context`, `@type`, `@id`, `dc:title`, `dc:created`, `version`, `status`
   - Confirm `result_type` ontology: `immediate | intermediate | final` aligns with RBM-GAC concepts
   - Run JSON-LD validation on sample artifacts (REQ-001 example included)

3. Result Mapping & Causality
   - Validate that `associated_causes` and `associated_features` are suitable to link intermediate results to causes and product features
   - Suggest additional fields if needed to capture causality metadata

4. Template Governance
   - Review `template-configurable_daath-zen-root.md` policies (applies_to, recommended_versions)
   - Suggest `stable` vs `experimental` tagging guidance

5. Usability & Examples
   - Ensure the generated REQ artifacts include clear examples for `outputs` mapping (immediate/intermediate/final)
   - Confirm `generated_from` and `template_root` usage help with traceability

6. Migration Guidance
   - Recommend any migration notes to include when converting existing REQUIREMENTS to workbooks/REQ-XXX.md

## Required Deliverables
- A short review comment in this file (add notes under 'HYPATIA REVIEW NOTES')
- Approve template as `stable` or label `experimental` with suggestions
- If major changes required, list them as action items with suggested owner (HYPATIA / SALOMON / MORPHEUS)

---

## HYPATIA REVIEW NOTES

- [ ] Review completed on: __/__/____
- Reviewer: HYPATIA
- Notes:

## How to provide the review

1. Add comments directly in this file under 'Notes' and prefix them with `HYPATIA:` so automation can detect them.
2. For proposed template changes, include a short rationale and suggested line range or patch snippet.
3. Indicate whether the template should be marked `stable` or remain `experimental`.
4. Suggested deadline for initial review: 2026-01-17 (one week)

*If you prefer, open a PR against branch `feature/canonical-stubs-batch-1` and tag @HYPATIA.*

## Acceptance Criteria for Review

- [ ] Templates declared `stable` or `experimental` with justification
- [ ] Manifesto coherence comments resolved or annotated
- [ ] Any required field additions proposed with rationale and example
- [ ] Expected follow-up tasks assigned with owners and target dates
