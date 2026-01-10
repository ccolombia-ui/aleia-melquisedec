# research-autopoietic-template - Arquitectura

**Versión**: v0.1.0
**Creado**: 2026-01-09
**Tipo**: research
**Template**: research-autopoietic v4.3.1 (self-referential)
**Estado**: 010-define (inception)

---

## 🎯 Visión

Diseñar un **sistema de templates autopoiéticos** donde:

1. **Templates aprenden** de ejecuciones previas (autopoiesis)
2. **Patterns evolucionan** con confidence scores basados en evidencia
3. **Scripts gestionan** lifecycle completo (init → validate → consolidate → analyze)
4. **Conocimiento persiste** en triple formato (markdown + Neo4j + vector)

---

## 🏗️ Arquitectura de Alto Nivel

```
apps/research-autopoietic-template/     (Este proyecto)
│
├── 050-release/outputs/                (OUTPUTS = TEMPLATES)
│   ├── templates/
│   │   └── research-autopoietic/
│   │       ├── v4.3.1/                 (Versión estable actual)
│   │       └── v4.3.2/                 (Próxima versión)
│   │
│   ├── scripts/                        (Scripts Python)
│   │   ├── init-spec.py
│   │   ├── validate-checkpoint.py
│   │   ├── consolidate-lessons.py
│   │   └── autopoiesis-analyze.py
│   │
│   ├── patterns/                       (PATTERN-XXX.yaml)
│   │   ├── PATTERN-001-Literature-Review.yaml
│   │   └── PATTERN-002-Atomic-Synthesis.yaml
│   │
│   └── lenses/                         (Familias de lenses)
│       ├── research-method/
│       └── architecture/
│
└── 060-reflect/feedback-aggregator/    (Feedback de proyectos)
    ├── neo4j-X-feedback.md
    └── keter-migration-feedback.md
```

---

## 📐 Principios de Diseño

### 1. Autopoiesis Medida (P2)

- Patterns con **confidence scores** (0.0-1.0)
- Thresholds: 0.90 (auto), 0.80 (suggest), 0.50 (track)
- Feedback loop: proyecto → feedback → análisis → evolución

### 2. Triple Persistencia (P6)

Todo conocimiento en 3 formatos:
- **Markdown**: Documentos originales (atomics, ADRs)
- **Neo4j**: Grafo de conceptos y relaciones
- **Vector**: Embeddings para similarity search

### 3. Validación Continua (P5)

5 Checkpoints:
- **CK-01** (010-define): Requirements completos
- **CK-02** (020-conceive): ≥20 atomics + investigación
- **CK-03** (030-design): ≥5 ADRs + arquitectura
- **CK-04** (040-build): Scripts + templates implementados
- **CK-05** (050-release): Outputs publicados + lessons

### 4. Issue-Driven (P3)

Todo nace de **ISSUE.yaml**:
- Problema estructurado (RBM-GAC)
- Rostros asignados por fase
- Checkpoints definidos
- Outputs esperados

---

## 🔄 Ciclo de Vida

### Fase 010: Define (MELQUISEDEC)

**Input**: ISSUE.yaml
**Output**: requirements.md (RBM-GAC), design.md (este archivo)
**Checkpoint**: CK-01

### Fase 020: Conceive (HYPATIA)

**Input**: Requirements
**Output**:
- 01-literature/ (papers, docs)
- 02-atomics/ (conceptos atómicos)
- 03-datasets/ (datos de investigación)

**Checkpoint**: CK-02 (≥20 atomics, triple persistencia)

### Fase 030: Design (SALOMON)

**Input**: Atomics + literature
**Output**:
- architecture/ (diseño de templates)
- adrs/ (decisiones clave)
- specifications/ (specs de scripts)

**Checkpoint**: CK-03 (≥5 ADRs)

### Fase 040: Build (MORPHEUS)

**Input**: Arquitectura + specs
**Output**:
- Templates v4.3.1/
- Scripts Python/
- Patterns YAML/

**Checkpoint**: CK-04 (scripts funcionando)

### Fase 050: Release (ALMA)

**Input**: Implementaciones
**Output**:
- 050-release/outputs/ (publicación)
- lessons-consolidated.md

**Checkpoint**: CK-05 (outputs disponibles)

### Fase 060: Reflect (MELQUISEDEC)

**Input**: lessons-consolidated.md + feedback de proyectos
**Output**:
- analysis.md (análisis de efectividad)
- pattern-evolution.md (scores actualizados)
- new-issues/ (mejoras identificadas)

**Checkpoint**: Post-CK-05 (template evolucionado)

---

## 🔗 Relaciones con Otros Proyectos

### Proyectos que USAN templates

```
apps/research-neo4j-llamaindex-architecture/
└── usa: templates/v4.3.1/
    envía: 060-reflect/template-improvements.md
    destino: apps/research-autopoietic-template/060-reflect/feedback-aggregator/

apps/research-keter-migration/
└── usa: templates/v4.3.1/
    envía: 060-reflect/template-improvements.md
    destino: apps/research-autopoietic-template/060-reflect/feedback-aggregator/
```

### Este proyecto EVOLUCIONA templates

```
apps/research-autopoietic-template/
└── recibe: feedback de múltiples proyectos
    analiza: autopoiesis-analyze.py
    actualiza: patterns/ con nuevos scores
    versiona: v4.3.1 → v4.3.2
    publica: 050-release/outputs/
```

---

## 📊 Métricas de Éxito

| Métrica | Objetivo | Actual |
|---------|----------|--------|
| **Templates publicados** | ≥3 versiones | 0 |
| **Patterns validados** | ≥8 con conf ≥0.80 | 0 |
| **Scripts funcionando** | ≥6 scripts Python | 0 |
| **Proyectos usando** | ≥2 proyectos | 0 |
| **Tiempo setup** | ≤2 horas | - |
| **ADRs documentados** | ≥5 decisiones | 0 |
| **Atomics creados** | ≥20 conceptos | 0 |

---

## 🚧 Estado Actual

**Fase**: 010-define (inception)
**Próximo milestone**: CK-01
**Bloqueadores**: Ninguno

### Tareas Inmediatas

1. ✅ Crear ISSUE.yaml (P3)
2. ✅ Crear design.md (este archivo)
3. ⏳ Crear requirements.md (RBM-GAC)
4. ⏳ Crear estructura de carpetas (010-060)
5. ⏳ Configurar .spec-workflow/
6. ⏳ Configurar .melquisedec/

---

## 📚 Referencias

- [Manifiesto MELQUISEDEC v4.0.0](../../docs/manifiesto/bereshit-v3.0.0.md)
- [Principios Fundacionales](../../docs/manifiesto/01-fundamentos/04-principios-fundacionales.md)
- [Template Design v4.3.1](.spec-workflow/_meta/templates/research-autopoietic-template/unified-research-template-design-v4.3.1.md) (self-reference)

---

**Última actualización**: 2026-01-09
**Responsable**: MELQUISEDEC (010-define)
