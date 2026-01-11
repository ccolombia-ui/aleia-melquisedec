# tasks/ - Atomic Task Breakdown

## Purpose

This folder contains individual atomic tasks that implement the methodology steps defined in `3-steps/`. Each task is self-contained, executable, and follows the DAATH-ZEN task format with Rostro, MCPs, and Lesson references.

## Relationship to Steps

**Steps** (in `3-steps/`) are high-level phases of methodology execution.
**Tasks** (in `tasks/`) are atomic, executable work items that implement steps.

Example:
- **Step 3-steps/step-002-extract-concepts.md** (8 hours, Phase 1)
  - Task tasks/task-3.1-identify-core-concepts.md (2 hours)
  - Task tasks/task-3.2-document-concept-definitions.md (3 hours)
  - Task tasks/task-3.3-create-examples.md (2 hours)
  - Task tasks/task-3.4-validate-extractions.md (1 hour)

## Naming Convention

Use format: `task-{step-number}.{task-number}-{action}.md`

Examples:
- `task-1.1-define-research-scope.md`
- `task-2.1-collect-academic-papers.md`
- `task-2.2-collect-standards-docs.md`
- `task-3.1-identify-core-concepts.md`

## DAATH-ZEN Task Format

```markdown
---
task_id: "{step}.{task}"
task_name: "{Action} + {Object} + {Context}"
step_reference: "3-steps/step-{number}-{action}.md"
estimated: "{hours} hours"
priority: "{HIGH|MEDIUM|LOW}"
dependencies: ["task-{x}.{y}", "task-{z}.{w}"]
---

# Task {Step}.{Task}: {Action} + {Object} + {Context}

- _Rostro: {ROSTRO-NAME}_
- _MCPs: base=[memory, neo4j] | specialized=[tool1, tool2]_
- _Lesson: lessons-learned/task-{step}-{task}-{name}.md_
- _Estimated: {hours} hours_
- _Priority: {HIGH|MEDIUM|LOW}_

## Description

{Clear description of what needs to be done - be specific and actionable}

## Prerequisites

**Required Knowledge:**
- Understanding of {concept from 2-extracts/}
- Familiarity with {tool or technique}

**Required Inputs:**
- {Input 1}: {Location or source}
- {Input 2}: {Location or source}

**Dependencies:**
- Task {x}.{y} must be complete
- {External resource} must be available

## Procedure

### 1. {Sub-task 1}

{Detailed step-by-step instructions}

```bash
# Example command if applicable
command --option value
```

**Expected Output:** {What you should see}

### 2. {Sub-task 2}

{More detailed instructions}

**Decision Point:** If {condition}, then {action A}, otherwise {action B}

### 3. {Sub-task 3}

{Final instructions}

## Deliverables

1. **{Deliverable 1}**
   - Location: `{path/to/file}`
   - Format: {markdown|yaml|diagram}
   - Contents: {Brief description}

2. **{Deliverable 2}**
   - Location: `{path/to/file}`
   - Format: {file type}
   - Contents: {Brief description}

## Validation

### Success Criteria

- [ ] {Criterion 1} - {How to verify}
- [ ] {Criterion 2} - {How to verify}
- [ ] {Criterion 3} - {How to verify}

### Validation Commands

```bash
# Verify deliverable 1
test-command {deliverable-1}

