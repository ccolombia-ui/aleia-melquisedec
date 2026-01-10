# Lesson 001: KeterDoc Architecture Implementation Gap

```yaml
---
# Lesson Metadata (Following manifesto/02-arquitectura/05-autopoiesis-system.md)
id: "lesson-001-keterdoc-architecture-gap"
session_id: "session-001-keterdoc-gap-analysis"
domain_id: "domain-melquisedec-architecture"
rostro: "SALOMON"  # Equilibrio - Analyzed trade-offs
confidence: 0.95
status: "validated"
applies_to: "research-autopoietic-template"
date_extracted: "2026-01-10"
validated_in_sessions: []  # Will be populated as more projects use this

# KeterDoc/HKM Standard
'@context': 'https://melquisedec.org/context/v1'
'@type': 'Lesson'
'@id': 'https://melquisedec.org/lessons/lesson-001-keterdoc-gap'

is_a: 'lesson'
version: '1.0.0'

dc:
  title: 'KeterDoc Architecture Implementation Gap'
  creator: ['MELQUISEDEC', 'HYPATIA', 'SALOMON']
  date: '2026-01-10'
  subject: ['architecture', 'metadata', 'templates', 'yaml-ld', 'keterdoc']
  source:
    - 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    - 'docs/manifiesto/02-arquitectura/04-sincronizacion-knowledge.md'
    - 'docs/manifiesto/02-arquitectura/05-autopoiesis-system.md'

seci:
  derives_from:
    - '../chatlog/session-001-keterdoc-gap-analysis/full-transcript.md'
  informs:
    - '../../.spec-workflow/specs/spec-001-implement-keterdoc-architecture/'
---
```

---

## Executive Summary

**Problem**: 3212 lines of manifesto documentation define KeterDoc/HKM metadata standard, template-per-artifact system, and YAML-LD integration, but **NONE of it is implemented** in current `research-autopoietic-template`.

**Impact**: Critical architectural misalignment causing:
- No traceability (missing SECI model)
- No semantic web integration (missing YAML-LD)
- No artifact-specific guidance (missing templates)
- Incompatibility with documented tools (Obsidian, spec-workflow-mcp use MD, we use YAML)

**Solution**: Systematic 7-phase migration to align implementation with documented architecture.

**Confidence**: 0.95 (very high - based on extensive documentation reading)

---

## Context

### The Question That Started It All

User asked: **"¿LOS YAML QUE USAMOS SON YAML-LD?"**

This innocent question revealed a fundamental architecture gap: we're using simple YAML when manifesto specifies YAML-LD for semantic web integration.

### The Discovery

Deeper investigation uncovered that **5 foundational architectural components** documented in manifesto are completely missing from implementation:

1. KeterDoc/HKM metadata standard
2. Template-per-artifact system
3. Lens-specific template variants
4. YAML-LD semantic web integration
5. Workflow-pattern configuration

---

## The 5 Critical Gaps

### Gap 1: KeterDoc/HKM Metadata Standard NOT Implemented

**What Manifesto Defines** (templates-hkm.md, 575 lines):

```yaml
---
# Required Fields
id: "unique-identifier"
is_a: "artifact-type"  # concept|analysis|decision|output
version: "X.Y.Z"

# Dublin Core (dc) - Standard metadata
dc:
  title: "Human-readable title"
  creator: ["HYPATIA", "SALOMON"]
  date: "2026-01-10"
  subject: ["tag1", "tag2"]
  source: ["https://...", "DOI:..."]

# SECI Model (seci) - Traceability
seci:
  derives_from: ["../source1.md", "../source2.md"]
  informs: ["../derivative1.md"]
---
```

**Current Implementation**:

```yaml
problem: "..."
gap: "..."
goal: "..."
outcomes: ["..."]
```

**Consequences**:
- ❌ No traceability: Can't track "concept X derived from paper Y"
- ❌ No categorization: Can't filter by artifact type (is_a)
- ❌ No versioning: Can't track artifact evolution
- ❌ No standard metadata: Can't query by creator, date, subject

**Root Cause**: Templates created without implementing HKM documentation.

---

### Gap 2: Template-per-Artifact System Missing

**What Manifesto Specifies**:

Each artifact type needs specific template:
- `0-inbox/`: issue-tpl.md, task-tpl.md, dependency-tpl.md
- `1-literature/`: paper-tpl.md, book-tpl.md, article-tpl.md
- `2-atomic/`: concept-tpl.md, definition-tpl.md, question-tpl.md
- `3-workbook/`: analysis-tpl.md, decision-tpl.md, experiment-tpl.md
- `4-dataset/`: template-tpl.md, schema-tpl.md, diagram-tpl.md
- `5-outputs/`: output-tpl.md, deliverable-tpl.md

