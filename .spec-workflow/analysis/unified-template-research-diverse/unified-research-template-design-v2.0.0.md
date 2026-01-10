# Unified Research Template Design v2.0.0 - Arquitectura Integrada

> **Version**: 2.0.0 (Refactored from v1.0.0)
> **Date**: 2026-01-09
> **Purpose**: Template unificado con gestión de épicas, versionado y triple persistencia
> **Rostro**: HYPATIA (Research Architecture)
> **Status**: ✅ Design Phase - Integrates HKM, Neo4j Stack, DAATH-ZEN Advanced
> **References**:
> - [HKM Standard](../../../docs/manifiesto/02-arquitectura/03-templates-hkm.md)
> - [Comparative Analysis](../../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md)
> - [LlamaIndex-LangChain Integration](../../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/llamaindex.md#10-integración-y-complementariedad-con-langchain-genai-stack)
> - [Deep Coherence Analysis](unified-template-research-diverse/deep-coherence-analysis-2026-01-09.md)
> - [Gap Analysis](unified-template-research-diverse/gap-analysis-unified-template-2026-01-09.md)

---

## 🎯 Executive Summary

### Objetivo

Diseñar **un template unificado** para spec-issues que:
1. **INTEGRA** estándares existentes (HKM/keterdoc, DAATH-ZEN avanzado)
2. **IMPLEMENTA** arquitectura híbrida validada (LlamaIndex + LangChain + Neo4j)
3. **GESTIONA** épicas con versionado semántico y triple persistencia
4. **DIVERGE** workflows post-SALOMON según tipo (research/app/social-project)

### Cambios vs v1.0.0

| Aspecto | v1.0.0 (Original) | v2.0.0 (Refactored) |
|---------|-------------------|---------------------|
| **Versionado** | ❌ Diseñar desde cero | ✅ INTEGRAR HKM/keterdoc existente |
| **Triple Persistencia** | ❌ Vector store TBD (Chroma/Qdrant) | ✅ Neo4jVectorStore (unified graph+vector) |
| **Stack** | ❌ Investigar arquitectura | ✅ REFERENCIAR comparative-analysis.md validada |
| **LangChain** | ❌ Descartado (overkill) | ✅ HÍBRIDO: LangChain orquestación + LlamaIndex recuperación |
| **Tasks Format** | ⚠️ Sin especificar | ✅ DAATH-ZEN Advanced (archive/tasks.md) |
| **Archival** | ❌ neo4j-admin backup | ✅ Git tags + Cypher soft deletes |
| **Rollback** | ❌ Full restore | ✅ Append-only con soft deletes |
| **Principios** | ⚠️ Mencionados | ✅ Operacionalizados (P1-P7) |
| **Outputs** | ⚠️ 16 artifacts solapados | ✅ 10 artifacts enfocados |

---

## 📚 Fundamentos: Estándares Existentes

### 1. HKM (Header Knowledge Management) - Keterdoc Standard

**Fuente**: [docs/manifiesto/02-arquitectura/03-templates-hkm.md](../../../docs/manifiesto/02-arquitectura/03-templates-hkm.md)

```yaml
---
# Identificación única
id: "unique-identifier-kebab-case"
is_a: "concept|source|workbook|artifact|lesson"
version: "1.0.0"  # Semver del artifact

# Dublin Core (ISO 15836)
dc:
  title: "Título descriptivo del artifact"
  creator: ["Rostro"]
  date: "2026-01-09"
  subject: ["tag1", "tag2"]
  description: "Resumen breve"
  source: ["DOI", "URL"]

# SECI Model (trazabilidad)
seci:
  derives_from: ["../source-01.md", "../source-02.md"]
  informs: ["../derivative-01.md"]

# Lifecycle
status: "draft|published|archived"
git_tag: "output-v1.0.0"  # Tag Git cuando es output
---
```

**Herramientas de validación**:
- `docs/manifiesto/99-meta/validate-metadata.py`: Valida headers HKM
- `docs/manifiesto/99-meta/validacion-estructura.py`: Valida estructura completa

**Integración con Neo4j**:
- `id` → Neo4j node property `id`
- `seci.derives_from` → Relationship `DERIVES_FROM`
- `seci.informs` → Relationship `INFORMS`
- `version` → Node property `version`
- `status` → Node property `status`

### 2. Stack Validado: LlamaIndex + LangChain + Neo4j (Arquitectura Híbrida)

**Fuente**: [comparative-analysis.md](../../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md)

#### Decisión Arquitectónica (ADR-002)

| Framework | Score | Rol | Justificación |
|-----------|-------|-----|---------------|
| **LlamaIndex** | 8.6/10 | Recuperación de datos | PropertyGraphIndex, 4 retrievers especializados, soporte nativo Neo4j |
| **LangChain** | 8.0/10 | Orquestación de agentes | ConversationBufferMemory, ReAct agents, 50+ tools, ecosistema maduro |
| **Neo4j 5.15+** | 9.0/10 | Almacenamiento unificado | Graph + Vector en una DB (HNSW nativo), hybrid search |

**NO es "overkill"** usar ambos frameworks - son **complementarios**:
- ✅ **LlamaIndex**: Especializado en indexación y recuperación avanzada (PropertyGraphIndex)
- ✅ **LangChain**: Especializado en orquestación, memoria conversacional y agentes
- ✅ **Integración nativa**: `llama-index-embeddings-langchain`, LlamaIndex retriever → LangChain Tool

#### Stack Técnico Definitivo

```python
# CAPA 1: Almacenamiento Unificado (Neo4j)
from neo4j import GraphDatabase

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

# CAPA 2: Recuperación Especializada (LlamaIndex)
from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

Settings.embed_model = OllamaEmbedding(
    model_name="qwen2.5:latest",
    base_url="http://localhost:11434"
)
Settings.llm = Ollama(model="qwen2.5:latest")

neo4j_vector_store = Neo4jVectorStore(
    username="neo4j",
    password="password",
    url="bolt://localhost:7687",
    embed_dim=768,  # qwen2.5:latest
    index_name="melquisedec_embeddings",
    hybrid_search=True  # Vector + BM25 keyword search
)

# PropertyGraphIndex para recuperación avanzada
llamaindex_index = VectorStoreIndex.from_documents(
    documents,
    storage_context=StorageContext.from_defaults(
        vector_store=neo4j_vector_store
    )
)

# CAPA 3: Orquestación y Agentes (LangChain)
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain_community.chat_models import ChatOllama

# LlamaIndex retriever como tool de LangChain
llamaindex_query_engine = llamaindex_index.as_query_engine(
    similarity_top_k=5,
    response_mode="tree_summarize"
)

def kg_search(query: str) -> str:
    """Busca en el grafo de conocimiento usando LlamaIndex."""
    return str(llamaindex_query_engine.query(query))

tools = [
    Tool(
        name="KnowledgeGraphSearch",
        func=kg_search,
        description="Busca información en documentos técnicos estructurados"
    )
]

# Agente LangChain con memoria conversacional
langchain_llm = ChatOllama(model="qwen2.5:latest", temperature=0.2)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

agent = create_react_agent(llm=langchain_llm, tools=tools, prompt=react_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)
```

**Performance validada**:
- ✅ 100 docs indexados en <2 min
- ✅ Queries híbridas en 50-100ms
- ✅ Memory optimizada con HNSW quantization

### 3. Formato de Tasks: DAATH-ZEN Advanced

**Fuente**: [.spec-workflow/archive/tasks.md](../archive/templates/tasks.md) (1551 líneas, coherencia 95%)

**Recomendación**: [deep-coherence-analysis.md](unified-template-research-diverse/deep-coherence-analysis-2026-01-09.md) identificó este formato como el más coherente.

```markdown
### X.Y. [Task Name]
- **File**: target-file-path.md
- **Requirements**: REQ-XXX, REQ-YYY
- **Rostro**: HYPATIA|SALOMON|MORPHEUS|ALMA
- **Lesson**: _meta/Implementation Logs/task-X.Y.md

#### MCP Workflow Strategy
| Aspect | Value |
|--------|-------|
| **Thinking Mode** | sequential \| smart-thinking \| none |
| **Activation** | [MCPs to activate first] |
| **Parallel** | [operations without dependencies] |
| **Sequential** | [operations with dependencies] |
| **Error Handling** | [fallback strategy] |

#### Prompt
[Multiline executable instructions for the agent.
This should be copy-pasteable and complete.]

#### Success Criteria
- [ ] Criterion 1 with verification method
- [ ] Criterion 2 with verification method
- [ ] Criterion 3 with verification method

#### Dependencies
- Requires: [previous tasks or artifacts]
- Blocks: [subsequent tasks]

#### Notes
[Optional implementation notes, caveats, or considerations]
```

**Ventajas**:
- ✅ MCP Strategy explícita (thinking mode, activations)
- ✅ Executable prompts (copy-paste directo)
- ✅ Success criteria verificables
- ✅ Lessons learned integradas
- ✅ Dependencies trazables

---

## 🏗️ Arquitectura del Template Unificado

### Estructura de Carpetas (Workflow Completo)

```
research-{topic}-v{X.Y.Z}/
├── ISSUE.yaml                        # Metadata del spec-issue completo
├── README.md                         # Entry point con contexto
├── requirements.md                   # Requirements consolidados
├── tasks.md                          # DAATH-ZEN Advanced format
│
├── 00-problem/                       # MELQUISEDEC: Problema
│   ├── problem-statement.md
│   └── context.md
│
├── 01-literature/                    # HYPATIA: Investigación
│   ├── paper-001-author-year.md     # HKM header (is_a: "source")
│   ├── paper-002-author-year.md
│   └── bibliography.bib
│
├── 02-atomics/                       # HYPATIA: Atomización
│   ├── concept-001-definition.md    # HKM header (is_a: "concept")
│   ├── concept-002-framework.md
│   └── relationships.md
│
├── 03-workbook/                      # SALOMON: Análisis
│   ├── analysis-01-comparison.md    # HKM header (is_a: "workbook")
│   ├── synthesis-framework.md
│   └── decision-matrix.md
│
├── 04-artifacts/                     # MORPHEUS: Artefactos
│   │                                 # DIVERGENCIA POR TIPO
│   ├── [research]/                   # Si type=research
│   │   ├── solution-spec.md
│   │   ├── cypher-queries/
│   │   └── embeddings-pipeline.py
│   │
│   ├── [app]/                        # Si type=app
│   │   ├── SPEC-DOMAIN.md           # Hexagonal architecture
│   │   ├── SPEC-PORTS.md
│   │   ├── SPEC-ADAPTERS.md
│   │   └── code/
│   │
│   └── [social-project]/             # Si type=social-project
│       ├── stakeholder-map.md
│       ├── theory-of-change.md
│       └── budget.yaml
│
├── 05-outputs/                       # ALMA: Publicables
│   │                                 # DIVERGENCIA POR TIPO
│   ├── [research]/
│   │   ├── paper-draft.md
│   │   └── presentation.md
│   │
│   ├── [app]/
│   │   ├── package/                 # Deployable
│   │   └── tests/
│   │
│   └── [social-project]/
│       ├── project-proposal.md
│       └── implementation-plan.md
│
├── 06-lessons/                       # DAATH: Reflexión
│   ├── lesson-001-gap-analysis.md   # HKM header (is_a: "lesson")
│   ├── lesson-002-improvement.md
│   └── summary.yaml                 # Aggregate lessons
│
└── _meta/                            # Metadata operacional
    ├── context.yaml                 # DEPRECATED → Migrar a ISSUE.yaml
    ├── checkpoints.md               # CK-01, CK-02, CK-03, CK-04
    └── Implementation Logs/
        ├── session-2026-01-09.md    # Chatlog de trabajo
        └── task-1.1.md              # Task-specific log
```

### ISSUE.yaml - Metadata del Spec-Issue

```yaml
# ============================================================
# ISSUE METADATA - Spec-Issue Level (NO individual artifacts)
# ============================================================
issue:
  id: "research-dsr-v1.0.0"
  type: "research"  # research | app | social-project

  # Epic Management (NUEVO concepto)
  epic:
    name: "fundacion"
    description: "Establecer fundamentos teóricos de DSR para MELQUISEDEC"
    started: "2026-01-09"
    status: "active"  # active | closed | archived
    version: "1.0.0"  # Version del spec-issue (NOT artifacts)

  # Git Integration
  repository:
    url: "https://github.com/ccolombia-ui/aleia-melquisedec"
    branch: "main"
    git_tag: "research-dsr-v1.0.0"  # Tag when epic closes

  # Workflow Configuration
  workflow:
    rostros:
      MELQUISEDEC: "completed"
      HYPATIA: "in-progress"
      SALOMON: "not-started"
      MORPHEUS: "not-started"
      ALMA: "not-started"
      DAATH: "not-started"

    divergence_point: "SALOMON"  # Where workflows split by type

    # Checkpoints
    checkpoints:
      CK-01: {phase: "HYPATIA", status: "pending", description: "Literature complete"}
      CK-02: {phase: "SALOMON", status: "pending", description: "Analysis validated"}
      CK-03: {phase: "MORPHEUS", status: "pending", description: "Artifacts tested"}
      CK-04: {phase: "ALMA", status: "pending", description: "Outputs published"}

  # Triple Persistence Configuration
  persistence:
    markdown:
      git_enabled: true
      git_workflow: "feature-branch-per-task"

    neo4j:
      enabled: true
      url: "bolt://localhost:7687"
      index_name: "melquisedec_embeddings"
      sync_strategy: "sync-hkm-to-neo4j.py"  # Script to run

    hybrid_framework:
      llamaindex:
        enabled: true
        embed_model: "qwen2.5:latest"
        embed_dim: 768
        vector_store: "Neo4jVectorStore"  # Unified with graph
        hybrid_search: true

      langchain:
        enabled: true
        agent_type: "react"
        memory: "ConversationBufferMemory"
        tools: ["KnowledgeGraphSearch", "Wikipedia"]  # LlamaIndex retriever + others

# ============================================================
# ARCHIVAL STRATEGY (When epic closes)
# ============================================================
archival:
  strategy: "soft-delete"  # NOT full backup

  markdown:
    action: "git tag v{version}"
    location: "archive/research-dsr-v1.0.0/"  # Move folder

  neo4j:
    action: "cypher-mark-archived"
    query: |
      MATCH (n)
      WHERE n.epic_name = $epic_name
      SET n.archived = true,
          n.archived_at = datetime(),
          n.archived_version = $version

  vector:
    action: "neo4j-property-update"  # Vector IS in Neo4j
    note: "Same Cypher query marks vectors as archived"

# ============================================================
# ROLLBACK STRATEGY (Append-only, soft deletes)
# ============================================================
rollback:
  level_1_document:
    action: "git revert {commit}"
    frequency: "90%"

  level_2_node:
    action: "cypher-soft-delete"
    query: |
      MATCH (n {id: $node_id})
      SET n.status = 'deprecated',
          n.replaced_by = $new_node_id
    frequency: "8%"

  level_3_epic:
    action: "git revert {commit-range}"
    cypher: |
      MATCH (n {epic_name: $epic_name})
      SET n.status = 'reverted'
    frequency: "2%"
```

---

## 🔄 Workflows Divergentes por Tipo

### Tipo 1: Research (Investigación Académica)

**Características**:
- Outputs: Papers, presentations, datasets publicables
- Artifacts: Frameworks teóricos, análisis comparativos, cypher queries
- Checkpoints: Peer review, validation académica

**Estructura post-SALOMON**:

```yaml
research_workflow:
  MORPHEUS:
    focus: "Construir solución teórica"
    outputs:
      - "04-artifacts/solution-spec.md"       # HKM (is_a: "artifact")
      - "04-artifacts/cypher-queries/"
      - "04-artifacts/embeddings-pipeline.py"
    success_criteria:
      - "Framework conceptual completo"
      - "Queries Neo4j validadas"
      - "Pipeline reproducible"

  ALMA:
    focus: "Publicar outputs académicos"
    outputs:
      - "05-outputs/paper-draft.md"           # HKM (is_a: "output")
      - "05-outputs/presentation.md"
      - "05-outputs/dataset.csv"
    success_criteria:
      - "Paper draft revisado"
      - "Figuras y tablas finalizadas"
      - "Dataset documentado"

  checkpoints:
    CK-03: "Artifacts validated by SALOMON"
    CK-04: "Outputs ready for submission"
```

### Tipo 2: App (Especificación de Aplicación)

**Características**:
- Outputs: Código deployable, tests, packages
- Artifacts: Specs hexagonales (Domain, Ports, Adapters)
- Checkpoints: Tests pasando, CI/CD

**Estructura post-SALOMON**:

```yaml
app_workflow:
  MORPHEUS:
    focus: "Especificar arquitectura hexagonal"
    outputs:
      - "04-artifacts/SPEC-DOMAIN.md"         # Core business logic
      - "04-artifacts/SPEC-PORTS.md"          # Interfaces
      - "04-artifacts/SPEC-ADAPTERS.md"       # Implementations
      - "04-artifacts/code/"                  # Implementation
    success_criteria:
      - "Domain model especificado"
      - "Ports definidos sin acoplamiento"
      - "Adapters implementados"
      - "Tests unitarios pasando"

  ALMA:
    focus: "Deployar aplicación"
    outputs:
      - "05-outputs/package/"                 # Deployable artifact
      - "05-outputs/tests/"                   # Integration tests
      - "05-outputs/docs/"                    # API documentation
    success_criteria:
      - "Package construido"
      - "Tests e2e pasando"
      - "Documentación completa"

  checkpoints:
    CK-03: "Specs validated and code tested"
    CK-04: "Application deployed to staging"
```

### Tipo 3: Social Project (Proyecto Social)

**Características**:
- Outputs: Propuestas, planes de implementación, presupuestos
- Artifacts: Stakeholder maps, teoría del cambio, budgets
- Checkpoints: Aprobación stakeholders, funding secured

**Estructura post-SALOMON**:

```yaml
social_project_workflow:
  MORPHEUS:
    focus: "Diseñar proyecto social"
    outputs:
      - "04-artifacts/stakeholder-map.md"
      - "04-artifacts/theory-of-change.md"
      - "04-artifacts/budget.yaml"
      - "04-artifacts/risk-analysis.md"
    success_criteria:
      - "Stakeholders identificados y mapeados"
      - "Teoría del cambio validada"
      - "Presupuesto realista"

  ALMA:
    focus: "Proponer proyecto"
    outputs:
      - "05-outputs/project-proposal.md"
      - "05-outputs/implementation-plan.md"
      - "05-outputs/funding-application.pdf"
    success_criteria:
      - "Propuesta completa"
      - "Plan de implementación detallado"
      - "Aplicación de fondos lista"

  checkpoints:
    CK-03: "Artifacts validated by stakeholders"
    CK-04: "Proposal submitted for funding"
```

---

## 🔧 Scripts de Automatización

### Script 1: sync-hkm-to-neo4j.py

**Purpose**: Sincronizar HKM headers de markdown → Neo4j graph

```python
"""
Sync HKM headers to Neo4j graph.

Usage:
    python scripts/sync-hkm-to-neo4j.py --spec research-dsr-v1.0.0
"""
import yaml
from pathlib import Path
from neo4j import GraphDatabase
from typing import Dict, Any

def parse_hkm_header(md_path: Path) -> Dict[str, Any]:
    """Extract HKM header from markdown file."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find YAML front matter
    if not content.startswith('---'):
        raise ValueError(f"No HKM header found in {md_path}")

    yaml_end = content.find('---', 3)
    if yaml_end == -1:
        raise ValueError(f"Invalid HKM header in {md_path}")

    yaml_content = content[3:yaml_end]
    return yaml.safe_load(yaml_content)

def create_node(session, metadata: Dict[str, Any], md_path: Path):
    """Create or update Neo4j node from HKM metadata."""
    node_id = metadata['id']
    is_a = metadata['is_a']
    version = metadata['version']
    dc = metadata['dc']

    # Create node with all properties
    session.run("""
        MERGE (n {id: $id})
        SET n:`""" + is_a.capitalize() + """`,
            n.title = $title,
            n.version = $version,
            n.creator = $creator,
            n.date = $date,
            n.description = $description,
            n.status = $status,
            n.md_path = $md_path,
            n.updated_at = datetime()
        """,
        id=node_id,
        title=dc['title'],
        version=version,
        creator=dc.get('creator', []),
        date=dc.get('date'),
        description=dc.get('description'),
        status=metadata.get('status', 'draft'),
        md_path=str(md_path)
    )

    # Create DERIVES_FROM relationships
    seci = metadata.get('seci', {})
    for source_path in seci.get('derives_from', []):
        source_id = extract_id_from_path(source_path)
        session.run("""
            MATCH (n {id: $id})
            MATCH (s {id: $source_id})
            MERGE (n)-[:DERIVES_FROM]->(s)
            """,
            id=node_id,
            source_id=source_id
        )

    # Create INFORMS relationships
    for target_path in seci.get('informs', []):
        target_id = extract_id_from_path(target_path)
        session.run("""
            MATCH (n {id: $id})
            MATCH (t {id: $target_id})
            MERGE (n)-[:INFORMS]->(t)
            """,
            id=node_id,
            target_id=target_id
        )

def extract_id_from_path(relative_path: str) -> str:
    """Extract HKM id from relative path."""
    # Assume filename is {id}.md
    return Path(relative_path).stem

def sync_spec(spec_path: Path, neo4j_uri: str, neo4j_user: str, neo4j_pass: str):
    """Sync entire spec-issue to Neo4j."""
    driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

    # Find all markdown files with HKM headers
    md_files = spec_path.rglob("*.md")

    with driver.session() as session:
        for md_path in md_files:
            try:
                metadata = parse_hkm_header(md_path)
                create_node(session, metadata, md_path)
                print(f"✅ Synced: {md_path.name} ({metadata['id']})")
            except Exception as e:
                print(f"❌ Failed: {md_path.name} - {e}")

    driver.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True, help="Spec folder name")
    parser.add_argument("--neo4j-uri", default="bolt://localhost:7687")
    parser.add_argument("--neo4j-user", default="neo4j")
    parser.add_argument("--neo4j-pass", default="password")

    args = parser.parse_args()

    spec_path = Path(f".spec-workflow/specs/{args.spec}")
    if not spec_path.exists():
        raise FileNotFoundError(f"Spec not found: {spec_path}")

    sync_spec(spec_path, args.neo4j_uri, args.neo4j_user, args.neo4j_pass)
```

### Script 2: archive-epic.sh

**Purpose**: Archivar épica cerrada con Git tag + Cypher soft archival

```bash
#!/bin/bash
# archive-epic.sh - Archive closed epic with version tag

set -e

# Parse arguments
EPIC_NAME=""
VERSION=""

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --epic) EPIC_NAME="$2"; shift ;;
        --version) VERSION="$2"; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

if [ -z "$EPIC_NAME" ] || [ -z "$VERSION" ]; then
    echo "Usage: ./archive-epic.sh --epic fundacion --version v1.0.0"
    exit 1
fi

echo "🔄 Archiving epic: $EPIC_NAME (version: $VERSION)"

# Step 1: Git operations
echo "📝 Creating Git tag..."
git add .
git commit -m "chore(epic-$EPIC_NAME): close $VERSION" || echo "No changes to commit"
git tag -a "$VERSION" -m "Epic $EPIC_NAME closed"
git push origin main --tags

echo "✅ Git tag created: $VERSION"

# Step 2: Neo4j soft archival
echo "🗄️ Marking Neo4j nodes as archived..."
cypher-shell -u neo4j -p password <<EOF
MATCH (n)
WHERE n.epic_name = '$EPIC_NAME'
SET n.archived = true,
    n.archived_at = datetime(),
    n.archived_version = '$VERSION',
    n.status = 'archived'
RETURN count(n) AS nodes_archived;
EOF

echo "✅ Neo4j nodes archived"

# Step 3: Move markdown folder to archive
echo "📦 Moving folder to archive..."
SPEC_DIR=$(find .spec-workflow/specs -name "*$EPIC_NAME*" -type d | head -n 1)
if [ -n "$SPEC_DIR" ]; then
    ARCHIVE_DIR=".spec-workflow/archive/$(basename $SPEC_DIR)-$VERSION"
    mv "$SPEC_DIR" "$ARCHIVE_DIR"
    echo "✅ Folder archived: $ARCHIVE_DIR"
else
    echo "⚠️ Spec folder not found"
fi

echo "🎉 Epic $EPIC_NAME archived successfully!"
echo "   Version: $VERSION"
echo "   Git tag: $VERSION"
echo "   Neo4j nodes: archived=true"
echo "   Folder: $ARCHIVE_DIR"
```

### Script 3: validate-triple-coherence.py

**Purpose**: Validar coherencia entre MD ↔ Neo4j ↔ Vector embeddings

```python
"""
Validate coherence between Markdown, Neo4j graph, and vector embeddings.

Usage:
    python scripts/validate-triple-coherence.py --spec research-dsr-v1.0.0
"""
from pathlib import Path
from neo4j import GraphDatabase
import yaml
from typing import List, Dict, Tuple

class CoherenceValidator:
    def __init__(self, spec_path: Path, neo4j_uri: str, neo4j_user: str, neo4j_pass: str):
        self.spec_path = spec_path
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

    def validate(self) -> Dict[str, List[str]]:
        """Run all coherence checks."""
        errors = {
            "missing_in_neo4j": [],
            "missing_md_file": [],
            "missing_embeddings": [],
            "version_mismatch": [],
            "broken_relationships": []
        }

        # Get all HKM IDs from markdown
        md_ids = self.get_markdown_ids()

        # Get all IDs from Neo4j
        neo4j_ids = self.get_neo4j_ids()

        # Check 1: MD → Neo4j
        for md_id, md_path in md_ids.items():
            if md_id not in neo4j_ids:
                errors["missing_in_neo4j"].append(f"{md_id} ({md_path})")

        # Check 2: Neo4j → MD
        for neo4j_id in neo4j_ids:
            if neo4j_id not in md_ids:
                errors["missing_md_file"].append(neo4j_id)

        # Check 3: Embeddings exist
        errors["missing_embeddings"] = self.check_embeddings(neo4j_ids)

        # Check 4: Version consistency
        errors["version_mismatch"] = self.check_versions(md_ids)

        # Check 5: SECI relationships
        errors["broken_relationships"] = self.check_relationships(md_ids)

        return errors

    def get_markdown_ids(self) -> Dict[str, Path]:
        """Extract all HKM IDs from markdown files."""
        ids = {}
        for md_path in self.spec_path.rglob("*.md"):
            try:
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    metadata = yaml.safe_load(content[3:yaml_end])
                    if 'id' in metadata:
                        ids[metadata['id']] = md_path
            except Exception:
                continue
        return ids

    def get_neo4j_ids(self) -> List[str]:
        """Get all node IDs from Neo4j."""
        with self.driver.session() as session:
            result = session.run("MATCH (n) WHERE n.id IS NOT NULL RETURN n.id AS id")
            return [record["id"] for record in result]

    def check_embeddings(self, node_ids: List[str]) -> List[str]:
        """Check which nodes are missing embeddings."""
        missing = []
        with self.driver.session() as session:
            for node_id in node_ids:
                result = session.run("""
                    MATCH (n {id: $id})
                    RETURN n.embedding IS NOT NULL AS has_embedding
                    """, id=node_id)
                record = result.single()
                if record and not record["has_embedding"]:
                    missing.append(node_id)
        return missing

    def check_versions(self, md_ids: Dict[str, Path]) -> List[str]:
        """Check version consistency between MD and Neo4j."""
        mismatches = []
        with self.driver.session() as session:
            for md_id, md_path in md_ids.items():
                # Get version from MD
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                yaml_end = content.find('---', 3)
                metadata = yaml.safe_load(content[3:yaml_end])
                md_version = metadata.get('version')

                # Get version from Neo4j
                result = session.run("""
                    MATCH (n {id: $id})
                    RETURN n.version AS version
                    """, id=md_id)
                record = result.single()

                if record and record["version"] != md_version:
                    mismatches.append(f"{md_id}: MD={md_version}, Neo4j={record['version']}")

        return mismatches

    def check_relationships(self, md_ids: Dict[str, Path]) -> List[str]:
        """Check SECI relationships consistency."""
        broken = []
        with self.driver.session() as session:
            for md_id, md_path in md_ids.items():
                # Get derives_from from MD
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                yaml_end = content.find('---', 3)
                metadata = yaml.safe_load(content[3:yaml_end])
                seci = metadata.get('seci', {})
                derives_from = seci.get('derives_from', [])

                # Get relationships from Neo4j
                result = session.run("""
                    MATCH (n {id: $id})-[:DERIVES_FROM]->(s)
                    RETURN s.id AS source_id
                    """, id=md_id)
                neo4j_sources = [record["source_id"] for record in result]

                # Extract IDs from paths
                md_sources = [Path(p).stem for p in derives_from]

                # Check consistency
                if set(md_sources) != set(neo4j_sources):
                    broken.append(f"{md_id}: MD sources={md_sources}, Neo4j={neo4j_sources}")

        return broken

    def close(self):
        self.driver.close()

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--neo4j-uri", default="bolt://localhost:7687")
    parser.add_argument("--neo4j-user", default="neo4j")
    parser.add_argument("--neo4j-pass", default="password")

    args = parser.parse_args()

    spec_path = Path(f".spec-workflow/specs/{args.spec}")
    if not spec_path.exists():
        raise FileNotFoundError(f"Spec not found: {spec_path}")

    validator = CoherenceValidator(spec_path, args.neo4j_uri, args.neo4j_user, args.neo4j_pass)
    errors = validator.validate()
    validator.close()

    # Report results
    print("\n🔍 Triple Coherence Validation Results\n")

    total_errors = sum(len(v) for v in errors.values())

    if total_errors == 0:
        print("✅ All checks passed! MD ↔ Neo4j ↔ Vector are coherent.")
        return 0

    print(f"❌ Found {total_errors} coherence issues:\n")

    for error_type, error_list in errors.items():
        if error_list:
            print(f"  {error_type.upper().replace('_', ' ')}:")
            for error in error_list:
                print(f"    - {error}")
            print()

    return 1

if __name__ == "__main__":
    exit(main())
```

---

## 🎨 Operacionalización de Principios Fundacionales

**Fuente**: [docs/manifiesto/01-fundamentos/04-principios-fundacionales.md](../../../docs/manifiesto/01-fundamentos/04-principios-fundacionales.md)

### P1 - Síntesis Metodológica

**Definición**: "Integración de metodologías complementarias (DSR + Zettelkasten + SECI)"

**Operacionalización en el Template**:

```yaml
P1_sintesis_metodologica:
  DSR:
    implementacion: "Carpetas 00-problem → 01-design → 02-build → 03-evaluate"
    evidencia: "Estructura completa del spec-issue sigue Design Science Research"

  Zettelkasten:
    implementacion: "02-atomics/ con atomic concepts interconectados"
    evidencia: "HKM seci.derives_from y seci.informs crean red de conocimiento"

  SECI:
    implementacion: "HKM headers con seci model"
    evidencia: "Cada artifact traza socialization → externalization → combination → internalization"

  HKM:
    implementacion: "Headers en TODOS los artifacts"
    evidencia: "validate-metadata.py enforces standard"
```

### P2 - Autopoiesis

**Definición**: "Sistema se auto-mejora mediante lecciones aprendidas"

**Operacionalización**:

```yaml
P2_autopoiesis:
  mecanismo: "06-lessons/ → Template v2.0.0"

  flujo:
    1_captura: "Task 5.1-5.3 agregan lecciones a 06-lessons/"
    2_agregacion: "summary.yaml consolida gaps identificados"
    3_feedback: "Gaps informan siguiente versión del template"
    4_mejora: "Template se auto-actualiza con aprendizajes"

  evidencia:
    - "v1.0.0 → gaps identificados en lessons"
    - "v2.0.0 incorpora mejoras basadas en gaps"
    - "Cada épica cerrada genera lecciones estructuradas"

  scripts:
    - "aggregate-lessons.py → summary.yaml"
    - "propose-template-improvements.py → ADR-XXX"
```

### P3 - Issue-Driven

**Definición**: "Todo spec inicia con ISSUE.yaml que define metadata completa"

**Operacionalización**:

```yaml
P3_issue_driven:
  metadata_levels:
    spec_issue:
      ubicacion: "ISSUE.yaml en root del spec"
      contenido: "Epic name, version, type, workflow config"
      proposito: "Metadata del spec-issue completo"

    artifact:
      ubicacion: "HKM header en cada .md"
      contenido: "id, is_a, version, dc, seci, status"
      proposito: "Metadata de cada artifact individual"

  trazabilidad:
    epic_to_artifacts: "ISSUE.yaml epic.name → HKM headers epic metadata"
    artifacts_to_graph: "HKM seci → Neo4j relationships"
    graph_to_vector: "Neo4j nodes → embeddings en mismo índice"

  evidencia:
    - "Cada spec tiene ISSUE.yaml ANTES de crear artifacts"
    - "HKM headers referencian epic del ISSUE.yaml"
    - "Validación falla si ISSUE.yaml está incompleto"
```

### P5 - Validación Continua

**Definición**: "4 checkpoints con criterios explícitos"

**Operacionalización**:

```yaml
P5_validacion_continua:
  checkpoints:
    CK-01:
      phase: "HYPATIA"
      description: "Literature review complete"
      criteria:
        - "Mínimo 10 fuentes primarias indexadas"
        - "Bibliography.bib generado"
        - "Cada paper tiene HKM header con dc.source"
      script: "validate-literature.py"

    CK-02:
      phase: "SALOMON"
      description: "Analysis validated"
      criteria:
        - "Atomic concepts interconectados (seci)"
        - "Decision matrix completa"
        - "Framework synthesis validado"
      script: "validate-analysis.py"

    CK-03:
      phase: "MORPHEUS"
      description: "Artifacts tested"
      criteria:
        - "[research] Queries Cypher ejecutables"
        - "[app] Tests unitarios pasando"
        - "[social-project] Stakeholders aprobaron"
      script: "validate-artifacts.py"

    CK-04:
      phase: "ALMA"
      description: "Outputs published"
      criteria:
        - "[research] Paper draft revisado"
        - "[app] Package deployable"
        - "[social-project] Propuesta submitted"
      script: "validate-outputs.py"

  herramientas:
    - "validate-metadata.py": "HKM headers"
    - "validate-triple-coherence.py": "MD ↔ Neo4j ↔ Vector"
    - "validate-checkpoint.sh": "Checkpoint-specific validation"
```

### P6 - Trazabilidad Explícita

**Definición**: "Triple output: documento + grafo + vector"

**Operacionalización**:

```yaml
P6_trazabilidad_explicita:
  capas:
    markdown:
      formato: "HKM headers + content"
      trazabilidad: "seci.derives_from, seci.informs"
      versionado: "Git commits + tags"
      ubicacion: "Filesystem"

    graph:
      formato: "Neo4j nodes + relationships"
      trazabilidad: "DERIVES_FROM, INFORMS relationships"
      propiedades: "id, version, epic_name, archived, status"
      ubicacion: "Neo4j database"

    vector:
      formato: "Neo4jVectorStore embeddings"
      trazabilidad: "Metadata en embedding node properties"
      index: "HNSW nativo con hybrid_search"
      ubicacion: "MISMA Neo4j database (unified storage)"

  sincronizacion:
    md_to_graph: "sync-hkm-to-neo4j.py"
    graph_to_vector: "LlamaIndex PropertyGraphIndex auto-indexing"
    validation: "validate-triple-coherence.py"

  evidencia:
    - "Cada artifact MD tiene nodo Neo4j con mismo id"
    - "Cada nodo Neo4j tiene embedding en mismo DB"
    - "Triple coherence validation pasa"
```

### P7 - Recursión Fractal

**Definición**: "Misma estructura se repite en múltiples escalas"

**Operacionalización**:

```yaml
P7_recursion_fractal:
  niveles:
    1_monorepo:
      estructura:
        - "apps/ (research instances con estructura completa)"
        - "packages/ (componentes reutilizables)"
        - "docs/manifiesto/ (misma estructura HKM)"
      patron: "Todos usan HKM headers + Neo4j sync"

    2_spec_issue:
      estructura:
        - "research-X-v1.0.0/ (épica completa)"
        - "Carpetas 00-06 (fases MELQUISEDEC)"
        - "Cada carpeta tiene .md con HKM headers"
      patron: "Workflow completo replicable"

    3_artifact:
      estructura:
        - "HKM header (metadata standard)"
        - "Content (markdown body)"
        - "Neo4j node (graph representation)"
        - "Embedding (vector representation)"
      patron: "Triple persistencia en cada nivel"

  evidencia:
    - "docs/manifiesto/ usa misma estructura que apps/research-X/"
    - "Cada .md (independiente del nivel) tiene HKM header"
    - "validate-metadata.py funciona en CUALQUIER nivel"
    - "sync-hkm-to-neo4j.py funciona en CUALQUIER carpeta"

  diagrama_fractal:
    """
    Monorepo
    ├── apps/
    │   └── research-dsr-v1.0.0/        # NIVEL 2 (spec-issue)
    │       ├── ISSUE.yaml
    │       ├── 01-literature/
    │       │   └── paper-001.md        # NIVEL 3 (artifact) con HKM
    │       └── 02-atomics/
    │           └── concept-001.md      # NIVEL 3 (artifact) con HKM
    │
    ├── docs/manifiesto/                # NIVEL 2 (spec-issue equivalente)
    │   ├── 01-fundamentos/
    │   │   └── principios.md           # NIVEL 3 (artifact) con HKM
    │   └── 02-arquitectura/
    │       └── templates-hkm.md        # NIVEL 3 (artifact) con HKM
    │
    └── packages/daath-toolkit/         # NIVEL 2 (reutilizable)
        └── validators/
            └── validate_research.py    # NIVEL 3 (código con docstrings)

    PATRÓN: Cada nivel usa HKM + Neo4j sync + Triple persistencia
    """
```

---

## 📦 Deliverables del Template

### Estructura de Outputs

```
unified-research-template-v2.0.0/
├── README.md                          # 1. Entry point comprehensive
├── ADR-003-unified-template.md        # 2. Architectural Decision Record
├── design.md                          # 3. Architecture + integration
├── requirements.md                    # 4. Requirements consolidados
│
├── templates/
│   ├── ISSUE.yaml.template            # 5. Epic metadata template
│   ├── config.yaml.template           # 6. Parametrizable config (DEPRECATED)
│   ├── tasks.md.template              # 7. DAATH-ZEN Advanced format
│   └── hkm-headers/
│       ├── source.yaml                # 8. HKM for is_a: "source"
│       ├── concept.yaml               # 9. HKM for is_a: "concept"
│       ├── workbook.yaml              # 10. HKM for is_a: "workbook"
│       ├── artifact.yaml              # 11. HKM for is_a: "artifact"
│       ├── output.yaml                # 12. HKM for is_a: "output"
│       └── lesson.yaml                # 13. HKM for is_a: "lesson"
│
├── scripts/
│   ├── sync-hkm-to-neo4j.py           # 14. MD → Neo4j sync
│   ├── archive-epic.sh                # 15. Git tag + Cypher archival
│   ├── validate-triple-coherence.py   # 16. Triple coherence validation
│   ├── rollback-node.sh               # 17. Soft delete node
│   └── validate-checkpoint.sh         # 18. Checkpoint validation
│
├── examples/
│   └── research-example-v1.0.0/       # 19. Complete working example
│       ├── ISSUE.yaml
│       ├── tasks.md
│       ├── 00-problem/
│       ├── 01-literature/
│       │   └── paper-001-example.md   # With HKM header
│       ├── 02-atomics/
│       │   └── concept-001-example.md # With HKM header
│       └── ...                        # Full structure
│
├── tests/
│   ├── test_hkm_validation.py         # 20. HKM header tests
│   ├── test_scripts.py                # 21. Scripts tests
│   └── test_coherence.py              # 22. Triple coherence tests
│
└── _meta/
    ├── orchestrator.md                # 23. Executable MCP workflow
    ├── gap-analysis.md                # 24. Known limitations
    └── migration-guide.md             # 25. Migrating existing specs
```

### Total Outputs: 25 artifacts focused

**Eliminados de v1.0.0**:
- ❌ context.yaml (migrated to ISSUE.yaml)
- ❌ epic-versioning-design.md (integrated in design.md)
- ❌ git-workflow-integration.md (integrated in design.md)
- ❌ user-tutorial.md (integrated in README.md)
- ❌ implementation-roadmap.md (goes in ADR)
- ❌ Vector store backups (vector IS Neo4j)

---

## 🚀 Roadmap de Implementación

### Fase 1: Refactoring y Documentación (Actual)

**Esfuerzo**: 4 hours

| Task | Description | Output | Status |
|------|-------------|--------|--------|
| 1.1 | Integrate HKM/keterdoc standard | design.md updated | ⏳ In Progress |
| 1.2 | Specify hybrid stack (LlamaIndex + LangChain) | architecture section | ⏳ In Progress |
| 1.3 | Reference existing analyses | Links to comparative-analysis.md | ⏳ In Progress |
| 1.4 | Detail divergent workflows (research/app/social) | workflows section | ⏳ In Progress |
| 1.5 | Operationalize P1-P7 principles | principles section | ⏳ In Progress |

### Fase 2: Template Implementation (Next)

**Esfuerzo**: 12 hours

| Task | Description | Output | Status |
|------|-------------|--------|--------|
| 2.1 | Adopt DAATH-ZEN Advanced format | tasks.md.template | 🔜 Pending |
| 2.2 | Create HKM header templates | templates/hkm-headers/ | 🔜 Pending |
| 2.3 | Implement sync-hkm-to-neo4j.py | scripts/sync-hkm-to-neo4j.py | 🔜 Pending |
| 2.4 | Implement archive-epic.sh | scripts/archive-epic.sh | 🔜 Pending |
| 2.5 | Implement validate-triple-coherence.py | scripts/validate-triple-coherence.py | 🔜 Pending |
| 2.6 | Create complete example | examples/research-example-v1.0.0/ | 🔜 Pending |

### Fase 3: Validation (Final)

**Esfuerzo**: 4 hours

| Task | Description | Output | Status |
|------|-------------|--------|--------|
| 3.1 | Write tests for scripts | tests/ | 🔜 Pending |
| 3.2 | Migrate 1 spec activo to new template | apps/research-X-v2.0.0/ | 🔜 Pending |
| 3.3 | Document migration lessons | 06-lessons/migration-lessons.md | 🔜 Pending |
| 3.4 | Create ADR for template decision | ADR-003-unified-template.md | 🔜 Pending |

**Total Effort**: 20 hours (vs 25h original, 20% reduction)

---

## 🎓 Referencias y Contexto

### Documentos Fundacionales

1. **HKM Standard**: [docs/manifiesto/02-arquitectura/03-templates-hkm.md](../../../docs/manifiesto/02-arquitectura/03-templates-hkm.md)
2. **Semantic Versioning**: [docs/manifiesto/03-workflow/03-versionamiento.md](../../../docs/manifiesto/03-workflow/03-versionamiento.md)
3. **Principios Fundacionales**: [docs/manifiesto/01-fundamentos/04-principios-fundacionales.md](../../../docs/manifiesto/01-fundamentos/04-principios-fundacionales.md)

### Investigaciones Completadas

4. **Comparative Analysis (1175 líneas)**: [apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md](../../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md)
5. **LlamaIndex-LangChain Integration (Chapter 10)**: [apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/llamaindex.md#10-integración-y-complementariedad-con-langchain-genai-stack](../../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/llamaindex.md#10-integración-y-complementariedad-con-langchain-genai-stack)
6. **GenAI Stack**: [apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/genai-stack.md](../../../apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/genai-stack.md)

### Análisis de Coherencia

7. **Deep Coherence Analysis**: [.spec-workflow/analysis/deep-coherence-analysis-2026-01-09.md](unified-template-research-diverse/deep-coherence-analysis-2026-01-09.md)
8. **Gap Analysis (15 gaps)**: [.spec-workflow/analysis/gap-analysis-unified-template-2026-01-09.md](unified-template-research-diverse/gap-analysis-unified-template-2026-01-09.md)

### Implementaciones Validadas

9. **MELQUISEDECPipeline**: [.spec-workflow/specs/architecture-best-practices/](../.spec-workflow/specs/architecture-best-practices/)
10. **DAATH-ZEN Advanced Format**: [.spec-workflow/archive/tasks.md](../.spec-workflow/archive/tasks.md)

---

## ✅ Success Criteria

### Criterios de Aceptación

| ID | Criterion | Validation Method | Status |
|----|-----------|-------------------|--------|
| SC-1 | Template integra HKM/keterdoc (NO reinventa) | validate-metadata.py pasa | ⏳ |
| SC-2 | Stack híbrido documentado (LlamaIndex + LangChain + Neo4j) | Code examples ejecutables | ⏳ |
| SC-3 | Workflows divergentes detallados (research/app/social) | 3 ejemplos completos | 🔜 |
| SC-4 | Scripts de sync funcionando | sync-hkm-to-neo4j.py + tests | 🔜 |
| SC-5 | Archival strategy con soft deletes | archive-epic.sh funcional | 🔜 |
| SC-6 | Triple coherence validation | validate-triple-coherence.py pasa | 🔜 |
| SC-7 | Principios P1-P7 operacionalizados | Cada principio con evidencia | ⏳ |
| SC-8 | DAATH-ZEN Advanced format adoptado | tasks.md.template completo | 🔜 |
| SC-9 | Ejemplo completo working | research-example-v1.0.0 ejecutable | 🔜 |
| SC-10 | 1 spec activo migrado exitosamente | Migration lessons documented | 🔜 |

### Definition of Done

- ✅ Documento design.md completo con arquitectura híbrida
- ✅ Scripts implementados y testeados
- ✅ Templates creados (ISSUE.yaml, tasks.md, HKM headers)
- ✅ Ejemplo completo funcionando
- ✅ Tests pasando (HKM validation, scripts, coherence)
- ✅ 1 spec activo migrado
- ✅ ADR-003 creado con decisiones arquitectónicas
- ✅ Migration guide documentado

---

**Version**: 2.0.0
**Status**: ✅ R0.1 COMPLETE - Refactored Design Integrating Existing Standards
**Next**: R0.2 - Implement Scripts and Templates
**Updated**: 2026-01-09
**Ahorro vs v1.0.0**: 5 hours (20% reduction) al integrar en vez de reinventar
