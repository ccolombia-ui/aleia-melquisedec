---
# YAML-LD for Semantic Web (NEW FORMAT - Following Lesson-001)
'@context': 'https://melquisedec.org/context/v1'
'@type': 'ResearchIssue'
'@id': 'https://melquisedec.org/issues/spec-001-implement-keterdoc-architecture'

# KeterDoc/HKM Standard Metadata
id: 'spec-001-implement-keterdoc-architecture'
is_a: 'research-issue'
version: '1.0.0'
permalink: '.spec-workflow/specs/spec-001-implement-keterdoc-architecture/ISSUE.md'

# Dublin Core (dc) - Standard Metadata
dc:
  title: 'Implement KeterDoc Architecture with YAML-LD and Template System'
  creator: ['MELQUISEDEC', 'HYPATIA', 'SALOMON', 'MORPHEUS']
  date: '2026-01-10'
  subject:
    - 'keterdoc'
    - 'yaml-ld'
    - 'templates'
    - 'architecture'
    - 'metadata'
    - 'semantic-web'
    - 'autopoiesis'
  source:
    - 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    - 'docs/manifiesto/02-arquitectura/04-sincronizacion-knowledge.md'
    - 'docs/manifiesto/02-arquitectura/05-autopoiesis-system.md'
    - '060-reflect/lessons/lesson-001-keterdoc-architecture-gap.md'

# SECI Model (seci) - Knowledge Traceability
seci:
  derives_from:
    - '../../../060-reflect/chatlog/session-001-keterdoc-gap-analysis/full-transcript.md'
    - '../../../060-reflect/lessons/lesson-001-keterdoc-architecture-gap.md'
  informs: []  # Will be populated with outputs

# Workflow Configuration (NEW - Following Lesson-001)
artifact_template: '../../../_templates/daath-template/artifact-templates/by-type/issue-tpl.md'
workflow_pattern: 'PATTERN-007-Problem-RBM-GAC'
lens: 'DSR'  # Design Science Research (building artifact: KeterDoc system)

# MELQUISEDEC Workflow State
estado: 'inbox'  # inbox → literature → atomic → workbook → outputs
prioridad: 'crítica'
estimacion_esfuerzo: '10 weeks'
rostros_asignados: ['MELQUISEDEC', 'HYPATIA', 'SALOMON', 'MORPHEUS', 'ALMA']
---

# ISSUE-001: Implement KeterDoc Architecture with YAML-LD and Template System

## 🎯 Executive Summary

**Problem**: 3212 lines of manifesto documentation define complete KeterDoc/HKM metadata standard, template-per-artifact system, YAML-LD integration, and autopoiesis mechanisms, but **NONE of it is implemented** in current `research-autopoietic-template`.

**Goal**: Systematically migrate implementation to align with documented architecture through 7-phase plan, culminating in complete manifesto-wide implementation (21 specs total).

**Impact**:
- ✅ Enable semantic web integration (Neo4j RDF triples)
- ✅ Ensure artifact traceability (SECI model)
- ✅ Standardize cross-project templates (28+ templates × 4 lenses)
- ✅ Activate autopoiesis (pattern confidence scores)
- ✅ Achieve full manifesto coherence (6 modules, 21 specs)

**Timeline**: 10 weeks (7 phases + 21 incremental specs)

---

## 📋 Problem Statement (RBM-GAC Format)

### Gap Identified

**Current State**:
- ISSUE.yaml with custom structure (`problem`, `gap`, `goal`, `outcomes`)
- No KeterDoc/HKM metadata (id, is_a, version, dc, seci)
- Generic `template-base.yaml` without artifact-specific structure
- Simple YAML without semantic web features (@context, @type, @id)
- No workflow-pattern configuration per artifact
- Tools use MD (Obsidian, spec-workflow-mcp) but we use YAML

**Desired State**:
- ISSUE.md with YAML-LD frontmatter + KeterDoc metadata
- 28+ artifact-specific templates (concept, analysis, decision, output, etc.)
- 4 lens variants per template (DSR, IMRAD, DDD, Social) = 112 total
- Semantic web ready (@context, RDF triple generation)
- Configurable workflow-patterns per artifact type
- Full tool compatibility (Obsidian, spec-workflow-mcp)
- Complete manifesto implementation (21 specs covering 6 modules)

