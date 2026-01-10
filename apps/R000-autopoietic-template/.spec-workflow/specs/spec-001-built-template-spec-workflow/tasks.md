# SPEC-001: Built Template spec-workflow - Implementation Tasks

## Overview

Este documento desglosa la implementación de SPEC-001 en tareas específicas y medibles compatible con spec-workflow-mcp.

**Total Estimado**: 5.5 semanas (110-130 horas de desarrollo)

- Phase 1: Base Infrastructure - 15 horas ✅ COMPLETADO
- Phase 2: Research Foundation (HYPATIA→SALOMÓN) - 34 horas (4.25 días) - **NUEVA FASE REESTRUCTURADA**
- Phase 3: Template System - 17 horas
- Phase 4: Compilation Pipeline - 18 horas
- Phase 5: Validation & Quality - 14 horas
- Phase 6: Integration & Deployment - 10 horas
- Phase 7: Documentation & Testing - 20 horas

**Note**: Phase 2 implementa pipeline HYPATIA→SALOMÓN: primero adquirir conocimiento de dominio (literatura, análisis atómico, GraphRAG), luego sintetizar en IMRAD workbooks. Esto previene "invención" de contenido sin fundamento epistemológico - todo debe ser rastreable a fuentes reales.

**References:**

- [Requirements](./requirements.md) - Requisitos funcionales y no funcionales
- [Design](./design.md) - Arquitectura y decisiones de diseño
- [Tech Steering](../../steering/tech.md) - Stack técnico (si existe)

---

## Tasks

### 1. Base Infrastructure

- [X] 1.1. Crear Schema JSON-LD Keter-Doc

  - **File**: `packages/core-mcp/schemas/keter-doc-protocol-v1.0.0.jsonld`
  - **Requirements**: REQ-001-01
  - **Estimación**: 3 horas
  - **Prioridad**: 🔴 ALTA
  - **Subtareas**:
    - Definir @context con vocabularios (Dublin Core, FOAF, Schema.org)
    - Definir términos de ontología MELQUISEDEC (P1-P10, 5 Rostros)
    - Definir tipos de documentos (@type: ResearchSpecification, etc.)
    - Agregar validación de URNs (pattern: urn:melquisedec:*)
    - Escribir schema JSON Schema Draft 7
  - **Validación**:
    ```bash
    npm install -g jsonld-cli
    jsonld validate keter-doc-protocol-v1.0.0.jsonld
    ```
  - **_Prompt**: Role: Schema Architect | Task: Create JSON-LD schema v1.0.0 with complete MELQUISEDEC ontology (10 principles, 5 Rostros), Dublin Core compliance, and URN validation patterns | Restrictions: Must validate against JSON-LD 1.1 spec, include all metadata fields from requirements.md REQ-001-01 | Success: Schema validates, includes all required vocabularies, URN patterns work, dates require ISO8601 format
- [X] 1.2. Crear Template Base daath-zen-base.md

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/daath-zen-base.md`
  - **Requirements**: REQ-002-01
  - **Estimación**: 4 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 1.1
  - **Subtareas**:
    - Crear frontmatter YAML con HKM header
    - Agregar bloque JSON-LD metadata
    - Crear tabla de metadatos Markdown
    - Agregar sección Overview con placeholder
    - Agregar sección Principios Aplicados
    - Agregar footer de compilación (auto-generated)
  - **_Prompt**: Role: Template Designer | Task: Create base template with HKM header, JSON-LD metadata block, metadata table, Overview section, Principios section, and compilation footer | Restrictions: All placeholders must be documented, format must be valid Markdown, footer must warn against manual editing | Success: Template validates with markdownlint, all placeholders defined, compilation metadata present
- [X] 1.3. Crear Configuración de Herencia config.yaml-ld

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/config.yaml-ld`
  - **Requirements**: REQ-002-02
  - **Estimación**: 3 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 1.2
  - **Subtareas**:
    - Definir @context JSON-LD
    - Definir template base con secciones
    - Definir 6 variantes (requirements, design, tasks, product, tech, structure)
    - Configurar secciones adicionales por variante
    - Configurar source patterns (workbook paths)
  - **Validación**:
    ```bash
    yamllint config.yaml-ld
    python -c "import yaml; print(yaml.safe_load(open('config.yaml-ld')))"
    ```
  - **_Prompt**: Role: Configuration Engineer | Task: Define template hierarchy in YAML-LD format with base template and 6 variants extending it, include section definitions and workbook path patterns | Restrictions: Valid YAML syntax, all 6 variants must extend base, path patterns use glob syntax | Success: YAML validates, base points to correct file, all variants defined with correct inheritance, path patterns work
- [X] 1.4. Implementar TemplateHierarchy Class

  - **File**: `packages/daath-toolkit/templates/template_hierarchy.py`, `packages/daath-toolkit/templates/__init__.py`, `tests/test_template_hierarchy.py`
  - **Requirements**: REQ-002-01, REQ-002-02
  - **Estimación**: 5 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 1.3
  - **Subtareas**:
    - Implementar `__init__(config_path)` para cargar config
    - Implementar `load_template(variant)` con merge lógica
    - Implementar `_merge_templates(base, variant, config)`
    - Implementar cache LRU para templates cargados
    - Escribir 5 tests unitarios
  - **Validación**:
    ```bash
    pytest tests/test_template_hierarchy.py -v --cov
    mypy packages/daath-toolkit/templates/template_hierarchy.py
    ```
  - **_Prompt**: Role: Python Developer | Task: Implement TemplateHierarchy class that loads config.yaml-ld, resolves template inheritance (base + variant merge), implements LRU cache, and includes complete type hints | Restrictions: Must use Python 3.10+, cache should improve performance, all public methods must have docstrings | Success: Loads config without errors, resolves inheritance correctly, cache works, 5+ unit tests pass with >80% coverage, mypy passes with no errors

### 2. Research Foundation (HYPATIA→SALOMÓN Pipeline)

