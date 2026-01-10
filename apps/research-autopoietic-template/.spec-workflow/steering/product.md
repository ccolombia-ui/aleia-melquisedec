# Product Vision - Research Autopoietic Templates

> **Document Type:** Strategic Product Definition
> **Owner:** MELQUISEDEC
> **Status:** Living Document
> **Last Updated:** 2024-01 (Phase 010-define)

---

## Vision Statement

**Crear un sistema de templates autopoiéticos que evolucionen basados en feedback empírico de múltiples proyectos de investigación, reduciendo el tiempo de setup de 8h a 2h mientras mantienen consistencia cross-proyecto y trazabilidad completa.**

---

## Problem Space

### Current Pain Points

1. **Inconsistencia Cross-Proyecto:**
   - Cada proyecto research reinventa estructura
   - Sin formato estándar para ISSUE.yaml, requirements, etc.
   - Patterns descubiertos no se propagan a otros proyectos

2. **Alto Tiempo de Setup:**
   - ~8 horas para estructurar proyecto research desde cero
   - Configurar .spec-workflow/, .melquisedec/, triple persistencia manualmente
   - Re-aprender convenciones cada vez

3. **Pérdida de Conocimiento:**
   - Mejoras descubiertas en proyectos no retroalimentan templates
   - Sin sistema para capturar y agregar feedback
   - Lessons-learned quedan aisladas en cada proyecto

4. **Falta de Validación:**
   - Templates no tienen confidence scores
   - No se sabe qué patterns funcionan en la práctica
   - Sin métricas de adopción o efectividad

### Stakeholders

**Primary Users:**
- **Investigadores (Yo mismo):** Crean proyectos research en `apps/`
- **MELQUISEDEC (Rostro):** Define problemas y analiza autopoiesis
- **HYPATIA (Rostro):** Usa templates para literature review y atomics
- **SALOMON (Rostro):** Usa templates para ADRs y arquitectura
- **MORPHEUS (Rostro):** Implementa siguiendo structure templates
- **ALMA (Rostro):** Consolida lessons usando template patterns

**Secondary Users:**
- **Futuros Proyectos Research:** Adoptan templates mejorados
- **Comunidad (potencial):** Si templates se publican como open-source

---

## Product Goals

### North Star Metric
**Tiempo de setup nuevo proyecto research: ≤2 horas** (desde 8h baseline)

### Supporting Metrics

| Métrica | Baseline | Target | Medición |
|---------|----------|--------|----------|
| **Proyectos usando templates** | 0 | ≥2 | Count en `apps/research-*` |
| **Feedback recibido** | 0 | ≥5 mejoras documentadas | Count en `060-reflect/feedback-aggregator/` |
| **Patterns validados** | 0 | ≥8 con confidence ≥0.80 | Analizar `050-release/outputs/patterns/*.yaml` |
| **Versiones templates** | 0 | ≥3 (v4.3.1, v4.3.2, v4.4.0) | Git tags en repo |
| **ADRs documentados** | 0 | ≥5 | Count en `030-design/adrs/ADR-*.md` |
| **Scripts automatizados** | 0 | ≥6 funcionales | Count en `050-release/outputs/scripts/` |

---

## Product Principles

### 1. Autopoiesis Medida (P2)
**Templates que se auto-mejoran vía feedback empírico.**

- Cada pattern tiene confidence score basado en adopción real
- Feedback loop: proyecto → mejoras → pattern → nueva versión
- Threshold: ≥0.80 para incluir pattern en template publicado
- Formula: `(projects_validated / projects_total) * (adrs_count / 2)`

### 2. Triple Persistencia (P6)
**Conocimiento en 3 formatos: Markdown + Graph + Vector.**

- Conceptos sobre templates/patterns en `.melquisedec/domain/markdown/`
- Relaciones en Neo4j (cypher queries en `.melquisedec/domain/cypher/`)
- Búsqueda semántica vía embeddings (`.melquisedec/domain/embeddings/`)
- Sync automático con `sync-triple-persistence.py`

### 3. Issue-Driven Workflow (P3)
**ISSUE.yaml es source of truth, todo deriva de él.**

