# 6-outputs/ - Final Deliverables

## Purpose

This folder contains the final outputs of the academic research: SPECIFICATION.yaml (formal methodology specification), ROADMAP.md (execution plan), and the final literature review. These artifacts make the methodology executable and publishable.

## Required Files

### 1. SPECIFICATION.yaml (NEW in v2)
**Purpose:** Complete, structured specification of methodology (400-600 lines)

**Key Sections:**
- **metadata**: Title, version, author, spec:issue, status
- **overview**: Purpose, scope (included/excluded), target audience, domains
- **foundation**: Theoretical basis (sources, concepts), key principles
- **steps**: Full specification of each methodology step (inputs, outputs, procedure, validation, dependencies, related concepts)
- **concepts**: Core concepts (references to 3-atomics/), patterns
- **execution**: Prerequisites (knowledge, resources, tools), duration, phases, parallel execution
- **validation**: Completeness criteria, quality metrics
- **integration**: Related methodologies, cross-methodology concepts (references to 5-analysis-connection/)
- **references**: Primary sources, standards, related work
- **dublin_core**: DC metadata
- **changelog**: Version history

**Template:** See `methodology-workbook/6-outputs/README.md` for full YAML template (300+ lines)

**Example Structure:**
```yaml
metadata:
  title: "Ontology Engineering Methodology"
  version: "1.0.0"
  spec_issue: "SPEC-001"

overview:
  purpose: |
    Systematic approach to ontology development following ISO 25964-1
    and METHONTOLOGY framework...

steps:
  - id: "step-001"
    name: "Define Ontology Scope"
    inputs: [{name: "Domain requirements", source: "0-prompts/scope.md"}]
    outputs: [{name: "Scope document", location: "artifacts/scope.yaml"}]
    procedure: {file: "3-steps/step-001-define-scope.md"}
    related_concepts: ["atomic-001-ontology", "atomic-005-domain"]

concepts:
  core:
    - {id: "concept-001", name: "Ontology", extract: "3-atomics/atomic-001-ontology.md"}
```

---

### 2. ROADMAP.md (NEW in v2)
**Purpose:** 3-phase execution plan with timeline and milestones

**Template:**
```markdown
# {METHODOLOGY_NAME} Execution Roadmap

## Overview
- **Total Duration**: {X} hours ({Y} days)
- **Phases**: 3
- **Deliverable**: SPECIFICATION.yaml + Literature Review

## Phase 1: Foundation ({hours}h, Days 1-2)

**Objective:** Establish research context and collect sources

### Day 1 (8h)
- [ ] Define research scope (2h) → `0-prompts/scope.md`
- [ ] Document research questions (2h) → `0-prompts/research-questions.md`
- [ ] Collect 4-5 primary sources (4h) → `1-literature/`

### Day 2 (8h)
- [ ] Collect remaining sources (4h) → `1-literature/` (8-10 total)
- [ ] Begin atomic extraction (4h) → `3-atomics/` (4-6 atomics)

**Checkpoint B1:** 8+ sources collected, 4+ atomics extracted

---

## Phase 2: Analysis ({hours}h, Days 3-4)

**Objective:** Extract atomics and analyze themes

### Day 3 (8h)
- [ ] Complete atomic extraction (4h) → `3-atomics/` (10-12 total)
- [ ] Identify 2-3 major themes (4h) → `2-analysis/`

### Day 4 (8h)
- [ ] Complete theme analysis (4h) → `2-analysis/` (4-5 themes)
- [ ] Create concept map diagram (2h) → `4-canvas/concept-map.md`
- [ ] Document methodology steps (2h) → `3-steps/` (5-7 steps)

**Checkpoint B2:** 10+ atomics, 4+ themes, 5+ steps, 1+ diagram

---

## Phase 3: Synthesis ({hours}h, Days 5-6)

**Objective:** Synthesize findings and create specification

### Day 5 (8h)
- [ ] Create workflow diagrams (2h) → `4-canvas/` (3-5 total)
- [ ] Map conceptual bridges (3h) → `5-analysis-connection/mapping-*.md`
- [ ] Write synthesis document (3h) → `4-artifacts/synthesis-{topic}.md`

### Day 6 (8h)
- [ ] Write SPECIFICATION.yaml (5h) → `6-outputs/SPECIFICATION.yaml`
- [ ] Write final literature review (2h) → `6-outputs/final-{topic}-review.md`
- [ ] Validate workbook (1h) → Run validation scripts

**Checkpoint B3:** SPECIFICATION.yaml complete (400+ lines), all validations pass

---

## Milestones

| Phase | End Date | Deliverable | Validation |
|-------|----------|-------------|------------|
| Phase 1 | Day 2 | 8+ sources, 4+ atomics | Checkpoint B1 |
| Phase 2 | Day 4 | 10+ atomics, 4+ themes, 5+ steps | Checkpoint B2 |
| Phase 3 | Day 6 | SPECIFICATION.yaml, literature review | Checkpoint B3 + all validations |
```

