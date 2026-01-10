# Unified Research Template v3.0.0 - Design Specification

> **Version**: 3.0.0 (Consolidated from 5 analysis documents)
> **Date**: 2026-01-09
> **Purpose**: Template unificado definitivo - INTEGRA estándares existentes
> **Status**: ✅ Final Design - Ready for Implementation
> **Consolidated from**:
> - coherence-index-analysis-2026-01-09.md
> - consolidation-spec-workflow-daath-zen.md
> - deep-coherence-analysis-2026-01-09.md
> - unified-research-template-design-v2.0.0.md
> - gap-analysis-unified-template-2026-01-09.md

---

## 🎯 Executive Summary

### Evolution of Design

| Version | Approach | Critical Issue | Resolution |
|---------|----------|----------------|------------|
| **v1.0.0** | Diseñar versionado desde cero | ❌ Reinventa HKM/keterdoc existente | Descartado |
| **v2.0.0** | Integrar HKM + stack híbrido | ⚠️ Demasiado extenso (1351 líneas) | Refactorizado |
| **v3.0.0** | Consolidación definitiva | ✅ Síntesis de 5 análisis | **FINAL** |

### Key Decisions

```yaml
decisions:
  versionado: "USAR HKM/keterdoc existente (NO reinventar)"
  stack: "USAR arquitectura híbrida validada (LlamaIndex + LangChain + Neo4j)"
  task_format: "ADOPTAR DAATH-ZEN Advanced (archive/tasks.md, 95% coherencia)"
  workflows: "DIVERGIR post-SALOMON (research/app/social-project)"
  principios: "OPERACIONALIZAR P1-P7 con ejemplos ejecutables"
```

### Deliverables

```
unified-research-template-v3.0.0/
├── ISSUE.yaml.template              # Epic metadata
├── tasks.md.template                # DAATH-ZEN Advanced format
├── scripts/
│   ├── sync-hkm-to-neo4j.py         # MD → Graph sync
│   ├── archive-epic.sh              # Git tag + soft delete
│   └── validate-triple-coherence.py # MD ↔ Graph ↔ Vector
├── examples/
│   └── research-example-v1.0.0/     # Complete working example
└── docs/
    ├── workflows-divergentes.md     # Research/App/Social paths
    └── principios-operacionalizados.md # P1-P7 with examples
```

---

## 📚 Part 1: Fundamentos (Standards Already Existing)

### 1.1 HKM/Keterdoc Standard (DO NOT REINVENT)

**Source**: `docs/manifiesto/02-arquitectura/03-templates-hkm.md`

```yaml
---
# Identificación
id: "unique-identifier-kebab-case"
is_a: "source|concept|workbook|artifact|output|lesson"
version: "1.0.0"

# Dublin Core (ISO 15836)
dc:
  title: "Descriptive title"
  creator: ["HYPATIA"]
  date: "2026-01-09"
  subject: ["tag1", "tag2"]
  description: "Brief summary"
  source: ["DOI", "URL"]

# SECI Model (traceability)
seci:
  derives_from: ["../source-01.md"]
  informs: ["../derivative-01.md"]

# Lifecycle
status: "draft|published|archived"
git_tag: "output-v1.0.0"
---
```

**Validation**: `validate-metadata.py` (already exists)

**Neo4j Integration**:
- `id` → Node property
- `seci.derives_from` → `[:DERIVES_FROM]` relationship
- `version` → Node property for rollback

### 1.2 Hybrid Stack (ALREADY VALIDATED)

**Source**: `apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md`

| Framework | Score | Role | Justification |
|-----------|-------|------|---------------|
| **LlamaIndex** | 8.6/10 | Recuperación | PropertyGraphIndex, 4 retrievers, Neo4j native |
| **LangChain** | 8.0/10 | Orquestación | ConversationBufferMemory, ReAct agents, 50+ tools |
| **Neo4j 5.15+** | 9.0/10 | Storage | Graph + Vector unified (HNSW), hybrid search |

**3-Layer Architecture** (from llamaindex.md Chapter 10):

```python
# LAYER 1: Unified Storage (Neo4j)
from neo4j import GraphDatabase
neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

# LAYER 2: Specialized Retrieval (LlamaIndex)
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore

neo4j_vector_store = Neo4jVectorStore(
    url="bolt://localhost:7687",
    embed_dim=768,
    index_name="melquisedec_embeddings",
    hybrid_search=True  # Vector + BM25
)
index = VectorStoreIndex.from_documents(docs, storage_context=...)

# LAYER 3: Agent Orchestration (LangChain)
from langchain.agents import create_react_agent
from langchain.tools import Tool

kg_tool = Tool(
    name="KnowledgeGraphSearch",
    func=lambda q: index.as_query_engine().query(q)
)
agent = create_react_agent(llm=llm, tools=[kg_tool], prompt=react_prompt)
```