- Formato RBM-GAC (Gap, Goal, Outcomes)
- tasks.md auto-generado desde spec-config.yaml
- Checkpoints con criterios verificables
- Trazabilidad: issue → requirements → design → build → release

### 4. Validación Continua (P5)
**Checkpoints previenen avance sin completar criterios.**

- 5 checkpoints (CK-01 through CK-05)
- Script `validate-checkpoint.py` con exit codes
- No avanzar a fase siguiente sin validar anterior
- Lessons capturadas en cada checkpoint

### 5. Modularity & Composition
**Templates se componen de patterns reutilizables.**

- Patterns son bounded contexts (DDD lens)
- Scripts son building blocks independientes
- Lenses se aplican según metodología (DSR, Zettelkasten, DDD, etc.)
- Templates versiones pueden mezclar diferentes sets de patterns

---

## Product Roadmap

### Phase 1: Foundation (010-define, 020-conceive) - Weeks 1-2
**Goal:** Establecer base teórica y conceptual

**Deliverables:**
- [x] ISSUE.yaml con problema RBM-GAC
- [x] requirements.md detallado
- [x] design.md con arquitectura
- [x] spec-config.yaml con lenses y patterns iniciales
- [ ] ≥20 atomics sobre templates, autopoiesis, DSR, DDD
- [ ] Literature review completo
- [ ] Triple persistencia inicializada

**Success Criteria:** CK-01 y CK-02 validados

---

### Phase 2: Design (030-design) - Weeks 3-4
**Goal:** Arquitectura y decisiones documentadas

**Deliverables:**
- [ ] ≥5 ADRs sobre templates (confidence formula, feedback location, etc.)
- [ ] Architecture diagrams (Mermaid) mostrando autopoiesis flow
- [ ] Specifications para 6 scripts
- [ ] Pattern specifications detalladas
- [ ] Patterns actualizados con ADR references

**Success Criteria:** CK-03 validado

---

### Phase 3: Build (040-build) - Weeks 5-6
**Goal:** Implementación templates, scripts, patterns

**Deliverables:**
- [ ] Templates v4.3.1 completos (estructura 010-060)
- [ ] 6 scripts implementados y testeados:
  - `init-spec.py`
  - `validate-checkpoint.py`
  - `consolidate-lessons.py`
  - `autopoiesis-analyze.py`
  - `generate-tasks-md.py`
  - `sync-triple-persistence.py`
- [ ] ≥8 patterns con confidence scores
- [ ] Feedback aggregator funcional

**Success Criteria:** CK-04 validado

---

### Phase 4: Release (050-release) - Week 7
**Goal:** Publicar outputs y aplicar a ≥2 proyectos

**Deliverables:**
- [ ] `050-release/outputs/` publicado con:
  - Templates v4.3.1
  - 6 scripts
  - ≥8 patterns (≥0.80 confidence)
  - Lenses (DSR, Zettelkasten, DDD, Autopoiesis)
- [ ] Aplicar template a `research-keter-migration`
- [ ] Aplicar template a `research-neo4j-llamaindex-architecture`
- [ ] Lessons consolidadas por ALMA
- [ ] README.md con quick start

**Success Criteria:** CK-05 validado, tiempo setup ≤2h medido en 2 proyectos

---

### Phase 5: Reflect & Evolve (060-reflect) - Week 8+
**Goal:** Capturar feedback y liberar v4.3.2+

**Deliverables:**
- [ ] Feedback recibido de ≥2 proyectos en `060-reflect/feedback-aggregator/`
- [ ] `autopoiesis-analyze.py` ejecutado, patterns actualizados
- [ ] New issues para v4.3.2 o v4.4.0
- [ ] Template version mejorada publicada
- [ ] Cycle completo documentado (autopoiesis log)

**Success Criteria:** ≥1 nueva versión liberada basada en feedback real

---

## Features & Capabilities

### MVP (v4.3.1)

**Core Features:**
- ✅ Six-Phase Lifecycle (010-060 structure)
- ✅ ISSUE.yaml format (RBM-GAC)
- ✅ spec-config.yaml with lenses/patterns/rostros
- ✅ .spec-workflow/ structure
- ✅ .melquisedec/ structure (triple persistence)
- ⏳ 6 lifecycle scripts
- ⏳ ≥8 validated patterns
- ⏳ Feedback aggregator

