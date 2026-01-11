# IMRAD Workbook Template

---
**Metadata (Dublin Core + Spec Extensions)**

```yaml
title: "{{TOPIC_NAME}}: IMRAD Research Synthesis"
creator: "{{AGENT_NAME}}"
date: "{{ISO_DATE}}"
description: "Structured research synthesis on {{TOPIC_NAME}} following the IMRAD methodology (Introduction, Methods, Results, And Discussion)"
subject: ["{{PRIMARY_SUBJECT}}", "{{SECONDARY_SUBJECT}}"]
language: "en"
format: "text/markdown"
publisher: "Aleia-Melquisedec Research Repository"
contributor: ["SALOMON (Synthesis Lead)", "{{ADDITIONAL_CONTRIBUTORS}}"]
spec:issue: "spec-000"
spec:owner: "SALOMON"
keter-doc:version: "1.0.0"
keter-doc:schema: "https://aleia-melquisedec.org/schemas/imrad/v1"
```

---

## Purpose

This workbook follows the **IMRAD methodology** for structured research synthesis. IMRAD stands for:

- **I**ntroduction: Context, problem statement, research questions
- **M**ethods: Methodology, data sources, analysis approach
- **R**esults: Findings, patterns, evidence
- **A**nd **D**iscussion: Interpretation, implications, limitations, conclusions

The workbook consists of 7 markdown files representing the complete research paper structure.

---

## File Structure

```
imrad-template/
├── README.md (this file)
├── 01-introduction.md
├── 02-literature-review.md
├── 03-methodology.md
├── 04-results.md
├── 05-discussion.md
├── 06-conclusion.md
└── 07-references.md
```

---

## How to Use This Template

### Step 1: Clone Template
```bash
# From tools/create-workbook.sh or manually:
cp -r templates/imrad-template/ workbooks/wb-{{TOPIC_SLUG}}/
```

### Step 2: Update Metadata
- Replace `{{TOPIC_NAME}}` with your research topic (e.g., "Daath-Zen Framework Design")
- Replace `{{AGENT_NAME}}` with agent identifier (e.g., "SALOMON")
- Replace `{{ISO_DATE}}` with current date (e.g., "2026-01-11")
- Update subjects, contributors, and spec:issue as needed

### Step 3: Follow IMRAD Workflow

**File 01: Introduction**
- **Context**: What is the background?
- **Problem**: What gap or challenge exists?
- **Research Questions**: What will this synthesis answer?
- **Scope**: What is included/excluded?

**File 02: Literature Review**
- **Existing Research**: What has been done?
- **Key Theories**: What frameworks apply?
- **Gaps**: What is missing or unclear?
- **Positioning**: How does this work fit?

**File 03: Methodology**
- **Data Sources**: Where did inputs come from? (e.g., atomics from HYPATIA)
- **Analysis Approach**: How were patterns identified?
- **Tools & Techniques**: What methods were used?
- **Validation**: How were findings verified?

**File 04: Results**
- **Patterns Identified**: What themes emerged?
- **Evidence**: What data supports findings?
- **Visualizations**: Diagrams, tables, charts
- **Key Findings**: What are the main discoveries?

**File 05: Discussion**
- **Interpretation**: What do results mean?
- **Implications**: What are practical applications?
- **Limitations**: What constraints exist?
- **Future Work**: What comes next?

**File 06: Conclusion**
- **Summary**: Recap key findings
- **Contributions**: What did this add?
- **Recommendations**: What should practitioners do?
- **Closing**: Final thoughts

**File 07: References**
- **Citations**: All sources in APA/IEEE/Chicago format
- **Sources**: Academic papers, books, frameworks, atomics
- **Links**: URLs to referenced documents

---

## Validation Checklist

Before completing this workbook, verify:

- [ ] **README.md**: All metadata fields populated (9 Dublin Core + 2 spec fields)
- [ ] **01-introduction.md**: Problem, research questions, scope defined
- [ ] **02-literature-review.md**: At least 5 sources cited
- [ ] **03-methodology.md**: Clear data sources and analysis approach
- [ ] **04-results.md**: Findings with evidence and visualizations
- [ ] **05-discussion.md**: Interpretation, implications, limitations
- [ ] **06-conclusion.md**: Summary, contributions, recommendations
- [ ] **07-references.md**: All sources properly cited
- [ ] **Cross-references**: Files link to each other and external sources
- [ ] **Section Headers**: Each file has proper H1/H2/H3 structure

Run validation:
```bash
python tools/validation/validate-imrad-structure.py workbooks/wb-{{TOPIC_SLUG}}/
python tools/validation/validate-metadata.py workbooks/wb-{{TOPIC_SLUG}}/README.md
```

---

## Success Criteria

- ✅ All 7 files present with structured content
- ✅ Research questions clearly defined in Introduction
- ✅ Methods transparently documented
- ✅ Results supported by evidence
- ✅ Discussion includes implications and limitations
- ✅ References complete and properly formatted
- ✅ All validations pass (0 errors)

---

## Agent Protocols

**SALOMON (Synthesis Lead)**:
- Primary owner of IMRAD workbooks
- Receives atomics from HYPATIA
- Synthesizes findings into structured research
- Creates all 7 files following IMRAD structure
- Ensures coherence across sections

**HYPATIA (Input Provider)**:
- Provides atomics as data source for Methods section
- May collaborate on Literature Review (File 02)
- Supplies citations for References (File 07)

**MORPHEUS (Validation)**:
- Validates file structure (all 7 files present)
- Checks metadata compliance
- Verifies section headers exist in each file
- Ensures cross-references are valid
- Generates validation report

**ALMA (Publication)**:
- Publishes approved synthesis to `_melquisedec/domain/markdown/`
- Creates Neo4j ingestion for Results and Conclusions
- Updates knowledge graph with synthesized concepts

---

## Section Templates

### 01-introduction.md
```markdown
# Introduction

## Context
[Provide background and motivation]

## Problem Statement
[What gap or challenge exists?]

## Research Questions
1. RQ1: [Question]
2. RQ2: [Question]

## Scope
- **In Scope**: [What is included]
- **Out of Scope**: [What is excluded]
```

### 03-methodology.md
```markdown
# Methodology

## Data Sources
- **Atomics**: Received from HYPATIA (workbook: wb-academic-research-xxx)
- **Literature**: References from 02-literature-review.md
- **Frameworks**: Existing models and patterns

## Analysis Approach
1. Thematic analysis of atomics
2. Pattern identification
3. Cross-source validation

## Tools & Techniques
- Pattern matching
- Concept mapping
- Synthesis matrices
```

### 04-results.md
```markdown
# Results

## Pattern 1: [Pattern Name]
**Evidence**: [Data supporting this pattern]
**Frequency**: [How often it appeared]
**Sources**: [References to atomics/literature]

## Visualization
[Mermaid diagram or table]

## Key Findings
1. Finding 1
2. Finding 2
```

---

## Related Documents

- [Academic Research Template](../academic-research-template/README.md)
- [Daath-Zen Design Template](../../manifest/templates-daath-zen/daath-zen-design.md)
- [Validation Tools Documentation](../../../tools/validation/README.md)
- [SPEC-000 Tasks](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/tasks.md)

---

**Template Version**: 1.0.0
**Last Updated**: 2026-01-11
**Maintained By**: MORPHEUS (Template Guardian)
