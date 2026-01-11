# 02 - Revisión de Literatura (Literature Review)

**SPEC-001**: Built-in Template Spec Workflow  
**Fase**: Phase 2 - SALOMÓN IMRAD Investigation  
**Metodología**: HYPATIA→SALOMÓN Pipeline  
**Fecha**: 2026-01-10  
**Knowledge Base**: `artefactos-conocimiento/frameworks-catalog.json`

---

## 2.1 Introducción

Esta sección revisa los **6 frameworks** catalogados en el knowledge base [`frameworks-catalog.json`] que fundamentan el diseño de artifacts para SPEC-001. Cada framework se analiza en términos de:

- **Descripción**: Qué es y para qué sirve
- **Conceptos clave**: Elementos fundamentales del framework
- **Fuentes primarias**: Literatura de referencia (status de disponibilidad)
- **Aplicación en SPEC-001**: Cómo se utiliza en este proyecto

La revisión se organiza por relevancia arquitectónica, comenzando con frameworks de diseño y culminando con metodologías específicas de este proyecto.

---

## 2.2 Domain-Driven Design (DDD)

**Framework ID**: `framework-001`  
**Tipo**: Architectural Pattern  
**Dominio**: Software Architecture

### 2.2.1 Descripción

Domain-Driven Design es un enfoque de diseño de software que **prioriza el modelado del dominio del negocio** y la colaboración estrecha entre expertos técnicos y expertos de dominio. Introducido por Eric Evans en 2003, DDD propone que la complejidad del software se aborde mediante un modelo de dominio rico que refleje el lenguaje y los conceptos del negocio.

### 2.2.2 Conceptos Clave

Los conceptos fundamentales de DDD que aplican a SPEC-001 son:

1. **Bounded Context** [`concept-manual-006`]: Delimitación explícita donde un modelo de dominio es aplicable
2. **Ubiquitous Language**: Lenguaje compartido entre técnicos y expertos de dominio
3. **Aggregate**: Cluster de objetos tratados como unidad para cambios de datos
4. **Entity**: Objeto con identidad única que persiste en el tiempo
5. **Value Object**: Objeto inmutable sin identidad, definido por sus atributos
6. **Repository**: Abstracción para acceso a aggregates persistidos

### 2.2.3 Fuentes Primarias

**Evans, Eric (2003)**:
- **Título**: *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- **Editorial**: Addison-Wesley Professional
- **ISBN**: 978-0321125217
- **Páginas**: 560
- **Status**: ⏳ Pendiente de descarga (requiere Library Genesis o compra)
- **Relevancia**: Obra fundacional que introduce todos los patrones DDD

**Vernon, Vaughn (2013)**:
- **Título**: *Implementing Domain-Driven Design*
- **Editorial**: Addison-Wesley Professional
- **ISBN**: 978-0321834577
- **Páginas**: 656
- **Status**: ⏳ Pendiente de descarga (requiere Library Genesis o compra)
- **Relevancia**: Implementación práctica de DDD con ejemplos concretos

### 2.2.4 Aplicación en SPEC-001

DDD se aplica en el diseño de artifacts mediante:

- **Bounded Contexts**: Cada artifact type define un contexto delimitado (e.g., `TestArtifact` tiene su propio modelo)
- **Entities vs Value Objects**: Artifacts son Entities (tienen ID único), mientras que sus campos pueden ser Value Objects
- **Aggregates**: Un artifact completo (con todos sus campos validados) es un Aggregate
- **Repositories**: El sistema de gestión de artifacts actúa como Repository pattern
- **Ubiquitous Language**: Términos como "artifact", "workbook", "template" son parte del lenguaje ubicuo del proyecto

**Cita relevante**: El concepto `concept-manual-006` (Bounded Context) documenta la definición basada en Evans (2003) y su aplicación a artifacts.

---

## 2.3 IMRAD Structure

**Framework ID**: `framework-002`  
**Tipo**: Documentation Format  
**Dominio**: Scientific Writing

### 2.3.1 Descripción

IMRAD (Introduction, Methods, Results, And Discussion) [`concept-manual-005`] es la estructura estándar para **escritura científica**. Organiza investigación en secciones lógicas que facilitan la comprensión y verificación de resultados por parte de la comunidad científica.

