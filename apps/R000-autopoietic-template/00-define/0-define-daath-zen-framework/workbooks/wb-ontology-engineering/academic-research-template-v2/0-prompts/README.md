# 0-prompts/ - Initial Research Context

## Purpose

This folder contains the initial prompts, context, and scope definitions that initiated the academic research workbook. It documents **why** this research exists and **what questions** guide the investigation.

## Required Files

### 1. initial-research-prompt.md
Document the original research question and motivation:
- **Central Question**: The main research question driving this work
- **Context**: Why this research is needed (problem statement)
- **Motivation**: Real-world applications or theoretical importance
- **Objectives**: 3-5 primary objectives (what you aim to achieve)
- **Hypothesis**: Initial hypothesis or expected findings
- **Scope**: High-level boundaries (what's included/excluded)
- **Methodology**: Brief description of research approach

**Example:**
```markdown
# Initial Research Prompt: Ontology Engineering for Triple Persistence

## Central Question
How can ontology engineering methodologies provide formal foundation for knowledge management in Triple Persistence architecture?

## Context
The ALEIA-MELQUISEDEC system requires formal knowledge representation across three persistence layers (Neo4j, Redis, Elasticsearch). Current implementation lacks ontological rigor.

## Motivation
- Web Semantic standards (OWL 2, RDF) provide proven frameworks
- Neo4j knowledge graphs benefit from formal ontologies
- METHONTOLOGY and NeOn provide systematic approaches
```

### 2. research-questions.md
Document 5-7 specific, answerable research questions:
- **Question ID**: P1, P2, P3, etc. (for traceability)
- **Question Text**: Clear, specific question
- **Subquestions**: 2-3 more granular subquestions
- **Importance**: Why this question matters (CRÍTICA, ALTA, MEDIA)
- **Expected Hours**: Time estimate to answer this question
- **Sources Needed**: Types of sources required (standards, papers, books)

**Example:**
```markdown
# Research Questions

## P1: What are the foundational concepts of ontology engineering? [CRÍTICA]

**Subquestions:**
- P1.1: How is an "ontology" defined in the literature?
- P1.2: What are the core components (classes, properties, axioms)?
- P1.3: How do formal ontologies differ from taxonomies?

**Importance:** CRÍTICA - Foundation for all subsequent questions

**Expected Hours:** 6 hours

**Sources Needed:**
- ISO 25964-1:2011 (Thesauri and interoperability)
- Gruber 1993 (seminal definition)
- Noy & McGuinness 2001 (ontology development guide)
```

### 3. scope.md (optional but recommended)
Detailed scope boundaries:
- **In Scope**: Topics, methodologies, domains explicitly covered
- **Out of Scope**: Topics intentionally excluded
- **Assumptions**: Preconditions or givens
- **Constraints**: Limitations (time, resources, access)
- **Dependencies**: Prerequisites or related work
- **Success Criteria**: How to know when research is complete

**Example:**
```markdown
# Research Scope

## In Scope
- Ontology engineering methodologies (METHONTOLOGY, NeOn)
- OWL 2 standard (W3C Recommendation)
- Mapping ontologies to DDD patterns
- Neo4j integration patterns

## Out of Scope
- Full implementation of ontology editor
- Automated ontology learning from text
- Performance benchmarking of reasoners
- Non-graph persistence layers (relational DBs)

## Assumptions
- Reader has basic understanding of DDD
- Neo4j 5.x is target platform
- OWL 2 DL is the ontology language
```

## Tips for Effective Prompts

1. **Be Specific**: Avoid vague questions like "What is ontology?" → "How is ontology defined in ISO 25964-1:2011?"
2. **Prioritize Questions**: Mark as CRÍTICA/ALTA/MEDIA to guide research effort
3. **Estimate Time**: Realistic time estimates help with planning
4. **Define Success Early**: Clear criteria avoid scope creep
5. **Document Assumptions**: Make implicit knowledge explicit
6. **Link to Sources**: Reference specific standards or papers when known

## Relationship to Other Folders

- **→ 1-literature/**: Research questions guide source selection
- **→ 2-analysis/**: Questions define themes to analyze
- **→ 3-atomics/**: Questions determine which concepts to extract
- **→ 3-steps/**: Scope defines methodology steps needed
- **→ 6-outputs/SPECIFICATION.yaml**: Questions shape specification structure

## Validation Checklist

- [ ] `initial-research-prompt.md` exists with all required sections
- [ ] `research-questions.md` exists with 5-7 questions (IDs P1-P7)
- [ ] Each question has subquestions, importance, time estimate
- [ ] `scope.md` exists (optional but recommended for complex research)
- [ ] All questions are specific and answerable (not overly broad)
- [ ] Priorities assigned (CRÍTICA/ALTA/MEDIA)
- [ ] Total estimated hours is realistic (20-40 hours typical)

---

**Maintained by:** HYPATIA (Research Lead)
**Last Updated:** 2026-01-11
