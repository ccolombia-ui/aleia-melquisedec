# Documento de Consolidación: spec-workflow-mcp + DAATH-ZEN

> **Fecha**: 2025-01-09
> **Propósito**: Consolidar la adopción de spec-workflow-mcp con el trabajo previo de DAATH-ZEN
> **Estado**: En progreso - Pendiente revisión de investigaciones previas

---

## 1. Resumen Ejecutivo

### 1.1 Situación Actual
El proyecto `aleia-melquisedec` está adoptando el framework `spec-workflow-mcp` para estructurar el desarrollo basado en especificaciones. Sin embargo, existe trabajo previo significativo en `aleia-bereshit` que debe integrarse.

### 1.2 Problema Identificado
El archivo `archive/tasks.md` (1551 líneas) fue archivado correctamente porque:
- ❌ Mezclaba requirements + design + tasks (violación de separation of concerns)
- ❌ No soportaba configuración para 3 tipos de producto
- ❌ No usaba artifact-templates como microprompts
- ❌ Contenía código inline en lugar de referencias

### 1.3 Dirección Propuesta
Adoptar spec-workflow-mcp completamente, integrando:
- **Steering docs** globales (product, tech, structure)
- **Spec docs** por feature (requirements, design, tasks)
- **Artifact templates** como microprompts configurables
- **Spec-types** para configuración por tipo de producto

---

## 2. Análisis de spec-workflow-mcp

### 2.1 Estructura Oficial
```
.spec-workflow/
├── steering/              # Documentos directivos GLOBALES
│   ├── product.md         # Visión del producto
│   ├── tech.md            # Stack tecnológico
│   └── structure.md       # Organización del proyecto
│
├── specs/                 # Especificaciones por feature
│   └── {spec-name}/
│       ├── requirements.md  # QUÉ construir (BLOCKING: approval)
│       ├── design.md        # CÓMO construirlo (BLOCKING: approval)
│       └── tasks.md         # TRACKING implementación (BLOCKING: approval)
│
├── approvals/             # Aprobaciones pendientes
└── archive/               # Specs completados/archivados
```

### 2.2 Workflow Secuencial (OBLIGATORIO)
```
1. requirements.md → APPROVAL REQUIRED
                    ↓
2. design.md       → APPROVAL REQUIRED
                    ↓
3. tasks.md        → APPROVAL REQUIRED
                    ↓
4. Implementation (task by task)
```

### 2.3 Contexto por Fase
| Fase | Contexto Requerido | Contexto Opcional |
|------|-------------------|-------------------|
| requirements | template:spec:requirements | steering:product, steering:tech |
| design | template:spec:design, spec:requirements | steering:tech, steering:structure |
| tasks | template:spec:tasks, spec:design | spec:requirements |
| implementation | spec:tasks | spec:requirements, spec:design |

---

## 3. Arquitectura Correcta: .spec-workflow por App

### 3.1 Principio Clave
> **Cada app/metodología es un PRODUCTO INDEPENDIENTE** con su propio `.spec-workflow/`.
> Los steering docs (product, tech, structure) son específicos de cada app, NO globales al monorepo.

### 3.2 Estructura del Monorepo
```
aleia-melquisedec/                    # MONOREPO
├── .spec-workflow/                   # Specs del MONOREPO (infraestructura, docs globales)
│   ├── steering/
│   │   ├── product.md               # Visión del monorepo
│   │   ├── tech.md                  # Stack compartido
│   │   └── structure.md             # Organización del monorepo
│   └── specs/
│       └── {monorepo-level-specs}/
│
├── apps/
│   ├── research-keter-migration/
│   │   └── .spec-workflow/          # Specs de ESTE producto
│   │       ├── steering/
│   │       │   ├── product.md       # Visión de Keter Migration
│   │       │   ├── tech.md          # Stack de Keter Migration
│   │       │   └── structure.md     # Estructura de Keter Migration
│   │       └── specs/
│   │
│   ├── research-neo4j-llamaindex/
│   │   └── .spec-workflow/          # Specs de ESTE producto
│   │       ├── steering/
│   │       │   ├── product.md       # Visión de Neo4j-LlamaIndex
│   │       │   ├── tech.md          # Stack específico
│   │       │   └── structure.md
│   │       └── specs/
│   │
│   └── {nueva-metodologia}/
│       └── .spec-workflow/          # Specs de ESTE producto
│           ├── steering/
│           │   ├── product.md       # Visión específica
│           │   ├── tech.md          # Stack específico
│           │   └── structure.md     # Estructura específica
│           ├── spec-types/          # Tipos de spec para ESTA metodología
│           ├── artifact-templates/  # Templates para ESTA metodología
│           └── specs/
│
├── packages/                        # Shared packages
│   └── daath-toolkit/
│       └── .spec-workflow/          # Specs del toolkit
│
└── docs/                            # Documentación global
```