**Objetivo**: Pipeline de dos fases para fundamentar artefactos en conocimiento de dominio REAL. **HYPATIA** (Rostro de Investigación) adquiere conocimiento, **SALOMÓN** (Rostro de Síntesis) lo sintetiza en artefactos.

**Metodología**:
1. **Phase 2.1 - HYPATIA**: Knowledge Acquisition → Literatura, análisis atómico, embeddings, GraphRAG
2. **Phase 2.2-2.6 - SALOMÓN**: IMRAD Synthesis → Sintetizar con citas a fuentes reales

**Ubicación**: `apps/R000-autopoietic-template/_melquisedec/domain/`

**Estimación Total**: 34 horas (4.25 días) - incremento de 8 horas vs versión original

---

- [ ] 2.1. HYPATIA: Knowledge Acquisition & GraphRAG Construction

  - **File**: `apps/R000-autopoietic-template/_melquisedec/domain/artefactos-conocimiento/`
  - **Requirements**: REQ-001-04a (nuevo)
  - **Estimación**: 10 horas (1.25 días)
  - **Prioridad**: 🔴 CRÍTICA (bloquea todo SALOMÓN)
  - **Dependencias**: 1.4
  - **Subtareas**:
    - **Literature Search & Download**:
      - DDD: Buscar y descargar Evans (2003) "Domain-Driven Design", Vernon (2013) "Implementing DDD"
      - ISO: Descargar ISO/IEC 21838-1:2019, ISO/IEC 21838-2:2019 (BFO)
      - IMRAD: Sollaci & Pereira (2004) "IMRAD structure paper"
      - Code: Clonar repo spec-workflow-mcp, analizar código fuente del dashboard
    - **Atomic Analysis** (extraer conceptos de fuentes):
      - Para cada PDF: extract text → semantic chunking → LLM identify concepts
      - Para code: AST parsing → identify patterns (schemas, validators)
      - Crear markdown por concepto en `concepts/` con definición + fuente
      - Documentar frameworks en `frameworks/` (DDD strategic, DDD tactical, IMRAD, RBM)
    - **Semantic Chunking & Embeddings**:
      - Chunk literatura con LangChain RecursiveCharacterTextSplitter (512 tokens)
      - Generate embeddings con Ollama (model: nomic-embed-text, dim: 768)
      - Store embeddings en `embeddings/literature-chunks-embeddings.json`
    - **GraphRAG Construction** (Neo4j):
      - Diseñar schema: (Concept)-[:PART_OF]->(Framework), (Concept)-[:CITED_IN]->(Source), (Concept)-[:RELATES_TO]->(Artifact)
      - Ingestar conceptos a Neo4j con source attribution
      - Crear relaciones semánticas entre conceptos
      - Implementar queries de retrieval (semantic search, concept traversal)
  - **Entregables**:
    - `artefactos-conocimiento/literature/` - 10+ fuentes organizadas por categoría (ddd/, iso/, imrad/, spec-workflow-mcp/)
    - `artefactos-conocimiento/concepts/` - 50+ definiciones atómicas en markdown
    - `artefactos-conocimiento/frameworks/` - 5+ frameworks documentados
    - `artefactos-conocimiento/embeddings/` - Vectors de todos los chunks literarios
    - `artefactos-conocimiento/graphs/schema.cypher` - Schema de Neo4j
    - `artefactos-conocimiento/graphs/ingestion-queries.cypher` - Scripts de ingesta
    - `artefactos-conocimiento/graphs/semantic-queries.cypher` - Queries de ejemplo
    - `artefactos-conocimiento/README.md` - Guía de uso del knowledge base
  - **Validación**:
    - [ ] 10+ literatura sources descargadas y catalogadas en literature/
    - [ ] 50+ conceptos atómicos extraídos con definiciones claras
    - [ ] Embeddings generados para todos los chunks (verificar con similarity search test)
    - [ ] GraphRAG operativo en Neo4j (test con 5 queries de ejemplo)
    - [ ] Semantic search funciona (top-k retrieval <100ms)
    - [ ] README documenta cómo consultar knowledge base
  - **_Prompt**: Role: HYPATIA - Research Investigator + Knowledge Engineer | Task: Conduct comprehensive knowledge acquisition for spec-workflow-mcp domain by: 1) Searching and downloading key literature (DDD books via Semantic Scholar/Z-Library, ISO standards from official sources, IMRAD papers from PubMed, spec-workflow-mcp repo from GitHub), 2) Performing atomic analysis to extract 50+ core concepts with LLM (for each source: extract text → semantic chunking → identify atomic concepts → save as markdown in concepts/ with definition, source citation, related concepts), 3) Creating semantic chunks with embeddings using Ollama nomic-embed-text model (chunk size 512, overlap 50), 4) Constructing GraphRAG in Neo4j with concept relationships (schema: Concept nodes with PART_OF Framework, CITED_IN Source, RELATES_TO Artifact edges), 5) Implementing retrieval patterns for semantic search | Tools: Semantic Scholar API for papers, GitHub API for repo clone, PyPDF2/pdfplumber for text extraction, LangChain SemanticChunker, Ollama Python client, Neo4j Python driver | Deliverables: Complete artefactos-conocimiento/ folder with literature/ (10+ sources), concepts/ (50+ atomic definitions), frameworks/ (5+ documented), embeddings/ (all chunk vectors), graphs/ (Neo4j schema + queries), README.md (usage guide) | Restrictions: MUST cite ALL sources with page/line numbers, NO invented concepts without source, embeddings MUST use nomic-embed-text model, Neo4j schema MUST support semantic queries, all concepts MUST be traceable to source | Success Criteria: 10+ literature sources downloaded and organized, 50+ atomic concepts extracted with clear definitions and sources, embeddings generated for all chunks and searchable, GraphRAG operational with 5 test queries working (<100ms latency), semantic search retrieves relevant concepts with >0.8 similarity, README provides clear instructions for querying knowledge base

---

