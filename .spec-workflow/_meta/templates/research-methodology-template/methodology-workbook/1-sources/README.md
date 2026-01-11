# 1-sources/ - Literature and Knowledge Sources

## Purpose

This folder contains all literature and knowledge sources used in the methodology research. Sources should be properly cited and organized by type.

## Organization

### By Source Type

**academic-papers/** - Peer-reviewed papers
- Use format: `{author-year}-{title-short}.pdf` or `.md`
- Include full citation in markdown notes

**books/** - Reference books and chapters
- Use format: `{author-year}-{book-title}-chapter-{n}.md`
- Extract relevant chapter summaries

**standards/** - ISO, IEEE, or domain-specific standards
- Use format: `{standard-id}-{standard-name}.pdf` or `.md`
- Note: Standards are authoritative sources

**practitioner-guides/** - Industry guides, white papers
- Use format: `{org-year}-{guide-name}.pdf` or `.md`
- Useful for practical implementation patterns

**online-resources/** - Blogs, tutorials, documentation
- Use markdown format with URL in frontmatter
- Capture permanent URL in case of link rot

## Citation Format (APA Recommended)

```markdown
---
title: "{Paper Title}"
author: "{Author Name(s)}"
year: {YYYY}
source: "{Journal/Conference}"
url: "{DOI or URL}"
citation: "{Author, A. (Year). Title. Source, Volume(Issue), pages.}"
---

# Summary

{Your summary of key points}

# Key Concepts

- {Concept 1}: {Definition}
- {Concept 2}: {Definition}

# Relevance to Methodology

{Why this source matters for your research}

# Quotes and Extracts

> "{Direct quote from source}"
>
> — {Author, Year, p. {page}}

# Related Sources

- See also: {Other source}
- Contradicts: {Conflicting source}
- Extends: {Source this builds upon}
```

## Best Practices

1. **Always cite sources properly** - Track where concepts come from
2. **Organize by theme** - Create subfolders if >10 sources
3. **Extract as you read** - Don't just store PDFs, summarize key points
4. **Note relevance** - Explain why each source matters
5. **Track citations** - Maintain references.bib or similar for final outputs
6. **Primary sources first** - Prefer original papers over summaries
7. **Check currency** - Note if source is outdated or superseded

## Example Structure

```
1-sources/
├── academic-papers/
│   ├── evans-2003-ddd-blue-book.md
│   ├── sollaci-2004-imrad-structure.md
│   └── iso-25964-2011-thesauri.md
├── books/
│   ├── vernon-2013-implementing-ddd-chapter-02.md
│   └── gamma-1994-design-patterns-chapter-01.md
├── standards/
│   ├── ISO-15836-2009-dublin-core.md
│   └── IEEE-830-1998-srs-template.md
└── references.md (master citation list)
```

## Target: 8-12 Sources

Aim for diverse, authoritative sources:
- 2-3 foundational papers/books
- 1-2 standards documents
- 3-5 practitioner guides
- 2-3 recent papers (last 5 years)

Too few sources = shallow research
Too many sources = analysis paralysis

Balance depth with breadth.
