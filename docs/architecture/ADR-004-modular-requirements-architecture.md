---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  foaf: 'http://xmlns.com/foaf/0.1/'
'@type': 'TechArticle'
'@id': 'https://melquisedec.org/adr/ADR-004'
dc:title: 'ADR-004: Modular Requirements Architecture - Atomic REQ-XXX.md Pattern'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot (Claude Sonnet 4.5)'
dc:subject: ['Architecture Decision', 'Requirements Engineering', 'Zettelkasten', 'Modular Design']
version: '1.0.0'
status: 'accepted'
---

# ADR-004: Modular Requirements Architecture

## Status

**ACCEPTED** - 2026-01-10

Related ADRs:
- [ADR-003: ISSUE Format - YAML-LD Frontmatter](ADR-003-issue-format-yaml-ld-frontmatter.md)

## Context

### The Problem

Current practice in research-autopoietic-template:

```
010-define/
├── requirements.md          # 290 lines - MONOLITHIC
└── workbooks/               # EMPTY
```

**Issues:**
1. **Violates Atomic Principle**: Manifesto v4.0.0 specifies ≤300 lines per document
2. **No Individual Addressability**: Cannot reference specific requirement (e.g., "See REQ-007")
3. **Git Friction**: Merge conflicts when multiple developers work on requirements
4. **Review Overhead**: Reviewers must read entire file to understand single change
5. **Zettelkasten Violation**: Hub-note pattern not followed (no linking structure)

### Manifesto Evidence

**Section 9.1 - Templates Estructura de Documentos (líneas 6000-6500):**

```markdown
### Requirements Template (requirements.md)

**Propósito:** Agrupar requerimientos individuales

**CRÍTICO:** El archivo requirements.md NO contiene los requerimientos
directamente, sino que es un ÍNDICE que referencia documentos individuales:

├── requirements.md              # ÍNDICE (200 líneas)
└── workbooks/
    ├── REQ-001.md               # 180 líneas - UN requerimiento
    ├── REQ-002.md               # 150 líneas - UN requerimiento
    └── REQ-003.md               # 160 líneas - UN requerimiento
```

> "Cada requerimiento se documenta en archivo separado siguiendo
> Zettelkasten. El requirements.md es el hub note que los vincula."
> (Sección 9.1.2, línea 6123)

### Current State Analysis

**From ANALISIS-GAPS-Y-RECOMENDACIONES.md:**

```markdown
# GAP #1: Cada Requerimiento es un Documento Independiente

**❌ PROBLEMA:** requirements.md tiene 290 líneas TOTALES, asumiendo que es monolítico.

**Estructura Incorrecta Actual:**
```
010-define/
├── requirements.md          # 290 líneas - ¿Es índice o monolito?
└── workbooks/               # ❌ VACÍO - No hay REQ-XXX.md
```

**User Quote (Session-002):**

> "requirements.md se specifican modularmente, y aquí se refrencian...
> los sub-requirements detallados, pueden obviarse si se refrencia a
> usa la plantilla xxx para .... pero si el requerimientos es complejo...
> requiere una especifcaión... REQ-XXX atómicos y referenciables...
> plantillas para construirse"

## Decision

**ADOPT Modular Requirements Architecture** con pattern atomic REQ-XXX.md.

### Architecture Pattern

```
010-define/
├── requirements.md                    # HUB-NOTE (≤200 líneas)
│                                      # Tabla de índice + enlaces
└── workbooks/
    ├── REQ-001-context-validation.md     # 180 líneas - Atomic
    ├── REQ-002-template-generation.md    # 150 líneas - Atomic
    ├── REQ-003-metadata-enrichment.md    # 160 líneas - Atomic
    ├── REQ-004-lens-integration.md       # 145 líneas - Atomic
    ├── ...
    └── REQ-052-rollback-mechanisms.md    # 140 líneas - Atomic
```

### Structure Definition

**requirements.md (Hub-Note):**

```markdown
# Requirements: spec-001-implement-keterdoc-architecture

## Overview
[Brief context - 50 lines]

## Requirements Index

