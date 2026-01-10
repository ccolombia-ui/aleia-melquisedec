# Análisis de Gaps y Recomendaciones
## research-autopoietic-template

> **Fecha:** 2026-01-10
> **Versión:** 1.0.0
> **Autor:** GitHub Copilot (Claude Sonnet 4.5)
> **Propósito:** Análisis crítico de gaps entre manifiesto y estructura actual, con recomendaciones de corrección

---

## 📊 RESUMEN EJECUTIVO

### Hallazgos Críticos

**🔴 GAPS CRÍTICOS IDENTIFICADOS:**

1. **❌ Desalineación Fundamental:** El folder fue creado sin revisar rigurosamente el manifiesto
2. **❌ INDICE Desactualizado:** El índice propone un approach "atómico" pero la estructura real es monolítica
3. **❌ Confusión Workflow:** Mezcla "Main Spec" con "Sub-Issues" sin claridad
4. **❌ Templates No Documentados:** Menciona templates pero no especifica que cada REQ es documento independiente
5. **❌ Sin Implementación Real:** 157 issues propuestos, 0 implementados
6. **❌ Spec-workflow-mcp Mal Aplicado:** Usa herramienta para casos que no requieren approval

### Lo que SÍ está Correcto

**✅ ACIERTOS:**

1. ✅ ISSUE.yaml creado correctamente siguiendo RBM-GAC
2. ✅ Estructura de carpetas 010-060 siguiendo manifiesto
3. ✅ Principios documentados correctamente
4. ✅ Intención de modularidad (approach atómico) es correcta
5. ✅ README.md bien estructurado

---

## 🔍 ANÁLISIS DETALLADO DE GAPS

### GAP #1: Cada Requerimiento es un Documento Independiente

#### Lo que Dice el Manifiesto

**Sección 9.1 - Templates (líneas 6000-6500):**

```markdown
# 9.1 Templates Estructura de Documentos

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

**Evidencia en Manifiesto:**

> "Cada requerimiento se documenta en archivo separado siguiendo
> Zettelkasten. El requirements.md es el hub note que los vincula."
> (Sección 9.1.2, línea 6123)

#### Lo que Tiene el Proyecto Actualmente

**❌ PROBLEMA:** [requirements.md](requirements.md) tiene 290 líneas TOTALES, asumiendo que es monolítico.

**Estructura Incorrecta Actual:**
```
010-define/
├── requirements.md          # 290 líneas - ¿Es índice o monolito?
└── workbooks/               # ❌ VACÍO - No hay REQ-XXX.md
```

#### Corrección Requerida

**✅ ESTRUCTURA CORRECTA:**

```
010-define/
├── requirements.md                    # 200 líneas - ÍNDICE con tabla
└── workbooks/
    ├── REQ-001-template-system.md     # 180 líneas
    ├── REQ-002-pattern-registry.md    # 150 líneas
    ├── REQ-003-confidence-scores.md   # 160 líneas
    ├── ...
    └── REQ-015-rollback-mechanisms.md # 140 líneas
```

**Contenido de requirements.md (ÍNDICE):**

```markdown
# Requirements - Research Autopoietic Templates

## Índice de Requerimientos

| ID | Nombre | Prioridad | Estado | Dependencias |
|----|--------|-----------|--------|--------------|
| [[REQ-001-template-system]] | Template System | Alta | ⏳ En progreso | - |
| [[REQ-002-pattern-registry]] | Pattern Registry | Alta | ❌ No iniciado | REQ-001 |
| [[REQ-003-confidence-scores]] | Confidence Scores | Alta | ❌ No iniciado | - |
| ... | ... | ... | ... | ... |

## Métricas

- Total: 15 requerimientos
- Completados: 0 (0%)
- En progreso: 1 (6.7%)
- Bloqueados: 3 (20%)
```

---

### GAP #2: INDICE-COMPLETO-ARTEFACTOS.md Propone Pero No Implementa

#### El Problema

**INDICE-COMPLETO-ARTEFACTOS.md v3.1.0:**
- Propone 157 issues (REQ, CONCEPT, LIT, DESIGN, IMPL)
- Documenta approach "atómico" vs "monolítico"
- **PERO:** No hay NINGÚN issue creado en `.spec-workflow/specs/`

**Verificación:**
```bash
# Comando ejecutado:
ls .spec-workflow/specs/

