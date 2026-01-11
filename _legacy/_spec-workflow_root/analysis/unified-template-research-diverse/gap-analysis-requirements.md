# Gap Analysis & Requirements - Unified Research Template

> **Date**: 2026-01-09
> **Methodology**: Sequential Thinking (5 thoughts)
> **Analyzed**: 5 analysis documents consolidated
> **Purpose**: Critical gaps & requirements for v3.0.0 implementation

---

## 🎯 Executive Summary

### Core Finding

**Original v1.0.0 design proposed reinventing 3 systems that already exist**:

```yaml
reinventing:
  versionado: "HKM/keterdoc already exists (45+ files using it)"
  stack: "Neo4j+LlamaIndex architecture already validated (1175-line analysis)"
  task_format: "DAATH-ZEN Advanced already documented (archive/tasks.md, 1551 lines)"

impact:
  effort_wasted: "16 hours (36% of 25h estimate)"
  fragmentation_risk: "Creating parallel standards"
  decision: "v1.0.0 REJECTED → v2.0.0 REFACTORED → v3.0.0 CONSOLIDATED"
```

### Critical Gaps Identified

| GAP | Description | Impact | Status |
|-----|-------------|--------|--------|
| **GAP-1** | Versionado: Reinvents HKM/keterdoc | 🔴 Critical | Fixed in v3.0.0 |
| **GAP-2** | Stack: Ignores validated architecture | 🔴 Critical | Fixed in v3.0.0 |
| **GAP-3** | Task Format: Doesn't use best format | 🔴 Critical | Fixed in v3.0.0 |
| **GAP-4** | Workflows: No divergence by type | 🔴 Critical | Fixed in v3.0.0 |
| **GAP-5** | Principles: Not operationalized | ⚠️ High | Fixed in v3.0.0 |

---

## 🔴 GAP-1: Versionado - HKM/Keterdoc Already Exists

### Problem

```markdown
# v1.0.0 proposed (Task 3):
versioning:
  current_version: "v1.0.0"
  current_epic: "fundacion"

# This REINVENTS existing standard
```

### Reality

**HKM/keterdoc standard already complete** (`docs/manifiesto/02-arquitectura/03-templates-hkm.md`):

```yaml
---
id: "unique-identifier"
version: "1.0.0"              # ✅ Semver
dc:
  title: "..."
  creator: ["Rostro"]
  date: "2026-01-09"
  source: ["DOI"]
seci:
  derives_from: ["source.md"]  # ✅ Traceability
  informs: ["derivative.md"]    # ✅ Dependency graph
status: "published"             # ✅ Lifecycle
git_tag: "output-v1.0.0"       # ✅ Git integration
---
```

**Tools already exist**:
- `validate-metadata.py` - Validates HKM headers
- Used in 45+ files in `docs/manifiesto/`

### Fix Requirements

```yaml
REQ-1.1:
  title: "Integrate HKM standard (do NOT reinvent)"
  action: "Use existing HKM headers in ALL artifacts"
  validation: "validate-metadata.py passes"
  priority: "P0 - Blocker"

REQ-1.2:
  title: "Epic metadata separate from artifact metadata"
  action: "ISSUE.yaml for epic-level, HKM headers for artifact-level"
  validation: "Clear separation documented"
  priority: "P0 - Blocker"

REQ-1.3:
  title: "Neo4j integration uses HKM fields"
  action: "sync-hkm-to-neo4j.py reads HKM seci relationships"
  validation: "Script creates [:DERIVES_FROM] from seci.derives_from"
  priority: "P1 - Critical"
```

### Impact

- **Effort saved**: 4 hours (no need to design versionado)
- **Risk avoided**: Fragmentation of metadata standard
- **Benefit**: Reuse existing validation tooling

---

## 🔴 GAP-2: Stack - Architecture Already Validated

### Problem

```markdown
# v1.0.0 proposed (Task 4):
vector:
  store: "chroma/qdrant/weaviate"  # TBD

# This IGNORES 1175-line comparative analysis
```

### Reality

**Stack decision already made** (`comparative-analysis.md`):

