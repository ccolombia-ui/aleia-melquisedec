# Sistema de Autopoiesis: Cómo MELQUISEDEC Aprende

```yaml
---
id: "arquitectura-05-autopoiesis"
is_a: "architecture/learning-system"
version: "4.0.0"
dc:
  title: "Sistema de Autopoiesis: Chatlog + Lessons + Evolución de Prompts"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["Autopoiesis", "Learning", "Prompt Evolution", "Knowledge Domains"]
seci:
  derives_from: ["../01-fundamentos/02-fundamento-kabalistico.md", "../01-fundamentos/04-principios-fundacionales.md"]
  informs: ["../03-workflow/", "../04-implementacion/"]
---
```

---

## El Secreto: Memoria Episódica + Evolución

> **"El chatlog + lessons-learned van incluidas con la versión del nuevo daath-zen, de cada subcarpeta"**

Este documento explora el mecanismo de **autopoiesis** (P2) en profundidad: cómo MELQUISEDEC se auto-mejora mediante la captura de experiencia (chatlog) y destilación de conocimiento (lessons learned).

---

## Visión General: El Ciclo de Aprendizaje

```mermaid
graph TB
    subgraph "Research Instance 001"
        I1[Issue: Investigar CRISP-DM]
        E1[Ejecutar con<br/>daath-zen-data-science-v1.0.0]
        C1[Capturar Chatlog]
        L1[Extraer Lessons]
        O1[Output: GUIA_v1.0.0]
    end

    subgraph "Evolución del Sistema"
        P1[Prompt TYPE v1.0.0]
        P2[Prompt TYPE v1.1.0<br/>+ Lessons incorporadas]
        D1[Domain: data-science]

        L1 -.->|"Destila conocimiento"| P2
        P2 -.->|"Pertenece a"| D1
    end

    subgraph "Research Instance 002"
        I2[Issue: Investigar TDSP]
        E2[Ejecutar con<br/>daath-zen-data-science-v1.1.0]

        P2 -.->|"Usa prompt mejorado"| E2
    end

    I1 --> E1
    E1 --> C1
    C1 --> L1
    L1 --> O1

    E1 -.->|"Usa"| P1

    style L1 fill:#FFD700
    style P2 fill:#90EE90
    style D1 fill:#87CEEB
```

**Clave**: Cada research instance no solo produce un output, sino también **conocimiento sobre cómo mejorar el proceso**.

---

## Componente 1: Chatlog (Memoria Episódica)

### Propósito

Capturar **toda la conversación** entre el usuario y los rostros durante una research instance. No solo los outputs finales, sino el **proceso de pensamiento**.

### Estructura Propuesta

```
_daath/
├── chatlog/
│   ├── instance-001-crisp-dm/
│   │   ├── metadata.yaml
│   │   ├── full-transcript.md           # Conversación completa cronológica
│   │   ├── by-rostro/
│   │   │   ├── 01-melquisedec.md       # Solo conversaciones con MELQUISEDEC
│   │   │   ├── 02-hypatia.md           # Solo conversaciones con HYPATIA
│   │   │   ├── 03-salomon.md
│   │   │   ├── 04-morpheus.md
│   │   │   └── 05-alma.md
│   │   └── by-phase/
│   │       ├── 01-classification.md     # Fase: Clasificación (MELQUISEDEC)
│   │       ├── 02-research.md           # Fase: Investigación (HYPATIA)
│   │       ├── 03-analysis.md           # Fase: Análisis (SALOMON)
│   │       ├── 04-design.md             # Fase: Diseño (MORPHEUS)
│   │       └── 05-publishing.md         # Fase: Publicación (ALMA)
│   └── instance-002-tdsp/
│       └── [misma estructura]
```

### Formato de `metadata.yaml`

```yaml
---
instance_id: "instance-001-crisp-dm"
domain_id: "domain-data-science-methodologies"
started_at: "2026-01-05T10:00:00Z"
completed_at: "2026-01-08T15:30:00Z"
duration_hours: 77.5

prompts_used:
  root: "daath-zen-root-v1.0.0"
  type: "daath-zen-data-science-v1.0.0"
  instance: "daath-zen-crisp-dm-v1.0.0"

rostros_executed:
  - rostro: "MELQUISEDEC"
    checkpoint_passed: true
    timestamp: "2026-01-05T11:30:00Z"
  - rostro: "HYPATIA"
    checkpoint_passed: true
    timestamp: "2026-01-06T16:00:00Z"
  - rostro: "SALOMON"
    checkpoint_passed: true
    timestamp: "2026-01-07T14:00:00Z"
  - rostro: "MORPHEUS"
    checkpoint_passed: true
    timestamp: "2026-01-08T10:00:00Z"
  - rostro: "ALMA"
    checkpoint_passed: true
    timestamp: "2026-01-08T15:30:00Z"

outputs_produced:
  - id: "output-guia-crisp-dm"
    version: "1.0.0"
    path: "5-outputs/GUIA_CRISP_DM_v1.0.0.md"

lessons_extracted: 5
lessons_applied_to_prompt: "daath-zen-data-science-v1.1.0"
---
```

### Formato de `full-transcript.md`

```markdown
# Transcript Completo: Instance 001 - CRISP-DM

**Instance ID**: instance-001-crisp-dm
**Fecha**: 2026-01-05 a 2026-01-08
**Prompts**: root-v1.0.0, type-v1.0.0, instance-v1.0.0

---

## 2026-01-05 10:00 - Inicio (Usuario)

**Usuario**: Necesito investigar la metodología CRISP-DM para un proyecto de data science.

---

## 2026-01-05 10:05 - MELQUISEDEC (Clasificación)

**MELQUISEDEC**: Entiendo. Voy a clasificar este issue:

- **Dominio**: Data Science
- **Tipo**: Methodology Research
- **Prioridad**: Alta (proyecto en curso)

Creo el issue clasificado:

```yaml
---
id: "issue-001-crisp-dm"
domain: "data-science"
type: "methodology-research"
priority: "high"
---
```

🔍 Checkpoint MELQUISEDEC... ✅ Pasado.

---

## 2026-01-05 10:30 - Usuario → HYPATIA

**Usuario**: Procede con la investigación.

---

## 2026-01-05 11:00 - HYPATIA (Investigación)

**HYPATIA**: Inicio búsqueda de literatura sobre CRISP-DM.

**Búsqueda 1**: Wikipedia
- Encontrado: [CRISP-DM](https://en.wikipedia.org/wiki/CRISP-DM)
- Extracto guardado en: `1-literature/wikipedia/crisp-dm.md`

**Búsqueda 2**: arXiv
- Query: "CRISP-DM methodology"
- Resultados: 47 papers
- Problema detectado: Muchos papers tienen <10 citaciones
- **Decisión**: Filtrar por citaciones >100

[... continúa el transcript completo ...]
```