# Resultado:
autopoietic-templates/    # ← Main Spec (único que existe)
# ❌ NO EXISTEN: REQ-001/, CONCEPT-001/, LIT-001/, etc.
```

#### La Confusión

El índice dice:

> "**Paso 1:** Crear Issue Directory
> `mkdir -p .spec-workflow/specs/REQ-001-template-system/`"

**❌ PERO:** Nadie ejecutó estos pasos. El índice es puramente teórico.

#### Corrección Requerida

**Opción A: Implementar lo Propuesto (Recomendada)**

1. Crear template base: `requirement-issue.yaml`
2. Crear primeros 3 ejemplos:
   - `.spec-workflow/specs/REQ-001-template-system/`
   - `.spec-workflow/specs/CONCEPT-001-autopoiesis/`
   - `.spec-workflow/specs/LIT-001-hevner-dsr/`
3. Crear workbooks correspondientes
4. Actualizar INDICE con progreso real

**Opción B: Actualizar INDICE a Realidad**

- Reconocer que el approach atómico NO está implementado
- Documentar el plan pero sin pretender que existe
- Crear roadmap realista de implementación

---

### GAP #3: Confusión sobre Main Spec vs Sub-Issues

#### Lo que Dice el Manifiesto sobre spec-workflow-mcp

**Manifiesto, Sección 10 - Herramienta spec-workflow-mcp:**

```markdown
# 10. spec-workflow-mcp: Workflows

## Main Spec (CON approval)

**Uso:** Spec principal del proyecto (1 por investigación)
**Workflow:** Requirements → Design → Tasks → Implementation
**Tools:** `mcp_spec-workflow2_spec-workflow-guide()`, `approvals()`
**Timing:** 8 semanas (4 fases × 2 semanas)

## Sub-Issues (SIN approval)

**Uso:** Componentes atómicos (REQ, CONCEPT, LIT, DESIGN, IMPL)
**Workflow:** Crear ISSUE.yaml → Escribir workbook → Actualizar índice
**Tools:** `create_file`, `replace_string_in_file`
**Timing:** 30 min - 5 h según tipo
```

#### El Problema Actual

**INDICE-COMPLETO-ARTEFACTOS.md:**

- Sección "MAIN SPEC vs SUB-ISSUES" (líneas 300-600)
- **Diagrama de decisión** explicando cuándo usar cada workflow
- **PERO:** Mezcla conceptos y no queda claro qué hacer primero

**Pregunta Sin Respuesta:**

> "¿Creo el Main Spec (autopoietic-templates) O creo los Sub-Issues (REQ-001)?"

#### Corrección Requerida

**✅ JERARQUÍA CLARA:**

```
NIVEL 1: Main Spec (autopoietic-templates)
  ├── requirements.md         # Documento del Main Spec
  └── design.md               # Documento del Main Spec

NIVEL 2: Sub-Issues (componentes atómicos)
  ├── REQ-001/
  │   ├── ISSUE.yaml
  │   └── workbook (en 010-define/workbooks/)
  ├── CONCEPT-001/
  └── LIT-001/
```

**Flujo Recomendado:**

1. **PRIMERO:** Completar Main Spec (Requirements Phase)
   - Aprobar requirements.md del Main Spec
   - Este requirements.md es el ÍNDICE de REQ-XXX

2. **SEGUNDO:** Crear Sub-Issues (REQ-001, REQ-002)
   - Cada REQ-XXX es archivo separado
   - NO requieren approval (es trabajo interno)

3. **TERCERO:** Consolidar para Design Phase del Main Spec
   - Leer todos los REQ-XXX
   - Crear design.md del Main Spec
   - Solicitar approval de design.md

---

### GAP #4: Templates No Están Especificados Correctamente

#### Lo que Dice el Manifiesto

**Sección 9 - Sistema de Templates:**

```markdown
# 9.1 Templates por Tipo

## requirement-issue.yaml (Template para REQ-XXX)

id: REQ-{XXX}-{nombre}
type: requirement
category: functional|non-functional|constraint
priority: high|medium|low
status: draft|active|completed

requirement:
  description: "..."
  acceptance_criteria:
    - "Criterion 1"
    - "Criterion 2"

dependencies:
  requirements: [REQ-YYY]
  concepts: [CONCEPT-ZZZ]

workbook: "010-define/workbooks/REQ-{XXX}.md"
```

#### El Problema Actual

**❌ NO EXISTE:** Ningún template para issues atómicos

**Ubicación Esperada:**
```
.spec-workflow/_meta/templates/
├── requirement-issue.yaml.template    # ❌ NO EXISTE
├── concept-issue.yaml.template        # ❌ NO EXISTE
├── literature-issue.yaml.template     # ❌ NO EXISTE
├── design-issue.yaml.template         # ❌ NO EXISTE
└── implementation-issue.yaml.template # ❌ NO EXISTE
```

#### Corrección Requerida

**Crear Templates Base:**

1. `requirement-issue.yaml.template`
2. `concept-issue.yaml.template`
3. `literature-issue.yaml.template`
4. `design-issue.yaml.template`
5. `implementation-issue.yaml.template`

**Ejemplo: requirement-issue.yaml.template**

```yaml
---
id: REQ-{XXX}-{nombre-kebab-case}
type: requirement
category: functional  # functional|non-functional|constraint
priority: high        # high|medium|low
status: draft         # draft|active|completed|archived