**Gap**: 5 critical architectural components missing + incomplete manifesto implementation

---

### Context

**Discovery Trigger**: User question: "¿LOS YAML QUE USAMOS SON YAML-LD?"

**Investigation**: 4.5 hour session, 3212 lines of manifesto documentation read

**Key Findings**:
1. KeterDoc/HKM standard (575 lines) - NOT implemented
2. Output Triple architecture (MD + Graph + Vectors) - Partially implemented
3. Autopoiesis system (chatlog + lessons) - NOT implemented
4. 10 Principios Fundacionales - Partially followed
5. 6 manifesto modules - Documented but not systematically implemented

**Confidence**: 0.95 (very high - based on extensive documentation)

---

### Stakeholders Affected

| Stakeholder | Need | Impact |
|-------------|------|--------|
| **Developers** | Consistent templates, clear structure | HIGH - Daily workflow |
| **Researchers** | Traceability (seci), semantic search | HIGH - Knowledge management |
| **AI Agents** | Machine-readable metadata (YAML-LD) | CRITICAL - Automation |
| **Neo4j System** | RDF triples, relationships | HIGH - Graph queries |
| **Obsidian Users** | MD compatibility | HIGH - Tool integration |
| **Future Projects** | Reusable templates, patterns | CRITICAL - Scalability |

---

## 🎯 Goal (SMART)

**Specific**: Implement complete KeterDoc architecture with YAML-LD, 28+ templates, 4 lens variants, workflow-pattern system, and 21 manifesto-wide specs.

**Measurable**:
- ✅ 100% artifacts use KeterDoc metadata (id, is_a, dc, seci)
- ✅ 28+ artifact templates created
- ✅ 4 lens variants per template (112 total)
- ✅ @context YAML-LD definition validated
- ✅ RDF triple generation working
- ✅ Obsidian + spec-workflow-mcp compatibility confirmed
- ✅ 21 specs created covering all 6 manifesto modules
- ✅ Master index with results chain created

**Achievable**: 7 phases over 10 weeks, incremental validation

**Relevant**: Aligns implementation with documented manifesto (P1, P2, P3, P6)

**Time-bound**:
- Weeks 1-2: Phase 1 (Fundamentos)
- Weeks 3-4: Phase 2 (Lens Integration)
- Week 5: Phase 3 (Workflow-Pattern System)
- Week 6: Phase 4 (Migration Tools)
- Week 7: Phase 5 (Neo4j Integration)
- Week 8: Phase 6 (Pilot Migration)
- Weeks 9-10: Phase 7 (Manifesto-Wide Specs + Index Coherence)

---

## 🎯 Expected Outcomes

### Outcome 1: Semantic Web Integration

- **Type**: Technical Infrastructure
- **Description**: All artifacts generate valid RDF triples importable to Neo4j
- **Indicator**: `yaml-ld-to-rdf-triples.py` converts 100% of artifacts without errors
- **Target**: RDF import completes in <5 minutes for 100 artifacts
- **Validation**: Neo4j queries can traverse seci relationships

---

### Outcome 2: Template Standardization

- **Type**: Development Process
- **Description**: 28+ artifact-specific templates with 4 lens variants each
- **Indicator**: Developers select from `artifact-templates/by-type/` and `by-lens/`
- **Target**: 95% of new artifacts use standard templates
- **Validation**: `validate-keterdoc-compliance.py` passes on all new artifacts

---

### Outcome 3: Tool Compatibility

- **Type**: User Experience
- **Description**: ISSUE.md opens natively in Obsidian and processes with spec-workflow-mcp
- **Indicator**: No custom adapters or converters needed
- **Target**: Zero tool-specific workarounds
- **Validation**: Obsidian graph view shows links, spec-workflow-mcp generates tasks.md

---

### Outcome 4: Traceability Activation

- **Type**: Knowledge Management
- **Description**: SECI model (derives_from, informs) enables full artifact lineage tracking
- **Indicator**: Can query "show all concepts derived from paper X"
- **Target**: 100% of atomic concepts have seci.derives_from populated
- **Validation**: Neo4j graph visualizer shows complete knowledge tree

---

### Outcome 5: Autopoiesis Enablement

