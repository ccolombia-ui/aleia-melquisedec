# Research Autopoietic Templates

> **Meta-Research:** Diseño de sistema de templates autopoiéticos que evolucionan vía feedback empírico
> **Status:** 010-define (Inception) | Phase: Definition | Progress: 40%
> **Version:** v0.1.0 → Target v4.3.1

---

## 🎯 Propósito

**Crear templates de investigación que se auto-mejoren basados en feedback de múltiples proyectos**, reduciendo el tiempo de setup de 8h a 2h mientras mantienen consistencia cross-proyecto y trazabilidad completa.

**Esto es investigación meta-research:** Este proyecto usa v4.3.1 para diseñar las mejoras a v4.3.1+. Es self-referential por naturaleza.

---

## 🚀 Quick Start

### Para usar este proyecto:

```bash
cd apps/research-autopoietic-template

# 1. Revisar el problema que estamos resolviendo
cat ISSUE.yaml

# 2. Entender la arquitectura
cat design.md

# 3. Leer requirements detallados
cat 010-define/requirements.md

# 4. Ver configuración de lenses y patterns
cat .spec-workflow/specs/autopoietic-templates/spec-config.yaml

# 5. Explorar steering documents
cat .spec-workflow/steering/structure.md
cat .spec-workflow/steering/product.md
cat .spec-workflow/steering/tech.md
```

### Para crear proyecto research usando templates (futuro v4.3.1):

```bash
# Una vez completado este research, podrás hacer:
python 050-release/outputs/scripts/init-spec.py \
  --name my-research \
  --type autopoietic \
  --output ../apps/

# Setup completo en ≤2h (vs 8h manualmente)
```

---

## 📁 Estructura del Proyecto

```
research-autopoietic-template/
├── ISSUE.yaml                          # ✅ Issue-spec principal (RBM-GAC)
├── design.md                           # ✅ Arquitectura alto nivel
├── PROPOSITO.md                        # ✅ Template original
├── README.md                           # ✅ Este archivo
│
├── .spec-workflow/                     # ✅ Configuración spec-workflow-mcp
│   ├── steering/                       # ✅ Strategic documents
│   │   ├── structure.md                # ✅ Directory structure (living doc)
│   │   ├── product.md                  # ✅ Vision y roadmap
│   │   └── tech.md                     # ✅ Stack técnico
│   └── specs/autopoietic-templates/    # ✅ Este spec
│       └── spec-config.yaml            # ✅ Lenses, patterns, rostros, checkpoints
│
├── .melquisedec/                       # ✅ Knowledge management (P6)
│   ├── domain/                         # Triple persistencia (markdown + cypher + embeddings)
│   ├── lessons/                        # P2 Autopoiesis (checkpoint + consolidated)
│   ├── logs/                           # P5 Validación (validation + sync + autopoiesis)
│   └── context/                        # Smart-thinking MCP
│
├── 010-define/                         # ✅ Phase 1: Definition (MELQUISEDEC)
│   └── requirements.md                 # ✅ RBM-GAC detallado (≥8 secciones)
│
├── 020-conceive/                       # ⏳ Phase 2: Conception (HYPATIA)
│   ├── 01-literature/                  # Papers: DSR, Autopoiesis, DDD, Zettelkasten
│   └── 02-atomics/                     # ≥20 atomics sobre templates/patterns
│
├── 030-design/                         # ⏳ Phase 3: Design (SALOMON)
│   ├── architecture/                   # System design, diagrams
│   └── adrs/                           # ≥5 ADRs sobre decisiones templates
│
├── 040-build/                          # ⏳ Phase 4: Build (MORPHEUS)
│   └── research/                       # Templates v4.3.1, scripts, tests
│
├── 050-release/                        # ⏳ Phase 5: Release (ALMA)
│   └── outputs/                        # **PRIMARY DELIVERABLES**
│       ├── templates/                  # Templates versionados (v4.3.1+)
│       ├── scripts/                    # 6 scripts lifecycle
│       ├── patterns/                   # ≥8 patterns con confidence ≥0.80
│       └── lenses/                     # Lenses metodológicos
│
└── 060-reflect/                        # ⏳ Phase 6: Reflect (MELQUISEDEC)
    ├── feedback-aggregator/            # Feedback de proyectos (keter, neo4j)
    └── new-issues/                     # Issues para v4.3.2+
```

---

## 📊 Estado Actual (Phase 010-define)