requirement:
  description: |
    {Descripción clara de 1-2 párrafos del requerimiento}

  acceptance_criteria:
    - "WHEN {evento} THEN {sistema} SHALL {respuesta}"
    - "IF {precondición} THEN {sistema} SHALL {respuesta}"

  rationale: |
    {Por qué este requerimiento es necesario}

dependencies:
  requirements: []      # [REQ-001, REQ-002]
  concepts: []          # [CONCEPT-017]
  literature: []        # [LIT-003]

implements:
  - goal: "{Goal del ISSUE.yaml principal}"

workbook: "010-define/workbooks/REQ-{XXX}-{nombre}.md"

metrics:
  size_estimate: "{100-200 líneas}"
  complexity: "{low|medium|high}"
  timing_estimate: "{2-3 horas}"
---
```

---

### GAP #5: Approach Minimalista No Aplicado

#### Lo que Propone el Manifiesto

**Principio "Menos es Más" (Sección 4.2):**

> "Cada documento debe caber en una pantalla (≤300 líneas).
> Si supera 300 líneas, SPLIT en múltiples documentos."

**INDICE-COMPLETO-ARTEFACTOS.md v3.1.0:**

> "**CRITICAL**: Implementado sistema minimalista configurable
> - 1 template base (30 líneas genéricas)
> - 5 configs pequeños (requirement, concept, literature, design, implementation)
> - Variables dependientes CALCULADAS (NO hardcoded)"

#### El Problema Actual

**❌ NO IMPLEMENTADO:**

```bash
# Buscar sistema minimalista:
ls .spec-workflow/_meta/

# Resultado:
README-SISTEMA-MINIMALISTA.md    # ✅ Documentación existe
# ❌ PERO: template-base.yaml NO EXISTE
# ❌ PERO: config-requirement.yaml NO EXISTE
```

**README-SISTEMA-MINIMALISTA.md:**
- Documenta el sistema minimalista
- **PERO:** Es solo documentación teórica
- **NO HAY:** Implementación real de `template-base.yaml`

#### Corrección Requerida

**Implementar Sistema Minimalista:**

1. Crear `template-base.yaml` (30 líneas, genérico)
2. Crear `config-requirement.yaml` (variables específicas)
3. Crear `config-concept.yaml`
4. Crear `config-literature.yaml`
5. Crear `config-design.yaml`
6. Crear `config-implementation.yaml`

**Ejemplo: template-base.yaml**

```yaml
# Template Base Minimalista v1.0.0
# Variables se CALCULAN desde config-{type}.yaml

id: "{{type}}-{{id}}-{{name}}"
type: "{{type}}"
category: "{{category}}"
priority: "{{priority}}"
status: "{{status}}"