# Verify deliverable 2
validate-tool --check {deliverable-2}
```

### Expected Results

```
{Example output from validation}
```

## MCPs Used

**Base MCPs:**
- **memory**: Store concepts, patterns, progress
- **neo4j**: (Phase 2) Graph relationships between concepts

**Specialized MCPs:**
- **{tool1}**: {Why used}
- **{tool2}**: {Why used}

## Rostro Context

**{ROSTRO-NAME}** provides:
- {Capability 1}
- {Capability 2}
- {Relevant prior knowledge}

## Related

- **Step:** `3-steps/step-{number}-{action}.md`
- **Concepts:** `2-extracts/extract-{n}-{concept}.md`
- **Visualizations:** `4-canvas/{diagram}.md`
- **Lesson:** `lessons-learned/task-{step}-{task}-{name}.md`

## Time Estimate

- **Minimum:** {hours} hours (ideal conditions)
- **Expected:** {hours} hours (realistic)
- **Maximum:** {hours} hours (with complications)

## Common Issues

### Issue 1: {Problem}
**Symptoms:** {What you'll see}
**Cause:** {Why it happens}
**Solution:** {How to fix}

### Issue 2: {Problem}
**Symptoms:** {What you'll see}
**Cause:** {Why it happens}
**Solution:** {How to fix}

## Notes

{Any additional context, tips, or warnings}

## Lesson Learned

After completion, document in:
`lessons-learned/task-{step}-{task}-{name}.md`

Include:
- What went well
- What was challenging
- Time actual vs estimated
- Would do differently next time
```

## Rostro Assignments

Match tasks to appropriate Rostros based on capabilities:

**HYPATIA** (Research & Analysis):
- Literature collection tasks
- Concept extraction tasks
- Academic analysis tasks

**SALOMON** (Synthesis & Architecture):
- Framework design tasks
- Integration analysis tasks
- IMRAD documentation tasks

**MORPHEUS** (Validation & Structure):
- Validation tasks
- Structure verification tasks
- Cross-reference checking tasks

**ALMA** (Orchestration & Finalization):
- Publication tasks
- Final synthesis tasks
- Documentation compilation tasks

## MCP Selection

Choose MCPs based on task needs:

**Always Use:**
- `memory` - Track progress, concepts, context

**Phase 2 (Future):**
- `neo4j` - Graph relationships between concepts
- `embeddings` - Semantic search and retrieval

**Task-Specific:**
- `filesystem` - File operations (read, write, validate)
- `github` - Version control, collaboration
- `search` - Web research, paper discovery
- `validation` - Custom validators
- `diagram` - Mermaid rendering, visualization

## Best Practices

1. **Atomic tasks** - Each task completable in single session (1-4 hours)
2. **Clear dependencies** - Explicit prerequisites
3. **Concrete deliverables** - No vague "analyze X", specify "create analysis-X.md with 3 sections"
4. **Validation criteria** - How to know when done
5. **Time estimates** - Include min/expected/max
6. **MCPs appropriate** - Only list MCPs actually needed
7. **Rostro assigned** - Match capability to task needs
8. **Lessons tracked** - Every task has lesson-learned file path

## Task Granularity

**Too Coarse (Bad):**
```markdown
# Task 1: Complete Research
- Do all research (40 hours)
```

**Too Fine (Bad):**
```markdown
# Task 1.1: Open browser
# Task 1.2: Type URL
# Task 1.3: Click link
```

**Just Right (Good):**
```markdown
# Task 2.1: Collect academic papers on DDD (4 hours)
- Search Google Scholar for Evans 2003
- Search for bounded context papers
- Save 5-7 papers to 1-sources/
- Create summaries in markdown
```

## Example Task

```markdown
---
task_id: "2.1"
task_name: "Collect Academic Papers on Domain-Driven Design"
step_reference: "3-steps/step-002-literature-review.md"
estimated: "4 hours"
priority: "HIGH"
dependencies: ["task-1.1"]
---

# Task 2.1: Collect Academic Papers on Domain-Driven Design

- _Rostro: HYPATIA_
- _MCPs: base=[memory] | specialized=[search, filesystem]_
- _Lesson: lessons-learned/task-2-1-collect-ddd-papers.md_
- _Estimated: 4 hours_
- _Priority: HIGH_

## Description

Collect 5-7 academic papers on Domain-Driven Design (DDD) from Google Scholar, arXiv, and ACM Digital Library. Focus on papers covering bounded contexts, strategic design, and tactical patterns.

## Prerequisites

**Required Knowledge:**
- Basic understanding of DDD concepts
- Familiarity with academic search engines

**Required Inputs:**
- Access to Google Scholar
- Research scope from Task 1.1

**Dependencies:**
- Task 1.1 (research scope defined) must be complete

## Procedure

### 1. Search Primary Sources

Search for foundational papers:

```bash
# Google Scholar search
"Domain-Driven Design" "Eric Evans" 2003-2010