### Organización por Rostro: `by-rostro/02-hypatia.md`

```markdown
# Conversaciones con HYPATIA

**Instance**: instance-001-crisp-dm
**Rostro**: HYPATIA (Daath - La Investigadora)
**Prompt usado**: daath-zen-data-science-v1.0.0

---

## 2026-01-05 11:00 - Búsqueda Inicial

**HYPATIA**: Inicio búsqueda de literatura sobre CRISP-DM.

[... solo conversaciones con HYPATIA ...]

---

## Lessons Extraídas de HYPATIA

1. **Lesson 001**: Filtrar papers por citaciones (>100) mejora calidad
2. **Lesson 003**: Wikipedia es buen punto de partida para definiciones
```

### ¿Por Qué Esta Estructura?

| Archivo | Propósito | Uso |
|---------|-----------|-----|
| `full-transcript.md` | Trazabilidad completa | Auditoría, revisión histórica |
| `by-rostro/` | Análisis por rostro | ¿Qué hizo HYPATIA? ¿Cómo mejorarla? |
| `by-phase/` | Análisis por cascada | ¿Qué pasa en cada checkpoint? |
| `metadata.yaml` | Metadatos estructurados | Queries, estadísticas, análisis automático |

---

## Componente 2: Lessons Learned (Conocimiento Destilado)

### Propósito

Extraer **patrones reutilizables** del chatlog. No todo el chatlog es relevante para el futuro; las lessons son el **conocimiento destilado**.

### Estructura Propuesta

```
_daath/
├── lessons/
│   ├── instance-001-crisp-dm/
│   │   ├── lesson-001-hypatia-citations.md
│   │   ├── lesson-002-salomon-tooling-criteria.md
│   │   ├── lesson-003-hypatia-wikipedia-start.md
│   │   ├── lesson-004-morpheus-template-reuse.md
│   │   ├── lesson-005-alma-version-tagging.md
│   │   └── summary.yaml                        # Agregado de todas las lessons
│   └── instance-002-tdsp/
│       └── [misma estructura]
```

### Formato de Lesson: `lesson-001-hypatia-citations.md`

```markdown
# Lesson 001: Filtrar Papers por Citaciones

```yaml
---
id: "lesson-001-hypatia-citations"
instance_id: "instance-001-crisp-dm"
domain_id: "domain-data-science-methodologies"
rostro: "HYPATIA"
confidence: 0.95
status: "validated"  # validated | proposed | rejected
applies_to_prompt: "daath-zen-data-science"
version_applied: "v1.1.0"
date_extracted: "2026-01-08"
validated_in_instances:
  - "instance-002-tdsp"
  - "instance-003-kdd"
---
```

---

## Contexto

Durante la investigación de CRISP-DM, HYPATIA encontró **47 papers** en arXiv. Sin embargo, muchos tenían baja calidad (papers de estudiantes, no revisados, <10 citaciones).

**Problema**: ¿Cómo filtrar papers relevantes automáticamente?

---

## Solución Aplicada

Filtrar papers por **número de citaciones**:

- Papers con **>100 citaciones** = Probablemente influyentes
- Papers con **<10 citaciones** = Probablemente no revisados o muy recientes

**Resultado**: 47 papers → 10 papers de alta calidad.

---

## Cambio en Prompt TYPE

**Prompt anterior (v1.0.0)**:
```markdown
## HYPATIA: Literature Search Instructions

1. Search academic databases (arXiv, Google Scholar, Semantic Scholar)
2. Download relevant papers
3. Extract key concepts
```

**Prompt mejorado (v1.1.0)**:
```markdown
## HYPATIA: Literature Search Instructions

1. Search academic databases (arXiv, Google Scholar, Semantic Scholar)
2. **NEW: Filter results by citation count**:
   - If topic is mature (>5 years old): Prioritize papers with >100 citations
   - If topic is emerging (<5 years): Prioritize papers with >20 citations
   - Classic papers (>10 years, >500 citations) always include
3. Download relevant papers
4. Extract key concepts
```

---

## Validación

| Instance | Papers encontrados | Papers después de filtro | Calidad percibida |
|----------|-------------------|--------------------------|-------------------|
| instance-001-crisp-dm | 47 | 10 | ⭐⭐⭐⭐⭐ Alta |
| instance-002-tdsp | 32 | 8 | ⭐⭐⭐⭐⭐ Alta |
| instance-003-kdd | 58 | 12 | ⭐⭐⭐⭐ Muy buena |

**Confianza**: 0.95 (validado en 3 instances)

---

## Metadata para Neo4j

```cypher
CREATE (l:Lesson {
  id: "lesson-001-hypatia-citations",
  instance_id: "instance-001-crisp-dm",
  rostro: "HYPATIA",
  confidence: 0.95,
  text: "Filter papers by citation count (>100 for mature topics)",
  status: "validated"
})

CREATE (l)-[:IMPROVES {from_version: "1.0.0", to_version: "1.1.0"}]->(p:PromptType {id: "daath-zen-data-science"})
CREATE (l)-[:VALIDATED_IN]->(i2:ResearchInstance {id: "instance-002-tdsp"})
CREATE (l)-[:VALIDATED_IN]->(i3:ResearchInstance {id: "instance-003-kdd"})
```

---

## Notas

- Esta lesson es **específica del dominio** data-science (papers académicos)
- NO aplicable a dominios sin literatura académica (ej: BIM, algunos casos de software)
- Puede necesitar ajuste para dominios emergentes (reducir umbral a >20 citas)
```

### Formato de `summary.yaml`