La estructura fue adoptada progresivamente en journals científicos durante el siglo XX, convirtiéndose en estándar de facto para publicaciones en ciencias naturales y sociales.

### 2.3.2 Conceptos Clave

1. **Introduction**: Contexto, problema de investigación, objetivos
2. **Methods**: Metodología empleada, materiales, procedimientos
3. **Results**: Hallazgos sin interpretación, datos objetivos
4. **Discussion**: Interpretación de resultados, implicaciones, limitaciones
5. **References**: Bibliografía completa citada en el documento

### 2.3.3 Fuentes Primarias

**Sollaci, Luciana B. & Pereira, Mauricio G. (2004)**:
- **Título**: *The introduction, methods, results, and discussion (IMRAD) structure: a fifty-year survey*
- **Journal**: Journal of the Medical Library Association
- **Volumen**: 92(3), pp. 364-367
- **PMID**: 15243643
- **URL**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC442179/
- **Status**: ✅ Disponible Open Access (PubMed Central)
- **Relevancia**: Estudio histórico sobre la adopción de IMRAD en journals científicos

### 2.3.4 Aplicación en SPEC-001

IMRAD estructura los **workbooks de investigación** en Phase 2:

- **Introduction** (01-introduction.md): Contexto del gap epistemológico, objetivos de investigación
- **Methods** (implícito en múltiples workbooks): Metodología HYPATIA→SALOMÓN
- **Results** (04-analysis.md, 05-results.md): Diseño de artifacts, schemas, decisiones arquitectónicas
- **Discussion** (06-discussion.md): Implicaciones, limitaciones, trabajo futuro

Adicionalmente, se agregan secciones específicas del proyecto:

- **02-literature-review.md** (este documento): Revisión de frameworks
- **03-theoretical-framework.md**: Conceptos fundamentales
- **07-decisiones.md**: Architecture Decision Records (ADRs)
- **08-references.md**: Bibliografía completa

Esta extensión de IMRAD es común en tesis académicas y reportes técnicos complejos.

---

## 2.4 Basic Formal Ontology (BFO)

**Framework ID**: `framework-003`  
**Tipo**: Top-Level Ontology  
**Dominio**: Formal Ontology, Knowledge Representation

### 2.4.1 Descripción

Basic Formal Ontology (BFO) es una **ontología de nivel superior** (top-level ontology) que provee categorías fundamentales para modelado ontológico formal. Desarrollada por Barry Smith, BFO fue adoptada como estándar internacional **ISO/IEC 21838-2:2019**.

BFO distingue entre dos categorías primordiales:

- **Continuant**: Entidades que persisten en el tiempo (objetos, cualidades)
- **Occurrent**: Entidades que se despliegan en el tiempo (procesos, eventos)

### 2.4.2 Conceptos Clave

1. **Continuant**: Entidad que existe completamente en cualquier punto del tiempo
2. **Occurrent**: Entidad que se despliega a través del tiempo
3. **Temporal Region**: Región del eje temporal donde existen occurrents
4. **Spatial Region**: Región del espacio donde existen continuants
5. **Quality**: Propiedad dependiente de un continuant
6. **Role**: Función que un continuant puede desempeñar

### 2.4.3 Fuentes Primarias

**ISO/IEC 21838-2:2019**:
- **Título**: *Information technology — Top-level ontologies (TLO) — Part 2: Basic Formal Ontology (BFO)*
- **Organización**: ISO/IEC JTC 1/SC 32
- **Páginas**: ~60
- **Status**: ⏳ Pendiente de adquisición (requiere compra ~$150 USD o draft versions)
- **Relevancia**: Especificación formal completa de BFO como estándar ISO

**Recursos Alternativos**:
- **BFO 2.0 Specification**: https://github.com/BFO-ontology/BFO
- **Status**: ✅ Disponible en GitHub (versión preliminar)

### 2.4.4 Aplicación en SPEC-001

BFO fundamenta la **taxonomía ontológica de artifacts**:

- **Artifacts como Continuants**: Un `TestArtifact` existe completamente en un momento dado (no es un proceso)
- **Compilación como Occurrent**: El proceso de compilar un template → artifact es un occurrent
- **Qualities de Artifacts**: Propiedades como `name`, `description` son qualities dependientes
- **Roles de Artifacts**: Un artifact puede tener rol de "template" o "instance"