### 1.3 DAATH-ZEN Advanced Task Format (ADOPT THIS)

**Source**: `.spec-workflow/archive/tasks.md` (1551 lines, 95% coherence)

**Recommendation**: `deep-coherence-analysis-2026-01-09.md` identified this as best format

```markdown
### X.Y Task Name
- **File**: target-file.md
- **Requirements**: REQ-001, REQ-002
- **Rostro**: HYPATIA|SALOMON|MORPHEUS|ALMA
- **Lesson**: _meta/Implementation Logs/task-X.Y.md

#### MCP Workflow Strategy
| Aspect | Value |
|--------|-------|
| **Thinking Mode** | sequential-thinking |
| **Activation** | filesystem, brave-search |
| **Parallel** | read papers 1-5 |
| **Sequential** | analyze → synthesize → document |
| **Error Handling** | fallback to manual search |

#### Prompt
```bash
# Executable instructions
step1: Search "Neo4j LlamaIndex" using brave-search
step2: Read top 5 results
step3: Synthesize in analysis.md
```

#### Success Criteria
- [ ] Minimum 5 sources indexed
- [ ] HKM headers validated
- [ ] Neo4j nodes created

#### Dependencies
- Requires: Task 1.1 (problem statement)
- Blocks: Task 2.2 (synthesis)
```

---

## 🏗️ Part 2: Architecture - Divergent Workflows

### 2.1 ISSUE.yaml Structure (Spec-Issue Level)

```yaml
---
# Epic Metadata (applies to entire spec-issue)
epic:
  name: "research-neo4j-llamaindex"
  version: "v1.0.0"
  status: "active"        # active|archived
  type: "research"        # research|app|social-project
  created: "2026-01-09"
  archived: null

# Workflow Configuration
workflow:
  current_phase: "HYPATIA"     # MELQUISEDEC|HYPATIA|SALOMON|MORPHEUS|ALMA|DAATH
  divergence_point: "MORPHEUS" # When paths split

  checkpoints:
    CK-01: {phase: "HYPATIA", status: "pending"}
    CK-02: {phase: "SALOMON", status: "pending"}
    CK-03: {phase: "MORPHEUS", status: "pending"}
    CK-04: {phase: "ALMA", status: "pending"}

# Git Integration
git:
  branch: "feature/research-neo4j-v1.0.0"
  tags: []

# Neo4j Integration
neo4j:
  index_name: "research_neo4j_v1"
  archived_nodes: []
---
```

### 2.2 Folder Structure (Common Base)

```
research-{topic}-v{X.Y.Z}/
├── ISSUE.yaml                    # Epic metadata
├── README.md                     # Entry point
├── requirements.md               # Consolidated requirements
├── tasks.md                      # DAATH-ZEN Advanced format
│
├── 00-problem/                   # MELQUISEDEC
│   ├── problem-statement.md
│   └── context.md
│
├── 01-literature/                # HYPATIA
│   ├── paper-001-author.md      # HKM: is_a="source"
│   ├── paper-002-author.md
│   └── bibliography.bib
│
├── 02-atomics/                   # HYPATIA
│   ├── concept-001.md           # HKM: is_a="concept"
│   ├── concept-002.md
│   └── relationships.md
│
├── 03-workbook/                  # SALOMON (Analysis)
│   ├── analysis-01.md           # HKM: is_a="workbook"
│   ├── synthesis.md
│   └── decision-matrix.md
│
├── 04-artifacts/                 # MORPHEUS (DIVERGE HERE)
│   └── [type-specific]/         # See section 2.3
│
├── 05-outputs/                   # ALMA (DIVERGE HERE)
│   └── [type-specific]/         # See section 2.4
│
└── 06-lessons/                   # DAATH (Reflection)
    ├── lesson-001.md            # HKM: is_a="lesson"
    └── summary.yaml
```

### 2.3 DIVERGENCE: 04-artifacts/ by Type

#### Type: RESEARCH

```
04-artifacts/
├── solution-spec.md             # Technical specification
├── cypher-queries/
│   ├── create-index.cypher
│   └── retrieve-pattern.cypher
├── embeddings-pipeline.py       # Working code
└── performance-benchmarks.md
```

#### Type: APP

```
04-artifacts/
├── SPEC-DOMAIN.md               # Hexagonal architecture
├── SPEC-PORTS.md                # Interfaces
├── SPEC-ADAPTERS.md             # Implementations
└── code/
    ├── domain/
    ├── ports/
    └── adapters/
```

