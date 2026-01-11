# 3-steps/ - Methodology Steps

## Purpose

This folder contains step-by-step formalization of how to execute the methodology. Each step is documented with prerequisites, procedures, deliverables, and validation criteria, making the methodology repeatable and teachable.

## Naming Convention

**Format:** `step-{number}-{action-slug}.md`

**Examples:**
- `step-001-define-research-scope.md`
- `step-002-collect-academic-sources.md`
- `step-003-extract-atomic-concepts.md`
- `step-004-analyze-themes.md`
- `step-005-create-visualizations.md`
- `step-006-synthesize-findings.md`
- `step-007-write-specification.md`

## Step Template

```markdown
---
step_id: "{number}"
step_name: "{Action} + {Object} + {Context}"
order: {execution_order}
duration: "{hours} hours"
phase: "{Phase name}"
prerequisites:
  - "{prerequisite 1}"
  - "step-{n}"
deliverables:
  - "{output 1}"
  - "{output 2}"
validates:
  - "{validation criterion 1}"
related_concepts:
  - "atomic-{n}"
---

# Step {Number}: {Action} + {Object} + {Context}

## Purpose

{Why this step exists - what problem it solves or knowledge it creates. Be specific about the transformation that occurs.}

## Prerequisites

### Required Inputs
- **{Input 1}**: From `{location}` (e.g., `0-prompts/research-questions.md`)
- **{Input 2}**: From `{location}` or `{external source}`

### Required Knowledge
- Understanding of [[atomic-{n}-{concept}]] from `3-atomics/`
- Familiarity with {tool or technique}

### Required Tools
- **{Tool 1}**: {Purpose and installation if needed}
- **{Tool 2}**: {Purpose}

## Procedure

### 1. {Sub-task 1 Name}

{Detailed step-by-step instructions for first sub-task}

**Actions:**
1. {Action 1}
2. {Action 2}
3. {Action 3}

**Example:**
```bash
# Command if applicable
command --flag value
```

**Expected Output:** {What you should see or create}

---

### 2. {Sub-task 2 Name}

{Detailed instructions for second sub-task}

**Decision Point:**
- **IF** {condition}: THEN {action A}
- **ELSE**: {action B}

**Quality Check:** Verify that {criterion is met}

---

### 3. {Sub-task 3 Name}

{Instructions for third sub-task}

**Iteration:** Repeat until {completion condition}

---

## Deliverables

### 1. {Deliverable 1 Name}

- **Location**: `{path/to/file}`
- **Format**: {markdown|yaml|diagram|etc.}
- **Contents**: {Brief description of what it contains}
- **Size**: {Expected size - e.g., "300-500 lines", "5-8 pages"}

**Example:**
```markdown
# Example content structure
...
```

### 2. {Deliverable 2 Name}

- **Location**: `{path/to/file}`
- **Format**: {file type}
- **Contents**: {Description}

---

## Validation

### Success Criteria

- [ ] **{Criterion 1}**: {How to verify - e.g., "All 8 sources have complete citations"}
- [ ] **{Criterion 2}**: {How to verify}
- [ ] **{Criterion 3}**: {How to verify}

### Validation Commands

```powershell
# Command to verify deliverable 1
Test-Path "{deliverable-path}"

# Validate structure
python tools/validation/validate-{aspect}.py {file}
```

### Quality Metrics

- **Completeness**: {Percentage or count - e.g., "100% of research questions addressed"}
- **Accuracy**: {Metric - e.g., "0 broken cross-references"}
- **Consistency**: {Metric - e.g., "All citations in APA format"}

---

## Common Issues & Solutions

### Issue 1: {Problem Description}

**Symptom:** {What you observe}

**Cause:** {Why it happens}

**Solution:** {How to fix it}

### Issue 2: {Another Problem}

**Symptom:** {What you observe}

**Solution:** {How to fix}

---

## Workflow Integration

### Inputs from Previous Steps
- `step-{n}` provides `{output}` → used as `{input}` in this step

### Outputs to Next Steps
- This step produces `{output}` → consumed by `step-{m}` as `{input}`

### Parallel Work
- Can run in parallel with: `step-{x}`, `step-{y}`
- Must complete before: `step-{z}`

---

## Related Documentation

- **Concepts**: [[atomic-{n}-{concept}]], [[atomic-{m}-{another}]]
- **Visualizations**: `4-canvas/workflow-{aspect}.md`
- **Tasks**: `tasks/task-{step}.1-{subtask}.md` through `tasks/task-{step}.N-{subtask}.md`

---

## Agent Assignment

**Primary:** {Agent name} (e.g., HYPATIA, SALOMON)
**Support:** {Supporting agent if applicable}
**Validation:** MORPHEUS (always)

---

## Estimated Timeline

- **Minimum**: {hours} hours (with perfect focus)
- **Typical**: {hours} hours (with normal interruptions)
- **Maximum**: {hours} hours (if complex or new to methodology)

**Factors affecting duration:**
- {Factor 1}
- {Factor 2}
```

## Common Steps in Academic Research

### Step 001: Define Research Scope (2-3 hours)
- Input: Initial research idea
- Output: `0-prompts/initial-research-prompt.md`, `0-prompts/research-questions.md`, `0-prompts/scope.md`
- Purpose: Clarify research boundaries and questions

### Step 002: Collect Academic Sources (6-8 hours)
- Input: Research questions from Step 001
- Output: 8-10 source documents in `1-literature/`
- Purpose: Gather authoritative sources (books, papers, standards)

### Step 003: Extract Atomic Concepts (8-10 hours)
- Input: Sources from Step 002
- Output: 10-12 atomic files in `3-atomics/`
- Purpose: Distill sources into reusable knowledge units

### Step 004: Analyze Themes (6-8 hours)
- Input: Atomics from Step 003, sources from Step 002
- Output: 4-5 theme analyses in `2-analysis/`
- Purpose: Identify patterns across sources

### Step 005: Create Visualizations (4-6 hours)
- Input: Concepts from Step 003, themes from Step 004
- Output: 3-5 Mermaid diagrams in `4-canvas/`
- Purpose: Visualize relationships and workflows

### Step 006: Map Conceptual Bridges (3-4 hours)
- Input: Atomics from Step 003
- Output: Mapping documents in `5-analysis-connection/`
- Purpose: Connect this methodology to existing frameworks (e.g., DDD)

### Step 007: Synthesize Findings (4-6 hours)
- Input: All previous outputs
- Output: `4-artifacts/synthesis-{topic}.md`
- Purpose: Integrate all findings into coherent narrative

### Step 008: Write Specification (6-8 hours)
- Input: Synthesis from Step 007, steps from this folder
- Output: `6-outputs/SPECIFICATION.yaml`, `6-outputs/ROADMAP.md`
- Purpose: Formalize methodology as executable specification

## Validation Checklist

- [ ] At least 5-7 step documents exist
- [ ] Each step has:
  - [ ] Complete metadata (step_id, name, order, duration, prerequisites, deliverables)
  - [ ] Purpose section (why this step exists)
  - [ ] Prerequisites section (inputs, knowledge, tools)
  - [ ] Procedure section (detailed sub-tasks)
  - [ ] Deliverables section (outputs with locations)
  - [ ] Validation section (success criteria)
- [ ] Steps are sequenced logically (order field)
- [ ] All prerequisite references are valid
- [ ] All deliverable paths are correct
- [ ] Related atomics cross-referenced

---

**Maintained by:** HYPATIA (Research Lead) + SALOMON (Synthesis)
**Last Updated:** 2026-01-11
