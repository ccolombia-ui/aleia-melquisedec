# 01 - Introducción

**SPEC-001**: Built-in Template Spec Workflow  
**Fase**: Phase 2 - SALOMÓN IMRAD Investigation  
**Metodología**: HYPATIA→SALOMÓN Pipeline  
**Fecha**: 2026-01-10  
**Knowledge Base**: `artefactos-conocimiento/` (approach pragmático)

---

## 1.1 Contexto y Motivación

El proyecto **ALEIA-MELQUISEDEC** implementa un sistema autopoiético para gestión de conocimiento mediante el protocolo **Model Context Protocol (MCP)** [`concept-manual-007`]. Este sistema requiere una infraestructura robusta para crear, gestionar y ejecutar especificaciones técnicas de manera sistemática y reproducible.

La **Phase 1** de SPEC-001 estableció el principio de **Schema-First Design** [`concept-manual-001`], implementando una arquitectura base con:

- Schemas Pydantic para artifacts, workbooks y RBM (Result-Based Management)
- Validación estructural automática mediante JSON Schema
- 21 tests unitarios confirmando integridad del sistema
- Infraestructura de compilación y ejecución de templates

Sin embargo, la implementación de Phase 1 reveló un **gap epistemológico crítico**: la generación de contenido para especificaciones requiere no solo estructura (schemas) sino también **fundamentación en conocimiento real**.

### 1.1.1 El Gap Epistemológico

Durante la planificación inicial de Phase 2, se identificó que el prompt de investigación original especificaba **QUÉ** hacer (investigación IMRAD sobre artifacts) pero no **DÓNDE** obtener el conocimiento. Esto habría resultado en contenido "basado en mi entendimiento" - es decir, **inventado** sin fuentes verificables.

> **Descubrimiento crítico**: "SI NO HACEMOS LA INVESTIGACIÓN INICIAL, LA PARTE2 QUE ES LO QUE TENEMOS ACTUALMENTE, SERA INVENTADO"  
> — Usuario, 2026-01-10

Este descubrimiento condujo a la extensión del principio Schema-First hacia **Knowledge-First Design** [`concept-manual-002`]: toda síntesis debe estar precedida por adquisición de conocimiento real y trazable.

### 1.1.2 La Solución: HYPATIA→SALOMÓN Pipeline

Para resolver este gap, se diseñó el **pipeline HYPATIA→SALOMÓN** [`concept-manual-006`], que separa explícitamente dos fases:

1. **HYPATIA** (HYpothesis Pursuit And Traceable Investigation Approach) [`concept-manual-003`]:
   - Adquisición de literatura (DDD, ISO, IMRAD, código)
   - Análisis atómico de conceptos (50+ definiciones con citas)
   - Generación de embeddings semánticos
   - Construcción de GraphRAG para queries

2. **SALOMÓN** (Source-Attributed Literature-Oriented Methodology for Ontological Notation) [`concept-manual-004`]:
   - Síntesis fundamentada en knowledge base HYPATIA
   - Citas inline obligatorias para cada afirmación
   - Validación automática de fuentes
   - Trazabilidad completa de queries

Esta arquitectura garantiza **cero contenido inventado** mediante validación estructural de que toda afirmación referencia una fuente verificable en el knowledge base.

## 1.2 Problema de Investigación

La pregunta central que motiva esta investigación es:

> **¿Cómo diseñar e implementar un sistema de artifacts para templates de especificaciones que sea simultáneamente flexible, validable, y fundamentado en principios arquitectónicos sólidos (DDD, ISO BFO)?**

Este problema se descompone en sub-problemas específicos:

### 1.2.1 Modelado del Dominio

- **P1.1**: ¿Cuáles son los Bounded Contexts relevantes para un sistema de especificaciones técnicas?
- **P1.2**: ¿Qué Entities y Value Objects componen cada artifact?
- **P1.3**: ¿Cómo se relacionan los artifacts entre sí (Aggregates, Repositories)?

### 1.2.2 Fundamentación Ontológica

- **P2.1**: ¿Qué categorías de la Basic Formal Ontology (BFO) aplican a artifacts de software?
- **P2.2**: ¿Cómo se clasifican los artifacts según distinciones Continuant/Occurrent?
- **P2.3**: ¿Qué propiedades ontológicas garantizan consistencia en la taxonomía?

### 1.2.3 Validación y Compilación