| Framework | Score | Decision | Role |
|-----------|-------|----------|------|
| LlamaIndex | 8.6/10 | ✅ ADOPTED | Recuperación (PropertyGraphIndex, 4 retrievers) |
| LangChain | 8.0/10 | ✅ ADOPTED | Orquestación (ReAct agents, memory) |
| Neo4j GraphRAG | 6.95/10 | ⚠️ Complementary | Optional for specific cases |

**Hybrid architecture validated** (`llamaindex.md` Chapter 10):

```python
# 3-Layer Architecture (ALREADY VALIDATED)
# Layer 1: Neo4j (unified graph + vector)
# Layer 2: LlamaIndex (specialized retrieval)
# Layer 3: LangChain (agent orchestration)

# NO separate vector store needed - Neo4jVectorStore is unified
```

**Performance benchmarks exist**:
- 100 docs indexed in <2 min
- Queries: 50-100ms
- HNSW quantization validated

### Fix Requirements

```yaml
REQ-2.1:
  title: "Use Neo4jVectorStore (unified storage)"
  action: "Eliminate TBD - specify Neo4jVectorStore definitively"
  validation: "Code examples use Neo4jVectorStore"
  priority: "P0 - Blocker"

REQ-2.2:
  title: "Document hybrid architecture (3 layers)"
  action: "Reference llamaindex.md Chapter 10 for integration"
  validation: "Architecture section has 3-layer code example"
  priority: "P0 - Blocker"

REQ-2.3:
  title: "Reference comparative-analysis.md"
  action: "Link to existing analysis instead of re-researching"
  validation: "References section includes comparative-analysis.md"
  priority: "P1 - Critical"

REQ-2.4:
  title: "Clarify LangChain is NOT overkill"
  action: "Document complementary roles (LlamaIndex retrieval + LangChain orchestration)"
  validation: "Stack section explains why BOTH frameworks"
  priority: "P1 - Critical"
```

### Impact

- **Effort saved**: 8 hours (no need to research stack)
- **Risk avoided**: Choosing suboptimal architecture
- **Benefit**: Proven performance characteristics

---

## 🔴 GAP-3: Task Format - DAATH-ZEN Advanced Exists

### Problem

```markdown
# v1.0.0 had no specific task format
# v2.0.0 mentioned DAATH-ZEN but didn't adopt format
# Best format is ALREADY DOCUMENTED
```

### Reality

**`archive/tasks.md` is superior format** (identified by `deep-coherence-analysis.md`):

| Feature | Basic Format | archive/tasks.md | Benefit |
|---------|--------------|------------------|---------|
| MCP Workflow Strategy | ❌ No | ✅ Table | Plan MCPs upfront |
| Thinking Mode | ❌ No | ✅ Explicit | sequential/smart-thinking choice |
| Executable Prompt | ❌ One line | ✅ Multi-line code block | Copy-paste ready |
| Success Criteria | ❌ Inline | ✅ Checklist | Easy validation |
| Lessons | ❌ No | ✅ Linked | Track implementation logs |

**Coherence score**: 95% (highest of all formats analyzed)

### Fix Requirements

```yaml
REQ-3.1:
  title: "Adopt DAATH-ZEN Advanced format"
  action: "Use archive/tasks.md structure as template"
  validation: "tasks.md.template matches archive/tasks.md format"
  priority: "P0 - Blocker"

REQ-3.2:
  title: "MCP Workflow Strategy table mandatory"
  action: "All tasks specify: Thinking Mode, Activation, Parallel, Sequential"
  validation: "Example task has complete MCP strategy"
  priority: "P1 - Critical"

REQ-3.3:
  title: "Executable prompts"
  action: "Prompts in code blocks, copy-pasteable"
  validation: "Example prompt can be executed without modification"
  priority: "P1 - Critical"

REQ-3.4:
  title: "Success criteria as checklists"
  action: "Use - [ ] format with verification methods"
  validation: "Each criterion specifies HOW to verify"
  priority: "P2 - High"
```

### Impact

- **Effort saved**: 2 hours (no need to design format)
- **Risk avoided**: Multiple incompatible task formats
- **Benefit**: Standardization across all specs

---

## 🔴 GAP-4: Workflows - No Divergence by Type

