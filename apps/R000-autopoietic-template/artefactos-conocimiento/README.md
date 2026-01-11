# Artefactos de Conocimiento - SPEC-001

Este directorio contiene el **knowledge base** para la implementación de SPEC-001 (Built-in Template Spec Workflow). Implementa la arquitectura **HYPATIA→SALOMÓN** que garantiza cero contenido inventado mediante fundamentación en fuentes reales.

## 📚 Estructura

```
artefactos-conocimiento/
├── literature/           # Fuentes primarias descargadas
│   ├── ddd/             # Domain-Driven Design (Evans 2003, Vernon 2013)
│   ├── iso/             # ISO/IEC 21838-1:2019, 21838-2:2019 (BFO)
│   ├── imrad/           # Papers sobre IMRAD (Sollaci & Pereira 2004)
│   └── spec-workflow-mcp/ # Código fuente del servidor MCP
├── concepts/            # 50+ conceptos atómicos con citas
├── frameworks/          # Metodologías documentadas (DDD, IMRAD, RBM, ISO BFO)
├── embeddings/          # Representaciones vectoriales (Ollama nomic-embed-text 768dim)
├── graphs/              # GraphRAG (Neo4j schema + queries)
└── README.md           # Este archivo
```

## 🔬 Metodología HYPATIA

**HYPATIA** (HYpothesis Pursuit And Traceable Investigation Approach) es la fase de **adquisición de conocimiento** que precede a toda síntesis.

### Pipeline HYPATIA

1. **Descarga de Literatura** (2h)
   - DDD: Evans (2003) "Domain-Driven Design", Vernon (2013) "Implementing DDD"
   - ISO: ISO/IEC 21838-1:2019, ISO/IEC 21838-2:2019
   - IMRAD: Sollaci & Pereira (2004), otros papers metodológicos
   - Código: Repositorio spec-workflow-mcp completo

2. **Análisis Atómico** (4h)
   - Extracción de 50+ conceptos atómicos con LLM
   - Cada concepto incluye:
     - **Definición**: Texto extraído literalmente
     - **Fuente**: Referencia bibliográfica completa
     - **Página**: Número de página exacto
     - **Relaciones**: Conceptos relacionados
   - Almacenamiento en `concepts/` como archivos JSON

3. **Generación de Embeddings** (2h)
   - Chunking semántico con LangChain (512 tokens)
   - Modelo: Ollama `nomic-embed-text` (768 dimensiones)
   - Almacenamiento en `embeddings/` como archivos `.npy`

4. **Construcción de GraphRAG** (2h)
   - Base de datos: Neo4j 5.15+
   - Schema:
     ```cypher
     (Concept)-[:PART_OF]->(Framework)
     (Concept)-[:CITED_IN]->(Source)
     (Concept)-[:RELATES_TO]->(Artifact)
     ```
   - Queries almacenadas en `graphs/queries/`

## 📖 Metodología SALOMÓN

**SALOMÓN** (Source-Attributed Literature-Oriented Methodology for Ontological Notation) es la fase de **síntesis fundamentada** que opera sobre el knowledge base HYPATIA.

### Principios SALOMÓN

1. **Consulta GraphRAG**: Todo contenido inicia con query semántica
2. **Búsqueda Vectorial**: Similaridad >0.75 en embeddings
3. **Citas Inline**: Cada afirmación cita fuente (Autor YYYY, p.NNN)
4. **Validación Automática**: `source_validator.py` rechaza contenido sin fuentes
5. **Trazabilidad Completa**: Queries documentadas en 04-analysis.md

### Output SALOMÓN

- **8 Workbooks IMRAD** con citas inline
- **07-decisiones.md**: ADRs citando fuentes específicas con páginas
- **08-references.md**: Bibliografía completa
- **Validator Report**: Confirmación de cero claims sin fuente

## 🚫 Principio: Knowledge-First Design

