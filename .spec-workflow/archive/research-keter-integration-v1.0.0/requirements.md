# Research App Integration v1.0.0 - Requirements

## Overview

Este spec aborda una pregunta arquitectónica fundamental para el ecosistema DAATH-ZEN MELQUISEDEC: **¿Cómo gestionar aplicaciones de investigación (como keter) en relación al framework?**

El objetivo es establecer criterios claros, documentar decisiones arquitectónicas y crear guidelines reutilizables para evaluar si una app debe:

- Permanecer en repo separado (como aleia-bereshit)
- Convertirse en package interno (packages/)
- Evolucionar a herramienta standalone

**Caso de Estudio**: App `keter` en `C:\proyectos\aleia-bereshit\apps\keter`

---

## Context & Problem Statement

### Situación Actual

```
aleia-melquisedec/          (Framework: metodología + tooling)
├── packages/
│   ├── core-mcp/
│   └── daath-toolkit/
├── apps/
│   └── 00-template/        (Solo template?)
└── docs/

aleia-bereshit/             (Colección de investigaciones)
├── apps/
│   ├── keter/              ← SUJETO DE ANÁLISIS
│   └── ... otros?
```

### Preguntas Sin Responder

1. ¿Es keter candidato a convertirse en package?
2. ¿Debería vivir en melquisedec como un branch, estar en un repo solo o permanecer en bereshit?
3. ¿Qué criterios usamos para decidir esto?
4. ¿Cómo gestionamos specs multi-repo?
5. ¿Qué hace apps/ en melquisedec si no contiene apps reales?

### Consecuencias de No Decidir

- Crecimiento orgánico sin criterios → monorepo caótico
- Duplicación de código entre repos
- Falta de claridad sobre dónde contribuir
- Dificultad para gestionar dependencias

---

## User Stories

### US-1: Como arquitecto del sistema, quiero criterios claros para decidir dónde vive cada componente

**Para**: Mantener coherencia arquitectónica a medida que el ecosistema crece
**Criterios de Aceptación**:

- Existe ADR documentando estrategia multi-repo
- Existe decision tree: "¿Dónde poner este código?"
- Guidelines cubren: packages, apps, repos separados

### US-2: Como desarrollador de keter, quiero saber si debo convertirlo en package

**Para**: Hacerlo reutilizable o mantenerlo como investigación aislada
**Criterios de Aceptación**:

- Análisis de keter: estructura, madurez, dependencias
- Decisión documentada: package / app / tool
- Si es package: roadmap de conversión

### US-3: Como mantenedor de melquisedec, quiero clarificar el rol de apps/

**Para**: Evitar confusión sobre si se esperan investigaciones internas
**Criterios de Aceptación**:

- Decisión documentada: apps/ = examples/ o solo template
- Actualización de ARQUITECTURA_MONOREPO.md
- README.md de apps/ clarifica su propósito

### US-4: Como futuro creador de investigaciones, quiero un template de repo independiente

**Para**: Iniciar nuevos proyectos con estructura consistente
**Criterios de Aceptación**:

- Template repo structure documentado
- Incluye: pyproject.toml, .gitignore, README, PROPOSITO.md
- Integración con daath-toolkit clara

### US-5: Como usuario de spec-workflow, quiero gestionar specs que cruzan repos

**Para**: Aplicar metodología DAATH-ZEN en proyectos multi-repo
**Criterios de Aceptación**:

- Guidelines para specs multi-repo
- Ejemplo: spec en melquisedec, trabajo en bereshit
- Estrategia de tracking y sincronización

---

## Functional Requirements

### REQ-1: Análisis Detallado de Keter

**Descripción**: Estudiar la app keter para determinar su naturaleza y potencial

**Sub-requisitos**:

- REQ-1.1: Inspeccionar estructura de directorios
- REQ-1.2: Analizar dependencias (requirements.txt, imports)
- REQ-1.3: Evaluar cobertura de tests (si existe)
- REQ-1.4: Identificar funcionalidad core vs experimental
- REQ-1.5: Determinar nivel de madurez (prototipo / beta / estable)

**Validación**: Documento de análisis completo en `analysis/keter-evaluation.md`

---