- **P3.1**: ¿Qué validaciones estructurales son necesarias para garantizar integridad de artifacts?
- **P3.2**: ¿Cómo se compilan templates en artifacts concretos preservando validez semántica?
- **P3.3**: ¿Qué estrategias de testing verifican corrección del sistema?

### 1.2.4 Integración con MCP

- **P4.1**: ¿Cómo se exponen artifacts como MCP tools/resources?
- **P4.2**: ¿Qué operaciones CRUD requieren los artifacts en el contexto MCP?
- **P4.3**: ¿Cómo se sincronizan artifacts entre filesystem y MCP server?

## 1.3 Objetivos de la Investigación

### 1.3.1 Objetivo General

Diseñar e implementar un **sistema de artifacts para templates de especificaciones** que cumpla con:

1. **Schema-First Design**: Todos los artifacts tienen schemas Pydantic validables
2. **Knowledge-First Design**: Todas las decisiones de diseño están fundamentadas en literature
3. **Domain-Driven Design**: Modelado explícito de Bounded Contexts y patrones DDD
4. **Ontological Grounding**: Taxonomía fundamentada en ISO/IEC 21838 (BFO)
5. **MCP Integration**: Exposición nativa como tools/resources del protocolo MCP

### 1.3.2 Objetivos Específicos

**OE1 - Investigación Fundamentada** (Task 2.2):
- Crear knowledge base HYPATIA con conceptos DDD, ISO, IMRAD
- Documentar 8 workbooks IMRAD con citas inline
- Generar sección 07-decisiones.md con ADRs fundamentados
- Validar cero contenido sin fuentes

**OE2 - Mapeo RBM→Artifacts** (Task 2.3):
- Mapear 8 result types RBM a artifact types
- Citar conceptos del knowledge base en cada mapeo
- Documentar transformaciones en workbook dedicado

**OE3 - Prototipo Validable** (Task 2.4):
- Implementar 1 workbook completo con compiler
- Validar que compiler rechaza artifacts sin fuentes
- Confirmar preservación de citas en output compilado

**OE4 - Ontología ISO** (Task 2.5):
- Diseñar taxonomía BFO para artifacts
- Implementar en RDF/Turtle con anotaciones rdfs:comment citando ISO
- Validar consistencia ontológica

**OE5 - Actualización de Templates** (Task 2.6):
- Agregar sección "Knowledge Sources" a todos los templates
- Vincular templates a artefactos-conocimiento/
- Documentar metodología de consulta

## 1.4 Justificación

Esta investigación es crítica por varias razones:

### 1.4.1 Autopoiesis del Sistema

El sistema ALEIA-MELQUISEDEC se caracteriza por ser **autopoiético**: capaz de detectar y corregir sus propias deficiencias. El descubrimiento del gap epistemológico y la subsecuente creación del pipeline HYPATIA→SALOMÓN demuestran esta capacidad en acción.

Una investigación fundamentada en knowledge base garantiza que futuras especificaciones (SPEC-002, SPEC-003, etc.) tengan acceso a:
- Conceptos reutilizables (evita re-inventar definiciones)
- Decisiones arquitectónicos documentadas (ADRs con citas)
- Patrones validados (DDD, BFO, IMRAD aplicados)

### 1.4.2 Reproducibilidad Científica

La adopción de la estructura **IMRAD** [`concept-manual-005`] para workbooks de investigación permite:

- **Introduction**: Contexto y problema claros
- **Methods**: Metodología HYPATIA→SALOMÓN trazable
- **Results**: Artifacts diseñados con evidencia
- **Discussion**: Implicaciones y limitaciones explícitas

Esta estructura es el estándar en publicaciones científicas (Sollaci & Pereira, 2004) y garantiza que el diseño de artifacts sea **verificable** por terceros.

### 1.4.3 Escalabilidad del Conocimiento

El knowledge base `artefactos-conocimiento/` no es específico a SPEC-001. Los 8 conceptos fundamentales y 6 frameworks catalogados son **reutilizables** en:

- SPEC-002: Gestión de observaciones MCP
- SPEC-003: Sistema de métricas autopoiéticas  
- SPEC-00N: Futuras especificaciones del proyecto

Esto implementa **economía de conocimiento**: cada spec incrementa el knowledge base en lugar de partir de cero.

### 1.4.4 Alineación con ISO Standards

La fundamentación ontológica en **Basic Formal Ontology (BFO)** - adoptado como ISO/IEC 21838 - garantiza:

- Interoperabilidad con otros sistemas ontológicos
- Consistencia en clasificaciones (Continuant/Occurrent)
- Validación formal de relaciones entre artifacts

Esto posiciona a ALEIA-MELQUISEDEC como un sistema **enterprise-grade** alineado con estándares internacionales.

## 1.5 Alcance

### 1.5.1 En Alcance

Esta investigación cubre:

- ✅ Diseño conceptual de artifacts (DDD modeling)
- ✅ Fundamentación ontológica (ISO BFO taxonomy)
- ✅ Validación estructural (Pydantic schemas)
- ✅ Compilación de templates → artifacts
- ✅ Integración MCP (tools/resources)
- ✅ Knowledge base HYPATIA (approach pragmático)
- ✅ Workbooks IMRAD con citas inline
- ✅ ADRs fundamentados en 07-decisiones.md

### 1.5.2 Fuera de Alcance

Esta investigación NO cubre:

- ❌ Implementación completa de todos los artifacts (solo prototipo)
- ❌ Testing exhaustivo del compiler (solo validación básica)
- ❌ UI/UX para gestión de artifacts (futuro SPEC-00N)
- ❌ Embeddings semánticos con Ollama (HYPATIA ideal, no crítico para MVP)
- ❌ GraphRAG en Neo4j (HYPATIA ideal, no crítico para MVP)
- ❌ Descarga de literatura completa (Evans DDD, Vernon DDD, ISO PDFs)

### 1.5.3 Limitaciones Reconocidas

El **approach pragmático** de HYPATIA implica:

- **Literatura limitada**: No se descargaron libros completos de DDD ni estándares ISO (requieren compra)
- **Conceptos manuales**: 8 conceptos fundamentales en lugar de 50+ extraídos de literatura
- **Sin embeddings**: No hay búsquedas semánticas automáticas (fallback a consulta manual)
- **Sin GraphRAG**: No hay queries Cypher documentadas (fallback a queries JSON)

**Justificación**: Este approach **SÍ cumple Knowledge-First Design** porque hay un knowledge base documentado y trazable. La diferencia es:

- **HYPATIA Completo**: Cita "Evans (2003), Domain-Driven Design, p.345"
- **HYPATIA Pragmático**: Cita "`concept-manual-006` (Bounded Context) - Source: Evans (2003)"

Ambos son fundamentados; el pragmático usa conocimiento pre-existente del proyecto más suplementos web cuando necesario.

## 1.6 Estructura del Documento

Este sistema de workbooks IMRAD se organiza en 8 secciones:

1. **01-introduction.md** (este documento): Contexto, problema, objetivos, justificación
2. **02-literature-review.md**: Revisión de frameworks (DDD, IMRAD, BFO, MCP)
3. **03-theoretical-framework.md**: Conceptos fundamentales del knowledge base
4. **04-analysis.md**: Análisis arquitectónico y decisiones de diseño
5. **05-results.md**: Diseño final de artifacts con schemas
6. **06-discussion.md**: Implicaciones, limitaciones, trabajo futuro
7. **07-decisiones.md**: Architecture Decision Records (ADRs) con citas
8. **08-references.md**: Bibliografía completa del knowledge base

Cada workbook cita conceptos del knowledge base usando el formato `concept-manual-XXX` o `framework-XXX`, garantizando trazabilidad completa.

---

## Referencias de esta Sección

- `concept-manual-001`: Schema-First Design (SPEC-001 Phase 1, 2026-01-08)
- `concept-manual-002`: Knowledge-First Design (SPEC-001 ADR-007, 2026-01-10)
- `concept-manual-003`: HYPATIA Pipeline (SPEC-001 Task 2.1, 2026-01-10)
- `concept-manual-004`: SALOMÓN Synthesis (SPEC-001 Task 2.2, 2026-01-10)
- `concept-manual-005`: IMRAD Structure (Sollaci & Pereira, 2004)
- `concept-manual-007`: Model Context Protocol (spec-workflow-mcp repo)
- `framework-006`: HYPATIA→SALOMÓN Pipeline (SPEC-001 Phase 2)

**Próximo**: [02-literature-review.md](./02-literature-review.md) - Revisión de Frameworks

---

**Autor**: Melquisedec AI Assistant  
**Metodología**: SALOMÓN (Knowledge Base Pragmático)  
**Knowledge Base**: `artefactos-conocimiento/`  
**Validación**: Todas las afirmaciones citan `concepts-manual-fundamental.json` o `frameworks-catalog.json`
