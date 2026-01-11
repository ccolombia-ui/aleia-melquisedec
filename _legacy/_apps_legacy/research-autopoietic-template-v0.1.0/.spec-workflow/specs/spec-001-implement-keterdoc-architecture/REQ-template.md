---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  foaf: 'http://xmlns.com/foaf/0.1/'
'@type': 'TechArticle'
'@id': 'https://melquisedec.org/requirements/REQ-template'
dc:title: 'REQ-000: Requirements Template - Atomic Specification Pattern'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot (Claude Sonnet 4.5)'
dc:subject: ['Requirements Engineering', 'Modular Architecture', 'Zettelkasten', 'Atomic Documents']
version: '1.0.0'
status: 'template'
is_a: 'requirement-template'
---

# REQ-000: Requirements Template

> **Purpose:** Esta plantilla define la estructura estándar para documentar **UN requerimiento atómico**.
>
> **Principle:** Atomic Knowledge (≤300 líneas por documento)
> **Pattern:** Zettelkasten Hub-Note linking
> **Usage:** Cada REQ-XXX.md sigue esta estructura

---

## 📋 Metadata Section

```yaml
# Copy YAML-LD frontmatter above and customize:
'@id': 'https://melquisedec.org/requirements/REQ-XXX-your-requirement-slug'
dc:title: 'REQ-XXX: Your Requirement Title'
dc:created: 'YYYY-MM-DD'
dc:subject: ['category1', 'category2']  # e.g., ['Core Architecture', 'Validation']
status: 'draft | active | completed | deprecated'
priority: 'critical | high | medium | low'
```

### Linked Requirements

| Relation | REQ ID | Title | Reason |
|----------|--------|-------|--------|
| Depends On | REQ-001 | Context Validation | Prerequisite for... |
| Blocks | REQ-015 | Rollback Mechanisms | Must complete before... |
| Related | REQ-003 | Template Structure | Shares implementation with... |

---

## 1. Problem Statement

**What problem does this requirement solve?**

```
Template:
- Current State: [Describe what exists today]
- Pain Point: [What's broken/missing/inefficient]
- Impact: [Who's affected and how]
- Evidence: [Data/examples supporting the problem]
```

**Example:**

Current State: Los requerimientos se documentan monolíticamente en `requirements.md` (800+ líneas).

Pain Point: Imposible referenciar requerimientos específicos, dificulta revisión atómica, viola principio de modularidad.

Impact: Developers y reviewers deben leer documento completo para entender un solo requisito. Git diffs son confusos.

Evidence: Manifesto v4.0.0 línea 6123: "Cada requerimiento se documenta en archivo separado siguiendo Zettelkasten."

---

## 2. Requirement Specification

### 2.1 Functional Requirements

**FR-XXX.1:** [Primary capability]

```gherkin
GIVEN [precondition/context]
WHEN [action/trigger]
THEN [expected outcome]
```

**Example:**

FR-001.1: Atomic Requirement Creation

```gherkin
GIVEN a new requirement is identified
WHEN developer creates REQ-XXX.md from template
THEN file follows YAML-LD frontmatter + 6-section structure
AND file size ≤ 300 lines
AND requirements.md hub-note links to REQ-XXX.md
```

**FR-XXX.2:** [Secondary capability]

(Add more FR-XXX.X as needed, each with GIVEN-WHEN-THEN)

### 2.2 Non-Functional Requirements

**NFR-XXX.1:** [Quality attribute - Performance/Security/Usability]

```
Metric: [How to measure]
Target: [Acceptable threshold]
Critical: [Failure threshold]
```

**Example:**

NFR-001.1: Document Size Constraint

```
Metric: Line count in REQ-XXX.md
Target: 150-250 lines (optimal readability)
Critical: ≤ 300 lines (atomic principle)
```

**NFR-XXX.2:** [Another quality attribute]

---

## 3. Acceptance Criteria

**AC-XXX.1:** [Testable condition]

```
Test Method: [How to verify]
Pass Criteria: [Specific pass condition]
Fail Criteria: [Specific fail condition]
```

**Example:**

AC-001.1: YAML-LD Frontmatter Validation

```
Test Method: JSON-LD Playground validation + schema check
Pass Criteria:
  - Frontmatter parses as valid JSON-LD
  - Required fields present (@context, @type, @id, dc:title, dc:created)
  - @id follows URI pattern https://melquisedec.org/requirements/REQ-XXX
Fail Criteria:
  - YAML syntax errors
  - Missing required fields
  - Invalid @id URI
```

**AC-XXX.2:** [Another testable condition]

**AC-XXX.3:** [Another testable condition]

