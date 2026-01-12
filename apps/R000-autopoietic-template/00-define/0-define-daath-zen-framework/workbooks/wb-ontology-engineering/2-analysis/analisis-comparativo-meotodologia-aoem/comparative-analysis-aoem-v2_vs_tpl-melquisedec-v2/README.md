# Análisis Comparativo: AOEM v2 ↔ Template Melquisedec v2/v3

> **Proyecto**: Análisis Comparativo de Metodologías de Ingeniería Ontológica  
> **Fecha inicio**: 2026-01-11  
> **Estado**: HITO 3 - Implementation & POC Integration (60% completado)  
> **Versión**: 0.4.0

---

## 🚀 Inicio Rápido

**¿Primera vez aquí?** → Lee primero: **[00-GUIA-PARA-DUMMIES.md](./00-GUIA-PARA-DUMMIES.md)** (15 min) 📚

**¿Eres stakeholder?** → Lee solo: `00-GUIA-PARA-DUMMIES.md` + este README (10 min) 👔

**¿Eres domain expert?** → Lee: Guías dummies + `hito-2-conceptualizacion/README-HITO2.md` (30 min) 🧑‍🏫

**¿Eres ontology engineer?** → Lee: Todo el proyecto (2-3 horas) 👨‍💻

---

## 📋 ¿Qué Es Este Proyecto? (En 3 Líneas)

Este proyecto compara dos metodologías de ingeniería ontológica:
- **AOEM v2.0** (metodología ágil genérica)
- **Template Melquisedec v2/v3** (templates específicos con ISO 704 + SKOS + OTTR)

**Objetivo**: Crear **AOEM v3.0** combinando lo mejor de ambos mundos.

---

## 📂 Estructura del Directorio (Reorganizada por HITOs)

