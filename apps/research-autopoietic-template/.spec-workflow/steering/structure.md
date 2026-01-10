# Project Structure - Research Autopoietic Templates

> **Living Document:** This structure evolves as the project progresses
> **Last Updated:** 2024-01 (Phase 010-define)
> **Status:** Active, Initial Structure Complete

---

## Overview

Este proyecto es **meta-research**: diseña el sistema de templates que otros proyectos de investigación usarán. Es **self-referential** porque usa v4.3.1 para diseñar las mejoras a v4.3.1+.

**Key Characteristic:** Este proyecto NO produce código de aplicación, produce **templates, scripts, patterns, y lenses** que otros consumen.

---

## Directory Structure

```
apps/research-autopoietic-template/
│
├── README.md                           # Quick start y overview
├── PROPOSITO.md                        # Purpose y objectives (template original)
├── ISSUE.yaml                          # Issue-spec principal (P3)
├── design.md                           # Arquitectura alto nivel
├── .gitignore                          # Git exclusions
│
├── .spec-workflow/                     # Configuración spec-workflow-mcp
│   ├── config.toml                     # [PENDING] Tzimtzum config
│   ├── steering/                       # [√] Strategic documents
│   │   ├── structure.md                # [√] Este archivo
│   │   ├── product.md                  # [PENDING] Vision y roadmap
│   │   └── tech.md                     # [PENDING] Stack y dependencies
│   │
│   ├── specs/                          # Specifications
│   │   └── autopoietic-templates/      # [√] Este spec
│   │       ├── ISSUE.yaml              # [PENDING] Symlink a root
│   │       ├── spec-config.yaml        # [√] Lenses, patterns, rostros
│   │       ├── design.md               # [PENDING] Symlink a root
│   │       ├── tasks.md                # [PENDING] Auto-generado
│   │       └── requirements/
│   │           └── requirements.md     # [PENDING] Symlink a 010-define/
│   │
│   ├── approvals/                      # [PENDING] Approval requests
│   └── archive/                        # [PENDING] Closed specs
│
├── .melquisedec/                       # [√] Knowledge management (P6)
│   ├── domain/                         # [√] Triple persistencia
│   │   ├── markdown/                   # [√] Concepts sobre templates/patterns
│   │   ├── cypher/                     # [√] Graph queries
│   │   └── embeddings/                 # [√] Vector embeddings
│   │
│   ├── lessons/                        # [√] P2 Autopoiesis
│   │   ├── checkpoint-lessons/         # [√] CK-01, CK-02, etc.
│   │   ├── phase-lessons/              # [PENDING] 010, 020, etc.
│   │   └── consolidated/               # [√] ALMA aggregations
│   │
│   ├── logs/                           # [√] P5 Validación
│   │   ├── validation-logs/            # [PENDING] Checkpoint validations
│   │   ├── sync-logs/                  # [PENDING] Triple persistence syncs
│   │   └── autopoiesis-logs/           # [PENDING] Pattern evolution
│   │
│   └── context/                        # [√] Smart-thinking MCP
│       ├── sessions/                   # [PENDING] MCP sessions
│       ├── thoughts/                   # [PENDING] Sequential thinking
│       └── memories/                   # [PENDING] Persistent context
│
├── 010-define/                         # [√] Phase 1: Definition (MELQUISEDEC)
│   ├── requirements.md                 # [√] RBM-GAC detailed
│   ├── design.md                       # [PENDING] Symlink a root
│   └── ISSUE.yaml                      # [PENDING] Symlink a root
│
├── 020-conceive/                       # [√] Phase 2: Conception (HYPATIA)
│   ├── 01-literature/                  # [√] Papers, books, references
│   │   ├── dsr/                        # [PENDING] Design Science Research
│   │   ├── autopoiesis/                # [PENDING] Maturana & Varela
│   │   ├── ddd/                        # [PENDING] Domain-Driven Design
│   │   └── zettelkasten/               # [PENDING] Zettelkasten method
│   │
│   ├── 02-atomics/                     # [√] Atomic notes (Zettelkasten)
│   │   ├── concepts/                   # [PENDING] ≥20 atomics required
│   │   ├── connections/                # [PENDING] Links between atomics
│   │   └── index.md                    # [PENDING] MOC (Map of Content)
│   │
│   ├── 03-datasets/                    # [PENDING] Feedback data
│   │   └── feedback-examples/          # [PENDING] Template mejoras
│   │
│   ├── 04-artifacts/                   # [PENDING] Intermediate outputs
│   │   └── pattern-drafts/             # [PENDING] Early patterns
│   │
│   └── 05-outputs/                     # [PENDING] Phase deliverables
│       └── literature-review.md        # [PENDING] Synthesis
│
├── 030-design/                         # [√] Phase 3: Design (SALOMON)
│   ├── architecture/                   # [√] System design
│   │   ├── template-structure.md       # [PENDING] Template anatomy
│   │   ├── autopoiesis-flow.md         # [PENDING] Feedback loop
│   │   └── diagrams/                   # [PENDING] Mermaid diagrams
│   │
│   ├── workbook/                       # [PENDING] Design workbook
│   │   └── design-sessions.md          # [PENDING] Design thinking sessions
│   │
│   ├── adrs/                           # [√] Architectural Decision Records
│   │   ├── ADR-001-pattern-confidence-formula.md    # [PENDING] ≥5 ADRs
│   │   ├── ADR-002-feedback-aggregator-location.md  # [PENDING]
│   │   └── template.md                              # [PENDING] ADR template
│   │
│   └── specifications/                 # [√] Detailed specs
│       ├── script-specs/               # [PENDING] Specs for 6 scripts
│       └── pattern-specs/              # [PENDING] Specs for patterns
│
├── 040-build/                          # [√] Phase 4: Build (MORPHEUS)
│   └── research/                       # [√] Implementation artifacts
│       ├── templates/                  # [PENDING] Template implementations
│       ├── scripts/                    # [PENDING] 6 scripts lifecycle
│       └── tests/                      # [PENDING] Unit tests
│
├── 050-release/                        # [√] Phase 5: Release (ALMA)
│   └── outputs/                        # [√] **PRIMARY DELIVERABLES**
│       ├── templates/                  # [√] Published templates
│       │   └── research-autopoietic/
│       │       └── v4.3.1/             # [√] Version directory
│       │           └── [PENDING] template files
│       │
│       ├── scripts/                    # [√] Lifecycle scripts
│       │   ├── init-spec.py            # [PENDING] Init new project
│       │   ├── validate-checkpoint.py  # [PENDING] Validate CK
│       │   ├── consolidate-lessons.py  # [PENDING] Aggregate lessons
│       │   ├── autopoiesis-analyze.py  # [PENDING] Process feedback
│       │   ├── generate-tasks-md.py    # [PENDING] Auto-gen tasks.md
│       │   └── sync-triple-persistence.py  # [PENDING] Sync md→graph→vector
│       │
│       ├── patterns/                   # [√] Validated patterns
│       │   ├── PATTERN-001-six-phase-lifecycle.yaml      # [PENDING]
│       │   ├── PATTERN-002-issue-spec-sot.yaml           # [PENDING]
│       │   ├── PATTERN-007-triple-persistence.yaml       # [PENDING]
│       │   ├── PATTERN-012-feedback-aggregator.yaml      # [PENDING]
│       │   └── PATTERN-015-confidence-scoring.yaml       # [PENDING]
│       │
│       └── lenses/                     # [√] Methodology lenses
│           ├── research-methodologies/ # [PENDING] DSR, Zettelkasten
│           └── architecture-styles/    # [PENDING] DDD, Event Sourcing
│
└── 060-reflect/                        # [√] Phase 6: Reflect (MELQUISEDEC)
    ├── feedback-aggregator/            # [√] **CRITICAL FOR AUTOPOIESIS**
    │   ├── research-keter-migration/   # [PENDING] Feedback from keter
    │   │   └── template-improvements.md
    │   ├── research-neo4j/             # [PENDING] Feedback from neo4j
    │   │   └── template-improvements.md
    │   └── aggregation-log.md          # [PENDING] Analysis log
    │
    └── new-issues/                     # [√] Next iteration
        └── ISSUE-SPEC-002-vXXX.yaml    # [PENDING] Future specs
```