---

## 4. Implementation Guidance

### 4.1 Architecture Context

**Where does this fit in the system?**

```
Layer: [Presentation | Business Logic | Data | Infrastructure]
Component: [Specific component/module]
Pattern: [Design pattern applied]
```

**Example:**

```
Layer: Documentation Architecture
Component: requirements/workbooks/
Pattern: Zettelkasten + Hub-Note Linking
Integration: Obsidian vault, Neo4j knowledge graph
```

### 4.2 Technical Approach

**Recommended implementation strategy:**

```markdown
1. [Step 1 with technical detail]
   - Subtask A
   - Subtask B

2. [Step 2]
   - Subtask A

3. [Validation step]
```

**Example:**

1. Create REQ-XXX.md from template
   - Copy REQ-template.md
   - Update YAML-LD frontmatter (especially @id, dc:title, dc:created)
   - Fill 6 sections (Problem, Specification, Acceptance, Implementation, Dependencies, Verification)

2. Link from requirements.md hub-note
   - Add row to requirements table with ID, title, priority, status
   - Use relative path: `[REQ-XXX](workbooks/REQ-XXX-slug.md)`

3. Validate structure
   - Run `wc -l REQ-XXX.md` (check ≤300 lines)
   - Validate YAML-LD in JSON-LD Playground
   - Check all sections filled

### 4.3 Code Examples (if applicable)

```python
# Example pseudocode or actual implementation snippet
def validate_requirement_file(filepath):
    """Validate REQ-XXX.md follows template structure."""
    with open(filepath) as f:
        content = f.read()

    # Check YAML-LD frontmatter
    assert content.startswith('---\n')
    frontmatter = extract_frontmatter(content)
    assert '@context' in frontmatter
    assert '@id' in frontmatter

    # Check sections present
    required_sections = [
        '## 1. Problem Statement',
        '## 2. Requirement Specification',
        '## 3. Acceptance Criteria',
        '## 4. Implementation Guidance',
        '## 5. Dependencies and Constraints',
        '## 6. Verification Plan'
    ]
    for section in required_sections:
        assert section in content

    # Check atomic principle
    line_count = len(content.split('\n'))
    assert line_count <= 300, f"File exceeds 300 lines: {line_count}"
```

### 4.4 Files to Create/Modify

**New Files:**
```
- apps/research-autopoietic-template/010-define/workbooks/REQ-XXX-slug.md
```

**Modified Files:**
```
- apps/research-autopoietic-template/010-define/requirements.md (add link in table)
```

---

## 5. Dependencies and Constraints

### 5.1 Dependencies

**Requires (Must exist before implementing this requirement):**

| Type | Dependency | Reason |
|------|------------|--------|
| Document | requirements.md hub-note | Where to link from |
| Template | REQ-template.md | Structure to follow |
| Standard | KeterDoc YAML-LD | Metadata format |

**Example:**

| Type | Dependency | Reason |
|------|------------|--------|
| Document | requirements.md | Hub-note for linking |
| Standard | Manifesto v4.0.0 Section 9.1 | Defines atomic requirement pattern |
| Tool | Obsidian | For vault navigation |
| Tool | JSON-LD Playground | For frontmatter validation |

### 5.2 Constraints

**Technical Constraints:**

- ⚠️ File size ≤ 300 lines (Manifesto atomic principle)
- ⚠️ YAML-LD frontmatter must validate as JSON-LD
- ⚠️ @id must be globally unique URI

**Business Constraints:**

- ⏱️ Time: [If time-bound]
- 💰 Cost: [If cost-bound]
- 🔒 Security: [If security-critical]

**Example:**

Technical:
- ⚠️ Obsidian must render frontmatter + Markdown correctly
- ⚠️ @id URI must resolve if published

Business:
- ⏱️ Template must be usable within 15 minutes (developer efficiency)

### 5.3 Assumptions

**We assume:**

- [ ] Assumption 1 (with validation plan)
- [ ] Assumption 2

**Example:**