```
comparative-analysis-aoem-v2_vs_tpl-melquisedec-v2/
│
├── 00-GUIA-PARA-DUMMIES.md           # ⭐ EMPIEZA AQUÍ (analogías, glosario, FAQs)
├── README.md                          # Este archivo (resumen ejecutivo)
│
├── research/                          # Investigaciones formales
│   └── ottr-instantiation-format-research.md
│
├── hito-1-analisis/                   # 📊 HITO 1: Análisis de gaps (COMPLETADO ✅)
│   ├── README-HITO1.md                # Guía HITO 1
│   ├── 01-analisis-resumen.md         # Resumen ejecutivo
│   └── 02-mapeo-aoem-template.md      # Matriz AOEM ↔ Template
│
├── hito-2-conceptualizacion/          # 🎨 HITO 2: Templates mejorados (COMPLETADO ✅)
│   ├── README-HITO2.md                # Guía HITO 2
│   ├── templates-documentacion/       # YAML templates para humanos
│   │   ├── concept-template-v3.yaml
│   │   └── definition-template-v3.md
│   ├── templates-ottr-automatizacion/ # OTTR templates para máquinas
│   │   ├── ottr-templates/
│   │   ├── instances/
│   │   ├── output/
│   │   └── prefixes.ttl
│   ├── reuse-assessment.md
│   ├── competency-questions.md
│   └── gaps-detallado.md
│
└── hito-3-implementacion/             # 🤖 HITO 3: CI/CD & Experiments (EN PROGRESO 60%)
    ├── README-HITO3.md                # Guía HITO 3
    ├── ci-cd/                         # GitHub Actions pipeline
    ├── validation-scripts/            # ROBOT, pySHACL, SPARQL tests
    ├── shacl-shapes/                  # Constraint shapes
    └── embedding-experiment/          # PyKEEN TransE model

### ✅ HITO 1: Análisis de Gaps (COMPLETADO 100%)

**📖 Guía**: [hito-1-analisis/README-HITO1.md](./hito-1-analisis/README-HITO1.md)

**Qu✅ HITO 2: Conceptualization & Template Enrichment (COMPLETADO 100%)

**📖 Guía**: [hito-2-conceptualizacion/README-HITO2.md](./hito-2-conceptualizacion/README-HITO2.md)

**Qué hicimos**:
- Crear templates mejorados (YAML v3 + OTTR)
- Documentar ontologías a reutilizar
- Definir competency questions
- Generar ejemplos ejecutables (POC Biblioteca)

**Deliverables completados** ✅:
- `concept-template-v3.yaml` (16 secciones enriquecidas)
- `definition-template-v3.md` (ISO 704 intensional + Gruber axioms)
- `reuse-assessment.md` (6 ontologías evaluadas, 73% ahorro)
- `competency-questions.md` (5 CQs + SPARQL 1.1)
- `gaps-detallado.md` (14 gaps con roadmap, 6 P0 completados)
- `prefixes.ttl` (namespaces centralizados para OTTR)
- `ottr-templates/` (2 templates: concept + relation)
- `instances/` (34 instanciaciones: 15 conceptos + 19 relaciones)
- `output/library-ontology-example.ttl` (ejemplo TTL ~200 triples)

**Resultados clave**:
- Template Melquisedec v3 integra: ISO 704 + SKOS + OWL 2 DL + OTTR + DDD
- Cobertura: 78% con ontologías estándar reutilizadas
- ROI: 73% reducción esfuerzo (15h→4h) con automatización OTTR
- 6/8 gaps P0 resueltos (multilingual, axioms, reuse, CQs, OTTR, modularización)

---

### 🔄 HITO 3: Implementation & POC Integration (60% COMPLETADO)

**📖 Guía**: [hito-3-implementacion/README-HITO3.md](./hito-3-implementacion/README-HITO3.md)

**Qué estamos haciendo**:
- Implementar pipeline CI/CD para validación automática
- Crear scripts de validación (ROBOT, pySHACL, SPARQL)
- Entrenar modelo PyKEEN para embeddings semánticos
- Evaluar calidad con métricas estándar (Hits@10, MR, MRR)

**Deliverables completados** ✅:
- `.github/workflows/ontology-validation.yml` (CI/CD GitHub Actions)
- `validation-scripts/run_robot.sh` (OWL consistency check)
- `validation-scripts/run_shacl.py` (constraint validation)
- `validation-scripts/run_sparql_tests.py` (CQ automation)
- `shacl-shapes/concept-shapes.ttl` (7 shapes: Libro, Autor, Préstamo, etc.)
- `embedding-experiment/pykeen_config.yaml` (TransE config)
- `embedding-experiment/train_embeddings.py` (training script)
- `embedding-experiment/evaluate_embeddings.py` (metrics + t-SNE viz)

**Deliverables pendientes** ⏳:
- Ejecutar pipeline en GitHub Actions (primer PR)
- Generar reportes de validación (HTML + JSON)
- Entrenar modelo PyKEEN con biblioteca-ontology.ttl
- Generar visualización t-SNE de embeddings

**Progreso**: 60% completado
- Pipeline configurado (3 etapas: ROBOT + SHACL + SPARQL)
- Scripts listos para ejecución local y CI/CD
- Experimento PyKEEN preparado (TransE, 100 dims, 500 epochs)

---

### 🔄 HITO 2: Conceptualization & Template Enrichment (EN PROGRESO)

**Deliverables:**
- ✅ `templates-proposals/ottr-templates/` (2 templates OTTR)
- ✅ `competency-questions.md` (5 CQs con SPARQL)
- ✅ `research/ottr-instantiation-format-research.md` (investigación formato instanciación)
- ✅ `instances/*.ottrinst` (instanciaciones de ejemplo POC Biblioteca)
- ⏳ `output/library-ontology.ttl` (TTL generado vía Lutra)
- ⏳ `03-gaps-y-propuestas-aoem-v3.md` (análisis detallado de gaps)
- ⏳ Actualización de `concept.yaml` template v3
- ⏳ Creación de `definition.md` template v3 (ISO 704 + Gruber axioms)

**Estado actual:**
- Templates OTTR creados con sintaxis estándar OTTR/stOTTR
- CQs testeables con SPARQL 1.1 sobre POC Biblioteca
- **Decisión de formato**: TTL + .ottrinst (fundamentado en filosofía OTTR oficial)

---

### ⏳ HITO 3: Implementation & POC Integration (PENDIENTE)

**Deliverables:**
- `04-integracion-poc.md`: Integration plan with library-ontology.ttl
- `05-ci-pipeline-example.yml`: GitHub Actions snippet (ROBOT + pySHACL + CQ-tests)
- Embedding experiment report (PyKEEN/RDF2Vec con precision@k)

---

### ⏳ HITO 4: Governance & Final AOEM v3 Draft (PENDIENTE)

**Deliverables:**
- `06-aoem-v3-draft.md`: Final synthesis document
- KPI catalogue (mapping stability %, embedding staleness, CQ pass rate, etc.)
- PR checklist template (human-in-loop + automated checks)
- Governance policy (agent acceptance rules)

---

## 🔬 Investigación: Formato de Instanciación OTTR

### Pregunta de Investigación

**¿Guardar solo TTL resultante o TTL + archivos .ottrinst?**

### Respuesta (basada en investigación formal)

**✅ Recomendación: TTL + .ottrinst (ambos formatos)**

#### Fuentes consultadas:
1. **Documentación oficial OTTR** (https://ottr.xyz)
2. **Paper académico**: "Insights from an OTTR-centric Ontology Engineering Methodology" (Blum et al., WOP@ISWC 2023)
3. **Perplexity Reasoning**: Análisis de filosofía de diseño OTTR
4. **Casos de uso industriales**: Grundfos Industrial Ontology Engineering Platform (ISWC 2023)

#### Razones técnicas:

1. **Principio fundamental OTTR** (de ottr.xyz):
   > "Template definitions are kept in a single location and can be updated without changing the instances"
   
   → Esto **requiere** mantener instancias separadas (.ottrinst) para beneficiarse de esta arquitectura

2. **Trazabilidad y debugging**:
   - Solo TTL = "caja negra" (no sabes qué template generó qué axioma)
   - TTL + .ottrinst = trazabilidad completa (cada axioma rastreable a template + parámetros)

3. **Reproducibilidad y evolución**:
   - Con .ottrinst: cambio en template → re-ejecutar Lutra → nuevo TTL (segundos)
   - Sin .ottrinst: cambio en template → re-crear manualmente toda la ontología (horas/días)

4. **Separación de responsabilidades** (del paper):
   - Domain experts gestionan .ottrinst (contenido/datos)
   - Ontology engineers gestionan .ottr (diseño/patrones)
   - Esta separación es CORE en metodología OTTR-centric

5. **CI/CD pipeline óptimo**:
   ```
   .ottrinst + templates → Lutra → TTL → ROBOT validate → pySHACL → CQ tests
   ```
   Version control de .ottrinst documenta cambios de CONTENIDO vs cambios de DISEÑO

6. **Alineación con Template Melquisedec v3**:
   - Ya usamos estructura modular con templates reutilizables
   - .ottrinst complementa strategy existente
   - Facilita integración con AOEM v3 (OTTR es P0 priority en HITO 1)

**Ver detalles completos**: `research/ottr-instantiation-format-research.md`

---

## 🚀 Cómo Usar Este Análisis

### Para Domain Experts:
1. Revisar `01-analisis-resumen.md` (executive summary)
2. Consultar `competency-questions.md` para entender qué se puede consultar
3. Editar instanciaciones en `instances/*.ottrinst` (formato tabular/simple)

### Para Ontology Engineers:
1. Revisar `02-mapeo-aoem-template.md` (mapping matrix con evidencias)
2. Estudiar templates OTTR en `templates-proposals/ottr-templates/`
3. Ejecutar Lutra para generar TTL:
   ```bash
   java -jar lutra.jar \
     --library templates-proposals/ottr-templates/ \
     --input templates-proposals/instances/*.ottrinst \
     --output templates-proposals/output/library-ontology.ttl
   ```
4. Validar con ROBOT + pySHACL + CQ-tests

### Para Stakeholders/Reviewers:
1. Leer este README (overview completo)
2. Revisar deliverables de cada HITO (secuencial)
3. Validar acceptance criteria en validation gates

---

## 📊 Prioridades (de HITO 1 Mapping Matrix)

### P0 (Crítico - 7 items):
1. OTTR templates (≥2) → **COMPLETADO** ✅
2. CQs con SPARQL tests (≥5) → **COMPLETADO** ✅
3. Formal axioms (ISO 704 + Gruber) → **PENDIENTE**
4. Governance policy → **PENDIENTE**
5. CI pipeline (ROBOT + pySHACL) → **PENDIENTE**
6. Embedding lifecycle → **PENDIENTE**
7. KPI catalogue → **PENDIENTE**

### P1 (Alto - 4 items):
1. Mapping maintenance workflow
2. OBDA cost-aware query optimization
3. Explainability/provenance (PROV-O)
4. Agent governance rules

### P2 (Medio - restantes)

---

## 📖 Referencias

### Metodologías:
- **AOEM 2.0**: Agile Ontology Engineering Methodology (5 phases)
- **Template Melquisedec v3**: ISO 704 + SKOS + DDD + EPPO integration
- **OTTR Methodology**: Blum et al. 2023 (WOP@ISWC)

### Estándares:
- **ISO 704**: Terminological definitions (genus proximum + differentia specifica)
- **SKOS**: Simple Knowledge Organization System (W3C Recommendation)
- **OWL 2 DL**: Web Ontology Language (Description Logic profile)
- **SPARQL 1.1**: Query language for RDF

### Herramientas:
- **Lutra**: OTTR reference implementation (Java CLI)
- **ROBOT**: ROBOT is an OBO Tool (ontology automation)
- **pySHACL**: Python SHACL validator
- **PyKEEN**: Python KGE (Knowledge Graph Embeddings) library

---

## 👥 Contribuidores

- **Ontology Engineer**: Análisis AOEM v2, diseño templates OTTR, mapping matrix
- **Domain Expert**: Validación de CQs, documentación template headers, ejemplos POC Biblioteca
- **Research**: Investigación formal OTTR instantiation format (web search + academic papers)

---

## 📝 Changelog

### [0.2.0] - 2026-01-11
- ✅ HITO 2 iniciado: templates OTTR creados
- ✅ CQs con SPARQL tests creados
- ✅ Investigación formato instanciación completada (decisión: TTL + .ottrinst)
- ✅ Estructura de directorios reorganizada

### [0.1.0] - 2026-01-10
- ✅ HITO 1 completado: resumen + mapping matrix
- ✅ Prompt comparativo enriquecido con v3 analysis (9652 lines)
- ✅ 4 HITOS definidos con validation gates

---

## 🔗 Enlaces Relacionados

- [AOEM 2.0 Guide Parte 4](../../aoem-2.0-guia-parte-4-workflows.md)
- [AOEM 2.0 Guide Parte 5](../../aoem-2.0-guia-parte-5-ai-frameworks.md)
- [Template Melquisedec v3 Analysis](../analysis-for-create-template_v3-ontology-tooling.md)
- [OTTR Official Site](https://ottr.xyz)
- [Lutra Reference Implementation](https://gitlab.com/ottr/lutra/lutra)

---

**Estado**: 🔄 HITO 2 en progreso | **Próximo paso**: Crear instanciaciones .ottrinst de ejemplo