### 3.3 Estructura Interna de Cada App
```
apps/{app-name}/
└── .spec-workflow/
    ├── steering/                    # Steering docs de ESTA app
    │   ├── product.md               # Visión del producto
    │   ├── tech.md                  # Stack tecnológico
    │   └── structure.md             # Organización interna
    │
    ├── spec-types/                  # Configuración por tipo de spec
    │   ├── investigacion-metodologia.yaml
    │   ├── investigacion-app.yaml
    │   └── investigacion-proyecto-social.yaml
    │
    ├── artifact-templates/          # Microprompts
    │   ├── README.md
    │   ├── daath-zen-concepto-tpl.md
    │   ├── daath-zen-workbook-tpl.md
    │   ├── daath-zen-dataset-tpl.md
    │   └── shared/
    │       ├── document-section-tpl.md
    │       ├── yaml-ld-node-tpl.md
    │       └── cypher-node-tpl.md
    │
    ├── task-patterns/               # Patrones reutilizables
    │   ├── analyze-existing-pattern.md
    │   ├── generate-outputs-pattern.md
    │   └── validate-coherence-pattern.md
    │
    ├── specs/                       # Specs del producto
    │   └── {spec-name}/
    │       ├── requirements.md
    │       ├── design.md
    │       └── tasks.md
    │
    └── archive/                     # Specs completados
```

### 3.2 Relación entre Componentes
```
                    ┌─────────────────────┐
                    │   STEERING DOCS     │
                    │  (product/tech/     │
                    │   structure)        │
                    └─────────┬───────────┘
                              │ references
                              ▼
┌─────────────────────────────────────────────────────┐
│                    SPEC TYPE CONFIG                  │
│  (investigacion-metodologia.yaml)                   │
│  - artifact_types: [concepto, workbook, dataset]    │
│  - required_outputs: [md, yaml-ld, cypher]          │
│  - rostros: [MELQUISEDEC, HYPATIA, SALOMON...]     │
└─────────────────────────┬───────────────────────────┘
                          │ configures
                          ▼
┌─────────────────────────────────────────────────────┐
│                 SPEC DOCUMENTS                       │
│  specs/{spec-name}/                                 │
│  ├── requirements.md → refs spec-type config       │
│  ├── design.md       → refs artifact-templates     │
│  └── tasks.md        → refs task-patterns          │
└─────────────────────────┬───────────────────────────┘
                          │ uses
                          ▼
┌─────────────────────────────────────────────────────┐
│              ARTIFACT TEMPLATES                      │
│  (microprompts)                                     │
│  - Input: config + contenido                        │
│  - Output: folder + document.md + yaml-ld + cypher │
└─────────────────────────────────────────────────────┘
```

---

## 4. Mapping: archive/tasks.md → Nueva Estructura

### 4.1 Contenido que va a requirements.md
- User stories
- Requisitos funcionales (REQ-1, REQ-2...)
- Criterios de aceptación
- Requisitos no funcionales

### 4.2 Contenido que va a design.md
- Decisiones de arquitectura (ADRs)
- Schema de Neo4j
- Estructura de outputs
- Referencias a guías y templates
- Patrones de validación

