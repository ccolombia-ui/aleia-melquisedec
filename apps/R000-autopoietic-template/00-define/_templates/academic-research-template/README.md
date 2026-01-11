# Academic Research Workbook Template

---
**Metadata (Dublin Core + Spec Extensions)**

```yaml
title: "{{TOPIC_NAME}}: Academic Research Literature Review"
creator: "{{AGENT_NAME}}"
date: "{{ISO_DATE}}"
description: "Comprehensive academic literature review on {{TOPIC_NAME}} following the Academic Research methodology (5-folder structure)"
subject: ["{{PRIMARY_SUBJECT}}", "{{SECONDARY_SUBJECT}}"]
language: "en"
format: "text/markdown"
publisher: "Aleia-Melquisedec Research Repository"
contributor: ["HYPATIA (Research Lead)", "{{ADDITIONAL_CONTRIBUTORS}}"]
spec:issue: "spec-000"
spec:owner: "HYPATIA"
keter-doc:version: "1.0.0"
keter-doc:schema: "https://aleia-melquisedec.org/schemas/academic-research/v1"
```

---

## Purpose

This workbook follows the **Academic Research methodology** for systematic literature review. It consists of 5 folders:

1. **1-literature/**: Source collection and documentation
2. **2-analysis/**: Critical analysis of themes and patterns
3. **3-atomics/**: Atomic concept extraction
4. **4-artifacts/**: Synthesis and intermediate outputs
5. **6-outputs/**: Final deliverables and publications

---

## Folder Structure

```
academic-research-template/
├── README.md (this file)
├── 1-literature/
│   └── (source documents, papers, references)
├── 2-analysis/
│   └── (theme analysis, pattern identification)
├── 3-atomics/
│   └── (atomic concepts: atomic-001-{name}.md, atomic-002-{name}.md, ...)
├── 4-artifacts/
│   └── (synthesis documents, intermediate outputs)
└── 6-outputs/
    └── (final literature review, publications)
```

---

## How to Use This Template

### Step 1: Clone Template
```bash
# From tools/create-workbook.sh or manually:
cp -r templates/academic-research-template/ workbooks/wb-{{TOPIC_SLUG}}/
```

### Step 2: Update Metadata
- Replace `{{TOPIC_NAME}}` with your research topic (e.g., "Domain-Driven Design")
- Replace `{{AGENT_NAME}}` with agent identifier (e.g., "HYPATIA")
- Replace `{{ISO_DATE}}` with current date (e.g., "2026-01-11")
- Update subjects, contributors, and spec:issue as needed

### Step 3: Follow Research Workflow

**Day 1-2: Literature Collection (1-literature/)**
- Document academic sources: books, papers, frameworks
- Create one file per source or category
- Example: `1-literature/ddd-evans-2003.md`, `1-literature/books-strategic-design.md`
- Include proper citations (APA, IEEE, or Chicago style)

**Day 3-4: Critical Analysis (2-analysis/)**
- Identify recurring themes across sources
- Document patterns and anti-patterns
- Example: `2-analysis/themes-ddd.md`, `2-analysis/patterns-tactical.md`
- Cross-reference sources from 1-literature/

**Day 5-6: Atomic Extraction (3-atomics/)**
- Extract atomic concepts (indivisible knowledge units)
- Naming: `atomic-001-bounded-context.md`, `atomic-002-ubiquitous-language.md`
- Each atomic must include:
  - **Definition**: Clear, concise definition
  - **Source**: Citation from literature
  - **Examples**: 2-3 concrete examples
  - **Related**: Links to other atomics

**Day 7-8: Synthesis & Output (4-artifacts/ + 6-outputs/)**
- Synthesize findings in `4-artifacts/synthesis-{{TOPIC}}.md`
- Create final output in `6-outputs/final-{{TOPIC}}-literature-review.md`
- Ensure all atomics are cross-referenced
- Include comprehensive references section

---

## Validation Checklist

Before completing this workbook, verify:

- [ ] **README.md**: All metadata fields populated (9 Dublin Core + 2 spec fields)
- [ ] **1-literature/**: At least 8-10 sources documented
- [ ] **2-analysis/**: At least 4-5 themes analyzed
- [ ] **3-atomics/**: At least 8-10 atomics extracted (proper naming: `atomic-XXX-{title}.md`)
- [ ] **4-artifacts/**: Synthesis document present
- [ ] **6-outputs/**: Final literature review with citations
- [ ] **Cross-references**: Atomics link to sources and each other
- [ ] **Citations**: All sources properly cited (APA/IEEE/Chicago)

Run validation:
```bash
python tools/validation/validate-academic-research.py workbooks/wb-{{TOPIC_SLUG}}/
python tools/validation/validate-metadata.py workbooks/wb-{{TOPIC_SLUG}}/README.md
```

---

## Success Criteria

- ✅ 10+ academic sources documented
- ✅ 5+ themes identified and analyzed
- ✅ 10+ atomics extracted with proper structure
- ✅ Final synthesis integrates all findings
- ✅ All validations pass (0 errors)

---

## Agent Protocols

**HYPATIA (Research Lead)**:
- Primary owner of this workbook type
- Responsible for literature collection (Days 1-2)
- Executes critical analysis (Days 3-4)
- Extracts atomics (Days 5-6)
- Passes atomics to SALOMON for synthesis

**SALOMON (Synthesis)**:
- Receives atomics from HYPATIA
- Creates synthesis document (Day 7)
- Produces final output (Day 8)
- Ensures cross-references are complete

**MORPHEUS (Validation)**:
- Validates structure completeness
- Checks metadata compliance
- Verifies atomic naming convention
- Generates validation report

**ALMA (Publication)**:
- Publishes approved outputs to `_melquisedec/domain/markdown/`
- Creates Neo4j ingestion scripts
- Updates knowledge graph

---

## Example Atomics

**Good Atomic Naming:**
- ✅ `atomic-001-bounded-context.md`
- ✅ `atomic-002-ubiquitous-language.md`
- ✅ `atomic-010-aggregate-root.md`

**Bad Atomic Naming:**
- ❌ `atomic1.md` (no leading zeros)
- ❌ `concept-bounded-context.md` (wrong prefix)
- ❌ `atomic-001.md` (missing descriptive name)

---

## Related Documents

- [Daath-Zen Requirements Template](../../manifest/templates-daath-zen/daath-zen-requirements.md)
- [IMRAD Template](../imrad-template/README.md)
- [Validation Tools Documentation](../../../tools/validation/README.md)
- [SPEC-000 Tasks](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/tasks.md)

---

**Template Version**: 1.0.0
**Last Updated**: 2026-01-11
**Maintained By**: MORPHEUS (Template Guardian)