- [ ] 2.2. SALOMÓN: IMRAD Investigation (Fundamentada en Knowledge Base)

  - **File**: `apps/R000-autopoietic-template/_melquisedec/domain/workbooks/spec-workflow-artifacts-investigation/`
  - **Requirements**: REQ-001-04b (renombrado)
  - **Estimación**: 8 horas (1 día)
  - **Prioridad**: 🔴 CRÍTICA
  - **Dependencias**: 2.1 (HYPATIA knowledge base DEBE estar completo)
  - **Subtareas**:
    - **01-introduction.md**: Query GraphRAG por conceptos relacionados a artifacts + semantic search para contexto
    - **02-methods.md**: Citar frameworks/ para metodologías (DDD, IMRAD) usadas en investigación
    - **03-results.md**: Sintetizar hallazgos desde atomic-analysis/ de spec-workflow-mcp code + literature/
    - **04-analysis.md**: Use GraphRAG para encontrar patrones conceptuales + embeddings para similarity
    - **05-discussion.md**: Synthesize estrategias desde múltiples fuentes en literature/
    - **06-conclusions.md**: Decisiones fundamentadas en evidencia del knowledge base
    - **07-decisiones.md**: ← **NUEVO** - ADRs con justificación completa en literature/ y concepts/
    - **08-references.md**: Bibliografía completa con todos los sources citados
  - **Entregables**:
    - `01-introduction.md` - Con citas a concepts/ (ej: "According to [ddd-bounded-context](../artefactos-conocimiento/concepts/ddd-bounded-context.md)...")
    - `02-methods.md` - Con referencias a frameworks/ (ej: "Following DDD Strategic Design [1]...")
    - `03-results.md` - Con links a atomic-analysis/ (ej: "Dashboard code analysis shows [2]...")
    - `04-analysis.md` - Documentar GraphRAG queries usadas (ej: "MATCH (c:Concept)-[:RELATES_TO]->(a:Artifact)...")
    - `05-discussion.md` - Síntesis de múltiples fuentes con attribution
    - `06-conclusions.md` - Hallazgos validados contra knowledge base
    - **07-decisiones.md** - ADRs fundamentados (ej: "ADR-001: Use DDD Bounded Contexts - Based on Evans (2003, p.345)...")
    - `08-references.md` - Bibliografía COMPLETA en formato académico
  - **Validación**:
    - [ ] Cada claim tiene citation a artefactos-conocimiento/ (zero "based on my understanding")
    - [ ] **07-decisiones.md existe y contiene ADRs fundamentados con sources**
    - [ ] GraphRAG queries documentadas en 04-analysis.md
    - [ ] Semantic search usage logged (qué queries, qué resultados)
    - [ ] Validator automático confirma zero unsourced claims
    - [ ] 08-references.md contiene ALL sources citados en workbooks
  - **_Prompt**: Role: SALOMÓN - Synthesis Architect | Task: Conduct IMRAD investigation of spec-workflow-mcp artifacts using HYPATIA knowledge base (from task 2.1), synthesize findings with COMPLETE source attribution ensuring ZERO invented content | Methodology: For each IMRAD section: 1) Query GraphRAG for relevant concepts (MATCH queries on Neo4j), 2) Perform semantic search in embeddings for supporting evidence (Ollama similarity search), 3) Cite atomic-analysis files from literature/spec-workflow-mcp/, 4) Synthesize findings with inline citations [concept-name], 5) Document GraphRAG queries used, 6) Create NEW section 07-decisiones.md with fundamented ADRs (each ADR MUST cite literature source with page number), 7) Generate complete bibliography in 08-references.md | Input Required: artefactos-conocimiento/ knowledge base from task 2.1 MUST be complete | Restrictions: EVERY claim MUST cite source (literature/X, concepts/Y, atomic-analysis/Z), MUST create 07-decisiones.md with ADRs citing page numbers, NO speculation without evidence, NO "based on my understanding" phrases, USE GraphRAG for discovery not invention, DOCUMENT all queries in 04-analysis.md | Deliverables: 8 IMRAD workbooks (01-08) with complete source attribution, 07-decisiones.md with fundamented ADRs, GraphRAG query log in 04-analysis.md, semantic search trace, 08-references.md with academic bibliography | Success Criteria: All 8 workbooks completed with proper IMRAD structure, 07-decisiones.md contains 5+ ADRs each citing specific literature sources with page numbers, every statement has verifiable citation, GraphRAG queries documented and reproducible, semantic search usage traced, automated validator confirms zero unsourced claims, bibliography is complete and properly formatted

---

- [ ] 2.3. SALOMÓN: Mapeo RBM → Artefactos (Domain Model Fundamentado)

  - **File**: `apps/R000-autopoietic-template/_melquisedec/domain/models/rbm-artifacts-mapping.md`
  - **Requirements**: REQ-001-05
  - **Estimación**: 4 horas (0.5 día)
  - **Prioridad**: 🔴 CRÍTICA
  - **Dependencias**: 2.2 (IMRAD workbooks)
  - **Subtareas**:
    - Query concepts/ para definiciones de RBM (Resultado Final, Resultado Intermedio, Resultado Inmediato)
    - Mapear RF → producto.md citando concepts/rbm-resultado-final.md
    - Mapear RI → requirements.md citando DDD bounded contexts
    - Mapear Rinm → design.md usando concepts/ddd-aggregate.md
    - Crear diagrama C4 Level 2 (Container) del modelo
    - Identificar bounded contexts por nivel RBM con citas a Evans (2003)
  - **Entregables**:
    - `rbm-artifacts-mapping.md` - Mapeo completo con citations
    - Diagrama Mermaid de RBM chain embedded
    - Bounded contexts table con references
  - **Validación**:
    - [ ] Cada mapeo cita concept relevante en artefactos-conocimiento/
    - [ ] Diagrama C4 muestra bounded contexts claramente
    - [ ] Citas a Evans (2003) para DDD patterns
  - **_Prompt**: Role: SALOMÓN - Domain Modeler | Task: Create formal RBM→Artifacts mapping using concepts from HYPATIA knowledge base, query concepts/ for RBM definitions, map each RBM level to artifacts with citations, create C4 diagram, identify bounded contexts per RBM level citing Evans (2003) | Restrictions: MUST cite concepts/ for all RBM terms, MUST reference DDD literature for bounded context definitions, diagrams MUST be embedded (Mermaid/PlantUML), zero speculation | Success: Complete mapping with all citations traceable, C4 diagram clear, bounded contexts defined with literature references