**Total**: 28+ artifact-specific templates

**Current Reality**:
- `template-base.yaml` with generic variables `{type}`, `{number}`, `{name}`
- No artifact-specific structure
- No validation of required sections per artifact type

**Consequences**:
- ❌ Ambiguity: "What should a concept include?"
- ❌ Inconsistency: Each developer invents structure
- ❌ No enforcement: Can't validate artifact completeness

**Root Cause**: Template system not aligned with artifact taxonomy.

---

### Gap 3: Lens-Specific Template Variants Missing

**What Manifesto Implies**:

Templates should vary by research lens (paradigm):

| Lens | Concept Template Focus | Analysis Template Focus |
|------|------------------------|-------------------------|
| **DSR** | Artifact construction | Build vs buy trade-offs |
| **IMRAD** | Literature concepts | Paper structure sections |
| **DDD** | Domain concepts | Bounded context analysis |
| **Social** | Stakeholder concepts | Journey maps |

**Example**: `concept-dsr-tpl.md` ≠ `concept-imrad-tpl.md`

**Current Reality**:
- No lens differentiation
- Same template structure for all paradigms
- No guidance on paradigm-specific artifacts

**Consequences**:
- ❌ Inappropriate structure: DSR research using IMRAD paper template
- ❌ Missing guidance: "How does concept differ in DDD vs Social?"
- ❌ No paradigm alignment: Can't enforce lens-appropriate artifacts

**Root Cause**: Lens system not integrated with template system.

---

### Gap 4: YAML-LD NOT Used (Semantic Web Missing)

**What Manifesto References**:

Semantic web integration for Neo4j via RDF triples.

**Should Have**:

```yaml
'@context': 'https://melquisedec.org/context/v1'
'@type': 'Concept'
'@id': 'https://melquisedec.org/concepts/concept-001'

id: 'concept-001'
# ... rest of metadata
```

**Current Reality**:
- Simple YAML without `@context`, `@type`, `@id`
- No namespace definition
- No semantic web features

**Consequences**:
- ❌ Harder Neo4j integration: Manual Cypher instead of RDF import
- ❌ No linked data: Can't reference artifacts via URIs
- ❌ No ontology: Can't leverage semantic web tools
- ❌ No standard vocabularies: Reinventing metadata schemes

**Root Cause**: YAML-LD standard not adopted in template design.

---

### Gap 5: Workflow-Pattern Configuration Missing

**What User Requested**:

> "yaml debería incluir referencia a la plantilla de artefacto, workflow-pattern configurable para lograr este artefacto"

**Should Have**:

```yaml
artifact_template: '../artifact-templates/concept-tpl.md'
workflow_pattern: 'PATTERN-002-atomic-synthesis'
lens: 'DSR'
```

