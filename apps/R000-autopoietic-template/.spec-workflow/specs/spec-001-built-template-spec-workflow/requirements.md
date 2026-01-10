# SPEC-001: Built Template spec-workflow - Requirements

## Metadatos

| Campo | Valor |
|-------|-------|
| **Spec ID** | SPEC-001 |
| **Nombre** | Built Template spec-workflow |
| **Versión** | 1.0.0 |
| **Fecha** | 2026-01-10 |
| **Estado** | Requirements (Pending Approval) |
| **Autor** | GitHub Copilot (Claude Sonnet 4.5) |
| **Propósito** | Crear sistema de templates daath-zen con integración RBM para specs autopoiéticos |

---

## Overview

Este spec implementa una **meta-especificación** que define cómo se estructurarán todas las specs futuras en el proyecto MELQUISEDEC. Es una **especificación de infraestructura lingüística** que crea el lenguaje y gramática para expresar especificaciones de investigación autopoiética.

### Problema Central

**Estado Actual** (Sin SPEC-001):
- Templates genéricos de spec-workflow-mcp sin adaptación a metodología RBM
- Contenido duplicado entre specs (historias de usuario, decisiones arquitectónicas)
- Sin trazabilidad causal entre requisitos y resultados (RBM)
- Sin mecanismo de evolución autopoiética de templates
- Sin interoperabilidad semántica (JSON-LD) para graph database

**Estado Objetivo** (Con SPEC-001):
- Sistema de templates daath-zen con herencia (base + 6 variantes)
- Workbooks RBM como fuente única de verdad (modular, reutilizable)
- Compilación automática: workbooks → specs monolíticos
- Protocolo keter-doc (JSON-LD) para persistencia triple (MD + Neo4j + Vector)
- Templates evolucionan mediante feedback autopoiético

### Insight Crítico

> **"No especificar features antes de especificar cómo especificar."**

SPEC-001 es arquitectura lingüística: define el vocabulario antes de escribir la historia.

---

## Principios MELQUISEDEC Aplicados

- **P1 (Síntesis Metodológica)**: Orquesta spec-workflow-mcp + RBM + Obsidian + Neo4j
- **P2 (Autopoiesis por Diseño)**: Templates mejoran mediante lecciones capturadas
- **P3 (Issue-Driven)**: Cada tarea de investigación es un issue rastreable
- **P5 (Checkpoints Incrementales)**: Validación en cada fase del workflow
- **P6 (Persistencia Triple)**: Markdown + Graph (Neo4j) + Vector embeddings
- **P7 (Recursión Fractal)**: Estructura RBM se repite en todos los niveles
- **P8 (Tzimtzum Metodológico)**: Templates limitan para enfocar
- **P9 (Inmutabilidad)**: Specs compilados son snapshots read-only

---

## User Stories

### US-001: Como investigador, quiero templates adaptados a RBM
**Para que** mis specs tengan trazabilidad causal (Resultado Final → RI → Rinm → REQ)

**Criterios de Aceptación**:
- [ ] Template daath-zen-requirements incluye sección de Matriz de Coherencia RBM
- [ ] Template referencia workbooks, no contenido inline duplicado
- [ ] Compilación genera diagrama Mermaid de cadena causal
- [ ] Todos los REQ-XXX mapean a Resultados Inmediatos (Productos)

**Relacionado**: RI-002 (Template System)

---

### US-002: Como desarrollador, quiero workbooks modulares que se compilen a specs
**Para que** pueda reutilizar contenido entre specs sin duplicación

**Criterios de Aceptación**:
- [ ] Estructura de carpetas workbook refleja jerarquía RBM (rf/ri-XXX/rinm-XXX/)
- [ ] Script `compile_spec_from_workbook.py` procesa transclusions Obsidian `![[]]`
- [ ] Archivo compilado es read-only con advertencia en header
- [ ] Compilación toma < 5 segundos para workbook de 50 productos

**Relacionado**: RI-003 (Compilation Pipeline)

---

### US-003: Como arquitecto, quiero protocolo keter-doc para interoperabilidad semántica
**Para que** todos los documentos sean ingestables en Neo4j con relaciones explícitas

**Criterios de Aceptación**:
- [ ] Cada documento tiene metadata JSON-LD con @context, @type, @id
- [ ] Schema usa vocabularios estándar (Dublin Core, FOAF, Schema.org)
- [ ] Ontología MELQUISEDEC define términos custom (P1-P10, 5 Rostros)
- [ ] Validador keter-doc verifica schema antes de compilación

**Relacionado**: RI-001 (Base Infrastructure / Keter-Doc Protocol)

---

### US-004: Como investigador, quiero templates que hereden de base común
**Para que** cambios globales (header HKM, versión) se propaguen automáticamente

**Criterios de Aceptación**:
- [ ] `config.yaml-ld` define jerarquía de herencia (base → variantes)
- [ ] Template base contiene solo elementos universales (HKM header, Dublin Core, keter-doc)
- [ ] 6 templates variantes (requirements, design, tasks, product, tech, structure) extienden base
- [ ] Actualizar versión de base propaga a todas las variantes en < 1 minuto

**Relacionado**: RI-002 (Template System / Base Template)

---

### US-005: Como desarrollador, quiero validación automática de coherencia RBM
**Para que** detección de errores (REQ huérfanos, cadena rota) ocurra antes de aprobación

**Criterios de Aceptación**:
- [ ] Validador verifica: todos los REQ mapean a Rinm
- [ ] Validador verifica: todos los Rinm mapean a RI
- [ ] Validador verifica: todos los RI mapean a RF
- [ ] Validación falla con mensaje claro si hay breaks en cadena

**Relacionado**: RI-004 (Validation System)

---

### US-006: Como nuevo contribuidor, quiero guías y ejemplos de uso
**Para que** pueda crear mi primer workbook y spec en < 2 horas

**Criterios de Aceptación**:
- [ ] `template-usage-guide.md` explica paso a paso cómo usar templates
- [ ] `workbook-creation-guide.md` muestra estructura y convenciones
- [ ] Workbook de ejemplo `wb-rbm-example-auth` incluye 2 RI, 3 Rinm, 5 REQ
- [ ] README principal enlaza a todos los guides

**Relacionado**: RI-005 (Documentation & Examples)

---

## 🔬 Phase 1.5: Research Foundation User Stories

### US-007: Como arquitecto, quiero investigación IMRAD de artefactos spec-workflow-mcp
**Para que** comprenda formalmente QUÉ son los artefactos y CÓMO poblarlos desde dominio

**Criterios de Aceptación**:
- [ ] 7 workbooks IMRAD (01-introduction through 07-references) completados con 200+ líneas cada uno
- [ ] Preguntas de investigación respondidas con evidencia (código del dashboard, literatura DDD)
- [ ] Diagramas de bounded contexts usando notación DDD estándar
- [ ] Mapeo RBM → Artefactos con ejemplos concretos de SPEC-001
- [ ] Referencias bibliográficas formales (Evans, Vernon, ISO/IEC 21838)

**Relacionado**: RI-001.5 (Research Foundation)

---

### US-008: Como investigador, quiero modelo de dominio DDD de spec-workflow-mcp
**Para que** cada artefacto tenga bounded context identificado y entidades definidas

**Criterios de Aceptación**:
- [ ] Diagrama C4 Context level muestra bounded contexts (Spec Management, Design, Template)
- [ ] Cada bounded context lista Entities, Value Objects, Aggregates
- [ ] Matriz de mapeo: RBM Level × Artefacto × Bounded Context × Entity
- [ ] Modelo soporta generación automática de artefactos desde workbooks
- [ ] Archivo `_melquisedec/domain/models/rbm-artifacts-mapping.md` completo con ejemplos

**Relacionado**: RI-001.5 (Research Foundation / Domain Model)

---

### US-009: Como desarrollador, quiero workbook prototipo que compile a artefactos
**Para que** vea cómo investigación de dominio (IMRAD) se transforma en requirements.md, design.md, tasks.md