---

- [ ] 2.4. SALOMÓN: Prototipo Workbook Fundamentado

  - **File**: `apps/R000-autopoietic-template/_melquisedec/domain/workbooks/spec-001-prototype/`
  - **Requirements**: REQ-001-06
  - **Estimación**: 8 horas (1 día)
  - **Prioridad**: 🟡 ALTA
  - **Dependencias**: 2.3
  - **Subtareas**:
    - Crear workbook prototipo para SPEC-001 con estructura RBM
    - Cada producto (PROD-XXX.md) DEBE citar artefactos-conocimiento/
    - Implementar compiler/ script que valida sources antes de compilar
    - Script DEBE verificar que cada claim tiene citation
  - **Entregables**:
    - Workbook completo con source attribution
    - `compiler/compile.py` - Con source validation
    - `compiler/tests/test_source_validation.py` - Tests de validator
  - **Validación**:
    - [ ] Cada PROD-XXX.md cita sources
    - [ ] Compiler valida sources antes de output
    - [ ] Tests de validation pass
  - **_Prompt**: Role: SALOMÓN - Workbook Architect | Task: Create prototype RBM workbook for SPEC-001 where EVERY product cites artefactos-conocimiento/, implement compiler with source validation that fails if unsourced claims detected | Restrictions: NO product without citations, compiler MUST validate sources, tests MUST verify validation | Success: Workbook demonstrates knowledge-driven approach, compilation validates sources, tests confirm validation works

---

- [ ] 2.5. SALOMÓN: Ontología ISO/IEC 21838 (Alineada con ISO Real)

  - **File**: `apps/R000-autopoietic-template/_melquisedec/domain/ontologies/spec-workflow-ontology.ttl`
  - **Requirements**: REQ-001-07
  - **Estimación**: 4 horas (0.5 día)
  - **Prioridad**: 🟡 ALTA
  - **Dependencias**: 2.2
  - **Subtareas**:
    - Usar ISO specs descargados en literature/iso-standards/
    - Alinear con BFO (Basic Formal Ontology) según ISO/IEC 21838-2
    - Cada clase DEBE citar ISO spec con section number
    - Validar con reasoner (HermiT o Pellet)
  - **Entregables**:
    - `spec-workflow-ontology.ttl` - Con comments citando ISO sections
    - `ontology-validation-report.md` - Reasoner output
  - **Validación**:
    - [ ] Cada clase tiene rdfs:comment citando ISO spec
    - [ ] Reasoner valida sin errores
    - [ ] Alineación con BFO verificada
  - **_Prompt**: Role: SALOMÓN - Ontology Engineer | Task: Create ISO/IEC 21838 compliant ontology using downloaded ISO specs from literature/iso-standards/, align with BFO per ISO/IEC 21838-2, cite ISO sections in rdfs:comment for each class, validate with reasoner | Restrictions: MUST cite ISO spec sections, MUST align with BFO, MUST validate with reasoner, NO invented ontology concepts | Success: Ontology cites ISO sections, reasoner validates, BFO alignment clear

---

- [ ] 2.6. SALOMÓN: Actualización de Templates con Trazabilidad

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/daath-zen-base.md` (v1.1)
  - **Requirements**: REQ-001-08
  - **Estimación**: 2 horas (0.25 día)
  - **Prioridad**: 🟡 MEDIA
  - **Dependencias**: 2.1-2.5
  - **Subtareas**:
    - Agregar sección "🔬 Knowledge Sources" que referencia artefactos-conocimiento/
    - Placeholders: {{WORKBOOK_NAME}}, {{BOUNDED_CONTEXTS}}, {{ONTOLOGY_CLASSES}}
    - Actualizar TemplateValidator para verificar citations
  - **Entregables**:
    - Templates v1.1 con Knowledge Sources section
    - Validator updated con source checking
  - **Validación**:
    - [ ] Templates incluyen Knowledge Sources section
    - [ ] Validator detecta missing citations
    - [ ] Tests verify citation validation
  - **_Prompt**: Role: SALOMÓN - Template Engineer | Task: Update templates to include "Knowledge Sources" section pointing to artefactos-conocimiento/, add placeholders for workbook/BC/ontology references, update TemplateValidator to check citations | Restrictions: Templates MUST enforce citations, validator MUST detect unsourced content | Success: Templates have Knowledge Sources, validator works, tests pass

---

### 3. Template System

- [ ] 3.1. Crear Template daath-zen-requirements.md

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/daath-zen-requirements.md`
  - **Requirements**: REQ-003-01
  - **Estimación**: 4 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 1.4
  - **Subtareas**:
    - Extender daath-zen-base
    - Agregar sección Matriz de Coherencia (Mermaid + tabla)
    - Agregar sección User Stories
    - Agregar sección Functional Requirements
    - Agregar sección Non-Functional Requirements
    - Agregar sección Dependencies
    - Configurar placeholders para workbook refs
  - **_Prompt**: Role: Requirements Template Designer | Task: Create requirements variant extending base template, add RBM sections (Coherence Matrix with Mermaid diagram, User Stories, Functional/Non-Functional Requirements, Dependencies), configure placeholders for workbook transclusions | Restrictions: Must extend daath-zen-base, RBM format must follow design.md specifications, all workbook refs must use transclusion syntax | Success: Template extends base correctly, all RBM sections present, placeholders documented, format compatible with spec-workflow-mcp