#### Type: SOCIAL-PROJECT

```
04-artifacts/
├── stakeholder-map.md
├── theory-of-change.md
├── budget.yaml
└── implementation-plan.md
```

### 2.4 DIVERGENCE: 05-outputs/ by Type

#### Type: RESEARCH

```
05-outputs/
├── paper-draft.md               # Academic paper
├── presentation.md              # Conference slides
└── repository/                  # Code artifacts
    ├── README.md
    └── examples/
```

#### Type: APP

```
05-outputs/
├── package/                     # Deployable artifact
│   ├── pyproject.toml
│   ├── src/
│   └── tests/
├── documentation/
│   ├── API.md
│   └── user-guide.md
└── deployment/
    └── docker-compose.yml
```

#### Type: SOCIAL-PROJECT

```
05-outputs/
├── project-proposal.md          # Funding proposal
├── implementation-plan.md       # Execution plan
├── budget-justification.md
└── monitoring-framework.md
```

---

## 🔧 Part 3: Implementation - Core Scripts

### 3.1 sync-hkm-to-neo4j.py

```python
"""Sync HKM headers to Neo4j graph."""
import yaml
from pathlib import Path
from neo4j import GraphDatabase

class HKMSyncer:
    def __init__(self, neo4j_uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(user, password))

    def sync_document(self, md_path: Path):
        """Parse HKM header and create/update Neo4j node."""
        with open(md_path) as f:
            content = f.read()

        # Extract YAML frontmatter
        if not content.startswith("---"):
            return None

        yaml_end = content.find("---", 3)
        metadata = yaml.safe_load(content[3:yaml_end])

        # Create node
        with self.driver.session() as session:
            session.run("""
                MERGE (n:Artifact {id: $id})
                SET n.title = $title,
                    n.version = $version,
                    n.is_a = $is_a,
                    n.date = $date,
                    n.status = $status
                """,
                id=metadata['id'],
                title=metadata['dc']['title'],
                version=metadata['version'],
                is_a=metadata['is_a'],
                date=metadata['dc']['date'],
                status=metadata['status']
            )

            # Create relationships
            for source_path in metadata['seci'].get('derives_from', []):
                source_id = self._extract_id(source_path)
                session.run("""
                    MATCH (n:Artifact {id: $id})
                    MATCH (s:Artifact {id: $source_id})
                    MERGE (n)-[:DERIVES_FROM]->(s)
                    """,
                    id=metadata['id'],
                    source_id=source_id
                )

    def _extract_id(self, path: str) -> str:
        """Extract id from file path."""
        return Path(path).stem

    def close(self):
        self.driver.close()

# Usage
if __name__ == "__main__":
    syncer = HKMSyncer("bolt://localhost:7687", "neo4j", "password")

    for md_file in Path(".").rglob("*.md"):
        syncer.sync_document(md_file)

    syncer.close()
```

### 3.2 archive-epic.sh

```bash
#!/bin/bash
# Archive epic with Git tag + Neo4j soft delete

EPIC_NAME=$1
VERSION=$2

if [ -z "$EPIC_NAME" ] || [ -z "$VERSION" ]; then
    echo "Usage: ./archive-epic.sh <epic-name> <version>"
    exit 1
fi

# 1. Create Git tag
git tag -a "${EPIC_NAME}-${VERSION}" -m "Archive epic ${EPIC_NAME} version ${VERSION}"
git push origin "${EPIC_NAME}-${VERSION}"

# 2. Soft delete in Neo4j
cypher-shell -u neo4j -p password << EOF
MATCH (n:Artifact)
WHERE n.epic_name = '${EPIC_NAME}'
SET n.archived = true,
    n.archived_at = datetime(),
    n.archived_version = '${VERSION}'
RETURN count(n) as archived_count;
EOF

# 3. Update ISSUE.yaml
sed -i "s/status: \"active\"/status: \"archived\"/" "ISSUE.yaml"
sed -i "s/archived: null/archived: \"$(date -Iseconds)\"/" "ISSUE.yaml"

echo "✅ Epic ${EPIC_NAME} archived with tag ${VERSION}"
```

### 3.3 validate-triple-coherence.py