---

## Current Status (Phase 010-define)

### Completed (✅)
- [x] ISSUE.yaml created (RBM-GAC problem structure)
- [x] design.md created (architecture + lifecycle)
- [x] requirements.md created (detailed RBM-GAC)
- [x] spec-config.yaml created (lenses, patterns, rostros, checkpoints)
- [x] Directory structure 010-060 created
- [x] .melquisedec/ structure created
- [x] .spec-workflow/ structure created
- [x] steering/structure.md (this file)

### In Progress (🔄)
- [ ] .spec-workflow/steering/product.md (vision, roadmap)
- [ ] .spec-workflow/steering/tech.md (stack, dependencies)
- [ ] .spec-workflow/config.toml (tzimtzum config)
- [ ] Create symlinks (ISSUE.yaml, design.md, requirements.md)
- [ ] Generate tasks.md from spec-config.yaml
- [ ] README.md update with quick start

### Pending CK-01 Validation
- [ ] All required files exist in expected paths
- [ ] ISSUE.yaml parseable and complete
- [ ] requirements.md covers ≥80% expected sections
- [ ] design.md includes architecture + lifecycle + metrics
- [ ] Run: `python validate-checkpoint.py --checkpoint CK-01`

---

## Key Relationships

### Inputs (What This Project Consumes)
- **Manifiesto Melquisedec:** Principios P1-P10 guían diseño
- **Principios Tzimtzum:** Workflow incremental y rostros
- **v4.3.1 Draft:** Self-reference, esta guía es punto de partida
- **Feedback from Projects:** research-keter-migration, research-neo4j

