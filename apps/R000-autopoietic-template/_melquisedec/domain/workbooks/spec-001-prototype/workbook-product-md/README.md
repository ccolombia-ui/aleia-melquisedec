# Workbook: product.md (SPEC-001 Prototype)

**Bounded Context**: Product Vision & Strategy
**Artifact Generated**: `product.md` (steering document)
**Methodology**: Scoping Review (Arksey & O'Malley Framework)

---

## 🎯 Objetivo

Este workbook investiga y sintetiza el conocimiento necesario para generar el artefacto **product.md** del framework spec-workflow-mcp. El objetivo es comprender qué debe contener un documento de producto efectivo, basado en literatura académica y frameworks de la industria.

**Research Question**: *¿Qué elementos debe contener un documento de producto (product.md) para comunicar efectivamente la visión, stakeholders, y métricas de éxito de un proyecto de software?*

---

## 📂 Estructura 1-6 Epistemológica

Este workbook sigue el flujo: **ENTRADA → PROCESO → EXTRACCIÓN → VALIDACIÓN → INGESTA → COMPILACIÓN**

### 1️⃣ `1-literature/` - ENTRADA: Fuentes Primarias

Fuentes verificables organizadas por categoría:

- **`book/`**: Libros sobre product management
  - *Inspired: How to Create Tech Products Customers Love* (Cagan, 2017)
  - *The Lean Startup* (Ries, 2011)
  - *Crossing the Chasm* (Moore, 1991)

- **`paper/`**: Papers académicos
  - Product vision papers, lean canvas methodology

- **`framework/`**: Frameworks de la industria
  - Lean Canvas (Maurya)
  - Business Model Canvas (Osterwalder)
  - Scrum Product Vision (Schwaber & Sutherland)
  - Roman Pichler's Product Vision Board

- **`library/`**: Código y ejemplos
  - spec-workflow-mcp product.md examples
  - GitHub product documentation patterns

**Principio**: *"Every claim must be traceable to source"* - NO especulación, solo conocimiento verificable.

---

### 2️⃣ `2-analysis/` - PROCESO: Análisis + Síntesis

Análisis de las fuentes con citas inline:

- **`analysis-001-product-vision-components.md`**: ¿Qué elementos conforman una visión de producto? (citando Cagan, Pichler)
- **`analysis-002-stakeholder-mapping.md`**: ¿Cómo identificar y documentar stakeholders? (citando Lean Canvas, PMI)
- **`analysis-003-success-metrics.md`**: ¿Qué métricas de éxito son relevantes? (citando OKR framework, SMART goals)
- **`discussion-product-md-structure.md`**: Síntesis de estructura óptima para product.md

**Formato**: Markdown con inline citations `[source-name]`, ej: "According to Cagan (2017) [inspired-book]..."

---

### 3️⃣ `3-atomics/` - EXTRACCIÓN: Conocimiento Atomizado

Conceptos estructurados en JSON:

- **`concept-product-vision.json`**: Definición, fuentes, relaciones
- **`concept-stakeholder.json`**: Tipos, roles, intereses
- **`concept-success-criteria.json`**: Tipos de métricas, frameworks (OKR, SMART)
- **`concept-value-proposition.json`**: Canvas, componentes

**Schema Example**:
```json
{
  "id": "concept-product-vision",
  "name": "Product Vision",
  "definition": "A clear, inspiring, long-term goal for the product...",
  "sources": [
    {"type": "book", "ref": "inspired-book", "page": 35},
    {"type": "framework", "ref": "roman-pichler-vision-board"}
  ],
  "related_concepts": ["concept-stakeholder", "concept-value-proposition"],
  "examples": ["..."]
}
```

**Principio**: *"One concept, one file"* - Granularidad atómica para reusabilidad.

---

### 4️⃣ `4-artefact/` - VALIDACIÓN: Tests, Patterns, Contracts

Tests y contratos que validan conocimiento:

- **`test-product-vision-completeness.md`**: Checklist de completitud de visión
- **`contract-product-md-schema.json`**: Contrato JSON Schema para product.md
- **`pattern-vision-template.md`**: Template pattern para sección de visión
- **`validation-rules.md`**: Reglas de validación (ej: "Vision debe ser <200 words")

**Principio**: *"Test your knowledge"* - Si no es verificable, no es conocimiento sólido.

---

### 5️⃣ `5-compiler/` - COMPILACIÓN: Builder del Artefacto

Script y template para generar `product.md` (builder que crea outputs):

#### `compile-product.py`
- Lee todos los análisis de `2-analysis/`
- Lee conceptos atomizados de `3-atomics/`
- Valida contra `4-artefact/contract-product-md-schema.json`
- Renderiza `templates/product.md.j2` con Jinja2
- Output intermediario: Documento compilado listo para ingesta en 6-outputs/

#### `templates/product.md.j2`
```jinja2
# Product Vision: {{project_name}}

## Overview
{{vision_statement}}

## Stakeholders
{% for stakeholder in stakeholders %}
- **{{stakeholder.role}}**: {{stakeholder.interest}}
{% endfor %}
```

**Principio**: *"Artifacts are compiled, not written"* - Humanos escriben atomics, compiler escribe artifacts.

---

### 6️⃣ `6-outputs/` - INGESTA: Índices Neo4j + Embeddings

Preparación para GraphRAG y semantic search (índices referenciados al artefacto compilado):

#### `cypher/`
- **`ingest-product-concepts.cypher`**: Crea nodos `(Concept:Product)` en Neo4j con relación a artifact compilado
- **`relate-product-to-requirements.cypher`**: Relaciona product concepts → requirements
- **`query-examples.cypher`**: Queries de ejemplo para semantic retrieval

#### `embeddings/`
- **`product-concepts-embeddings.json`**: Vectors de conceptos (Ollama nomic-embed-text) vinculados al artifact
- **`literature-chunks-embeddings.json`**: Vectors de chunks de literatura

**Formato Embeddings**:
```json
{
  "concept_id": "concept-product-vision",
  "artifact_ref": "product.md",
  "text": "Product Vision is a clear, inspiring, long-term goal...",
  "embedding": [0.023, -0.145, 0.678, ...],  // 768 dimensions
  "metadata": {
    "source": "inspired-book",
    "page": 35
  }
}
```

**Output final**: `.spec-workflow/steering/product.md` (artefacto spec-workflow-mcp válido)

**Principio**: *"Knowledge is queryable"* - Neo4j para graph traversal, embeddings para semantic similarity, ambos referenciando el artefacto final.
- **{{stakeholder.role}}**: {{stakeholder.interest}}
{% endfor %}

## Success Criteria
{{success_criteria}}

---
**Compiled from**: workbook-product-md/
**Sources**: {{source_count}} references
**Last Updated**: {{compilation_date}}
```

**Principio**: *"Artifacts are compiled, not written"* - DRY, single source of truth en workbook.

---

## 🔬 Metodología: Scoping Review

Seguimos el framework de Arksey & O'Malley (2005):

1. **Research Question** (↑ arriba): ¿Qué debe contener product.md según spec-workflow-mcp?
2. **Study Identification** (`1-literature/`): Buscar fuentes relevantes (spec-workflow-mcp oficial, frameworks)
3. **Study Selection** (`2-analysis/`): Analizar fuentes, extraer hallazgos
4. **Data Charting** (`3-atomics/`): Atomizar conocimiento en JSON
5. **Collating, Summarizing, Reporting** (`5-compiler/`): Sintetizar en product.md (builder)
6. **Knowledge Ingestion** (`6-outputs/`): Ingestar en Neo4j + embeddings (índices al artefacto)

**NO es IMRAD** porque no estamos probando hipótesis experimental - estamos mapeando un dominio de conocimiento existente.

---

## ✅ Validation Rules

Antes de compilar, verificar:

1. **`1-literature/` NO está vacío**: Sin sources = invención
2. **`2-analysis/` cita `1-literature/`**: No unsourced claims
3. **`3-atomics/` JSON válido**: Schema compliance
4. **`5-compiler/` valida structure**: Check antes de output
6. **`6-outputs/` referencia artefacto**: Índices vinculados al output compiladoilación
5. **`compiler/` valida structure**: Check antes de output

**Command**:
```bash
python 5-compiler/compile-product.py --validate
```

---

## 📚 Referencias Clave

### Books
- Cagan, M. (2017). *Inspired: How to Create Tech Products Customers Love*. Wiley.
- Ries, E. (2011). *The Lean Startup*. Crown Business.
- Moore, G. A. (1991). *Crossing the Chasm*. HarperBusiness.

### Frameworks
- Maurya, A. (2012). *Running Lean: Iterate from Plan A to a Plan That Works*. O'Reilly.
- Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.
- Pichler, R. (2016). *Strategize: Product Strategy and Product Roadmap Practices*. Pichler Consulting.

### Papers
- Arksey, H., & O'Malley, L. (2005). "Scoping studies: towards a methodological framework". *International Journal of Social Research Methodology*, 8(1), 19-32.

---

## 🚀 Usage

### Para investigadores (Phase 2.2):
1. Coleccionar literatura en `1-literature/` (foco: spec-workflow-mcp format)
2. Analizar en `2-analysis/` con citas
3. Atomizar en `3-atomics/` como JSON
4. Crear tests en `4-artefact/`
5. Compilar con `python 5-compiler/compile-product.py` (builder)
6. Generar índices en `6-outputs/` (Neo4j + embeddings referenciando artefacto)

### Para futuros specs (SPEC-002+):
1. Clonar este workbook como template
2. Adaptar `5-compiler/templates/product.md.j2` según necesidades
3. Reutilizar conceptos de `3-atomics/` si aplican
4. Compilar con nuevo proyecto y generar índices

---

## 📊 Status

- [x] Estructura 1-6 creada (1-literature/ → 6-outputs/, con 5-compiler/ como builder)
- [x] Literatura spec-workflow-mcp documentada (1-literature/framework/spec-workflow-mcp-product-format.md)
- [ ] Análisis completado (2-analysis/)
- [ ] Conceptos atomizados (3-atomics/)
- [ ] Tests creados (4-artefact/)
- [ ] Compiler implementado (5-compiler/)
- [ ] Índices generados (6-outputs/ Neo4j + embeddings)
- [ ] product.md compilado exitosamente

**Next**: Completar 2-analysis/ sintetizando spec-workflow-mcp + frameworks (Pichler, Maurya, Cagan)

---

**Created**: 2026-01-11
**SPEC**: SPEC-001 Built Template spec-workflow
**Task**: 2.2 SALOMÓN: Create workbook-product-md/
**Bounded Context**: Product Vision & Strategy