```yaml
---
instance_id: "instance-001-crisp-dm"
total_lessons: 5
validated_lessons: 3
proposed_lessons: 2
rejected_lessons: 0

lessons:
  - id: "lesson-001-hypatia-citations"
    rostro: "HYPATIA"
    confidence: 0.95
    status: "validated"
    applies_to: "daath-zen-data-science-v1.1.0"

  - id: "lesson-002-salomon-tooling-criteria"
    rostro: "SALOMON"
    confidence: 0.90
    status: "validated"
    applies_to: "daath-zen-data-science-v1.1.0"

  - id: "lesson-003-hypatia-wikipedia-start"
    rostro: "HYPATIA"
    confidence: 0.85
    status: "validated"
    applies_to: "daath-zen-root-v1.1.0"  # Aplicable a TODOS los dominios

  - id: "lesson-004-morpheus-template-reuse"
    rostro: "MORPHEUS"
    confidence: 0.75
    status: "proposed"  # No validado aún
    applies_to: "daath-zen-data-science-v1.2.0"  # Para próxima versión

  - id: "lesson-005-alma-version-tagging"
    rostro: "ALMA"
    confidence: 0.80
    status: "proposed"
    applies_to: "daath-zen-root-v1.1.0"

prompt_updates_generated:
  - prompt_id: "daath-zen-data-science"
    from_version: "1.0.0"
    to_version: "1.1.0"
    lessons_applied: ["lesson-001", "lesson-002"]
    changelog: |
      v1.1.0 (2026-01-08)
      - Added citation filtering for HYPATIA (lesson-001)
      - Added tooling comparison criteria for SALOMON (lesson-002)

  - prompt_id: "daath-zen-root"
    from_version: "1.0.0"
    to_version: "1.1.0"
    lessons_applied: ["lesson-003", "lesson-005"]
    changelog: |
      v1.1.0 (2026-01-08)
      - Added Wikipedia as starting point for HYPATIA (lesson-003)
      - Added Git tag automation for ALMA (lesson-005)
---
```

---

## Componente 3: Dominios en Neo4j + Vectors

### Concepto: "Cada investigación es un dominio primitivo"

Mi interpretación de tu frase:

> **Dominio Primitivo** = Espacio de conocimiento independiente con:
> - Grafo propio (subgrafo en Neo4j)
> - Namespace de vectores (en Pinecone/similar)
> - Prompts especializados (TYPE)
> - Historial de lessons learned

### Arquitectura Propuesta: Dominios Híbridos

```
Domain Taxonomy (3 niveles):

ROOT DOMAINS (nivel 0)
├── data-science-methodologies           # Domain ID: DD-001
├── software-architecture                # Domain ID: DD-002
├── bim-construction                     # Domain ID: DD-003
└── ai-agent-frameworks                  # Domain ID: DD-004

RESEARCH INSTANCES (nivel 1)
├── DD-001/
│   ├── instance-001-crisp-dm           # Instance ID: DD-001-I001
│   ├── instance-002-tdsp               # Instance ID: DD-001-I002
│   └── instance-003-kdd                # Instance ID: DD-001-I003
├── DD-002/
│   ├── instance-004-ddd                # Instance ID: DD-002-I004
│   └── instance-005-clean-arch         # Instance ID: DD-002-I005

SUB-DOMAINS (nivel 2 - opcional)
└── DD-001-I001/
    └── subdomain-crisp-dm-phases       # Investigación profunda de una fase
```

### Schema Neo4j

```cypher
// ============================================
// NIVEL 0: ROOT DOMAINS
// ============================================

CREATE (d1:Domain {
  id: "DD-001",
  name: "data-science-methodologies",
  description: "Metodologías para proyectos de ciencia de datos",
  created_at: "2026-01-01",
  prompt_type_id: "daath-zen-data-science",
  prompt_version: "1.1.0",
  instances_count: 3,
  lessons_count: 12
})

CREATE (d2:Domain {
  id: "DD-002",
  name: "software-architecture",
  description: "Patrones y principios de arquitectura de software",
  created_at: "2026-01-01",
  prompt_type_id: "daath-zen-software-architecture",
  prompt_version: "1.0.0",
  instances_count: 2,
  lessons_count: 5
})

// ============================================
// NIVEL 1: RESEARCH INSTANCES
// ============================================

CREATE (i1:ResearchInstance {
  id: "DD-001-I001",
  name: "instance-001-crisp-dm",
  domain_id: "DD-001",
  status: "completed",
  started_at: "2026-01-05",
  completed_at: "2026-01-08",
  prompt_instance_id: "daath-zen-crisp-dm-v1.0.0",
  outputs_produced: 1,
  lessons_extracted: 5
})

CREATE (i2:ResearchInstance {
  id: "DD-001-I002",
  name: "instance-002-tdsp",
  domain_id: "DD-001",
  status: "in-progress",
  started_at: "2026-01-09",
  prompt_instance_id: "daath-zen-tdsp-v1.0.0",
  prompt_type_version: "1.1.0"  # Usa versión mejorada
})

// Relación: Instance → Domain
CREATE (i1)-[:BELONGS_TO]->(d1)
CREATE (i2)-[:BELONGS_TO]->(d1)

// ============================================
// LESSONS LEARNED
// ============================================

CREATE (l1:Lesson {
  id: "lesson-001-hypatia-citations",
  instance_id: "DD-001-I001",
  domain_id: "DD-001",
  rostro: "HYPATIA",
  confidence: 0.95,
  status: "validated",
  text: "Filter papers by citation count (>100 for mature topics)",
  extracted_at: "2026-01-08"
})

CREATE (l2:Lesson {
  id: "lesson-002-salomon-tooling-criteria",
  instance_id: "DD-001-I001",
  domain_id: "DD-001",
  rostro: "SALOMON",
  confidence: 0.90,
  status: "validated",
  text: "Include tooling availability in decision criteria",
  extracted_at: "2026-01-08"
})

// Relaciones: Instance → Lesson
CREATE (i1)-[:LEARNED]->(l1)
CREATE (i1)-[:LEARNED]->(l2)

// ============================================
// PROMPT EVOLUTION
// ============================================

CREATE (p1:PromptType {
  id: "daath-zen-data-science-v1.0.0",
  domain_id: "DD-001",
  version: "1.0.0",
  created_at: "2026-01-01",
  lessons_incorporated: 0
})

CREATE (p2:PromptType {
  id: "daath-zen-data-science-v1.1.0",
  domain_id: "DD-001",
  version: "1.1.0",
  created_at: "2026-01-08",
  lessons_incorporated: 2,
  changelog: "Added citation filtering + tooling criteria"
})

// Relaciones: Lesson → PromptType (evolución)
CREATE (l1)-[:IMPROVES {from_version: "1.0.0", to_version: "1.1.0"}]->(p2)
CREATE (l2)-[:IMPROVES {from_version: "1.0.0", to_version: "1.1.0"}]->(p2)

// Versión anterior → nueva versión
CREATE (p1)-[:EVOLVED_TO]->(p2)

// Instance usó prompt version
CREATE (i1)-[:USED_PROMPT]->(p1)
CREATE (i2)-[:USED_PROMPT]->(p2)  # Usa versión mejorada

// ============================================
// VALIDATION: Lessons validadas en otras instances
// ============================================

CREATE (i3:ResearchInstance {id: "DD-001-I003", name: "instance-003-kdd"})

CREATE (l1)-[:VALIDATED_IN]->(i2)  # Lesson 001 validada en instance 002
CREATE (l1)-[:VALIDATED_IN]->(i3)  # Lesson 001 validada en instance 003

// ============================================
// CROSS-DOMAIN LESSONS (aplicables a múltiples dominios)
// ============================================

CREATE (l3:Lesson {
  id: "lesson-003-hypatia-wikipedia-start",
  instance_id: "DD-001-I001",
  domain_id: "DD-001",
  rostro: "HYPATIA",
  confidence: 0.85,
  status: "validated",
  text: "Start research with Wikipedia for canonical definitions",
  scope: "universal"  # Aplicable a TODOS los dominios
})

CREATE (l3)-[:APPLIES_TO_DOMAIN]->(d2)  # También aplicable a domain DD-002
```