> **"SI NO HACEMOS LA INVESTIGACIÓN INICIAL, LA PARTE2... SERA INVENTADO"**  
> — Usuario, descubrimiento del gap epistemológico (2026-01-10)

Este knowledge base implementa el principio de **Knowledge-First Design**: la extensión de Schema-First a nivel epistemológico. Ninguna síntesis puede preceder a la adquisición de conocimiento real.

### Anti-Pattern Detectado

```
❌ SYNTHESIS WITHOUT FOUNDATION
Prompt: "Investiga sobre DDD y escribe un análisis IMRAD"
Result: LLM genera contenido "basado en mi entendimiento" → INVENTADO
```

### Pattern Correcto

```
✅ HYPATIA→SALOMÓN PIPELINE
1. HYPATIA: Descarga Evans (2003) → Extrae conceptos → Crea embeddings
2. SALOMÓN: Query GraphRAG → Encuentra "Bounded Context (Evans 2003, p.345)" → Cita
Result: Contenido fundamentado en fuentes reales → TRAZABLE
```

## 🛠️ Herramientas Requeridas

### Obligatorias

- **Ollama**: Modelo `nomic-embed-text` para embeddings
  ```bash
  ollama pull nomic-embed-text
  ```

- **Neo4j 5.15+**: Base de datos de grafos
  ```bash
  docker run -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:5.15
  ```

- **Python 3.13+**: Scripts HYPATIA
  ```bash
  pip install langchain pypdf2 pdfplumber neo4j ollama semantic-scholar
  ```

### Opcionales

- **Zotero**: Gestión de bibliografía
- **Obsidian**: Navegación de conceptos interconectados

## 📊 Métricas de Éxito

### HYPATIA Completado

- ✅ 10+ fuentes descargadas en `literature/`
- ✅ 50+ conceptos atómicos en `concepts/`
- ✅ Embeddings generados en `embeddings/`
- ✅ GraphRAG operacional (Neo4j)
- ✅ Búsqueda semántica con latencia <100ms

### SALOMÓN Completado

- ✅ 8 workbooks IMRAD con citas inline
- ✅ 07-decisiones.md con ADRs fundamentados
- ✅ 08-references.md con bibliografía completa
- ✅ Validator reporta 0 unsourced claims
- ✅ GraphRAG queries documentadas en 04-analysis.md

## 🔍 Uso del Knowledge Base

### Consultar Conceptos

```python
from hypatia_engine import HypatiaKnowledgeEngine

engine = HypatiaKnowledgeEngine("artefactos-conocimiento/")
results = engine.search_concepts("bounded context", similarity_threshold=0.8)

for concept in results:
    print(f"{concept.name}: {concept.definition}")
    print(f"  Fuente: {concept.source}, p.{concept.page}")
```

### Validar Contenido

```python
from source_validator import SourceValidator

validator = SourceValidator("artefactos-conocimiento/")
report = validator.validate_workbook("02-literature-review.md")

if report.unsourced_claims:
    for claim in report.unsourced_claims:
        print(f"❌ Claim sin fuente: {claim}")
else:
    print("✅ Todo el contenido está fundamentado")
```

## 📝 Historial

- **2026-01-10**: Creación inicial del knowledge base
- **2026-01-10**: Descubrimiento del gap epistemológico
- **2026-01-10**: Implementación de arquitectura HYPATIA→SALOMÓN

## 🎓 Referencias del Diseño

Este diseño está fundamentado en:

- **Schema-First Design**: Principio establecido en Phase 1 (SPEC-001)
- **GraphRAG**: Microsoft Research (2023) "From Local to Global"
- **Semantic Chunking**: LangChain metodología
- **BFO Ontology**: ISO/IEC 21838-2:2019
- **IMRAD Structure**: Sollaci & Pereira (2004)

---

**Mantenedor**: Melquisedec AI Assistant  
**Proyecto**: ALEIA-MELQUISEDEC (R000 Autopoietic Template)  
**Spec**: SPEC-001 (Built-in Template Spec Workflow)
