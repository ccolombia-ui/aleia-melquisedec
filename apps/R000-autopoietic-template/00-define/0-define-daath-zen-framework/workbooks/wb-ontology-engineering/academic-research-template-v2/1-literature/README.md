# 1-literature/ - Source Collection

## Purpose

This folder contains documentation of all academic sources collected during literature review: books, papers, standards, frameworks, and other references.

## File Organization

### By Source Type
- `books-{topic}.md`: Books on specific topics
- `papers-{topic}.md`: Academic papers grouped by theme
- `standards-{topic}.md`: ISO, W3C, IEEE standards
- `frameworks-{topic}.md`: Methodologies and frameworks

### By Individual Source
- `{author-year}-{title}.md`: Individual source document
- Example: `evans-2003-ddd.md`, `w3c-2012-owl2-primer.md`

## Source Documentation Template

```markdown
---
source_id: "SRC-{number}"
type: "{book|paper|standard|framework}"
title: "{Full Title}"
author: ["{Author 1}", "{Author 2}"]
year: {YYYY}
publisher: "{Publisher}"
url: "{URL if available}"
citation_style: "{APA|IEEE|Chicago}"
relevance: "{HIGH|MEDIUM|LOW}"
pages_of_interest: ["{page ranges}"]
---

# {Author Year}: {Title}

## Citation

**{Citation Style}:**
{Full citation}

## Summary

{2-3 paragraph summary of the work}

## Key Concepts

- **{Concept 1}**: {Brief description}
- **{Concept 2}**: {Brief description}
- **{Concept 3}**: {Brief description}

## Relevant Excerpts

### {Topic 1} (p. {page})

> {Quoted text from source}

**Analysis:** {Your interpretation or why this matters}

### {Topic 2} (p. {page})

> {Another quoted excerpt}

**Analysis:** {Your interpretation}

## Related Atomics

- [[atomic-001-{concept}]]: Extracts concept from this source
- [[atomic-005-{another-concept}]]: References this work

## Notes

{Your notes, questions, or critiques}
```

## Quality Criteria

- **8-10 sources minimum** for completeness
- **Primary sources** (standards, seminal papers) over secondary
- **Recent work** (last 5 years) alongside foundational classics
- **Diverse perspectives** (multiple authors, institutions)
- **Proper citations** (consistent style: APA, IEEE, or Chicago)
- **Page numbers** for all excerpts and quotes

## Validation Checklist

- [ ] At least 8 source documents
- [ ] Each source has complete metadata (author, year, title, citation)
- [ ] Each source includes summary (2-3 paragraphs)
- [ ] Key concepts listed for each source
- [ ] Relevant excerpts with page numbers
- [ ] Cross-references to atomics (3-atomics/)
- [ ] Consistent citation style (APA/IEEE/Chicago)

---

**Maintained by:** HYPATIA (Research Lead)
**Last Updated:** 2026-01-11
