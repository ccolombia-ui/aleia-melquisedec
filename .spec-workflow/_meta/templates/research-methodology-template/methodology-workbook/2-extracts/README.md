# 2-extracts/ - Extracted Concepts and Patterns

## Purpose

This folder contains atomic concept extractions from the sources in `1-sources/`. Each extract should be self-contained, properly cited, and focused on a single concept or pattern.

## Naming Convention

Use format: `extract-{number}-{concept-name}.md`

Examples:
- `extract-001-bounded-context.md`
- `extract-002-ubiquitous-language.md`
- `extract-003-strategic-design.md`

## Extract Template

```markdown
---
id: extract-{number}
concept: "{Concept Name}"
source: "{Author Year}"
source_file: "1-sources/{filename}.md"
category: "{core|pattern|principle|practice}"
related: ["extract-{n}", "extract-{m}"]
---

# {Concept Name}

## Definition

{Clear, concise definition of the concept}

> "{Direct quote from source if available}"
>
> — {Author, Year, p. {page}}

## Context

{When/why this concept is used}

## Key Characteristics

- {Characteristic 1}
- {Characteristic 2}
- {Characteristic 3}

## Examples

### Example 1: {Scenario}
{Concrete example showing concept in practice}

### Example 2: {Scenario}
{Another example, preferably different domain}

## Related Concepts

- **{Related Concept 1}** (`extract-{n}`): {Relationship}
- **{Related Concept 2}** (`extract-{m}`): {Relationship}

## Practical Application

{How to apply this concept in practice}

## Common Pitfalls

- {Pitfall 1}: {How to avoid}
- {Pitfall 2}: {How to avoid}

## Further Reading

- {Source 1} - {Why relevant}
- {Source 2} - {Why relevant}

## Tags

`{tag1}` `{tag2}` `{tag3}`
```

## Categories

**core** - Fundamental concepts essential to methodology
**pattern** - Recurring solutions to common problems
**principle** - Guiding rules or best practices
**practice** - Concrete techniques or procedures

## Best Practices

1. **One concept per file** - Keep extracts atomic and focused
2. **Always cite source** - Traceability is critical
3. **Provide examples** - Abstract concepts need concrete illustrations
4. **Link related concepts** - Show connections between extracts
5. **Use consistent structure** - Follow template for all extracts
6. **Include quotes** - Direct quotes provide authority
7. **Tag appropriately** - Enable easy searching and filtering

## Target: 10-15 Extracts

Quality over quantity:
- 3-5 core concepts (foundational)
- 3-5 patterns (solutions)
- 2-3 principles (guidelines)
- 2-3 practices (techniques)

## Cross-Referencing

Extracts should reference:
- Source files in `1-sources/`
- Related extracts in `2-extracts/`
- Steps in `3-steps/` (where applicable)
- Canvas visualizations in `4-canvas/` (where depicted)

## Example Extract

```markdown
---
id: extract-001
concept: "Bounded Context"
source: "Evans 2003"
source_file: "1-sources/academic-papers/evans-2003-ddd-blue-book.md"
category: "core"
related: ["extract-002", "extract-005"]
---

# Bounded Context

## Definition

A bounded context is an explicit boundary within which a domain model is defined and applicable. Inside the boundary, all terms and phrases of the Ubiquitous Language have specific meaning, and the model reflects the language with precision.

> "Multiple models are in play on any large project. Yet when code based on distinct models is combined, software becomes buggy, unreliable, and difficult to understand."
>
> — Evans, 2003, p. 335

## Context

Used in strategic design to manage complexity in large software systems. Particularly important when multiple teams work on different parts of the system, or when integrating with external systems.

## Key Characteristics

- Explicit boundary definition
- Internal consistency of language
- Protection from external model corruption
- Clear ownership by single team
- Explicit translation at boundaries

... (continues)
```

## Validation

Before moving to 3-steps/:
- [ ] All extracts properly cited
- [ ] Each extract has examples
- [ ] Related concepts linked
- [ ] Consistent structure across all extracts
- [ ] Core concepts identified (mark with `category: core`)
