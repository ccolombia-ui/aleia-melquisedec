# App-Spec Template

> **Template ID**: `app-spec-template`
> **Version**: `1.0.0`
> **Type**: `app-spec`
> **Purpose**: Investigación formal → Especificación de aplicación trazable

---

## 🎯 Propósito

Este template guía la **especificación formal de aplicaciones** mediante investigación rigurosa. El resultado es una spec completamente trazable: cada decisión de diseño se fundamenta en literatura formal (ISO, frameworks, estándares).

**¿Qué problema resuelve?**

- Evitar specs "inventadas" sin fundamento
- Garantizar trazabilidad: `código → spec → concepto atómico → fuente formal`
- Parametrizar el tipo de arquitectura: HEX, HEX-WF, HEX-WF-MCP

---

## 📊 Flujo de Trabajo

```
┌─────────────────────────────────────────────────────────────────────┐
│                         APP-SPEC WORKFLOW                           │
│            De Investigación Formal a Especificación Trazable        │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ MELQUISEDEC │────▶│   HYPATIA   │────▶│   SALOMON   │────▶│  MORPHEUS   │
│  (Keter)    │     │   (Daath)   │     │  (Tiferet)  │     │   (Yesod)   │
│             │     │             │     │             │     │             │
│ Clasificar  │     │ Investigar  │     │ Especificar │     │ Implementar │
│ app_type    │     │ literatura  │     │ arquitectura│     │ código      │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │                   │
      ▼                   ▼                   ▼                   ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 0-inbox/    │     │01-literature│     │ 03-workbook │     │04-artifacts │
│ ISSUE.yaml  │     │02-atomics/  │     │ SPEC-*.md   │     │ código/     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                                  │
                                                                  ▼
                                                          ┌─────────────┐
                                                          │    ALMA     │
                                                          │  (Malkuth)  │
                                                          │             │
                                                          │ Instanciar  │
                                                          │ validar     │
                                                          └─────────────┘
                                                                  │
                                                                  ▼
                                                          ┌─────────────┐
                                                          │ 05-outputs/ │
                                                          │ package     │
                                                          └─────────────┘
```

---

## 🔧 Tipos de Aplicación (`app_type`)

El template se parametriza según el tipo de arquitectura:

| app_type | Descripción | SALOMON especifica | MORPHEUS implementa |
|----------|-------------|-------------------|---------------------|
| **HEX** | Hexagonal básico | Domain, Ports, Adapters | Entidades, interfaces, implementaciones |
| **HEX-WF** | Hex + Workflows | + Patterns, Procedures | + Scripts de workflow |
| **HEX-WF-MCP** | Hex + WF + MCP | + MCP Tools spec | + MCP Server |

### Diagrama de Decisión

```
                    ┌──────────────────┐
                    │ ¿Qué necesitas?  │
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│    HEX        │    │   HEX-WF      │    │  HEX-WF-MCP   │
│               │    │               │    │               │
│ App simple    │    │ App con       │    │ App con       │
│ sin workflows │    │ workflows     │    │ workflows +   │
│ complejos     │    │ complejos     │    │ MCP tools     │
│               │    │               │    │               │
│ Ej: Library   │    │ Ej: Pipeline  │    │ Ej: Agent     │
│     CRUD      │    │     ETL       │    │     Backend   │
└───────────────┘    └───────────────┘    └───────────────┘
```

---

## 📁 Estructura del Template

```
app-spec-template/
├── README.md                    ← Este archivo
├── config.yaml                  ← Configuración (app_type, scope, etc.)
├── requirements.md              ← QUÉ investigar y especificar
├── design.md                    ← CÓMO investigar y especificar
├── tasks.md                     ← Tareas por rostro
└── _meta/
    ├── orchestrator.md          ← Automatización
    └── templates/               ← Plantillas para specs
        ├── ISSUE.yaml.template
        ├── atomic-concept.md.template
        ├── SPEC-DOMAIN.md.template      ← Spec de domain (SALOMON)
        ├── SPEC-PORTS.md.template       ← Spec de ports (SALOMON)
        ├── SPEC-ADAPTERS.md.template    ← Spec de adapters (SALOMON)
        ├── SPEC-WORKFLOWS.md.template   ← Spec de workflows (HEX-WF+)
        └── SPEC-MCP.md.template         ← Spec de MCP tools (HEX-WF-MCP)
```

---

## 🔄 Rol de Cada Rostro

### 0. MELQUISEDEC (Orquestador)

**Pregunta**: "¿Qué tipo de app y qué flujo de conocimiento?"

- Recibe el request del usuario
- Clasifica `app_type`: HEX | HEX-WF | HEX-WF-MCP
- Crea ISSUE.yaml en `0-inbox/`
- Inicia cascada H → S → Mo → A

---

### 1. HYPATIA (Investigadora)

**Pregunta**: "¿Qué dice la literatura canónica?"

**Input**: ISSUE.yaml con `app_type` y dominio
**Output**: `01-literature/` + `02-atomics/`