- **Type**: System Evolution
- **Description**: Chatlog + lessons → pattern confidence scores → template evolution
- **Indicator**: Confidence scores update automatically after each project
- **Target**: Patterns with confidence ≥0.90 auto-apply in new projects
- **Validation**: Pattern evolution visible in changelog (v1.0.0 → v1.1.0)

---

### Outcome 6: Manifesto Coherence ✨ NEW

- **Type**: System Completeness
- **Description**: All 6 manifesto modules systematically implemented via 21 specs
- **Indicator**: Master index shows results chain connecting all specs
- **Target**: 100% of manifesto sections have corresponding implementation spec
- **Validation**:
  - All 21 specs created with ISSUE.md + requirements.md + design.md
  - Master index `docs/manifiesto/00-master-index.md` visualizes conceptualization map
  - No orphaned documentation (every manifesto section → spec)

---

## 🚀 High-Level Activities

### Activity 1: Phase 1 - Fundamentos (Weeks 1-2)

**Contributes to**: Outcomes 1, 2 (Foundation for all)

**Type**: Architecture + Implementation

**Tasks**:
1. Define @context YAML-LD vocabulary
2. Create context.jsonld in project root
3. Validate with JSON-LD playground
4. Create 6 base templates: concept, analysis, decision, experiment, output, lesson
5. Document template structure and usage

**Estimación**: 2 weeks (80 hours)

**Deliverable**:
- `context.jsonld` (validated)
- `artifact-templates/by-type/` (6 templates with examples)
- `docs/guides/KETERDOC-QUICKSTART.md`

---

### Activity 2: Phase 2 - Lens Integration (Weeks 3-4)

**Contributes to**: Outcome 2 (Template Standardization)

**Type**: Template Design

**Tasks**:
1. Create artifact-templates/by-lens/ structure (4 folders)
2. Generate 24 lens-specific templates (6 base × 4 lenses)
3. Document differences: DSR vs IMRAD vs DDD vs Social
4. Create filled examples for each lens variant
5. Write lens selection guide

**Estimación**: 2 weeks (80 hours)

**Deliverable**:
- `artifact-templates/by-lens/dsr/` (6 templates)
- `artifact-templates/by-lens/imrad/` (6 templates)
- `artifact-templates/by-lens/ddd/` (6 templates)
- `artifact-templates/by-lens/social/` (6 templates)
- `docs/guides/LENS-SELECTION-GUIDE.md`

---

### Activity 3: Phase 3 - Workflow-Pattern System (Week 5)

**Contributes to**: Outcome 5 (Autopoiesis)

**Type**: Configuration + Pattern Design

**Tasks**:
1. Define artifact-workflows.yaml mapping (artifact_type → pattern)
2. Create 10 PATTERN-*.yaml files with:
   - steps (sequence of actions)
   - validation_criteria (success checks)
   - confidence_score (0.00-1.00)
   - lens_applicability (which lenses apply)
3. Document pattern evolution mechanism
4. Create pattern confidence tracking system

**Estimación**: 1 week (40 hours)

**Deliverable**:
- `config/artifact-workflows.yaml`
- `patterns/PATTERN-000-output-triple.yaml` through `PATTERN-009.yaml`
- `docs/guides/PATTERN-SYSTEM.md`
- `tools/autopoiesis/update-pattern-confidence.py`

---

### Activity 4: Phase 4 - Migration Tools (Week 6)

**Contributes to**: Outcome 2, 4 (Automation)

**Type**: Tooling + Automation

**Tasks**:
1. Script: convert-issue-yaml-to-md.py
2. Script: generate-artifact-from-template.py
3. Script: validate-keterdoc-compliance.py
4. Script: extract-seci-relationships.py
5. Create test suite for all scripts

**Estimación**: 1 week (40 hours)

**Deliverable**:
- `tools/keterdoc/convert-issue-yaml-to-md.py`
- `tools/keterdoc/generate-artifact-from-template.py`
- `tools/keterdoc/validate-keterdoc-compliance.py`
- `tools/keterdoc/extract-seci-relationships.py`
- `tests/keterdoc/` (unit tests, >80% coverage)

---

### Activity 5: Phase 5 - Neo4j Integration (Week 7)

**Contributes to**: Outcome 1, 4 (Semantic Web + Traceability)

**Type**: Integration + Data Pipeline

**Tasks**:
1. Script: yaml-ld-to-rdf-triples.py
2. Cypher queries for RDF import
3. SECI relationship extraction (derives_from → Neo4j edges)
4. Semantic query examples (SPARQL-like)
5. Performance testing (1000+ artifacts)

