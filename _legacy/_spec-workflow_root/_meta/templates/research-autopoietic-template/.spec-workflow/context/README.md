# Context Management - Research Autopoietic Template

Esta carpeta contiene archivos de persistencia de contexto para thinking modes (sequential-thinking, smart-thinking, reasoning-branches).

## ⚠️ CORRECTS GAP #2 from Design v3.0.0

El diseño v3.0.0 mencionaba context management pero no operacionalizaba la estrategia. Esta carpeta **implementa concretamente** cómo se gestiona el contexto durante una épica.

---

## Estructura

```
.spec-workflow/context/
├── README.md                      # Esta guía
├── session-template.json          # Template para sesión smart-thinking
├── thoughts-graph-schema.json     # Schema del thought graph
├── connections-schema.json        # Schema de connections
├── sessions/                      # Sesiones de smart-thinking
│   └── session-[ID].json
├── thoughts/                      # Thought graphs
│   └── thoughts-graph-[DATE].json
├── branches/                      # Reasoning branches
│   ├── main.json
│   └── alt-[NAME].json
└── memories/                      # Relevant memories
    └── memories-[CHECKPOINT].json
```

---

## 1. Smart-Thinking Sessions

### ¿Qué es?

Smart-thinking MCP mantiene sesiones persistentes que capturan:
- Thoughts individuales con ID
- Connections entre thoughts (type, strength, description)
- Métricas (confidence, relevance, quality)
- Context acumulado

### Cuándo Usar

- **HYPATIA (CK-02)**: Síntesis de atomics desde literatura
- **SALOMON (CK-03)**: Análisis comparativo con alternativas
- **DAATH (Post-CK-04)**: Reflexión sobre lessons learned

### Workflow

```bash
# 1. Iniciar sesión (automático al primer llamado a smart-thinking)
# El MCP retorna session_id

# 2. Agregar thoughts iterativamente
{
  "thought": "Concepto X se conecta con Y porque...",
  "connections": [
    {
      "targetId": "previous-thought-id",
      "type": "supports",
      "strength": 0.85
    }
  ]
}

# 3. Persistir sesión al finalizar checkpoint
# Copiar session JSON a sessions/session-[ID].json
```

### Archivo: session-[ID].json

```json
{
  "session_id": "mk7du8d29yen8x0nnk",
  "checkpoint": "CK-02",
  "phase": "HYPATIA",
  "started": "2025-01-15T10:30:00Z",
  "updated": "2025-01-15T14:22:00Z",
  "thoughts": [
    {
      "id": "thought-001",
      "content": "Neo4j vector search es más rápido que flat index en top-k queries",
      "timestamp": "2025-01-15T10:35:00Z",
      "metrics": {
        "confidence": 0.85,
        "relevance": 0.9,
        "quality": 0.8
      }
    }
  ],
  "connections": [
    {
      "source": "thought-001",
      "target": "thought-002",
      "type": "supports",
      "strength": 0.85,
      "description": "Evidencia experimental apoya hipótesis"
    }
  ],
  "metadata": {
    "total_thoughts": 15,
    "total_connections": 22,
    "avg_confidence": 0.78
  }
}
```

---

## 2. Thoughts Graph

### ¿Qué es?

Representación en grafo de todos los thoughts y connections de la sesión.

### Archivo: thoughts-graph-[DATE].json

```json
{
  "nodes": [
    {
      "id": "thought-001",
      "label": "Concepto principal",
      "type": "concept",
      "checkpoint": "CK-02",
      "metrics": {
        "confidence": 0.85,
        "relevance": 0.9,
        "quality": 0.8
      }
    }
  ],
  "edges": [
    {
      "source": "thought-001",
      "target": "thought-002",
      "type": "supports",
      "strength": 0.85
    }
  ],
  "metadata": {
    "created": "2025-01-15T14:22:00Z",
    "checkpoint": "CK-02",
    "total_nodes": 15,
    "total_edges": 22,
    "density": 0.195
  }
}
```

### Visualización

Puede visualizarse con:
- Neo4j Browser (importar como grafo)
- Mermaid diagram (convertir a sintaxis Mermaid)
- D3.js (web visualization)

---

## 3. Connections Schema

### Tipos de Connections

