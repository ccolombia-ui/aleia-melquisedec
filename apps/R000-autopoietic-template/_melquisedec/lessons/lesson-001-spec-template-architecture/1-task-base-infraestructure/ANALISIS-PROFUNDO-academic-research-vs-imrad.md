# 🎓 Análisis Profundo: Academic Research vs IMRAD Methodology

**Fecha**: 2026-01-10  
**Contexto**: Clarificación metodológica para spec-000 y workbooks domain/  
**Autor**: GitHub Copilot (Claude Sonnet 4.5)  
**Status**: 📚 Deep Analysis (Esperando Feedback)

---

## 📋 Resumen Ejecutivo

### Problema Identificado

El usuario detectó **confusión metodológica crítica** en la propuesta:

**❌ PROPUESTA INCORRECTA**:
```
_melquisedec/domain/
└── workbooks/              # Usar IMRAD para TODO
    ├── spec-000-daath-zen-templates-analysis/
    │   ├── 01-introduction.md
    │   ├── 02-methods.md
    │   └── ...
```

**✅ PROPUESTA CORRECTA**:
```
_melquisedec/domain/
└── workbooks/              # DOS TIPOS de metodología
    ├── academic-research/  # Literatura → Análisis → Atómicos → Artifacts
    │   ├── 1-literature/
    │   ├── 2-analysis/
    │   ├── 3-atomics/
    │   ├── 4-artifacts/
    │   └── 6-outputs/
    │
    └── imrad-research/     # Análisis específico con IMRAD
        ├── 01-introduction.md
        ├── 02-methods.md
        └── ...
```

### Clarificación Clave del Usuario

**Usuario dijo**:
> "CADA WORKFLOW SE REALIZA USANDO LA METODOLOGÍA **IMRAD CUANDO ES UN ANÁLISIS**, 01-INTRODUCTION, 02-METHOD, ...  
> pero usamos la **metodología de investigación académica (revisión científica) CUANDO ESTAMOS DESCUBRIENDO UN DOMINIO DE CONOCIMIENTO**"

---

## 🔬 Parte 1: Explicación para Dummies

### ¿Qué son "amendments/"?

**Analogía Simple**: Piensa en amendments/ como **"notas al margen"** de un libro.

#### Escenario

Imaginemos que haces spec-000 (investigación inicial) y descubres que templates DAATH-ZEN necesitan 30 líneas de código.

**Escribes en tu workbook**:
```markdown
# 06-conclusion.md (spec-000)

Decisión: Template base debe tener 30 líneas máximo
```

**3 meses después**, en spec-001 (implementación), descubres que **necesitas 35 líneas** porque hay un caso especial.

**¿Qué haces?**

**OPCIÓN A (Mala)**: Editar 06-conclusion.md y cambiar "30" por "35"
- ❌ Pierdes historia: ¿Por qué cambió?
- ❌ Git blame confuso
- ❌ Futuro no sabe contexto

**OPCIÓN B (Buena - Hybrid con amendments/)**:
```markdown
# 06-conclusion.md (spec-000)

## 6. Conclusion (Original)
Decisión: Template base debe tener 30 líneas máximo

---

## 6.1 Amendment from spec-001

**Resumen**: Durante implementación, descubrimos caso especial que requiere 35 líneas.

**Ver detalles completos**: [[amendments/spec-001-amendment-template-size]]
```

**Archivo separado**:
```markdown
# amendments/spec-001-amendment-template-size.md

**Fecha**: 2026-01-15
**Spec origen**: spec-001
**Workbook afectado**: spec-000/06-conclusion

## Contexto
Durante implementación de spec-001, descubrimos que...

## Hallazgo Nuevo
Necesitamos 35 líneas (no 30) porque...

## Impacto
- Decisión original SIGUE VÁLIDA
- Solo ajuste menor (+5 líneas)

## Implementación
- [x] Actualizar template-base.yaml con 35 líneas
- [x] Documentar caso especial en README
```

**Ventajas**:
- ✅ Conclusión original preservada (historia clara)
- ✅ Cambio documentado POR SEPARADO (fácil de revisar)
- ✅ Obsidian links conectan todo ([[wikilinks]])
- ✅ Git muestra: 1 archivo original + 1 amendment nuevo

**En resumen**: amendments/ son **actualizaciones documentadas** que NO destruyen el trabajo original.

---

## 🔬 Parte 2: Dos Metodologías de Investigación

### 2.1 IMRAD: Para Análisis Específico

**Cuándo usar**: Ya sabes **QUÉ** investigar, necesitas **analizar profundamente**.

**Ejemplo**: "Quiero analizar las 6 versiones de templates DAATH-ZEN para crear template unificado"

**Estructura**:
```
workbook-imrad-templates-analysis/
├── 01-introduction.md      # Problema: 6 templates inconsistentes
├── 02-methods.md           # Metodología: Análisis comparativo línea-por-línea
├── 03-results.md           # Tabla comparativa: líneas, placeholders, metadata
├── 04-analysis.md          # Patrones comunes identificados
├── 05-discussion.md        # Implicaciones: template unificado reduce 70% código
├── 06-conclusion.md        # Decisión: Adoptar daath-zen-base.md como base
└── 07-references.md        # Links a 6 templates analizados
```

**Características IMRAD**:
- ✅ **Lineal**: Introduction → Conclusion (1 dirección)
- ✅ **Específico**: Responde pregunta concreta (¿cuál es mejor template?)
- ✅ **Validable**: Results sin interpretación, Analysis separado
- ✅ **Reproducible**: Otro investigador puede repetir Methods

**Papers científicos usan IMRAD**: Cell, Nature, Science, JAMA

---

### 2.2 Academic Research: Para Descubrir Dominio

**Cuándo usar**: NO sabes **QUÉ** existe, necesitas **explorar territorio desconocido**.

**Ejemplo**: "¿Qué frameworks, ontologías, y cypher patterns opensource existen para grafos de conocimiento?"

**Estructura (propuesta del usuario)**:
```
workbook-academic-opensource-ontologies/
├── 1-literature/           # HYPATIA busca fuentes
│   ├── book/
│   │   ├── evans-2003-ddd/
│   │   │   ├── metadata.yaml
│   │   │   ├── content.md
│   │   │   └── citations.bib
│   │   └── vernon-2013-implementing-ddd/
│   ├── paper/
│   │   ├── sollaci-2004-imrad/
│   │   └── kitchenham-2007-systematic-review/
│   ├── framework/
│   │   ├── schema-org/
│   │   ├── foaf-ontology/
│   │   └── neo4j-gds/
│   └── library/
│       ├── llamaindex/
│       └── langchain/
│
├── 2-analysis/             # SALOMON analiza literatura
│   ├── comparative-frameworks.md       # Comparación Schema.org vs FOAF
│   ├── neo4j-gds-patterns-review.md    # Análisis de patterns GDS
│   ├── embedding-models-survey.md      # Survey de modelos embeddings
│   └── recommendations.md              # Recomendaciones para adoptar
│
├── 3-atomics/              # MORPHEUS genera contenidos-atómicos
│   ├── schema-org-core-concepts.md     # Concepto: Schema.org Person
│   ├── foaf-relationship-types.md      # Concepto: FOAF knows relationship
│   ├── neo4j-pagerank-algorithm.md     # Algoritmo: PageRank en Neo4j
│   └── nomic-embed-benchmarks.md       # Benchmark: Nomic Embed 768dim
│
├── 4-artifacts/            # MORPHEUS crea artefactos
│   ├── test-schema-org-mapping.py      # Test: Mapear Person a Neo4j
│   ├── cypher-pattern-pagerank.cypher  # Pattern: PageRank query
│   ├── moc-dataset-ontology.ttl        # Mock: Ontology sample
│   └── contract-embedding-api.py       # Contract: Embedding API
│
└── 6-outputs/              # ALMA publica outputs
    ├── index-frameworks.md             # Índice de frameworks encontrados
    ├── cypher-for-ingestion.cypher     # Queries para ingestar a Neo4j
    ├── embeddings-nomic-vectors.npy    # Vectores generados
    └── README.md                       # ALMA-generated overview
```

