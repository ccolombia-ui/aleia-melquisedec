# Template Analysis Report — research-autopoietic-template

Date: 2026-01-10
Project: research-autopoietic-template

## Summary

- Documents scanned: 25
- Duplicates found: 0
- Semantic gaps detected (headings from `raw-manifiesto.md` poorly covered by corpus): 58
- Documents with low coherence (score < 0.3): 25
- Coverage (unit tests): 87.33% (pytest + coverage)

> Result: Automated quality gate (coverage) is above the 85% threshold.

---

## Key Findings

1. Coverage & Quality
   - Test suite: 24 unit tests (passing)
   - Total coverage: 87.33% (meets >85% requirement)

2. Duplicates
   - No near-duplicate documents detected at threshold 0.85.

3. Semantic Gaps (examples)
   - The analysis detected 58 manifesto headings with low coverage across repository documents.
   - Examples of low-coverage headings:
     - "Patrones de Bloqueo: 3 Escenarios" (coverage 0.16)
     - "Excepciones al Bloqueo" (coverage 0.12)
     - "1. EJECUCIÓN" (coverage 0.08)
     - "Responsabilidad" (coverage 0.04)
     - "Stakeholders Afectados" (coverage 0.16)
     - ... (full list available in artifacts)

4. Coherence
   - Many core docs show low paragraph-level coherence (avg pairwise paragraph sim < 0.3):
     - `raw-manifiesto.md` (0.03)
     - `design.md` (0.09)
     - `PROPOSITO.md` (0.03)
     - `requirements.md` (0.10)
     - `tech.md` (0.04)
     - `mvp-triple-persistence.md` (0.07)
     - Full per-document scores available in artifacts

---

## Recommendations (Minimalist Reorganization)

Objective: Reduce duplication of effort, create a single source of truth per manifesto heading, and increase coherence.

1. Canonicalization (Single Source of Truth)
   - For each manifesto heading (P1..P10 and subheadings), create a single canonical document `canonical/<heading-slug>.md` that contains the authoritative text.
   - Add frontmatter: `canonical_for: "<heading>"`, `rostro: <owner>`, `canonical=true`.

2. Minimal TOC-driven Structure
   - Generate a minimal TOC from `raw-manifiesto.md` headings and ensure each TOC item is backed by exactly one canonical document.
   - Keep the template repository lightweight: only the canonical docs + short summaries per folder (010-050) and a grid of mappings.

3. Remove & Merge
   - Merge near-duplicates and archive replaced files with a short redirect note linking to canonical doc.
   - Use PRs with `--squash` and standard commit message referencing the canonical id.

4. Tagging & Rostros
   - Introduce a controlled vocabulary (10-20 tags) and tag each canonical file.
   - Assign `rostro` to each canonical doc to establish ownership and acceptance criteria.

5. CI Enforcement
   - Add a pre-commit or CI check that:
     - Validates `canonical_for` uniqueness (no two canonical files claim the same heading)
     - Ensures each manifesto heading has either a canonical doc or a TODO entry
     - Fails build when coherence falls below a threshold for newly added docs

6. Incremental Work Plan (first 2 weeks)
   - Week 1: Create canonical docs for P1-P3, add controlled tags, update TOC
   - Week 2: Merge duplicates for the 5 highest-traffic docs and run coherence re-evaluation

---

## Next Steps & Artifacts

- Scripts added:
  - `packages/triple-persistence/examples/06_analyze_template.py` — offline analysis (duplicates, gaps, coherence)
  - `packages/triple-persistence/examples/05_analyze_manifiesto.py` — manifesto-specific interactive analysis

- Documents created:
  - `packages/triple-persistence/ANALYZE-DOCUMENT.md` — how-to guide
  - `packages/triple-persistence/QUALITY-REPORT.md` — QA report and metrics

---

If you want, I can now:
1. Automatically create `canonical/` stubs for the top N manifesto headings and open PRs with suggested merges.
2. Implement CI checks to validate `canonical_for` uniqueness and minimum coverage per heading.

Which of the two would you like me to do next?