### ✅ Completado
- [x] ISSUE.yaml con problema RBM-GAC
- [x] design.md con arquitectura y lifecycle
- [x] requirements.md con 10 secciones detalladas
- [x] spec-config.yaml con 4 lenses, 5 patterns, 6 rostros, 5 checkpoints
- [x] Estructura carpetas 010-060 creada
- [x] .melquisedec/ inicializado (domain, lessons, logs, context)
- [x] .spec-workflow/ configurado (steering, specs)
- [x] steering/structure.md (directory structure, living doc)
- [x] steering/product.md (vision, roadmap, metrics)
- [x] steering/tech.md (stack, scripts architecture)

### ⏳ Pendiente para CK-01
- [ ] Crear symlinks (ISSUE.yaml, design.md, requirements.md)
- [ ] Generar tasks.md desde spec-config.yaml
- [ ] Actualizar README.md con ejemplos uso (este archivo ✅)
- [ ] Validar checkpoint: `python validate-checkpoint.py --checkpoint CK-01`

### 📈 Métricas
- **Completion:** 40% (010-define en progreso)
- **Atomics:** 0/20 (target en 020-conceive)
- **ADRs:** 0/5 (target en 030-design)
- **Patterns:** 5 definidos, 0 validados (target ≥8 con confidence ≥0.80)
- **Scripts:** 0/6 (target en 040-build)
- **Projects Using:** 0/2 (target en 050-release)

---

## 🔄 Autopoiesis Cycle

Este proyecto implementa P2 (Autopoiesis) mediante feedback loop:

```
1. Projects USE templates → 050-release/outputs/templates/
2. Projects ENCOUNTER issues → Documentan mejoras
3. Projects SEND feedback → 060-reflect/feedback-aggregator/{project}/
4. MELQUISEDEC ANALYZES → autopoiesis-analyze.py
5. PATTERNS UPDATED → Confidence scores recalculados
6. NEW VERSION released → v4.3.2, v4.4.0, etc.
└─> LOOP CONTINUES
```

**Self-Improvement:** Templates aprenden de su uso real.

---

## 🎯 Objetivos (RBM-GAC)

### Gap
- No existe sistema de templates autopoiéticos
- Proyectos reinventan estructura cada vez
- Feedback se pierde, no se propaga
- Sin confidence scores ni evidencia empírica

### Goal
- Templates versionados semánticamente
- Patterns con confidence ≥0.80
- Scripts lifecycle automatizados
- Tiempo setup: 8h → 2h

### Outcomes (Measurable)
- ≥3 versiones templates (v4.3.1+)
- ≥8 patterns validados (confidence ≥0.80)
- ≥6 scripts funcionales
- ≥2 proyectos adoptando templates
- Setup time ≤2h (medido en 2 proyectos)
- ≥5 ADRs documentados
- ≥20 atomics capturados

### Outcomes (Qualitative)
- Consistencia cross-proyecto
- Trazabilidad: feedback → ADR → pattern → template
- Documentación autopoiesis completa

---

## 🔬 Metodologías Aplicadas

### 1. Design Science Research (DSR)
- Templates son **artefactos científicos**
- Evaluación iterativa con proyectos reales
- Contribución: templates publicables

### 2. Zettelkasten
- ≥20 atomics sobre templates/autopoiesis/patterns
- Knowledge graph en Neo4j
- Progressive elaboration

### 3. Domain-Driven Design (DDD)
- Patterns como bounded contexts
- Ubiquitous language (ISSUE, SPEC, PATTERN)
- Strategic design: patterns → templates

### 4. Autopoiesis Theory
- Templates se auto-producen via feedback
- Operational closure: patterns evolucionan internamente
- Structural coupling: adaptación a proyectos

---

## 📦 Deliverables Esperados (050-release/outputs/)

### Templates (v4.3.1)
- Estructura 010-060 completa
- ISSUE.yaml, requirements.md, design.md templates
- .spec-workflow/ y .melquisedec/ configurados
- README con quick start

### Scripts (6 scripts)
1. `init-spec.py` - Inicializar proyecto desde template
2. `validate-checkpoint.py` - Validar criterios CK-XX
3. `consolidate-lessons.py` - Agregar lessons
4. `autopoiesis-analyze.py` - Procesar feedback, actualizar patterns
5. `generate-tasks-md.py` - Auto-generar tasks.md
6. `sync-triple-persistence.py` - Sync markdown → Neo4j → vectors

### Patterns (≥8 con confidence ≥0.80)
- PATTERN-001: Six-Phase Lifecycle
- PATTERN-002: Issue-Spec as Source of Truth
- PATTERN-007: Triple Persistence
- PATTERN-012: Feedback Aggregator
- PATTERN-015: Confidence Scoring
- + 3 más a descubrir en research

### Lenses (Metodológicos)
- DSR (Design Science Research)
- Zettelkasten (Knowledge Management)
- DDD (Domain-Driven Design)
- Autopoiesis (Self-Improvement)