**Características Academic Research**:
- ✅ **Exploratorio**: No sabes qué encontrarás (descubrimiento)
- ✅ **Iterativo**: 1-lit → 2-analysis → descubres más lit → repites
- ✅ **Acumulativo**: Cada fuente agrega conocimiento al knowledge base
- ✅ **Multi-formato**: Books, papers, frameworks, libraries (heterogéneo)
- ✅ **Genera atomics**: Output son contenidos-atómicos para triple persistence

**Systematic Literature Reviews usan esto**: Kitchenham & Charters (2007)

---

## 🔍 Parte 3: Mejores Prácticas de Investigación Académica

### 3.1 Systematic Literature Review (SLR) - Kitchenham & Charters (2007)

**Definición**: Metodología rigurosa para identificar, evaluar y sintetizar literatura existente sobre un tema.

**Fases**:
1. **Planning**: Definir research questions, criterios inclusión/exclusión
2. **Conducting**: Búsqueda sistemática, screening, extracción datos
3. **Reporting**: Síntesis, conclusiones, recomendaciones

**Estructura propuesta por Kitchenham**:
```
systematic-review/
├── protocol.md             # Research questions, search strategy
├── search-results.md       # Todas las fuentes encontradas
├── inclusion-criteria.md   # Criterios de selección
├── data-extraction.md      # Datos extraídos de cada fuente
├── quality-assessment.md   # Evaluación de calidad de fuentes
└── synthesis.md            # Síntesis de hallazgos
```

**Mapeo a propuesta usuario**:
```
1-literature/               = Conducting (búsqueda + extracción)
2-analysis/                 = Reporting (síntesis)
```

---

### 3.2 Zettelkasten Method - Luhmann (1992)

**Definición**: Sistema de notas atómicas interconectadas para knowledge management.

**Principios**:
1. **Atomicidad**: Cada nota = 1 idea (no más)
2. **Conectividad**: Notas se linkan entre sí (bidirectional)
3. **Emergencia**: Conocimiento emerge de conexiones

**Estructura Luhmann**:
```
zettelkasten/
├── 1a-concepto-bounded-context.md        # Nota atómica 1a
├── 1a1-ejemplo-ecommerce-context.md      # Sub-nota 1a1 (deriva de 1a)
├── 1b-concepto-ubiquitous-language.md    # Nota atómica 1b
└── 2-relacion-context-language.md        # Conecta 1a + 1b
```

**Mapeo a propuesta usuario**:
```
3-atomics/                  = Zettelkasten notes
```

**Referencia**:
- Luhmann, Niklas (1992). "Communicating with Slip Boxes"
- Ahrens, Sönke (2017). "How to Take Smart Notes"

---

### 3.3 Dublin Core Metadata - DCMI (2020)

**Definición**: Estándar ISO 15836 para metadata de recursos digitales.

**15 Core Elements**:
```yaml
---
dc:
  title: "Domain-Driven Design"                # Título
  creator: ["Eric Evans"]                      # Autor
  date: "2003"                                 # Fecha publicación
  subject: ["DDD", "Bounded Context"]          # Keywords
  description: "Book about DDD patterns"       # Resumen
  publisher: "Addison-Wesley"                  # Editorial
  type: "book"                                 # Tipo recurso
  format: "application/pdf"                    # Formato
  identifier: "ISBN:978-0321125217"            # Identificador único
  source: "https://..."                        # URL origen
  language: "en"                               # Idioma
  relation: ["implements:ISO-21838"]           # Relaciones
  coverage: "Software Architecture"            # Cobertura temática
  rights: "Copyright 2003"                     # Derechos
---
```

**Mapeo a propuesta usuario**:
```
1-literature/{type}/{id}/metadata.yaml  = Dublin Core
```

---

### 3.4 PRISMA Guidelines - Moher et al. (2009)

**Definición**: Guías para reportar systematic reviews y meta-analyses.

**Diagrama de Flujo PRISMA**:
```
Identificación:
- Papers encontrados en bases de datos: 500
- Papers encontrados en otras fuentes: 50
↓
Screening:
- Papers después de eliminar duplicados: 450
- Papers screened: 450
- Papers excluidos: 380
↓
Elegibilidad:
- Full-text articles assessed: 70
- Full-text excluded (con razones): 40
↓
Inclusión:
- Studies included in synthesis: 30
```

**Mapeo a propuesta usuario**:
```
1-literature/sources.yaml   = PRISMA flow tracking
2-analysis/review-log.md    = Inclusión/exclusión rationale
```

---

### 3.5 Grounded Theory - Glaser & Strauss (1967)

**Definición**: Metodología cualitativa para generar teoría desde datos.

**Proceso**:
1. **Open Coding**: Identificar conceptos en datos
2. **Axial Coding**: Relacionar conceptos (categorías)
3. **Selective Coding**: Integrar categorías en teoría

**Ejemplo**:
```
Open Coding (1-literature/):
- Concepto: "Bounded Context" (DDD)
- Concepto: "Namespace" (C++)
- Concepto: "Package" (Java)

Axial Coding (2-analysis/):
- Categoría: "Modularity Mechanisms"
- Relación: Bounded Context = DDD's Namespace

Selective Coding (3-atomics/):
- Teoría: "Modularity patterns map across paradigms"
```

---

## 📊 Parte 4: Comparación Metodológica Profunda

### 4.1 Tabla Comparativa

| Aspecto | IMRAD | Academic Research |
|---------|-------|-------------------|
| **Objetivo** | Analizar pregunta específica | Descubrir dominio desconocido |
| **Estructura** | Lineal (7 secciones fijas) | Iterativa (4-6 carpetas flexibles) |
| **Input** | Hipótesis clara | Research questions amplias |
| **Output** | Conclusión + decisión | Knowledge base + atomics |
| **Duración** | 2-5 días | 1-4 semanas |
| **Rostros** | SALOMON (diseña) + MORPHEUS (valida) | HYPATIA → SALOMON → MORPHEUS → ALMA |
| **Reproducibilidad** | Alta (Methods replicables) | Media (búsqueda subjetiva) |
| **Validación** | Results vs Analysis separados | Peer review + quality assessment |
| **Formato Output** | Markdown (7 archivos) | Markdown + PDF + RDF + Cypher |
| **Metodología Base** | Sollaci & Pereira (2004) | Kitchenham & Charters (2007) |

---

### 4.2 Cuándo Usar Cada Una

#### IMRAD ✅

**Casos de uso**:
1. **Análisis comparativo concreto**: "¿Cuál template DAATH-ZEN es mejor?"
2. **Validación de hipótesis**: "¿Template minimalista reduce complejidad?"
3. **Diseño fundamentado**: "¿Cómo mapear RBM a artifacts?"
4. **Decisiones arquitectónicas**: "¿Usar LlamaIndex o LangChain?"

**Indicadores**:
- Ya tienes fuentes específicas a analizar
- Pregunta tiene respuesta binaria o selección entre opciones
- Output es **diseño** o **decisión**

**Ejemplo SPEC-000**:
```
Workbook: spec-000-daath-zen-templates-analysis (IMRAD)
- Ya conocemos las 6 versiones de templates
- Pregunta: ¿Cuál estructura unificada emerge?
- Output: template-base.yaml diseñado
```

---

#### Academic Research ✅

**Casos de uso**:
1. **Exploración de dominio**: "¿Qué ontologías opensource existen?"
2. **State-of-the-art**: "¿Qué frameworks de grafos hay disponibles?"
3. **Knowledge base creation**: Construir biblioteca de conceptos
4. **Discovery research**: No sabes qué encontrarás