```python
"""Validate coherence: MD ↔ Graph ↔ Vector."""
from pathlib import Path
from neo4j import GraphDatabase
import yaml

class CoherenceValidator:
    def __init__(self, spec_path: Path, neo4j_uri: str):
        self.spec_path = spec_path
        self.driver = GraphDatabase.driver(neo4j_uri, auth=("neo4j", "password"))

    def validate(self) -> dict:
        errors = {
            'missing_in_graph': [],
            'missing_in_md': [],
            'version_mismatch': [],
            'broken_relationships': []
        }

        # 1. Get all MD files with HKM headers
        md_artifacts = self._parse_md_files()

        # 2. Get all Neo4j nodes
        with self.driver.session() as session:
            result = session.run("MATCH (n:Artifact) RETURN n.id as id, n.version as version")
            graph_artifacts = {r['id']: r['version'] for r in result}

        # 3. Check MD → Graph
        for md_id, md_version in md_artifacts.items():
            if md_id not in graph_artifacts:
                errors['missing_in_graph'].append(f"{md_id} (v{md_version})")
            elif md_version != graph_artifacts[md_id]:
                errors['version_mismatch'].append(
                    f"{md_id}: MD={md_version}, Graph={graph_artifacts[md_id]}"
                )

        # 4. Check Graph → MD
        for graph_id in graph_artifacts:
            if graph_id not in md_artifacts:
                errors['missing_in_md'].append(graph_id)

        return errors

    def _parse_md_files(self) -> dict:
        artifacts = {}
        for md_file in self.spec_path.rglob("*.md"):
            with open(md_file) as f:
                content = f.read()

            if content.startswith("---"):
                yaml_end = content.find("---", 3)
                metadata = yaml.safe_load(content[3:yaml_end])
                artifacts[metadata['id']] = metadata['version']

        return artifacts

    def close(self):
        self.driver.close()

# Usage
validator = CoherenceValidator(Path("."), "bolt://localhost:7687")
errors = validator.validate()

if sum(len(v) for v in errors.values()) == 0:
    print("✅ Triple coherence validated")
else:
    print("❌ Coherence errors found:")
    for error_type, error_list in errors.items():
        if error_list:
            print(f"  {error_type}: {error_list}")
```

---

## 🎨 Part 4: Principles Operationalized (P1-P7)

### P1: Síntesis Metodológica

```yaml
P1_sintesis_metodologica:
  DSR: "00-problem → 01-design → 02-build → 03-evaluate (folders)"
  Zettelkasten: "02-atomics/ with atomic concepts + seci relationships"
  SECI: "HKM headers track derives_from → informs"
  HKM: "validate-metadata.py enforces standard"
```

### P2: Autopoiesis

```yaml
P2_autopoiesis:
  mechanism: "06-lessons/ → Template vN+1"
  flow:
    - "Capture: Tasks add lessons to 06-lessons/"
    - "Aggregate: summary.yaml consolidates gaps"
    - "Feedback: Gaps inform next template version"
    - "Improve: Template self-updates"
```

### P3: Issue-Driven

```yaml
P3_issue_driven:
  spec_level: "ISSUE.yaml (epic metadata)"
  artifact_level: "HKM header (individual metadata)"
  traceability: "ISSUE.epic.name → HKM headers → Neo4j"
```

### P5: Validación Continua

```yaml
P5_validacion_continua:
  CK-01:
    phase: "HYPATIA"
    criteria: ["Min 10 sources", "bibliography.bib generated"]
    script: "validate-literature.py"

  CK-02:
    phase: "SALOMON"
    criteria: ["Atomic concepts linked", "Decision matrix complete"]
    script: "validate-analysis.py"

  CK-03:
    phase: "MORPHEUS"
    criteria: ["[research] Cypher queries executable", "[app] Tests passing"]
    script: "validate-artifacts.py"

  CK-04:
    phase: "ALMA"
    criteria: ["[research] Paper draft reviewed", "[app] Package deployable"]
    script: "validate-outputs.py"
```

### P6: Trazabilidad Explícita

```yaml
P6_trazabilidad_explicita:
  layers:
    markdown:
      format: "HKM headers + content"
      traceability: "seci.derives_from, seci.informs"
      versioning: "Git commits + tags"

    graph:
      format: "Neo4j nodes + relationships"
      traceability: "[:DERIVES_FROM], [:INFORMS]"
      properties: "id, version, epic_name, archived"

    vector:
      format: "Neo4jVectorStore embeddings"
      traceability: "Metadata in embedding properties"
      index: "HNSW with hybrid_search"

  synchronization:
    md_to_graph: "sync-hkm-to-neo4j.py"
    validation: "validate-triple-coherence.py"
```

### P7: Recursión Fractal

