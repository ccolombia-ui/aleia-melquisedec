# Methodology Workbook Template

## Purpose

This template provides a structured framework for researching and documenting a methodology. It's based on validated baseline patterns from ontology engineering and DDD methodologies.

## Structure

### 7-Folder Architecture

**0-prompts/** - Initial prompts, context, and scope definitions
- `prompt-initial.md` - Starting prompt that initiated the workbook
- `context.md` - Context and scope for the methodology research

**1-sources/** - Literature and knowledge sources
- Academic papers, books, standards documents
- Use proper citation format (APA recommended)

**2-extracts/** - Extracted concepts and patterns
- Key concepts from sources
- Patterns and principles identified
- Use atomic naming convention: `extract-{number}-{concept-name}.md`

**3-steps/** - Methodology steps and procedures
- Step-by-step breakdown of methodology execution
- Workflow definitions
- Use naming: `step-{number}-{action}.md`

**4-canvas/** - Visual models and diagrams
- Mermaid diagrams showing workflows
- Conceptual models (entity-relationship, class diagrams)
- Process flows

**5-analysis-connection/** - Integration analysis with other methodologies
- Cross-methodology concept mapping
- Equivalence matrices
- Semantic bridges between approaches

**6-outputs/** - Final deliverables
- `{methodology-name}-SPECIFICATION.yaml` - Complete specification
- `{methodology-name}-ROADMAP.md` - Execution roadmap
- `{methodology-name}-PROGRESS.md` - Progress tracking template

**tasks/** - Atomic task breakdown
- Individual task markdown files
- Follow DAATH-ZEN task format with Rostro, MCPs, Lesson

## Metadata Template

```yaml
---
# Dublin Core Metadata
dc:title: "{Methodology Name} Research Workbook"
dc:creator: "{Agent Name}"
dc:date: "{YYYY-MM-DD}"
dc:description: "Research workbook for {methodology name} methodology investigation"
dc:subject: "methodology, {domain}, {approach}"
dc:type: "Research Workbook"
dc:format: "text/markdown"
dc:identifier: "workbook-{methodology-id}"
dc:language: "en"

# Spec Workflow Fields
spec:issue: "SPEC-{number}"
spec:owner: "{Agent Name}"

# Keter-Doc Schema
keter-doc:version: "1.0.0"
keter-doc:schema: "https://keter-doc.org/schema/v1"
---
```

## Usage

### 1. Initialize Workbook

```bash
# Copy template
cp -r methodology-workbook/ workbooks/wb-{methodology-name}/

# Update README metadata
# Replace placeholders with actual values
```

### 2. Populate Folders

**Start with 0-prompts/**:
- Document initial research objectives
- Define scope boundaries
- Set success criteria

**Progress through 1-sources/**:
- Collect academic papers
- Document standards (ISO, IEEE)
- Gather practitioner books

**Extract to 2-extracts/**:
- Identify key concepts (10-15 atomics)
- Extract patterns and principles
- Use atomic naming convention

**Define 3-steps/**:
- Break methodology into executable steps
- Document prerequisites and deliverables per step
- Create workflow diagram in 4-canvas/

**Create 4-canvas/**:
- Visualize methodology workflow (Mermaid)
- Create concept maps
- Show relationships between concepts

**Analyze in 5-analysis-connection/**:
- Map concepts to other methodologies
- Create equivalence matrices
- Document semantic bridges

**Synthesize in 6-outputs/**:
- Create SPECIFICATION.yaml (full methodology spec)
- Create ROADMAP.md (execution plan)
- Create PROGRESS.md (tracking template)

### 3. Atomic Task Creation

In `tasks/` folder, create individual tasks:

```markdown
# Task {Number}: {Action} + {Object} + {Context}

- _Rostro: {ROSTRO-NAME}_
- _MCPs: base=[memory, neo4j] | specialized=[tool1, tool2]_
- _Lesson: lessons-learned/task-{number}-{name}.md_
- _Estimated: {hours} hours_
- _Priority: {HIGH|MEDIUM|LOW}_

## Description
{What needs to be done}

## Prerequisites
- {Dependency 1}
- {Dependency 2}

## Deliverables
- {Output 1}
- {Output 2}

## Validation
```bash
# Command to verify completion
```

## Success Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}
```

### 4. SPECIFICATION.yaml Structure

```yaml
metadata:
  title: "{Methodology Name}"
  version: "1.0.0"
  author: "{Agent}"
  date: "{YYYY-MM-DD}"
  spec_issue: "SPEC-{number}"

overview:
  purpose: "{Why this methodology exists}"
  scope: "{What it covers}"
  target_audience: "{Who uses it}"

foundation:
  theoretical_basis:
    - source: "{Author Year}"
      concept: "{Key concept}"
      extract: "2-extracts/extract-{number}-{concept}.md"

steps:
  - id: "step-001"
    name: "{Step name}"
    description: "{What happens}"
    inputs: ["{Input 1}", "{Input 2}"]
    outputs: ["{Output 1}", "{Output 2}"]
    duration: "{hours} hours"
    file: "3-steps/step-001-{name}.md"

validation:
  criteria:
    - id: "VAL-001"
      description: "{What to check}"
      method: "{How to check}"

implementation:
  prerequisites: ["{Prereq 1}", "{Prereq 2}"]
  estimated_duration: "{total} hours"
  phases:
    - phase: "1"
      steps: ["step-001", "step-002"]
      duration: "{hours} hours"
```

## Best Practices

### Atomic Extraction
- Each atomic should be self-contained
- Include source citation
- Provide examples
- Use consistent naming: `extract-{number}-{concept-name}.md`

### Step Documentation
- Clear prerequisites
- Explicit deliverables
- Validation criteria
- Estimated duration

### Canvas Creation
- Use Mermaid for diagrams
- Keep visualizations simple
- Show relationships clearly
- Include legends

### Progress Tracking
- Update PROGRESS.md regularly
- Note blockers and dependencies
- Document lessons learned
- Track actual vs estimated time

## Validation Checklist

Before completing workbook:

- [ ] All 7 folders populated with content
- [ ] SPECIFICATION.yaml complete with all sections
- [ ] ROADMAP.md created with execution plan
- [ ] PROGRESS.md template ready for tracking
- [ ] All atomics properly named and cited
- [ ] All steps documented with validation criteria
- [ ] Canvas visualizations created
- [ ] Analysis-connection documents cross-methodology mapping
- [ ] Tasks folder contains atomic task breakdown
- [ ] Metadata complete in all markdown files

## Examples

See validated baseline methodologies:
- `inputs/baseline/methologies/01-onotology-eng-meth/` - ISO 25964-1 + METHONTOLOGY (3 hrs, 512-line SPECIFICATION.yaml)
- `inputs/baseline/methologies/02-ddd-meth/` - Evans + Vernon DDD (4.8 hrs, 527-line SPECIFICATION.yaml)

## Notes

**Phase 1 vs Phase 2**:
- Phase 1 (Current): Manual workbook execution
- Phase 2 (Future): Automated sync to Neo4j + embeddings via sync-all.sh

**SPECIFICATION.yaml Role**:
Acts as extraction contract - defines exactly what to extract, preventing scope creep and ensuring completeness.

**Naming Conventions**:
- Atomics: `extract-{number}-{concept-name}.md`
- Steps: `step-{number}-{action}.md`
- Tasks: `task-{number}-{action}.md`
- Outputs: `{methodology-name}-{document-type}.{ext}`
