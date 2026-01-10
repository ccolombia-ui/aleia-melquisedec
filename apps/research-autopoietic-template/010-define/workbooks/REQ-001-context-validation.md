---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/requirements/REQ-001-context-validation'
dc:title: 'REQ-001: Define YAML-LD @context Vocabulary'
dc:created: '2026-01-10'
version: '1.0.0'
status: 'draft'
result_type: 'immediate'  # This requirement produces an immediate artifact (context.jsonld)
associated_causes:
  - 'cause-001-knowledge-standardization'
associated_features:
  - 'feat-keterdoc-metadata'
outputs:
  immediate: 'context.jsonld (defines namespaces and mappings)'
  intermediate: 'KeterDoc frontmatter examples (used by templates)'
  final: 'Validated RDF triples and Neo4j nodes representing the context'
generated_from: '_templates/daath-zen-patterns/daath-zen-req-template.md'
template_root: '_templates/daath-zen-patterns/template-configurable_daath-zen-root.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'Context vocabulary and KeterDoc metadata required by all templates.'
---

# REQ-001: Define YAML-LD @context Vocabulary

**Priority**: Critical
**Type**: Architecture
**Effort**: 16 hours

## 1. Problem Statement

Current metadata usage across MELQUISEDEC artifacts is inconsistent: plain YAML without consistent context causes extraction and embedding inconsistencies. Defining a shared `context.jsonld` centralizes the vocabulary and enables consistent RDF/JSON-LD generation, embedding enrichment, and Neo4j ingestion.

## 2. Requirement Specification

### 2.1 Functional Requirements

FR-001.1: Create `context.jsonld` containing namespaces for `dc`, `seci`, `mel`, and KeterDoc fields: `id`, `is_a`, `version`, `permalink`.

FR-001.2: Provide 3 usage examples (Issue, Requirement, Lesson) showing YAML-LD frontmatter and JSON-LD expansion.

### 2.2 Non-Functional Requirements

NFR-001.1: `context.jsonld` must validate in JSON-LD Playground and produce consistent RDF triples.

NFR-001.2: Changes to the context require a MAJOR version bump following semver and documented migration notes.

## 3. Acceptance Criteria

- AC-001.1: `context.jsonld` exists in project root and contains required namespaces.
- AC-001.2: 3 example artifacts demonstrate correct usage and pass JSON-LD validation.
- AC-001.3: Neo4j ingestion script accepts RDF triples generated from context and creates expected nodes.

## 4. Implementation Guidance

1. Draft initial `context.jsonld` with namespaces: `dc`, `seci`, `mel`, `schema`.
2. Create examples: `_examples/issue-example.md`, `_examples/req-example.md`, `_examples/lesson-example.md` using YAML-LD frontmatter.
3. Add validation script `tools/validate-context-jsonld.py` (simple JSON-LD parse + expansion test).

## 5. Dependencies and Constraints

- Depends on: None (foundation requirement)
- Constraint: Use stable URIs for namespaces; choose `https://melquisedec.org/` prefix when possible.

## 6. Verification Plan

- Run `tools/validate-context-jsonld.py` → output: success
- Validate examples in JSON-LD Playground
- Import RDF triples to Neo4j test instance and confirm expected labels and properties

---

*Generated from daath-zen-req-template (configurable) and references template root for versioning and manifesto coherence.*