**Tareas**:
1. Buscar fuentes formales (ISO, CMIS, frameworks, papers)
2. Documentar contenido relevante
3. Atomizar conceptos (Zettelkasten)
4. Mapear relaciones entre conceptos

**Ejemplo para keter (document management)**:
```yaml
01-literature/
├── standards/
│   ├── ISO-16175-3/          # Records management
│   └── CMIS-v1.1/            # Content Management
├── frameworks/
│   ├── hexagonal-architecture/
│   └── domain-driven-design/
└── sources.yaml

02-atomics/
├── CMIS-Document-Object.md   # Concepto: Document en CMIS
├── CMIS-Repository.md        # Concepto: Repository en CMIS
├── HEX-Port-Pattern.md       # Concepto: Port (interface)
└── relationships.yaml        # Relaciones entre conceptos
```

---

### 2. SALOMON (Arquitecto de Spec)

**Pregunta**: "¿Cómo se especifica esta app según la investigación?"

**Input**: `02-atomics/` (conceptos formales)
**Output**: `03-workbook/` (SPECS trazables)

**Tareas según `app_type`**:

#### HEX (básico):
- SPEC-DOMAIN.md: Entidades, value objects, aggregates
- SPEC-PORTS.md: Interfaces (inbound/outbound)
- SPEC-ADAPTERS.md: Implementaciones de ports

#### HEX-WF (+ workflows):
- Todo de HEX +
- SPEC-WORKFLOWS.md: Patterns, procedures

#### HEX-WF-MCP (+ MCP):
- Todo de HEX-WF +
- SPEC-MCP.md: MCP tools, server config

**Trazabilidad obligatoria**:
```markdown
# SPEC-DOMAIN.md

## DocumentEntity

### Trazabilidad
- **Atomic**: [CMIS-Document-Object](../02-atomics/CMIS-Document-Object.md)
- **Standard**: ISO 16175-3, CMIS v1.1
- **Literature**: [01-literature/standards/CMIS-v1.1/](../01-literature/standards/CMIS-v1.1/)

### Especificación
...
```

---

### 3. MORPHEUS (Implementador)

**Pregunta**: "¿Cómo se implementa esta spec?"

**Input**: `03-workbook/SPEC-*.md`
**Output**: `04-artifacts/` (código, tests, configs)

**Tareas**:
1. Generar código según specs de SALOMON
2. Crear tests (unit, integration)
3. Crear configuraciones (schemas, environments)
4. Validar que código traza a spec

**Estructura de output**:
```
04-artifacts/
├── src/
│   ├── domain/           # De SPEC-DOMAIN.md
│   │   ├── entities/
│   │   └── value_objects/
│   ├── ports/            # De SPEC-PORTS.md
│   │   ├── inbound/
│   │   └── outbound/
│   └── adapters/         # De SPEC-ADAPTERS.md
│       ├── repositories/
│       └── services/
├── tests/
│   ├── unit/
│   └── integration/
├── config/
│   ├── schemas/
│   └── environments/
└── README.md             # Cómo usar el código
```

---

### 4. ALMA (Instanciador)

**Pregunta**: "¿El código es coherente y funciona?"

**Input**: `04-artifacts/`
**Output**: `05-outputs/` (package publicable)

**Tareas**:
1. Validar coherencia (tests pasan, linting ok)
2. Crear package instalable
3. Generar documentación final
4. Validar trazabilidad completa
5. Publicar (tag, release)

---

## ✅ Checkpoints

| Checkpoint | Rostro | Criterio |
|------------|--------|----------|
| CK-01 | HYPATIA | ≥3 fuentes formales, ≥10 atomics con trazabilidad |
| CK-02 | SALOMON | Specs completas según app_type, 100% trazables |
| CK-03 | MORPHEUS | Código implementa spec, tests ≥80% coverage |
| CK-04 | ALMA | Package publicable, trazabilidad validada |

---

## 🚀 Cómo Usar Este Template

### 1. Copiar template
```bash
cp -r _templates/app-spec-template/ .spec-workflow/specs/mi-app-spec/
```

### 2. Configurar `config.yaml`
```yaml
research:
  name: "mi-app"
  full_name: "Mi Aplicación"
  app_type: "HEX-WF"  # HEX | HEX-WF | HEX-WF-MCP
  domain: "document-management"

scope:
  research_questions:
    - "¿Qué estándares aplican a este dominio?"
    - "¿Qué entidades del dominio existen?"
    - "¿Qué ports necesita la arquitectura?"
```

### 3. Ejecutar orquestador
```powershell
# Seguir _meta/orchestrator.md paso a paso
```

---

## 📚 Referencias

- [03-cinco-rostros.md](../../docs/manifiesto/01-fundamentos/03-cinco-rostros.md)
- [01-research-instance.md](../../docs/manifiesto/02-arquitectura/01-research-instance.md)
- [research-methodology-template](../.spec-workflow/specs/research-methodology-template/)

---

**Versión**: 1.0.0
**Última actualización**: 2026-01-09