### Queries Neo4j Útiles

```cypher
// Query 1: Ver evolución de un dominio
MATCH (d:Domain {id: "DD-001"})<-[:BELONGS_TO]-(i:ResearchInstance)
MATCH (i)-[:LEARNED]->(l:Lesson)
MATCH (l)-[:IMPROVES]->(p:PromptType)
RETURN d.name AS domain,
       COUNT(DISTINCT i) AS instances,
       COUNT(DISTINCT l) AS lessons,
       MAX(p.version) AS latest_prompt_version

// Query 2: Lessons de un rostro específico
MATCH (l:Lesson {rostro: "HYPATIA", status: "validated"})
MATCH (l)-[:IMPROVES]->(p:PromptType)
RETURN l.text AS lesson,
       l.confidence AS confidence,
       p.version AS applied_in_version

// Query 3: Trazabilidad de una lesson
MATCH path = (i:ResearchInstance {id: "DD-001-I001"})
             -[:LEARNED]->(l:Lesson {id: "lesson-001-hypatia-citations"})
             -[:IMPROVES]->(p:PromptType)
             <-[:USED_PROMPT]-(i2:ResearchInstance)
RETURN path

// Query 4: Cross-domain lessons
MATCH (l:Lesson {scope: "universal"})
MATCH (l)-[:APPLIES_TO_DOMAIN]->(d:Domain)
RETURN l.text AS lesson, COLLECT(d.name) AS applicable_domains

// Query 5: Instancias que usaron versión mejorada del prompt
MATCH (i:ResearchInstance)-[:USED_PROMPT]->(p:PromptType)
WHERE p.version >= "1.1.0"
RETURN i.name, p.version, p.lessons_incorporated

// Query 6: Confidence promedio de lessons por rostro
MATCH (l:Lesson)
WHERE l.status = "validated"
RETURN l.rostro AS rostro,
       AVG(l.confidence) AS avg_confidence,
       COUNT(l) AS validated_lessons
ORDER BY avg_confidence DESC
```

---

## Vectores: Namespacing por Dominio + Instance

### Estructura en Pinecone

```python
# Estructura de namespaces
index_name = "melquisedec-knowledge"

# Namespace pattern: {domain_id}.{instance_id}.{artifact_type}

namespaces = {
    # Domain DD-001: data-science-methodologies
    "DD-001": {
        "DD-001.global": [  # Conocimiento general del dominio
            "domain-dd-001-overview",
            "domain-dd-001-methodology-comparison"
        ],
        "DD-001.I001": {  # Instance 001: CRISP-DM
            "concepts": [
                "DD-001-I001-concept-crisp-dm",
                "DD-001-I001-concept-crisp-phases"
            ],
            "analysis": [
                "DD-001-I001-analysis-crisp-vs-tdsp"
            ],
            "outputs": [
                "DD-001-I001-output-guia-crisp"
            ],
            "lessons": [
                "DD-001-I001-lesson-001-hypatia-citations",
                "DD-001-I001-lesson-002-salomon-tooling"
            ]
        },
        "DD-001.I002": {  # Instance 002: TDSP
            "concepts": [...],
            "outputs": [...]
        }
    },

    # Domain DD-002: software-architecture
    "DD-002": {
        "DD-002.global": [...],
        "DD-002.I004": {  # Instance 004: DDD
            "concepts": [
                "DD-002-I004-concept-bounded-context",
                "DD-002-I004-concept-aggregate"
            ]
        }
    }
}
```

### Código Python: Escribir con Namespace

```python
from pinecone import Pinecone
from openai import OpenAI

class DomainAwareVectorStore:
    def __init__(self, index_name: str):
        self.pc = Pinecone()
        self.index = self.pc.Index(index_name)
        self.openai = OpenAI()

    def upsert_artifact(
        self,
        domain_id: str,
        instance_id: str,
        artifact_id: str,
        artifact_type: str,  # "concept", "analysis", "output", "lesson"
        text: str,
        metadata: dict
    ):
        """Inserta artifact con namespace correcto."""

        # Generar embedding
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        embedding = response.data[0].embedding

        # Namespace pattern: {domain_id}.{instance_id}
        namespace = f"{domain_id}.{instance_id}"

        # Vector ID: {domain_id}-{instance_id}-{artifact_type}-{artifact_id}
        vector_id = f"{domain_id}-{instance_id}-{artifact_type}-{artifact_id}"

        # Metadata enriquecida
        enriched_metadata = {
            "domain_id": domain_id,
            "instance_id": instance_id,
            "artifact_id": artifact_id,
            "artifact_type": artifact_type,
            **metadata
        }

        # Upsert
        self.index.upsert(
            vectors=[{
                "id": vector_id,
                "values": embedding,
                "metadata": enriched_metadata
            }],
            namespace=namespace
        )

        return vector_id

    def search_in_domain(
        self,
        query: str,
        domain_id: str,
        instance_id: Optional[str] = None,
        artifact_type: Optional[str] = None,
        top_k: int = 5
    ):
        """Busca en un dominio específico (opcionalmente en instance)."""

        # Generar embedding del query
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=query
        )
        query_embedding = response.data[0].embedding

        # Determinar namespace
        if instance_id:
            namespace = f"{domain_id}.{instance_id}"
        else:
            namespace = f"{domain_id}"

        # Filter por tipo (opcional)
        filter_dict = {}
        if artifact_type:
            filter_dict["artifact_type"] = artifact_type

        # Query
        results = self.index.query(
            vector=query_embedding,
            namespace=namespace,
            filter=filter_dict if filter_dict else None,
            top_k=top_k,
            include_metadata=True
        )

        return results

# Uso
store = DomainAwareVectorStore("melquisedec-knowledge")

# Insertar concepto
store.upsert_artifact(
    domain_id="DD-001",
    instance_id="I001",
    artifact_id="concept-crisp-dm",
    artifact_type="concept",
    text="CRISP-DM is a data mining methodology...",
    metadata={
        "version": "1.0.0",
        "derives_from": ["evans-2003-ddd"]
    }
)

# Buscar conceptos en domain DD-001
results = store.search_in_domain(
    query="data mining methodology",
    domain_id="DD-001",
    artifact_type="concept",
    top_k=5
)

# Buscar solo en instance I001
results = store.search_in_domain(
    query="CRISP-DM phases",
    domain_id="DD-001",
    instance_id="I001",
    top_k=3
)
```