### Outputs (What This Project Produces)
- **Templates:** Estructura 010-060 + archivos config versionados
- **Scripts:** 6 scripts lifecycle automatizados
- **Patterns:** ≥8 patterns con confidence scores ≥0.80
- **Lenses:** Metodologías aplicables (DSR, DDD, Zettelkasten, etc.)

### Consumers (Who Uses These Outputs)
- **research-keter-migration:** Adopta templates y provee feedback
- **research-neo4j-llamaindex-architecture:** Adopta templates
- **Future Research Projects:** En `apps/research-*`

---

## Autopoiesis Cycle

```
┌─────────────────────────────────────────────────────────┐
│ 1. Projects USE templates from 050-release/outputs/    │
│    └─> Copy structure, follow lifecycle                │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 2. Projects ENCOUNTER issues/improvements               │
│    └─> Document in template-improvements.md            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 3. Projects SEND feedback to 060-reflect/feedback-     │
│    aggregator/{project-name}/                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 4. MELQUISEDEC ANALYZES feedback                        │
│    └─> python autopoiesis-analyze.py --aggregate       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 5. PATTERNS UPDATED with new confidence scores          │
│    └─> Evidence added, ADRs created if needed          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 6. NEW VERSION released (v4.3.2, v4.4.0, etc.)         │
│    └─> Templates in 050-release/outputs/templates/     │
└────────────────────┬────────────────────────────────────┘
                     │
                     └──────────────┐
                                    ↓
                              [LOOP CONTINUES]
```

---

## Evolution Notes

**Version History:**
- **v0.1.0 (2024-01):** Initial structure, phase 010-define inception
- **v0.2.0 (planned):** After CK-02, with ≥20 atomics and literature review
- **v0.3.0 (planned):** After CK-03, with ≥5 ADRs and architecture
- **v1.0.0 (planned):** After CK-05, first public release with outputs

**Known Gaps (to address in future phases):**
- No scripts implemented yet (040-build)
- No real feedback yet (060-reflect needs ≥1 adopting project)
- Confidence scores are initial estimates (need empirical validation)
- Triple persistence not populated (020-conceive will initialize)

**Self-Referential Bootstrap:**
This structure itself is the first output of applying v4.3.1 thinking. As we work through phases 010-060, improvements discovered will feed back into v4.3.1+ design. The structure document you're reading will evolve as the project does.

---

## Quick Navigation

- **Problem Definition:** See [ISSUE.yaml](../../ISSUE.yaml)
- **Architecture:** See [design.md](../../design.md)
- **Detailed Requirements:** See [010-define/requirements.md](../../010-define/requirements.md)
- **Configuration:** See [.spec-workflow/specs/autopoietic-templates/spec-config.yaml](../specs/autopoietic-templates/spec-config.yaml)
- **Outputs (when ready):** See [050-release/outputs/](../../050-release/outputs/)

---

**Maintained by:** MELQUISEDEC (010-define, 060-reflect)
**Next Update:** After completing CK-01 validation
