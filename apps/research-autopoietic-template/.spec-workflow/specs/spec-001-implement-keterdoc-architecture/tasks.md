# Tasks: spec-001-implement-keterdoc-architecture

## Phase 1: Foundations (REQ-001..REQ-010)

### REQ-001: Define YAML-LD @context Vocabulary
- [x] **Task 1.1**: Create `apps/research-autopoietic-template/.spec-workflow/context.jsonld`
    - [x] Define namespaces: `mel`, `dc`, `rdf`, `rdfs`, `xsd`
    - [x] Define term mappings: `seci`, `derives_from`, `informs`, etc.
    - [x] Define `artifact_template` and `lens` properties
    - [x] **Verification**: Validate JSON syntax
- [x] **Task 1.2**: Create online validation example (JSON-LD Playground)
    - [x] Create a snippet `examples/req-001-example.jsonld` (Created 3 artifacts instead)
    - [ ] Document validation steps in `Implementation Logs`
- [x] **Task 1.3**: Update Root Template with local @context reference
    - [x] Modify `_templates/daath-zen-patterns/template-configurable_daath-zen-root.md`
    - [x] Ensure `@context` points to the local file (for now) or URL

### REQ-002: Base Template & Generator
- [ ] **Task 2.1**: Refine `tools/generate_from_daath_template.py`
    - [ ] Implement argument parsing (FILE, ID, TITLE)
    - [ ] Implement Jinja2-like variable replacement or Regex replacement
    - [ ] Handle `result_type` mapping
- [ ] **Task 2.2**: Create `daath-zen-req-template.md` (Already done? Verify)
    - [ ] Ensure it uses the new `@context`
    - [ ] Validate inheritance from `template-configurable_daath-zen-root.md`

### REQ-003: Metadata Enrichment
- [ ] **Task 3.1**: Define "Metadata Quality" metrics
    - [ ] Add `quality_score` to frontmatter?
    - [ ] Check mapping to `associated_causes`

---

## Phase 2: Patterns & Tools (REQ-011..)
*To be expanded after Phase 1*