| Type | Descripción | Cuándo Usar |
|------|-------------|-------------|
| **supports** | Pensamiento A apoya/refuerza B | Evidencia que confirma hipótesis |
| **contradicts** | Pensamiento A contradice B | Evidencia contraria o alternativa |
| **refines** | Pensamiento A refina/precisa B | Versión mejorada de concepto |
| **branches** | Pensamiento A ramifica desde B | Exploración alternativa |
| **derives** | Pensamiento A deriva lógicamente de B | Implicación lógica |
| **associates** | Pensamiento A se asocia con B | Relación lateral |
| **exemplifies** | Pensamiento A ejemplifica B | Caso concreto de concepto |
| **generalizes** | Pensamiento A generaliza B | Abstracción de patrón |
| **compares** | Pensamiento A compara con B | Análisis comparativo |
| **contrasts** | Pensamiento A contrasta con B | Diferencias destacadas |
| **questions** | Pensamiento A cuestiona B | Duda o crítica |
| **extends** | Pensamiento A extiende B | Expansión de idea |
| **analyzes** | Pensamiento A analiza B | Descomposición analítica |
| **synthesizes** | Pensamiento A sintetiza B+C+... | Combinación de ideas |
| **applies** | Pensamiento A aplica B | Uso práctico de concepto |
| **evaluates** | Pensamiento A evalúa B | Juicio crítico |

### Archivo: connections-schema.json

```json
{
  "schema_version": "1.0.0",
  "connection_types": [
    {
      "type": "supports",
      "bidirectional": false,
      "strength_range": [0.0, 1.0],
      "required_fields": ["source", "target", "type", "strength"],
      "optional_fields": ["description", "confidence"]
    }
  ],
  "validation": {
    "strength": "Must be between 0.0 and 1.0",
    "target": "Must exist in thoughts graph",
    "description": "Recommended for clarity"
  }
}
```

---

## 4. Reasoning Branches

### ¿Qué son?

Mecanismo para explorar alternativas de diseño en paralelo sin contaminar el razonamiento principal.

### Cuándo Usar

- **SALOMON (CK-03)**: Comparar arquitecturas alternativas
- **MORPHEUS (CK-04)**: Explorar implementaciones diferentes

### NO Usar Cuando

- Necesitas razonamiento secuencial (usa sequential-thinking)
- Alternativas son mutuamente excluyentes desde el inicio

### Workflow

```bash
# 1. Crear branch alternativa
reasoning-branches create alt-hexagonal "Explorar hexagonal architecture"

# 2. Trabajar en branch
reasoning-branches switch alt-hexagonal
# ... agregar thoughts en contexto alternativo ...

# 3. Comparar con main
reasoning-branches compare main alt-hexagonal

# 4. Merge mejor alternativa
reasoning-branches merge alt-hexagonal main --strategy=full
```

### Archivo: branches/main.json

```json
{
  "branch_id": "main",
  "created": "2025-01-15T10:00:00Z",
  "checkpoint": "CK-03",
  "thoughts": [
    "thought-001",
    "thought-002"
  ],
  "status": "active"
}
```

### Archivo: branches/alt-hexagonal.json

```json
{
  "branch_id": "alt-hexagonal",
  "parent": "main",
  "branched_from_thought": "thought-005",
  "created": "2025-01-16T11:30:00Z",
  "checkpoint": "CK-03",
  "description": "Explorar hexagonal architecture como alternativa",
  "thoughts": [
    "alt-thought-001",
    "alt-thought-002"
  ],
  "status": "merged",
  "merged_at": "2025-01-16T15:45:00Z",
  "merge_strategy": "full"
}
```

---

## 5. Relevant Memories

### ¿Qué son?

Subset de thoughts/connections más relevantes para cada checkpoint, filtrados por relevancia y confidence.

### Archivo: memories/memories-CK-02.json

```json
{
  "checkpoint": "CK-02",
  "phase": "HYPATIA",
  "created": "2025-01-15T16:00:00Z",
  "memories": [
    {
      "thought_id": "thought-007",
      "content": "LlamaIndex Neo4jVectorIndex integra graph + vector",
      "relevance": 0.95,
      "confidence": 0.9,
      "connections_count": 8,
      "why_relevant": "Concepto clave para arquitectura híbrida"
    }
  ],
  "metadata": {
    "total_memories": 10,
    "avg_relevance": 0.87,
    "avg_confidence": 0.82,
    "selection_criteria": "relevance >= 0.8 AND confidence >= 0.75 AND connections_count >= 5"
  }
}
```

---

## 6. Usage Guide per Rostro

### MELQUISEDEC (CK-01)

**Thinking Mode**: Sequential
**Context Files**: Ninguno (problema aún no requiere context complejo)

```bash
# Usar sequential-thinking para análisis estructurado del problema
sequential-thinking "Definir problem statement paso a paso..."
```

### HYPATIA (CK-02)

**Thinking Mode**: Smart-Thinking
**Context Files**: `sessions/session-[ID].json`, `thoughts/thoughts-graph-[DATE].json`

```bash
# Iniciar sesión smart-thinking
smart-thinking "Sintetizar concepto de 01-literature/paper-xyz.md"

# Agregar thoughts iterativamente
smart-thinking "Concepto X se conecta con Y porque..."

# Al finalizar CK-02, exportar sesión
# Copiar session JSON a sessions/session-ck-02.json
```