# Focus keywords
"bounded context" OR "ubiquitous language" OR "strategic design"
```

**Expected Output:** 10-15 candidate papers

### 2. Filter and Select

Criteria for selection:
- Peer-reviewed (conference or journal)
- Published 2003-present
- Cites Evans 2003 or Vernon 2013
- Discusses strategic or tactical DDD

**Target:** 5-7 papers

### 3. Download and Organize

For each paper:
1. Download PDF to `1-sources/academic-papers/`
2. Name: `{author-year}-{title-short}.pdf`
3. Create markdown summary: `{author-year}-{title-short}.md`

## Deliverables

1. **Papers Collection**
   - Location: `1-sources/academic-papers/`
   - Format: PDF + Markdown summaries
   - Contents: 5-7 papers with summaries

2. **References List**
   - Location: `1-sources/references.md`
   - Format: Markdown with APA citations
   - Contents: Full citations for all papers

## Validation

### Success Criteria

- [ ] 5-7 papers collected and saved
- [ ] Each paper has markdown summary
- [ ] All papers properly cited in references.md
- [ ] Papers cover DDD strategic and tactical patterns

### Validation Commands

```bash
# Count papers
find 1-sources/academic-papers/ -name "*.pdf" | wc -l
# Should be >= 5

# Check summaries exist
for pdf in 1-sources/academic-papers/*.pdf; do
  basename="${pdf%.pdf}"
  [ -f "${basename}.md" ] || echo "Missing summary: $pdf"
done
```

## MCPs Used

**Base MCPs:**
- **memory**: Store paper metadata, track progress

**Specialized MCPs:**
- **search**: Web search for papers, DOI lookup
- **filesystem**: Save PDFs, create summaries

## Rostro Context

**HYPATIA** provides:
- Academic research expertise
- Literature review skills
- Citation management knowledge

## Related

- **Step:** `3-steps/step-002-literature-review.md`
- **Next Task:** `task-2.2-collect-standards-docs.md`
- **Lesson:** `lessons-learned/task-2-1-collect-ddd-papers.md`

## Time Estimate

- **Minimum:** 3 hours (if papers easy to find)
- **Expected:** 4 hours (realistic)
- **Maximum:** 6 hours (if access issues)

## Common Issues

### Issue 1: Paywalls
**Symptoms:** Can't download paper
**Cause:** No institutional access
**Solution:** Try preprint servers (arXiv), ResearchGate, or contact authors

### Issue 2: Too Many Results
**Symptoms:** Overwhelmed with choices
**Cause:** Broad search terms
**Solution:** Focus on highly-cited papers (100+ citations) or recent surveys

## Notes

Prefer papers that:
- Provide practical examples
- Include case studies
- Offer critiques or extensions of DDD

Avoid papers that:
- Only mention DDD tangentially
- Are purely theoretical without examples
- Require extensive prerequisite knowledge

## Lesson Learned

After completion, document in:
`lessons-learned/task-2-1-collect-ddd-papers.md`
```

## Target: 10-15 Tasks

For methodology execution (40-80 hours):
- Phase 1: 3-5 tasks
- Phase 2: 4-6 tasks
- Phase 3: 2-4 tasks

## Validation

Before workbook complete:
- [ ] All steps from 3-steps/ broken into atomic tasks
- [ ] Each task 1-4 hours (not 8+)
- [ ] Rostro assigned appropriately
- [ ] MCPs listed for each task
- [ ] Lesson-learned path specified
- [ ] Dependencies explicit
- [ ] Deliverables concrete
- [ ] Validation criteria clear
