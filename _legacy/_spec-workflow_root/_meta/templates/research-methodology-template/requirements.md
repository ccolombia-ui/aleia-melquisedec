# Research Methodology: {{research.full_name}} - Requirements

> **Spec**: research-methodology-template
> **Version**: {{research.version}}
> **Created**: {{research.created}}
> **Owner**: {{research.owner}}
> **Status**: Draft

---

## Metadata

```yaml
---
id: "req-research-{{research.name}}"
version: "{{research.version}}"
created: "{{research.created}}"
owner: "{{research.owner}}"
status: "draft"
melquisedec:
  principles: ["P1", "P2", "P3", "P5", "P6", "P7"]
  workflow: "DAATH-ZEN"
---
```

---

## 📋 Overview

Esta investigación busca realizar una **{{research.type}}** de la metodología **{{research.full_name}}** para:

1. **Comprender** sus fundamentos, fases y artefactos
2. **Extraer** conocimiento atómico trazable (Zettelkasten)
3. **Identificar** frameworks y bibliotecas canónicas para adopción
4. **Generar** artefactos ejecutables (workflows, scripts, grafos de conocimiento)
5. **Adoptar** las mejores prácticas en el contexto MELQUISEDEC

### Tipo de Investigación

**{{research.type}}**:
- `formal-review`: Revisión exhaustiva con análisis profundo (2-3 semanas)
- `quick-scan`: Escaneo rápido para overview (3-5 días)
- `deep-dive`: Investigación profunda en aspecto específico (4-6 semanas)

### Principios MELQUISEDEC Aplicados

- **P1 (Síntesis Metodológica)**: NO inventar, ADAPTAR mejores prácticas
- **P2 (Autopoiesis)**: Lessons learned mejoran el template
- **P3 (Issue-Driven)**: Todo parte de ISSUE.yaml
- **P5 (Validación Continua)**: Checkpoints por rostro
- **P6 (Trazabilidad)**: Triple output (MD + Graph + Vectors)
- **P7 (Recursión Fractal)**: Template reutilizable

---

## 🎯 Research Questions (RQs)