**Criterios de Aceptación**:
- [ ] Workbook prototipo para SPEC-001 en `_melquisedec/domain/workbooks/spec-001-prototype/`
- [ ] 8 archivos IMRAD (01-08.md) con estructura completa (Introduction → References)
- [ ] Script `compile.py` funcional que genera requirements.md, design.md, tasks.md
- [ ] Tests de compilador con 80%+ coverage
- [ ] Artefactos compilados pasan validación del dashboard spec-workflow-mcp
- [ ] TODO contenido en artefactos tiene fuente rastreable en workbook

**Relacionado**: RI-001.5 (Research Foundation / Workbook-to-Artifact Pipeline)

---

### US-010: Como investigador, quiero ontología formal ISO/IEC 21838 de spec-workflow
**Para que** conceptos estén definidos formalmente y validados con reasoner

**Criterios de Aceptación**:
- [ ] Ontología en OWL/Turtle alineada con BFO (Basic Formal Ontology)
- [ ] Clases definidas: Artifact, Requirement, DesignDecision, Task, BoundedContext
- [ ] Propiedades definidas: hasRequirement, satisfies, produces, maps_to_artifact
- [ ] Reasoner (HermiT o Pellet) valida consistencia sin contradicciones
- [ ] Queries SPARQL pueden extraer mapeo RBM → Artefactos
- [ ] Archivo `_melquisedec/domain/ontologies/spec-workflow-ontology.ttl` completo

**Relacionado**: RI-001.5 (Research Foundation / Formal Ontology)

---

### US-011: Como desarrollador, quiero templates con trazabilidad epistemológica
**Para que** cada claim en artefactos tenga fuente en workbook de dominio

**Criterios de Aceptación**:
- [ ] Templates incluyen sección "🔬 Knowledge Sources" referenciando workbooks
- [ ] Placeholders para workbook references funcionan ({{WORKBOOK_NAME}}, {{BOUNDED_CONTEXTS}})
- [ ] Validator detecta claims sin fuente y falla compilación
- [ ] Tests cubren escenarios de trazabilidad válida e inválida
- [ ] Documentación explica formato de citas a workbooks (path, line number)

**Relacionado**: RI-001.5 (Research Foundation / Traceable Templates)

---

## Functional Requirements

### REQ-001-01: Schema JSON-LD para Protocolo Keter-Doc

**Objetivo**: Definir schema JSON-LD 1.1 para metadata de documentos.

**Especificación**:

```yaml
# keter-doc-protocol-v1.0.0.jsonld
{
  "@context": {
    "@vocab": "http://melquisedec.org/ontology#",
    "dc": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "schema": "http://schema.org/",
    "melq": "http://melquisedec.org/ontology#"
  },
  "@type": "ResearchSpecification",
  "@id": "urn:melquisedec:spec:{spec-id}",
  "dc:title": "string",
  "dc:created": "ISO8601 datetime",
  "dc:creator": {
    "@type": "foaf:Agent",
    "foaf:name": "string"
  },
  "melq:implementsPrinciple": [
    { "@id": "urn:melquisedec:principle:P1" }
  ],
  "melq:hasIntermediateResult": [
    { "@id": "urn:melquisedec:spec:{spec-id}:ri:{ri-id}" }
  ]
}
```

**Criterios de Validación**:
- [ ] Schema valida contra especificación JSON-LD 1.1
- [ ] Incluye todos los 10 principios MELQUISEDEC (P1-P10)
- [ ] Soporta 5 Rostros (MELQUISEDEC, HYPATIA, SALOMON, MORPHEUS, ALMA)
- [ ] Grafo RDF genera sin errores usando herramienta `rdflib`
- [ ] Ingestión a Neo4j exitosa con script de prueba

**Priority**: 🔴 **ALTA** - Fundamento de interoperabilidad

**Resultado Intermedio**: RI-001 (Base Infrastructure)
**Resultado Inmediato**: Rinm-001 (Keter-Doc Protocol)

---

### REQ-001-02: Formato HKM Header

**Objetivo**: Estandarizar header Hermenéutica del Conocimiento MELQUISEDEC.

**Especificación**:

```yaml
---
# HKM Header v1.0.0
keter_protocol_version: "1.0.0"
document_type: "ResearchSpecification"
document_id: "urn:melquisedec:spec:001"
spec_name: "built-template-spec-workflow"
phase: "requirements"
version: "1.0.0"
created: "2026-01-10T12:50:24Z"
modified: "2026-01-10T15:30:00Z"
author: "GitHub Copilot (Claude Sonnet 4.5)"
rostro_primary: "MELQUISEDEC"  # Architect
status: "draft"
approval_required: true

# Principios Aplicados
principles:
  - P1: "Síntesis Metodológica"
  - P2: "Autopoiesis por Diseño"
  - P6: "Persistencia Triple"

# Metadata Dublin Core
dc_title: "Built Template spec-workflow"
dc_description: "Sistema de templates daath-zen con integración RBM"
dc_subject: ["meta-specification", "template-system", "RBM", "autopoiesis"]
dc_language: "es-MX"
dc_rights: "MIT License"

# Trazabilidad
parent_issue: "urn:melquisedec:issue:spec-001"
related_specs: []
dependencies: ["spec-workflow-mcp>=1.0.0", "obsidian>=1.5.0"]
---
```

**Criterios de Validación**:
- [ ] Parser YAML lee header sin errores
- [ ] Todos los campos obligatorios presentes
- [ ] Fechas en formato ISO8601
- [ ] URNs siguen patrón `urn:melquisedec:{type}:{id}`
- [ ] Rostro es uno de los 5 válidos

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-001 (Base Infrastructure)
**Resultado Inmediato**: Rinm-001 (Keter-Doc Protocol)

---

### REQ-001-03: Campos Dublin Core

**Objetivo**: Mapear todos los campos Dublin Core requeridos.

**Campos Obligatorios**:
- `dc:title` - Título del documento
- `dc:creator` - Autor (persona o agente)
- `dc:created` - Fecha de creación (ISO8601)
- `dc:subject` - Array de keywords
- `dc:description` - Resumen breve
- `dc:type` - Tipo de recurso (Text, Dataset, Software)
- `dc:format` - MIME type (text/markdown)
- `dc:language` - Código ISO 639-1 (es, en)

**Campos Opcionales**:
- `dc:contributor` - Contribuidores adicionales
- `dc:modified` - Última modificación
- `dc:rights` - Licencia
- `dc:relation` - URIs de documentos relacionados

**Criterios de Validación**:
- [ ] Template base incluye todos los campos obligatorios
- [ ] Validador verifica presencia de obligatorios
- [ ] Campos opcionales son realmente opcionales (no rompen compilación)
- [ ] Valores cumplen con spec Dublin Core ISO 15836

**Priority**: 🟡 **MEDIA**

**Resultado Intermedio**: RI-001 (Base Infrastructure)
**Resultado Inmediato**: Rinm-001 (Keter-Doc Protocol)

---

## 🔬 Phase 2: Research Foundation (NUEVA FASE)

> **Justificación**: Antes de diseñar templates, necesitamos comprender FORMALMENTE qué son los artefactos de spec-workflow-mcp, qué conceptos contienen, y cómo poblarlos desde conocimiento de dominio usando DDD, IMRAD e ISO/IEC 21838. Esta investigación fundamenta epistemológicamente la generación de artefactos.

---

### REQ-001-04: Investigación IMRAD de Artefactos spec-workflow-mcp

**Objetivo**: Realizar investigación formal usando estructura IMRAD (Introduction, Methods, Results, Analysis, Discussion) para comprender qué son los artefactos de spec-workflow-mcp (requirements.md, design.md, tasks.md, producto.md, tech.md, structure.md), qué conceptos de dominio contienen, y cómo diligenciarlos desde conocimiento generado vs invención.

**Preguntas de Investigación**:

1. **¿Qué secciones espera el dashboard en cada artefacto?**
   - Analizar código del dashboard (implementación-log-manager.ts, server.ts)
   - Identificar parsers, validadores, y extractores de metadata
   - Documentar schema esperado para cada artefacto