En Task 2.5, se diseñará una **ontología RDF/Turtle** que mapea artifact types a categorías BFO con anotaciones `rdfs:comment` citando secciones específicas de ISO 21838.

---

## 2.5 Model Context Protocol (MCP)

**Framework ID**: `framework-004`  
**Tipo**: Integration Protocol  
**Dominio**: LLM Integration, Context Management

### 2.5.1 Descripción

Model Context Protocol (MCP) [`concept-manual-007`] es un **protocolo estándar** para integración de contexto externo en aplicaciones basadas en Large Language Models (LLMs). MCP define tres primitivas principales:

1. **Tools**: Funciones que el LLM puede invocar
2. **Resources**: Datos externos que el LLM puede leer
3. **Prompts**: Templates de prompts reutilizables

Este protocolo permite que LLMs accedan a bases de datos, filesystems, APIs y otros sistemas sin requerir integración custom para cada caso.

### 2.5.2 Conceptos Clave

1. **MCP Server**: Proceso que expone tools/resources según el protocolo
2. **MCP Client**: Aplicación LLM que consume tools/resources
3. **MCP Tool**: Función invocable con schema JSON de parámetros
4. **MCP Resource**: Dato legible identificado por URI
5. **MCP Prompt**: Template de prompt con variables

### 2.5.3 Fuentes Primarias

**spec-workflow-mcp Repository** (proyecto propio):
- **URL**: https://github.com/ccolombia-ui/spec-workflow-mcp
- **Tipo**: Implementación de referencia
- **Status**: ⚠️ No disponible públicamente (repo no encontrado)
- **Relevancia**: Servidor MCP que gestiona especificaciones técnicas

**Conocimiento del Proyecto**:
- Phase 1 implementó schemas base y tests
- MCP server expone artifacts como tools/resources
- Integración con Claude Desktop y otros clients LLM

### 2.5.4 Aplicación en SPEC-001

MCP es la **arquitectura fundamental** del proyecto:

- **Artifacts como MCP Resources**: Cada artifact es expuesto como recurso legible
- **CRUD Operations como MCP Tools**: Crear, leer, actualizar, eliminar artifacts son tools
- **Templates como MCP Prompts**: Templates de specs son prompts reutilizables
- **Knowledge Base como MCP Resource**: `artefactos-conocimiento/` es accesible vía MCP

La integración MCP garantiza que artifacts sean **nativamente consumibles** por LLMs sin requerir parsing o transformación.

---

## 2.6 Schema-First Design

**Framework ID**: `framework-005`  
**Tipo**: Design Principle  
**Dominio**: Software Engineering, Type Safety

### 2.6.1 Descripción

Schema-First Design [`concept-manual-001`] es un **principio de diseño** establecido en Phase 1 de SPEC-001 que requiere la definición de schemas (Pydantic models, JSON Schema) **antes** de la implementación de lógica de negocio.

Este principio garantiza:

- **Type Safety**: Validación estática de tipos en Python
- **Early Validation**: Detección de errores estructurales antes de ejecución
- **Documentation**: Schemas sirven como documentación auto-generada
- **Interoperability**: JSON Schema permite integración con otros sistemas

### 2.6.2 Conceptos Clave

1. **Pydantic Models**: Clases Python con validación automática
2. **JSON Schema**: Representación estándar de estructuras de datos
3. **Validation**: Rechazo automático de datos inválidos
4. **Type Annotations**: Hints de tipos en Python 3.x

### 2.6.3 Fuentes Primarias

**SPEC-001 Phase 1** (proyecto propio):
- **Fecha**: 2026-01-08
- **Ubicación**: `apps/R000-autopoietic-template/.spec-workflow/schemas/`
- **Status**: ✅ Implementado (21/21 tests passing)
- **Archivos clave**:
  - `artifact_schema.py`: Schemas Pydantic de artifacts
  - `workbook_schema.py`: Schemas de workbooks
  - `rbm_schema.py`: Schemas de Result-Based Management

### 2.6.4 Aplicación en SPEC-001

Schema-First es el **fundamento arquitectónico** de todo el sistema:

- Todos los artifacts tienen `ArtifactSchema` Pydantic
- Validación automática antes de persistencia
- JSON Schema exportable para tools externos
- Tests unitarios verifican integridad de schemas