{{#each scope.research_questions}}
- **RQ{{add @index 1}}**: {{this}}
{{/each}}

### Hipótesis Iniciales (Opcional)

{{#if scope.hypothesis}}
{{#each scope.hypothesis}}
- **H{{add @index 1}}**: {{this}}
{{/each}}
{{else}}
_No se definieron hipótesis iniciales. Se realizará investigación exploratoria._
{{/if}}

---

## 👥 User Stories

### US-1: Arquitecto MELQUISEDEC
**Como** arquitecto de MELQUISEDEC
**Quiero** entender las fases de {{research.name}}
**Para** mapearlas a los rostros DAATH-ZEN y workflows existentes

**Criterios de Aceptación**:
- Cada fase documentada con propósito y artefactos
- Mapeo explícito fase → rostro
- Patrones identificados

### US-2: Investigador (HYPATIA)
**Como** investigador
**Quiero** fuentes canónicas validadas
**Para** evitar información de baja calidad y asegurar trazabilidad

**Criterios de Aceptación**:
- ≥{{quality.metrics.min_sources}} fuentes documentadas
- ≥{{quality.metrics.min_peer_reviewed}} fuentes peer-reviewed
- Metadata Dublin Core completa por fuente

### US-3: Implementador (MORPHEUS)
**Como** implementador
**Quiero** scripts de ingesta listos para usar
**Para** cargar el conocimiento a Neo4j sin esfuerzo manual

**Criterios de Aceptación**:
- Scripts Cypher parametrizados
- Scripts idempotentes (re-ejecutables)
- Embeddings generados automáticamente

### US-4: Validador (ALMA)
**Como** validador
**Quiero** trazabilidad completa desde fuentes hasta grafo
**Para** auditar y verificar integridad del conocimiento

**Criterios de Aceptación**:
- Cada atomic referencia fuente original
- Triple output poblado (MD + Graph + Vectors)
- Visualizaciones del grafo disponibles

---

## ✅ Functional Requirements

### REQ-SETUP: Inicialización de Estructura

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-SETUP-001 | Sistema debe crear estructura de carpetas según `config.yaml` | Alta |
| REQ-SETUP-002 | Crear `ISSUE.yaml` con metadata HKM + Dublin Core | Alta |
| REQ-SETUP-003 | Inicializar `.melquisedec/` para validaciones | Alta |

**Validación**: Estructura completa + ISSUE.yaml válido

---

### REQ-LIT: Literature Review

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-LIT-001 | Identificar mínimo {{quality.metrics.min_sources}} fuentes ({{quality.metrics.min_peer_reviewed}} peer-reviewed) | Alta |
| REQ-LIT-002 | Documentar contenido completo con metadata Dublin Core | Alta |
| REQ-LIT-003 | Organizar en `01-literature/{type}/{id}/` | Alta |
| REQ-LIT-004 | Formatos soportados: papers/, books/, frameworks/ | Media |
| REQ-LIT-005 | Generar `sources.yaml` como índice | Alta |

**Validación**: HYPATIA checkpoint (ck-01) PASS

---

### REQ-ATOM: Atomización de Conocimiento (Zettelkasten)

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-ATOM-001 | Extraer mínimo {{quality.metrics.min_atomics}} conceptos atómicos | Alta |
| REQ-ATOM-002 | Un concepto = un archivo `.md` con HKM header | Alta |
| REQ-ATOM-003 | Mapear relaciones semánticas en `relationships.yaml` | Alta |
| REQ-ATOM-004 | Formato YAML-LD compatible con Neo4j | Alta |
| REQ-ATOM-005 | Cada atomic debe referenciar fuente original (trazabilidad) | Alta |
| REQ-ATOM-006 | Generar `graph-ready/*.yaml` para ingesta directa | Media |

**Validación**: ≥{{quality.metrics.min_atomics}} atomics + relationships.yaml válido

---

### REQ-ANA: Análisis y Síntesis

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-ANA-001 | Análisis comparativo de enfoques (si aplica) | Alta |
| REQ-ANA-002 | Identificar mínimo {{quality.metrics.min_patterns}} patrones/prácticas | Alta |
| REQ-ANA-003 | Recomendar framework con justificación (ADR) | Alta |
| REQ-ANA-004 | Síntesis ≥1500 palabras respondiendo RQs | Alta |
| REQ-ANA-005 | Validar o refutar hipótesis iniciales | Media |
| REQ-ANA-006 | Workflow patterns identificados | Media |

**Validación**: SALOMON checkpoint (ck-02) PASS

---

### REQ-ART: Artefactos Ejecutables

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-ART-001 | Solution spec ≥{{quality.metrics.min_solution_spec_lines}} líneas | Alta |
| REQ-ART-002 | Implementation plan con milestones y dependencias | Alta |
| REQ-ART-003 | Testing strategy (TDD, coverage ≥{{quality.metrics.min_test_coverage}}%) | Media |
| REQ-ART-004 | Cypher queries parametrizados e idempotentes | Alta |
| REQ-ART-005 | Embeddings {{outputs.targets.embeddings}} | Alta |
| REQ-ART-006 | Scripts de carga con dry-run mode | Media |
| REQ-ART-007 | Documentación de uso de artefactos | Media |

**Validación**: MORPHEUS checkpoint (ck-03) PASS (auto-validated)

---

### REQ-EXEC: Ejecución y Validación

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-EXEC-001 | Cargar atomics + relationships a {{outputs.targets.graph_db}} | Alta |
| REQ-EXEC-002 | Validar integridad del grafo (nodos huérfanos, relaciones rotas) | Alta |
| REQ-EXEC-003 | Generar visualizaciones (PNG/SVG) de subgrafos clave | Media |
| REQ-EXEC-004 | Validar hipótesis iniciales contra datos del grafo | Alta |
| REQ-EXEC-005 | Reporte de validación con métricas | Alta |

**Validación**: ALMA checkpoint (ck-04) PASS

---

### REQ-LESSON: Lessons Learned (P2: Autopoiesis)

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-LESSON-001 | Documentar lecciones por rostro | Alta |
| REQ-LESSON-002 | Agregar `summary.yaml` de lecciones | Alta |
| REQ-LESSON-003 | Mejorar spec-issue template para v2.0.0 | Media |
| REQ-LESSON-004 | Identificar anti-patterns encontrados | Media |

**Validación**: Lessons documentadas en `06-lessons/`

---

## 🚫 Non-Functional Requirements

### NFR-1: Trazabilidad (P6)

- **NFR-1.1**: Toda fuente debe tener metadata Dublin Core completa
- **NFR-1.2**: Todo atomic debe referenciar fuente original (field: `source`)
- **NFR-1.3**: Triple output implementado:
  - **Markdown**: Archivos `.md` con HKM headers
  - **Graph**: Nodos y relaciones en Neo4j
  - **Vectors**: Embeddings en vector index
- **NFR-1.4**: Identificadores únicos (UUIDs o slugs) para todos los artefactos

### NFR-2: Minimalismo

- **NFR-2.1**: No duplicar información entre archivos
- **NFR-2.2**: Una sola fuente de verdad por artefacto
- **NFR-2.3**: Evitar documentos monolíticos (preferir archivos atómicos)
- **NFR-2.4**: DRY (Don't Repeat Yourself) en prompts y scripts

### NFR-3: Reproducibilidad

- **NFR-3.1**: Scripts idempotentes (re-ejecutables sin side effects)
- **NFR-3.2**: Versionamiento explícito (SemVer)
- **NFR-3.3**: Dependencias documentadas en `requirements.txt` / `package.json`
- **NFR-3.4**: Logs de ejecución registrados en `Implementation Logs/`

### NFR-4: Validación Continua (P5)

- **NFR-4.1**: Checkpoints por rostro con criterios claros
- **NFR-4.2**: Approval gates donde requerido (ver `config.yaml`)
- **NFR-4.3**: Auto-validación via tests (donde aplique)
- **NFR-4.4**: Validaciones bloqueantes (no continuar si checkpoint falla)

### NFR-5: Mantenibilidad

- **NFR-5.1**: Código limpio (linters: ruff, eslint, etc.)
- **NFR-5.2**: Documentación inline (docstrings, comments)
- **NFR-5.3**: Tests unitarios para scripts críticos
- **NFR-5.4**: README por carpeta con propósito claro

---

## 📊 Priority Order

| Priority | Requirements | Justification |
|----------|--------------|---------------|
| **P0 (Crítico)** | REQ-SETUP | Sin estructura no hay investigación |
| **P1 (Alta)** | REQ-LIT, REQ-ATOM | Sin literatura y atomización no hay conocimiento |
| **P2 (Alta)** | REQ-ANA | Sin análisis no hay síntesis ni valor |
| **P3 (Media)** | REQ-ART | Artefactos son outputs deseados pero no bloqueantes |
| **P4 (Media)** | REQ-EXEC | Validación final, depende de todo lo anterior |
| **P5 (Baja)** | REQ-LESSON | Mejora continua, no bloquea entrega |

---

## ✅ Success Criteria

La investigación se considera **exitosa** si cumple:

### Criteria por Fase

| Phase | Success Criteria |
|-------|-----------------|
| **Literature** | ≥{{quality.metrics.min_sources}} fuentes, ≥{{quality.metrics.min_peer_reviewed}} peer-reviewed |
| **Atomics** | ≥{{quality.metrics.min_atomics}} atomics extraídos + relationships.yaml válido |
| **Analysis** | RQs respondidas + framework recomendado (ADR) |
| **Artifacts** | Solution spec ≥{{quality.metrics.min_solution_spec_lines}} líneas + scripts ejecutables |
| **Execution** | Grafo Neo4j poblado + hipótesis validadas |
| **Lessons** | Lecciones documentadas por rostro |

### Validaciones Técnicas

- ✅ Todos los checkpoints PASS
- ✅ Validadores automáticos ejecutados sin errores
- ✅ Triple output completo (MD + Graph + Vectors)
- ✅ Zero anti-patterns detectados

---

## 🚫 Out of Scope

**NO incluye**:
- Implementación completa del framework (solo spec y scripts)
- Migración de proyectos existentes a la metodología
- Capacitación de usuarios finales
- Integración con herramientas externas (Jira, Notion, etc.)
- Desarrollo de UI/UX para visualización

**Puede incluirse en futuras versiones**:
- Automatización completa del workflow (CI/CD)
- Dashboard de métricas en tiempo real
- Plugin VS Code para gestión de investigaciones

---

## 📚 References

- **Steering Documents**:
  - Product: `.spec-workflow/steering/product.md`
  - Tech: `.spec-workflow/steering/tech.md`
  - Principios MELQUISEDEC: `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md`

- **Related Specs**:
  - Spec Workflow Guide: `.spec-workflow/specs/README.md`

- **External**:
  - Design Science Research: [Hevner et al. 2004]
  - Zettelkasten Method: [Ahrens, "How to Take Smart Notes"]
  - Neo4j Knowledge Graphs: [Neo4j Docs](https://neo4j.com/docs/)

---

**Document Status**: Draft → Approval Pending → Approved
**Next Step**: Create `design.md` after requirements approval