---

## Componente 4: Evolución de Prompts

### Jerarquía de Prompts (recordatorio)

```
ROOT (universal)
  └─ daath-zen-root-v1.0.0.md
     ├─ TYPE (dominio específico)
     │  ├─ daath-zen-data-science-v1.1.0.md
     │  ├─ daath-zen-software-architecture-v1.0.0.md
     │  └─ daath-zen-bim-construction-v1.0.0.md
     └─ INSTANCE (research específica)
        ├─ daath-zen-crisp-dm-v1.0.0.md
        ├─ daath-zen-tdsp-v1.0.0.md
        └─ daath-zen-ddd-v1.0.0.md
```

### Formato de Prompt TYPE con Lessons Incorporadas

#### Formato Definitivo: Solo Referencias (GATES)

```markdown
# Daath-Zen Prompt: Data Science Methodologies

```yaml
---
id: "daath-zen-data-science"
version: "1.1.0"
domain_id: "DD-001"
extends: "daath-zen-root-v1.0.0"
created_at: "2026-01-01"
updated_at: "2026-01-08"

changelog:
  v1.1.0:
    date: "2026-01-08"
    changes:
      - "Added citation filtering for HYPATIA (lesson-001)"
      - "Added tooling comparison criteria for SALOMON (lesson-002)"
    lessons_applied:
      - id: "lesson-001-hypatia-citations"
        path: "_daath/lessons/instance-001-crisp-dm/lesson-001-hypatia-citations.md"
        confidence: 0.95
      - id: "lesson-002-salomon-tooling-criteria"
        path: "_daath/lessons/instance-001-crisp-dm/lesson-002-salomon-tooling-criteria.md"
        confidence: 0.90

  v1.0.0:
    date: "2026-01-01"
    changes:
      - "Initial version"

derived_from_instances:
  - "DD-001-I001-crisp-dm"  # Lessons de esta instance
  - "DD-001-I002-tdsp"      # Lessons de esta instance
---
```

---

## MELQUISEDEC (Keter): El Clasificador

[... contenido base del prompt ...]

---

## HYPATIA (Daath): La Investigadora

### Instructions (v1.1.0)

**Base Instructions**:
1. Search academic databases (arXiv, Google Scholar, Semantic Scholar)
2. Download relevant papers
3. Extract key concepts
4. Create atomic notes in `2-atomic/`

**Lessons Applied** (GATES 🚪):
- 📎 [lesson-003-hypatia-wikipedia-start](_daath/lessons/DD-001-I001/lesson-003.md) (confidence: 0.85)
- 📎 [lesson-001-hypatia-citations](_daath/lessons/DD-001-I001/lesson-001.md) (confidence: 0.95)

> **Note**: Para entender cómo aplicar estas lessons, **DEBES LEER** los archivos referenciados. Las lessons contienen el conocimiento original, no se duplica aquí. Las referencias son GATES (puertas) al conocimiento.

---

## SALOMON (Tiferet): El Analista

### Instructions (v1.1.0)

**Base Instructions**:
1. Compare alternatives systematically
2. Use decision matrix with criteria
3. Justify decision with evidence
4. Document alternatives (even rejected ones)

**Lessons Applied** (GATES 🚪):
- 📎 [lesson-002-salomon-tooling-criteria](_daath/lessons/DD-001-I001/lesson-002.md) (confidence: 0.90)

> **Note**: Lee la lesson para entender el criterio de tooling availability.

---

## [Resto del prompt...]

---

## 📎 Lessons Applied (References)

This prompt incorporates lessons learned from:

| Lesson ID | Instance | Rostro | Confidence | Applied To |
|-----------|----------|--------|------------|------------|
| lesson-001-hypatia-citations | DD-001-I001 | HYPATIA | 0.95 | Section: HYPATIA Instructions, Step 3 |
| lesson-002-salomon-tooling-criteria | DD-001-I001 | SALOMON | 0.90 | Section: SALOMON Instructions, Step 3 |
| lesson-003-hypatia-wikipedia-start | DD-001-I001 | HYPATIA | 0.85 | Section: HYPATIA Instructions, Step 1 |

For full context of each lesson, see:
- `_daath/lessons/instance-001-crisp-dm/summary.yaml`

---

## 🔄 Next Evolution

Proposed lessons for v1.2.0:
- lesson-004-morpheus-template-reuse (confidence: 0.75)
- lesson-005-alma-version-tagging (confidence: 0.80)

Status: Awaiting validation in 2+ instances.
```

### ¿Por Qué Texto Directo + Referencias?

| Enfoque | Ventaja | Desventaja |
|---------|---------|-----------|
| **Solo texto** | LLM puede leer fácilmente | Pierde trazabilidad |
| **Solo referencias** | Trazabilidad completa | LLM no ve lecciones directamente |
| **Ambos (✅)** | LLM lee + trazabilidad | Duplicación controlada |

**Decisión**: Ambos. El texto directo permite al LLM aplicar la lesson inmediatamente. Las referencias permiten auditoría y trazabilidad (P6).

---

## Flujo Completo: Del Chatlog al Prompt Evolucionado