2. **¿Cuáles son los conceptos de dominio clave en cada artefacto?**
   - requirements.md: User Stories, Functional Requirements, Non-Functional Requirements
   - design.md: ADRs, Architecture Diagrams, Components, Data Models
   - tasks.md: Task Hierarchy, Estimates, Dependencies, Deliverables
   - producto.md: Product Vision, Stakeholders, Metrics
   - tech.md: Technology Stack, Dependencies, Integrations
   - structure.md: Directory Tree, Module Boundaries, Conventions

3. **¿Cómo mapean los artefactos a la cadena RBM?**
   - RF (Resultado Final) → producto.md (visión de producto)
   - RI (Resultado Intermedio) → requirements.md (features/epics)
   - Rinm (Resultado Inmediato) → design.md (componentes), tasks.md (deliverables)
   - Products → tasks.md (productos internos de cada task)
   - Activities → tasks.md (actividades operativas)

4. **¿Cuál es la estrategia para poblar artefactos desde investigación?**
   - DDD Bounded Contexts → tech.md (microservicios/módulos)
   - IMRAD Literature Review → design.md (ADRs con referencias)
   - ISO/IEC 21838 Ontology → structure.md (taxonomía formal de conceptos)
   - Context Engineering → producto.md (stakeholders, contexts of use)

**Metodología IMRAD**:

```markdown
# Workbook: 01-introduction.md
- Problema: No sabemos qué son los artefactos formalmente
- Hipótesis: Los artefactos son proyecciones de dominios bounded contexts
- Objetivos: Comprender estructura, semántica, y estrategia de población

# Workbook: 02-methods.md
- Análisis de código del dashboard (AST parsing)
- Ingeniería reversa de schemas esperados
- Mapeo RBM → Artefactos (domain modeling)
- DDD Event Storming de spec-workflow process

# Workbook: 03-results.md
- Diagramas de estructura esperada (JSON schemas)
- Bounded contexts identificados (diagrama C4)
- Tablas de mapeo RBM → Artefactos
- Ontología preliminar (OWL/Turtle)

# Workbook: 04-analysis.md
- Patrones comunes entre artefactos
- Estrategias de compilación workbook → artifact
- Validación de hipótesis (artefactos = proyecciones de BC)

# Workbook: 05-discussion.md
- Implicaciones para diseño de templates
- Limitaciones del approach actual
- Trabajo futuro (automatización de compilación)

# Workbook: 06-conclusion.md
- Síntesis de hallazgos
- Decisiones de diseño fundamentadas
- Próximos pasos (Phase 2 con conocimiento sólido)

# Workbook: 07-references.md
- Literatura DDD (Eric Evans, Vaughn Vernon)
- ISO/IEC 21838 spec
- Código del dashboard spec-workflow-mcp
```

**Entregables**:
- 7 archivos Markdown en `_melquisedec/domain/workbooks/spec-workflow-artifacts-investigation/`
- Estructura IMRAD completa con 200+ líneas de análisis por workbook
- Diagramas embebidos (Mermaid, C4, UML)
- Referencias bibliográficas formales

**Criterios de Validación**:
- [ ] Cada workbook tiene estructura IMRAD válida (Introduction → Discussion)
- [ ] Preguntas de investigación respondidas con evidencia (código, literatura)
- [ ] Diagramas de bounded contexts usando DDD notation
- [ ] Mapeo RBM → Artefactos con ejemplos concretos
- [ ] Referencias a código del dashboard con line numbers
- [ ] Conclusiones fundamentan decisiones de diseño de Phase 2

**Priority**: 🔴 **CRÍTICA** (bloquea Phase 2)

**Resultado Intermedio**: RI-001.5 (Research Foundation)
**Resultado Inmediato**: Rinm-001.5 (Domain Knowledge Base)

---

### REQ-001-05: Mapeo RBM → Artefactos (Domain Model)

**Objetivo**: Crear modelo de dominio formal que mapea la cadena RBM (Resultado Final → Resultado Intermedio → Resultado Inmediato → Products → Activities) a artefactos de spec-workflow-mcp.

**Modelo de Dominio**:

```
┌─────────────────────────────────────────────────────────────┐
│ RF (Resultado Final)                                        │
│ "Sistema de templates para spec-workflow-mcp"               │
│ └─→ producto.md                                             │
│     - Visión de producto                                    │
│     - Stakeholders                                          │
│     - Métricas de éxito                                     │
└─────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│ RI (Resultado Intermedio)                                   │
│ "Base Infrastructure", "Template System", etc.              │
│ └─→ requirements.md                                         │
│     - Functional Requirements (REQ-001-*, REQ-003-*)        │
│     - User Stories (US-001, US-002)                         │
│     - Non-Functional Requirements                           │
└─────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│ Rinm (Resultado Inmediato)                                  │
│ "Keter-Doc Schema", "Template Base", "Hierarchy System"    │
│ └─→ design.md + tasks.md                                    │
│     - design.md: Componentes, ADRs, Arquitectura           │
│     - tasks.md: Deliverables por task                       │
└─────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│ Products (Productos Internos)                               │
│ "keter-doc-schema.json", "daath-zen-base.md"               │
│ └─→ tasks.md (sección "Deliverables")                      │
│     - Archivos concretos generados por cada task           │
└─────────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│ Activities (Actividades Operativas)                         │
│ "Crear schema", "Validar con JSON Schema", "Escribir tests"│
│ └─→ tasks.md (sección "_Prompt" de cada subtask)           │
│     - Acciones específicas a ejecutar                       │
└─────────────────────────────────────────────────────────────┘
```

**Bounded Contexts Identificados (DDD)**:

1. **Spec Management Context**
   - Entities: Specification, Requirement, UserStory
   - Value Objects: Priority, Status, Category
   - Aggregates: SpecificationAggregate (root: Specification)
   - Repositories: SpecificationRepository
   - Services: SpecificationCompiler

2. **Design Context**
   - Entities: ArchitectureDecisionRecord, Component, DataModel
   - Value Objects: ADRStatus, ComponentType
   - Aggregates: DesignAggregate
   - Services: DiagramGenerator, DesignValidator

3. **Template Context**
   - Entities: Template, TemplateHierarchy, Placeholder
   - Value Objects: TemplateType, InheritanceRule
   - Aggregates: TemplateLibrary
   - Services: TemplateCompiler, PlaceholderResolver

**Entregables**:
- Diagram Mermaid de mapeo RBM → Artefactos
- Modelo de dominio DDD (bounded contexts, entities, value objects)
- Matriz de mapeo: RBM Level × Artefacto × Bounded Context
- Archivo `_melquisedec/domain/models/rbm-artifacts-mapping.md`

**Criterios de Validación**:
- [ ] Cada nivel de RBM mapea a al menos un artefacto
- [ ] Cada artefacto tiene bounded contexts identificados
- [ ] Diagramas DDD usan notación estándar (agregados, entities, VOs)
- [ ] Matriz de mapeo tiene ejemplos concretos de SPEC-001
- [ ] Modelo soporta generación automática de artefactos desde workbooks

**Priority**: 🔴 **CRÍTICA** (dependency de REQ-001-04)

**Resultado Intermedio**: RI-001.5 (Research Foundation)
**Resultado Inmediato**: Rinm-001.5 (Domain Model)

---

### REQ-001-06: Prototipo de Workbook Fundamentado

**Objetivo**: Crear workbook prototipo para SPEC-001 mismo usando estructura IMRAD, demostrando cómo investigación de dominio (literatura, análisis atómico, ADRs) compila a artefactos finales (requirements.md, design.md, tasks.md).

**Estructura del Workbook**:

```
_melquisedec/domain/workbooks/spec-001-prototype/
├── 01-introduction.md      # Problema, hipótesis, objetivos
├── 02-methods.md           # Metodología DDD + IMRAD + ISO
├── 03-results-literature.md # Literatura Review (DDD, templates, MCP)
├── 04-results-analysis.md  # Análisis atómico de requerimientos
├── 05-results-adrs.md      # ADRs (decisiones arquitectónicas)
├── 06-synthesis.md         # Síntesis hacia artefactos
├── 07-discussion.md        # Implicaciones, limitaciones
├── 08-references.md        # Bibliografía formal
└── compiler/
    ├── compile.py          # Script que genera requirements.md, design.md, tasks.md
    ├── templates/          # Templates Jinja2 para cada artefacto
    │   ├── requirements.md.j2
    │   ├── design.md.j2
    │   └── tasks.md.j2
    └── tests/
        └── test_compiler.py
```

**Ejemplo de Compilación**:

```python
# compile.py
from pathlib import Path
import jinja2

def compile_requirements(workbook_dir: Path) -> str:
    """Compila requirements.md desde workbook IMRAD"""
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
    template = env.get_template("requirements.md.j2")
    
    # Extraer datos del workbook
    introduction = parse_markdown(workbook_dir / "01-introduction.md")
    atomic_requirements = parse_markdown(workbook_dir / "04-results-analysis.md")
    
    # Renderizar
    return template.render(
        title=introduction["problem"],
        requirements=atomic_requirements["functional_reqs"],
        user_stories=atomic_requirements["user_stories"],
        references=parse_markdown(workbook_dir / "08-references.md")
    )
```

**Flujo de Trabajo**:

1. **Research Phase** (Workbooks 01-08)
   - Investigar dominio usando IMRAD
   - Literatura review (DDD papers, MCP spec)
   - Análisis atómico de necesidades
   - Documentar ADRs con justificación

2. **Compilation Phase** (compiler/)
   - Extraer secciones relevantes de workbooks
   - Aplicar templates Jinja2
   - Generar requirements.md, design.md, tasks.md
   - Validar output contra schemas

3. **Validation Phase**
   - Verificar coherencia entre artefactos
   - Confirmar que todo contenido tiene fuente en workbook
   - Ejecutar tests de compilador

**Entregables**:
- 8 workbooks IMRAD con 100+ líneas cada uno
- Script `compile.py` funcional con tests (80%+ coverage)
- Templates Jinja2 para requirements.md, design.md, tasks.md
- Artefactos compilados que pasan validación del dashboard
- Documentación del proceso de compilación

**Criterios de Validación**:
- [ ] Workbooks tienen estructura IMRAD completa
- [ ] Script de compilación genera artefactos válidos
- [ ] Todo contenido de artefactos tiene fuente rastreable en workbook
- [ ] Tests de compilador tienen 80%+ coverage
- [ ] Artefactos compilados pasan validación del dashboard spec-workflow-mcp
- [ ] Documentación explica paso a paso el proceso

**Priority**: 🔴 **CRÍTICA** (prototype y prueba de concepto)

**Resultado Intermedio**: RI-001.5 (Research Foundation)
**Resultado Inmediato**: Rinm-001.5 (Workbook-to-Artifact Pipeline)

---

### REQ-001-07: Ontología ISO/IEC 21838 de Spec-Workflow

**Objetivo**: Crear ontología formal de conceptos de spec-workflow-mcp usando ISO/IEC 21838 (top-level ontology) en formato OWL/Turtle, definiendo taxonomía de artefactos, bounded contexts, y relaciones.

**Estructura de Ontología**:

```turtle
@prefix : <http://aleia.melquisedec.dev/ontology/spec-workflow#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix bfo: <http://purl.obolibrary.org/obo/bfo.owl#> .

# Top-Level Classes (BFO alignment)
:Artifact a owl:Class ;
    rdfs:subClassOf bfo:GenericallyDependentContinuant ;
    rdfs:label "Artifact"@en ;
    rdfs:comment "Information artifact that documents part of a specification"@en .

:Requirement a owl:Class ;
    rdfs:subClassOf :Artifact ;
    rdfs:label "Requirement"@en ;
    rdfs:comment "Functional or non-functional requirement"@en .

:DesignDecision a owl:Class ;
    rdfs:subClassOf :Artifact ;
    rdfs:label "Design Decision"@en ;
    rdfs:comment "Architecture Decision Record (ADR)"@en .

:Task a owl:Class ;
    rdfs:subClassOf bfo:PlannedProcess ;
    rdfs:label "Task"@en ;
    rdfs:comment "Unit of work with deliverables"@en .

# Properties
:hasRequirement a owl:ObjectProperty ;
    rdfs:domain :Specification ;
    rdfs:range :Requirement .

:satisfies a owl:ObjectProperty ;
    rdfs:domain :DesignDecision ;
    rdfs:range :Requirement .

:produces a owl:ObjectProperty ;
    rdfs:domain :Task ;
    rdfs:range :Artifact .

# RBM Chain
:ResultadoFinal a owl:Class ;
    rdfs:subClassOf bfo:Objective ;
    rdfs:label "Resultado Final"@es .

:ResultadoIntermedio a owl:Class ;
    rdfs:subClassOf :ResultadoFinal ;
    rdfs:label "Resultado Intermedio"@es .

:maps_to_artifact a owl:ObjectProperty ;
    rdfs:domain :ResultadoFinal ;
    rdfs:range :Artifact .

# Bounded Contexts
:BoundedContext a owl:Class ;
    rdfs:label "Bounded Context (DDD)"@en ;
    rdfs:comment "Domain-Driven Design bounded context"@en .

:SpecManagementContext a :BoundedContext ;
    rdfs:label "Spec Management Context"@en .

:DesignContext a :BoundedContext ;
    rdfs:label "Design Context"@en .

:TemplateContext a :BoundedContext ;
    rdfs:label "Template Context"@en .
```

**Requisitos ISO/IEC 21838**:

1. **Upper Ontology Alignment**: Usar BFO (Basic Formal Ontology) como top-level
2. **Formal Definitions**: Cada clase tiene definición formal con necessary/sufficient conditions
3. **Axiomatization**: Axiomas OWL para inferencia (e.g., "Task produces Artifact → Artifact created by Task")
4. **Modularity**: Ontología dividida en módulos (core, rbm, ddd, templates)
5. **Reasoner Validation**: Validar con HermiT o Pellet (consistencia, subsumption)

**Entregables**:
- Archivo `_melquisedec/domain/ontologies/spec-workflow-ontology.ttl`
- Módulos: core.ttl, rbm.ttl, ddd.ttl, templates.ttl
- Reporte de reasoner (Pellet) validando consistencia
- Diagrama visual de taxonomía (OntoGraf o similar)
- Queries SPARQL de ejemplo para extraer conocimiento

**Criterios de Validación**:
- [ ] Ontología alineada con BFO (ISO/IEC 21838-2)
- [ ] Cada clase tiene rdfs:label, rdfs:comment, definición formal
- [ ] Axiomas OWL permiten inferencia (tested con reasoner)
- [ ] Reasoner valida consistencia sin contradicciones
- [ ] Queries SPARQL pueden extraer mapeo RBM → Artefactos
- [ ] Documentación explica decisiones ontológicas

**Priority**: 🟡 **ALTA** (formal foundation, pero no bloquea implementation)

**Resultado Intermedio**: RI-001.5 (Research Foundation)
**Resultado Inmediato**: Rinm-001.5 (Formal Ontology)

---

### REQ-001-08: Actualización de Templates con Insights de Dominio

**Objetivo**: Actualizar templates base (daath-zen-base.md) para incluir secciones de "Knowledge Sources" que referencian workbooks de dominio, asegurando trazabilidad epistemológica desde investigación hasta artefactos.

**Nuevas Secciones en Templates**:

```markdown
---
# HKM Header
# (existente)
---

# JSON-LD Metadata
# (existente)
---

## 🔬 Knowledge Sources

> Este documento fue generado desde workbooks de dominio. Cada sección tiene fuente rastreable en investigación IMRAD.

**Workbooks Base**:
- `_melquisedec/domain/workbooks/{{WORKBOOK_NAME}}/`
  - 01-introduction.md → Problema y objetivos
  - 02-methods.md → Metodología aplicada
  - 03-results-literature.md → Literatura review
  - 04-results-analysis.md → Análisis atómico
  - 05-results-adrs.md → Decisiones arquitectónicas
  - 06-synthesis.md → Síntesis hacia este artefacto
  - 07-discussion.md → Implicaciones y limitaciones
  - 08-references.md → Bibliografía formal

**Domain Model**:
- `_melquisedec/domain/models/rbm-artifacts-mapping.md`
- Bounded Contexts: {{BOUNDED_CONTEXTS}}
- RBM Level: {{RBM_LEVEL}}

**Ontology**:
- `_melquisedec/domain/ontologies/spec-workflow-ontology.ttl`
- Classes: {{ONTOLOGY_CLASSES}}
- Properties: {{ONTOLOGY_PROPERTIES}}

**⚠️ Trazabilidad**: Cada claim en este documento debe tener cita a workbook o literatura.

---

# {{DOCUMENT_TITLE}}
# (resto del template existente)
---
```

**Validaciones Adicionales**:

```python
# En TemplateValidator class
def validate_knowledge_sources(self, document: str) -> ValidationResult:
    """Valida que todo contenido tenga fuente en workbooks"""
    claims = extract_claims(document)
    sources = extract_sources(document)
    
    for claim in claims:
        if not has_source(claim, sources):
            return ValidationError(f"Claim '{claim}' no tiene fuente en workbook")
    
    return ValidationSuccess()
```

**Entregables**:
- Templates actualizados (daath-zen-base.md, all children)
- Validator que verifica trazabilidad a workbooks
- Tests para validación de knowledge sources
- Documentación de cómo citar workbooks

**Criterios de Validación**:
- [ ] Todos los templates tienen sección "Knowledge Sources"
- [ ] Placeholders para workbook references funcionan
- [ ] Validator detecta claims sin fuente
- [ ] Tests cubren escenarios de trazabilidad válida/inválida
- [ ] Documentación explica formato de citas a workbooks

**Priority**: 🟡 **MEDIA** (mejora calidad, pero no bloquea)

**Resultado Intermedio**: RI-001.5 (Research Foundation)
**Resultado Inmediato**: Rinm-001.5 (Traceable Templates)

---

## 📐 Phase 2: Template System

---

### REQ-003-01: Estructura de Template Base

**Objetivo**: Crear template `daath-zen-base.md` con elementos universales.

**Contenido**:

```markdown
---
# HKM Header
# (REQ-001-02)
---

# JSON-LD Metadata
# (REQ-001-01)

---

# {{DOCUMENT_TITLE}}

## Metadatos

{{METADATA_TABLE}}

---

## Overview

{{OVERVIEW_CONTENT}}

---

## Principios MELQUISEDEC Aplicados

{{PRINCIPLES_LIST}}

---

{{BODY_SECTIONS}}

---

## Referencias

{{REFERENCES}}

---

**Compilado desde**: `{{WORKBOOK_PATH}}`
**Fecha de compilación**: `{{COMPILATION_TIMESTAMP}}`
**Versión de compilador**: `{{COMPILER_VERSION}}`
**⚠️ ADVERTENCIA**: Este archivo es generado. Editar workbook, no este archivo.
```

**Criterios de Validación**:
- [ ] Todos los placeholders están documentados
- [ ] Secciones universales presentes (Metadatos, Overview, Principios)
- [ ] Footer de compilación incluido
- [ ] Formato Markdown válido

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-002 (Template System)
**Resultado Inmediato**: Rinm-001 (Base Template)

---

### REQ-003-02: Reglas de Herencia de Templates

**Objetivo**: Definir sistema de herencia en `config.yaml-ld`.

**Especificación**:

```yaml
# config.yaml-ld v1.0.0
"@context":
  "@vocab": "http://melquisedec.org/template#"
  "dc": "http://purl.org/dc/terms/"

version: "1.0.0"
created: "2026-01-10"
maintainer: "MELQUISEDEC Architecture Team"

template_hierarchy:
  base:
    name: "daath-zen-base"
    version: "1.0.0"
    file: "templates/daath-zen-base.md"
    sections:
      - name: "hkm_header"
        mandatory: true
        format: "yaml-frontmatter"
      - name: "keter_protocol"
        mandatory: true
        format: "json-ld"
      - name: "metadata_table"
        mandatory: true
      - name: "overview"
        mandatory: true
      - name: "principles_applied"
        mandatory: true
      - name: "compilation_footer"
        mandatory: true
        auto_generated: true

  variants:
    requirements:
      extends: "base"
      version: "1.0.0"
      file: "templates/daath-zen-requirements.md"
      additional_sections:
        - name: "coherence_matrix"
          format: "mermaid + yaml"
          source: "workbook"
        - name: "user_stories"
          source: "workbook"
          path: "ri-*/rinm-*/REQ-*-story.md"
        - name: "functional_requirements"
          source: "workbook"
          path: "ri-*/rinm-*/REQ-*.md"

    design:
      extends: "base"
      version: "1.0.0"
      file: "templates/daath-zen-design.md"
      additional_sections:
        - name: "architecture_diagrams"
          format: "mermaid"
        - name: "adr_decisions"
          source: "workbook"
          path: "decisions/ADR-*.md"
        - name: "component_specifications"
          source: "generated"

    tasks:
      extends: "base"
      version: "1.0.0"
      file: "templates/daath-zen-tasks.md"
      additional_sections:
        - name: "task_list"
          format: "markdown-checklist"
          source: "workbook"
        - name: "implementation_order"
          format: "mermaid-gantt"
        - name: "metrics_definition"
          source: "workbook"
```

**Criterios de Validación**:
- [ ] Parser YAML-LD lee config sin errores
- [ ] Jerarquía base → variantes es válida (no ciclos)
- [ ] Todas las variantes extienden base
- [ ] Secciones adicionales no duplican base
- [ ] Paths de source="workbook" usan glob patterns válidos

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-002 (Template System)
**Resultado Inmediato**: Rinm-001 (Base Template)

---

### REQ-003-03: Template requirements.md con Secciones RBM

**Objetivo**: Crear template variante para requirements con integración RBM.

**Secciones Específicas**:

1. **Coherence Matrix** (después de Overview):
```markdown
## Matriz de Coherencia RBM

\```mermaid
graph TB
    RF[Resultado Final: {{RF_TITLE}}]

    RF --> RI1[RI-001: {{RI1_TITLE}}]
    RF --> RI2[RI-002: {{RI2_TITLE}}]

    RI1 --> Rinm1[Rinm-001: {{RINM1_TITLE}}]
    RI1 --> Rinm2[Rinm-002: {{RINM2_TITLE}}]

    Rinm1 --> REQ1[REQ-001-01: {{REQ1_TITLE}}]
    Rinm1 --> REQ2[REQ-001-02: {{REQ2_TITLE}}]
\```

**Cadena Causal**:

{{COHERENCE_MATRIX_TABLE}}
```

2. **User Stories** (después de Matriz):
```markdown
## User Stories

{{USER_STORIES_FROM_WORKBOOK}}
```

3. **Functional Requirements** (después de User Stories):
```markdown
## Functional Requirements

{{FUNCTIONAL_REQUIREMENTS_FROM_WORKBOOK}}
```

**Criterios de Validación**:
- [ ] Diagrama Mermaid renderiza correctamente
- [ ] Tabla de coherencia incluye columnas: RF, RI, Rinm, REQ, Métricas
- [ ] User stories siguen formato: "Como X, quiero Y, para que Z"
- [ ] Cada REQ tiene: Objetivo, Especificación, Criterios de Validación, Priority, Trazabilidad

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-002 (Template System)
**Resultado Inmediato**: Rinm-002 (Variant Templates)

---

### REQ-003-04: Template design.md con ADRs

**Objetivo**: Template variante para design con Architecture Decision Records.

**Secciones Específicas**:

```markdown
## Decisiones Arquitectónicas (ADRs)

{{ADR_LIST_FROM_WORKBOOK}}

---

## Diagrama de Arquitectura

\```mermaid
{{ARCHITECTURE_DIAGRAM}}
\```

---

## Especificación de Componentes

{{COMPONENT_SPECS_FROM_WORKBOOK}}

---

## Estrategia de Migración

{{MIGRATION_STRATEGY}}

---

## Plan de Rollback

{{ROLLBACK_PLAN}}
```