### Problem

```markdown
# v1.0.0 and v2.0.0 treat all outputs the same
# Research, App, and Social-Project have DIFFERENT outputs
# Single workflow forces artificial homogeneity
```

### Reality

**Outputs differ fundamentally by type**:

| Phase | Research | App | Social-Project |
|-------|----------|-----|----------------|
| 04-artifacts | Cypher queries, pipelines | Domain/Ports/Adapters | Stakeholder map, theory of change |
| 05-outputs | Paper draft, presentation | Deployable package, tests | Proposal, implementation plan |

**Divergence point**: After SALOMON (analysis), workflows split

### Fix Requirements

```yaml
REQ-4.1:
  title: "Define divergent workflows"
  action: "Document 3 paths post-SALOMON"
  validation: "workflows-divergentes.md with 3 complete examples"
  priority: "P0 - Blocker"

REQ-4.2:
  title: "Type-specific folder structures"
  action: "04-artifacts/ and 05-outputs/ diverge by ISSUE.yaml type"
  validation: "Examples show research/app/social structures"
  priority: "P0 - Blocker"

REQ-4.3:
  title: "Type-specific success criteria"
  action: "CK-03 and CK-04 checkpoints differ by type"
  validation: "Checkpoint validation respects type"
  priority: "P1 - Critical"

REQ-4.4:
  title: "ISSUE.yaml type field"
  action: "type: research|app|social-project determines workflow"
  validation: "ISSUE.yaml.template includes type with options"
  priority: "P1 - Critical"
```

### Impact

- **Effort saved**: 3 hours (clear guidance vs trial-and-error)
- **Risk avoided**: Forcing inappropriate artifacts
- **Benefit**: Natural fit for each project type

---

## ⚠️ GAP-5: Principles - Not Operationalized

### Problem

```markdown
# v1.0.0 and v2.0.0 MENTION P1-P7 but don't show HOW
# Principles remain abstract without concrete examples
# No mapping to template components
```

### Reality

**7 Principles exist** (`docs/manifiesto/01-fundamentos/04-principios-fundacionales.md`):

- P1: Síntesis Metodológica (DSR + Zettelkasten + SECI)
- P2: Autopoiesis (self-improvement through lessons)
- P3: Issue-Driven (metadata-centric)
- P5: Validación Continua (4 checkpoints)
- P6: Trazabilidad Explícita (triple output)
- P7: Recursión Fractal (pattern repeats at all levels)

**But HOW are they implemented?** Not documented.

### Fix Requirements

```yaml
REQ-5.1:
  title: "Operationalize each principle"
  action: "Show concrete implementation for P1-P7"
  validation: "principios-operacionalizados.md with yaml examples"
  priority: "P1 - Critical"

REQ-5.2:
  title: "Map principles to components"
  action: "P1 → folder structure, P6 → sync scripts, etc."
  validation: "Each principle has 'implementation' and 'evidence' fields"
  priority: "P2 - High"

REQ-5.3:
  title: "P2 Autopoiesis mechanism"
  action: "Document: 06-lessons/ → summary.yaml → template vN+1"
  validation: "Flow diagram showing feedback loop"
  priority: "P2 - High"

REQ-5.4:
  title: "P7 Fractal structure"
  action: "Show pattern at 3 levels: monorepo, spec-issue, artifact"
  validation: "Diagram showing HKM headers at all levels"
  priority: "P2 - High"
```

### Impact

- **Effort saved**: 2 hours (vs discovering through practice)
- **Risk avoided**: Principle violations
- **Benefit**: Philosophical coherence

---

## 📋 Requirements Summary

### P0 - Blockers (Must-Have for v3.0.0)

| ID | Requirement | Component | Effort |
|----|-------------|-----------|--------|
| REQ-1.1 | Integrate HKM standard | Templates | 1h |
| REQ-1.2 | Separate epic/artifact metadata | ISSUE.yaml | 1h |
| REQ-2.1 | Use Neo4jVectorStore | Architecture | 30min |
| REQ-2.2 | Document 3-layer hybrid | Architecture | 1h |
| REQ-3.1 | Adopt DAATH-ZEN Advanced | tasks.md | 2h |
| REQ-4.1 | Define divergent workflows | Documentation | 3h |
| REQ-4.2 | Type-specific structures | Examples | 2h |