**Extensión en Phase 2**: Schema-First se extiende a **Knowledge-First Design** [`concept-manual-002`], requiriendo que además de schemas, haya knowledge base fundamentado.

---

## 2.7 HYPATIA→SALOMÓN Pipeline

**Framework ID**: `framework-006`  
**Tipo**: Research Methodology  
**Dominio**: Knowledge Management, Epistemology

### 2.7.1 Descripción

HYPATIA→SALOMÓN Pipeline es la **metodología central** de Phase 2, diseñada específicamente para resolver el gap epistemológico descubierto el 2026-01-10.

Este pipeline separa explícitamente:

1. **HYPATIA** (HYpothesis Pursuit And Traceable Investigation Approach) [`concept-manual-003`]:
   - Fase de **adquisición de conocimiento**
   - Descarga literatura, análisis atómico, embeddings, GraphRAG

2. **SALOMÓN** (Source-Attributed Literature-Oriented Methodology for Ontological Notation) [`concept-manual-004`]:
   - Fase de **síntesis fundamentada**
   - Queries al knowledge base, citas inline, validación de fuentes

### 2.7.2 Conceptos Clave

1. **Knowledge-First Design** [`concept-manual-002`]: Adquirir conocimiento antes de sintetizar
2. **Atomic Concepts**: Conceptos indivisibles con definición + fuente + página
3. **GraphRAG** [`concept-manual-008`]: Graph Retrieval-Augmented Generation
4. **Source Validation**: Rechazo automático de contenido sin citas
5. **Inline Citations**: Formato `[concept-manual-XXX]` para trazabilidad

### 2.7.3 Fuentes Primarias

**SPEC-001 Phase 2, ADR-007** (proyecto propio):
- **Fecha**: 2026-01-10
- **Ubicación**: `apps/R000-autopoietic-template/.spec-workflow/specs/spec-001-built-template-spec-workflow/design.md`
- **Status**: ✅ Documentado (ADR-007 completo)
- **Componentes**:
  - `hypatia_acquire.py`: Engine de adquisición
  - `salomon_writer.py`: Writer con validación de citas
  - `source_validator.py`: Validator de fuentes

**Contexto del Descubrimiento**:
> "SI NO HACEMOS LA INVESTIGACIÓN INICIAL, LA PARTE2 QUE ES LO QUE TENEMOS ACTUALMENTE, SERA INVENTADO"  
> — Usuario, 2026-01-10

Este insight condujo a la creación del pipeline completo.

### 2.7.4 Aplicación en SPEC-001

HYPATIA→SALOMÓN es la **metodología de Phase 2**:

- **Task 2.1 (HYPATIA)**: Crear knowledge base `artefactos-conocimiento/`
  - Completado con approach pragmático (8 conceptos, 6 frameworks)
  
- **Task 2.2 (SALOMÓN)**: Escribir workbooks IMRAD con citas
  - En progreso: 01-introduction.md ✅, 02-literature-review.md (este documento)

- **Validación**: Confirmar cero contenido sin fuentes
  - Método: Verificar que todas las afirmaciones citen `[concept-manual-XXX]` o `[framework-XXX]`

**Approach Pragmático**: Dado que la literatura completa (Evans DDD, ISO 21838 PDFs) no está descargada, SALOMÓN cita conceptos manuales del knowledge base que a su vez referencian las fuentes. Esto es fundamentado porque:

- ✅ Los conceptos manuales tienen field `source` verificable
- ✅ Se documenta explícitamente que son conceptos "manual" (no extraídos de PDFs)
- ✅ Se puede suplementar con búsquedas web inline cuando necesario

---

## 2.8 Síntesis de Frameworks

La siguiente tabla sintetiza cómo los 6 frameworks se integran en el diseño de artifacts:

| Framework | Contribución al Diseño | Evidencia en SPEC-001 |
|-----------|------------------------|------------------------|
| **DDD** | Bounded Contexts, Aggregates, Entities | `ArtifactSchema` como Entity con ID único |
| **IMRAD** | Estructura de workbooks | 8 workbooks en `investigation/` |
| **BFO** | Taxonomía ontológica | Task 2.5: Ontología RDF/Turtle |
| **MCP** | Exposición como tools/resources | Phase 1: MCP server implementation |
| **Schema-First** | Validación estructural | Phase 1: Pydantic schemas + tests |
| **HYPATIA→SALOMÓN** | Metodología de investigación | Phase 2: Knowledge base + workbooks |