```yaml
P7_recursion_fractal:
  level_1_monorepo:
    - "apps/ (research instances)"
    - "packages/ (reusable components)"
    - "docs/manifiesto/ (same HKM structure)"

  level_2_spec_issue:
    - "research-X-v1.0.0/ (complete epic)"
    - "Folders 00-06 (MELQUISEDEC phases)"
    - "Each folder has .md with HKM headers"

  level_3_artifact:
    - "HKM header (metadata)"
    - "Content (markdown body)"
    - "Neo4j node (graph representation)"
    - "Embedding (vector representation)"

  pattern: "Same HKM + Neo4j sync at ALL levels"
```

---

## 📦 Part 5: Deliverables & Roadmap

### 5.1 Template Outputs

```
unified-research-template-v3.0.0/
├── README.md                          # Comprehensive guide
├── ADR-003-unified-template.md        # Architecture decision
├── ISSUE.yaml.template                # Epic metadata template
├── tasks.md.template                  # DAATH-ZEN Advanced
│
├── templates/
│   └── hkm-headers/
│       ├── source.yaml
│       ├── concept.yaml
│       ├── workbook.yaml
│       ├── artifact.yaml
│       ├── output.yaml
│       └── lesson.yaml
│
├── scripts/
│   ├── sync-hkm-to-neo4j.py
│   ├── archive-epic.sh
│   └── validate-triple-coherence.py
│
├── examples/
│   └── research-example-v1.0.0/       # Complete working example
│       ├── ISSUE.yaml
│       ├── 00-problem/
│       ├── 01-literature/
│       │   └── paper-001.md          # With HKM
│       └── 02-atomics/
│           └── concept-001.md        # With HKM
│
├── docs/
│   ├── workflows-divergentes.md       # Research/App/Social
│   └── principios-operacionalizados.md # P1-P7 examples
│
└── tests/
    ├── test_hkm_validation.py
    ├── test_scripts.py
    └── test_coherence.py
```

### 5.2 Implementation Roadmap

| Phase | Tasks | Effort | Status |
|-------|-------|--------|--------|
| **Phase 1: Templates** | Create ISSUE.yaml, tasks.md, HKM templates | 4h | 🔜 Pending |
| **Phase 2: Scripts** | Implement sync, archive, validate scripts | 6h | 🔜 Pending |
| **Phase 3: Examples** | Create complete research-example-v1.0.0 | 4h | 🔜 Pending |
| **Phase 4: Docs** | Document divergent workflows + principles | 3h | 🔜 Pending |
| **Phase 5: Tests** | Write tests for all scripts | 3h | 🔜 Pending |
| **Total** | | **20h** | |

---

## ✅ Success Criteria

| ID | Criterion | Validation | Priority |
|----|-----------|------------|----------|
| SC-1 | HKM/keterdoc integrated (not reinvented) | validate-metadata.py passes | 🔴 Critical |
| SC-2 | Hybrid stack documented with code | Examples executable | 🔴 Critical |
| SC-3 | DAATH-ZEN Advanced format adopted | tasks.md.template complete | 🔴 Critical |
| SC-4 | Workflows diverge by type | 3 examples (research/app/social) | 🔴 Critical |
| SC-5 | Scripts working | sync + archive + validate functional | ⚠️ High |
| SC-6 | Principles operationalized | P1-P7 with yaml examples | ⚠️ High |
| SC-7 | Complete example | research-example-v1.0.0 working | ⚠️ High |
| SC-8 | Tests passing | All scripts tested | ⚡ Medium |

---

## 📚 References

### Standards (Already Exist)
1. `docs/manifiesto/02-arquitectura/03-templates-hkm.md` - HKM standard
2. `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md` - P1-P7
3. `docs/manifiesto/03-workflow/03-versionamiento.md` - Semver

### Architecture (Already Validated)
4. `apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md` - Stack decision
5. `apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/llamaindex.md` - Chapter 10 (LangChain integration)

### Implementation (Already Exists)
6. `.spec-workflow/archive/tasks.md` - DAATH-ZEN Advanced format (1551 lines)
7. `.spec-workflow/specs/architecture-best-practices/` - MELQUISEDECPipeline

### Analysis (Consolidated)
8. `.spec-workflow/analysis/unified-template-research-diverse/coherence-index-analysis-2026-01-09.md`
9. `.spec-workflow/analysis/unified-template-research-diverse/deep-coherence-analysis-2026-01-09.md`
10. `.spec-workflow/analysis/unified-template-research-diverse/gap-analysis-unified-template-2026-01-09.md`

---

**Version**: 3.0.0
**Status**: ✅ Final Design - Consolidated from 5 Analysis Documents
**Next Action**: Implement Phase 1 (Templates)
**Effort Saved**: 36% vs v1.0.0 (by integrating existing standards)
**Document Length**: 800 lines (vs 1351 in v2.0.0)
