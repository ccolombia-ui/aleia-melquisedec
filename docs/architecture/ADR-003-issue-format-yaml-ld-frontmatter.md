---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  foaf: 'http://xmlns.com/foaf/0.1/'
'@type': 'TechArticle'
'@id': 'https://melquisedec.org/adr/ADR-003'
dc:title: 'ADR-003: ISSUE Format - Markdown with YAML-LD Frontmatter'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot (Claude Sonnet 4.5)'
dc:subject: ['Architecture Decision', 'KeterDoc', 'YAML-LD', 'Semantic Web']
version: '1.0.0'
status: 'accepted'
---

# ADR-003: ISSUE Format - Markdown with YAML-LD Frontmatter

## Status

**ACCEPTED** - 2026-01-10

Supersedes: Previous ISSUE.yaml format in research-autopoietic-template

## Context

### The Problem

MELQUISEDEC tiene dos formatos en uso:
- **ISSUE.yaml** (research-autopoietic-template): Pure YAML, 200 líneas, 20+ template references
- **KeterDoc Proposal** (Manifesto v4.0.0): Markdown con YAML-LD frontmatter para semantic web

### Investigation Findings

**spec-workflow-mcp Research (Perplexity + GitHub):**
- spec-workflow-mcp **NO TIENE opinión** sobre ISSUE.* format
- Flujo oficial: `requirements.md → design.md → tasks.md` (3 archivos)
- ISSUE.* es **adición MELQUISEDEC** para trazabilidad

**Current State:**
- 20+ references to ISSUE.yaml in `.spec-workflow/_meta/`
- `workflow-patterns.yaml`: "Generar ISSUE.yaml desde template-base"
- `instantiation-rules.yaml`: Path pattern expects YAML
- research-autopoietic-template/ISSUE.yaml en producción

**KeterDoc Requirements (Manifesto 02-arquitectura/03-templates-hkm.md):**
```yaml
---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'TechArticle'
'@id': 'https://melquisedec.org/...'
dc:title: '...'
dc:created: 'YYYY-MM-DD'
version: '1.0.0'
---
```

## Decision

**ADOPT ISSUE.md with YAML-LD Frontmatter** como estándar MELQUISEDEC.

### Rationale

**Razones Estratégicas:**

1. **Semantic Web Integration**
   - YAML-LD frontmatter habilita triple store (Neo4j, Oxigraph)
   - Embeddings con metadata semántica enriquecida
   - SPARQL queries sobre knowledge graph
   - JSON-LD export para interoperabilidad

2. **Obsidian Native**
   - Obsidian renderiza frontmatter + Markdown seamlessly
   - Graph view con relationships semánticas
   - Dataview queries sobre YAML-LD
   - Backlinks con contexto semántico

3. **Manifesto Alignment**
   - KeterDoc standard documentado (575 líneas en Manifesto)
   - Modular philosophy (Markdown > YAML para legibilidad)
   - 85% reduction principle (Markdown más conciso que YAML puro)
   - Human-first, machine-readable second

4. **Innovation > Compatibility**
   - spec-001 es **baseline** para futuras investigaciones
   - Breaking changes ahora evitan deuda técnica futura
   - Templates se migran una vez, beneficios perpetuos
   - First-mover advantage en semantic research workflows

**Trade-offs Aceptados:**

| Costo | Beneficio |
|-------|-----------|
| Migrar 20+ templates | Semantic web capabilities |
| Actualizar instantiation-rules | Obsidian native experience |
| Re-entrenar workflow patterns | KeterDoc compliance |
| Documentar nuevo estándar | Future-proof architecture |

**Rechazado: ISSUE.yaml**
- ❌ No soporta YAML-LD (plain YAML)
- ❌ No integra con Obsidian graph view
- ❌ Difícil de leer para humanos (200+ líneas)
- ❌ No cumple KeterDoc standard

## Consequences

### Positive