{{type}}:
  {{#if description}}
  description: "{{description}}"
  {{/if}}

  {{#if acceptance_criteria}}
  acceptance_criteria: {{acceptance_criteria}}
  {{/if}}

  {{#if key_concepts}}
  key_concepts: {{key_concepts}}
  {{/if}}

dependencies:
  {{#each dependency_types}}
  {{this}}: []
  {{/each}}

workbook: "{{territory}}/{{workbook_path}}"

metrics:
  size_estimate: "{{calculated.size_estimate}}"
  complexity: "{{calculated.complexity}}"
  timing_estimate: "{{calculated.timing_estimate}}"
```

**Ejemplo: config-requirement.yaml**

```yaml
# Config para Requerimientos (REQ-XXX)

type: "requirement"
territory: "010-define/workbooks"
workbook_path: "REQ-{{id}}-{{name}}.md"

categories:
  - "functional"
  - "non-functional"
  - "constraint"

dependency_types:
  - "requirements"
  - "concepts"
  - "literature"

fields:
  - name: "description"
    required: true
    type: "string"
  - name: "acceptance_criteria"
    required: true
    type: "array"
  - name: "rationale"
    required: false
    type: "string"

calculated:
  size_estimate:
    formula: "base_lines + (criteria_count * 15)"
    base_lines: 100
  complexity:
    formula: "if dependencies > 3 then 'high' else 'medium'"
  timing_estimate:
    formula: "(size_estimate / 60) hours"
```

---

## 🎯 RECOMENDACIONES DE CORRECCIÓN

### Recomendación #1: Actualizar INDICE-COMPLETO-ARTEFACTOS.md

**Acción:** Reescribir secciones clave para reflejar realidad actual

**Cambios Específicos:**

#### Sección "📊 Resumen Ejecutivo"

**ANTES (Incorrecto):**
```markdown
### Inventario Total de Artefactos (Actualizado)

| Categoría | Issues | Docs | Total | % Completado |
|-----------|--------|------|-------|--------------|
| **📋 Fundamentos** | 15 REQ | 15 workbooks | 30 | 6.7% (2 ✅) |
```

**DESPUÉS (Correcto):**
```markdown
### Inventario Total de Artefactos (Estado Real)

| Categoría | Issues Propuestos | Issues Creados | % Implementado |
|-----------|-------------------|----------------|----------------|
| **📋 Fundamentos** | 15 REQ | 0 | 0% |
| **🧠 Conceptos** | 50 CONCEPT | 0 | 0% |
| **📚 Literatura** | 25 LIT | 0 | 0% |
| **🏛️ Diseño** | 5 DESIGN | 0 | 0% |
| **🔨 Implementación** | 62 IMPL | 0 | 0% |
| **TOTAL** | **157 issues** | **0** | **0%** |

**Estado Actual:** Approach atómico DOCUMENTADO pero NO implementado.
```

#### Sección "🎯 Próximos Pasos Inmediatos"

**AGREGAR:**

```markdown
### ⚠️ CRÍTICO: Estado Real del Proyecto

**❌ LO QUE NO ESTÁ HECHO:**
1. ❌ Ningún Sub-Issue creado (0/157)
2. ❌ Ningún workbook escrito (0/15 REQ)
3. ❌ Templates de issues no existen
4. ❌ Sistema minimalista no implementado

**✅ LO QUE SÍ ESTÁ HECHO:**
1. ✅ ISSUE.yaml principal
2. ✅ Estructura de carpetas 010-060
3. ✅ README.md y documentación
4. ✅ Este índice (como plan)

**🎯 PRIORIDAD INMEDIATA (Sprint 0):**

1. **Decidir:** ¿Implementar approach atómico O mantener monolítico?
2. **Si Atómico:** Crear templates + primeros 3 ejemplos
3. **Si Monolítico:** Actualizar INDICE para reflejar realidad
4. **Ambos Casos:** Crear REQ-001 (template system) como prueba
```

---

### Recomendación #2: Crear Documento de Gaps (Este Archivo)

**Acción:** Mantener este análisis como referencia

**Ubicación:** `010-define/ANALISIS-GAPS-Y-RECOMENDACIONES.md`

**Propósito:**
- Documentar gaps identificados
- Proporcionar evidencia desde manifiesto
- Guiar correcciones futuras

---

### Recomendación #3: Implementar Primeros 3 Ejemplos (Proof of Concept)

**Objetivo:** Validar approach atómico con casos reales

**Tareas:**

#### 3.1. Crear Templates Base

```bash
# Crear templates de issues
.spec-workflow/_meta/templates/
├── requirement-issue.yaml.template
├── concept-issue.yaml.template
└── literature-issue.yaml.template
```

#### 3.2. Crear Primeros 3 Issues

**REQ-001: Template System**
```bash
mkdir -p .spec-workflow/specs/REQ-001-template-system/
create ISSUE.yaml
create 010-define/workbooks/REQ-001-template-system.md
update 010-define/requirements.md (índice)
```

**CONCEPT-001: Autopoiesis**
```bash
mkdir -p .spec-workflow/specs/CONCEPT-001-autopoiesis/
create ISSUE.yaml
create 020-conceive/02-atomics/CONCEPT-001-autopoiesis.md
create 020-conceive/concepts-index.md (nuevo índice)
```

**LIT-001: Hevner DSR**
```bash
mkdir -p .spec-workflow/specs/LIT-001-hevner-dsr/
create ISSUE.yaml
create 020-conceive/01-literature/LIT-001-hevner-dsr.md
create 020-conceive/literature-index.md (nuevo índice)
```

#### 3.3. Validar Approach

**Criterios de Validación:**
- ✅ Cada issue es autocontenido
- ✅ Tamaño ≤300 líneas por documento
- ✅ Referencias bidireccionales funcionan
- ✅ Obsidian graph view es navegable
- ✅ Toma ≤35 min crear un REQ-XXX

**Si Validación Exitosa:**
→ Continuar con REQ-002, REQ-003, etc.

**Si Validación Falla:**
→ Revertir a approach monolítico documentado

---

### Recomendación #4: Actualizar requirements.md a Índice

**Objetivo:** Convertir requirements.md en hub note

**Acción:**

#### Paso 1: Backup Actual

```bash
cp 010-define/requirements.md 010-define/requirements-old.md
```

#### Paso 2: Crear Nuevo requirements.md (Índice)

```markdown
# Requirements - Research Autopoietic Templates

> **Spec ID:** ISSUE-SPEC-001-design-autopoietic-templates
> **Phase:** 010-define
> **Rostro:** MELQUISEDEC
> **Status:** active

---

## 🎯 Visión General

Este documento es el **ÍNDICE** de todos los requerimientos individuales.
Cada requerimiento se documenta en archivo separado siguiendo approach
Zettelkasten (notas atómicas vinculadas).

**Total Requerimientos:** 15
**Ubicación Workbooks:** `010-define/workbooks/REQ-XXX-{nombre}.md`
**Ubicación Issues:** `.spec-workflow/specs/REQ-XXX-{nombre}/`

---

## 📋 Tabla de Requerimientos

| ID | Nombre | Prioridad | Estado | Dependencias | Tamaño |
|----|--------|-----------|--------|--------------|--------|
| [[REQ-001-template-system]] | Template System Architecture | Alta | ⏳ En progreso | - | 180 líneas |
| [[REQ-002-pattern-registry]] | Pattern Registry | Alta | ❌ No iniciado | REQ-001 | 150 líneas |
| [[REQ-003-confidence-scores]] | Confidence Scores | Alta | ❌ No iniciado | - | 160 líneas |
| [[REQ-004-triple-persistence]] | Triple Persistence Sync | Alta | ❌ No iniciado | - | 170 líneas |
| [[REQ-005-template-versioning]] | Template Versioning | Media | ❌ No iniciado | REQ-001 | 140 líneas |
| [[REQ-006-lens-adaptation]] | Lens Adaptation | Media | ❌ No iniciado | REQ-001 | 150 líneas |
| [[REQ-007-autopoietic-feedback]] | Autopoietic Feedback Loop | Alta | ❌ No iniciado | REQ-003 | 180 líneas |
| [[REQ-008-phase-state]] | Phase State Management | Media | ❌ No iniciado | - | 140 líneas |
| [[REQ-009-checkpoint-validation]] | Checkpoint Validation | Alta | ❌ No iniciado | REQ-008 | 150 líneas |
| [[REQ-010-script-orchestration]] | Script Orchestration | Media | ❌ No iniciado | - | 160 líneas |
| [[REQ-011-pattern-evolution]] | Pattern Evolution | Media | ❌ No iniciado | REQ-002, REQ-007 | 150 líneas |
| [[REQ-012-neo4j-sync]] | Neo4j Synchronization | Alta | ❌ No iniciado | REQ-004 | 170 líneas |
| [[REQ-013-vector-embedding]] | Vector Embedding | Media | ❌ No iniciado | REQ-004 | 150 líneas |
| [[REQ-014-dashboard-ui]] | Dashboard UI (ASCII) | Baja | ❌ No iniciado | - | 120 líneas |
| [[REQ-015-rollback-mechanism]] | Rollback Mechanism | Media | ❌ No iniciado | - | 140 líneas |

---

## 📊 Métricas de Progreso

### Por Estado
- ✅ Completados: 0 (0%)
- ⏳ En progreso: 1 (6.7%)
- ❌ No iniciados: 14 (93.3%)

### Por Prioridad
- 🔴 Alta: 7 requerimientos (46.7%)
- 🟡 Media: 7 requerimientos (46.7%)
- 🟢 Baja: 1 requerimiento (6.6%)

### Por Dependencias
- Sin dependencias: 9 requerimientos (60%)
- Con 1 dependencia: 4 requerimientos (26.7%)
- Con 2+ dependencias: 2 requerimientos (13.3%)

---

## 🔄 Workflow de Requerimientos

### Crear Nuevo Requerimiento (REQ-XXX)

**Paso 1:** Crear issue directory
```bash
mkdir -p .spec-workflow/specs/REQ-XXX-{nombre}/
```

**Paso 2:** Crear ISSUE.yaml
```bash
cp .spec-workflow/_meta/templates/requirement-issue.yaml.template \
   .spec-workflow/specs/REQ-XXX-{nombre}/ISSUE.yaml
# Editar: id, description, acceptance_criteria, dependencies
```

**Paso 3:** Crear workbook
```bash
# Crear archivo:
010-define/workbooks/REQ-XXX-{nombre}.md

# Contenido (180 líneas promedio):
# - Gap (problema actual)
# - Goal (objetivo del requerimiento)
# - Outcomes (criterios mesurables)
# - Acceptance Criteria (EARS format)
# - Dependencias (REQ/CONCEPT/LIT)
# - Implementado Por (IMPL-XXX)
# - Success Criteria
```

**Paso 4:** Actualizar este índice
```markdown
| [[REQ-XXX-{nombre}]] | {Nombre} | {Prioridad} | ⏳ En progreso | ... | {Tamaño} |
```

**Paso 5:** Commit
```bash
git add .spec-workflow/specs/REQ-XXX-{nombre}/
git add 010-define/workbooks/REQ-XXX-{nombre}.md
git add 010-define/requirements.md
git commit -m "feat: Add REQ-XXX {nombre} requirement"
```

---

## 🎓 Filosofía: Approach Atómico

### ¿Por Qué Documentos Separados?

**Ventajas:**
- ✅ **Cognitive Load Óptimo:** 150-200 líneas por documento
- ✅ **Zero Conflicts:** Múltiples personas trabajando simultáneamente
- ✅ **Progress Granular:** "REQ-001 ✅, REQ-002 ⏳, REQ-003 ❌"
- ✅ **Easy Review:** Reviewers evalúan 1 requerimiento a la vez
- ✅ **Paralelización:** 3-4 personas trabajando en paralelo
- ✅ **Obsidian-Friendly:** Graph view navegable

**Reglas:**
- 📏 **Límite Superior:** 200 líneas por workbook
- 🔗 **Referencias Bidireccionales:** [[REQ-001]] menciona [[CONCEPT-017]] y viceversa
- 📋 **Issue-Driven:** Cada REQ-XXX tiene issue trackeable
- 🎯 **Autocontenido:** Cada workbook es comprensible por sí solo

---

## 📖 Referencias

### Manifiesto MELQUISEDEC

- **Sección 9.1:** Templates de Documentos (requisitos)
- **Sección 4.2:** Principio "Menos es Más" (≤300 líneas)
- **Principio P7:** Recursión Fractal (issue-spec pattern)

### Documentos Relacionados

- [INDICE-COMPLETO-ARTEFACTOS.md](INDICE-COMPLETO-ARTEFACTOS.md) - Índice maestro completo
- [ANALISIS-GAPS-Y-RECOMENDACIONES.md](ANALISIS-GAPS-Y-RECOMENDACIONES.md) - Gaps identificados
- [ISSUE.yaml](../ISSUE.yaml) - Issue principal del proyecto
- [design.md](../design.md) - Arquitectura de alto nivel

---

**Versión:** 2.0.0 (ÍNDICE)
**Última actualización:** 2026-01-10
**Mantenido por:** MELQUISEDEC (Rostro Orquestador)
**Filosofía:** "Menos es Más" - Un requerimiento, un archivo
```

#### Paso 3: Migrar Contenido Actual a REQ-001

```bash
# Extraer información relevante de requirements-old.md
# Crear 010-define/workbooks/REQ-001-template-system.md
# Completar con 180 líneas detalladas
```

---

### Recomendación #5: Activar MCP Tools y Comenzar Implementación

#### Contexto: Herramientas Disponibles

**MCPs Activados:**
- ✅ `spec-workflow2_spec-workflow-guide` - Workflow para Main Spec
- ✅ `spec-workflow2_steering-guide` - Workflow para Steering Docs
- ✅ `spec-workflow2_approvals` - Sistema de aprobaciones
- ✅ `spec-workflow2_log-implementation` - Logging de implementaciones

**MCPs Disponibles (No Activados):**
- ⏳ Smart-thinking (memoria) - Para conceptos
- ⏳ Obsidian (vault) - Para navegación
- ⏳ Filesystem (avanzado) - Para operaciones de archivos
- ⏳ Git (avanzado) - Para operaciones git

#### Workflow Recomendado

**Fase 1: Setup (Sprint 0) - 3 días**

1. **Día 1:** Crear Templates Base
   - `requirement-issue.yaml.template`
   - `concept-issue.yaml.template`
   - `literature-issue.yaml.template`
   - **Tool:** `create_file`

2. **Día 2:** Crear Primeros 3 Ejemplos
   - REQ-001-template-system
   - CONCEPT-001-autopoiesis
   - LIT-001-hevner-dsr
   - **Tool:** `create_file` + `replace_string_in_file`

3. **Día 3:** Validar y Ajustar
   - Review de approach
   - Ajustes a templates
   - Documentar learnings

**Fase 2: Requirements (Sprint 1) - 1 semana**

1. **Completar Main Spec Requirements.md (ÍNDICE)**
   - **Tool:** `mcp_spec-workflow2_spec-workflow-guide()`
   - Crear requirements.md como índice
   - **Tool:** `mcp_spec-workflow2_approvals(action: request)`
   - Poll hasta approved
   - **Tool:** `mcp_spec-workflow2_approvals(action: delete)`

2. **Crear Sub-Issues REQ-002 a REQ-005**
   - **NO USAR:** approvals (sub-issues no requieren)
   - **USAR:** `create_file` para ISSUE.yaml + workbook
   - **USAR:** `replace_string_in_file` para actualizar índice

**Fase 3: Conceive (Sprint 2-3) - 2 semanas**

1. **Literatura (PARALELO):** LIT-001 a LIT-010
   - Lectura + notas
   - 1-2 horas por paper

2. **Conceptos (PARALELO):** CONCEPT-001 a CONCEPT-020
   - Extracción desde literatura
   - 30 min por concepto

**Fase 4: Design (Sprint 4-5) - 2 semanas**

1. **Completar Main Spec Design.md**
   - **Tool:** `mcp_spec-workflow2_spec-workflow-guide()`
   - **Tool:** `approvals(action: request/status/delete)`

2. **Crear DESIGN-001 a DESIGN-005** (sub-issues)
   - **Tool:** `create_file`

**Fase 5: Build (Sprint 6-12) - 6 semanas**

1. **Implementar IMPL-001 a IMPL-062**
   - Scripts (22), Templates (28), Patterns (8), Lenses (4)
   - **⚠️ CRÍTICO:** `mcp_spec-workflow2_log-implementation()`

**Fase 6: Release (Sprint 13-14) - 2 semanas**

1. **Completar Main Spec Tasks.md**
   - **Tool:** `mcp_spec-workflow2_spec-workflow-guide()`
   - **Tool:** `approvals(action: request/status/delete)`

2. **Publicar Outputs**

---

## 🚀 PLAN DE ACCIÓN INMEDIATO

### Sprint 0: Proof of Concept (3 días)

#### Objetivo
Validar approach atómico creando primeros 3 ejemplos

#### Tareas

**✅ Tarea 0.1: Crear requirement-issue.yaml.template**
- **Ubicación:** `.spec-workflow/_meta/templates/requirement-issue.yaml.template`
- **Tamaño:** ~50 líneas
- **Timing:** 30 min
- **Tool:** `create_file`

**✅ Tarea 0.2: Crear REQ-001 (Ejemplo Completo)**
- **Issue:** `.spec-workflow/specs/REQ-001-template-system/ISSUE.yaml`
- **Workbook:** `010-define/workbooks/REQ-001-template-system.md` (180 líneas)
- **Timing:** 1 hora
- **Tools:** `create_file` × 2, `replace_string_in_file` (índice)

**✅ Tarea 0.3: Crear CONCEPT-001 (Ejemplo Completo)**
- **Issue:** `.spec-workflow/specs/CONCEPT-001-autopoiesis/ISSUE.yaml`
- **Workbook:** `020-conceive/02-atomics/CONCEPT-001-autopoiesis.md` (100 líneas)
- **Índice:** `020-conceive/concepts-index.md` (nuevo)
- **Timing:** 45 min
- **Tools:** `create_file` × 3

**✅ Tarea 0.4: Crear LIT-001 (Ejemplo Completo)**
- **Issue:** `.spec-workflow/specs/LIT-001-hevner-dsr/ISSUE.yaml`
- **Workbook:** `020-conceive/01-literature/LIT-001-hevner-dsr.md` (150 líneas)
- **Índice:** `020-conceive/literature-index.md` (nuevo)
- **Timing:** 1.5 horas (lectura + notas)
- **Tools:** `create_file` × 3

**✅ Tarea 0.5: Validar Approach**
- Review de 3 ejemplos
- Verificar navegación Obsidian
- Documentar learnings
- **Timing:** 1 hora

#### Criterios de Éxito

✅ **3 Issues Creados:**
- REQ-001-template-system
- CONCEPT-001-autopoiesis
- LIT-001-hevner-dsr

✅ **3 Workbooks Escritos:**
- Cada uno ≤300 líneas
- Referencias bidireccionales funcionan
- Sintaxis Markdown correcta

✅ **3 Índices Actualizados:**
- requirements.md (ÍNDICE)
- concepts-index.md (nuevo)
- literature-index.md (nuevo)

✅ **Validación Obsidian:**
- Graph view muestra 3 nodos conectados
- Backlinks funcionan
- Tags (`#template-system`, `#autopoiesis`, `#dsr`) funcionan

#### Decisión Post-Sprint

**Si Validación Exitosa:**
→ Continuar con Sprint 1 (REQ-002 a REQ-005)

**Si Validación Falla:**
→ Revertir a approach monolítico
→ Actualizar INDICE para reflejar decisión
→ Documentar razones del fracaso

---

### Sprint 1: Requirements Phase (1 semana)

#### Objetivo
Completar Main Spec Requirements.md y crear REQ-002 a REQ-005

#### Tareas

**Parte A: Main Spec (CON Approval) - 2 días**

✅ **Tarea 1.1: Actualizar requirements.md a ÍNDICE**
- Convertir a hub note (200 líneas)
- Tabla de 15 requerimientos
- Métricas de progreso
- **Timing:** 2 horas
- **Tool:** `replace_string_in_file`

✅ **Tarea 1.2: Solicitar Approval del Main Spec**
- **Tool:** `mcp_spec-workflow2_spec-workflow-guide()`
- **Tool:** `mcp_spec-workflow2_approvals(action: request)`
- Poll status hasta approved
- **Tool:** `mcp_spec-workflow2_approvals(action: delete)`
- **Timing:** 1-2 días (espera approval)

**Parte B: Sub-Issues (SIN Approval) - 3 días**

✅ **Tarea 1.3: Crear REQ-002 Pattern Registry**
- ISSUE.yaml + workbook (150 líneas)
- Update requirements.md
- **Timing:** 1 hora
- **Tools:** `create_file` × 2, `replace_string_in_file`

✅ **Tarea 1.4: Crear REQ-003 Confidence Scores**
- ISSUE.yaml + workbook (160 líneas)
- Update requirements.md
- **Timing:** 1 hora
- **Tools:** `create_file` × 2, `replace_string_in_file`

✅ **Tarea 1.5: Crear REQ-004 Triple Persistence**
- ISSUE.yaml + workbook (170 líneas)
- Update requirements.md
- **Timing:** 1.5 horas
- **Tools:** `create_file` × 2, `replace_string_in_file`

✅ **Tarea 1.6: Crear REQ-005 Template Versioning**
- ISSUE.yaml + workbook (140 líneas)
- Update requirements.md
- **Timing:** 1 hora
- **Tools:** `create_file` × 2, `replace_string_in_file`

#### Criterios de Éxito

✅ **Main Spec Approved:**
- requirements.md (ÍNDICE) approved
- Approval deleted successfully

✅ **5 Sub-Issues Creados:**
- REQ-001 (Sprint 0) + REQ-002 a REQ-005
- Cada uno con ISSUE.yaml + workbook

✅ **Índice Actualizado:**
- Tabla muestra 5/15 requerimientos
- Estado: 1 completado, 4 en progreso

---

## 📝 CONCLUSIONES

### Estado Actual del Proyecto

**✅ LO BUENO:**
- Investigación bien fundamentada en manifiesto
- Principios correctos identificados
- Intención de modularidad es acertada
- Documentación exhaustiva (INDICE, README)

**❌ LO MALO:**
- Gap entre documentación y realidad
- Approach atómico propuesto pero no implementado
- Confusión sobre workflows (Main Spec vs Sub-Issues)
- Templates no existen físicamente

**🎯 LO URGENTE:**
- Crear primeros 3 ejemplos (Sprint 0)
- Validar approach atómico
- Actualizar INDICE a realidad
- Definir roadmap ejecutable

### Mensaje Clave para el Equipo

> **"El manifiesto es correcto. La intención es correcta.
> Pero el folder se creó sin ejecutar lo propuesto.
> Ahora hay que IMPLEMENTAR lo que se documentó."**

**Pasos Concretos:**

1. **DECIDIR:** ¿Implementar approach atómico? (Recomendado: SÍ)
2. **VALIDAR:** Sprint 0 (3 días) con 3 ejemplos
3. **EJECUTAR:** Sprint 1 (1 semana) con REQ-002 a REQ-005
4. **ITERAR:** Continuar hasta 157 issues completados

### Filosofía para Avanzar

**Principio DAATH-ZEN aplicado:**

> "Mejor esperar y hacer bien, que inventar y refactorizar."

**Aplicado a este proyecto:**

- ✅ ESPERAR: Completar Sprint 0 antes de continuar
- ✅ HACER BIEN: Cada issue autocontenido, ≤300 líneas
- ❌ INVENTAR: No asumir que algo existe si no se ve
- ❌ REFACTORIZAR: No crear monolitos que luego hay que dividir

---

**Versión:** 1.0.0
**Fecha:** 2026-01-10
**Próxima Revisión:** Post-Sprint 0 (2026-01-13)
**Mantenedor:** MELQUISEDEC (AI Research Architect)
