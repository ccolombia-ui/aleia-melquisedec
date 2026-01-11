# tasks/ - Atomic Task Breakdown

## Purpose

This folder contains atomic, executable tasks that implement methodology steps from `3-steps/`. Each task follows DAATH-ZEN format with Rostro, MCPs, and Lesson references.

## Relationship to Steps

**Steps** (`3-steps/`) are high-level methodology phases (6-8 hours each).
**Tasks** (`tasks/`) are atomic work items (1-3 hours each) that implement steps.

**Example:**
- **Step 3-steps/step-002-collect-sources.md** (8 hours)
  - Task `task-2.1-search-academic-papers.md` (2h)
  - Task `task-2.2-review-standards-docs.md` (2h)
  - Task `task-2.3-document-sources.md` (3h)
  - Task `task-2.4-validate-citations.md` (1h)

## Naming Convention

**Format:** `task-{step}.{task}-{action-slug}.md`

**Examples:**
- `task-1.1-define-research-scope.md`
- `task-2.1-search-academic-papers.md`
- `task-3.1-extract-core-concepts.md`
- `task-4.1-identify-major-themes.md`

## DAATH-ZEN Task Template

```markdown
---
task_id: "{step}.{task}"
task_name: "{Action} + {Object} + {Context}"
step_reference: "3-steps/step-{number}-{action}.md"
estimated: "{hours} hours"
priority: "{HIGH|MEDIUM|LOW}"
dependencies: ["task-{x}.{y}"]
---

# Task {Step}.{Task}: {Action} + {Object} + {Context}

- _Rostro: {AGENT_NAME}_
- _MCPs: base=[memory, neo4j] | specialized=[tool1, tool2]_
- _Lesson: _melquisedec/lessons/task-{step}-{task}-{name}.md_
- _Estimated: {hours} hours_
- _Priority: {HIGH|MEDIUM|LOW}_

## Description

{Clear, specific description of what needs to be done. Be actionable.}

## Prerequisites

### Required Knowledge
- Understanding of [[atomic-{n}-{concept}]] from `3-atomics/`
- Familiarity with {tool or technique}

### Required Inputs
- **{Input 1}**: From `{location}` (e.g., `0-prompts/research-questions.md`)
- **{Input 2}**: From {source}

### Dependencies
- ✅ Task {x}.{y} must be complete
- {External resource} must be available

## Procedure

### 1. {Sub-task 1}

{Detailed step-by-step instructions}

**Example:**
```bash
# Command if applicable
python tools/validation/validate.py
```

**Expected Output:** {What you should create}

---

### 2. {Sub-task 2}

{More instructions}

**Decision Point:**
- **IF** {condition}: THEN {action A}
- **ELSE**: {action B}

---

### 3. {Sub-task 3}

{Final instructions}

## Deliverables

### 1. {Deliverable 1}

- **Location**: `{path/to/file}`
- **Format**: {markdown|yaml|etc.}
- **Contents**: {Brief description}
- **Size**: {Expected size - e.g., "5-8 sources"}

**Quality Criteria:**
- [ ] {Criterion 1}
- [ ] {Criterion 2}

### 2. {Deliverable 2}

- **Location**: `{path}`
- **Format**: {type}
- **Contents**: {Description}

## Validation

### Success Criteria

- [ ] {Criterion 1} - {How to verify}
- [ ] {Criterion 2} - {How to verify}
- [ ] {Criterion 3} - {How to verify}

### Validation Commands

```powershell
# Verify deliverable exists
Test-Path "{deliverable-path}"

# Validate content
python tools/validation/validate-{aspect}.py {file}
```

## Next Steps

- **On Success**: Proceed to Task {step}.{next_task}
- **On Failure**: {What to do if validation fails}

## Related Documentation

- **Step**: `3-steps/step-{number}-{action}.md`
- **Concepts**: [[atomic-{n}]], [[atomic-{m}]]
- **Lesson**: `_melquisedec/lessons/task-{step}-{task}.md` (created after completion)
```

## Common Task Breakdown

### Step 001 (Define Scope) → 2-3 tasks
- `task-1.1-document-research-questions.md` (2h)
- `task-1.2-define-scope-boundaries.md` (1h)

### Step 002 (Collect Sources) → 4 tasks
- `task-2.1-search-academic-papers.md` (2h)
- `task-2.2-review-standards-docs.md` (2h)
- `task-2.3-document-sources.md` (3h)
- `task-2.4-validate-citations.md` (1h)

### Step 003 (Extract Atomics) → 3 tasks
- `task-3.1-identify-core-concepts.md` (3h)
- `task-3.2-document-concept-definitions.md` (4h)
- `task-3.3-create-concept-examples.md` (2h)

### Step 004 (Analyze Themes) → 3 tasks
- `task-4.1-identify-major-themes.md` (2h)
- `task-4.2-compare-across-sources.md` (3h)
- `task-4.3-synthesize-theme-patterns.md` (3h)

### Step 005 (Create Visualizations) → 3 tasks
- `task-5.1-create-concept-map.md` (2h)
- `task-5.2-create-workflow-diagram.md` (2h)
- `task-5.3-create-step-dependencies.md` (1h)

### Step 006 (Map Bridges) → 2 tasks
- `task-6.1-create-equivalence-matrix.md` (2h)
- `task-6.2-document-integration-patterns.md` (2h)

### Step 007 (Synthesize) → 1 task
- `task-7.1-write-synthesis-document.md` (5h)

### Step 008 (Write Specification) → 2 tasks
- `task-8.1-write-specification-yaml.md` (5h)
- `task-8.2-write-literature-review.md` (3h)

**Total:** ~20 tasks across 8 steps

## Quality Criteria

- **5-10 tasks minimum** for methodology implementation
- **1-3 hours per task** (atomic, executable)
- **DAATH-ZEN format** (Rostro, MCPs, Lesson)
- **Clear success criteria** per task
- **Cross-referenced** to steps and concepts

## Validation Checklist

- [ ] At least 5 task documents exist
- [ ] Each task has:
  - [ ] Complete metadata (task_id, name, step_reference, estimated, priority, dependencies)
  - [ ] DAATH-ZEN format (Rostro, MCPs, Lesson)
  - [ ] Description (clear and actionable)
  - [ ] Prerequisites (knowledge, inputs, dependencies)
  - [ ] Procedure (detailed sub-tasks)
  - [ ] Deliverables (outputs with locations)
  - [ ] Validation (success criteria)
- [ ] Tasks map to steps (every step has 1+ tasks)
- [ ] Task dependencies are valid
- [ ] Time estimates are realistic (1-3 hours each)

---

**Maintained by:** HYPATIA (Research Lead) + SALOMON (Synthesis)
**Last Updated:** 2026-01-11