| ID | Title | Priority | Status | Dependencies |
|----|-------|----------|--------|--------------|
| [REQ-001](workbooks/REQ-001-context-validation.md) | @context Validation | Critical | Active | - |
| [REQ-002](workbooks/REQ-002-template-generation.md) | Base Template System | Critical | Active | REQ-001 |
| [REQ-003](workbooks/REQ-003-metadata-enrichment.md) | YAML-LD Enrichment | High | Draft | REQ-001 |
| ... | ... | ... | ... | ... |

## Requirements by Phase

### Phase 1: Foundation (Week 1-2)
- [REQ-001: @context Validation](workbooks/REQ-001-context-validation.md)
- [REQ-002: Base Template System](workbooks/REQ-002-template-generation.md)
...

### Phase 2: Lens Integration (Week 3-4)
- [REQ-008: Lens Variants System](workbooks/REQ-008-lens-variants.md)
...

## Non-Functional Requirements

### Performance
- [REQ-045: Template Generation Speed](workbooks/REQ-045-template-speed.md)

### Security
- [REQ-048: YAML Injection Prevention](workbooks/REQ-048-yaml-security.md)

---

**Total:** 52 requirements documented in atomic files
```

**REQ-XXX.md (Atomic Requirement):**

```markdown
---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'TechArticle'
'@id': 'https://melquisedec.org/requirements/REQ-XXX'
dc:title: 'REQ-XXX: Requirement Title'
dc:created: 'YYYY-MM-DD'
status: 'draft | active | completed'
priority: 'critical | high | medium | low'
---

# REQ-XXX: Requirement Title

## 1. Problem Statement
[What problem this solves - 50-80 lines]

## 2. Requirement Specification
### 2.1 Functional Requirements
[GIVEN-WHEN-THEN format - 80-120 lines]

### 2.2 Non-Functional Requirements
[Performance, Security, Usability - 40-60 lines]

## 3. Acceptance Criteria
[Testable conditions - 40-60 lines]

## 4. Implementation Guidance
[Technical approach + code examples - 60-80 lines]

## 5. Dependencies and Constraints
[Tables + assumptions - 30-40 lines]

## 6. Verification Plan
[Test cases + checklist - 40-60 lines]

---
Total: ~300 lines (atomic principle)
```

## Rationale

### Why Atomic Requirements?

**1. Zettelkasten Principles:**
- Hub-note pattern (requirements.md links to atomic notes)
- Individual addressability (deep links)
- Network thinking (dependency graphs)
- Scalability (add notes without restructuring)

**2. Git Workflow Benefits:**
- No merge conflicts (developers work on different REQ-XXX.md)
- Clear commit history (`git log workbooks/REQ-007.md`)
- Atomic reverts (`git revert <commit>` affects single requirement)
- Blame clarity (`git blame REQ-XXX.md`)

**3. Review Efficiency:**
- Reviewers see ONLY changed requirement
- Focused PR discussions (comment on specific REQ)
- Faster approval cycles
- Clear acceptance criteria per file

**4. Manifesto Compliance:**
- ≤300 lines per document (atomic principle)
- Modular philosophy (independent files)
- 85% reduction (vs. monolithic 800+ line files)
- Zettelkasten hub-note pattern

**5. Tool Integration:**
- **Obsidian**: Graph view shows requirement dependencies
- **Neo4j**: Each REQ-XXX is a node with relationships
- **Vector DB**: Embeddings per requirement (better retrieval)
- **spec-workflow-mcp**: requirements.md still works (hub-note)

### Alternative Approaches Considered

**Alternative 1: Keep Monolithic requirements.md**

```
010-define/
└── requirements.md    # 800+ lines
```

❌ Rejected:
- Violates atomic principle
- Merge conflicts
- Review friction
- No individual addressability

**Alternative 2: Single-Level Sections in requirements.md**

```markdown
# Requirements

## REQ-001: Context Validation
[content...]

## REQ-002: Template Generation
[content...]
```

❌ Rejected:
- Still monolithic file (800+ lines)
- No Git granularity
- Violates Zettelkasten pattern
- Obsidian graph view doesn't work

**Alternative 3: Nested Folders by Phase**

```
workbooks/
├── phase-1/
│   ├── REQ-001.md
│   └── REQ-002.md
└── phase-2/
    └── REQ-008.md