### 4.3 Contenido que va a tasks.md
- Lista de tareas con status
- Referencias a requirements (REQ-X)
- Referencias a design (design.md#section)
- Files afectados

### 4.4 Contenido que va a artifact-templates/
- Microprompts para generar artefactos
- Templates de documentos
- Templates de Cypher
- Templates de YAML-LD

### 4.5 Contenido que va a task-patterns/
- Patrones reutilizables de tareas
- Secuencias comunes de trabajo

---

## 5. Investigaciones Previas (aleia-bereshit)

> **NOTA**: Los archivos están fuera del workspace actual.
> Pendiente revisión de:

### 5.1 Archivos a Revisar
| Archivo | Propósito Esperado | Integración |
|---------|-------------------|-------------|
| `R003_METODOLOGIA_DATA_DRIVEN_AUTOGESTIVA.md` | Metodología base | Extraer para steering/product.md |
| `templates/` | Templates existentes | Migrar a artifact-templates/ |
| `_daath/ai-working/prompts/` | Prompts de IA | Convertir a microprompts |
| `0-inbox/daath-zen.md` | Definición DAATH-ZEN | Extraer para requirements.md |
| `_daath/CONTEXTO_ESTRUCTURA_CANONICA_V3.md` | Estructura canónica | Usar para structure.md |

### 5.2 Preguntas para Revisión
1. ¿Qué templates existentes pueden convertirse en artifact-templates?
2. ¿Qué prompts de IA pueden ser microprompts?
3. ¿Hay ADRs implícitos que debamos documentar?
4. ¿Qué validadores existen que podemos reutilizar?

---

## 6. Plan de Migración

### Fase 1: Estructura Base
- [ ] Crear steering docs (product.md, tech.md, structure.md)
- [ ] Crear spec-types/ con configuración por tipo de producto
- [ ] Crear artifact-templates/ con README

### Fase 2: Primer Spec Piloto
- [ ] Elegir un spec piloto (ej: daath-zen-concepto)
- [ ] Crear requirements.md minimalista
- [ ] Crear design.md con ADRs y referencias
- [ ] Crear tasks.md minimalista con referencias

### Fase 3: Integración de Trabajo Previo
- [ ] Revisar archivos de aleia-bereshit
- [ ] Extraer contenido relevante
- [ ] Crear artifact-templates basados en prompts existentes
- [ ] Documentar ADRs implícitos

### Fase 4: Validación y Tooling
- [ ] Crear validators para los 3 tipos de output
- [ ] Implementar propagación de cambios en templates
- [ ] Integrar con spec-workflow-mcp dashboard

---

## 7. Respuestas a Preguntas del Usuario

### 7.1 ¿Pueden los steering docs ser específicos por app/metodología?
**SÍ**. Cada `apps/{app-name}/` tiene su propio `.spec-workflow/` con sus steering docs.

```
apps/research-keter-migration/.spec-workflow/steering/product.md  # Específico de Keter
apps/research-neo4j-llamaindex/.spec-workflow/steering/product.md # Específico de Neo4j
```

El monorepo root también puede tener `.spec-workflow/` para specs de infraestructura global.

### 7.2 ¿Dónde van los ADRs?
**En design.md** de cada spec. Los ADRs son decisiones de diseño específicas del feature.

### 7.3 ¿Cómo debe verse un tasks.md minimalista?
Ver [minimal-tasks-example.md](./examples/minimal-tasks-example.md)

### 7.4 ¿Cómo referenciar templates desde design.md?
Ver [design-with-adrs-example.md](./examples/design-with-adrs-example.md)

---

## 8. Conclusiones

### 8.1 Fortalezas del Enfoque
- ✅ Separación clara de concerns (requirements/design/tasks)
- ✅ Workflow secuencial con approvals
- ✅ Templates configurables por tipo de producto
- ✅ Trazabilidad completa (REQ → Task → Output)

### 8.2 Riesgos a Mitigar
- ⚠️ Curva de aprendizaje para el nuevo sistema
- ⚠️ Migración de contenido existente
- ⚠️ Integración con trabajo previo de aleia-bereshit

### 8.3 Próximos Pasos Inmediatos
1. **Revisar archivos de aleia-bereshit** (requiere acceso)
2. **Crear steering docs globales**
3. **Implementar primer spec piloto**
4. **Validar con el equipo**

---

## Anexo A: Corrección del Análisis Previo

El documento `deep-coherence-analysis-2026-01-09.md` contenía un error:
- **ERROR**: Recomendaba promover `archive/tasks.md` como template base
- **CORRECCIÓN**: El archivo fue archivado intencionalmente porque viola spec-workflow-mcp

El archivo mezclaba:
- Requisitos (debe ir en requirements.md)
- Diseño/ADRs (debe ir en design.md)
- Tareas (debe ir en tasks.md)
- Templates (debe ir en artifact-templates/)

La nueva arquitectura propuesta corrige esto separando responsabilidades.
