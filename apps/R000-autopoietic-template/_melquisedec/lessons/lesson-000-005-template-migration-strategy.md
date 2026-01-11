# LESSON-000-005: Estrategia de Migración de Templates de Investigación

**spec:issue**: SPEC-000
**spec:owner**: GitHub Copilot
**Fecha**: 2026-01-11
**Contexto**: Gap Resolution - Task-000-004 Ontology Workbook
**Tipo**: Análisis de Contradicción + Estrategia de Migración

---

## Resumen Ejecutivo

Durante la ejecución de GAP-2 (crear template enriquecido) se creó un nuevo template `methodology-workbook` **sin analizar primero** el template existente `academic-research-template`. Esto generó:

❌ **Fragmentación de estándares**: Dos templates con estructuras diferentes
❌ **Pérdida de validaciones**: El template existente tiene validadores probados
❌ **Duplicación de esfuerzos**: Documentar lo mismo en dos formatos
❌ **Confusión metodológica**: ¿Cuándo usar cada template?

Esta lección documenta el **análisis comparativo** y propone una **estrategia de migración inteligente** que:

✅ **Preserve** el academic-research-template existente
✅ **Enriquezca** con mejores prácticas del baseline validado
✅ **Documente** diferencias y casos de uso
✅ **Unifique** estándares en un solo template mejorado

---

## Análisis Comparativo

### Template 1: academic-research-template (EXISTENTE)

**Ubicación**: `00-define/_templates/academic-research-template/`

**Estructura** (5 carpetas):
```
1-literature/    → Colección de fuentes (papers, libros, frameworks)
2-analysis/      → Análisis crítico de temas y patrones
3-atomics/       → Extracción de conceptos atómicos
4-artifacts/     → Síntesis e outputs intermedios
6-outputs/       → Entregables finales (literature reviews)
```

**Fortalezas**:
- ✅ **Probado y validado** en workbooks existentes
- ✅ **Herramientas de validación** (`validate-academic-research.py`, `validate-metadata.py`)
- ✅ **Protocolo de agentes** documentado (HYPATIA → SALOMON → MORPHEUS → ALMA)
- ✅ **Metadatos Dublin Core** + extensiones spec:
- ✅ **Nomenclatura clara** de atómicos (`atomic-XXX-{title}.md`)
- ✅ **Workflow de 8 días** establecido

**Debilidades**:
- ❌ **No documenta prompts iniciales** (falta carpeta 0-prompts/)
- ❌ **No formaliza pasos metodológicos** (falta carpeta 3-steps/)
- ❌ **No incluye diagramas visuales** (falta carpeta 4-canvas/)
- ❌ **No genera SPECIFICATION.yaml** (solo markdown en 6-outputs/)
- ❌ **No documenta conexiones conceptuales** (falta carpeta 5-analysis-connection/)

**Uso actual**: DDD workbook, IMRAD workbooks (tasks 5-10 en spec-000)

---

### Template 2: methodology-workbook (NUEVO - CREADO EN GAP-2)

**Ubicación**: `.spec-workflow/_meta/templates/research-methodology-template/methodology-workbook/`

**Estructura** (7 carpetas + tasks):
```
0-prompts/              → Contexto inicial, preguntas de investigación, alcance
1-sources/              → Colección de fuentes (equivalente a 1-literature/)
2-extracts/             → Extracción atómica (equivalente a 3-atomics/)
3-steps/                → Pasos metodológicos formalizados (NUEVO)
4-canvas/               → Diagramas Mermaid, workflows visuales (NUEVO)
5-analysis-connection/  → Puentes conceptuales entre metodologías (NUEVO)
6-outputs/              → SPECIFICATION.yaml + ROADMAP.md + PROGRESS.md (ENRIQUECIDO)
tasks/                  → Tareas atómicas DAATH-ZEN (NUEVO)
```

