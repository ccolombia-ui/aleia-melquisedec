# Requirements - Research Autopoietic Templates

> **Spec ID:** ISSUE-SPEC-001-design-autopoietic-templates
> **Phase:** 010-define
> **Rostro:** MELQUISEDEC
> **Status:** active
> **Created:** 2024-01

---

## 1. Problem Statement (RBM-GAC)

### Gap Analysis

**Situación Actual:**
- Proyectos de investigación crean templates ad-hoc sin sistema de evolución
- No existe mecanismo para capturar y propagar mejoras entre proyectos
- Templates no rastrean confidence scores ni evidencia empírica
- Feedback sobre templates se pierde o no se integra sistemáticamente
- Cada proyecto reinventa patrones sin aprovechar conocimiento previo

**Evidencia:**
- 3+ proyectos en `apps/` usando estructuras inconsistentes
- Sin historial de evolución de templates (sin versionado semántico)
- P2 Autopoiesis no implementado para templates
- Falta integración triple persistencia → Neo4j para patterns

### Goal

**Objetivo Principal:**
Diseñar e implementar sistema de templates autopoiéticos donde templates evolucionen basados en feedback empírico de múltiples proyectos de investigación.

**Criterios de Éxito:**
1. Templates versionados semánticamente (v4.3.1, v4.3.2, etc.)
2. Patterns con confidence scores ≥0.80
3. Scripts del lifecycle automatizados
4. Reducción tiempo setup: 8h → 2h
5. Trazabilidad completa: mejora → ADR → pattern → template

### Outcomes

**Cuantitativos (Measurable):**
| Métrica | Objetivo | Validación |
|---------|----------|------------|
| **Versiones Templates** | ≥3 versiones (v4.3.1+) | Revisar `050-release/outputs/templates/` |
| **Patterns Validados** | ≥8 patterns con confidence ≥0.80 | Analizar `050-release/outputs/patterns/*.yaml` |
| **Scripts Lifecycle** | ≥6 scripts (init, validate, consolidate, etc.) | Verificar `050-release/outputs/scripts/` |
| **Proyectos Adopción** | ≥2 proyectos usando templates | Buscar `.spec-workflow/specs/` en `apps/research-*` |
| **Tiempo Setup** | Reducción de 8h a 2h | Medir tiempo real en 2 nuevos proyectos |
| **ADRs Documentados** | ≥5 ADRs sobre decisiones templates | Contar archivos en `030-design/adrs/ADR-*.md` |
| **Atomics Capturados** | ≥20 atomics sobre autopoiesis/templates | Contar archivos en `020-conceive/02-atomics/*.md` |

**Cualitativos:**
1. **Consistencia Cross-Proyecto:**
   - Todos proyectos usan misma estructura `.spec-workflow/`
   - Mismo formato ISSUE.yaml (P3)
   - Mismas convenciones de naming

2. **Trazabilidad Decisiones:**
   - Cada patrón referencia ADR que lo justifica
   - ADRs referencian atomics/literature que proveen evidencia
   - Mejoras trazables desde feedback → pattern → template version

3. **Documentación Autopoiesis:**
   - P2 implementado con scripts de análisis
   - Feedback loop documentado (proyecto → template app → evolución)
   - Confidence scores basados en métricas empíricas

---

## 2. Scope

### In Scope

**Diseño y Creación:**
1. Template research autopoiético completo (v4.3.1 base)
2. Sistema de patterns con confidence scoring
3. Scripts para lifecycle (init, validate, consolidate, analyze)
4. Lenses para diferentes metodologías (DSR, Zettelkasten, DDD)
5. Estructura `.spec-workflow/` y `.melquisedec/`
6. Feedback aggregator en `060-reflect/`

**Infraestructura:**
1. Triple persistencia: Markdown + Neo4j + Vector embeddings
2. Autopoiesis scripts para analizar feedback y actualizar patterns
3. Versionado semántico de templates
4. Documentación completa (README, guides, ADRs)

**Validación:**
1. 5 checkpoints con criterios verificables
2. Aplicar template en ≥2 proyectos existentes
3. Capturar feedback y ejecutar 1 ciclo de evolución
4. Medir tiempo setup antes/después

