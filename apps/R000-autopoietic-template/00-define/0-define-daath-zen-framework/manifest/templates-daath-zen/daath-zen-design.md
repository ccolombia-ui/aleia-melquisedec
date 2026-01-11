# DAATH-ZEN Template: Design Document

## Template Structure

This template defines the structure for design documents in the DAATH-ZEN methodology. It extends `daath-zen-base.md` with Architecture Decision Records (ADRs) and system component specifications.

---

## Sections

### 1. Overview
Brief summary of the design, scope, and key architectural decisions.

### 2. Architecture Decision Records (ADRs)
Each ADR documents a significant architectural decision using this format:

```markdown
### ADR-{NUMBER}: {Decision Title}

**Context**: What is the situation that requires a decision?

**Decision**: What architectural choice was made?

**Rationale**: Why was this decision made? What are the driving factors?

**Consequences**:
- ✅ **Pros**: Positive outcomes
- ❌ **Cons**: Negative outcomes or trade-offs
- 🔧 **Mitigations**: How cons are addressed

**Implementation**: Code example or configuration snippet

**References**: Links to requirements, external docs, or related ADRs
```

**Example**:
```markdown
### ADR-001: Use Markdown for Source of Truth

**Context**: Need a human-readable, version-controllable format for documentation.

**Decision**: Use Markdown files as primary source of truth for all documentation.

**Rationale**:
- Human-readable in plain text
- Git-friendly (line-based diffs)
- Universal tool support (editors, viewers, converters)
- Lightweight (no database required)

**Consequences**:
- ✅ **Pros**: Easy to edit, version control, no vendor lock-in
- ❌ **Cons**: No built-in relational queries, manual indexing required
- 🔧 **Mitigations**: Use frontmatter metadata + Neo4j for graph queries

**Implementation**:
\`\`\`yaml
---
# YAML frontmatter for structured metadata
dc:title: "My Document"
dc:date: "2026-01-11"
spec:issue: "SPEC-000"
---
\`\`\`

**References**: REQ-000-03 (Triple Persistence)
```

### 3. System Components Design
For each major component:

```markdown
### Component {NUMBER}: {Component Name}

**Purpose**: What this component does

**Design**: Architecture diagram (Mermaid), class structure, API contracts

**Validation Rules**: Quality gates and acceptance criteria

**References**: Related requirements and ADRs
```

### 4. Data Flow & Integration
- Mermaid diagrams showing data movement
- Integration points between components
- External system interfaces

### 5. Non-Functional Requirements Design
How each NFR is achieved:
- **Performance**: Caching strategies, parallel processing
- **Maintainability**: Modular design, clear APIs
- **Usability**: Error handling, clear messages
- **Scalability**: Growth strategies, bottleneck avoidance

### 6. Risk Analysis & Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {Risk description} | Low/Medium/High | Low/Medium/High | {Mitigation strategy} |

### 7. Testing Strategy
- Unit test approach and coverage targets
- Integration test scenarios
- Validation test cases

### 8. Traceability Matrix
| Requirement | Design Component | Validation |
|-------------|------------------|------------|
| REQ-{SPEC}-XX | ADR-YYY, Component Z | Test suite |

---

## Usage in Workbooks

### Academic Research Workbook
When researching design patterns, atomics should capture:
- Architectural patterns (layered, hexagonal, event-driven)
- Design principles (SOLID, DRY, KISS)
- ADR best practices

### IMRAD Workbook
When synthesizing design knowledge:
- **Introduction**: Design challenges and objectives
- **Literature Review**: Survey of architectural patterns and ADRs
- **Methodology**: Design process and decision-making approach
- **Results**: ADRs and component specifications
- **Discussion**: Trade-offs and design rationale
- **Conclusion**: Summary of architectural decisions
- **References**: Design patterns literature, ADR examples

---

## Metadata Requirements

All design documents MUST include:
- `spec:issue`: Spec ID
- `spec:owner`: Agent responsible
- Dublin Core fields (title, description, subject, date)
- Links to related requirements document

---

## References

- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) - Michael Nygard
- [C4 Model](https://c4model.com/) - System architecture diagrams
- [SPEC-000 Design](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/design.md)

---

**Template Version**: 1.0.0
**Last Updated**: 2026-01-11
**Owner**: MORPHEUS