**Estimación**: 1 week (40 hours)

**Deliverable**:
- `tools/neo4j/yaml-ld-to-rdf-triples.py`
- `tools/neo4j/import-rdf-to-neo4j.cypher`
- `tools/neo4j/semantic-queries/` (10 example queries)
- `docs/guides/NEO4J-INTEGRATION.md`

---

### Activity 6: Phase 6 - Pilot Migration (Week 8)

**Contributes to**: All Outcomes (Validation)

**Type**: Testing + Validation

**Tasks**:
1. Migrate research-autopoietic-template ISSUE.yaml → ISSUE.md
2. Convert 20+ existing artifacts to new templates
3. Run full validation suite
4. Test Obsidian integration (open, edit, save)
5. Test spec-workflow-mcp integration (generate tasks.md)
6. Extract lesson-002-migration-validation.md

**Estimación**: 1 week (40 hours)

**Deliverable**:
- `research-autopoietic-template/ISSUE.md` (migrated)
- `research-autopoietic-template/020-conceive/02-atomics/` (20+ concepts migrated)
- `060-reflect/lessons/lesson-002-migration-validation.md`
- Migration report (successes, failures, adjustments)

---

### Activity 7: Phase 7 - Manifesto-Wide Specs + Index Coherence (Weeks 9-10) ✨ NEW

**Contributes to**: Outcome 6 (Manifesto Coherence)

**Type**: Systematic Implementation + Documentation

**Tasks**:

#### 7.1 - Module 01-fundamentos (4 specs)
- [ ] spec-002: Visual identity for "Qué es MELQUISEDEC"
- [ ] spec-003: Interactive Árbol de la Vida diagram
- [ ] spec-004: 5 Rostros assignment automation
- [ ] spec-005: P1-P10 compliance checker

#### 7.2 - Module 02-arquitectura (5 specs)
- [ ] spec-006: Research Instance structure validator
- [ ] spec-007: Sistema de Checkpoints automation (CK-01 to CK-05)
- [ ] spec-008: KnowledgeWriter API + Reconciliador deployment
- [ ] spec-009: Autopoiesis system implementation (chatlog + lessons)
- [ ] spec-010: KeterDoc validation suite (this spec completes it)

#### 7.3 - Module 03-workflow (4 specs)
- [ ] spec-011: Kanban board integration
- [ ] spec-012: Trazabilidad graph visualizer
- [ ] spec-013: Versionamiento automation
- [ ] spec-014: MCPs integration guide

#### 7.4 - Module 04-implementacion (3 specs)
- [ ] spec-015: Flujo-completo wizard (CLI tool)
- [ ] spec-016: Lessons-learned extraction automation
- [ ] spec-017: Interactive checklist validator

#### 7.5 - Module 05-casos-estudio (2 specs)
- [ ] spec-018: CASO-01-DDD documentation as template
- [ ] spec-019: CASO-02-PROMPTS-DINAMICOS documentation

#### 7.6 - Module 06-referencias (1 spec)
- [ ] spec-020: Glosario kabalístico with search

#### 7.7 - Master Index Coherence (1 spec) 🎯 CRITICAL
- [ ] spec-021: **Rebuild master index with results chain and conceptualization map**

**Estimación**: 2 weeks (80 hours)

**Deliverable**:
- `.spec-workflow/specs/spec-002/` through `spec-021/` (20 folders)
- Each spec has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md
- `docs/manifiesto/00-master-index.md` (NEW - results chain)
- `docs/manifiesto/00-conceptualization-map.mermaid` (NEW - visual system)
- `docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md` (tracking)

**Key Artifact: Master Index Structure**

```markdown
# 00-master-index.md

## Results Chain (Dependency Flow)

```mermaid
graph TB
    spec-001[spec-001: KeterDoc<br/>Foundation]
    spec-002[spec-002: Visual<br/>Identity]
    spec-005[spec-005: P1-P10<br/>Checker]
    spec-010[spec-010: Validation<br/>Suite]

    spec-001 --> spec-002
    spec-001 --> spec-005
    spec-001 --> spec-010
    spec-005 --> spec-007
    spec-010 --> spec-017

    [... complete chain ...]
