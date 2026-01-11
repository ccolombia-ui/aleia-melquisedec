# 3-atomics/ - Atomic Concept Extraction

## Purpose

This folder contains atomic concepts extracted from sources - indivisible knowledge units that form the building blocks of understanding. Each atomic is a self-contained concept with definition, source, examples, and relationships.

## Naming Convention

**Format:** `atomic-{number}-{concept-slug}.md`

**Rules:**
- Use 3-digit zero-padded numbers: `001`, `002`, `010`, `100`
- Use kebab-case for concept slugs: `bounded-context`, `ubiquitous-language`
- One concept per file (atomic = indivisible)

**Good Names:**
- ✅ `atomic-001-bounded-context.md`
- ✅ `atomic-002-ubiquitous-language.md`
- ✅ `atomic-010-aggregate-root.md`

**Bad Names:**
- ❌ `atomic1.md` (no leading zeros)
- ❌ `concept-bounded-context.md` (wrong prefix)
- ❌ `atomic-001.md` (missing descriptive slug)

## Atomic Template

```markdown
---
atomic_id: "atomic-{number}"
concept_name: "{Concept Name}"
category: "{core|supporting|advanced}"
source: "{Author Year}"
source_reference: "1-literature/{source-file}.md"
related_atomics: ["atomic-{x}", "atomic-{y}"]
---

# Atomic {Number}: {Concept Name}

## Definition

{Clear, concise definition from authoritative source. One paragraph maximum.}

**Source:** {Full citation with page number}

## Explanation

{2-3 paragraph elaboration explaining:
- What this concept means in simple terms
- Why it's important
- How it relates to broader context
}

## Examples

### Example 1: {Example Name}

{Concrete example demonstrating the concept}

**Context:** {Where this example applies}

### Example 2: {Another Example Name}

{Another concrete example}

**Context:** {Where this applies}

### Example 3: ALEIA-MELQUISEDEC Context

{How this concept applies to ALEIA-MELQUISEDEC system specifically}

**Application:** {Specific use case in our system}

## Properties / Characteristics

- **Property 1**: {Description}
- **Property 2**: {Description}
- **Property 3**: {Description}

## Related Concepts

- **[[atomic-{x}-{concept}]]**: {How they relate} (e.g., "is a type of", "contains", "depends on")
- **[[atomic-{y}-{another}]]**: {Relationship}
- **Opposite:** {Contrasting concept if applicable}

## Misconceptions

**❌ Common Mistake:** {What people often get wrong}

**✅ Correct Understanding:** {Clarification}

## References

**Primary:**
- {Full citation 1} - p. {page}

**Secondary:**
- {Full citation 2} - p. {page}
- {Full citation 3} - p. {page}

## Tags

`{tag1}` `{tag2}` `{tag3}` (for future search/filtering)
```

## Quality Criteria

- **10-12 atomics minimum** for completeness
- **150-300 words each** (concise but complete)
- **Source citations** with page numbers
- **2-3 examples** per atomic (including ALEIA-MELQUISEDEC context)
- **Cross-references** to related atomics
- **Clear definition** from authoritative source

## Atomic Categories

### Core Concepts
Foundational concepts essential to understanding the methodology.
**Examples:** Ontology, Class, Property, Axiom

### Supporting Concepts
Important concepts that build on core concepts.
**Examples:** Taxonomy, Reasoning, OWL Restriction

### Advanced Concepts
Specialized or complex concepts for deep understanding.
**Examples:** SWRL Rules, Description Logic, Open World Assumption

## Validation Checklist

- [ ] At least 10 atomics extracted
- [ ] Proper naming convention (`atomic-XXX-{concept}.md`)
- [ ] Each atomic 150-300 words
- [ ] Each atomic has:
  - [ ] Clear definition from source
  - [ ] 2-3 examples (including ALEIA context)
  - [ ] Source citation with page numbers
  - [ ] 2+ cross-references to related atomics
  - [ ] Category (core/supporting/advanced)
- [ ] No duplicate concepts (one per atomic)
- [ ] Cross-references use double brackets `[[atomic-XXX-name]]`

## Tips

1. **Extract, don't invent**: Definitions must come from authoritative sources
2. **Be atomic**: If a concept can be divided, it's not atomic yet
3. **Link abundantly**: Over-connect rather than under-connect
4. **Include ALEIA context**: Every atomic should have system-specific example
5. **Cite precisely**: Always include page numbers
6. **Use consistent terminology**: Match source terminology exactly

---

**Maintained by:** HYPATIA (Research Lead)
**Last Updated:** 2026-01-11
