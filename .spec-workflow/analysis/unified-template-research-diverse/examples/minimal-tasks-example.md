# Ejemplo: tasks.md Minimalista

> **Concepto clave**: Los tasks son SIMPLES, MINIMALISTAS. Referencian documentos formales.
> El detalle vive en `requirements.md` y `design.md`.

---

## 📋 Formato spec-workflow-mcp Oficial

```markdown
# [Spec-Name] Implementation Tasks

## Overview
Brief summary referencing requirements and design documents.

**References:**
- [Requirements](./requirements.md) - REQ-1 to REQ-N
- [Design](./design.md) - Architecture decisions, ADRs
- [Tech Steering](../../../steering/tech.md) - Stack guidelines

## Tasks

### 1. [Category/Module Name]

#### 1.1 [Task Title]
- **Status**: pending | in-progress | completed
- **Files**: `path/to/file.ts`
- **Requirements**: REQ-1, REQ-2
- **Acceptance Criteria**:
  - [ ] Criterion from requirements.md

#### 1.2 [Task Title]
- **Status**: pending
- **Files**: `path/to/file.ts`
- **Requirements**: REQ-3
- **Design Reference**: design.md#section-name
```

---

## 🎯 Ejemplo Concreto: INVESTIGACIÓN-SPEC-METODOLOGIA

### `.spec-workflow/specs/daath-zen-concepto/tasks.md`

```markdown
# DAATH-ZEN-CONCEPTO Implementation Tasks

## Overview
Implementación del artefacto CONCEPTO para la metodología DAATH-ZEN.

**References:**
- [Requirements](./requirements.md) - REQ-C1 a REQ-C4
- [Design](./design.md) - ADR-001, Template refs
- [Artifact Template](../../artifact-templates/daath-zen-concepto-tpl.md)

---

## Tasks

### 1. Estructura del Artefacto

#### 1.1 Crear folder structure
- **Status**: pending
- **Files**: `outputs/concepts/{concept-name}/`
- **Requirements**: REQ-C1
- **Outputs**:
  - [ ] `{concept-name}/`
  - [ ] `document.md`
  - [ ] `metadata.yaml-ld`
  - [ ] `graph.cypher`

#### 1.2 Generar documento principal
- **Status**: pending
- **Files**: `document.md`
- **Requirements**: REQ-C2
- **Template**: `artifact-templates/daath-zen-concepto-tpl.md#document-section`

### 2. Validación y Outputs

#### 2.1 Generar Cypher para Neo4j
- **Status**: pending
- **Files**: `graph.cypher`
- **Requirements**: REQ-C3
- **Design Reference**: design.md#neo4j-schema

#### 2.2 Validar coherencia con ontología
- **Status**: pending
- **Requirements**: REQ-C4
- **Validator**: `validators/concept-validator.py`
```

---

## 📐 Comparación: Antes vs Después

### ❌ ANTES (archive/tasks.md - 1551 líneas)
```markdown
## TASK: Analizar framework existente

### Contexto
El framework DAATH-ZEN existe como documentación dispersa...
[200 líneas de contexto que debería estar en requirements.md]

### Criterios de Aceptación
- Documentar los 5 Rostros del DAATH-ZEN
- Crear matriz de responsabilidades
[50 líneas que deberían estar en requirements.md]

### Guía de Implementación
1. Revisar archivos en _templates/daath-zen-patterns/
2. Extraer definiciones formales...
[100 líneas que deberían estar en design.md]

### Outputs Esperados
- Cypher: CREATE (rostro:Rostro {...})
[Código inline que debería estar en un template]
```

### ✅ DESPUÉS (Minimalista)
```markdown
#### 1.1 Analizar framework DAATH-ZEN existente
- **Status**: pending
- **Files**: `analysis/daath-zen-framework-analysis.md`
- **Requirements**: REQ-F1, REQ-F2
- **Design Reference**: design.md#daath-zen-ontology
- **Acceptance Criteria**:
  - [ ] Los 5 Rostros documentados (REQ-F1)
  - [ ] Matriz de responsabilidades generada (REQ-F2)
```

**Nota**: El detalle vive en los documentos referenciados, no en el task.

---

## 📚 Dónde Vive Cada Cosa

| Contenido | Documento | Razón |
|-----------|-----------|-------|
| Qué es el DAATH-ZEN | `requirements.md` | Define el "qué" |
| Criterios de aceptación | `requirements.md` | Son requerimientos funcionales |
| Cómo estructurar los outputs | `design.md` | Decisiones de arquitectura |
| ADRs (Architecture Decision Records) | `design.md` | Decisiones técnicas |
| Referencias a guías/templates | `design.md` | Recursos de diseño |
| Lista de tareas con status | `tasks.md` | Solo tracking |
| Código de templates/microprompts | `artifact-templates/` | Artefactos reutilizables |

---

## 🔄 Flujo de Trabajo

```
1. requirements.md (BLOCKING: Approval Required)
   ↓
2. design.md (BLOCKING: Approval Required)
   ↓
3. tasks.md (BLOCKING: Approval Required)
   ↓
4. Implementation (task by task)
   └── Each task references requirements + design
```

---

## 💡 Insight Clave

> **spec-workflow-mcp separa CONCERNS:**
> - `requirements.md` = QUÉ construir (user stories, requisitos)
> - `design.md` = CÓMO construirlo (ADRs, arquitectura, refs a templates)
> - `tasks.md` = TRACKING de implementación (simple, con refs)
>
> El archivo `archive/tasks.md` mezclaba TODO esto en un solo lugar.
> Por eso fue archivado correctamente.