**Out of Scope (MVP):**
- ❌ Web UI para gestionar templates
- ❌ CLI tipo `npm create` (solo scripts Python)
- ❌ Notificaciones automáticas de nuevas versiones
- ❌ CI/CD integration
- ❌ Public marketplace

---

### Future Versions (v4.4.0+)

**v4.4.0 - Advanced Automation:**
- CLI unificado tipo `melq-template create`
- Auto-detection de mejoras (LLM-powered analysis)
- Validación automática en CI/CD
- Dashboard web para ver patterns y confidence

**v5.0.0 - Collaborative Templates:**
- Public template marketplace
- Community-contributed patterns
- Peer review system para patterns
- Cross-organization feedback aggregation

---

## Success Criteria (Product Level)

### Must Have (v4.3.1)
1. ✅ Templates reduce setup time a ≤2h
2. ✅ ≥2 proyectos adoptan templates exitosamente
3. ✅ ≥8 patterns con confidence ≥0.80
4. ✅ Autopoiesis cycle completado (feedback → pattern update → new version)

### Should Have
1. ⏳ ≥5 ADRs documentan decisiones clave
2. ⏳ ≥20 atomics capturados y triple-persistidos
3. ⏳ Scripts testeados y funcionando sin errores
4. ⏳ README con quick start que funciona end-to-end

### Nice to Have
1. ⏳ ≥3 lenses documentados (DSR, DDD, Zettelkasten + Autopoiesis)
2. ⏳ Architecture diagrams visualizing autopoiesis flow
3. ⏳ Examples de uso en diferentes contextos
4. ⏳ Video tutorial de setup

---

## Risk Mitigation

| Risk | Impact | Mitigation Strategy |
|------|--------|---------------------|
| **Self-referential paradox:** Usar v4.3.1 incompleto para diseñarse | High | Bootstrap iterativo: mejorar mientras se usa |
| **Feedback insuficiente:** <2 proyectos adoptan | High | Aplicar proactivamente a keter y neo4j |
| **Complexity creep:** Scripts muy complejos | Medium | MVP simple primero, iterar después |
| **Tiempo estimado incorrecto:** 2h muy ambicioso | Medium | Medir realmente, ajustar objetivo |
| **Scope creep:** Features fuera de MVP | High | Defer a v4.4.0+, strict adherencia a In Scope |

---

## Dependencies & Constraints

### Technical Dependencies
- Python ≥3.10
- Neo4j ≥5.0
- OpenAI API (embeddings)
- spec-workflow-mcp (como referencia, no como npm package)

### Organizational Constraints
- Monorepo: Templates permanecen en `apps/research-autopoietic-template/`
- Solo yo como usuario inicial (validar con 1 persona antes de escalar)
- No external dependencies (standalone templates)

### Timeline Constraints
- 8 weeks para v4.3.1 completo (010 through 060)
- CK-01 completar en semana 1

---

## Communication Plan

### Internal (Rostros)
- **MELQUISEDEC:** Define problema, analiza feedback (010, 060)
- **HYPATIA:** Research, atomics, literatura (020)
- **SALOMON:** Arquitectura, ADRs (030)
- **MORPHEUS:** Build scripts y templates (040)
- **ALMA:** Consolidate lessons, publish (050)

### External (Future)
- Blog post explicando autopoiesis en templates
- GitHub repo público con templates
- LinkedIn post sobre reducción 8h → 2h

---

## Appendices

### Related Documents
- [ISSUE.yaml](../../ISSUE.yaml): Problema RBM-GAC
- [design.md](../../design.md): Arquitectura técnica
- [requirements.md](../../010-define/requirements.md): Requirements detallados
- [structure.md](./structure.md): Directory structure
- [Manifiesto Melquisedec](../../../docs/manifiesto/): Principios guía

### Changelog
- **2024-01:** Initial vision document (MELQUISEDEC, phase 010-define)

---

**Maintained by:** MELQUISEDEC
**Review Cycle:** After each checkpoint (CK-01 through CK-05)
**Next Review:** After CK-01 validation