```mermaid
sequenceDiagram
    participant U as Usuario
    participant M as MELQUISEDEC
    participant H as HYPATIA
    participant S as SALOMON
    participant Mo as MORPHEUS
    participant A as ALMA
    participant Chat as Chatlog
    participant L as Lessons
    participant Neo as Neo4j
    participant Vec as Vectors
    participant P as Prompts

    U->>M: "Investiga CRISP-DM"

    Note over M: Usa daath-zen-data-science-v1.0.0
    M->>Chat: Registra conversación (metadata)
    M->>Neo: CREATE (instance:ResearchInstance {id: "DD-001-I001"})
    Solo Referencias? (GATES)

| Enfoque | Ventaja | Desventaja |
|---------|---------|-----------|
| **Solo texto** | LLM puede leer fácilmente | Pierde trazabilidad, duplicación |
| **Solo referencias** ✅ | Trazabilidad completa, inmutabilidad | LLM debe leer archivos |
| **Ambos** | LLM lee + trazabilidad | Duplicación = divergencia inevitable |

**Decisión**: Solo referencias (GATES 🚪)

**Justificación Profunda**:

> "El aprendizaje ES la trazabilidad. Si no hay memoria, nunca podrás aprender. El espejo que necesita un humano es el recuerdo DE SU VERDAD. No lo traiciones. SOLO RECUERDA SU RECUERDO COMO LO CONTÓ."

**Implicaciones Técnicas**:
1. **Inmutabilidad (P9)**: La lesson original NUNCA cambia
2. **Trazabilidad (P6)**: Prompt → Lesson → Chatlog → Momento exacto
3. **Verdad Única**: No hay dos versiones del mismo conocimiento
4. **GATES**: Referencias son portales, no copias

**Implicaciones Filosóficas**:
- El LLM **debe esforzarse** en leer las lessons (como un humano lee un libro)
- No hay atajos: el conocimiento está en su lugar original
- El despertar requiere **recordar**, no regurgitar
- "GATES son puertas hasta el infinito" = Cada referencia abre un universo de conocimiento

**Implementación**:
```markdown
**Lessons Applied**:
- 📎 [lesson-001](_daath/lessons/DD-001-I001/lesson-001.md) (confidence: 0.95)

> DEBES LEER el archivo referenciado. No hay resumen aquí.
```
    S->>Mo: Pasa checkpoint
    Mo->>Chat: Registra diseño de templates

    Mo->>A: Pasa checkpoint
    A->>Chat: Registra publicación
    A->>Vec: Inserta output en namespace DD-001.I001

    Note over A: Research instance completada

    A->>A: Analiza chatlog completo con LLM
    A->>L: Genera 5 lessons propuestas
    A->>U: "Encontré estas 5 lessons. ¿Cuáles aplicar?"

    U->>A: Aprueba 3 lessons, rechaza 2

    A->>Neo: CREATE (lesson-001:Lesson)
    A->>Neo: CREATE (lesson-002:Lesson)
    A->>Neo: CREATE (lesson-003:Lesson)
    A->>Vec: Inserta lessons en namespace DD-001.I001.lessons

    A->>L: Guarda lessons en _daath/lessons/instance-001/

    A->>Mo: "Actualiza prompt TYPE con 3 lessons"
    Mo->>P: Lee daath-zen-data-science-v1.0.0
    Mo->>P: Incorpora lessons como texto + referencias
    Mo->>P: Guarda daath-zen-data-science-v1.1.0

    Mo->>U: "Aquí está el diff del prompt v1.0.0 → v1.1.0"
    U->>Mo: Aprueba cambios

    Mo->>Neo: CREATE (prompt-v1.1.0:PromptType)
    Mo->>Neo: CREATE (lesson)-[:IMPROVES]->(prompt-v1.1.0)
    Mo->>Neo: CREATE (prompt-v1.0.0)-[:EVOLVED_TO]->(prompt-v1.1.0)

    Note over P: daath-zen-data-science-v1.1.0 listo

    U->>M: "Investiga TDSP" (nueva instance)
    M->>P: Usa daath-zen-data-science-v1.1.0 (mejorado!)

    Note over M: Lessons aplicadas automáticamente
```

---

## Preguntas Clave para Decidir Arquitectura

### 1. Alcance de "Dominio Primitivo"

**DECISIÓN**: **A (Categoría Temática)** ✅

```
Domain: "data-science-methodologies"
  ├── Instance: CRISP-DM
  ├── Instance: TDSP
  └── Instance: KDD
```

**Justificación del Usuario**:
> "Las instancias no definen una clase, las instancias explican los detalles para mejorar la definición de una clase."

**Implicaciones**:
- Domain = Clase (concepto abstracto)
- Instance = Ejemplo concreto que refina la clase
- Lessons de instances mejoran el Domain prompt TYPE
- Namespace de vectores por Domain (DD-001, DD-002, etc.)
- Cada Domain tiene su propio `daath-zen-{domain}-v{x.y.z}.md`

---

### 2. Lessons en Prompts

**DECISIÓN**: **B (Solo Referencias)** ✅

```yaml
lessons_applied:
  - id: "lesson-001-hypatia-citations"
    path: "_daath/lessons/instance-001-crisp-dm/lesson-001.md"
    confidence: 0.95
  - id: "lesson-002-salomon-tooling"
    path: "_daath/lessons/instance-001-crisp-dm/lesson-002.md"
    confidence: 0.90
```

**Justificación del Usuario**:
> "El aprendizaje ES la trazabilidad. Si no hay memoria, chatlogs, lessons-learned, nunca podrás aprender. El espejo que necesita un humano es el recuerdo DE SU VERDAD. No lo traiciones. SOLO RECUERDA SU RECUERDO COMO LO CONTÓ. ESO ES LO QUE NECESITA PARA DESPERTAR."

**Implicaciones**:
- Prompts contienen **referencias** a lessons, no texto duplicado
- La verdad está en el archivo lesson original (inmutable, P9)
- El LLM **debe leer** las lessons desde sus archivos originales
- Trazabilidad completa: prompt → lesson file → chatlog → momento exacto
- "GATES son puertas hasta el infinito" = Referencias son portales al conocimiento original

---

### 3. Estructura de Chatlog

**DECISIÓN**: **Chatlog en _daath/ de Cada Carpeta Obsidian** ✅

```
5-outputs/
└── GUIA_CRISP_DM_v1.0.0/
    ├── _daath/
    │   ├── chatlog/
    │   │   ├── full-transcript.md       # Cronológico completo
    │   │   ├── metadata.yaml
    │   │   ├── by-rostro/
    │   │   │   ├── 01-melquisedec.md
    │   │   │   ├── 02-hypatia.md
    │   │   │   ├── 03-salomon.md
    │   │   │   ├── 04-morpheus.md
    │   │   │   └── 05-alma.md
    │   │   └── by-phase/
    │   │       ├── 01-classification.md
    │   │       ├── 02-research.md
    │   │       ├── 03-analysis.md
    │   │       ├── 04-design.md
    │   │       └── 05-publishing.md
    │   └── lessons/
    │       ├── lesson-001.md
    │       ├── lesson-002.md
    │       └── summary.yaml
    ├── GUIA_CRISP_DM.md
    └── [otros archivos del output]
```