- [x] Developers have Obsidian installed (validated: onboarding checklist)
- [x] JSON-LD Playground accessible (validated: https://json-ld.org/playground/)
- [ ] Neo4j knowledge graph exists (TODO: Phase 3 implementation)

---

## 6. Verification Plan

### 6.1 Test Cases

**TC-XXX.1:** [Test case name]

```gherkin
GIVEN [test precondition]
WHEN [test action]
THEN [expected result]
```

**Example:**

TC-001.1: Create Valid Atomic Requirement

```gherkin
GIVEN REQ-template.md exists
WHEN developer copies to REQ-042-example.md
  AND updates YAML-LD frontmatter
  AND fills all 6 sections
THEN file validates against schema
  AND line count ≤ 300
  AND requirements.md links correctly
```

**TC-XXX.2:** [Another test case]

### 6.2 Validation Checklist

**Manual Verification:**

- [ ] YAML-LD frontmatter parses (JSON-LD Playground: pass)
- [ ] All required fields present (@context, @id, dc:title, dc:created)
- [ ] File size ≤ 300 lines (`wc -l`)
- [ ] All 6 sections filled with content (not just headings)
- [ ] Linked from requirements.md hub-note
- [ ] Obsidian renders correctly (no broken links)
- [ ] Git commit follows convention (`feat(requirements): add REQ-XXX`)

**Automated Verification (if tools exist):**

```bash
# Validation script example
./tools/validate-requirement.sh REQ-XXX-slug.md
# Checks:
# - YAML-LD syntax
# - Required sections
# - Line count
# - @id uniqueness
```

### 6.3 Success Metrics

**How do we know this requirement is successfully implemented?**

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| File Size | ≤ 300 lines | `wc -l REQ-XXX.md` |
| Frontmatter Validity | 100% pass | JSON-LD Playground |
| Section Completeness | 6/6 sections filled | Manual review |
| Link Integrity | 0 broken links | Obsidian graph view |
| Time to Create | ≤ 30 minutes | Developer survey |

---

## 7. Additional Notes

### 7.1 Design Decisions

**Why this approach over alternatives?**

**Alternative Considered:** Keep monolithic requirements.md

**Rejected Because:**
- Violates atomic principle (≤300 lines)
- No individual requirement addressability
- Git diffs confusing
- Review friction (must read entire file)

**Chosen Approach:** Atomic REQ-XXX.md files

**Benefits:**
- Individual addressability (deep links)
- Clear Git history per requirement
- Zettelkasten linking
- Parallel development (no merge conflicts)

### 7.2 Open Questions

**Unresolved issues:**

- ❓ Question 1: [Issue that needs clarification]
  - **Decision Needed By:** YYYY-MM-DD
  - **Blocking:** [What this blocks]

**Example:**

- ❓ Should REQ-XXX.md live in `010-define/workbooks/` or `010-define/requirements/`?
  - **Decision Needed By:** 2026-01-11
  - **Blocking:** Directory structure standardization
  - **Current Assumption:** `workbooks/` (aligned with Zettelkasten pattern)

### 7.3 References

**Related Documents:**

- [Manifesto v4.0.0 Section 9.1: Templates Estructura de Documentos](../../../docs/manifiesto/04-implementacion/02-templates-estructura.md)
- [ADR-004: Modular Requirements Architecture](#) (to be created)
- [requirements.md](../requirements.md) (hub-note)

**External Resources:**

- [Zettelkasten Method](https://zettelkasten.de/introduction/)
- [JSON-LD Playground](https://json-ld.org/playground/)
- [Schema.org Vocabulary](https://schema.org/)
- [Dublin Core Metadata](https://www.dublincore.org/specifications/dublin-core/)

---

## Template Usage Instructions

**To create a new atomic requirement:**

1. Copy this file: `cp REQ-template.md REQ-XXX-your-slug.md`
2. Update YAML-LD frontmatter:
   - Change `@id` to `https://melquisedec.org/requirements/REQ-XXX-your-slug`
   - Update `dc:title` to actual requirement title
   - Set `dc:created` to today's date
   - Update `dc:subject` with relevant tags
   - Change `status` to `draft`
3. Fill all 6 sections with content
4. Validate: Run `wc -l REQ-XXX-your-slug.md` (must be ≤300 lines)
5. Link from `requirements.md` hub-note
6. Commit: `git add REQ-XXX-your-slug.md && git commit -m "feat(requirements): add REQ-XXX"`

**Section Guidelines:**

- **Section 1 (Problem):** Keep to 50-80 lines (context + evidence)
- **Section 2 (Specification):** Keep to 80-120 lines (FR + NFR)
- **Section 3 (Acceptance):** Keep to 40-60 lines (3-5 criteria)
- **Section 4 (Implementation):** Keep to 60-80 lines (guidance + examples)
- **Section 5 (Dependencies):** Keep to 30-40 lines (table format)
- **Section 6 (Verification):** Keep to 40-60 lines (test cases + checklist)

Total: ~300 lines (includes frontmatter + sections)

---

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-01-10 | GitHub Copilot | Initial template creation |

---

**License:** GPL-3.0 (same as MELQUISEDEC project)
**Maintained By:** core-mcp team
**Last Review:** 2026-01-10
