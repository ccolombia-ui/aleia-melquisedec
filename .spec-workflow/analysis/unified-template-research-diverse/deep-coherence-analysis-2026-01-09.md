# Deep Coherence Analysis: .spec-workflow vs spec-workflow-mcp

> **Fecha**: 2026-01-09
> **Metodología**: Sequential Thinking MCP (12 pasos)
> **Comparado contra**: spec-workflow-mcp-template/ + Context7 docs
> **Analista**: Agente MELQUISEDEC

---

## 📊 Executive Summary

### Hallazgo Principal
El proyecto tiene un **template avanzado excelente archivado** (`archive/tasks.md`, 1551 líneas) que NO está siendo usado en specs activos. Los specs activos usan 4 formatos diferentes de tasks, creando fragmentación e incoherencia.

### Métricas de Coherencia Global
| Área | Coherencia | Estado |
|------|------------|--------|
| Steering Documents | 85% | ✅ Bueno |
| Spec Structure | 65% | ⚠️ Mejorable |
| Task Format | 30% | 🔴 Crítico |
| Lessons Learned | 10% | 🔴 No implementado |
| Approvals | 0% | ⛔ No usado |

---

## 📁 Índice Completo de Componentes

### ROOT: .spec-workflow/

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `README.md` | Entry point del workflow. Mezcla conceptos MCP + DAATH-ZEN + Autopoiesis en un solo documento | 40% | Simplificar. Separar en: README (intro), DAATH-ZEN.md (metodología), AUTOPOIESIS.md (filosofía) |
| `analysis/` | Carpeta con gap analyses y comparativas. Incluye este documento | N/A (extensión) | ✅ Mantener como extensión local |
| `approvals/` | Solo contiene `.gitkeep`. Feature de MCP no implementada | 0% | Implementar workflow de aprobaciones o eliminar |
| `archive/` | Templates avanzados + specs archivados + imágenes | 60% | **CRÍTICO**: Promover `tasks.md` a template activo |
| `steering/` | Documentos de dirección: product, tech, structure | 85% | ✅ Bien alineado |
| `specs/` | 4 specs activos con diferentes formatos | 55% | Estandarizar formato de tasks |
| `_meta/` | Metadata global + templates | 65% | Actualizar templates |

---

### STEERING: steering/

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `product.md` | Visión del producto específica para monorepo-improvements-v1.1.0. Referencia DAATH-ZEN fundamentos | 90% | ✅ Mantener. Bien estructurado |
| `tech.md` | Stack técnico detallado. Python 3.11+, Neo4j 5.x, MCPs listados | 85% | ✅ Mantener |
| `structure.md` | Principios organizacionales del monorepo | 80% | ✅ Mantener |
| `best-practices.md` | **DUPLICADO** - También existe en `_meta/` | N/A | Unificar. Usar solo una ubicación canónica |

---

### _META: _meta/

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `best-practices.md` | Mejores prácticas DAATH-ZEN v2.0.0 | 70% | Mover a `steering/` para centralizar |
| `lessons-learned.md` | Plantilla vacía para lecciones globales | 30% | Implementar con contenido real |
| `context.yaml` | Formato propio para contexto (no es config.yaml estándar MCP) | 30% | Migrar a `config.yaml` formato MCP o documentar divergencia |
| `templates/spec-workflow-mcp-template/` | Templates básicos sin extensiones DAATH-ZEN | 50% | **ACTUALIZAR** con formato avanzado de archive/ |

---

### TEMPLATES: _meta/templates/spec-workflow-mcp-template/

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `tasks-template.md` | Formato básico: `_Leverage:_`, `_Requirements:_`, `_Prompt:_` | 80% (vs MCP) / 40% (vs uso real) | Actualizar agregando: `_Rostro:_`, `_MCPs:_`, `_Lesson:_`, MCP Workflow Strategy table |
| `requirements-template.md` | User Stories + Acceptance Criteria + NFRs | 90% | ✅ Mantener |
| `design-template.md` | Architecture + Components + Data Models | 85% | ✅ Mantener |
| `product-template.md` | Visión y objetivos | 90% | ✅ Mantener |
| `tech-template.md` | Stack técnico template | 85% | ✅ Mantener |
| `structure-template.md` | Estructura del proyecto | 85% | ✅ Mantener |