**Indicadores**:
- No sabes cuántas fuentes existen
- Pregunta es exploratoria ("¿Qué...?", "¿Cuáles...?")
- Output es **knowledge base** + **contenidos-atómicos**

**Ejemplo SPEC-000**:
```
Workbook: spec-000-opensource-ontologies-investigation (Academic)
- NO conocemos todas las ontologías disponibles
- Pregunta: ¿Qué frameworks podemos reutilizar?
- Output: Catálogo de ontologías + atomics + cypher patterns
```

---

## 🎯 Parte 5: Propuesta Corregida de Workbooks

### 5.1 Workbooks spec-000 (Corregidos)

#### Workbook 1: spec-workflow-artifacts-investigation (Academic Research)

**Tipo**: Academic Research (NO IMRAD)  
**Duración**: 5 días  
**Rostros**: HYPATIA → SALOMON → MORPHEUS → ALMA

**Estructura**:
```
spec-workflow-artifacts-investigation/
├── 1-literature/
│   ├── sources.yaml                    # PRISMA flow: 20 fuentes
│   ├── framework/
│   │   └── spec-workflow-mcp/
│   │       ├── metadata.yaml           # Dublin Core
│   │       ├── content.md              # Dashboard code analysis
│   │       └── citations.bib
│   ├── paper/
│   │   └── hevner-2004-dsr/
│   └── book/
│       └── evans-2003-ddd/
│
├── 2-analysis/
│   ├── dashboard-code-analysis.md      # AST parsing de dashboard
│   ├── rbm-to-artifacts-mapping.md     # Mapeo RBM → spec-workflow
│   ├── product-md-structure.md         # Análisis product.md esperado
│   ├── tech-md-structure.md            # Análisis tech.md esperado
│   └── recommendations.md              # Qué artefactos adoptar
│
├── 3-atomics/
│   ├── concept-product-md.md           # Qué es product.md
│   ├── concept-tech-md.md              # Qué es tech.md
│   ├── concept-structure-md.md         # Qué es structure.md
│   ├── concept-requirements-md.md      # Qué es requirements.md
│   └── concept-design-md.md            # Qué es design.md
│
├── 4-artifacts/
│   ├── test-product-compiler.py        # Test: Compilar product.md
│   ├── schema-product-md.json          # JSON Schema para product.md
│   └── contract-dashboard-parser.py    # Contract: Parser dashboard
│
└── 6-outputs/
    ├── index-spec-workflow-artifacts.md    # Índice de artefactos
    ├── cypher-artifacts-ingestion.cypher   # Queries para Neo4j
    └── README.md                           # ALMA overview
```

**Research Questions**:
1. ¿Qué artefactos espera el dashboard de spec-workflow-mcp?
2. ¿Qué estructura JSON/YAML tiene cada artefacto?
3. ¿Cómo mapean conceptos RBM a estos artefactos?

---

#### Workbook 2: daath-zen-templates-analysis (IMRAD)

**Tipo**: IMRAD (análisis específico)  
**Duración**: 3 días  
**Rostros**: SALOMON (diseña) + MORPHEUS (valida)

**Estructura**:
```
daath-zen-templates-analysis/
├── 01-introduction.md      # Problema: 6 templates inconsistentes
├── 02-methods.md           # Análisis comparativo línea-por-línea
├── 03-results.md           # Tabla comparativa
├── 04-analysis.md          # Patrones comunes
├── 05-discussion.md        # Implicaciones
├── 06-conclusion.md        # Decisión: template-base.yaml
└── 07-references.md        # Links a 6 templates
```

**Research Question**:
- ¿Cuál estructura unificada emerge de 6 templates DAATH-ZEN?

---

#### Workbook 3: opensource-ontologies-investigation (Academic Research)

**Tipo**: Academic Research  
**Duración**: 4 días  
**Rostros**: HYPATIA → SALOMON → MORPHEUS → ALMA

**Estructura**:
```
opensource-ontologies-investigation/
├── 1-literature/
│   ├── framework/
│   │   ├── schema-org/
│   │   ├── foaf-ontology/
│   │   ├── neo4j-gds/
│   │   └── dbpedia/
│   ├── library/
│   │   ├── llamaindex/
│   │   └── langchain/
│   └── paper/
│       └── embedding-models-benchmarks/
│
├── 2-analysis/
│   ├── schema-org-vs-foaf.md
│   ├── neo4j-gds-patterns.md
│   └── embedding-models-comparison.md
│
├── 3-atomics/
│   ├── schema-org-person.md
│   ├── foaf-knows-relationship.md
│   └── pagerank-algorithm.md
│
├── 4-artifacts/
│   ├── test-schema-org-mapping.py
│   └── cypher-pattern-pagerank.cypher
│
└── 6-outputs/
    └── index-ontologies.md
```

---

#### Workbook 4: genai-stack-documentation (IMRAD)

**Tipo**: IMRAD (análisis de arquitectura existente)  
**Duración**: 2 días  
**Rostros**: SALOMON + MORPHEUS

**Estructura**:
```
genai-stack-documentation/
├── 01-introduction.md      # Estado actual GenAI-stack
├── 02-methods.md           # Análisis docker-compose.yml
├── 03-results.md           # Diagrama arquitectura
├── 04-analysis.md          # Gaps (falta MD ingestion)
├── 05-discussion.md        # Integración con triple-persistence
├── 06-conclusion.md        # Spec formal para spec-002
└── 07-references.md        # genai-stack.md (1,040 líneas)
```

---

#### Workbook 5: mcp-obsidian-integration (IMRAD)

**Tipo**: IMRAD (diseño de integración)  
**Duración**: 2 días  
**Rostros**: SALOMON + MORPHEUS

**Estructura**:
```
mcp-obsidian-integration/
├── 01-introduction.md      # Necesidad gestionar dominio con Obsidian
├── 02-methods.md           # Análisis MCP-Obsidian API
├── 03-results.md           # Diagrama integración
├── 04-analysis.md          # Estrategia sincronización
├── 05-discussion.md        # ALMA como orquestador
├── 06-conclusion.md        # Pipeline ALMA definido
└── 07-references.md        # MCP-Obsidian docs
```

---

#### Workbook 6: contenidos-atomicos-methodology (IMRAD)

**Tipo**: IMRAD (metodología design)  
**Duración**: 2 días  
**Rostros**: SALOMON + MORPHEUS

**Estructura**:
```
contenidos-atomicos-methodology/
├── 01-introduction.md      # Concepto contenidos-atómicos
├── 02-methods.md           # Análisis Zettelkasten
├── 03-results.md           # Template para atomic content
├── 04-analysis.md          # Relación con triple persistence
├── 05-discussion.md        # MORPHEUS automatizado
├── 06-conclusion.md        # Metodología estandarizada
└── 07-references.md        # Papers Zettelkasten
```

---

### 5.2 Resumen de Distribución

| Workbook | Tipo | Duración | Output Principal |
|----------|------|----------|------------------|
| 1. spec-workflow-artifacts | **Academic Research** | 5 días | Knowledge base de artefactos |
| 2. daath-zen-templates | **IMRAD** | 3 días | template-base.yaml diseño |
| 3. opensource-ontologies | **Academic Research** | 4 días | Catálogo ontologías + patterns |
| 4. genai-stack-documentation | **IMRAD** | 2 días | Arquitectura documentada |
| 5. mcp-obsidian-integration | **IMRAD** | 2 días | Pipeline ALMA diseñado |
| 6. contenidos-atomicos-methodology | **IMRAD** | 2 días | Metodología MORPHEUS |
| **TOTAL** | 2 Academic + 4 IMRAD | **18 días** | Knowledge base + Designs |

---

## 📁 Parte 6: Estructura domain/ Corregida

### 6.1 Estructura Actualizada