---

## ✅ Checkpoints

### CK-01 (010-define) - CURRENT
**Criterios:**
- [x] ISSUE.yaml completo y parseable
- [x] requirements.md con ≥8 secciones (RBM-GAC)
- [x] design.md con arquitectura + lifecycle + métricas
- [x] Estructura carpetas 010-060 creada
- [x] .spec-workflow/ y .melquisedec/ configurados
- [ ] README.md actualizado (este archivo ✅)
- [ ] tasks.md generado
- [ ] Validación: `python validate-checkpoint.py --checkpoint CK-01`

### CK-02 (020-conceive)
- [ ] ≥20 atomics en 020-conceive/02-atomics/
- [ ] Literature review completo
- [ ] Triple persistencia inicializada (≥10 concepts en .melquisedec/domain/)

### CK-03 (030-design)
- [ ] ≥5 ADRs en 030-design/adrs/
- [ ] Architecture diagrams (mermaid)
- [ ] Specifications para scripts

### CK-04 (040-build)
- [ ] Templates v4.3.1 completos
- [ ] 6 scripts implementados y testeados
- [ ] ≥8 patterns con confidence scores

### CK-05 (050-release)
- [ ] Outputs publicados
- [ ] ≥2 proyectos adoptaron templates
- [ ] Tiempo setup medido: ≤2h
- [ ] Lessons consolidadas

---

## 🔗 Relaciones

### Depende de:
- Manifiesto Melquisedec (principios P1-P10)
- Principios Tzimtzum (workflow incremental, rostros)
- v4.3.1 Draft (self-reference)

### Provee a:
- `research-keter-migration` (adoptará templates)
- `research-neo4j-llamaindex-architecture` (adoptará templates)
- Futuros proyectos research

### Retroalimenta a:
- Mejoras capturadas en `060-reflect/feedback-aggregator/`
- Patterns evolucionados → nueva versión templates
- Lessons learned → manifiesto actualizado

---

## 📚 Referencias

### Documentos Internos
- [ISSUE.yaml](./ISSUE.yaml) - Issue-spec principal
- [design.md](./design.md) - Arquitectura alto nivel
- [requirements.md](./010-define/requirements.md) - Requirements detallados
- [spec-config.yaml](./.spec-workflow/specs/autopoietic-templates/spec-config.yaml) - Config lenses/patterns
- [structure.md](./.spec-workflow/steering/structure.md) - Directory structure
- [product.md](./.spec-workflow/steering/product.md) - Vision y roadmap
- [tech.md](./.spec-workflow/steering/tech.md) - Stack técnico

### Documentos Externos
- [Manifiesto Melquisedec](../../docs/manifiesto/)
- [ADR-001: Monorepo Structure](../../docs/architecture/ADR-001-monorepo-structure.md)
- [v4.3.1 Template](../../.spec-workflow/_meta/templates/research-autopoietic-template/unified-research-template-design-v4.3.1.md)

---

## 🛠️ Tecnologías

- **Python 3.10+** - Scripts y análisis
- **Neo4j 5.0+** - Graph database (triple persistence)
- **OpenAI API** - Embeddings y síntesis (GPT-4)
- **YAML/Markdown** - Configuración y documentación
- **Mermaid** - Diagramas as code
- **Git** - Versionado semántico

---

## 🤝 Contribuir Feedback

Si usas estos templates en tu proyecto:

1. Documenta mejoras en tu proyecto:
   ```markdown
   # template-improvements.md
   ## Problema Encontrado
   - [Descripción del problema]

   ## Solución Propuesta
   - [Solución que funcionó]

   ## Evidencia
   - [Métricas, ejemplos, referencias]

   ## Prioridad
   - [ ] Low [ ] Medium [x] High
   ```

2. Copia a feedback aggregator:
   ```bash
   cp template-improvements.md \
     ../research-autopoietic-template/060-reflect/feedback-aggregator/mi-proyecto/
   ```

3. MELQUISEDEC analizará y actualizará patterns

---

## 📝 Changelog

- **v0.1.0 (2024-01):** Initial structure, phase 010-define inception
  - ISSUE.yaml created (RBM-GAC)
  - design.md created (architecture)
  - requirements.md created (detailed requirements)
  - spec-config.yaml created (lenses, patterns, rostros)
  - Directory structure 010-060 initialized
  - .spec-workflow/ and .melquisedec/ configured
  - steering/ documents complete (structure, product, tech)
  - README.md updated with comprehensive overview

---

**Maintained by:** MELQUISEDEC (010-define, 060-reflect)
**Current Phase:** 010-define (40% complete)
**Next Milestone:** CK-01 Validation
**Target v4.3.1:** 8 weeks (estimated)