**Fortalezas**:
- ✅ **Carpeta 0-prompts/** documenta contexto de investigación
- ✅ **Carpeta 3-steps/** formaliza metodología paso a paso
- ✅ **Carpeta 4-canvas/** incluye diagramas Mermaid
- ✅ **Carpeta 5-analysis-connection/** mapea conceptos entre metodologías
- ✅ **SPECIFICATION.yaml template** (400-600 líneas) en 6-outputs/
- ✅ **Carpeta tasks/** con formato DAATH-ZEN (Rostro, MCPs, Lesson)
- ✅ **1,746 líneas de documentación** en 9 READMEs

**Debilidades**:
- ❌ **No tiene validadores** (validate-academic-research.py no funciona con esta estructura)
- ❌ **No está probado** en workbooks reales (solo creado, no usado)
- ❌ **Fragmenta el estándar** existente sin justificación clara
- ❌ **Pierde nomenclatura** de atómicos validada (atomic-XXX vs. extracts)
- ❌ **No documenta agentes** (HYPATIA, SALOMON, MORPHEUS, ALMA)

**Uso actual**: Ninguno (creado pero no usado)

---

### Baseline Validado: 01-onotology-eng-meth

**Ubicación**: `inputs/baseline/methologies/01-onotology-eng-meth/`

**Estructura** (7+ carpetas + archivos raíz):
```
0-prompts/                       → Contexto y preguntas
1-sources/                       → Fuentes bibliográficas
2-extracts/                      → Conceptos extraídos
3-steps/                         → Pasos metodológicos
3-work-flow/                     → Workflow diagrams (duplica 3-steps?)
4-canvas/                        → Diagramas visuales
5-aleia-integration/             → Integración con ALEIA (¿sistema?)
6-outputs/                       → Outputs finales
tasks/                           → Tareas atómicas
RES_C.2.1_SPECIFICATION.yaml     → Especificación completa (512 líneas)
ROADMAP.md                       → Hoja de ruta
RES_C.2.1_PROGRESS.md            → Registro de progreso
CHECKPOINT_B1_VALIDATION.md      → Validaciones
CHECKPOINT_B2_VALIDATION.md      → Validaciones
GUIA_CONTEXTO_EFICIENTE.md       → Guía de uso
MCP_MEMORY_NODES.md              → Nodos MCP
```

**Fortalezas**:
- ✅ **Estructura completa** con todos los artefactos necesarios
- ✅ **Especificación YAML exhaustiva** (512 líneas con metadatos, conceptos, pasos, restricciones)
- ✅ **Checkpoints de validación** documentados
- ✅ **Guías de contexto** para reutilización
- ✅ **MCP nodes documentados** para memory

**Debilidades**:
- ❌ **Estructura variable** (3-steps/ + 3-work-flow/ duplican función)
- ❌ **No es un template** sino un workbook completo (con contenido específico)
- ❌ **No documenta protocolo de agentes** (HYPATIA, SALOMON, etc.)
- ❌ **Carpeta 5-aleia-integration/** no es semánticamente clara

---

## Problemas Identificados

### Problema 1: Fragmentación de Estándares

**Impacto**: 🔴 CRÍTICO

Ahora tenemos:
- Template existente (5 carpetas) usado en workbooks actuales
- Template nuevo (7 carpetas) no usado pero creado
- Baseline validado (7+ carpetas) como referencia

**Riesgo**: Futuros workbooks no sabrán qué template usar, generando inconsistencia.

### Problema 2: Pérdida de Validaciones

**Impacto**: 🔴 CRÍTICO

El template existente tiene:
```bash
python tools/validation/validate-academic-research.py workbooks/wb-topic/
python tools/validation/validate-metadata.py workbooks/wb-topic/README.md
```

El template nuevo **no tiene validadores compatibles**. Crear validadores nuevos duplica esfuerzos.

### Problema 3: Inconsistencia en Nomenclatura

**Impacto**: 🟡 ALTO

- Template existente: `3-atomics/atomic-001-bounded-context.md`
- Template nuevo: `2-extracts/atomic-001-class.md`
- Baseline validado: `2-extracts/concept-C1-ontology.md`

¿Qué convención seguimos?

### Problema 4: Duplicación de Carpetas

**Impacto**: 🟢 MEDIO

Baseline tiene `3-steps/` + `3-work-flow/`. ¿Son necesarias ambas?

---

## Estrategia de Migración (PROPUESTA)

### Opción A: Enriquecer Template Existente (RECOMENDADA ✅)

**Filosofía**: Partir del template existente probado y agregar carpetas faltantes del baseline validado.

**Estructura propuesta** (7 carpetas + tasks):
```
academic-research-template-v2/
├── README.md (actualizado con nuevas carpetas)
├── 0-prompts/               → AGREGAR (del nuevo template)
├── 1-literature/            → MANTENER (renombrar a 1-sources para consistencia?)
├── 2-analysis/              → MANTENER
├── 3-atomics/               → MANTENER (nomenclatura validada)
├── 3-steps/                 → AGREGAR (pasos metodológicos del baseline)
├── 4-canvas/                → AGREGAR (diagramas Mermaid del nuevo template)
├── 5-analysis-connection/   → AGREGAR (puentes conceptuales del nuevo template)
├── 6-outputs/               → ENRIQUECER (agregar SPECIFICATION.yaml template)
└── tasks/                   → AGREGAR (formato DAATH-ZEN del nuevo template)
```

**Ventajas**:
- ✅ Preserva validadores existentes (ajustándolos para nuevas carpetas)
- ✅ Mantiene nomenclatura validada (`atomic-XXX-{title}.md`)
- ✅ Compatible con workbooks existentes (DDD, IMRAD)
- ✅ Enriquece con mejores prácticas del baseline
- ✅ Una sola fuente de verdad (no fragmentación)

**Desventajas**:
- ⚠️ Requiere actualizar validadores para nuevas carpetas
- ⚠️ Migrar workbooks existentes (agregar carpetas faltantes)

---

### Opción B: Fusionar Templates (ALTERNATIVA)

**Filosofía**: Crear template híbrido que tome lo mejor de cada uno.

**Ventajas**:
- ✅ Oportunidad de rediseñar desde cero
- ✅ Nomenclatura consistente desde el inicio

**Desventajas**:
- ❌ Rompe compatibilidad con workbooks existentes
- ❌ Requiere reescribir validadores completamente
- ❌ Migración masiva de todos los workbooks

**Veredicto**: ❌ **NO RECOMENDADA** (demasiado disruptivo)

---

### Opción C: Templates Especializados (ALTERNATIVA)

**Filosofía**: Mantener ambos templates para diferentes casos de uso.

**Casos de uso**:
- `academic-research-template`: Para literatura reviews tradicionales (DDD, IMRAD)
- `methodology-workbook`: Para metodologías formales (Ontology, RBM, BSC)

**Ventajas**:
- ✅ No rompe nada existente
- ✅ Cada template optimizado para su propósito

**Desventajas**:
- ❌ Fragmentación de estándares continúa
- ❌ Confusión sobre cuándo usar cada uno
- ❌ Duplicación de documentación (2 READMEs, 2 sets de validadores)

**Veredicto**: ⚠️ **POSIBLE PERO SUBÓPTIMA** (mantiene fragmentación)

---

## Decisión Recomendada: OPCIÓN A

### Plan de Migración en 4 Fases

#### Fase 1: Análisis y Documentación (1 hora) ✅ EN PROGRESO
- [x] Crear este documento (LESSON-000-005)
- [ ] Revisar con usuario (confirmar estrategia)
- [ ] Documentar mappings de carpetas

#### Fase 2: Enriquecer Template Existente (3 horas)
- [ ] Crear `academic-research-template-v2/` basado en v1
- [ ] Agregar carpetas faltantes:
  - [ ] `0-prompts/` (con README detallado)
  - [ ] `3-steps/` (con template de paso metodológico)
  - [ ] `4-canvas/` (con README de diagramas Mermaid)
  - [ ] `5-analysis-connection/` (con README de puentes conceptuales)
  - [ ] `tasks/` (con README formato DAATH-ZEN)
- [ ] Enriquecer `6-outputs/README.md`:
  - [ ] Agregar template SPECIFICATION.yaml (400-600 líneas)
  - [ ] Agregar templates ROADMAP.md, PROGRESS.md
- [ ] Actualizar README.md principal con nuevas carpetas
- [ ] Documentar protocolo de agentes actualizado

#### Fase 3: Actualizar Validadores (2 horas)
- [ ] Modificar `validate-academic-research.py`:
  - [ ] Aceptar carpetas opcionales (0-prompts, 3-steps, 4-canvas, 5-analysis-connection, tasks)
  - [ ] Validar estructura SPECIFICATION.yaml si existe
  - [ ] Mantener validación de atomics en `3-atomics/`
- [ ] Crear tests de validación para nuevas carpetas
- [ ] Actualizar documentación de validadores

#### Fase 4: Migrar Workbook de Ontología (1 hora)
- [ ] Eliminar workbook actual (`wb-methodology-ontology-engineering/`)
- [ ] Copiar `academic-research-template-v2/` a `wb-ontology-engineering/`
- [ ] Migrar contenido creado (README.md, 0-prompts/) al nuevo template
- [ ] Continuar ejecución de Task-000-004 con template correcto

**Total estimado**: 7 horas

---

## Mappings de Carpetas

### De `methodology-workbook` → `academic-research-template-v2`

| Nuevo Template       | Template Existente V2 | Acción        |
|----------------------|-----------------------|---------------|
| 0-prompts/           | 0-prompts/            | AGREGAR       |
| 1-sources/           | 1-literature/         | MANTENER (¿renombrar?) |
| 2-extracts/          | 3-atomics/            | MANTENER (mejor nomenclatura) |
| 3-steps/             | 3-steps/              | AGREGAR       |
| 4-canvas/            | 4-canvas/             | AGREGAR       |
| 5-analysis-connection/ | 5-analysis-connection/ | AGREGAR     |
| 6-outputs/           | 6-outputs/            | ENRIQUECER    |
| tasks/               | tasks/                | AGREGAR       |

### ¿Renombrar 1-literature → 1-sources?

**Pros**:
- ✅ Consistencia con baseline validado
- ✅ "Sources" es más amplio (incluye standards, frameworks, no solo papers)

**Cons**:
- ❌ Rompe nomenclatura establecida
- ❌ Requiere actualizar validadores

**Decisión propuesta**: **MANTENER 1-literature/** por ahora, documentar alias en README.

---

## Nomenclatura de Atómicos (DECISIÓN CRÍTICA)

### Convenciones encontradas:

1. **academic-research-template**: `atomic-001-bounded-context.md` ✅
2. **methodology-workbook**: `atomic-{id}-{concepto}.md` ✅
3. **Baseline validado**: `concept-C1-ontology.md` ❌

**Decisión**: Mantener `atomic-XXX-{title}.md` (convención 1 y 2)

**Justificación**:
- Nomenclatura ya validada en herramientas
- "atomic" refleja granularidad (indivisible)
- Números con ceros a la izquierda (001, 002) facilitan ordenamiento

---

## Lecciones Aprendidas

### ❌ Error Cometido
**No analizar el template existente antes de crear uno nuevo**, asumiendo que no existía un estándar probado.

### ✅ Corrección Propuesta
**Partir siempre del existente, enriquecer en vez de reemplazar**, preservando validaciones y nomenclatura establecida.

### 🔑 Principio Clave
> **"Preservar y enriquecer, no reemplazar y fragmentar"**

Cuando encontramos estándares existentes:
1. **Analizar primero**: Leer template completo, validadores, workbooks que lo usan
2. **Comparar con baseline**: Identificar gaps (carpetas faltantes, documentación incompleta)
3. **Enriquecer inteligentemente**: Agregar carpetas/documentación faltante sin romper lo existente
4. **Validar migración**: Asegurar que workbooks existentes siguen funcionando
5. **Documentar cambios**: Crear LESSON como este para trazabilidad

---

## Próximos Pasos Inmediatos

### Decisión Requerida del Usuario

**¿Proceder con Opción A (Enriquecer Template Existente)?**

Si **SÍ**:
1. Implementar Fase 2 (crear academic-research-template-v2)
2. Implementar Fase 3 (actualizar validadores)
3. Implementar Fase 4 (migrar workbook ontología)
4. Continuar Task-000-004 con template unificado

Si **NO** (considerar Opción C):
1. Mantener ambos templates
2. Documentar casos de uso específicos
3. Continuar con workbook ontología usando methodology-workbook
4. Aceptar fragmentación como tradeoff

---

## Referencias

### Archivos Analizados
- `00-define/_templates/academic-research-template/README.md` (185 líneas)
- `.spec-workflow/_meta/templates/research-methodology-template/methodology-workbook/` (1,746 líneas en 9 READMEs)
- `inputs/baseline/methologies/01-onotology-eng-meth/RES_C.2.1_SPECIFICATION.yaml` (512 líneas)

### Commits Relacionados
- **3e36434**: Gap resolution (creó methodology-workbook)
- **084b129**: Baseline analysis (documentó metodologías validadas)

---

## Changelog

| Versión | Fecha      | Autor          | Cambios                                    |
|---------|------------|----------------|--------------------------------------------|
| 1.0.0   | 2026-01-11 | GitHub Copilot | Análisis inicial, propuesta Opción A      |

---

**Estado**: ⏳ PENDIENTE-DECISIÓN-USUARIO
**Impacto**: 🔴 CRÍTICO (bloquea continuación de Task-000-004)
**Decisión Requerida**: Confirmar Opción A (Enriquecer Template Existente) vs. Opción C (Templates Especializados)