```

## Conceptualization Map

[Visual showing how all 21 specs interconnect to form complete MELQUISEDEC system]

## Implementation Status

| Module | Specs | Status | Completion |
|--------|-------|--------|------------|
| 01-fundamentos | 4 | 🟡 In Progress | 25% |
| 02-arquitectura | 5 | 🟡 In Progress | 40% |
| [...]
```

---

## 🔍 Risks and Constraints

### Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **YAML-LD complexity** | Medium | High | Start with simple @context, expand gradually |
| **Template proliferation** | High | Medium | Start with 6 base, add lens variants iteratively |
| **Breaking changes** | High | Critical | Maintain backward compatibility, migrate incrementally |
| **Neo4j performance** | Low | Medium | Test with 1000+ artifacts, optimize queries |
| **Tool incompatibility** | Low | High | Test early with Obsidian + spec-workflow-mcp |
| **Scope creep (21 specs)** | High | High | Phase 7 is incremental, can defer non-critical specs |

### Constraints

- **Time**: 10 weeks (fixed timeline)
- **Resources**: Solo developer + AI assistance
- **Compatibility**: Must work with existing tools (Obsidian, Neo4j, spec-workflow-mcp)
- **Documentation**: Manifesto is extensive (3212 lines), must read thoroughly
- **Standards**: Must follow Dublin Core, SECI Model, YAML-LD spec

---

## 📊 Success Criteria (Validation)

### Phase 1-6 Criteria

1. ✅ **@context validated**: JSON-LD playground accepts context.jsonld
2. ✅ **Templates created**: 6 base + 24 lens variants = 30 total
3. ✅ **Patterns defined**: 10 PATTERN-*.yaml files with confidence scores
4. ✅ **Tools working**: All 7 scripts run without errors
5. ✅ **Neo4j integration**: RDF triples import successfully
6. ✅ **Pilot success**: research-autopoietic-template migrated, validated

### Phase 7 Criteria (NEW)

7. ✅ **21 specs created**: All manifesto modules have implementation specs
8. ✅ **Master index built**: Results chain shows dependencies between specs
9. ✅ **Conceptualization map**: Visual diagram shows system coherence
10. ✅ **No orphaned docs**: Every manifesto section has corresponding spec
11. ✅ **Implementation status**: Tracking document shows progress per module

### Overall Success

- **Quantitative**:
  - 100% of new artifacts use KeterDoc metadata
  - 95% pass validate-keterdoc-compliance.py
  - Neo4j queries return results in <1 second
  - 21 specs created covering 6 modules

- **Qualitative**:
  - Developers say "templates make creation easier"
  - Obsidian users say "works natively, no issues"
  - AI agents say "metadata is machine-readable"
  - System shows clear coherence from index

---

## 🔗 Related Artifacts

**Derives From**:
- [Chatlog: session-001-keterdoc-gap-analysis](../../060-reflect/chatlog/session-001-keterdoc-gap-analysis/full-transcript.md)
- [Lesson: lesson-001-keterdoc-architecture-gap](../../060-reflect/lessons/lesson-001-keterdoc-architecture-gap.md)
- [Manifesto: templates-hkm.md](../../../docs/manifiesto/02-arquitectura/03-templates-hkm.md)
- [Manifesto: sincronizacion-knowledge.md](../../../docs/manifiesto/02-arquitectura/04-sincronizacion-knowledge.md)

**Informs**:
- All 21 manifesto implementation specs (spec-002 through spec-021)
- Future projects using KeterDoc architecture

---

## 📝 Notes

### Why 7 Phases?

- **Phases 1-6**: Core KeterDoc architecture (8 weeks)
- **Phase 7**: Manifesto-wide coherence (2 weeks)
- **Rationale**: Build foundation first, then systematize all modules

### Why This Matters

This is not just "fixing YAML files". This is:
- ✅ Enabling semantic web (linked data, RDF triples)
- ✅ Activating autopoiesis (system learns from itself)
- ✅ Ensuring traceability (every artifact has lineage)
- ✅ Standardizing templates (consistency across projects)
- ✅ Achieving manifesto coherence (documented → implemented)

**This is the foundation for MELQUISEDEC v4.0.0 to actually work as documented.**

---

**Status**: ✅ Created
**Version**: 1.0.0
**Next Action**: Create requirements.md with detailed RBM-GAC breakdown