```
_melquisedec/domain/
├── workbooks/                              # RAIZ de workbooks
│   │
│   ├── academic-research/                  # TIPO 1: Academic Research
│   │   ├── spec-workflow-artifacts-investigation/
│   │   │   ├── 1-literature/
│   │   │   │   ├── sources.yaml            # PRISMA flow
│   │   │   │   ├── framework/
│   │   │   │   │   └── spec-workflow-mcp/
│   │   │   │   ├── paper/
│   │   │   │   └── book/
│   │   │   ├── 2-analysis/
│   │   │   │   ├── dashboard-code-analysis.md
│   │   │   │   └── recommendations.md
│   │   │   ├── 3-atomics/
│   │   │   │   ├── concept-product-md.md
│   │   │   │   └── concept-tech-md.md
│   │   │   ├── 4-artifacts/
│   │   │   │   ├── test-product-compiler.py
│   │   │   │   └── schema-product-md.json
│   │   │   └── 6-outputs/
│   │   │       └── index-artifacts.md
│   │   │
│   │   └── opensource-ontologies-investigation/
│   │       ├── 1-literature/
│   │       ├── 2-analysis/
│   │       ├── 3-atomics/
│   │       ├── 4-artifacts/
│   │       └── 6-outputs/
│   │
│   └── imrad-research/                     # TIPO 2: IMRAD Analysis
│       ├── daath-zen-templates-analysis/
│       │   ├── 01-introduction.md
│       │   ├── 02-methods.md
│       │   ├── 03-results.md
│       │   ├── 04-analysis.md
│       │   ├── 05-discussion.md
│       │   ├── 06-conclusion.md
│       │   └── 07-references.md
│       │
│       ├── genai-stack-documentation/
│       ├── mcp-obsidian-integration/
│       └── contenidos-atomicos-methodology/
│
├── amendments/                             # Amendments (Opción C Hybrid)
│   └── spec-001-amendment-template-validation.md
│
├── cypher/                                 # Triple Persistencia
│   ├── academic-research/
│   │   └── spec-workflow-artifacts/
│   │       ├── nodes.cypher
│   │       └── relationships.cypher
│   └── imrad-research/
│       └── daath-zen-templates/
│           ├── nodes.cypher
│           └── relationships.cypher
│
├── embeddings/                             # Vector embeddings
│   ├── academic-research/
│   └── imrad-research/
│
└── README.md                               # ALMA-generated overview
```

---

### 6.2 Explicación de Estructura

#### Separación por Tipo de Metodología

**Razón**: Dos metodologías requieren estructuras DIFERENTES.