**Total P0**: 10.5 hours

### P1 - Critical (Required for Production)

| ID | Requirement | Component | Effort |
|----|-------------|-----------|--------|
| REQ-1.3 | Neo4j integration uses HKM | Scripts | 2h |
| REQ-2.3 | Reference comparative-analysis | Documentation | 30min |
| REQ-2.4 | Clarify LangChain role | Documentation | 30min |
| REQ-3.2 | MCP Workflow Strategy mandatory | Template | 1h |
| REQ-3.3 | Executable prompts | Template | 1h |
| REQ-4.3 | Type-specific checkpoints | Validation | 1h |
| REQ-4.4 | ISSUE.yaml type field | Template | 30min |
| REQ-5.1 | Operationalize principles | Documentation | 2h |

**Total P1**: 8.5 hours

### P2 - High (Strongly Recommended)

| ID | Requirement | Component | Effort |
|----|-------------|-----------|--------|
| REQ-3.4 | Success criteria checklists | Template | 30min |
| REQ-5.2 | Map principles to components | Documentation | 1h |
| REQ-5.3 | P2 Autopoiesis mechanism | Documentation | 1h |
| REQ-5.4 | P7 Fractal structure | Documentation | 1h |

**Total P2**: 3.5 hours

**Grand Total**: 22.5 hours (realistic estimate vs 25h original)

---

## 🚀 Implementation Plan

### Phase 1: Foundation (Week 1)

**Focus**: Integrate existing standards

```yaml
tasks:
  - REQ-1.1: Create HKM header templates (source/concept/workbook/artifact/output/lesson)
  - REQ-1.2: Create ISSUE.yaml.template with epic metadata
  - REQ-2.1: Specify Neo4jVectorStore in architecture docs
  - REQ-2.2: Document 3-layer hybrid with code example
  - REQ-3.1: Create tasks.md.template using archive/tasks.md format

deliverables:
  - templates/hkm-headers/*.yaml
  - ISSUE.yaml.template
  - tasks.md.template
  - docs/architecture-hybrid.md

effort: 6 hours
blockers_resolved: REQ-1.1, REQ-1.2, REQ-2.1, REQ-2.2, REQ-3.1
```

### Phase 2: Divergence (Week 2)

**Focus**: Type-specific workflows

```yaml
tasks:
  - REQ-4.1: Document 3 workflows (research/app/social-project)
  - REQ-4.2: Create folder structures for each type
  - REQ-4.3: Define type-specific checkpoints
  - REQ-4.4: Add type field to ISSUE.yaml
  - REQ-3.2: Add MCP Workflow Strategy to template

deliverables:
  - docs/workflows-divergentes.md
  - examples/research-example-v1.0.0/
  - examples/app-example-v1.0.0/
  - examples/social-project-example-v1.0.0/

effort: 7 hours
blockers_resolved: REQ-4.1, REQ-4.2, REQ-3.2
```

### Phase 3: Implementation (Week 3)

**Focus**: Scripts and validation

```yaml
tasks:
  - REQ-1.3: Implement sync-hkm-to-neo4j.py
  - REQ-2.3: Add references to comparative-analysis
  - REQ-3.3: Create executable prompt examples
  - REQ-4.3: Implement type-aware checkpoint validation

deliverables:
  - scripts/sync-hkm-to-neo4j.py
  - scripts/archive-epic.sh
  - scripts/validate-triple-coherence.py
  - tests/test_scripts.py

effort: 6 hours
```

### Phase 4: Documentation (Week 4)

**Focus**: Principles and guides

```yaml
tasks:
  - REQ-5.1: Operationalize P1-P7 with examples
  - REQ-5.2: Map principles to components
  - REQ-5.3: Document P2 Autopoiesis flow
  - REQ-5.4: Diagram P7 Fractal structure
  - REQ-2.4: Clarify LangChain complementary role

deliverables:
  - docs/principios-operacionalizados.md
  - README.md (comprehensive guide)
  - ADR-003-unified-template.md

effort: 4 hours
```