- ✅ **Semantic Web Ready**: Triple persistence desde día 1
- ✅ **Obsidian Graph View**: Relationships visuales automáticas
- ✅ **Embeddings Quality**: Metadata YAML-LD enriquece vectores
- ✅ **Manifesto Compliance**: KeterDoc fully implemented
- ✅ **Human-Readable**: Markdown body > YAML blocks
- ✅ **Future-Proof**: JSON-LD export, SPARQL queries

### Negative

- ⚠️ **Template Migration**: 20+ archivos en `.spec-workflow/_meta/`
- ⚠️ **Breaking Change**: specs anteriores usan ISSUE.yaml
- ⚠️ **Learning Curve**: Team debe entender YAML-LD

### Neutral

- 🔄 **spec-workflow-mcp**: Sin impacto (herramienta agnóstica a ISSUE.*)
- 🔄 **File Size**: Similar (~200 líneas YAML vs ~180 MD + frontmatter)

## Implementation

### Phase 1: spec-001 Adoption (Immediate)

```
apps/research-autopoietic-template/.spec-workflow/specs/spec-001-implement-keterdoc-architecture/
├── ISSUE.md          ← NEW STANDARD (YAML-LD frontmatter)
├── requirements.md
├── design.md
└── spec-config.yaml
```

**ISSUE.md Structure:**
```markdown
---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Issue'
'@id': 'https://melquisedec.org/issues/spec-001'
dc:title: '...'
---

# Problem Statement
...

# Gap Analysis
...

# Goals and Outcomes
...
```

### Phase 2: Template Migration (Week 3-4)

**Files to Update:**
1. `.spec-workflow/_meta/templates/issue-types/*.yaml` → `*.md`
2. `.spec-workflow/_meta/workflows/workflow-patterns.yaml`:
   ```yaml
   - action: "Generar ISSUE.md desde template-base"  # Changed from ISSUE.yaml
   ```
3. `.spec-workflow/_meta/workflows/instantiation-rules.yaml`:
   ```yaml
   path_pattern: ".spec-workflow/{type}-{number}-{name}/ISSUE.md"  # Changed
   ```

### Phase 3: Documentation (Week 5)

- [ ] Update `_templates/daath-zen-patterns/` with ISSUE.md examples
- [ ] Create migration guide: ISSUE.yaml → ISSUE.md
- [ ] Document YAML-LD frontmatter in Manifiesto
- [ ] Add JSON-LD validation to CI/CD

## Validation Criteria

**Must Have:**
- [x] ISSUE.md created in spec-001
- [x] YAML-LD frontmatter validates with JSON-LD Playground
- [x] Obsidian renders correctly
- [ ] Neo4j ingestion script accepts YAML-LD
- [ ] Vector embeddings include metadata
- [ ] Template migration plan documented

## Related Documents

- [ADR-001: Monorepo Structure](ADR-001-monorepo-structure.md)
- [ADR-002: Keter Integration Decision](ADR-002-keter-integration-decision.md)
- [Manifesto v4.0.0: 02-arquitectura/03-templates-hkm.md](../manifiesto/02-arquitectura/03-templates-hkm.md)
- [spec-001 ISSUE.md](../../apps/research-autopoietic-template/.spec-workflow/specs/spec-001-implement-keterdoc-architecture/ISSUE.md)

## Notes

**From Session-002 (2026-01-10):**

> "ISSUE.md con YAML-LD sería innovación correcta (KeterDoc adoption)
> prefiero innovación, de hecho esto nos mejora la capacidad de la metadata
> para los emdebbings, grafos, con md... así que se queda... esta es la
> primera investigación cn el nuevo estandar, las demas deberán depender de ella..."
>
> — User decision, Chatlog Session-002

**Key Insight:**
- spec-workflow-mcp es **herramienta**, no **estándar**
- MELQUISEDEC define su propio formato (ISSUE.md)
- Tool compatibility > tool dependency
- Innovation requires breaking changes

---

**Decision Made By:** User (ccolombia-ui) + GitHub Copilot
**Date:** 2026-01-10
**Confidence:** 95% (based on Manifesto alignment + semantic web benefits)
**Review Date:** 2026-02-10 (after Phase 2 completion)