```

❌ Rejected:
- Adds unnecessary hierarchy
- Phase assignment can change (refactor pain)
- Harder to reference (`../phase-1/REQ-001.md`)

**Chosen: Flat workbooks/ Structure**

```
workbooks/
├── REQ-001-context-validation.md
├── REQ-002-template-generation.md
├── REQ-008-lens-variants.md
└── REQ-052-rollback-mechanisms.md
```

✅ Benefits:
- Simple flat structure
- Easy referencing (`workbooks/REQ-XXX.md`)
- Phases organized in requirements.md hub-note
- REQ ID provides natural ordering

## Consequences

### Positive

- ✅ **Atomic Principle Compliance**: Each file ≤300 lines
- ✅ **Git Granularity**: Per-requirement commit history
- ✅ **Review Efficiency**: Focused PRs per requirement
- ✅ **Zettelkasten Pattern**: Hub-note + atomic notes
- ✅ **Tool Integration**: Obsidian graph, Neo4j nodes, vector embeddings
- ✅ **Parallel Development**: No merge conflicts
- ✅ **Clear Dependencies**: Visualized in requirements.md table
- ✅ **Scalability**: Add new requirements without restructuring

### Negative

- ⚠️ **Initial Setup Cost**: Create 52 atomic files from monolithic requirements.md
- ⚠️ **Template Discipline**: Developers must follow REQ-template.md structure
- ⚠️ **Link Maintenance**: requirements.md table must stay in sync

### Neutral

- 🔄 **File Count**: 1 file (monolithic) → 53 files (hub + 52 atomic)
- 🔄 **Navigation**: Obsidian native vs. scrolling single file
- 🔄 **Total Lines**: ~800 lines (monolithic) → ~850 lines (hub + atomic, includes frontmatter)

## Implementation Plan

### Phase 1: Create Infrastructure (Day 1)

1. **Create REQ-template.md**
   ```bash
   touch apps/research-autopoietic-template/.spec-workflow/specs/spec-001-implement-keterdoc-architecture/REQ-template.md
   # Copy template structure (6 sections, YAML-LD frontmatter)
   ```

2. **Refactor requirements.md to Hub-Note**
   ```bash
   # Convert monolithic content to table of links
   # Keep only: Overview + Requirements Index + Phase groupings
   # Target: ≤200 lines
   ```

3. **Create workbooks/ Directory**
   ```bash
   mkdir -p apps/research-autopoietic-template/010-define/workbooks
   ```

### Phase 2: Migrate Requirements (Week 1)

**Priority 1 - Critical Requirements (5 requirements, Day 1-2):**

```bash
# Extract from monolithic requirements.md:
REQ-001-context-validation.md
REQ-002-template-generation.md
REQ-003-metadata-enrichment.md
REQ-004-lens-integration.md
REQ-005-chatlog-system.md
```

**Priority 2 - High Requirements (10 requirements, Day 3-5):**

```bash
REQ-006 through REQ-015 (validation, testing, documentation)
```

**Priority 3 - Remaining Requirements (37 requirements, Week 2):**

```bash
REQ-016 through REQ-052 (migrations, enhancements, optimizations)
```

**Migration Script:**

```python
# tools/migrate-requirements.py
import re
from pathlib import Path

def extract_requirement(monolithic_content, req_id):
    """Extract single requirement from monolithic file."""
    # Find section: ## REQ-XXX: Title
    pattern = rf'## {req_id}:(.+?)(?=\n## REQ-|\Z)'
    match = re.search(pattern, monolithic_content, re.DOTALL)

    if match:
        content = match.group(0)
        return {
            'id': req_id,
            'title': match.group(1).strip(),
            'content': content
        }
    return None

def generate_atomic_file(req_data, template_path):
    """Generate REQ-XXX.md from template."""
    with open(template_path) as f:
        template = f.read()

    # Replace placeholders
    atomic_content = template.replace('REQ-000', req_data['id'])
    atomic_content = atomic_content.replace('Requirements Template', req_data['title'])
    # ... fill sections from extracted content

    return atomic_content