**Total Implementation**: 23 hours (realistic with buffer)

---

## ✅ Acceptance Criteria

### For v3.0.0 Release

```yaml
AC-1:
  criterion: "All P0 requirements implemented"
  validation: "10.5 hours of P0 work completed"
  status: "Mandatory"

AC-2:
  criterion: "HKM integration validated"
  validation: "validate-metadata.py passes on examples"
  status: "Mandatory"

AC-3:
  criterion: "Scripts functional"
  validation: "sync-hkm-to-neo4j.py + archive-epic.sh + validate-triple-coherence.py working"
  status: "Mandatory"

AC-4:
  criterion: "3 complete examples"
  validation: "research/app/social examples with all folders"
  status: "Mandatory"

AC-5:
  criterion: "Divergent workflows documented"
  validation: "workflows-divergentes.md with 3 paths"
  status: "Mandatory"

AC-6:
  criterion: "DAATH-ZEN Advanced adopted"
  validation: "tasks.md.template matches archive/tasks.md structure"
  status: "Mandatory"

AC-7:
  criterion: "Principles operationalized"
  validation: "P1-P7 with concrete examples"
  status: "Strongly recommended"

AC-8:
  criterion: "Tests passing"
  validation: "pytest tests/ shows all green"
  status: "Nice to have"
```

---

## 📊 Effort Comparison

### Original (v1.0.0 Rejected)

```
Task 1: Analyze templates          → 3h
Task 2: Design architecture        → 4h
Task 3: Design epics system        → 4h  ❌ REDUNDANT (HKM exists)
Task 4: Design triple persistence  → 8h  ❌ REDUNDANT (stack validated)
Task 5: Git workflow integration   → 3h
Task 6: Validate design            → 3h
---------------------------------------------
TOTAL:                              25h
WASTED EFFORT:                      12h (48%)
```

### Optimized (v3.0.0)

```
Phase 1: Foundation (integrate)    → 6h  ✅ Reuses HKM + stack
Phase 2: Divergence (workflows)    → 7h  ✅ Clear type-specific paths
Phase 3: Implementation (scripts)  → 6h  ✅ Focused on sync/archive/validate
Phase 4: Documentation (principles)→ 4h  ✅ Operationalize P1-P7
---------------------------------------------
TOTAL:                              23h
EFFICIENCY GAIN:                    2h (8% faster even with more features)
```

**Key Insight**: Integration is FASTER than reinvention, even with added features (divergent workflows, operationalized principles)

---

## 🎯 Success Metrics

### Qualitative

- ✅ No fragmentation (single metadata standard)
- ✅ No redundant research (references existing analyses)
- ✅ Clear guidance (3 workflow examples)
- ✅ Testable (scripts have tests)
- ✅ Coherent (principles mapped to components)

### Quantitative

- ✅ 5 critical gaps resolved
- ✅ 23 requirements defined (10.5h P0 + 8.5h P1 + 3.5h P2)
- ✅ 3 divergent workflows documented
- ✅ 7 principles operationalized
- ✅ 3 core scripts implemented

---

## 📚 References

### Analysis Sources (Consolidated)

1. `coherence-index-analysis-2026-01-09.md` - Structure analysis (362 lines)
2. `consolidation-spec-workflow-daath-zen.md` - Integration strategy (335 lines)
3. `deep-coherence-analysis-2026-01-09.md` - Format analysis (347 lines)
4. `unified-research-template-design-v2.0.0.md` - Previous design (1351 lines)
5. `gap-analysis-unified-template-2026-01-09.md` - Original gaps (1169 lines)

### Standards (Referenced, Not Reinvented)

6. `docs/manifiesto/02-arquitectura/03-templates-hkm.md` - HKM standard
7. `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md` - P1-P7
8. `apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md` - Stack validation
9. `.spec-workflow/archive/tasks.md` - DAATH-ZEN Advanced format

---

**Version**: 1.0.0
**Status**: ✅ Requirements Defined - Ready for Implementation
**Next**: Execute Phase 1 (Foundation)
**Consolidated From**: 5 analysis documents totaling 3,564 lines
**This Document**: 600 lines (83% reduction while maintaining critical info)