### SALOMON (CK-03)

**Thinking Modes**: Sequential + Reasoning-Branches
**Context Files**: `branches/main.json`, `branches/alt-*.json`

```bash
# Análisis comparativo con sequential
sequential-thinking "Comparar LlamaIndex vs LangChain..."

# Explorar arquitectura alternativa con branches
reasoning-branches create alt-microservices "Explorar microservices vs monolith"
reasoning-branches switch alt-microservices
smart-thinking "En arquitectura microservices, cada servicio..."
reasoning-branches merge alt-microservices main --strategy=summary
```

### MORPHEUS (CK-04)

**Thinking Mode**: Sequential (implementación paso a paso)
**Context Files**: Ninguno (código habla por sí mismo)

### ALMA (CK-04)

**Thinking Mode**: Sequential (generación de outputs)
**Context Files**: Ninguno

### DAATH (Post-CK-04)

**Thinking Mode**: Smart-Thinking
**Context Files**: `memories/memories-CK-XX.json`, `sessions/session-daath.json`

```bash
# Reflexión final con smart-thinking
smart-thinking "Analizando experiencia con CK-02, identifico patrón..."

# Conectar lessons con conceptos de 02-atomics/
smart-thinking "Esta lesson refina concepto SECI Model porque..."

# Exportar memories relevantes
# Filtrar thoughts con relevance >= 0.8
# Guardar en memories/memories-final.json
```

---

## 7. Integration con Neo4j

Los thoughts y connections pueden sincronizarse a Neo4j para:
- Visualización con Neo4j Browser
- Queries Cypher sobre knowledge graph
- Análisis de patrones de razonamiento

### Sync Command

```bash
# Sincronizar thoughts graph a Neo4j
python packages/daath-toolkit/scripts/sync-thoughts-to-neo4j.py \
  --input .spec-workflow/context/thoughts/thoughts-graph-2025-01-15.json \
  --neo4j-uri bolt://localhost:7687 \
  --neo4j-user neo4j \
  --neo4j-password password
```

### Cypher Query Examples

```cypher
// Ver thought con más connections
MATCH (t:Thought)-[c:CONNECTED_TO]->(t2:Thought)
RETURN t.id, t.content, count(c) AS connections
ORDER BY connections DESC
LIMIT 10

// Ver thoughts por checkpoint
MATCH (t:Thought)
WHERE t.checkpoint = 'CK-02'
RETURN t.id, t.content, t.confidence, t.relevance
ORDER BY t.relevance DESC

// Path entre dos thoughts
MATCH path = shortestPath((t1:Thought {id: 'thought-001'})-[*]-(t2:Thought {id: 'thought-020'}))
RETURN path
```

---

## 8. Best Practices

### DO ✅

- **Exportar sesiones al finalizar checkpoints** (preserva contexto)
- **Documentar connections con description** (facilita interpretación)
- **Filtrar memories por relevance ≥0.8** (evita ruido)
- **Usar reasoning-branches solo para alternativas reales** (no overhead innecesario)
- **Validar thoughts-graph con validate-metadata.py** (coherencia HKM)

### DON'T ❌

- **No usar smart-thinking para análisis secuencial simple** (usar sequential-thinking)
- **No crear branches para cada pequeña decisión** (overhead de gestión)
- **No mezclar thoughts de checkpoints diferentes en misma sesión** (contamina contexto)
- **No olvidar strength en connections** (esencial para análisis de grafo)
- **No ignorar métricas confidence/relevance** (indican calidad de razonamiento)

---

## 9. Troubleshooting

### Problema: Session ID no persiste entre llamados

**Solución**: Copiar `session_id` retornado por primer llamado a smart-thinking y almacenar en ISSUE.yaml § workflow.autopoiesis.context_management.session_id

### Problema: Thought graph muy denso (muchas connections débiles)

**Solución**: Filtrar connections con `strength < 0.5` y regenerar graph

### Problema: Reasoning branches divergen demasiado

**Solución**: Hacer merge parcial (strategy=summary) para consolidar insights sin importar todos los thoughts

### Problema: Memories no capturan conceptos clave

**Solución**: Revisar criterios de filtrado (relevance, confidence, connections_count) y ajustar thresholds

---

## 10. References

- [ISSUE.yaml](../ISSUE.yaml) § workflow.autopoiesis.context_management
- [design.md](../design.md) § 6 "Context & Memory Management"
- [tasks.md](../tasks.md) § "Context Management"
- Smart-Thinking MCP Documentation: mcp_ai_smithery_l_smartthinking
- Reasoning Branches MCP: activate_reasoning_branch_management

---

**Ver**: [design.md](../../design.md) § 6 | [ISSUE.yaml](../../ISSUE.yaml) § workflow.autopoiesis