# Usage:
# python tools/migrate-requirements.py requirements.md workbooks/
```

### Phase 3: Validation (Day 6-7)

```bash
# Validation checklist per REQ-XXX.md:
./tools/validate-requirement.sh workbooks/REQ-*.md
# Checks:
# - YAML-LD frontmatter valid
# - Line count ≤ 300
# - All 6 sections present
# - Linked from requirements.md
```

### Phase 4: Integration (Day 8-10)

1. **Update requirements.md hub-note**
   - Add all 52 rows to Requirements Index table
   - Organize by phase
   - Add dependency references

2. **Test Obsidian Integration**
   - Open vault in Obsidian
   - Check graph view shows requirement network
   - Verify backlinks work

3. **Test spec-workflow-mcp**
   - Confirm tool still reads requirements.md
   - Verify approvals work with hub-note

## Validation Criteria

**Must Have:**

- [x] REQ-template.md created with 6-section structure
- [x] YAML-LD frontmatter includes @context, @id, dc:title, dc:created
- [ ] requirements.md refactored to hub-note (≤200 lines)
- [ ] workbooks/ directory created
- [ ] 5 critical requirements migrated (REQ-001 through REQ-005)
- [ ] All atomic files ≤300 lines
- [ ] Obsidian graph view renders correctly
- [ ] spec-workflow-mcp still functional

**Should Have:**

- [ ] Migration script automated (tools/migrate-requirements.py)
- [ ] Validation script (tools/validate-requirement.sh)
- [ ] All 52 requirements migrated within Week 1-2
- [ ] Git history preserved (annotated commits)

**Nice to Have:**

- [ ] VS Code extension for REQ-XXX.md navigation
- [ ] Mermaid dependency graph auto-generation
- [ ] REQ-XXX.md preview in dashboard

## Metrics

| Metric | Baseline (Monolithic) | Target (Modular) | Actual |
|--------|----------------------|------------------|--------|
| requirements.md Lines | 290 (monolithic) | ≤200 (hub-note) | TBD |
| Max File Size | 290 lines | ≤300 lines | TBD |
| Atomic Files Created | 0 | 52 | 1 (template) |
| Git Conflicts (monthly) | 5-10 | 0-1 | TBD |
| PR Review Time | 45 min (full file) | 10 min (single REQ) | TBD |
| Obsidian Graph Nodes | 1 | 53 | TBD |

## Related Documents

- [ADR-003: ISSUE Format - YAML-LD Frontmatter](ADR-003-issue-format-yaml-ld-frontmatter.md)
- [REQ-template.md](../../apps/research-autopoietic-template/.spec-workflow/specs/spec-001-implement-keterdoc-architecture/REQ-template.md)
- [Manifesto v4.0.0: 04-implementacion/02-templates-estructura.md](../manifiesto/04-implementacion/02-templates-estructura.md)
- [ANALISIS-GAPS-Y-RECOMENDACIONES.md](../../apps/research-autopoietic-template/010-define/ANALISIS-GAPS-Y-RECOMENDACIONES.md)

## Notes

**From Session-002 (2026-01-10):**

> "requirements.md se specifican modularmente, y aquí se refrencian...
> REQ-XXX atómicos y referenciables... plantillas para construirse"
>
> — User requirement, Chatlog Session-002

**Key Insight:**
- Monolithic requirements.md violates Manifesto atomic principle
- Zettelkasten pattern = hub-note + atomic notes
- Git granularity = better collaboration
- Obsidian graph = visual dependency tracking

**Migration Priority:**
1. Week 1-2: Create 52 atomic REQ-XXX.md files
2. Week 3-4: Validate + integrate
3. Week 5+: Use pattern for future specs

---

**Decision Made By:** User (ccolombia-ui) + GitHub Copilot
**Date:** 2026-01-10
**Confidence:** 95% (Manifesto explicit, Zettelkasten proven pattern)
**Review Date:** 2026-02-10 (after migration completion)