### Out of Scope

**No incluido en esta fase:**
1. ❌ Interfaz web para gestionar templates (futuro)
2. ❌ Sistema de notificaciones automáticas de nuevas versiones
3. ❌ CLI completo tipo `npm create` (solo scripts básicos)
4. ❌ Integración con CI/CD para validación automática
5. ❌ Marketplace público de templates

---

## 3. Functional Requirements

### FR-01: Template Structure
**Descripción:** Template debe incluir estructura completa 6 fases (010-060)
**Prioridad:** Critical
**Criterio Aceptación:**
- Carpetas 010-define, 020-conceive, 030-design, 040-build, 050-release, 060-reflect
- Cada fase con subcarpetas documentadas
- README.md en cada fase explicando propósito

### FR-02: ISSUE.yaml Format
**Descripción:** Formato estandarizado para issue-spec (P3)
**Prioridad:** Critical
**Criterio Aceptación:**
- Campos obligatorios: id, type, status, priority, problem (RBM-GAC)
- Campos opcionales: methodologies, rostros, outputs, triple_persistence
- Validación con schema YAML

### FR-03: Pattern Confidence Scoring
**Descripción:** Cada pattern debe tener confidence score basado en evidencia
**Prioridad:** High
**Criterio Aceptación:**
- Formato: `PATTERN-XXX.yaml` con campos: id, name, description, confidence, evidence, adrs
- Confidence calculado: `(projects_validated / projects_total) * (adrs_count / 2)`
- Threshold mínimo: 0.60 para inclusión, ≥0.80 para "validated"

### FR-04: Feedback Aggregator
**Descripción:** Sistema para capturar y agregar feedback de proyectos
**Prioridad:** High
**Criterio Aceptación:**
- Ubicación: `060-reflect/feedback-aggregator/{project-name}/template-improvements.md`
- Formato: problema encontrado, solución propuesta, evidencia, prioridad
- Script `autopoiesis-analyze.py` que procesa feedback y actualiza patterns

### FR-05: Triple Persistence
**Descripción:** Todos los conceptos/patterns/atomics en 3 formatos
**Prioridad:** High
**Criterio Aceptación:**
- Markdown en `.melquisedec/domain/markdown/`
- Cypher queries en `.melquisedec/domain/cypher/`
- Embeddings en `.melquisedec/domain/embeddings/`
- Script sync que mantiene coherencia

### FR-06: Lifecycle Scripts
**Descripción:** Scripts automatizados para operaciones comunes
**Prioridad:** Medium
**Criterio Aceptación:**
- `init-spec.py`: Crea estructura completa desde template
- `validate-checkpoint.py`: Valida criterios checkpoint
- `consolidate-lessons.py`: Agrega lessons de fases
- `autopoiesis-analyze.py`: Procesa feedback y actualiza patterns
- `generate-tasks-md.py`: Auto-genera tasks.md desde spec-config.yaml
- Todos con tests y documentación

---

## 4. Non-Functional Requirements

### NFR-01: Performance
**Criterio:** Setup tiempo ≤2h para nuevo proyecto research
**Medición:** Cronometrar desde `python init-spec.py` hasta primer commit

### NFR-02: Maintainability
**Criterio:** ADRs documentan todas decisiones arquitecturales
**Medición:** Cada pattern debe referenciar ≥1 ADR

### NFR-03: Usability
**Criterio:** Documentación completa con ejemplos prácticos
**Medición:** README con quick start + 3 ejemplos mínimo

### NFR-04: Reliability
**Criterio:** Validación checkpoints previene avance con criterios no cumplidos
**Medición:** Script `validate-checkpoint.py` con exit code != 0 si falla

### NFR-05: Traceability
**Criterio:** Trazabilidad completa desde feedback hasta template version
**Medición:** Poder seguir cadena: feedback → ADR → pattern → template commit

---

## 5. Constraints

### Technical Constraints
- **Python ≥3.10:** Scripts requieren features modernas
- **Neo4j ≥5.0:** Para graph queries avanzados
- **OpenAI API:** Para embeddings y análisis autopoiesis

