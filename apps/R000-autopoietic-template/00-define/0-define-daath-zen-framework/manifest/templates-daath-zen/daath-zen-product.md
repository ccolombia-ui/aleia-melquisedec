# DAATH-ZEN Template: Product Document

## Template Structure

This template defines the structure for product specification documents in the DAATH-ZEN methodology. It focuses on product vision, user stories, and feature specifications.

---

## Sections

### 1. Vision & Strategy

**Product Vision Statement**:
```markdown
For {target audience}
Who {statement of need or opportunity}
The {product name}
Is a {product category}
That {key benefit, reason to buy}
Unlike {primary competitive alternative}
Our product {statement of primary differentiation}
```

**Strategic Goals**:
- Goal 1: {Measurable objective}
- Goal 2: {Measurable objective}

### 2. User Stories & Use Cases

#### User Story Format
```markdown
#### US-{NUMBER}: {Story Title}

**As a** {user role}
**I want** {goal/desire}
**So that** {benefit/value}

**Acceptance Criteria**:
- Given {context}, when {action}, then {outcome}
- Given {context}, when {action}, then {outcome}

**Priority**: High/Medium/Low
**Effort**: S/M/L/XL
```

**Example**:
```markdown
#### US-001: Create Workbook from Template

**As a** Research Agent (HYPATIA/SALOMON)
**I want** to create a new workbook from a template
**So that** I can start investigation with proper structure

**Acceptance Criteria**:
- Given a template type (academic-research/imrad), when I run create-workbook.sh, then a new workbook is created with all required folders/files
- Given a topic name, when I create a workbook, then README.md is pre-populated with metadata

**Priority**: High
**Effort**: M (4 hours)
```

#### Use Case Format
```markdown
#### UC-{NUMBER}: {Use Case Title}

**Actor**: {Primary user}
**Preconditions**: {What must be true before}
**Main Flow**:
1. {Step 1}
2. {Step 2}
3. ...

**Alternative Flows**:
- {Alternative scenario}

**Postconditions**: {What is true after}
```

### 3. Feature Specifications

```markdown
#### Feature {NUMBER}: {Feature Name}

**Description**: {Brief overview}

**User Value**: {Why this matters to users}

**Requirements**: {Related REQ-XXX IDs}

**Mockups/Wireframes**: {Links or embedded images}

**Technical Notes**: {Implementation considerations}
```

### 4. Product Roadmap

```markdown
### Q1 2026
- Feature A (MVP)
- Feature B (Core)

### Q2 2026
- Feature C (Enhancement)
- Feature D (Scale)
```

### 5. Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| User Adoption | 100 active users | Analytics |
| Task Completion Rate | 90%+ | User surveys |
| Time to Value | < 1 hour | Onboarding tracking |

---

## Usage in Workbooks

### Academic Research Workbook
When researching product thinking, atomics should capture:
- User-centered design principles
- Product management frameworks (Lean, Jobs-to-be-Done)
- Prioritization techniques (RICE, MoSCoW)

### IMRAD Workbook
When synthesizing product knowledge:
- **Introduction**: Product management importance
- **Literature Review**: Survey of product methodologies
- **Methodology**: How user needs were identified
- **Results**: User stories and feature specifications
- **Discussion**: Prioritization rationale
- **Conclusion**: Product vision summary
- **References**: Product management literature

---

## Metadata Requirements

All product documents MUST include:
- `spec:issue`: Spec ID
- `spec:owner`: Agent responsible (typically SALOMON for product thinking)
- Dublin Core fields
- Links to requirements document (features → requirements mapping)

---

## References

- [User Story Mapping](https://www.jpattonassociates.com/user-story-mapping/) - Jeff Patton
- [Inspired: How to Create Tech Products Customers Love](https://www.svpg.com/inspired-how-to-create-products-customers-love/) - Marty Cagan
- [Jobs to be Done](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) - Clayton Christensen

---

**Template Version**: 1.0.0
**Last Updated**: 2026-01-11
**Owner**: MORPHEUS