---

### 3. final-{topic}-literature-review.md (PRESERVED from v1)
**Purpose:** Final literature review integrating all findings

**Template:**
```markdown
---
title: "{Topic}: Literature Review"
author: "{Agent}"
date: "{ISO_DATE}"
spec:issue: "{SPEC_ISSUE}"
type: "Literature Review"
---

# {Topic}: Literature Review

## Executive Summary
{2-3 paragraph overview of findings}

## Introduction
### Background
{Why this research matters}

### Research Questions
{Reference 0-prompts/research-questions.md - P1-P7}

### Scope
{Reference 0-prompts/scope.md}

## Literature Review
### {Theme 1}
{Synthesis from 2-analysis/themes-{topic}.md}
{Cross-references to [[atomic-XXX]] concepts}

### {Theme 2}
{Another theme synthesized}

## Key Findings
### Finding 1: {Title}
{From 4-artifacts/synthesis-{topic}.md}

### Finding 2: {Title}
{Another key finding}

## Conceptual Framework
{Reference 4-canvas/concept-map.md}
{Discuss relationships between concepts}

## Integration with {Existing Framework}
{Reference 5-analysis-connection/mapping-{source}-to-{target}.md}

## Implications for ALEIA-MELQUISEDEC
### Architectural
{How findings affect architecture}

### Implementation
{Practical guidance}

## Future Research
{Open questions from 4-artifacts/}

## References
{All sources from 1-literature/ in APA/IEEE/Chicago format}
```

---

## Quality Criteria

### SPECIFICATION.yaml
- ✅ 400-600 lines (comprehensive)
- ✅ All required sections present
- ✅ All steps documented with procedures
- ✅ All concepts cross-referenced to 3-atomics/
- ✅ Dublin Core metadata complete
- ✅ Valid YAML syntax

### ROADMAP.md
- ✅ 3 phases defined
- ✅ Daily breakdown (Days 1-6)
- ✅ Clear deliverables per day
- ✅ 3 checkpoints (B1, B2, B3)
- ✅ Realistic time estimates

### Final Literature Review
- ✅ 2000-3000 words
- ✅ All research questions addressed
- ✅ 5+ themes synthesized
- ✅ 10+ atomics cross-referenced
- ✅ References section complete

## Validation Checklist

- [ ] **SPECIFICATION.yaml exists** (400-600 lines)
- [ ] **ROADMAP.md exists** (3 phases, 6 days, 3 checkpoints)
- [ ] **final-{topic}-literature-review.md exists** (2000-3000 words)
- [ ] **SPECIFICATION.yaml is valid** (run `yamllint SPECIFICATION.yaml`)
- [ ] **All cross-references work** (atomics, steps, themes, sources)
- [ ] **Dublin Core metadata complete** in SPECIFICATION.yaml
- [ ] **Validation criteria defined** in SPECIFICATION.yaml

---

**Maintained by:** SALOMON (Synthesis Lead) + ALMA (Publication)
**Last Updated:** 2026-01-11