**Criterios de Validación**:
- [ ] ADRs siguen formato estándar (Context, Decision, Consequences)
- [ ] Diagrama de arquitectura usa notación C4 o similar
- [ ] Cada componente tiene: Propósito, API, Dependencias, Métricas
- [ ] Estrategia de migración incluye pasos secuenciados

**Priority**: 🟡 **MEDIA**

**Resultado Intermedio**: RI-002 (Template System)
**Resultado Inmediato**: Rinm-002 (Variant Templates)

---

### REQ-003-05: Template tasks.md con Checklist

**Objetivo**: Template variante para tasks con estructura de implementación.

**Secciones Específicas**:

```markdown
## Implementation Tasks

{{TASK_CHECKLIST_FROM_WORKBOOK}}

---

## Orden de Implementación

\```mermaid
gantt
    title Implementation Timeline
    dateFormat  YYYY-MM-DD

    {{GANTT_TASKS}}
\```

---

## Definición de Métricas

{{METRICS_DEFINITIONS}}

---

## Criterios de Completitud

{{COMPLETION_CRITERIA}}
```

**Criterios de Validación**:
- [ ] Tasks usan formato markdown checklist: `- [ ] Task description`
- [ ] Cada task tiene: ID, Description, Dependencies, Estimated Time
- [ ] Gantt chart renderiza correctamente
- [ ] Métricas son medibles y específicas

**Priority**: 🟡 **MEDIA**

**Resultado Intermedio**: RI-002 (Template System)
**Resultado Inmediato**: Rinm-002 (Variant Templates)

---

### REQ-003-06 a REQ-003-08: Templates de Steering

**Objetivo**: Templates para documentos steering (product, tech, structure).

**Contenido Mínimo**:
- **product.md**: Visión, Roadmap, User Personas
- **tech.md**: Stack tecnológico, Convenciones de código, Herramientas
- **structure.md**: Organización de carpetas, Naming conventions, Workflows

**Criterios de Validación**:
- [ ] Cada template tiene < 200 líneas
- [ ] Secciones alineadas con guías de spec-workflow-mcp
- [ ] Ejemplos provistos para cada sección

**Priority**: 🟢 **BAJA** (opcional, no bloqueante)

**Resultado Intermedio**: RI-002 (Template System)
**Resultado Inmediato**: Rinm-002 (Variant Templates)

---

### REQ-003-01: Parser de Estructura Workbook

**Objetivo**: Implementar función `parse_workbook_structure()`.

**Especificación**:

```python
# tools/compile_spec_from_workbook.py

def parse_workbook_structure(workbook_path: Path) -> Dict:
    """
    Escanea workbook y construye árbol RBM.

    Returns:
        {
            'resultado_final': {...},
            'intermediate_results': [
                {
                    'id': 'RI-001',
                    'path': Path(...),
                    'immediate_results': [
                        {
                            'id': 'Rinm-001',
                            'path': Path(...),
                            'products': [
                                {
                                    'id': 'REQ-001-01',
                                    'file': Path(...),
                                    'content': str
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    """
    # Implementación:
    # 1. Escanear carpetas ri-*
    # 2. Para cada RI, escanear rinm-*
    # 3. Para cada Rinm, escanear REQ-*.md
    # 4. Leer contenido y metadata de cada REQ
```

**Criterios de Validación**:
- [ ] Parser maneja workbooks vacíos sin crash
- [ ] Parser detecta IDs mal formateados y lanza error claro
- [ ] Parser preserva orden alfabético de carpetas
- [ ] Performance: < 1 segundo para 50 productos

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-003 (Compilation Pipeline)
**Resultado Inmediato**: Rinm-001 (Compiler Script)

---

### REQ-003-02: Procesador de Transclusions Obsidian

**Objetivo**: Implementar `process_transclusions()` para resolver `![[]]`.

**Especificación**:

```python
def process_transclusions(template: str, workbook_path: Path) -> str:
    """
    Procesa transclusions estilo Obsidian.

    Ejemplos:
        ![[ri-001/rinm-001/REQ-001-01-story]]
        → Contenido de REQ-001-01-story.md

        ![[resultado_final#Metricas]]
        → Solo sección "Metricas" de resultado_final.md
    """
    import re

    pattern = r'!\[\[([^\]#]+)(?:#([^\]]+))?\]\]'

    def replace_transclusion(match):
        path = match.group(1)
        section = match.group(2)  # Optional

        full_path = workbook_path / f"{path}.md"

        if not full_path.exists():
            return f"⚠️ Faltante: {path}"

        content = full_path.read_text()

        if section:
            # Extract section only
            return extract_section(content, section)

        return content

    return re.sub(pattern, replace_transclusion, template)
```

**Criterios de Validación**:
- [ ] Resuelve transclusions simples `![[path]]`
- [ ] Resuelve transclusions con sección `![[path#section]]`
- [ ] Maneja archivos faltantes con mensaje claro
- [ ] No procesa links normales `[[link]]` (solo transclusions `![[]]`)

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-003 (Compilation Pipeline)
**Resultado Inmediato**: Rinm-001 (Compiler Script)

---

### REQ-003-03: Constructor de Matriz de Coherencia

**Objetivo**: Implementar `build_coherence_matrix()`.

**Especificación**:

```python
def build_coherence_matrix(rbm_structure: Dict) -> Dict:
    """
    Genera matriz de coherencia RBM.

    Returns:
        {
            'final_result': {...},
            'chain': [
                {
                    'RF': 'RF-001',
                    'RI': 'RI-001',
                    'Rinm': 'Rinm-001',
                    'REQ': 'REQ-001-01',
                    'metrics': {...}
                }
            ],
            'orphans': [],  # REQs sin padre
            'breaks': []    # Breaks en cadena
        }
    """
```

**Criterios de Validación**:
- [ ] Matriz completa para workbook válido
- [ ] Detecta REQs huérfanos (sin Rinm padre)
- [ ] Detecta breaks en cadena (Rinm sin RI padre)
- [ ] Genera tabla Markdown formateada

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-003 (Compilation Pipeline)
**Resultado Inmediato**: Rinm-001 (Compiler Script)

---

### REQ-003-04: Renderizador de Template

**Objetivo**: Implementar `render_template()` con Jinja2.

**Especificación**:

```python
from jinja2 import Template

def render_template(template_path: Path, context: Dict) -> str:
    """
    Renderiza template con contexto.

    Args:
        template_path: Path a template Jinja2
        context: Diccionario con variables para reemplazar

    Returns:
        Contenido renderizado
    """
    template_content = template_path.read_text()
    template = Template(template_content)

    return template.render(**context)
```

**Contexto esperado**:
```python
context = {
    'DOCUMENT_TITLE': 'Requirements',
    'METADATA_TABLE': '...',
    'OVERVIEW_CONTENT': '...',
    'PRINCIPLES_LIST': '...',
    'COHERENCE_MATRIX_TABLE': '...',
    'USER_STORIES_FROM_WORKBOOK': '...',
    'FUNCTIONAL_REQUIREMENTS_FROM_WORKBOOK': '...',
    'WORKBOOK_PATH': 'wb-rbm-spec-001/',
    'COMPILATION_TIMESTAMP': '2026-01-10T15:30:00Z',
    'COMPILER_VERSION': '1.0.0'
}
```

**Criterios de Validación**:
- [ ] Template renderiza sin errores
- [ ] Variables no definidas generan warning (no crash)
- [ ] Output es Markdown válido
- [ ] Preserva formato de bloques de código

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-003 (Compilation Pipeline)
**Resultado Inmediato**: Rinm-001 (Compiler Script)

---

### REQ-004-01: Validador de Keter-Doc

**Objetivo**: Implementar `validate_keter_doc()`.

**Especificación**:

```python
from jsonschema import validate, ValidationError
import yaml

def validate_keter_doc(document_path: Path, schema_path: Path) -> Tuple[bool, List[str]]:
    """
    Valida documento contra schema keter-doc.

    Returns:
        (is_valid, error_messages)
    """
    # 1. Extraer frontmatter YAML
    content = document_path.read_text()
    frontmatter = extract_frontmatter(content)

    # 2. Validar contra schema JSON-LD
    schema = yaml.safe_load(schema_path.read_text())

    try:
        validate(instance=frontmatter, schema=schema)
        return (True, [])
    except ValidationError as e:
        return (False, [str(e)])
```

**Validaciones Específicas**:
- [ ] `@context`, `@type`, `@id` presentes
- [ ] URNs tienen formato correcto
- [ ] Fechas en ISO8601
- [ ] Principios referenciados existen (P1-P10)
- [ ] Rostro es uno de los 5 válidos

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-004 (Validation System)
**Resultado Inmediato**: Rinm-001 (Validators)

---

### REQ-004-02: Validador de Coherencia RBM

**Objetivo**: Implementar `validate_rbm_coherence()`.

**Especificación**:

```python
def validate_rbm_coherence(coherence_matrix: Dict) -> Tuple[bool, List[str]]:
    """
    Valida cadena causal RBM.

    Checks:
        1. Todos los REQ mapean a un Rinm
        2. Todos los Rinm mapean a un RI
        3. Todos los RI mapean a RF
        4. No hay ciclos

    Returns:
        (is_valid, error_messages)
    """
    errors = []

    # Check 1: REQs → Rinm
    orphan_reqs = [r for r in matrix['chain'] if not r['Rinm']]
    if orphan_reqs:
        errors.append(f"REQs huérfanos: {orphan_reqs}")

    # Check 2: Rinm → RI
    orphan_rinm = [r for r in matrix['chain'] if not r['RI']]
    if orphan_rinm:
        errors.append(f"Rinm huérfanos: {orphan_rinm}")

    # Check 3: RI → RF
    orphan_ri = [r for r in matrix['chain'] if not r['RF']]
    if orphan_ri:
        errors.append(f"RI huérfanos: {orphan_ri}")

    return (len(errors) == 0, errors)
```

**Criterios de Validación**:
- [ ] Detecta REQs sin Rinm padre
- [ ] Detecta Rinm sin RI padre
- [ ] Detecta RI sin RF padre
- [ ] Mensajes de error incluyen IDs específicos

**Priority**: 🔴 **ALTA**

**Resultado Intermedio**: RI-004 (Validation System)
**Resultado Inmediato**: Rinm-001 (Validators)

---

### REQ-004-03: Validador de Sincronización Neo4j

**Objetivo**: Implementar `validate_neo4j_sync()`.

**Especificación**:

```python
from neo4j import GraphDatabase

def validate_neo4j_sync(document_path: Path, neo4j_uri: str) -> Tuple[bool, List[str]]:
    """
    Valida que documento existe en Neo4j con relaciones correctas.

    Checks:
        1. Nodo Spec existe con metadata correcta
        2. Relaciones :IMPLEMENTS_PRINCIPLE presentes
        3. Relaciones :HAS_INTERMEDIATE_RESULT presentes

    Returns:
        (is_valid, error_messages)
    """
    driver = GraphDatabase.driver(neo4j_uri)

    with driver.session() as session:
        # Query para verificar nodo
        result = session.run("""
            MATCH (s:Spec {id: $spec_id})
            RETURN s,
                   [(s)-[:IMPLEMENTS_PRINCIPLE]->(p) | p] as principles,
                   [(s)-[:HAS_INTERMEDIATE_RESULT]->(ri) | ri] as results
        """, spec_id=extract_spec_id(document_path))

        # Verificar resultado
        # ...
```

**Criterios de Validación**:
- [ ] Nodo Spec existe en Neo4j
- [ ] Metadata coincide con documento
- [ ] Relaciones correctas presentes
- [ ] Error claro si no hay conexión a Neo4j

**Priority**: 🟡 **MEDIA** (opcional si no hay Neo4j disponible)

**Resultado Intermedio**: RI-004 (Validation System)
**Resultado Inmediato**: Rinm-001 (Validators)

---

### REQ-005-01: Guía de Uso de Templates

**Objetivo**: Crear `template-usage-guide.md`.

**Contenido Mínimo**:

```markdown
# Guía de Uso de Templates daath-zen

## 1. Elegir Template Apropiado
- requirements.md → Para especificar qué construir
- design.md → Para especificar cómo construir
- tasks.md → Para especificar pasos de implementación
- steering/product.md → Para visión y roadmap
- steering/tech.md → Para stack y convenciones
- steering/structure.md → Para organización de proyecto

## 2. Crear Workbook RBM
...

## 3. Compilar Workbook a Spec
...

## 4. Validar Antes de Someter
...

## 5. Someter para Aprobación
...
```

**Criterios de Validación**:
- [ ] Guía cubre flujo completo end-to-end
- [ ] Cada paso tiene ejemplo concreto
- [ ] Troubleshooting section incluida
- [ ] < 3000 palabras (lectura < 15 minutos)

**Priority**: 🟡 **MEDIA**

**Resultado Intermedio**: RI-005 (Documentation & Examples)
**Resultado Inmediato**: Rinm-001 (Guides)

---

### REQ-005-02: Guía de Creación de Workbook

**Objetivo**: Crear `workbook-creation-guide.md`.

**Contenido Mínimo**:

```markdown
# Guía de Creación de Workbook RBM

## Estructura Recomendada
\```
wb-rbm-{spec-name}/
├── resultado_final.md
├── ri-001-feature/
│   └── rinm-001-product/
│       ├── overview.md
│       ├── REQ-001-01-story.md
│       ├── REQ-001-02-rule.md
│       └── metrics.yaml
\```

## Convenciones de Naming
- Carpetas RI: `ri-{numero}-{slug}`
- Carpetas Rinm: `rinm-{numero}-{slug}`
- Archivos REQ: `REQ-{ri}-{rinm}-{tipo}.md`
- Tipos: story, rule, functional, contract, interface

## Escribir Resultado Final
...

## Escribir Resultados Intermedios (Features)
...

## Escribir Resultados Inmediatos (Productos)
...

## Definir Métricas
...
```

**Criterios de Validación**:
- [ ] Guía explica jerarquía RBM claramente
- [ ] Convenciones de naming documentadas
- [ ] Ejemplos de cada tipo de archivo
- [ ] Métricas de ejemplo provistas

**Priority**: 🟡 **MEDIA**

**Resultado Intermedio**: RI-005 (Documentation & Examples)
**Resultado Inmediato**: Rinm-001 (Guides)

---

### REQ-005-03: Workbook de Ejemplo (Autenticación)

**Objetivo**: Crear workbook `wb-rbm-example-auth`.

**Estructura**:

```
020-conceive/03-workbooks/wb-rbm-example-auth/
├── resultado_final.md
│   # RF: Sistema de autenticación seguro
│   # Métricas: 100% usuarios pueden autenticarse, <500ms login
│
├── ri-001-login/
│   ├── ri-001.md
│   └── rinm-001-email-password/
│       ├── overview.md
│       ├── REQ-001-01-story-registro.md
│       ├── REQ-001-02-story-login.md
│       ├── REQ-001-03-rule-validacion-email.md
│       └── metrics.yaml
│
└── ri-002-oauth/
    ├── ri-002.md
    └── rinm-001-google-oauth/
        ├── overview.md
        ├── REQ-002-01-story-login-google.md
        ├── REQ-002-02-contract-oauth-api.md
        └── metrics.yaml
```

**Criterios de Validación**:
- [ ] Workbook compila sin errores
- [ ] Matriz de coherencia completa
- [ ] README explica el ejemplo
- [ ] Incluye al menos 2 RI, 2 Rinm, 5 REQ

**Priority**: 🟡 **MEDIA**

**Resultado Intermedio**: RI-005 (Documentation & Examples)
**Resultado Inmediato**: Rinm-001 (Guides)

---

## Non-Functional Requirements