### REQ-2: ADR Multi-Repository Architecture

**Descripción**: Crear ADR-002 definiendo estrategia de arquitectura multi-repo

**Contenido Mínimo**:

```markdown
## Decision
- Framework (melquisedec) vs Apps (otros repos)
- Criterios para packages/ internos
- Estrategia de versionado multi-repo

## Rationale
- [Basado en análisis de pensamiento complejo]

## Consequences
- Pros / Cons / Mitigations
```

**Ubicación**: `docs/architecture/ADR-002-multi-repo-strategy.md`

**Validación**: ADR completo con 5 secciones estándar

---

### REQ-3: Decision Tree: "¿Dónde Vive Este Código?"

**Descripción**: Flowchart / checklist para evaluar componentes nuevos

**Criterios a Evaluar**:

```yaml
Propósito:
  - ¿Framework/tooling reutilizable? → packages/
  - ¿Investigación específica? → repo separado
  - ¿Ejemplo/demo? → apps/ (renombrado a examples/)

Dependencias:
  - ¿Solo depende de melquisedec? → puede ser interno
  - ¿Dependencias complejas propias? → repo separado

Versionado:
  - ¿Versiona con framework? → interno
  - ¿Ciclo independiente? → repo separado

Mantenimiento:
  - ¿Mismo equipo core? → puede ser interno
  - ¿Mantenedores diferentes? → repo separado

Madurez:
  - ¿Prototipo/experimental? → apps/ externo
  - ¿Estable/reutilizable? → considerar package
```

**Formato**: Diagrama mermaid + tabla de decisión

**Ubicación**: `docs/guides/component-placement-guidelines.md`

**Validación**: Aplicar tree a keter → resultado consistente con análisis

---

### REQ-4: Clarificación de apps/ en Melquisedec

**Descripción**: Decidir y documentar el rol de `apps/` en el framework

**Opciones**:

1. **Opción A**: Renombrar a `examples/`, solo contiene demos
2. **Opción B**: Mantener `apps/`, pero README claro: "solo templates y ejemplos"
3. **Opción C**: Eliminar completamente, mover 00-template/ a `packages/daath-toolkit/templates/`

**Deliverable**:

- Decisión documentada en ADR-002
- Actualización de ARQUITECTURA_MONOREPO.md
- README.md en apps/ explicando su propósito

**Validación**: No hay ambigüedad sobre si apps/ es para investigación real

---

### REQ-5: Template para Nuevos Repos de Investigación

**Descripción**: Crear template que repliquen estructura consistente para proyectos independientes

**Estructura**:

```
aleia-{nombre}/
├── README.md                    # Con badge de "DAATH-ZEN powered"
├── PROPOSITO.md                 # Manifiesto de la investigación
├── pyproject.toml              # Metadata del proyecto
├── .gitignore                  # Python standard + custom
├── apps/
│   └── {investigacion}/
│       ├── 0-inbox/
│       ├── 1-literature/
│       ├── 2-atomic/
│       ├── 3-workbook/
│       ├── 4-dataset/
│       ├── 5-outputs/
│       └── _daath/
├── packages/                   # Si genera paquetes reutilizables
│   └── {package-name}/
│       ├── pyproject.toml
│       ├── src/{package_name}/
│       └── tests/
└── tools/                      # Scripts específicos del proyecto
```

**Incluir**:

- Dependencies: `daath-toolkit` via pip
- Pre-commit config
- GitHub Actions template (tests, lint)

**Ubicación**: `docs/guides/new-research-repo-template.md`

**Validación**: Template aplicable a 3 casos de uso hipotéticos

---

### REQ-6: Guidelines para Specs Multi-Repo

**Descripción**: Documentar cómo gestionar specs que requieren trabajo en múltiples repos

**Escenarios**:

1. **Spec en melquisedec, trabajo en bereshit**:

   - Spec define estrategia
   - Logs de implementación pueden referenciar commits en otro repo
2. **Spec que crea nuevo repo**:

   - Spec documenta setup inicial
   - Repo nuevo incluye referencia al spec origin
3. **Cambios que afectan múltiples repos**:

   - Spec en repo principal
   - Sub-tasks para cada repo afectado

**Tracking**:

- Usar tags: `[MULTI-REPO: melquisedec, bereshit]`
- Logs incluyen: `Repository: aleia-bereshit | Commit: abc123`

**Ubicación**: `docs/guides/multi-repo-spec-workflow.md`

**Validación**: Este spec mismo debe seguir las guidelines

---

### REQ-7: Decisión sobre Keter

**Descripción**: Basado en análisis, decidir destino de keter

**Posibles Outcomes**:

**A. Mantener como App en Bereshit**

- Si: experimental, no reutilizable aún
- Acción: documentar y continuar desarrollo

**B. Convertir a Package**

- Si: código maduro, útil para otros proyectos
- Acción: crear roadmap de packaging (futuro spec)

**C. Promover a Repo Independiente**

- Si: proyecto grande, comunidad propia
- Acción: crear `aleia-keter` con template

**D. Integrar en Daath-Toolkit**

- Si: herramienta core del framework
- Acción: mover a `packages/daath-toolkit/keter/`

**Deliverable**: Documento de decisión + plan de acción

**Ubicación**: `analysis/keter-decision.md`

---

## Non-Functional Requirements

### NFR-1: Escalabilidad

- Guidelines deben aplicar a 10+ repos futuros sin modificación
- Decision tree debe cubrir 95% de casos sin ambigüedad

### NFR-2: Claridad

- Documentos legibles por contributor con 0 contexto previo
- Diagramas visuales para conceptos arquitectónicos

### NFR-3: Mantenibilidad

- ADRs y guidelines versionados (pueden evolucionar)
- Referencias cruzadas entre documentos actualizadas

### NFR-4: Consistencia con DAATH-ZEN

- Decisiones alineadas con filosofía modular
- Minimalismo: solo crear lo necesario
- Autopoiesis: permitir evolución orgánica pero guiada

---

## Success Criteria

### Criterio 1: Claridad Arquitectónica

- ✅ Cualquier dev puede decidir dónde poner código nuevo en <5min
- ✅ ADR-002 responde las 5 preguntas planteadas en "Problem Statement"

### Criterio 2: Aplicabilidad

- ✅ Decision tree aplicado a keter da resultado claro y consensuado
- ✅ Template usado para crear repo de prueba (puede ser mock)

### Criterio 3: Documentación

- ✅ 4 documentos nuevos: ADR, guidelines (x2), template
- ✅ 1 análisis: keter evaluation
- ✅ 1 decisión: keter future path

### Criterio 4: Meta-Compliance

- ✅ Este spec sigue sus propias guidelines para multi-repo

---

## Out of Scope (v1.0.0)

### No incluido en este spec:

- ❌ Implementación real de conversión de keter (si procede)
- ❌ Migración de código entre repos
- ❌ Configuración de CI/CD multi-repo
- ❌ Sistema de monorepo tools (Nx, Turborepo, etc.)
- ❌ Análisis de otras apps en bereshit (solo keter)

**Rationale**: Este spec es ESTRATÉGICO (define qué hacer), no TÁCTICO (cómo hacerlo). La implementación puede ser spec separado v1.1.0 o v2.0.0.

---

## Dependencies

### Prerequisitos:

- ✅ Acceso a `C:\proyectos\aleia-bereshit\apps\keter` (o info del usuario)
- ✅ ARQUITECTURA_MONOREPO.md actual entendido
- ✅ Filosofía DAATH-ZEN internalizada

### Bloqueantes:

- ⚠️ Si keter no existe o está vacío → spec reduce scope a guidelines genéricos
- ⚠️ Si bereshit tiene estructura diferente → adaptar análisis

---

## Priority & Phasing

### Phase 1: Discovery (High Priority)

- REQ-1: Análisis de keter
- REQ-3: Decision tree

### Phase 2: Documentation (High Priority)

- REQ-2: ADR-002
- REQ-4: Clarificación apps/

### Phase 3: Templates (Medium Priority)

- REQ-5: Template repo
- REQ-6: Multi-repo guidelines

### Phase 4: Decision (High Priority)

- REQ-7: Decisión sobre keter

**Rationale del Orden**:

- Primero entender (análisis)
- Luego documentar criterios generales
- Finalmente decidir caso específico