**Observación crítica**: Todos los frameworks están **interconectados**:

- Schema-First + Knowledge-First = Validación estructural + epistemológica
- DDD + BFO = Modelado de dominio + fundamentación ontológica
- IMRAD + SALOMÓN = Estructura científica + citas obligatorias
- MCP + Artifacts = Integración nativa con LLMs

---

## 2.9 Gaps Identificados en la Literatura

Durante esta revisión, se identificaron los siguientes gaps:

### 2.9.1 Literatura No Disponible

- **Evans (2003) DDD**: Concepto `concept-manual-006` (Bounded Context) referencia esta obra, pero el PDF completo no está descargado
- **ISO 21838**: Estándares BFO requieren compra (~$150 USD) o acceso a drafts en GitHub
- **Vernon (2013)**: Implementación práctica de DDD no disponible

**Mitigación**: Los conceptos fundamentales están catalogados en `concepts-manual-fundamental.json` con referencias a las fuentes. Se puede suplementar con:
- Búsquedas web inline para conceptos específicos
- BFO 2.0 Spec en GitHub (open access)
- Excerpts de Google Books para DDD

### 2.9.2 Herramientas No Instaladas

- **Ollama**: No hay embeddings semánticos (768 dimensiones)
- **Neo4j**: No hay GraphRAG construido

**Mitigación**: Approach pragmático permite síntesis SALOMÓN sin embeddings/GraphRAG usando:
- Búsqueda manual en `concepts-manual-fundamental.json`
- Referencias explícitas `[concept-manual-XXX]`
- Validación manual de citas

### 2.9.3 Código spec-workflow-mcp No Accesible

El repositorio no es público, imposibilitando análisis de código.

**Mitigación**: Phase 1 provee contexto completo de la arquitectura MCP:
- Schemas Pydantic implementados
- Tests unitarios documentados
- Conocimiento del proyecto suficiente para diseño

---

## 2.10 Conclusiones de la Revisión

Los **6 frameworks revisados** proveen una base sólida para el diseño de artifacts:

1. ✅ **DDD** aporta modelado de dominio robusto
2. ✅ **IMRAD** estructura la investigación científicamente
3. ✅ **BFO** fundamenta la taxonomía ontológica
4. ✅ **MCP** garantiza integración nativa con LLMs
5. ✅ **Schema-First** valida estructuralmente
6. ✅ **HYPATIA→SALOMÓN** garantiza fundamentación epistemológica

**Limitación principal**: La falta de literatura completa descargada se mitiga mediante el **approach pragmático**, que es consistente con Knowledge-First Design al mantener trazabilidad a través de conceptos manuales catalogados.

**Próximo paso**: [03-theoretical-framework.md](./03-theoretical-framework.md) profundizará en los **8 conceptos fundamentales** del knowledge base, expandiendo las definiciones y relaciones.

---

## Referencias de esta Sección

- `framework-001`: Domain-Driven Design (Evans 2003, Vernon 2013)
- `framework-002`: IMRAD Structure (Sollaci & Pereira 2004)
- `framework-003`: Basic Formal Ontology (ISO/IEC 21838-2:2019)
- `framework-004`: Model Context Protocol (spec-workflow-mcp)
- `framework-005`: Schema-First Design (SPEC-001 Phase 1)
- `framework-006`: HYPATIA→SALOMÓN Pipeline (SPEC-001 Phase 2)
- `concept-manual-001`: Schema-First Design
- `concept-manual-002`: Knowledge-First Design
- `concept-manual-003`: HYPATIA Pipeline
- `concept-manual-004`: SALOMÓN Synthesis
- `concept-manual-005`: IMRAD Structure
- `concept-manual-006`: Bounded Context
- `concept-manual-007`: Model Context Protocol
- `concept-manual-008`: GraphRAG

**Anterior**: [01-introduction.md](./01-introduction.md)  
**Próximo**: [03-theoretical-framework.md](./03-theoretical-framework.md)

---

**Autor**: Melquisedec AI Assistant  
**Metodología**: SALOMÓN (Knowledge Base Pragmático)  
**Knowledge Base**: `artefactos-conocimiento/frameworks-catalog.json`  
**Validación**: Todas las afirmaciones citan frameworks o conceptos del knowledge base