### NFR-001: Performance de Compilación
- Compilación workbook (50 productos) < 5 segundos
- Validación keter-doc < 500ms
- Validación coherencia RBM < 1 segundo
- Sincronización Neo4j < 2 segundos

### NFR-002: Usabilidad
- Nuevo usuario crea primer workbook en < 2 horas (con guías)
- Compilación exitosa al primer intento > 80%
- Mensajes de error claros y accionables
- Documentación de templates < 5000 palabras por documento

### NFR-003: Maintainability
- Código Python con type hints completos
- Cobertura de tests unitarios > 80%
- Todos los functions documentados con docstrings
- ADRs para todas las decisiones arquitectónicas mayores

### NFR-004: Interoperabilidad
- Templates compatibles con Obsidian (transclusions, links)
- Metadata ingestable en Neo4j sin transformación
- JSON-LD válido según spec 1.1
- Markdown renderiza correctamente en GitHub y VS Code

### NFR-005: Evolvability
- Templates versionados (semantic versioning)
- Changelog mantenido
- Hooks para agregar validadores custom
- Sistema de plugins para extender compilador

---

## Matriz de Coherencia RBM

### Resultado Final
**RF-001**: Sistema de templates daath-zen operativo con integración RBM y compilación automática

**Métricas de Éxito**:
- 6 templates creados y funcionando (base + 5 variantes)
- Compilación exitosa de workbook de ejemplo
- Validación keter-doc y RBM operativa
- Documentación completa con ejemplos

### Cadena Causal

| RF | RI | Rinm | REQ | Métrica |
|----|----|----|-----|---------|
| RF-001 | RI-001 | Rinm-001 | REQ-001-01 | Schema JSON-LD válido |
| RF-001 | RI-001 | Rinm-001 | REQ-001-02 | Header HKM completo |
| RF-001 | RI-001 | Rinm-001 | REQ-001-03 | Dublin Core mapeado |
| RF-001 | RI-001.5 | Rinm-001.5 | REQ-001-04 | Investigación IMRAD completada |
| RF-001 | RI-001.5 | Rinm-001.5 | REQ-001-05 | Mapeo RBM → Artefactos validado |
| RF-001 | RI-001.5 | Rinm-001.5 | REQ-001-06 | Workbook prototipo compila |
| RF-001 | RI-001.5 | Rinm-001.5 | REQ-001-07 | Ontología ISO validada |
| RF-001 | RI-001.5 | Rinm-001.5 | REQ-001-08 | Templates con trazabilidad |
| RF-001 | RI-002 | Rinm-001 | REQ-003-01 | Template base creado |
| RF-001 | RI-002 | Rinm-001 | REQ-003-02 | Config herencia válido |
| RF-001 | RI-002 | Rinm-002 | REQ-003-03 | Template requirements creado |
| RF-001 | RI-002 | Rinm-002 | REQ-003-04 | Template design creado |
| RF-001 | RI-002 | Rinm-002 | REQ-003-05 | Template tasks creado |
| RF-001 | RI-002 | Rinm-002 | REQ-003-06 | Template product creado |
| RF-001 | RI-002 | Rinm-002 | REQ-003-07 | Template tech creado |
| RF-001 | RI-002 | Rinm-002 | REQ-003-08 | Template structure creado |
| RF-001 | RI-003 | Rinm-001 | REQ-004-01 | Parser workbook funciona |
| RF-001 | RI-003 | Rinm-001 | REQ-004-02 | Transclusions resueltas |
| RF-001 | RI-003 | Rinm-001 | REQ-004-03 | Matriz coherencia generada |
| RF-001 | RI-003 | Rinm-001 | REQ-004-04 | Template renderiza |
| RF-001 | RI-004 | Rinm-001 | REQ-005-01 | Validador keter-doc funciona |
| RF-001 | RI-004 | Rinm-001 | REQ-005-02 | Validador RBM funciona |
| RF-001 | RI-004 | Rinm-001 | REQ-005-03 | Validador Neo4j funciona |
| RF-001 | RI-005 | Rinm-001 | REQ-006-01 | Guía de templates escrita |
| RF-001 | RI-005 | Rinm-001 | REQ-006-02 | Guía de workbook escrita |
| RF-001 | RI-005 | Rinm-001 | REQ-006-03 | Workbook ejemplo creado |

---

## Dependencies

### External Tools
- **spec-workflow-mcp** >= 1.0.0 - Base workflow system
- **Obsidian** >= 1.5.0 - Markdown editing with transclusions
- **Neo4j** >= 5.15.0 - Graph database para persistencia
- **Python** >= 3.10 - Scripting y compilación

### Python Packages
```txt
PyYAML>=6.0
jinja2>=3.1.0
jsonschema>=4.20.0
rdflib>=7.0.0
neo4j>=5.15.0
click>=8.1.0  # CLI
rich>=13.0.0  # Pretty printing
```

### Internal Dependencies
- `ANALISIS-spec-001-mejores-practicas.md` - Guía de escritura
- `LECCION-001-arquitectura-templates-specs.md` - Learnings capturados
- `raw-manifiesto-melquisedec.md` - Principios MELQUISEDEC

---

## Success Criteria

### Phase: Requirements (Este Documento)
- [ ] Todos los requirements escritos y numerados
- [ ] Matriz de coherencia RBM completa
- [ ] User stories tienen formato: Como X, quiero Y, para que Z
- [ ] Cada REQ tiene: Objetivo, Especificación, Validación, Priority, Trazabilidad
- [ ] Document aprobado por stakeholders vía dashboard

### Phase: Design (Siguiente)
- [ ] Arquitectura detallada de compilador
- [ ] Diagramas de flujo para cada paso
- [ ] ADRs para decisiones mayores (5+ decisiones)
- [ ] Especificación de interfaces Python
- [ ] Estrategia de testing definida

### Phase: Tasks (Siguiente)
- [ ] Desglose completo de tareas de implementación
- [ ] Orden de dependencias establecido
- [ ] Estimaciones de tiempo por task
- [ ] Criterios de completitud por task
- [ ] Gantt chart de timeline

### Phase: Implementation (Final)
- [ ] Todos los 6 templates creados
- [ ] `compile_spec_from_workbook.py` funcional
- [ ] 3 validadores operativos
- [ ] 3 guías documentadas
- [ ] 1 workbook de ejemplo compila exitosamente
- [ ] Tests unitarios > 80% coverage
- [ ] SPEC-002 puede usar sistema de templates nuevo

---

## Next Steps

1. **Someter este documento para aprobación** vía spec-workflow-mcp dashboard
2. **Esperar feedback** de stakeholders (arquitectos, desarrolladores)
3. **Iterar requirements** basado en comentarios de revisión
4. **Aprobar requirements** formalmente
5. **Proceder a design phase** usando template daath-zen-design.md
6. **Crear ADRs** para decisiones arquitectónicas críticas

---

## Referencias

- [spec-workflow-mcp Documentation](https://github.com/pimzino/spec-workflow-mcp)
- [ANALISIS-spec-001-mejores-practicas.md](../../../_melquisedec/lessons/ANALISIS-spec-001-mejores-practicas.md)
- [LECCION-001-arquitectura-templates-specs.md](../../../_melquisedec/lessons/LECCION-001-arquitectura-templates-specs.md)
- [raw-manifiesto-melquisedec.md](../../../_melquisedec/manifest/1-inputs/raw-manifiesto-melquisedec.md)
- [JSON-LD 1.1 Specification](https://www.w3.org/TR/json-ld11/)
- [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
- [Results-Based Management Handbook](https://www.undp.org/publications/handbook-planning-monitoring-and-evaluating-development-results)

---

**Compilado por**: GitHub Copilot (Claude Sonnet 4.5)
**Basado en**: Análisis de mejores prácticas y learnings capturados
**Estado**: Draft for Approval
**Próximo Documento**: design.md
**⚠️ Nota**: Este documento NO fue compilado desde workbook (es el primer spec, define el sistema de compilación). Futuros specs SÍ usarán compilación desde workbook.