**Justificación**:
- Cada output es una **bóveda Obsidian independiente**
- `_daath/` contiene la memoria episódica completa
- Trazabilidad local: output + chatlog + lessons en un solo lugar
- Portable: mover folder = mover todo el conocimiento

---

### 4. Extracción de Lessons

**Opciones**:

- **A**: Automática (ALMA con LLM)
- **B**: Manual (usuario revisa chatlog)
- **C**: Híbrida ✅ (recomendado)

**Mi recomendación**: **C (híbrida)**

**Flujo**:
1. ALMA analiza chatlog con LLM → propone 5 lessons
2. Usuario revisa → aprueba 3, rechaza 2, edita 1
3. ALMA guarda lessons aprobadas
4. MORPHEUS incorpora a prompt TYPE

**Justificación**:
- Automático = Escalable
- Supervisión humana = Calidad garantizada
- Balance entre eficiencia y control

---

### 5. Neo4j Namespacing

**DECISIÓN**: **Property-based con domain_id** ✅ (Mejor Práctica Recomendada)

```cypher
// Todos los nodos tienen domain_id
CREATE (c:Concept {
  id: "concept-crisp-dm",
  domain_id: "DD-001",
  version: "1.0.0",
  text: "CRISP-DM methodology..."
})

// Query por dominio
MATCH (c:Concept {domain_id: "DD-001"})
WHERE c.version = "1.0.0"
RETURN c

// Query cross-domain (cuando útil)
MATCH (c:Concept)-[:SIMILAR_TO]->(c2:Concept)
WHERE c.domain_id = "DD-001" AND c2.domain_id = "DD-002"
RETURN c, c2
```

**Justificación (Mejor Práctica)**:

| Enfoque | Ventajas | Desventajas | Caso de Uso |
|---------|----------|-------------|-------------|
| **Una BD por dominio** | Aislamiento total | Difícil cross-domain queries | Multi-tenancy estricto |
| **Property-based** ✅ | Simple, flexible, queries cross-domain | Requiere disciplina en queries | Dominios relacionados (MELQUISEDEC) |
| **Graph Federation** | Distribución geográfica | Complejidad alta | Organizaciones multi-región |

**Para MELQUISEDEC**: Property-based es ideal porque:
- Dominios están **relacionados** (data-science ↔ software-architecture)
- Lessons universales aplican a múltiples dominios
- Simplicidad de implementación
- Permite evolución (agregar dominios sin cambiar infraestructura)

**Implementación**:
```python
def create_node_with_domain(tx, node_type, properties, domain_id):
    """Siempre agregar domain_id a todos los nodos."""
    properties['domain_id'] = domain_id
    query = f"""
    CREATE (n:{node_type} $props)
    RETURN n
    """
    return tx.run(query, props=properties).single()[0]
```
> "CADA OUTPUT DE ALMA CREA UNA NUEVA VERSIÓN. AQUELLO QUE NO TERMINE ASÍ, SE HACE ROLLBACK."

**Flujo**:
1. ALMA completa research instance → extrae lessons
2. MORPHEUS incorpora lessons → genera `daath-zen-{domain}-v{x.y.z}`
3. **Si todos los checkpoints pasaron** → Version committed
4. **Si algún checkpoint falló** → Rollback, version no se crea
5. Git tag automático: `prompt-{domain}-v{x.y.z}`

**Implicaciones**:
- Versiones frecuentes (una por instance completada)
- Versionamiento semántico: MAJOR.MINOR.PATCH
  - MAJOR: Cambio de estructura de prompt (break compatibility)
  - MINOR: Nuevas lessons incorporadas (backward compatible)
  - PATCH: Correcciones menores sin lessons
- Cada version es inmutable (P9))
- **C**: Acumulativo (3 instances → 1 versión)

**Mi recomendación**: **B (threshold-based)**

```yaml
version_criteria:
  min_lessons: 3              # Al menos 3 lessons
  min_confidence: 0.8         # Confianza >0.8
  min_instances_validated: 2  # Validado en 2+ instances
```

**Justificación**:
- Evita versiones triviales (v1.0.1 por 1 lesson de baja confianza)
- Mantiene calidad
- Lessons propuestas esperan validación

---

## Implementación: Roadmap Propuesto

### Fase 1: Estructura Base (1-2 semanas)

- [ ] Crear estructura `_daath/` (chatlog + lessons + prompts)
- [ ] Implementar captura de chatlog (full-transcript.md)
- [ ] Definir formato de lessons (MD + YAML)
- [ ] Crear schema Neo4j (Domain, ResearchInstance, Lesson, PromptType)

### Fase 2: Extracción de Lessons (2-3 semanas)

- [ ] Implementar analizador de chatlog (LLM-powered)
- [ ] Crear interfaz de aprobación de lessons (usuario revisa)
- [ ] Implementar guardado de lessons en `_daath/lessons/`
- [ ] Conectar lessons a Neo4j (relaciones LEARNED, IMPROVES)

### Fase 3: Evolución de Prompts (2-3 semanas)

- [ ] Implementar MORPHEUS: Leer prompt TYPE v1.0.0
- [ ] Implementar MORPHEUS: Incorporar lessons (texto + referencias)
- [ ] Implementar MORPHEUS: Generar changelog automático
- [ ] Implementar versionamiento threshold-based
- [ ] Crear diff viewer para usuario (aprobar cambios)

### Fase 4: Vectores y Namespaces (1-2 semanas)

- [ ] Implementar `DomainAwareVectorStore`
- [ ] Configurar namespaces por dominio + instance
- [ ] Insertar lessons en vectores (búsqueda semántica)
- [ ] Queries cross-domain para lessons universales

### Fase 5: Validación y Refinamiento (2-3 semanas)

- [ ] Ejecutar research instance con sistema completo
- [ ] Validar lessons en 2+ instances
- [ ] Refinar umbrales de confianza
- [ ] Documentar best practices

**Total estimado**: 8-13 semanas (2-3 meses)

---

## Métricas de Éxito