- [ ] 3.2. Crear Template daath-zen-design.md

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/daath-zen-design.md`
  - **Requirements**: REQ-003-02
  - **Estimación**: 3 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 2.1
  - **Subtareas**:
    - Extender daath-zen-base
    - Agregar sección Architecture Overview
    - Agregar sección ADRs (Architecture Decision Records)
    - Agregar sección Component Design
    - Agregar sección Data Model
    - Agregar sección API Design
  - **_Prompt**: Role: Design Template Architect | Task: Create design variant with architecture sections (Overview, ADRs, Component Design, Data Model, API Design), support Mermaid diagrams, reference requirements via transclusion | Restrictions: Must extend daath-zen-base, ADR format must follow standard template, components must link to requirements | Success: Template complete, architecture sections documented, Mermaid diagrams supported, requirement traceability enabled
- [ ] 3.3. Crear Template daath-zen-tasks.md

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/daath-zen-tasks.md`
  - **Requirements**: REQ-003-03
  - **Estimación**: 3 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 2.2
  - **Subtareas**:
    - Extender daath-zen-base
    - Crear estructura de tasks compatible con spec-workflow-mcp
    - Agregar campos: Status, File, Requirements, _Prompt
    - Configurar placeholders para task metadata
    - Agregar sección Gantt Chart
  - **Validación**: Debe parsear correctamente con spec-workflow-mcp
  - **_Prompt**: Role: Task Template Specialist | Task: Create tasks variant with spec-workflow-mcp compatible format (checkboxes with X.Y. notation, File/Requirements/_Prompt fields), include Gantt chart section, support task dependencies | Restrictions: CRITICAL - Format must be `- [ ] X.Y. Title` with dot after number, must include all required spec-workflow-mcp fields, _Prompt must have Role|Task|Restrictions|Success structure | Success: Format parses correctly in spec-workflow-mcp, all required fields present, tasks are actionable and measurable
- [ ] 3.4. Crear Templates de Steering (product, tech, structure)

  - **File**: `apps/R000-autopoietic-template/_melquisedec/templates/daath-zen-product.md`, `daath-zen-tech.md`, `daath-zen-structure.md`
  - **Requirements**: REQ-003-04
  - **Estimación**: 3 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 2.3
  - **Subtareas**:
    - Crear template product (vision, stakeholders, success criteria)
    - Crear template tech (stack, architecture principles, standards)
    - Crear template structure (folder structure, conventions)
  - **_Prompt**: Role: Steering Document Architect | Task: Create 3 steering templates (product: vision/stakeholders/success criteria; tech: stack/principles/standards; structure: folders/conventions), each extending base template | Restrictions: Each template must be concise (<2000 words), support transclusions, follow MELQUISEDEC principles | Success: 3 templates created, each addresses its specific concern, all extend base template, compatible with spec-workflow-mcp steering docs
- [ ] 3.5. Tests de Template System

  - **File**: `tests/test_templates.py`
  - **Requirements**: REQ-006-01
  - **Estimación**: 4 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 2.4
  - **Subtareas**:
    - Test: Cada template carga correctamente
    - Test: Herencia funciona (base + variant)
    - Test: Placeholders están definidos
    - Test: Formato Markdown válido
    - Test: Templates parsean en spec-workflow-mcp
  - **Validación**:
    ```bash
    pytest tests/test_templates.py -v --cov
    ```
  - **_Prompt**: Role: QA Engineer | Task: Write comprehensive tests for template system - template loading, inheritance resolution, placeholder validation, Markdown format, spec-workflow-mcp compatibility | Restrictions: Must achieve >80% coverage, test all 6 templates, include edge cases | Success: All tests pass, coverage >80%, each template validated, format compatibility confirmed

### 4. Compilation Pipeline

- [ ] 3.1. Implementar Workbook Parser

  - **File**: `packages/daath-toolkit/compilation/workbook_parser.py`, `tests/test_workbook_parser.py`
  - **Requirements**: REQ-004-01
  - **Estimación**: 6 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 2.5
  - **Subtareas**:
    - Implementar `parse_workbook(path)` que escanea estructura
    - Implementar `extract_metadata()` de archivos YAML
    - Implementar `build_product_tree()` con RI/Rinm/REQ hierarchy
    - Implementar validación de estructura
    - Escribir 8 tests unitarios
  - **Validación**:
    ```bash
    pytest tests/test_workbook_parser.py -v --cov
    ```
  - **_Prompt**: Role: Parser Engineer | Task: Implement WorkbookParser that scans workbook directory structure, extracts metadata from YAML files, builds hierarchical product tree (RI → Rinm → REQ), validates structure against schema | Restrictions: Must handle nested directories, graceful error handling, validate required files exist | Success: Parses valid workbooks without errors, detects invalid structures, builds correct hierarchy, 8+ tests pass with >85% coverage
- [ ] 3.2. Implementar Transclusion Processor

  - **File**: `packages/daath-toolkit/compilation/transclusion_processor.py`, `tests/test_transclusion_processor.py`
  - **Requirements**: REQ-004-02
  - **Estimación**: 4 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 3.1
  - **Subtareas**:
    - Implementar `resolve_transclusions(template, workbook)`
    - Soporte para `{{include workbook.RI-001.overview}}`
    - Soporte para `{{list workbook.*.user_stories}}`
    - Implementar cache de archivos leídos
    - Manejar transclusions recursivas
    - Escribir 10 tests unitarios
  - **_Prompt**: Role: Transclusion Engine Developer | Task: Implement processor that resolves template transclusions ({{include}}, {{list}}), supports glob patterns, caches file reads, handles recursive inclusions, prevents infinite loops | Restrictions: Must support both single file and wildcard patterns, cache should be LRU-based, detect circular dependencies | Success: Resolves transclusions correctly, wildcard patterns work, recursive transclusions handled, cache improves performance, 10+ tests pass with >85% coverage