**academic-research/**:
- Folders: 1-literature/, 2-analysis/, 3-atomics/, 4-artifacts/, 6-outputs/
- Iterativa: HYPATIA descubre → SALOMON analiza → MORPHEUS atomiza → ALMA publica
- Output: Knowledge base (heterogéneo)

**imrad-research/**:
- Files: 01-07 secciones fijas
- Lineal: Introduction → Conclusion (1 dirección)
- Output: Diseño + decisión (homogéneo)

---

## 📋 Parte 7: Mejoras a Requirements, Design, Tasks

### 7.1 Requirements (Mejoras)

**❌ ANTES** (Incompleto):
```markdown
### REQ-001-04: Investigación IMRAD de Artefactos

Realizar investigación IMRAD...
```

**✅ DESPUÉS** (Claro):
```markdown
### REQ-001-04: Investigación de Artefactos spec-workflow-mcp

**Tipo de Workbook**: Academic Research (NO IMRAD)  
**Metodología**: Systematic Literature Review (Kitchenham 2007) + Zettelkasten

**Objetivo**: Descubrir qué artefactos espera dashboard de spec-workflow-mcp, construir knowledge base de conceptos.

**Estructura Output**:
```
_melquisedec/domain/workbooks/academic-research/spec-workflow-artifacts-investigation/
├── 1-literature/               # HYPATIA: Buscar fuentes
├── 2-analysis/                 # SALOMON: Analizar literatura
├── 3-atomics/                  # MORPHEUS: Generar atomics
├── 4-artifacts/                # MORPHEUS: Tests + schemas
└── 6-outputs/                  # ALMA: Publicar + ingestar
```

**Success Criteria**:
- [ ] ≥15 fuentes catalogadas en 1-literature/ (PRISMA flow)
- [ ] ≥8 contenidos-atómicos generados en 3-atomics/
- [ ] ≥3 artifacts ejecutables en 4-artifacts/ (tests passing)
- [ ] Cypher queries generadas en 6-outputs/ (Neo4j validated)
- [ ] Triple persistence funcional (md → graph → vectors)
```

---

### 7.2 Design (Mejoras)

**❌ ANTES** (Confuso):
```markdown
### Workbooks Structure

All workbooks follow IMRAD...
```

**✅ DESPUÉS** (Claro):
```markdown
### ADR-006: Dos Tipos de Workbooks

**Status**: Accepted

**Context**:
- IMRAD es excelente para análisis específicos (pregunta clara → decisión)
- Academic Research es necesario para descubrir dominios (exploración → knowledge base)
- Mezclarlos causa confusión metodológica

**Decision**:
Usar **dos estructuras de workbooks**:

1. **Academic Research**: Para descubrir dominio desconocido
   - Estructura: 1-literature/ → 6-outputs/
   - Metodología: SLR + Zettelkasten
   - Output: Knowledge base + atomics
   - Ejemplo: Investigar ontologías opensource

2. **IMRAD**: Para analizar pregunta específica
   - Estructura: 01-introduction.md → 07-references.md
   - Metodología: IMRAD (Sollaci 2004)
   - Output: Diseño + decisión
   - Ejemplo: Comparar 6 templates DAATH-ZEN

**Rationale**:
- Cada metodología tiene propósito diferente
- Separación evita "IMRAD para todo"
- Estructura refleja proceso cognitivo real

**Alternatives Considered**:
1. Solo IMRAD: ❌ No sirve para exploración
2. Solo Academic: ❌ No sirve para análisis específicos
3. Hybrid folders: ❌ Confusión (qué va dónde)

**Consequences**:
- ✅ Claridad metodológica
- ✅ Workbooks auto-documentan su tipo
- ⚠️ Requiere disciplina para elegir tipo correcto
```

---

### 7.3 Tasks (Mejoras)

**❌ ANTES** (Vago):
```markdown
### Task 2.2: Crear workbooks IMRAD

- File: apps/research-{{spec}}/workbooks/...
- Description: Crear 8 workbooks IMRAD
```

**✅ DESPUÉS** (Específico):
```markdown
### Task 2.2.1: Workbook 1 - spec-workflow-artifacts (Academic Research)

**Tipo de Workbook**: Academic Research  
**Duración estimada**: 5 días (40 horas)  
**Rostros**: HYPATIA → SALOMON → MORPHEUS → ALMA  
**Output Location**: `_melquisedec/domain/workbooks/academic-research/spec-workflow-artifacts-investigation/`

#### Estructura a Crear

```
spec-workflow-artifacts-investigation/
├── 1-literature/               # HYPATIA (Day 1-2, 16h)
│   ├── sources.yaml            # PRISMA flow: ≥15 fuentes
│   ├── framework/
│   │   └── spec-workflow-mcp/
│   │       ├── metadata.yaml   # Dublin Core
│   │       ├── content.md      # Dashboard code analysis
│   │       └── citations.bib
│   └── [otros types]
│
├── 2-analysis/                 # SALOMON (Day 3, 8h)
│   ├── dashboard-code-analysis.md
│   ├── rbm-to-artifacts-mapping.md
│   └── recommendations.md
│
├── 3-atomics/                  # MORPHEUS (Day 4, 8h)
│   ├── concept-product-md.md
│   ├── concept-tech-md.md
│   └── [≥8 atomics total]
│
├── 4-artifacts/                # MORPHEUS (Day 4, 4h)
│   ├── test-product-compiler.py
│   └── schema-product-md.json
│
└── 6-outputs/                  # ALMA (Day 5, 4h)
    ├── index-artifacts.md
    ├── cypher-ingestion.cypher
    └── README.md
```

#### Success Criteria

- [ ] **HYPATIA**: ≥15 fuentes en 1-literature/, metadata Dublin Core completa
- [ ] **SALOMON**: ≥3 analysis docs en 2-analysis/, ≥5 páginas cada uno
- [ ] **MORPHEUS**: ≥8 atomics en 3-atomics/, ≥3 artifacts ejecutables en 4-artifacts/
- [ ] **ALMA**: README.md generado, cypher queries validadas en Neo4j
- [ ] **Triple Persistence**: sync-all.sh ejecutado sin errores

#### Documentos que se Crearán

| Documento | Tipo | Rostro | Duración | Descripción |
|-----------|------|--------|----------|-------------|
| `1-literature/sources.yaml` | YAML | HYPATIA | 4h | PRISMA flow de 15+ fuentes |
| `1-literature/framework/spec-workflow-mcp/content.md` | MD | HYPATIA | 4h | Análisis código dashboard |
| `2-analysis/dashboard-code-analysis.md` | MD | SALOMON | 3h | AST parsing de dashboard |
| `2-analysis/rbm-to-artifacts-mapping.md` | MD | SALOMON | 3h | Mapeo RBM → spec-workflow |
| `3-atomics/concept-product-md.md` | MD | MORPHEUS | 1h | Qué es product.md (atómico) |
| `4-artifacts/test-product-compiler.py` | PY | MORPHEUS | 2h | Test compilar product.md |
| `6-outputs/cypher-ingestion.cypher` | CYPHER | ALMA | 2h | Queries para Neo4j |
| `6-outputs/README.md` | MD | ALMA | 1h | Overview generado |

#### Prompts

**HYPATIA (Day 1)**:
```
Contexto: Necesitamos descubrir qué artefactos espera el dashboard de spec-workflow-mcp.

Tarea: 
1. Analizar código del dashboard (implementation-log-manager.ts, server.ts)
2. Identificar parsers, validadores, extractores de metadata
3. Documentar en 1-literature/framework/spec-workflow-mcp/content.md
4. Crear metadata.yaml con Dublin Core

MCP tools:
- file_read: Leer archivos del dashboard
- grep_search: Buscar patterns de parsing
- semantic_search: Encontrar relacionados

Output: content.md (≥1000 palabras) + metadata.yaml
```

**SALOMON (Day 3)**:
```
Contexto: HYPATIA completó 1-literature/ con 15 fuentes.

Tarea:
1. Leer 1-literature/framework/spec-workflow-mcp/content.md
2. Crear 2-analysis/dashboard-code-analysis.md con:
   - Bounded contexts identificados (product, tech, structure, requirements, design)
   - JSON schemas esperados por dashboard
   - Estrategia de compilación
3. Mapear conceptos RBM a artefactos spec-workflow
4. Recomendar qué artefactos adoptar

Output: 3 analysis docs (≥5 páginas cada uno)
```

**MORPHEUS (Day 4)**:
```
Contexto: SALOMON completó 2-analysis/.

Tarea:
1. Generar contenidos-atómicos en 3-atomics/:
   - concept-product-md.md: Qué es, estructura, ejemplo
   - concept-tech-md.md: Qué es, estructura, ejemplo
   - [Repetir para cada artefacto]
2. Crear artifacts en 4-artifacts/:
   - test-product-compiler.py: Test que compila product.md
   - schema-product-md.json: JSON Schema validador
3. Validar con pytest

Output: 8 atomics + 3 artifacts (tests passing)
```

**ALMA (Day 5)**:
```
Contexto: MORPHEUS completó 3-atomics/ y 4-artifacts/.

Tarea:
1. Generar 6-outputs/README.md con overview
2. Crear cypher-ingestion.cypher con queries para Neo4j
3. Ejecutar sync-all.sh para triple persistence
4. Validar Neo4j + embeddings
5. Update Obsidian vault con backlinks

Output: README.md + cypher queries + triple persistence validada
```

---

### Task 2.2.2: Workbook 2 - daath-zen-templates (IMRAD)

**Tipo de Workbook**: IMRAD  
**Duración estimada**: 3 días (24 horas)  
**Rostros**: SALOMON (diseña) + MORPHEUS (valida)  
**Output Location**: `_melquisedec/domain/workbooks/imrad-research/daath-zen-templates-analysis/`

#### Estructura a Crear

```
daath-zen-templates-analysis/
├── 01-introduction.md      # SALOMON (Day 1, 3h)
├── 02-methods.md           # SALOMON (Day 1, 3h)
├── 03-results.md           # SALOMON (Day 2, 4h)
├── 04-analysis.md          # SALOMON (Day 2, 4h)
├── 05-discussion.md        # SALOMON (Day 3, 3h)
├── 06-conclusion.md        # SALOMON (Day 3, 3h)
└── 07-references.md        # SALOMON (Day 3, 2h)
```

#### Success Criteria

- [ ] **SALOMON**: 7 secciones IMRAD completadas (≥500 palabras cada una)
- [ ] **MORPHEUS**: template-base.yaml prototipado y validado
- [ ] Tabla comparativa de 6 templates en 03-results.md
- [ ] Decisión justificada en 06-conclusion.md (cita 03-results.md y 04-analysis.md)

#### Documentos que se Crearán

| Documento | Sección IMRAD | Rostro | Duración | Contenido |
|-----------|---------------|--------|----------|-----------|
| `01-introduction.md` | Introduction | SALOMON | 3h | Problema: 6 templates inconsistentes, hipótesis, objetivos |
| `02-methods.md` | Methods | SALOMON | 3h | Análisis comparativo línea-por-línea, extracción placeholders |
| `03-results.md` | Results | SALOMON | 4h | Tabla comparativa (líneas, placeholders, metadata) |
| `04-analysis.md` | Analysis | SALOMON | 4h | Patrones comunes, estructura unificada emergente |
| `05-discussion.md` | Discussion | SALOMON | 3h | Implicaciones: template unificado reduce 70% código |
| `06-conclusion.md` | Conclusion | SALOMON | 3h | Decisión: Adoptar daath-zen-base.md, diseño template-base.yaml |
| `07-references.md` | References | SALOMON | 2h | Links a 6 templates analizados |

[Continuar con Task 2.2.3 - 2.2.6 con mismo nivel de detalle]
```

---

## 🎯 Parte 8: Recomendaciones Finales

### 8.1 Checklist para Elegir Metodología

**Pregúntate**:

1. **¿Ya sé QUÉ voy a analizar?**
   - ✅ SÍ → IMRAD
   - ❌ NO → Academic Research

2. **¿Mi pregunta tiene respuesta binaria o selección?**
   - ✅ SÍ (ej: "¿A o B?", "¿Es X mejor que Y?") → IMRAD
   - ❌ NO (ej: "¿Qué existe?", "¿Cuáles son?") → Academic Research

3. **¿Output es diseño/decisión o knowledge base?**
   - ✅ Diseño/decisión → IMRAD
   - ❌ Knowledge base → Academic Research

4. **¿Puedo definir Methods reproducibles?**
   - ✅ SÍ (análisis comparativo, experimento) → IMRAD
   - ❌ NO (exploración, búsqueda iterativa) → Academic Research

---

### 8.2 Mejores Prácticas Aprendidas

#### De Systematic Literature Review (Kitchenham 2007)

1. **PRISMA flow tracking**: Documentar cuántas fuentes encontradas → screened → incluidas
2. **Inclusion/exclusion criteria**: Explicitar criterios de selección
3. **Quality assessment**: Evaluar calidad de fuentes (peer-reviewed > blog)
4. **Data extraction forms**: Templates consistentes para extraer datos

**Aplicar en**:
- `1-literature/sources.yaml`: PRISMA flow
- `2-analysis/review-log.md`: Inclusión/exclusión rationale

---

#### De Zettelkasten (Luhmann 1992)

1. **Atomicidad**: Cada nota = 1 idea (no más)
2. **Conectividad**: Backlinks [[]] entre notas
3. **Emergencia**: Conocimiento emerge de red, no jerarquía

**Aplicar en**:
- `3-atomics/`: Cada atomic = 1 concepto
- Obsidian [[wikilinks]] para conectar
- NO crear carpetas jerárquicas en atomics/

---

#### De IMRAD (Sollaci 2004)

1. **Separar findings de interpretation**: Results vs Analysis/Discussion
2. **Methods reproducibles**: Otro puede replicar
3. **Introduction narrowing**: General → Específico → Hipótesis

**Aplicar en**:
- `03-results.md`: Solo datos, sin interpretación
- `04-analysis.md`: Interpretación de 03-results.md
- `02-methods.md`: Paso a paso replicable

---

#### De Dublin Core (DCMI 2020)

1. **15 core elements**: Usar todos cuando aplique
2. **Controlled vocabularies**: Usar estándares (ISO 8601 para fechas)
3. **Persistent identifiers**: DOI, ISBN, URL permanentes

**Aplicar en**:
- `1-literature/{type}/{id}/metadata.yaml`: Dublin Core completo
- `dc:identifier`: Siempre incluir (DOI preferible)

---

### 8.3 Anti-Patterns a Evitar

❌ **"IMRAD para todo"**: No forzar IMRAD en exploración de dominio

❌ **"Academic Research para decisiones"**: No usar 6 folders para comparar 2 opciones

❌ **"Atomics gigantes"**: No crear concept-ddd-all.md (dividir en atomics pequeños)

❌ **"Literatura sin metadata"**: No omitir Dublin Core en 1-literature/

❌ **"Outputs sin índice"**: No olvidar index.md en 6-outputs/

❌ **"Artefactos sin owner"**: No omitir `spec:issue` y `spec:owner` en metadata

---

## 🔐 Parte 9: Gobernanza de Artefactos (Ownership + Pull Requests)

### 9.1 Problema: Artefactos Huérfanos

**Escenario**: spec-000 crea `concept-product-md.md` en 3-atomics/. Luego, spec-003 descubre mejores prácticas sobre product.md.

**¿Qué hacer?**

❌ **MAL**: spec-003 modifica directamente `concept-product-md.md`
- Problema: Rompe intención original de spec-000
- Problema: Git blame confuso (¿quién es dueño?)
- Problema: Futuro no sabe contexto de cambios

✅ **BIEN**: spec-003 crea **pull request** a spec-000 sugiriendo mejoras
- spec-000 sigue siendo **owner** (autoridad)
- spec-003 es **contributor** (sugiere)
- Cambio documentado con trazabilidad completa

---

### 9.2 Metadata Extendida con Ownership

#### Ejemplo: concept-product-md.md

```yaml
---
# Dublin Core Standard
dc:
  title: "Concepto: product.md Structure"
  creator: "spec-000-investigation-daath-zen"        # OWNER (spec que lo creó)
  contributor: ["spec-003-dashboard-improvements"]   # Specs que sugirieron cambios
  date: "2026-01-10"                                 # Fecha creación
  modified: "2026-01-15"                             # Última modificación
  subject: ["product.md", "spec-workflow-mcp", "artifact-structure"]
  description: "Contenido atómico que define la estructura y propósito de product.md en spec-workflow-mcp"
  type: "ContentoAtomic"
  format: "text/markdown"
  identifier: "atomic-000-001"                       # ID único
  source: "apps/research-keter-migration/spec-001/workbooks/.../2-analysis/product-md-structure.md"
  language: "es"
  relation: 
    - "isPartOf:spec-000"
    - "references:concept-tech-md"
    - "references:concept-structure-md"
  coverage: "Artifact Management, Spec Workflow"
  rights: "MIT License"

# Spec-Workflow Extensions (Trazabilidad)
spec:
  issue: "spec-000-investigation-daath-zen"          # Issue/Spec que GENERA y MANTIENE
  owner: "MORPHEUS"                                  # Rostro responsable
  status: "stable"                                   # stable | draft | deprecated
  version: "1.0.0"                                   # Semantic versioning
  amendments: 
    - issue: "spec-003-dashboard-improvements"       # Specs que solicitaron cambios
      date: "2026-01-15"
      type: "pull-request"                           # pull-request | suggestion | correction
      status: "merged"                               # pending | merged | rejected
      description: "Agregar sección sobre JSON Schema validation"
      approvedBy: "MORPHEUS"                         # Quien aprobó el cambio
  changeHistory:
    - version: "1.0.0"
      date: "2026-01-10"
      author: "spec-000/MORPHEUS"
      description: "Initial creation from 2-analysis/product-md-structure.md"
    - version: "1.1.0"
      date: "2026-01-15"
      author: "spec-000/MORPHEUS"
      description: "Incorporated feedback from spec-003 PR (JSON Schema section)"
  dependencies:
    - "concept-tech-md.md"                          # Atomics relacionados
    - "concept-structure-md.md"
  consumers:
    - "spec-001-prototype-architecture"             # Specs que USAN este atomic
    - "spec-002-triple-persistence"

# Keter-Doc Protocol Context
'@context': '../../../context.jsonld'
'@type': 'ContentoAtomic'
'@id': 'atomic-000-001'

---

# Concepto: product.md Structure

## Definición

`product.md` es un artefacto estructurado del sistema spec-workflow-mcp que documenta...

[Resto del contenido...]
```

---

### 9.3 Flujo de Pull Requests entre Specs

#### Paso 1: spec-003 descubre mejora

**spec-003** (en su workbook) identifica:
> "product.md debería incluir sección de JSON Schema validation para compatibilidad con dashboard"

---

#### Paso 2: spec-003 crea Pull Request Document

```markdown
# _melquisedec/domain/pull-requests/pr-003-to-000-product-md-schema.md

---
pr:
  id: "pr-003-to-000-001"
  from: "spec-003-dashboard-improvements"
  to: "spec-000-investigation-daath-zen"
  target: "3-atomics/concept-product-md.md"
  type: "enhancement"                       # enhancement | correction | clarification
  status: "pending"                         # pending | approved | rejected
  submittedBy: "spec-003/SALOMON"
  submittedDate: "2026-01-15"
  reviewedBy: null
  reviewedDate: null
---

## Context

Durante implementación de spec-003, descubrimos que dashboard de spec-workflow-mcp valida product.md usando JSON Schema. El atomic actual (`concept-product-md.md` de spec-000) NO menciona esta validación.

## Proposed Change

Agregar sección "### 3. JSON Schema Validation" en `concept-product-md.md`:

```markdown
### 3. JSON Schema Validation

El dashboard valida product.md contra `schemas/product-md.schema.json`:

\```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["title", "description", "status"],
  ...
}
\```

**Implicación**: product.md debe ser parseable a YAML/JSON para validación.
```

## Rationale

- **Completitud**: Atomic debe documentar TODAS las características de product.md
- **Validación**: Futuros specs necesitan saber sobre schema validation
- **Interoperabilidad**: Dashboard rechaza product.md inválidos (crítico)

## Impact

- **spec-000**: Atomic más completo (mejora calidad)
- **spec-001+**: Futuros specs evitan crear product.md inválidos
- **Riesgo**: Ninguno (solo agrega información, no cambia conclusiones)

## References

- spec-003: `workbooks/dashboard-integration/02-methods.md#L45-L78`
- Dashboard code: `implementation-log-manager.ts#L156` (validación schema)

## Requested Action

**MORPHEUS** (owner de `concept-product-md.md`):
- [ ] Revisar propuesta
- [ ] Aprobar/rechazar con justificación
- [ ] Si aprobado: Actualizar atomic + metadata (version bump 1.0.0 → 1.1.0)
```

---

#### Paso 3: MORPHEUS (spec-000) revisa PR

**MORPHEUS lee PR**, evalúa:
1. ¿Es factualmente correcto? (revisa dashboard code)
2. ¿Mejora el atomic? (sí, agrega info crítica)
3. ¿Rompe intención original? (no, solo amplía)

**Decisión**: ✅ **APPROVED**

---

#### Paso 4: MORPHEUS actualiza atomic

**Cambios**:
1. Agregar sección "JSON Schema Validation" en `concept-product-md.md`
2. Actualizar metadata:
   ```yaml
   spec:
     version: "1.1.0"  # Bump version
     amendments:
       - issue: "spec-003-dashboard-improvements"
         date: "2026-01-15"
         type: "pull-request"
         status: "merged"
         approvedBy: "MORPHEUS"
     changeHistory:
       - version: "1.1.0"
         date: "2026-01-15"
         author: "spec-000/MORPHEUS"
         description: "Incorporated spec-003 PR: JSON Schema validation section"
   ```

---

#### Paso 5: MORPHEUS actualiza PR status

```yaml
# pr-003-to-000-product-md-schema.md

pr:
  status: "approved"                    # pending → approved
  reviewedBy: "spec-000/MORPHEUS"
  reviewedDate: "2026-01-15"
  resolution: "merged-in-v1.1.0"
```

---

### 9.4 Tipos de Pull Requests

| Tipo | Descripción | Requiere Aprobación |
|------|-------------|---------------------|
| **enhancement** | Agregar información nueva | ✅ Sí (owner decide) |
| **correction** | Corregir error factual | ✅ Sí (verificar antes) |
| **clarification** | Mejorar redacción/claridad | ⚠️ Opcional (owner puede auto-merge) |
| **deprecation** | Marcar contenido obsoleto | ✅ Sí (decisión crítica) |
| **refactoring** | Reestructurar sin cambiar semántica | ✅ Sí (afecta consumers) |

---

### 9.5 Estructura domain/ con PRs

```
_melquisedec/domain/
├── workbooks/
│   ├── academic-research/
│   │   └── spec-workflow-artifacts-investigation/
│   │       ├── 3-atomics/
│   │       │   └── concept-product-md.md          # metadata incluye spec:issue
│   │       └── README.md                          # metadata incluye spec:issue
│   └── imrad-research/
│
├── pull-requests/                                  # NUEVA carpeta
│   ├── pending/
│   │   └── pr-004-to-000-ontology-clarification.md
│   ├── approved/
│   │   └── pr-003-to-000-product-md-schema.md
│   └── rejected/
│       └── pr-005-to-000-template-redesign.md     # Con justificación de rechazo
│
├── amendments/
│   └── spec-001-amendment-template-validation.md
│
└── README.md
```

---

### 9.6 Metadata en README.md de Workbooks

#### Ejemplo: spec-workflow-artifacts-investigation/README.md

```yaml
---
# Dublin Core
dc:
  title: "Workbook: spec-workflow-mcp Artifacts Investigation"
  creator: "spec-000-investigation-daath-zen"
  date: "2026-01-10"
  type: "AcademicResearchWorkbook"
  description: "Systematic literature review de artefactos esperados por spec-workflow-mcp dashboard"

# Spec-Workflow Extensions
spec:
  issue: "spec-000-investigation-daath-zen"        # OWNER
  workbookType: "academic-research"                 # academic-research | imrad
  status: "completed"                               # draft | in-progress | completed
  completionDate: "2026-01-15"
  rostros:
    - name: "HYPATIA"
      responsible: "1-literature/"
      completed: true
    - name: "SALOMON"
      responsible: "2-analysis/"
      completed: true
    - name: "MORPHEUS"
      responsible: "3-atomics/, 4-artifacts/"
      completed: true
    - name: "ALMA"
      responsible: "6-outputs/"
      completed: true
  outputs:
    - type: "contenidos-atomicos"
      count: 8
      location: "3-atomics/"
    - type: "artifacts"
      count: 3
      location: "4-artifacts/"
    - type: "cypher-queries"
      count: 5
      location: "6-outputs/cypher-ingestion.cypher"
  consumers:                                        # Specs que USAN este workbook
    - "spec-001-prototype-architecture"
    - "spec-002-triple-persistence"
  pullRequests:
    - id: "pr-003-to-000-001"
      from: "spec-003"
      status: "merged"
      target: "3-atomics/concept-product-md.md"

'@context': '../../../../context.jsonld'
'@type': 'ResearchWorkbook'
'@id': 'workbook-000-001'

---

# Workbook: spec-workflow-mcp Artifacts Investigation

## Overview

Este workbook documenta la investigación sistemática de los artefactos esperados por el dashboard de spec-workflow-mcp...

[Resto del contenido...]
```

---

### 9.7 Ventajas del Sistema de Ownership

#### ✅ Trazabilidad Completa

Cada artefacto responde:
- **¿Quién lo creó?**: `dc:creator` (spec-000)
- **¿Quién lo mantiene?**: `spec:owner` (MORPHEUS)
- **¿Quién contribuyó?**: `dc:contributor` (spec-003, spec-007)
- **¿Por qué cambió?**: `spec:changeHistory` (versioned)

---

#### ✅ Respeto por Autoridad

Solo el **owner** puede modificar:
- Otros specs **sugieren** (pull requests)
- Owner **evalúa** (aprueba/rechaza)
- Decisión documentada (trazabilidad)

**Ejemplo**:
```
spec-003 NO puede editar concept-product-md.md
spec-003 PUEDE crear pr-003-to-000-001.md
spec-000/MORPHEUS DECIDE si incorporar cambio
```

---

#### ✅ Colaboración Sin Caos

Múltiples specs pueden contribuir:
```yaml
dc:
  contributor: 
    - "spec-003-dashboard-improvements"
    - "spec-007-testing-strategy"
    - "spec-012-ci-cd-integration"
```

Cada contribución documentada en `spec:amendments`.

---

#### ✅ Evolución Controlada

Semantic versioning:
```yaml
spec:
  version: "1.2.3"
  changeHistory:
    - version: "1.0.0"  # Initial
    - version: "1.1.0"  # Enhancement (spec-003 PR)
    - version: "1.2.0"  # Enhancement (spec-007 PR)
    - version: "1.2.3"  # Correction (typo fix)
```

Consumers saben qué version usan:
```yaml
# spec-001 dependencies
dependencies:
  - artifact: "concept-product-md"
    version: "^1.1.0"  # Compatible con 1.1.x
```

---

### 9.8 Workflow PR entre Specs

#### Diagrama de Flujo

```
┌─────────────────────────────────────────────────────────────────┐
│ spec-003 descubre mejora para artefacto de spec-000            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ spec-003 crea pull-requests/pending/pr-003-to-000-xxx.md       │
│ - Describe cambio propuesto                                     │
│ - Justifica rationale                                           │
│ - Referencia evidencia (código, papers, etc.)                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ spec-003 notifica a spec-000 (tag en issues, email, etc.)      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ spec-000/OWNER (MORPHEUS) revisa PR                             │
│ - Lee propuesta                                                  │
│ - Valida evidencia                                               │
│ - Decide: APPROVE | REJECT | REQUEST_CHANGES                    │
└────────────┬──────────────────────┬─────────────────────────────┘
             │                      │
    ✅ APPROVE                ❌ REJECT
             │                      │
             ▼                      ▼
┌──────────────────────┐  ┌──────────────────────────────────────┐
│ MORPHEUS actualiza:  │  │ MORPHEUS documenta rechazo:          │
│ - Artefacto          │  │ - Razón (no aplica, incorrecto, etc.)│
│ - Metadata (version) │  │ - Mueve PR a rejected/               │
│ - PR status: merged  │  │ - PR status: rejected                │
└──────────────────────┘  └──────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│ spec-003 es notificado (PR merged o rejected)                   │
│ - Si merged: spec-003 actualiza dependencies a nueva version    │
│ - Si rejected: spec-003 puede apelar o cerrar                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 9.9 Anti-Patterns de Gobernanza

❌ **"Free-for-all editing"**: Cualquier spec edita cualquier artefacto
- Problema: Caos, conflictos, pérdida de intención original

❌ **"Ownership sin PR system"**: Owner único, pero sin forma de sugerir cambios
- Problema: Silos, conocimiento no fluye entre specs

❌ **"PRs sin review"**: Auto-merge sin evaluación
- Problema: Calidad degrada, errores propagados

❌ **"Metadata sin spec:issue"**: No se sabe quién es owner
- Problema: Nadie sabe a quién preguntar, artefactos huérfanos

❌ **"Versioning sin semver"**: Versiones arbitrarias (v1, v2, v3)
- Problema: Consumers no saben si cambio es breaking

---

### 9.10 Ejemplo Completo: Lifecycle de concept-product-md.md

#### T0: spec-000 crea atomic (2026-01-10)

```yaml
---
dc:
  creator: "spec-000"
spec:
  issue: "spec-000"
  owner: "MORPHEUS"
  version: "1.0.0"
  status: "stable"
---
# Concepto: product.md Structure
[Contenido inicial...]
```

---

#### T1: spec-003 sugiere mejora (2026-01-15)

```markdown
# pull-requests/pending/pr-003-to-000-product-md-schema.md
- from: spec-003
- to: spec-000
- target: concept-product-md.md
- type: enhancement
- proposal: "Agregar sección JSON Schema validation"
```

---

#### T2: MORPHEUS aprueba (2026-01-15)

```yaml
---
dc:
  creator: "spec-000"
  contributor: ["spec-003"]   # ← Agregado
spec:
  version: "1.1.0"              # ← Bump version
  amendments:
    - issue: "spec-003"
      status: "merged"
  changeHistory:
    - version: "1.1.0"
      description: "Added JSON Schema section (spec-003 PR)"
---
# Concepto: product.md Structure
[Contenido actualizado con sección JSON Schema...]
```

---

#### T3: spec-007 sugiere corrección (2026-01-20)

```markdown
# pull-requests/pending/pr-007-to-000-product-md-typo.md
- from: spec-007
- to: spec-000
- target: concept-product-md.md
- type: correction
- proposal: "Corregir typo: 'valiation' → 'validation'"
```

---

#### T4: MORPHEUS aprueba (2026-01-20)

```yaml
spec:
  version: "1.1.1"              # ← Patch version (typo fix)
  changeHistory:
    - version: "1.1.1"
      description: "Fixed typo (spec-007 PR)"
```

---

#### T5: spec-012 sugiere breaking change (2026-02-01)

```markdown
# pull-requests/pending/pr-012-to-000-product-md-redesign.md
- from: spec-012
- to: spec-000
- target: concept-product-md.md
- type: "refactoring"
- proposal: "Reestructurar completamente product.md (nueva sección 'Architecture')"
```

---

#### T6: MORPHEUS **RECHAZA** (2026-02-02)

```markdown
# pull-requests/rejected/pr-012-to-000-product-md-redesign.md

pr:
  status: "rejected"
  reviewedBy: "spec-000/MORPHEUS"
  resolution: |
    Rechazo porque:
    1. Breaking change requiere spec-workflow-mcp dashboard actualización
    2. No hay consenso en community sobre nueva estructura
    3. Impacto muy alto: 15+ specs consumers afectados
    
    Recomendación: Crear NUEVO atomic (concept-product-md-v2.md) en spec-012
    como propuesta alternativa, SIN modificar concept-product-md.md.
```

---

### 9.11 Integración con Keter-Doc Protocol

El sistema de ownership es **extensión** del Keter-Doc Protocol:

```jsonld
{
  "@context": {
    "dc": "http://purl.org/dc/terms/",
    "spec": "https://aleia-melquisedec.org/spec-workflow#",
    "ContentoAtomic": "spec:ContentoAtomic",
    "issue": "spec:issue",
    "owner": "spec:owner",
    "pullRequest": "spec:pullRequest",
    "amendment": "spec:amendment"
  },
  "@graph": [
    {
      "@id": "atomic-000-001",
      "@type": "ContentoAtomic",
      "dc:title": "Concepto: product.md Structure",
      "dc:creator": "spec-000",
      "dc:contributor": ["spec-003", "spec-007"],
      "spec:issue": "spec-000-investigation-daath-zen",
      "spec:owner": "MORPHEUS",
      "spec:version": "1.1.1",
      "spec:pullRequest": [
        {
          "@id": "pr-003-to-000-001",
          "spec:from": "spec-003",
          "spec:status": "merged"
        }
      ]
    }
  ]
}
```

---

### 9.12 Checklist de Metadata Completa

Antes de publicar **cualquier artefacto** (atomic, workbook, etc.), validar:

- [ ] **Dublin Core**: ≥8 elementos (`title`, `creator`, `date`, `type`, etc.)
- [ ] **spec:issue**: Issue/Spec que GENERA y MANTIENE el artefacto
- [ ] **spec:owner**: Rostro responsable (HYPATIA, SALOMON, MORPHEUS, ALMA)
- [ ] **spec:version**: Semantic versioning (1.0.0)
- [ ] **spec:status**: stable | draft | deprecated
- [ ] **@context**: Link a context.jsonld (Keter-Doc Protocol)
- [ ] **@type**: Tipo RDF (ContentoAtomic, ResearchWorkbook, etc.)
- [ ] **@id**: Identificador único (atomic-000-001, workbook-003-002)

**Script de validación** (futuro):
```bash
# Validar metadata de todos los artefactos
python tools/validate-metadata.py _melquisedec/domain/

# Output:
# ✅ concept-product-md.md: Metadata completa
# ❌ concept-tech-md.md: Falta spec:issue
# ❌ workbook-001/README.md: Falta @context
```

---

## 📚 Referencias Bibliográficas

### Methodologies

1. **Sollaci, L. B., & Pereira, M. G. (2004)**. The introduction, methods, results, and discussion (IMRAD) structure: a fifty-year survey. *Journal of the Medical Library Association*, 92(3), 364-367.

2. **Kitchenham, B., & Charters, S. (2007)**. Guidelines for performing systematic literature reviews in software engineering. *Technical Report EBSE-2007-01*, Keele University.

3. **Moher, D., et al. (2009)**. Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement. *PLoS Medicine*, 6(7), e1000097.

4. **Luhmann, N. (1992)**. Communicating with slip boxes: An empirical account. In *Universität als Milieu* (pp. 53-61).

5. **Glaser, B. G., & Strauss, A. L. (1967)**. The discovery of grounded theory: Strategies for qualitative research. Aldine.

### Standards

6. **Dublin Core Metadata Initiative (2020)**. DCMI Metadata Terms. Retrieved from http://dublincore.org/specifications/dublin-core/dcmi-terms/

7. **ISO 15836:2009**. Information and documentation -- The Dublin Core metadata element set.

### Books

8. **Ahrens, S. (2017)**. How to take smart notes: One simple technique to boost writing, learning and thinking. CreateSpace.

9. **Evans, E. (2003)**. Domain-driven design: Tackling complexity in the heart of software. Addison-Wesley.

---

## ✅ Checklist de Validación

Antes de proceder con spec-000, validar:

- [ ] **Metodología clara**: Cada workbook especifica si es Academic Research o IMRAD
- [ ] **Estructura correcta**: Academic usa 1-6 folders, IMRAD usa 01-07 files
- [ ] **Rostros asignados**: HYPATIA para literatura, SALOMON para análisis, etc.
- [ ] **Documentos listados**: Cada task especifica QUÉ documentos se crearán
- [ ] **Success criteria**: Métricas cuantitativas (≥15 fuentes, ≥8 atomics)
- [ ] **Triple persistence**: sync-all.sh en workflows MORPHEUS/ALMA
- [ ] **Obsidian integration**: Backlinks [[]] en atomics, Kanban sincronizado

---

**Esperando feedback del usuario para proceder con spec-000 corregido.**