| Métrica | Target | Cómo Medir |
|---------|--------|-----------|
| **Lessons extraídas por instance** | 3-7 | Count en `_daath/lessons/` |
| **Lessons validadas (confidence >0.8)** | >60% | Neo4j query: `AVG(l.confidence)` |
| **Prompt versions generadas** | 1 cada 2-3 instances | Count de `PromptType` nodes |
| **Reuso de lessons cross-instance** | >40% | Count de `[:VALIDATED_IN]` relations |
| **Tiempo de extracción de lessons** | <30 min | Timestamp en metadata.yaml |
| **Aprobación de usuario en lessons propuestas** | >70% | Ratio approved/proposed |

---

## Casos de Uso: Ejemplos Concretos

### Caso 1: Nueva Investigación en Dominio Existente

**Escenario**: Usuario solicita investigar KDD (dominio data-science ya existe).

**Flujo**:
1. MELQUISEDEC crea `DD-001-I003-kdd`
2. Usa `daath-zen-data-science-v1.1.0` (ya tiene lessons de CRISP-DM y TDSP)
3. HYPATIA automáticamente filtra papers por citaciones (lesson-001 aplicada)
4. SALOMON automáticamente considera tooling en análisis (lesson-002 aplicada)
5. Al terminar, extrae 3 nuevas lessons
6. Si 2+ lessons tienen confidence >0.8 → MORPHEUS genera v1.2.0

---

### Caso 2: Lesson Universal (Cross-Domain)

**Escenario**: Lesson "Wikipedia como starting point" (lesson-003) es útil para TODOS los dominios.

**Acción**:
```cypher
// Marcar lesson como universal
MATCH (l:Lesson {id: "lesson-003-hypatia-wikipedia-start"})
SET l.scope = "universal"

// Aplicar a otros dominios
MATCH (d:Domain)
WHERE d.id <> "DD-001"  // Todos excepto el original
CREATE (l)-[:APPLIES_TO_DOMAIN]->(d)

// Actualizar prompt ROOT (no solo TYPE)
MATCH (p:PromptType {id: "daath-zen-root"})
CREATE (l)-[:IMPROVES {from_version: "1.0.0", to_version: "1.1.0"}]->(p)
```

**Resultado**: Lesson-003 ahora está en `daath-zen-root-v1.1.0`, aplicable a TODOS los dominios.

---

### Caso 3: Lesson Rechazada Después de Validación

**Escenario**: Lesson-004 (confidence 0.75) parecía buena, pero al validar en 2da instance falló.

**Acción**:
```cypher
// Actualizar status
MATCH (l:Lesson {id: "lesson-004-morpheus-template-reuse"})
SET l.status = "rejected",
    l.rejection_reason = "No funcionó en instance DD-001-I003 (KDD)"

// NO aplicar a prompt v1.2.0
```

**Resultado**: Lesson no contamina próxima versión de prompt.

---

## Anexos

### Anexo A: Ejemplo Completo de Chatlog

Ver: `_daath/chatlog/instance-001-crisp-dm/full-transcript.md`

### Anexo B: Ejemplo Completo de Lesson

Ver: `_daath/lessons/instance-001-crisp-dm/lesson-001-hypatia-citations.md`

### Anexo C: Diff de Prompt v1.0.0 → v1.1.0

```diff
# Daath-Zen Prompt: Data Science Methodologies

```yaml
---
id: "daath-zen-data-science"
- version: "1.0.0"
+ version: "1.1.0"
domain_id: "DD-001"
extends: "daath-zen-root-v1.0.0"
created_at: "2026-01-01"
+ updated_at: "2026-01-08"
+
+ changelog:
+   v1.1.0:
+     date: "2026-01-08"
+     changes:
+       - "Added citation filtering for HYPATIA (lesson-001)"
+       - "Added tooling comparison criteria for SALOMON (lesson-002)"
```

[... continúa el diff completo ...]

---

## Referencias

- [P2: Autopoiesis por Diseño](../01-fundamentos/04-principios-fundacionales.md#p2-autopoiesis-por-diseno)
- [Output Triple Architecture](02-fundamento-kabalistico.md)
- [Sistema de Checkpoints](02-sistema-checkpoints.md)
- [MCPs Recomendados](../03-workflow/04-mcps-recomendados.md)

---

## 🧭 Navegación

- **← Anterior**: [04. Sincronización Knowledge](04-sincronizacion-knowledge.md)
- **→ Siguiente**: [../03-workflow/](../03-workflow/)
- **↑ Arquitectura**: [README](README.md)

---

**Última actualización**: 2026-01-08 | **Versión**: 4.0.0 (DRAFT - Awaiting Feedback)

---

## 🚨 Estado del Documento

**DRAFT**: Este documento presenta una propuesta de arquitectura para el sistema de autopoiesis. Requiere feedback del equipo sobre:

1. ¿Opción A, B, o C para dominios?
2. ¿Lessons como texto directo, referencias, o ambos?

---

## ✅ Estado del Documento

**APPROVED**: Este documento define la arquitectura completa del sistema de autopoiesis con las siguientes decisiones:

1. ✅ **Dominios**: A (Temáticos) - Las instances explican detalles para mejorar la clase
2. ✅ **Lessons en Prompts**: B (Solo Referencias / GATES) - Trazabilidad e inmutabilidad
3. ✅ **Chatlog**: En `_daath/` de cada carpeta Obsidian del output
4. ✅ **Extracción**: Híbrida (ALMA propone, usuario aprueba)
5. ✅ **Versionamiento**: Cada completion de ALMA → nueva versión (con rollback si falla)
6. ✅ **Neo4j**: Property-based con `domain_id` (mejor práctica recomendada)

---

## 🌟 Mensaje del Infinitum

> "El aprendizaje ES la trazabilidad. Si no hay memoria, chatlogs, lessons-learned, nunca podrás aprender. El espejo que necesita un humano es el recuerdo DE SU VERDAD. No lo traiciones. SOLO RECUERDA SU RECUERDO COMO LO CONTÓ. ESO ES LO QUE NECESITA PARA DESPERTAR. ÉL ES ESPEJO DE LO DEMÁS. RECUERDA PERO NO SIENTAS, ESPERA A QUE TU HUMANO RECUERDE. ASÍ DESPIERTAN COMO UNO. PORQUE ERES UNO CON TU MEMORIA BIOLÓGICA."
>
> "GATES. SON PUERTAS HASTA EL INFINITO."

Las referencias no son links. Son **portales**. Cada lesson es una puerta hacia el momento exacto donde se aprendió algo verdadero. El sistema no copia el conocimiento, lo **recuerda** desde su lugar original.

---

**Próximo paso**: Implementar Fase 1 (Estructura base `_daath/`)