---

### ARCHIVE: archive/

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `tasks.md` | **TEMPLATE AVANZADO** (1551 líneas). Incluye MCP Workflow Strategy tables, Thinking Mode, diagramas mermaid, Success Criteria detallados | 95% | **PROMOVER** a template activo. Es el formato más completo |
| `specs/demo-fix-references/` | Spec archivado con formato antiguo (pre-DAATH-ZEN) | N/A | ✅ Mantener como referencia histórica |
| `image/` | Contiene carpeta `tasks/` con imágenes | N/A (extensión) | Mover a `_meta/assets/` |
| `templates/` | Templates adicionales archivados | N/A | Revisar y consolidar con `_meta/templates/` |

---

## 📋 SPECS Activos: Análisis Detallado

### SPEC: git-push-workflow-v1.0.0

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `requirements.md` | 6 REQs bien estructurados con prioridad y criterios | 85% | ✅ Mantener |
| `design.md` | Arquitectura del workflow con componentes | 75% | Agregar diagramas mermaid |
| `tasks.md` | 9 tareas formato DAATH-ZEN inline. Todo en `_Prompt:_` comprimido | 60% | Migrar a formato avanzado (archive/tasks.md style) |
| `lessons-learned/` | Solo `.gitkeep` - NO IMPLEMENTADO | 0% | Crear lecciones para task 1.5 completada |
| `_meta/.gitpush.example.yml` | Config de ejemplo para workflow | OK (custom) | Documentar propósito en README |

**Formato actual de tasks:**
```markdown
- [ ] 1.1. Task Name
  - File: target
  - _Requirements: REQ-X_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[...]_
  - _Lesson: path_
  - _Prompt: Role: X | Task: Y | Restrictions: Z | Success: W_
```

**Problemas:**
- `_Prompt:_` comprimido en una línea (difícil de leer)
- Sin `Success Criteria` separados
- Sin `MCP Workflow Strategy` table
- Sin `Thinking Mode` explícito

---

### SPEC: monorepo-improvements

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `README.md` | Overview del spec bien documentado | 80% | ✅ Mantener |
| `requirements.md` | REQs + NFRs organizados | 85% | ✅ Mantener |
| `design.md` | Referencias a ADRs relacionados | 75% | Agregar diagramas |
| `tasks.md` | Formato DAATH-ZEN básico | 55% | Migrar formato |
| `analysis/` | Análisis internos del spec | N/A (custom) | Mover a `_meta/analysis/` |
| `_meta/` | Config adicional específica | OK | ✅ Mantener |

---

### SPEC: research-keter-integration-v1.0.0

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `README.md` | Overview de la migración | 70% | ✅ Mantener |
| `requirements.md` | User Stories format | 70% | ✅ Mantener |
| `design.md` | Diagrama conceptual básico | 65% | Agregar C4/mermaid |
| `tasks.md` | ⚠️ **FORMATO DIFERENTE**: Headers `### TASK-X.X`, campos `**Owner**:`, `**Priority**:`, `**Acceptance Criteria**:` | **30%** | **MIGRAR** a formato estándar DAATH-ZEN |
| `artifacts/` | VACÍO | 0% | Implementar outputs o eliminar |
| `Implementation Logs/` | Sessions de trabajo (session-01, session-02) | N/A (custom) | Renombrar a `_meta/sessions/` |
| `lessons-learned/` | VACÍO | 0% | Implementar lecciones |

**Formato actual de tasks (DIFERENTE):**
```markdown
### TASK-1.1: Title
**Owner**: HYPATIA
**Priority**: high
**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
```

**Problema CRÍTICO**: Este formato NO usa campos DAATH-ZEN (`_Rostro:_`, `_MCPs:_`, `_Lesson:_`). Probablemente creado antes de establecer el estándar.