### Organizational Constraints
- **Self-referential:** Este proyecto usa v4.3.1 para diseñar v4.3.1+
- **Monorepo:** Templates permanecen en `apps/research-autopoietic-template/`
- **No external dependencies:** Templates deben ser standalone (no npm packages centralizados)

### Timeline Constraints
- **CK-01 (010-define):** Completar requirements + design en primera semana
- **CK-02 (020-conceive):** ≥20 atomics en segunda semana
- **CK-05 (050-release):** Outputs publicados en 6 semanas

---

## 6. Assumptions

1. **Proyectos existentes colaboran:** `research-keter-migration` y `research-neo4j-llamaindex-architecture` proveerán feedback
2. **Neo4j disponible:** Infraestructura graph database operativa
3. **OpenAI API access:** Para embeddings y análisis
4. **Python environment:** Conda/venv configurado correctamente

---

## 7. Dependencies

### Internal Dependencies
- **Manifiesto Melquisedec:** Principios P1-P10 guían diseño
- **Principios Tzimtzum:** Workflow incremental y rostros
- **v4.3.1 Draft:** Esta guía es punto de partida (self-reference)

### External Dependencies
- **Design Science Research (DSR):** Metodología guía
- **Maturana & Varela:** Teoría autopoiesis
- **Domain-Driven Design (DDD):** Bounded contexts para patterns
- **Zettelkasten:** Atomics y knowledge graph

---

## 8. Risks and Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Scope creep:** Añadir features fuera de scope | Medium | High | Strict adherencia a In Scope, defer a v4.4.0 |
| **Feedback insuficiente:** <2 proyectos adoptan templates | Medium | High | Aplicar template a research-keter-migration y research-neo4j activamente |
| **Complejidad autopoiesis:** Scripts muy complejos | High | Medium | Empezar simple (count patterns, threshold básico), iterar |
| **Self-referential paradox:** Usar v4.3.1 incompleto para diseñar v4.3.1 | High | Medium | Bootstrap iterativo: mejorar template mientras se usa |
| **Tiempo estimado incorrecto:** 2h muy ambicioso | Medium | Low | Medir realmente en 2 proyectos, ajustar objetivo si necesario |

---

## 9. Success Criteria (Checkpoint CK-01)

**Para completar fase 010-define:**
- [x] ISSUE.yaml completo y validado
- [x] design.md con arquitectura y lifecycle
- [x] requirements.md (este documento) con RBM-GAC detallado
- [ ] Estructura carpetas 010-060 creada
- [ ] `.spec-workflow/` configurado
- [ ] `.melquisedec/` inicializado
- [ ] README.md actualizado con quick start
- [ ] Validación: `python validate-checkpoint.py --checkpoint CK-01`

**Criterios Validación CK-01:**
1. Todos los archivos requeridos existen en rutas esperadas
2. ISSUE.yaml parseable y campos requeridos presentes
3. requirements.md cubre ≥80% de secciones esperadas (1-9)
4. design.md incluye arquitectura + lifecycle + métricas

---

## 10. Next Steps

**Immediate (esta semana):**
1. Completar estructura carpetas (parcial ✅)
2. Crear `.spec-workflow/specs/autopoietic-templates/spec-config.yaml`
3. Crear `.spec-workflow/steering/{structure, product, tech}.md`
4. Inicializar `.melquisedec/domain/` con primeros conceptos
5. Generar `tasks.md` desde spec-config.yaml
6. Validar CK-01 con script

**Following (próxima fase 020-conceive):**
1. Literature review: DSR + Autopoiesis + DDD + Zettelkasten
2. Crear ≥20 atomics sobre patterns, templates, lifecycle
3. Comenzar triple persistencia (md → Neo4j → vectors)
4. Configurar feedback aggregator structure

---

## Referencias

- [Manifiesto Melquisedec](../../docs/manifiesto/)
- [Principios Tzimtzum](../../docs/manifiesto/01-fundamentos/)
- [v4.3.1 Template](../../.spec-workflow/_meta/templates/research-autopoietic-template/unified-research-template-design-v4.3.1.md)
- [ADR-001: Monorepo Structure](../../docs/architecture/ADR-001-monorepo-structure.md)

---

**Changelog:**
- 2024-01: Initial draft (MELQUISEDEC)