**Current Reality**:
- No `artifact_template` field (can't reference which template was used)
- No `workflow_pattern` field (can't configure process per artifact)
- No lens field (can't specify paradigm)

**Consequences**:
- ❌ No traceability: Can't track "which template generated this?"
- ❌ No configurability: Can't choose workflow per artifact type
- ❌ No autopoiesis: Can't learn "which patterns work for concept creation?"

**Root Cause**: Workflow-pattern system not integrated with artifact metadata.

---

## Why This Matters: Impact Analysis

### Immediate Impact (Technical Debt)

| Area | Impact | Severity |
|------|--------|----------|
| **Traceability** | Can't track artifact lineage (seci) | HIGH |
| **Semantic Search** | Can't query by metadata (dc) | HIGH |
| **Template Consistency** | Each developer invents structure | MEDIUM |
| **Neo4j Integration** | Manual Cypher instead of RDF | MEDIUM |
| **Tool Compatibility** | YAML vs MD (Obsidian, spec-workflow-mcp) | HIGH |

### Long-term Impact (Architectural)

| Area | Impact | Severity |
|------|--------|----------|
| **Autopoiesis** | Can't measure pattern effectiveness | CRITICAL |
| **Scalability** | Can't standardize cross-projects | HIGH |
| **Knowledge Management** | Can't leverage semantic web | HIGH |
| **Paradigm Support** | Can't properly support DSR vs IMRAD | MEDIUM |

---

## Solution Applied

### Architectural Decision: MD with YAML-LD Frontmatter

**Format**:

```markdown
---
# YAML-LD frontmatter (machine-processable)
'@context': 'https://melquisedec.org/context/v1'
'@type': 'ResearchIssue'
id: 'research-neo4j-001'
is_a: 'research-issue'
artifact_template: 'research-issue-tpl.md'
workflow_pattern: 'PATTERN-007-Problem-RBM-GAC'
lens: 'DSR'
dc:
  title: '...'
seci:
  derives_from: []
---

# Research: Neo4j Performance

[Markdown body - human-readable]
```

**Advantages**:
- ✅ Compatible Obsidian (MD + YAML frontmatter)
- ✅ Compatible spec-workflow-mcp (MD files)
- ✅ Human-readable body (Markdown)
- ✅ Machine-processable metadata (YAML-LD)
- ✅ Semantic web ready (@context, @type, @id)
- ✅ Can include diagrams (Mermaid inline)

---

## Migration Strategy: 7 Phases

### Phase 1: Fundamentos (Week 1-2)
**Goal**: Establish semantic web foundation

- [ ] Define @context YAML-LD vocabulary
- [ ] Create context.jsonld in project root
- [ ] Validate with JSON-LD playground
- [ ] Create 6 base templates (concept, analysis, decision, experiment, output, lesson)

**Deliverable**: `context.jsonld` + `artifact-templates/by-type/` (6 files)

---

### Phase 2: Lens Integration (Week 3-4)
**Goal**: Paradigm-specific template variants

- [ ] Create artifact-templates/by-lens/ structure
- [ ] 4 lenses × 6 templates = 24 files
- [ ] Document differences: DSR vs IMRAD vs DDD vs Social
- [ ] Example content for each lens variant

**Deliverable**: `artifact-templates/by-lens/` (24 files + README)

---

### Phase 3: Workflow-Pattern System (Week 5)
**Goal**: Configurable workflows per artifact

- [ ] Define artifact-workflows.yaml mapping
- [ ] Create 10 PATTERN-*.yaml files
- [ ] Include: steps, validation_criteria, confidence_score, lens_applicability
- [ ] Document pattern evolution (autopoiesis)

**Deliverable**: `config/artifact-workflows.yaml` + `patterns/` (10 files)

---

### Phase 4: Migration Tools (Week 6)
**Goal**: Automated conversion

- [ ] Script: convert-issue-yaml-to-md.py
- [ ] Script: generate-artifact-from-template.py
- [ ] Script: validate-keterdoc-compliance.py
- [ ] Validation: frontmatter is valid YAML-LD + KeterDoc

**Deliverable**: `tools/keterdoc/` (3 scripts + tests)

---

### Phase 5: Neo4j Integration (Week 7)
**Goal**: Semantic web triple generation

- [ ] Script: yaml-ld-to-rdf-triples.py
- [ ] Import triples to Neo4j via Cypher
- [ ] Test semantic queries (SPARQL-like)
- [ ] Validate relationships (seci.derives_from → Neo4j edges)

**Deliverable**: `tools/neo4j/` (scripts + queries)

---

### Phase 6: Pilot Migration (Week 8)
**Goal**: Validate in real project

- [ ] Migrate research-autopoietic-template ISSUE.yaml → ISSUE.md
- [ ] Convert existing artifacts to new templates
- [ ] Run full validation suite
- [ ] Document lessons learned (lesson-002)

**Deliverable**: Migrated project + lesson-002-migration-lessons.md

---

### Phase 7: Manifesto-Wide Specs (Week 9-10) 🆕
**Goal**: Complete system coherence

**Context**: Manifesto has 6 modules with multiple sections each. Create specs for systematic implementation:

**7.1 - Module 01-fundamentos/** (4 specs)
- [ ] spec-002: Implement "Qué es MELQUISEDEC" visual identity
- [ ] spec-003: Create interactive Árbol de la Vida diagram
- [ ] spec-004: Formalize 5 Rostros assignment rules
- [ ] spec-005: Validate P1-P10 compliance checker

**7.2 - Module 02-arquitectura/** (5 specs)
- [ ] spec-006: Implement Research Instance structure validation
- [ ] spec-007: Automate Sistema de Checkpoints (CK-01 to CK-05)
- [ ] spec-008: Deploy KnowledgeWriter API + Reconciliador
- [ ] spec-009: Implement Autopoiesis system (chatlog + lessons)
- [ ] spec-010: Create KeterDoc validation suite

**7.3 - Module 03-workflow/** (4 specs)
- [ ] spec-011: Implement Kanban board integration
- [ ] spec-012: Build trazabilidad graph visualizer
- [ ] spec-013: Create versionamiento automation
- [ ] spec-014: Document MCPs integration guide

**7.4 - Module 04-implementacion/** (3 specs)
- [ ] spec-015: Create flujo-completo wizard (CLI tool)
- [ ] spec-016: Automate lessons-learned extraction
- [ ] spec-017: Build interactive checklist validator

**7.5 - Module 05-casos-estudio/** (2 specs)
- [ ] spec-018: Document CASO-01-DDD as reference template
- [ ] spec-019: Document CASO-02-PROMPTS-DINAMICOS as reference

**7.6 - Module 06-referencias/** (1 spec)
- [ ] spec-020: Generate glosario kabalístico with search

**7.7 - Index Coherence** (1 spec)
- [ ] spec-021: **CRITICAL** - Rebuild index with results chain, conceptualization map

**Total**: 21 specs for complete manifesto implementation

**Deliverable**:
- 21 spec folders in `.spec-workflow/specs/spec-002/` through `spec-021/`
- Master index: `docs/manifiesto/00-master-index.md` (results chain)
- Conceptualization map: Visual diagram showing how all specs interconnect

---

## Validation Criteria

### How to Know This Lesson Is Valid

**Metric 1: Template Coverage**
- ✅ Success: 28+ artifact templates exist
- ✅ Success: 4 lens variants per template
- ❌ Failure: Generic templates only

**Metric 2: YAML-LD Adoption**
- ✅ Success: All artifacts have @context, @type, @id
- ✅ Success: RDF triples generate successfully
- ❌ Failure: Simple YAML still in use

**Metric 3: Tool Compatibility**
- ✅ Success: Obsidian can open ISSUE.md natively
- ✅ Success: spec-workflow-mcp processes MD files
- ❌ Failure: Tool-specific adapters needed

**Metric 4: Traceability**
- ✅ Success: Can query "show all concepts derived from paper X"
- ✅ Success: Neo4j graph visualizes seci relationships
- ❌ Failure: Manual tracking required

**Metric 5: Manifesto Coherence**
- ✅ Success: 21 specs created covering all 6 modules
- ✅ Success: Master index shows results chain
- ❌ Failure: Gaps remain in implementation

---

## Recommendations for Future

### For New Projects

1. **Always start with ISSUE.md** (not ISSUE.yaml)
2. **Always use KeterDoc/HKM metadata** (id, is_a, version, dc, seci)
3. **Always reference artifact_template** used
4. **Always specify lens** (DSR, IMRAD, DDD, Social)
5. **Always include workflow_pattern** for traceability

### For Existing Projects

1. **Migrate incrementally**: Phase 1 → Phase 7
2. **Validate continuously**: Run keterdoc-compliance.py after each change
3. **Document lessons**: Each migration = new lesson-learned
4. **Test in pilot**: Use research-autopoietic-template as testbed

### For Template Designers

1. **Study manifesto first**: Read all 3212 lines before creating templates
2. **Follow KeterDoc standard**: Don't reinvent metadata
3. **Create lens variants**: DSR ≠ IMRAD ≠ DDD
4. **Include examples**: Every template should have filled example
5. **Validate with users**: Test templates with real projects

---

## Related Artifacts

**Derives From**:
- [Chatlog: session-001-keterdoc-gap-analysis](../chatlog/session-001-keterdoc-gap-analysis/full-transcript.md)
- [Manifesto: templates-hkm.md](../../docs/manifiesto/02-arquitectura/03-templates-hkm.md)
- [Manifesto: sincronizacion-knowledge.md](../../docs/manifiesto/02-arquitectura/04-sincronizacion-knowledge.md)
- [Manifesto: autopoiesis-system.md](../../docs/manifiesto/02-arquitectura/05-autopoiesis-system.md)

**Informs**:
- [spec-001: Implement KeterDoc Architecture](../.spec-workflow/specs/spec-001-implement-keterdoc-architecture/)
- [spec-002 through spec-021]: Manifesto-wide implementation specs

**Similar Lessons**:
- (None yet - this is lesson-001)

---

## Confidence Evolution

| Date | Confidence | Reason |
|------|------------|--------|
| 2026-01-10 | 0.95 | Initial extraction from 4.5h session + 3212 lines documentation |
| TBD | ? | Will increase after Phase 6 pilot validates approach |

---

**Status**: ✅ Validated (based on extensive documentation)
**Next Validation**: After Phase 6 pilot migration
**Owner**: SALOMON (Tiferet - Equilibrio)
**Reviewers**: MELQUISEDEC (orchestration), MORPHEUS (implementation feasibility)