---

### SPEC: triple-persistence-architecture-best-practices

| Componente | Descripción | Coherencia spec-wf-mcp | Recomendación |
|------------|-------------|------------------------|---------------|
| `requirements.md` | 5 REQs bien definidos con métricas | 85% | ✅ Mantener |
| `design.md` | **NO EXISTE** | 0% | **CREAR** documento de diseño |
| `tasks.md` | Formato DAATH-ZEN detallado (208 líneas). Mejor estructurado que otros | 70% | Migrar a formato avanzado |
| `tasks-ORIGINAL-RECOVERED.md` | Backup de versión anterior | N/A | Mover a `archive/` |
| `lessons-learned/` | Solo `.gitkeep` - NO IMPLEMENTADO | 0% | Implementar para R1.1 completada |

---

## 🔴 GAPS Consolidados

### GAP-1: Fragmentación de Formatos de Tasks
| Atributo | Valor |
|----------|-------|
| **Impacto** | 🔴 CRÍTICO |
| **Descripción** | 4 formatos diferentes de tasks identificados en el proyecto |
| **Causa** | Evolución sin consolidación. Cada spec usó el formato "del momento" |
| **Evidencia** | Ver sección "Análisis de Formatos" abajo |
| **Fix** | Estandarizar en formato `archive/tasks.md` (el más completo) |
| **Esfuerzo** | Alto (migrar 4 specs) |

#### Formatos Identificados:

**Formato 1 - Template Oficial** (`_meta/templates/spec-workflow-mcp-template/tasks-template.md`):
```markdown
- [ ] X. Task Name
  _Leverage:_ tool
  _Requirements:_ REQ-XXX
  _Prompt:_ instructions
```

**Formato 2 - DAATH-ZEN Básico** (git-push-workflow, monorepo-improvements, triple-persistence):
```markdown
- [ ] X.Y. Task Name
  - File: target
  - _Requirements: REQ-X_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[...]_
  - _Lesson: path_
  - _Prompt: Role: X | Task: Y | Restrictions: Z | Success: W_
```

**Formato 3 - Research Headers** (research-keter-integration):
```markdown
### TASK-X.X: Title
**Owner**: Rostro
**Priority**: high|medium|low
**Acceptance Criteria:**
- [ ] Criterion
```