- [ ] 3.3. Implementar Coherence Matrix Builder

  - **File**: `packages/daath-toolkit/compilation/coherence_builder.py`, `tests/test_coherence_builder.py`
  - **Requirements**: REQ-004-03
  - **Estimación**: 5 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 3.2
  - **Subtareas**:
    - Implementar `build_matrix(product_tree)`
    - Generar Mermaid diagram con RI → Rinm → REQ
    - Generar tabla Markdown de trazabilidad
    - Calcular métricas (cobertura, órfanos)
    - Detectar inconsistencias
  - **_Prompt**: Role: Traceability Engineer | Task: Implement builder that generates RBM coherence matrix from product tree - creates Mermaid diagram showing RI→Rinm→REQ relationships, generates traceability table, calculates coverage metrics, detects orphan requirements | Restrictions: Mermaid syntax must be valid, table must show all relationships, metrics must be accurate | Success: Matrix generated correctly, Mermaid diagram renders, table complete, metrics accurate, detects orphans and inconsistencies
- [ ] 3.4. Implementar Template Renderer

  - **File**: `packages/daath-toolkit/compilation/template_renderer.py`, `tests/test_template_renderer.py`
  - **Requirements**: REQ-004-04
  - **Estimación**: 4 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 3.3
  - **Subtareas**:
    - Implementar `render(template, context)`
    - Soporte para placeholders {{VAR}}
    - Soporte para condicionales {{#if}}...{{/if}}
    - Soporte para loops {{#each}}...{{/each}}
    - Escape de caracteres especiales
  - **_Prompt**: Role: Template Engine Developer | Task: Implement renderer using Jinja2 or similar that replaces placeholders, handles conditionals and loops, escapes special characters, produces clean Markdown output | Restrictions: Must preserve Markdown format integrity, handle missing variables gracefully, sanitize user input | Success: Renders templates correctly, all placeholder types work, conditionals/loops functional, output is valid Markdown
- [ ] 3.5. Implementar SpecCompiler Orchestrator

  - **File**: `packages/daath-toolkit/compilation/spec_compiler.py`, `tests/test_spec_compiler.py`, `tools/compile_spec_from_workbook.py`
  - **Requirements**: REQ-004-05
  - **Estimación**: 6 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 3.4
  - **Subtareas**:
    - Implementar `compile(workbook_path, variant, output_path)`
    - Orquestar: Parser → Transclusion → Coherence → Renderer
    - Implementar error handling robusto
    - Crear CLI tool
    - Escribir 10 tests de integración
  - **Validación**:
    ```bash
    python tools/compile_spec_from_workbook.py --workbook wb-example --variant requirements --output output/req.md
    pytest tests/test_spec_compiler.py -v --cov
    ```
  - **_Prompt**: Role: Orchestration Engineer | Task: Implement SpecCompiler orchestrator that coordinates all pipeline components (Parser→Transclusion→Coherence→Renderer), provides clean CLI interface, handles errors gracefully, logs compilation steps | Restrictions: Must be idempotent, provide clear error messages, support all 6 template variants, compilation should be <5s for 50 products | Success: CLI works end-to-end, error messages are actionable, all variants compile, performance targets met, 10+ integration tests pass

### 5. Validation System

- [ ] 4.1. Implementar Keter-Doc Validator

  - **File**: `packages/daath-toolkit/validation/keter_doc_validator.py`, `tests/test_keter_doc_validator.py`
  - **Requirements**: REQ-005-01
  - **Estimación**: 5 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 3.5
  - **Subtareas**:
    - Implementar `validate(compiled_spec)` contra schema JSON-LD
    - Validar HKM header completo
    - Validar JSON-LD metadata
    - Validar URNs
    - Generar reporte de validación
  - **Validación**:
    ```bash
    pytest tests/test_keter_doc_validator.py -v --cov
    ```
  - **_Prompt**: Role: Validation Engineer | Task: Implement validator that checks compiled specs against keter-doc schema - validates HKM header completeness, JSON-LD metadata structure, URN formats, required fields presence, generates detailed validation report | Restrictions: Must validate against JSON-LD 1.1 spec, error messages must be specific and actionable, validation should be <500ms | Success: Detects all schema violations, error messages are clear, valid specs pass, invalid specs fail with actionable feedback, performance <500ms
- [ ] 4.2. Implementar RBM Coherence Validator

  - **File**: `packages/daath-toolkit/validation/rbm_validator.py`, `tests/test_rbm_validator.py`
  - **Requirements**: REQ-005-02
  - **Estimación**: 4 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 4.1
  - **Subtareas**:
    - Implementar `validate_coherence(matrix)`
    - Detectar requisitos órfanos (sin RI)
    - Detectar RI sin requisitos
    - Validar métricas de cobertura
    - Generar reporte de coherencia
  - **_Prompt**: Role: Coherence Analyst | Task: Implement validator that analyzes RBM coherence matrix - detects orphan requirements without parent RI, identifies RI without requirements, validates coverage metrics meet thresholds, generates coherence report | Restrictions: Must check bidirectional relationships, coverage thresholds configurable, report must highlight issues clearly | Success: Detects all coherence issues, orphans identified, coverage calculated correctly, report is actionable, validation <1s
- [ ] 4.3. Implementar Neo4j Sync Validator (Opcional)

  - **File**: `packages/daath-toolkit/validation/neo4j_validator.py`, `tests/test_neo4j_validator.py`
  - **Requirements**: REQ-005-03
  - **Estimación**: 4 horas
  - **Prioridad**: 🟡 MEDIA
  - **Dependencias**: 4.2
  - **Subtareas**:
    - Implementar `sync_to_neo4j(compiled_spec)`
    - Crear nodos para RI, Rinm, REQ
    - Crear relationships de trazabilidad
    - Validar sincronización exitosa
    - Escribir 6 tests (requiere Neo4j de prueba)
  - **_Prompt**: Role: Graph Database Engineer | Task: Implement optional validator that syncs compiled specs to Neo4j - creates nodes for RI/Rinm/REQ entities, establishes traceability relationships, validates sync success, handles connection errors gracefully | Restrictions: Must be optional (works without Neo4j), use neo4j-driver library, parameterized queries to prevent injection, graceful degradation if Neo4j unavailable | Success: Creates correct node structure, relationships accurate, sync validation works, handles errors gracefully, 6+ tests pass with Neo4j testcontainer
- [ ] 4.4. Integration Tests para Validation System

  - **File**: `tests/integration/test_validation_integration.py`
  - **Requirements**: REQ-006-01
  - **Estimación**: 2 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 4.3
  - **Subtareas**:
    - Test: Validación completa pipeline
    - Test: Detección de errores en cada validator
    - Test: Reporte consolidado de errores
  - **_Prompt**: Role: Integration Test Engineer | Task: Write integration tests that validate the complete validation pipeline - test each validator independently, test error detection capabilities, verify consolidated error reporting, ensure validators work together | Restrictions: Tests must be independent, use fixtures for test data, cover happy path and error cases | Success: All integration tests pass, error detection verified, report consolidation works, coverage >70%

### 6. Documentation & Examples

- [ ] 5.1. Crear Guía de Uso de Templates

  - **File**: `apps/R000-autopoietic-template/_melquisedec/docs/GUIA-TEMPLATES.md`
  - **Requirements**: REQ-007-01
  - **Estimación**: 3 horas
  - **Prioridad**: 🟡 MEDIA
  - **Dependencias**: 4.4
  - **Subtareas**:
    - Explicar jerarquía de templates
    - Documentar placeholders disponibles
    - Mostrar ejemplos de uso
    - Explicar herencia y customización
    - Troubleshooting común
  - **_Prompt**: Role: Technical Writer | Task: Create comprehensive template usage guide - explain template hierarchy (base + variants), document all available placeholders, provide concrete usage examples, explain inheritance and customization, include troubleshooting section | Restrictions: Must be <3000 words, include code examples, diagrams if helpful, beginner-friendly language | Success: Guide is clear and complete, covers all 6 templates, examples work, troubleshooting addresses common issues
- [ ] 5.2. Crear Guía de Creación de Workbook

  - **File**: `apps/R000-autopoietic-template/_melquisedec/docs/GUIA-WORKBOOK.md`
  - **Requirements**: REQ-007-02
  - **Estimación**: 3 horas
  - **Prioridad**: 🟡 MEDIA
  - **Dependencias**: 5.1
  - **Subtareas**:
    - Explicar estructura de workbook
    - Documentar formato de archivos
    - Explicar RI → Rinm → REQ hierarchy
    - Mostrar ejemplo paso a paso
    - Best practices y anti-patterns
  - **_Prompt**: Role: Methodology Expert | Task: Create workbook creation guide - explain directory structure and file formats, document RI→Rinm→REQ hierarchy, provide step-by-step example, share best practices and common pitfalls | Restrictions: Must be <3000 words, include visual diagrams, practical examples, actionable advice | Success: Guide enables users to create valid workbooks, structure is clear, examples are complete, best practices are actionable
- [ ] 5.3. Crear Workbook de Ejemplo (Autenticación)

  - **File**: `apps/R000-autopoietic-template/020-conceive/03-workbooks/wb-rbm-example-auth/*`
  - **Requirements**: REQ-007-03
  - **Estimación**: 4 horas
  - **Prioridad**: 🟡 MEDIA
  - **Dependencias**: 5.2
  - **Subtareas**:
    - Crear estructura completa de workbook
    - Crear 2 RI (login, oauth)
    - Crear 2 Rinm por RI (email-password, google)
    - Crear 5+ REQ distribuidos
    - Agregar README explicativo
  - **Validación**:
    ```bash
    python tools/compile_spec_from_workbook.py --workbook wb-rbm-example-auth --variant requirements --output output/example-requirements.md
    ```
  - **_Prompt**: Role: Example Developer | Task: Create complete authentication workbook example with 2 RI (login, oauth), 2 Rinm each (email-password, google), 5+ requirements distributed across Rinm, README explaining the example | Restrictions: Must follow RBM methodology, be realistic (not toy example), demonstrate best practices, compile without errors | Success: Workbook compiles successfully, structure is exemplary, README is clear, demonstrates key concepts, can be used as reference

### 7. Testing & Deployment

- [ ] 6.1. Integration Tests Completos

  - **File**: `tests/integration/test_full_compilation.py`, `test_template_system_integration.py`
  - **Requirements**: REQ-006-01
  - **Estimación**: 5 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 5.3
  - **Subtareas**:
    - Test: Compilación workbook ejemplo auth
    - Test: Compilación con todos los variants
    - Test: Validación completa pipeline
    - Test: Error handling en casos edge
    - Test: Performance benchmarks
  - **Validación**:
    ```bash
    pytest tests/integration/ -v --cov --cov-report=html
    ```
  - **_Prompt**: Role: Integration Test Specialist | Task: Write comprehensive end-to-end integration tests - compile example workbook with all variants, validate full pipeline, test error handling edge cases, run performance benchmarks | Restrictions: Must achieve >80% total coverage, tests must be reproducible, use fixtures for test data, include performance assertions | Success: 12+ integration tests pass, coverage >80%, all variants compile successfully, performance targets met, edge cases handled
- [ ] 6.2. Performance Benchmarks

  - **File**: `tests/benchmarks/test_compilation_performance.py`, `test_validation_performance.py`
  - **Requirements**: REQ-006-02
  - **Estimación**: 3 horas
  - **Prioridad**: 🟡 MEDIA
  - **Dependencies**: 6.1
  - **Subtareas**:
    - Benchmark: Compilación workbook (50 productos) < 5s
    - Benchmark: Validación keter-doc < 500ms
    - Benchmark: Validación coherencia RBM < 1s
    - Benchmark: Template loading < 100ms
  - **Validación**:
    ```bash
    pytest tests/benchmarks/ -v --benchmark-only
    ```
  - **_Prompt**: Role: Performance Engineer | Task: Create benchmark suite measuring compilation time (50 products <5s), keter-doc validation (<500ms), RBM coherence validation (<1s), template loading (<100ms), generate performance report | Restrictions: Use pytest-benchmark, run on consistent hardware, document results, fail if targets not met | Success: All benchmarks pass performance targets, results documented, suite runs reliably, performance regressions detected
- [ ] 6.3. Documentation Final

  - **File**: `apps/R000-autopoietic-template/_melquisedec/README.md`, `DEPLOYMENT.md`
  - **Requirements**: REQ-007-04
  - **Estimación**: 2 horas
  - **Prioridad**: 🟡 MEDIA
  - **Dependencias**: 6.2
  - **Subtareas**:
    - Crear README principal con overview y quick start
    - Crear DEPLOYMENT con installation y configuration
    - Agregar troubleshooting section
    - Agregar links a todas las guías
  - **_Prompt**: Role: Documentation Lead | Task: Create main README with system overview, quick start guide, links to detailed guides, examples, troubleshooting; create DEPLOYMENT guide with installation steps, configuration, validation, troubleshooting | Restrictions: README must be clear and inviting, DEPLOYMENT must be step-by-step, links must work, include prerequisites | Success: README is comprehensive and clear, DEPLOYMENT steps work reliably, all links functional, troubleshooting addresses common issues
- [ ] 6.4. Package y Deployment

  - **File**: `packages/daath-toolkit/setup.py`, `pyproject.toml`, `README.md`
  - **Requirements**: REQ-008-01
  - **Estimación**: 3 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 6.3
  - **Subtareas**:
    - Crear setup.py con dependencies
    - Crear pyproject.toml para build
    - Crear package README
    - Validar package builds
    - Deploy a repo MELQUISEDEC
  - **Validación**:
    ```bash
    python -m build
    pip install -e .
    python -c "from daath_toolkit.compilation import SpecCompiler"
    ```
  - **_Prompt**: Role: Package Engineer | Task: Create Python package setup with setup.py (dependencies), pyproject.toml (build config), package README (installation, usage), validate build process, deploy to repository | Restrictions: Follow Python packaging best practices, specify exact dependency versions, README must be pip-installable, package must be importable | Success: Package builds without errors, installs cleanly, imports work, README is clear, deployed successfully
- [ ] 6.5. Validation Post-Deployment

  - **File**: None (validation checklist)
  - **Requirements**: REQ-008-02
  - **Estimación**: 2 horas
  - **Prioridad**: 🔴 ALTA
  - **Dependencias**: 6.4
  - **Checklist**:
    - Templates disponibles en path correcto
    - CLI funciona: `compile_spec_from_workbook.py --help`
    - Compilación workbook ejemplo exitosa
    - Validación pasa sin errores
    - Neo4j sync funciona (si disponible)
    - spec-workflow-mcp acepta specs compilados
  - **_Prompt**: Role: Deployment Validator | Task: Execute complete post-deployment validation checklist - verify templates are accessible, CLI works, example workbook compiles, validation passes, Neo4j sync operational (if configured), compiled specs work with spec-workflow-mcp | Restrictions: All checks must pass before declaring deployment successful, document any issues encountered, have rollback plan ready | Success: All checklist items pass, no deployment errors, system ready for production use, SPEC-002 can use templates

---

## Progress Tracking

Use spec-workflow-mcp tools to track progress:

```bash
# Check overall status
spec-status --specName spec-001-built-template-spec-workflow

# List all tasks
manage-tasks --specName spec-001-built-template-spec-workflow --action list

# Get next pending task
manage-tasks --specName spec-001-built-template-spec-workflow --action next-pending

# Update task status (via dashboard or direct edit of this file)
# - [ ] = Pending
# - [-] = In Progress
# - [x] = Completed
```

---

## Implementation Notes

### Task Status Convention

- `- [ ]` : Pending (not started)
- `- [-]` : In Progress (actively working)
- `- [x]` : Completed (done and logged)

### Logging Implementation

After completing each task, use the log-implementation tool:

```bash
log-implementation \
  --specName spec-001-built-template-spec-workflow \
  --taskId X.Y \
  --summary "Brief description of what was implemented" \
  --artifacts '{"apiEndpoints": [...], "components": [...], "functions": [...]}' \
  --filesModified "[...]" \
  --filesCreated "[...]" \
  --statistics '{"linesAdded": N, "linesRemoved": M}'
```

### Completion Criteria

**Phase 1 Complete** when tasks 1.1-1.4 are all [x] and:

- Schema validates
- Base template exists
- Config parses correctly
- TemplateHierarchy class works with tests >80% coverage

**Phase 2 Complete** when tasks 2.1-2.5 are all [x] and:

- All 6 templates created
- Inheritance works
- Tests pass with >80% coverage

**Phase 3 Complete** when tasks 3.1-3.5 are all [x] and:

- CLI compiles workbooks successfully
- Performance <5s for 50 products
- Integration tests pass

**Phase 4 Complete** when tasks 4.1-4.4 are all [x] and:

- All validators operational
- Error detection comprehensive
- Tests pass >80% coverage

**Phase 5 Complete** when tasks 5.1-5.3 are all [x] and:

- Both guides written and clear
- Example workbook compiles

**Phase 6 Complete** when tasks 6.1-6.5 are all [x] and:

- All tests pass
- Benchmarks meet targets
- Package deployed
- Post-deployment validation successful

---

## References

- [requirements.md](./requirements.md) - Functional and non-functional requirements
- [design.md](./design.md) - Architecture and design decisions
- [spec-workflow-mcp Documentation](https://github.com/pimzino/spec-workflow-mcp)

---

**Total Tasks**: 26
**Total Estimation**: 100 hours (4 semanas)
**Format**: spec-workflow-mcp compatible
**Created**: 2026-01-10
**Status**: Ready for Implementation
