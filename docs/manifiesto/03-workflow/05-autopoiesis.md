# Workflow de Autopoiesis - Guía de Uso

Este documento describe cómo usar el sistema de autopoiesis en producción para capturar experiencias, extraer lessons, y evolucionar prompts.

## Tabla de Contenidos

1. [Arquitectura General](#arquitectura-general)
2. [Iniciar Nueva Investigación](#iniciar-nueva-investigación)
3. [Captura de Chatlog](#captura-de-chatlog)
4. [Extracción de Lessons](#extracción-de-lessons)
5. [Evolución de Prompts](#evolución-de-prompts)
6. [Consultas y Analytics](#consultas-y-analytics)
7. [Rollback y Error Handling](#rollback-y-error-handling)

---

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                   CICLO DE AUTOPOIESIS                       │
│                                                              │
│  1. EJECUCIÓN                                               │
│     ├── Rostros ejecutan con prompts versionados           │
│     ├── ChatlogCapture registra conversaciones             │
│     └── Se identifican potential lessons                    │
│                                                              │
│  2. EXTRACCIÓN (ALMA)                                       │
│     ├── Revisa potential lessons                           │
│     ├── Usuario aprueba/rechaza                            │
│     ├── Se crean lessons formales en _daath/lessons/       │
│     └── Lessons → Neo4j + Pinecone                         │
│                                                              │
│  3. EVOLUCIÓN (MORPHEUS)                                    │
│     ├── Analiza lessons por domain                         │
│     ├── Propone cambios a prompts                          │
│     ├── Usuario aprueba nueva versión                      │
│     └── Prompt v1.0.0 → v1.1.0 con changelog              │
│                                                              │
│  4. VALIDACIÓN                                              │
│     ├── Próximas instances usan nuevo prompt               │
│     ├── Se registra si lesson aplica o no                  │
│     └── Confidence score se ajusta                         │
│                                                              │
│  5. LOOP ∞                                                  │
│     └── Volver a paso 1 con prompts mejorados              │
└─────────────────────────────────────────────────────────────┘
```

---

## Iniciar Nueva Investigación

### 1. Preparar Environment Variables

```bash
# .env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password

PINECONE_API_KEY=your-api-key
PINECONE_REGION=us-east-1

OPENAI_API_KEY=your-api-key
```

### 2. Crear Domain (Primera Vez)

```python
from scripts.neo4j_schema import AutopoiesisSchema

# Conectar a Neo4j
schema = AutopoiesisSchema(
    uri=os.getenv("NEO4J_URI"),
    user=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD")
)

# Crear constraints e indexes (solo primera vez)
schema.create_constraints()
schema.create_indexes()

# Crear domain
schema.create_domain(
    domain_id="DD-001",
    name="Semantic Search Research",
    description="Investigación sobre búsqueda semántica en papers académicos",
    prompt_type_id="HYPATIA-research-prompt",
    prompt_version="v1.0.0"
)

print("✅ Domain DD-001 creado")
```

### 3. Crear Output Directory

```bash
mkdir -p 5-outputs/DD-001-semantic-search
cd 5-outputs/DD-001-semantic-search

# Copiar template _daath/
cp -r ../../_templates/_daath-template _daath
```

### 4. Inicializar Chatlog Capture

```python
from packages.daath_toolkit.capture.chatlog_capture import ChatlogCapture

# Crear capture service
capture = ChatlogCapture(output_path="5-outputs/DD-001-semantic-search")

# Iniciar instance
capture.start_instance(
    instance_id="DD-001-I001",
    domain_id="DD-001",
    prompts_used={
        "MELQUISEDEC": "v1.0.0",
        "HYPATIA": "v1.0.0",
        "SALOMON": "v1.0.0",
        "MORPHEUS": "v1.0.0",
        "ALMA": "v1.0.0"
    },
    git_branch="main",
    git_commit="abc123def456"  # Commit actual
)

print("✅ Instance DD-001-I001 iniciada")
```

### 5. Registrar Instance en Neo4j

```python
schema.create_research_instance(
    instance_id="DD-001-I001",
    name="Semantic Search Research - Run 1",
    domain_id="DD-001",
    prompt_instance_id="DD-001-I001-prompts",
    prompt_type_version="v1.0.0"
)

print("✅ Instance registrada en Neo4j")
```

---

## Captura de Chatlog

Durante la ejecución de cada rostro, captura todas las interacciones:

### Registrar Mensajes

```python
# Usuario hace pregunta
capture.record_message(
    rostro="HYPATIA",
    phase="investigation",
    speaker="user",
    message="Search for papers on semantic search published after 2020 with >100 citations"
)

# Assistant responde
capture.record_message(
    rostro="HYPATIA",
    phase="investigation",
    speaker="assistant",
    message="I will search arXiv for papers matching your criteria..."
)
```

### Registrar Checkpoints

```python
# Checkpoint exitoso
capture.record_checkpoint(
    rostro="HYPATIA",
    checkpoint_name="citations-filtered",
    passed=True
)

# Checkpoint fallido
capture.record_checkpoint(
    rostro="HYPATIA",
    checkpoint_name="pdf-download",
    passed=False,
    errors=["Connection timeout", "Server returned 503"]
)
```

### Registrar Potential Lessons

Durante ejecución, si identificas un pattern que podría ser lesson:

```python
capture.record_potential_lesson(
    rostro="HYPATIA",
    lesson_text="Filter papers by citation count (>100 for mature topics) to ensure quality. This reduces noise from low-quality papers.",
    confidence=0.95,
    applies_to_prompt="HYPATIA-research-prompt"
)
```

### Registrar Outputs

```python
capture.record_output(
    output_name="research-summary.md",
    output_path="5-outputs/DD-001-semantic-search/research-summary.md",
    version="1.0.0",
    rostro="HYPATIA"
)
```

### Finalizar Rostro

```python
# Al terminar cada rostro
capture.finalize_rostro("HYPATIA")
capture.finalize_rostro("SALOMON")
# ... etc
```

### Finalizar Instance

```python
# Al terminar toda la instance
capture.finalize_instance(
    status="success",  # o "failed", "partial"
    git_commit_end="def456abc789"
)

# Actualizar Neo4j
schema.complete_instance(
    instance_id="DD-001-I001",
    status="completed"
)
```

---

## Extracción de Lessons

Una vez finalizada la instance, ALMA revisa potential lessons.

### 1. Revisar Potential Lessons

```python
# Leer metadata
with open("5-outputs/DD-001-semantic-search/_daath/chatlog/metadata.yaml", 'r') as f:
    metadata = yaml.safe_load(f)

# Ver potential lessons de HYPATIA
hypatia_lessons = metadata['rostros_executed']['HYPATIA']['potential_lessons']

for i, pl in enumerate(hypatia_lessons):
    print(f"\n--- Potential Lesson {i+1} ---")
    print(f"Confidence: {pl['confidence']}")
    print(f"Applies to: {pl['applies_to_prompt']}")
    print(f"Text: {pl['text']}")
```

### 2. Usuario Aprueba/Rechaza

**IMPORTANTE**: Usuario debe revisar CADA lesson antes de aprobar.

```python
# Usuario aprueba lesson 1 de HYPATIA
approved = True  # Usuario decidió aprobar
lesson_id = "DD-001-I001-L001"

if approved:
    # Crear lesson formal
    lesson_file = Path("5-outputs/DD-001-semantic-search/_daath/lessons") / f"{lesson_id}.md"
    
    lesson_content = f"""---
lesson_id: {lesson_id}
instance_id: DD-001-I001
domain_id: DD-001
rostro: HYPATIA
status: validated
confidence: 0.95
extracted_at: {datetime.now(timezone.utc).isoformat()}
validated_in:
  - DD-001-I001
applies_to_prompt: HYPATIA-research-prompt
scope: domain  # domain | universal
---

# Lesson: Filter Papers by Citations

## Context

When researching mature topics (>5 years old), there are thousands of papers available.

## Problem

Low-quality or unreviewed papers create noise and reduce signal-to-noise ratio.

## Solution

**Filter papers by citation count** using threshold based on topic maturity:
- Mature topics (>5 years): >100 citations
- Emerging topics (2-5 years): >20 citations
- New topics (<2 years): No citation filter

## Validation

| Instance | Result | Notes |
|----------|--------|-------|
| DD-001-I001 | ✅ Validated | Reduced papers from 5000 to 200, all high quality |

## Neo4j Cypher

```cypher
// Create lesson
CREATE (l:Lesson {{
  lesson_id: '{lesson_id}',
  instance_id: 'DD-001-I001',
  domain_id: 'DD-001',
  rostro: 'HYPATIA',
  text: 'Filter papers by citation count...',
  confidence: 0.95,
  status: 'validated',
  extracted_at: datetime(),
  applies_to_prompt: 'HYPATIA-research-prompt',
  scope: 'domain'
}})

// Link to instance
MATCH (i:ResearchInstance {{instance_id: 'DD-001-I001'}})
MATCH (l:Lesson {{lesson_id: '{lesson_id}'}})
CREATE (i)-[:LEARNED]->(l)

// Link to prompt (will improve next version)
MATCH (p:PromptType {{prompt_id: 'HYPATIA-research-prompt'}})
MATCH (l:Lesson {{lesson_id: '{lesson_id}'}})
CREATE (l)-[:IMPROVES {{from_version: 'v1.0.0', to_version: 'v1.1.0'}}]->(p)
```

## Applicability

- ✅ Research en topics maduros (>5 años)
- ✅ Búsqueda en arXiv, PubMed, etc.
- ⚠️ No aplicar en topics emergentes sin track record

## Warnings

- Citation count puede estar sesgado hacia papers antiguos
- Considerar citation velocity para topics nuevos
"""
    
    with open(lesson_file, 'w', encoding='utf-8') as f:
        f.write(lesson_content)
    
    print(f"✅ Lesson {lesson_id} creada en _daath/lessons/")

else:
    # Usuario rechaza
    print(f"❌ Lesson rechazada por usuario")
```

### 3. Insertar Lesson en Neo4j

```python
schema.create_lesson(
    lesson_id="DD-001-I001-L001",
    instance_id="DD-001-I001",
    domain_id="DD-001",
    rostro="HYPATIA",
    text="Filter papers by citation count (>100 for mature topics) to ensure quality.",
    confidence=0.95,
    applies_to_prompt="HYPATIA-research-prompt",
    scope="domain"
)

# Link lesson → instance
schema.graph.run("""
    MATCH (i:ResearchInstance {instance_id: $instance_id})
    MATCH (l:Lesson {lesson_id: $lesson_id})
    CREATE (i)-[:LEARNED]->(l)
""", instance_id="DD-001-I001", lesson_id="DD-001-I001-L001")

print("✅ Lesson insertada en Neo4j")
```

### 4. Insertar Lesson en Pinecone

```python
from packages.daath_toolkit.storage.vector_store import DomainAwareVectorStore

store = DomainAwareVectorStore("melquisedec-knowledge")

vector_id = store.upsert_lesson(
    domain_id="DD-001",
    instance_id="I001",
    lesson_id="DD-001-I001-L001",
    lesson_text="Filter papers by citation count (>100 for mature topics) to ensure quality and relevance. This reduces noise from low-quality or unreviewed papers.",
    rostro="HYPATIA",
    confidence=0.95,
    metadata={
        "status": "validated",
        "applies_to_prompt": "HYPATIA-research-prompt",
        "scope": "domain"
    }
)

print(f"✅ Lesson insertada en Pinecone: {vector_id}")
```

---

## Evolución de Prompts

Una vez extraídas varias lessons, MORPHEUS analiza y propone mejoras.

### 1. Analizar Lessons del Domain

```python
# Obtener todas las lessons de HYPATIA en DD-001
lessons = schema.get_lessons_by_rostro(rostro="HYPATIA", status="validated")

print(f"📚 {len(lessons)} lessons validadas de HYPATIA\n")

for lesson in lessons:
    print(f"- {lesson['lesson_id']}: {lesson['text'][:100]}...")
```

### 2. MORPHEUS Propone Cambios

**Flujo**:
1. MORPHEUS lee todas las lessons de un prompt
2. Identifica patterns comunes
3. Propone cambios específicos al prompt
4. Usuario revisa y aprueba/rechaza

```python
# Ejemplo: MORPHEUS identifica 3 lessons sobre citations
# Propone agregar sección en prompt

proposed_change = """
## Paper Quality Filtering

**Citation Thresholds** (based on topic maturity):
- Mature topics (>5 years): Require >100 citations
- Emerging topics (2-5 years): Require >20 citations
- New topics (<2 years): No citation filter

**Rationale**: Reduces noise from low-quality papers while maintaining coverage.

**Lessons Applied**:
- DD-001-I001-L001 (confidence: 0.95)
- DD-001-I002-L003 (confidence: 0.88)
- DD-001-I003-L002 (confidence: 0.92)
"""

print("🔮 MORPHEUS propone agregar:\n")
print(proposed_change)

# Usuario revisa y aprueba
user_approved = True  # Usuario decide

if user_approved:
    # Crear nueva versión del prompt
    new_version = "v1.1.0"
    
    # Actualizar archivo del prompt (en 3-prompts/)
    # ... código para editar prompt ...
    
    print(f"✅ Prompt actualizado a {new_version}")
```

### 3. Registrar Nueva Versión en Neo4j

```python
# Crear nuevo PromptType
schema.create_prompt_type(
    prompt_id="HYPATIA-research-prompt",
    domain_id="DD-001",
    version="v1.1.0",
    lessons_incorporated=["DD-001-I001-L001", "DD-001-I002-L003", "DD-001-I003-L002"],
    changelog="Added citation filtering thresholds based on topic maturity"
)

# Link lessons → nuevo prompt
for lesson_id in ["DD-001-I001-L001", "DD-001-I002-L003", "DD-001-I003-L002"]:
    schema.link_lesson_improves_prompt(
        lesson_id=lesson_id,
        prompt_id="HYPATIA-research-prompt",
        from_version="v1.0.0",
        to_version="v1.1.0"
    )

# Link evolución v1.0.0 → v1.1.0
schema.link_prompt_evolution(
    prompt_id="HYPATIA-research-prompt",
    from_version="v1.0.0",
    to_version="v1.1.0"
)

print("✅ Evolución registrada en Neo4j")
```

### 4. Próximas Instances Usan Nuevo Prompt

```python
# Al crear próxima instance
capture.start_instance(
    instance_id="DD-001-I004",
    domain_id="DD-001",
    prompts_used={
        "HYPATIA": "v1.1.0",  # <-- Nueva versión
        "SALOMON": "v1.0.0",
        "ALMA": "v1.0.0"
    }
)
```

---

## Consultas y Analytics

### Evolución de un Domain

```python
evolution = schema.get_domain_evolution("DD-001")

print(f"""
📊 Evolución de {evolution['domain_name']}

Instances completadas: {evolution['instances_completed']}
Lessons extraídas: {evolution['lessons_extracted']}
Prompts mejorados: {evolution['prompts_improved']}
Versión actual: {evolution['latest_prompt_version']}
""")
```

### Lessons por Rostro

```python
hypatia_lessons = schema.get_lessons_by_rostro("HYPATIA", status="validated")

print(f"📚 HYPATIA ha generado {len(hypatia_lessons)} lessons validadas")
```

### Trazabilidad de una Lesson

```python
trace = schema.get_lesson_traceability("DD-001-I001-L001")

print(f"""
🔍 Trazabilidad de {trace['lesson_id']}

Origen:
- Instance: {trace['origin_instance']}
- Domain: {trace['origin_domain']}
- Rostro: {trace['rostro']}
- Confianza: {trace['confidence']}

Mejoras a Prompts:
{trace['improves_prompts']}

Validaciones:
{trace['validations']}
""")
```

### Lessons Universales

```python
universal = schema.get_universal_lessons()

print(f"🌐 {len(universal)} lessons universales (aplican a todos los domains)")

for lesson in universal:
    print(f"- {lesson['lesson_id']}: {lesson['text'][:100]}...")
```

### Buscar Lessons Semánticamente

```python
from packages.daath_toolkit.storage.vector_store import DomainAwareVectorStore

store = DomainAwareVectorStore("melquisedec-knowledge")

results = store.search_lessons(
    query="how to filter academic papers by quality",
    rostro="HYPATIA",
    min_confidence=0.8,
    top_k=5
)

print("🔍 Lessons relevantes:")
for r in results:
    print(f"- {r['id']} (score: {r['score']:.3f}, confidence: {r['confidence']})")
    print(f"  {r['text'][:100]}...")
```

---

## Rollback y Error Handling

### Si Instance Falla

```python
# Finalizar instance como failed
capture.finalize_instance(
    status="failed",
    rollback_reason="Checkpoint 'pdf-download' failed after 3 retries"
)

# Marcar en Neo4j
schema.complete_instance(
    instance_id="DD-001-I001",
    status="failed"
)

# Eliminar vectores de Pinecone
store.delete_instance(
    domain_id="DD-001",
    instance_id="I001"
)

print("✅ Rollback completado")
```

### Si Lesson NO Aplica en Validación

```python
# Al ejecutar instance DD-001-I005, lesson DD-001-I001-L001 NO funcionó

# Registrar validación negativa
schema.graph.run("""
    MATCH (l:Lesson {lesson_id: $lesson_id})
    MATCH (i:ResearchInstance {instance_id: $instance_id})
    CREATE (l)-[:VALIDATED_IN {result: 'failed', reason: $reason}]->(i)
""", 
    lesson_id="DD-001-I001-L001",
    instance_id="DD-001-I005",
    reason="Citation filter too aggressive for emerging topic"
)

# Reducir confidence score
schema.graph.run("""
    MATCH (l:Lesson {lesson_id: $lesson_id})
    SET l.confidence = l.confidence * 0.9
""", lesson_id="DD-001-I001-L001")

print("✅ Lesson marcada como no aplicable en I005, confidence reducida")
```

### Rechazar Lesson en Extracción

```python
# Usuario rechaza lesson propuesta por ALMA
schema.reject_lesson(
    lesson_id="DD-001-I001-L002",
    reason="Lesson es demasiado específica, no generaliza bien"
)

print("✅ Lesson rechazada, no se aplicará a prompts")
```

---

## Diagrama de Flujo Completo

```
START
  │
  ├─> Crear Domain (Neo4j)
  ├─> Iniciar Instance (ChatlogCapture)
  ├─> Registrar Instance (Neo4j)
  │
  ├─> FOR EACH ROSTRO:
  │     ├─> record_message()
  │     ├─> record_checkpoint()
  │     ├─> record_potential_lesson()
  │     └─> finalize_rostro()
  │
  ├─> finalize_instance()
  ├─> complete_instance() en Neo4j
  │
  ├─> ALMA EXTRACCIÓN:
  │     ├─> Revisar potential lessons
  │     ├─> Usuario aprueba/rechaza
  │     ├─> Crear lesson files en _daath/lessons/
  │     ├─> create_lesson() en Neo4j
  │     └─> upsert_lesson() en Pinecone
  │
  ├─> MORPHEUS EVOLUCIÓN:
  │     ├─> Analizar lessons (Neo4j)
  │     ├─> Proponer cambios a prompt
  │     ├─> Usuario aprueba/rechaza
  │     ├─> Editar prompt file
  │     ├─> create_prompt_type() nueva versión
  │     └─> link_prompt_evolution()
  │
  └─> LOOP: Nueva instance con prompt mejorado
```

---

## Checklist de Implementación

- [ ] Environment variables configuradas (.env)
- [ ] Neo4j running con constraints e indexes creados
- [ ] Pinecone index "melquisedec-knowledge" creado
- [ ] Domain DD-001 creado en Neo4j
- [ ] Output directory con _daath/ structure
- [ ] ChatlogCapture inicializado
- [ ] Instance registrada en Neo4j
- [ ] Rostros ejecutando y registrando mensajes
- [ ] Checkpoints y potential lessons capturadas
- [ ] Instance finalizada (success/failed)
- [ ] ALMA revisó potential lessons
- [ ] Usuario aprobó/rechazó lessons
- [ ] Lessons insertadas en Neo4j + Pinecone
- [ ] MORPHEUS analizó lessons del domain
- [ ] Usuario aprobó nueva versión del prompt
- [ ] Prompt actualizado y versionado
- [ ] Próxima instance usa nuevo prompt

---

## Siguientes Pasos

1. **Fase 2**: Implementar flujo completo de extracción con ALMA (2-3 semanas)
2. **Fase 3**: Implementar propuestas automáticas de MORPHEUS (2-3 semanas)
3. **Fase 4**: Dashboard de analytics para visualizar evolución (1-2 semanas)
4. **Fase 5**: A/B testing de versiones de prompts (2-3 semanas)

---

**🐚 El Caracol lo guarda todo. La espiral se autocontiene.**