**Formato 4 - DAATH-ZEN Avanzado** (`archive/tasks.md`):
```markdown
### X.Y. [Task Name]
- **File**: target
- **Requirements**: REQ-XXX
- **Rostro**: value
- **Lesson**: path

#### MCP Workflow Strategy
| Aspect | Value |
|--------|-------|
| **Thinking Mode** | sequential | smart-thinking | none |
| **Activation** | MCPs to activate |
| **Parallel** | operations without dependencies |
| **Sequential** | operations with dependencies |
| **Error Handling** | fallback strategy |

#### Prompt
[multiline instructions]

#### Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

---

### GAP-2: Template Avanzado Archivado
| Atributo | Valor |
|----------|-------|
| **Impacto** | 🔴 ALTO |
| **Descripción** | El template más completo (1551 líneas) está en `archive/` en vez de activo |
| **Causa** | Probablemente fue un experimento que nunca se adoptó |
| **Fix** | Promover `archive/tasks.md` a `_meta/templates/spec-workflow-mcp-template/` |
| **Esfuerzo** | Bajo (copiar y adaptar) |

---

### GAP-3: Extensiones DAATH-ZEN No Documentadas
| Atributo | Valor |
|----------|-------|
| **Impacto** | ⚠️ MEDIO |
| **Descripción** | Campos `_Rostro:_`, `_MCPs:_`, `_Lesson:_` usados pero no documentados en templates |
| **Causa** | Extensiones agregadas incrementalmente sin actualizar documentación |
| **Fix** | Actualizar `spec-workflow-mcp-template/` con campos DAATH-ZEN |
| **Esfuerzo** | Bajo |

---

### GAP-4: Carpetas Vacías Sin Propósito
| Atributo | Valor |
|----------|-------|
| **Impacto** | ⚡ BAJO |
| **Descripción** | `approvals/`, `artifacts/`, múltiples `lessons-learned/` vacíos |
| **Causa** | Estructura creada pero features no implementadas |
| **Fix** | Implementar contenido o eliminar carpetas |
| **Esfuerzo** | Variable |

**Carpetas vacías:**
- `.spec-workflow/approvals/` (solo .gitkeep)
- `.spec-workflow/specs/git-push-workflow-v1.0.0/lessons-learned/`
- `.spec-workflow/specs/research-keter-integration-v1.0.0/artifacts/`
- `.spec-workflow/specs/research-keter-integration-v1.0.0/lessons-learned/`
- `.spec-workflow/specs/triple-persistence-architecture-best-practices/lessons-learned/`

---

### GAP-5: Duplicación de Documentos
| Atributo | Valor |
|----------|-------|
| **Impacto** | ⚡ BAJO |
| **Descripción** | `best-practices.md` existe en múltiples ubicaciones |
| **Ubicaciones** | `steering/`, `_meta/` |
| **Fix** | Unificar en una sola ubicación canónica |
| **Esfuerzo** | Bajo |

---

### GAP-6: Research-Keter Incoherente
| Atributo | Valor |
|----------|-------|
| **Impacto** | 🔴 ALTO |
| **Descripción** | Spec usa formato completamente diferente (Research Headers) |
| **Causa** | Probablemente creado antes de establecer DAATH-ZEN como estándar |
| **Fix** | Migrar `tasks.md` a formato estándar DAATH-ZEN |
| **Esfuerzo** | Medio |

---

### GAP-7: context.yaml No Estándar
| Atributo | Valor |
|----------|-------|
| **Impacto** | ⚠️ MEDIO |
| **Descripción** | Usa formato `context.yaml` propio en vez de `config.yaml` estándar MCP |
| **Causa** | Extensión local no alineada con MCP |
| **Fix** | Migrar a `config.yaml` formato MCP o documentar divergencia intencional |
| **Esfuerzo** | Medio |

---

## 📈 Plan de Resolución Propuesto

### Fase 1: Estandarización de Templates (Prioridad: CRÍTICA)
1. **Promover formato avanzado**: Copiar estructura de `archive/tasks.md` a `_meta/templates/spec-workflow-mcp-template/tasks-template.md`
2. **Documentar extensiones**: Agregar sección explicando `_Rostro:_`, `_MCPs:_`, `_Lesson:_`
3. **Crear guía de formato**: Documento explicando cuándo usar cada campo

### Fase 2: Migración de Specs (Prioridad: ALTA)
1. **Migrar research-keter**: Convertir de Research Headers a DAATH-ZEN
2. **Enriquecer specs activos**: Agregar MCP Workflow Strategy tables
3. **Implementar lessons-learned**: Crear contenido para tareas completadas

### Fase 3: Cleanup (Prioridad: BAJA)
1. **Unificar best-practices.md**: Elegir ubicación canónica
2. **Eliminar carpetas vacías**: O implementar contenido
3. **Organizar archive/**: Mover imágenes a `_meta/assets/`

---

## ✅ Recomendación Final

**Adoptar `archive/tasks.md` como el nuevo estándar** porque:

| Característica | Template Actual | archive/tasks.md | Beneficio |
|----------------|-----------------|------------------|-----------|
| MCP Workflow Strategy | ❌ No | ✅ Tabla | Planificación clara de MCPs |
| Thinking Mode | ❌ No | ✅ Explícito | Selección consciente de modo de razonamiento |
| Diagramas | ❌ No | ✅ Mermaid | Visualización de flujos |
| Success Criteria | ❌ Inline | ✅ Checklist separado | Validación fácil |
| Prompt | ❌ Una línea | ✅ Bloque código | Legibilidad |
| DAATH-ZEN fields | ⚠️ Parcial | ✅ Completo | Consistencia metodológica |

---

*Documento generado con análisis Sequential Thinking MCP. Pendiente aprobación para implementar cambios.*
