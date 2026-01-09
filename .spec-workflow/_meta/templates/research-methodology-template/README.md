# Spec-Issue Template: Research Methodology

> **Template ID**: `research-methodology-template`
> **Version**: `1.1.0`
> **Created**: `2025-01-20`
> **Updated**: `2026-01-09`
> **Owner**: MELQUISEDEC
> **Purpose**: Generic, configurable spec-issue for formal research methodology investigations

---

## 🎯 Propósito

Esta plantilla implementa un **spec-issue configurable** para realizar investigaciones formales de **revisión de contenido científico/académico**, aplicando los principios MELQUISEDEC:

- ✅ **P1 - Síntesis Metodológica**: Combina DSR + Zettelkasten + Triple Output (no inventamos, adaptamos)
- ✅ **P2 - Autopoiesis**: Lessons learned automáticos → v2.0.0 del template
- ✅ **P3 - Issue-Driven**: Todo inicia con ISSUE.yaml (HKM + Dublin Core metadata)
- ✅ **P5 - Validación Continua**: 4 checkpoints con criterios explícitos
- ✅ **P6 - Trazabilidad Explícita**: Triple output (MD + Neo4j Graph + Vectors)
- ✅ **P7 - Recursión Fractal**: La estructura se repite a diferentes escalas

**¿Qué problema resuelve?**

- Unifica DSR (Design Science Research) con gestión formal de contenidos atómicos
- Automatiza la extracción de conocimiento trazable desde literatura académica
- Genera artefactos ejecutables (scripts, Cypher queries, embeddings)
- Crea grafo semántico en Neo4j con vectores para búsqueda semántica

---

## 🏗️ Arquitectura Híbrida

```
DSR Structure (phases)     +  Document Management (atoms)  →  Triple Output
├─ 00-problem              ├─ 01-literature                ├─ Markdown (filesystem)
├─ 01-design               ├─ 02-atomics                   ├─ Graph (Neo4j)
├─ 02-build                ├─ 03-workbook                  └─ Vectors (embeddings)
├─ 03-evaluate             ├─ 04-artifacts
└─ 04-lessons              ├─ 05-evaluate
                           └─ 06-lessons
```

---

## 📂 Contenido del Template

```
research-methodology-template/
├── README.md                    ← This file (entry point + diagrams)
├── config.yaml                  ← Single source of truth (parametrización)
├── requirements.md              ← WHAT + WHY (requirements phase)
├── design.md                    ← HOW (architecture design + MCP patterns)
├── tasks.md                     ← Detailed task breakdown (27 tasks) + MCP Workflows
└── _meta/                       ← Metadatos y assets de infraestructura
    ├── orchestrator.md          ← Executable workflow automation
    ├── templates/               ← Base file templates
    │   ├── ISSUE.yaml.template
    │   ├── atomic-concept.md.template
    │   ├── relationships.yaml.template
    │   └── checkpoint-validation.yaml.template
    ├── Implementation Logs/     ← Per-task execution logs
    └── lessons-learned/         ← Lessons documentation
```

---

## 📊 Diagramas de Arquitectura

### Workflow Completo: 5 Rostros DAATH-ZEN

```mermaid
sequenceDiagram
    autonumber
    participant U as Usuario
    participant M as MELQUISEDEC<br/>(Orquestador)
    participant H as HYPATIA<br/>(Investigadora)
    participant S as SALOMON<br/>(Arquitecto)
    participant MO as MORPHEUS<br/>(Implementador)
    participant A as ALMA<br/>(Ejecutora)
    participant CK as Checkpoints

    U->>M: Instanciar research (config.yaml)

    rect rgb(240, 248, 255)
        Note over M: Phase 0: Inicialización
        M->>M: Task 0.1: Crear estructura
        M->>M: Generar ISSUE.yaml + folders
    end

    M->>H: Handoff: Literature Review

    rect rgb(255, 248, 240)
        Note over H: Phase 1: Research
        H->>H: Task 1.1: Buscar fuentes (PARALLEL)
        H->>H: Task 1.2: Documentar contenido
        H->>H: Task 1.3: Atomizar (Zettelkasten)
        H->>H: Task 1.4: Mapear relaciones
        H->>H: Task 1.5: Graph-ready YAML
        H->>CK: Task 1.6: Checkpoint CK-01
    end

    alt CK-01 PASS + Approved
        CK-->>S: Proceed to SALOMON
    else CK-01 FAIL
        CK-->>H: Retry: Fix issues
    end

    rect rgb(240, 255, 240)
        Note over S: Phase 2: Analysis
        S->>S: Task 2.1: Análisis comparativo
        S->>S: Task 2.2: Identificar patterns
        S->>S: Task 2.3: Recomendar framework
        S->>S: Task 2.4: Síntesis final (≥1500 words)
        S->>CK: Task 2.5: Checkpoint CK-02
    end

    alt CK-02 PASS + Approved
        CK-->>MO: Proceed to MORPHEUS
    else CK-02 FAIL
        CK-->>S: Retry: Expand analysis
    end

    rect rgb(255, 240, 255)
        Note over MO: Phase 3: Build
        MO->>MO: Task 3.1: Solution spec (≥2000 lines)
        MO->>MO: Task 3.2: Implementation plan
        MO->>MO: Task 3.3: Testing strategy
        MO->>MO: Task 3.4: Cypher queries
        MO->>MO: Task 3.5: Generate embeddings
        MO->>MO: Task 3.6: Load scripts
        MO->>CK: Task 3.7: Checkpoint CK-03 (Auto)
    end

    CK-->>A: Proceed to ALMA (auto-approved)

    rect rgb(255, 255, 240)
        Note over A: Phase 4: Execute
        A->>A: Task 4.1: Load to Neo4j
        A->>A: Task 4.2: Validate graph
        A->>A: Task 4.3: Generate visualizations
        A->>A: Task 4.4: Validate hypotheses
        A->>CK: Task 4.5: Checkpoint CK-04
    end

    alt CK-04 PASS + Approved
        CK-->>M: Proceed to Lessons
    else CK-04 FAIL
        CK-->>A: Retry: Fix data issues
    end

    rect rgb(248, 248, 248)
        Note over M,A: Phase 5: Lessons Learned
        M->>M: Task 5.1: Document lessons per rostro
        M->>M: Task 5.2: Aggregate summary.yaml
        M->>M: Task 5.3: Improve template v2.0.0
    end

    M-->>U: ✅ Research Complete
```

### MCP Workflow: Task 1.1 (Parallel Search)

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Copilot Agent
    participant Brave as brave-search MCP
    participant arXiv as arxiv MCP
    participant C7 as context7 MCP
    participant FS as filesystem MCP
    participant Mem as memory MCP

    Note over Agent: Activate MCPs first
    Agent->>Brave: activate_brave_search_tools
    Agent->>C7: activate_library_documentation_tools

    Note over Agent,C7: PARALLEL EXECUTION (no dependencies)

    par Search Academic Papers
        Agent->>arXiv: search_papers("{{research.name}}")
        arXiv-->>Agent: Papers list (20 results)
    and Search Web Resources
        Agent->>Brave: brave_search("{{research.name}} frameworks best practices")
        Brave-->>Agent: Web results (20 results)
    and Search Library Docs
        Agent->>C7: resolve-library-id("{{research.name}}")
        C7->>C7: get-library-docs(id)
        C7-->>Agent: Documentation (5+ pages)
    end

    Note over Agent: SEQUENTIAL PROCESSING (has dependencies)

    Agent->>Agent: Aggregate results (papers + web + docs)
    Agent->>Agent: Deduplicate by DOI/URL
    Agent->>Agent: Filter by quality (peer-reviewed, recent)
    Agent->>Agent: Validate: ≥{{min_sources}} sources?

    alt Validation PASS
        Agent->>FS: Write sources.yaml
        Agent->>Mem: Store source IDs for Task 1.2
        Agent-->>Agent: ✅ Task 1.1 Complete
    else Validation FAIL (<5 sources)
        Agent->>Agent: Expand search (broader query)
        Agent->>Brave: brave_search("{{research.name}} alternatives")
    end
```

### MCP Workflow: Task 1.3 (Atomization with Sequential Thinking)

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Copilot Agent
    participant Think as sequential-thinking
    participant FS as filesystem MCP
    participant Mem as memory MCP

    Note over Agent: Thinking Mode: sequential-thinking

    Agent->>FS: Read all papers from 01-literature/
    FS-->>Agent: Paper contents

    loop For Each Paper
        Agent->>Think: Think(thought: "Identify main concepts in paper-001")
        Think-->>Agent: Concepts list (5-10 per paper)

        loop For Each Concept
            Agent->>Think: Think(thought: "Is this atomic? One idea only?")
            Think-->>Agent: Yes/No + reasoning

            alt Is Atomic
                Agent->>Think: Think(thought: "Extract definition + context")
                Think-->>Agent: Definition, context, examples
                Agent->>FS: Write atomic-XXX.md
                Agent->>Mem: Store {id, title, source, tags}
            else Not Atomic
                Agent->>Think: Think(thought: "Break into sub-concepts")
                Think-->>Agent: Sub-concepts list
                Note over Agent: Process each sub-concept
            end
        end
    end

    Agent->>Agent: Validate: ≥{{min_atomics}} atomics?
    Agent->>FS: Write atomics-index.yaml
```

### MCP Workflow: Task 2.3 (Framework Recommendation with Branch Exploration)

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Copilot Agent
    participant Smart as smart-thinking
    participant Mem as memory MCP
    participant FS as filesystem MCP

    Note over Agent: Thinking Mode: smart-thinking (branch exploration)

    Agent->>Mem: Load atomics + patterns from memory
    Agent->>Smart: Create main reasoning branch

    par Explore Framework Options (Parallel Branches)
        rect rgb(240, 248, 255)
            Agent->>Smart: create_branch("dsr-evaluation")
            loop Analyze DSR
                Smart->>Smart: Think(thought: "Evaluate DSR fit")
            end
            Smart-->>Agent: DSR: pros, cons, score=8/10
        end
    and
        rect rgb(255, 248, 240)
            Agent->>Smart: create_branch("crisp-dm-evaluation")
            loop Analyze CRISP-DM
                Smart->>Smart: Think(thought: "Evaluate CRISP-DM fit")
            end
            Smart-->>Agent: CRISP-DM: pros, cons, score=6/10
        end
    and
        rect rgb(240, 255, 240)
            Agent->>Smart: create_branch("zettelkasten-evaluation")
            loop Analyze Zettelkasten
                Smart->>Smart: Think(thought: "Evaluate Zettelkasten fit")
            end
            Smart-->>Agent: Zettelkasten: pros, cons, score=9/10
        end
    end

    Agent->>Smart: list_branches()
    Smart-->>Agent: 3 branch summaries

    Agent->>Smart: merge_branch("dsr-evaluation", strategy: "summary")
    Agent->>Smart: merge_branch("crisp-dm-evaluation", strategy: "summary")
    Agent->>Smart: merge_branch("zettelkasten-evaluation", strategy: "summary")

    Agent->>Smart: Think(thought: "Compare frameworks, recommend best")
    Smart-->>Agent: Recommendation: Zettelkasten + DSR hybrid

    Agent->>FS: Write framework-decision.md (ADR style)
```

### MCP Workflow: Task 2.4 (Final Synthesis with Deep Reasoning)

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Copilot Agent
    participant Perp as perplexity MCP
    participant Mem as memory MCP
    participant FS as filesystem MCP

    Note over Agent: Thinking Mode: perplexity_reason (deep reasoning)

    Agent->>Mem: Load all context (atomics, patterns, analysis)
    Mem-->>Agent: Full research context

    Agent->>Perp: perplexity_reason(messages: [system, user with RQs + context])

    Note over Perp: sonar-reasoning-pro model
    Perp->>Perp: Deep multi-step reasoning
    Perp->>Perp: Verify reasoning chain
    Perp->>Perp: Generate synthesis (≥1500 words)
    Perp-->>Agent: Comprehensive synthesis

    Agent->>Agent: Validate: All RQs answered?

    alt All RQs Covered
        Agent->>Agent: Validate: Word count ≥1500?
        Agent->>FS: Write final-synthesis.md
    else Missing RQ Answers
        Agent->>Perp: perplexity_reason(messages: ["Expand on RQ2..."])
        Perp-->>Agent: Extended answer
    end
```

### Triple Output Pipeline

```mermaid
sequenceDiagram
    autonumber
    participant Atomic as Atomic Concept<br/>(02-atomics/)
    participant MD as Markdown<br/>(Filesystem)
    participant Graph as Neo4j<br/>(Graph DB)
    participant Vec as Embeddings<br/>(Vectors)

    Note over Atomic,Vec: Each artifact exists in 3 dimensions (P6: Trazabilidad)

    rect rgb(240, 248, 255)
        Note over Atomic,MD: Dimension 1: Markdown
        Atomic->>MD: Write atomic-001.md
        MD->>MD: Store with HKM + Dublin Core metadata
        MD-->>Atomic: ✅ Persisted in filesystem
    end

    rect rgb(255, 248, 240)
        Note over Atomic,Graph: Dimension 2: Graph
        Atomic->>Graph: Transform to node.yaml
        Graph->>Graph: MERGE (n:Concept {id: "atomic-001"})
        Graph->>Graph: Create relationships
        Graph-->>Atomic: ✅ Persisted in Neo4j
    end

    rect rgb(240, 255, 240)
        Note over Atomic,Vec: Dimension 3: Vectors
        Atomic->>Vec: Generate embedding (qwen3-embedding)
        Vec->>Vec: 1536-dimensional vector
        Vec->>Graph: Store in Neo4j HNSW index
        Vec-->>Atomic: ✅ Indexed for semantic search
    end

    Note over MD,Vec: Query can use any dimension
```

### Checkpoint Decision Flow

```mermaid
flowchart TD
    Start([Task X.6: Checkpoint]) --> Validate{Validate<br/>Criteria}

    Validate -->|All criteria met| Status[status: PASS]
    Validate -->|Criteria not met| Fail[status: FAIL]

    Fail --> FixIssues[Fix Issues]
    FixIssues --> ReRun[Re-run previous tasks]
    ReRun --> Validate

    Status --> CheckApproval{require_approval?}

    CheckApproval -->|true| WaitApproval[Wait for Manual Approval]
    CheckApproval -->|false| AutoApprove[Auto-approved]

    WaitApproval --> UserReview[User reviews artifacts]
    UserReview --> Approve{Approved?}

    Approve -->|Yes| UpdateYAML[Update validation.yaml<br/>approved_by, approved_at]
    Approve -->|No| FixIssues

    UpdateYAML --> Proceed[Proceed to Next Rostro]
    AutoApprove --> Proceed

    Proceed --> End([Next Phase])

    style Start fill:#e1f5fe
    style End fill:#c8e6c9
    style Fail fill:#ffcdd2
    style Status fill:#c8e6c9
```

---

## 🚀 Quick Start: Instanciar una Investigación

### Paso 1: Copiar template y parametrizar

```powershell
# Copiar template a nueva investigación
$NewResearchName = "dsr"  # Cambiar por tu investigación
$TemplatePath = ".\.spec-workflow\specs\research-methodology-template"
$NewSpecPath = ".\.spec-workflow\specs\research-$NewResearchName"

Copy-Item -Recurse $TemplatePath $NewSpecPath
```

### Paso 2: Editar config.yaml

Abrir [config.yaml](config.yaml) y cambiar:

```yaml
research:
  name: "dsr"                            # ← ID único (slug)
  full_name: "Design Science Research"   # ← Nombre completo
  type: "formal-review"                  # ← formal-review | quick-scan | deep-dive
  version: "1.0.0"
  created: "2026-01-09"                  # ← Fecha de inicio
  owner: "MELQUISEDEC"

scope:
  research_questions:
    - "RQ1: ¿Qué es Design Science Research y cómo se estructura?"
    - "RQ2: ¿Cuáles son los artefactos típicos de DSR?"
    - "RQ3: ¿Cómo se evalúan artefactos en DSR?"

  domains:
    - "research-methodology"
    - "design-science"
    - "software-engineering"

  hypothesis:
    - "H1: DSR puede integrarse con Zettelkasten para gestión atómica"
    - "H2: Neo4j puede representar relaciones DSR efectivamente"
```

### Paso 3: Ejecutar workflow

```powershell
# Ver tasks.md para workflow MCP detallado por task
code ".\.spec-workflow\specs\research-$NewResearchName\tasks.md"

# Ejecutar Task 0.1 con orchestrator
# Ver _meta/orchestrator.md para comandos PowerShell
```

---

## 📋 Workflow DAATH-ZEN (5 Rostros)

```mermaid
graph TD
    M[MELQUISEDEC<br/>Orquestador] -->|Init| H[HYPATIA<br/>Investigadora]
    H -->|Literature +<br/>Atomization| CK1{Checkpoint<br/>CK-01}
    CK1 -->|Approved| S[SALOMON<br/>Arquitecto]
    S -->|Analysis +<br/>Synthesis| CK2{Checkpoint<br/>CK-02}
    CK2 -->|Approved| MO[MORPHEUS<br/>Implementador]
    MO -->|Artifacts +<br/>Scripts| CK3{Checkpoint<br/>CK-03}
    CK3 -->|Auto-approved| A[ALMA<br/>Ejecutora]
    A -->|Execution +<br/>Validation| CK4{Checkpoint<br/>CK-04}
    CK4 -->|Approved| L[Lessons Learned]
    L -->|P2: Autopoiesis| M
```

### Resumen por Rostro

| Rostro | Phase | Tasks | Thinking Mode | Key MCPs | Checkpoint |
|--------|-------|-------|---------------|----------|------------|
| **MELQUISEDEC** | 0-Init | 0.1 | None | filesystem | None |
| **HYPATIA** | 1-Research | 1.1-1.6 | sequential-thinking | brave, arxiv, context7 | CK-01 (manual) |
| **SALOMON** | 2-Analysis | 2.1-2.5 | smart-thinking | memory, perplexity | CK-02 (manual) |
| **MORPHEUS** | 3-Build | 3.1-3.7 | None | neo4j, ollama | CK-03 (auto) |
| **ALMA** | 4-Execute | 4.1-4.5 | None | neo4j | CK-04 (manual) |
| **ALL** | 5-Lessons | 5.1-5.3 | None | filesystem | None |

---

## 🔧 MCP Orchestration Patterns

### Pattern 1: Parallel Search
**Use case**: Task 1.1 (Literature discovery)
**MCPs**: brave-search + arxiv + context7 (parallel)
**Strategy**: Execute all searches simultaneously, aggregate results

### Pattern 2: Sequential Transform
**Use case**: Task 1.3 (Atomization)
**Thinking**: sequential-thinking
**Strategy**: Process each paper sequentially, extract atomics step by step

### Pattern 3: Branch Exploration
**Use case**: Task 2.3 (Framework recommendation)
**Thinking**: smart-thinking with branches
**Strategy**: Create parallel reasoning branches, merge summaries

### Pattern 4: Deep Reasoning
**Use case**: Task 2.4 (Final synthesis)
**Thinking**: perplexity_reason
**Strategy**: Multi-step reasoning with verification

### Pattern 5: Load & Verify
**Use case**: Task 4.1-4.2 (Neo4j ingestion)
**MCPs**: neo4j (write → verify)
**Strategy**: MERGE (idempotent), then validate integrity

---

## 🔍 Example: DSR Investigation

**Scenario**: Investigar "Design Science Research" para adoptar en MELQUISEDEC.

### Estructura generada

```
apps/research-dsr/
├── ISSUE.yaml                           ← HKM + Dublin Core metadata
├── README.md
├── 00-problem/
│   └── problem-statement.md
├── 01-literature/
│   ├── sources.yaml                     ← HYPATIA: 10+ fuentes
│   └── content/
│       ├── paper-001-hevner2004.md
│       └── paper-002-peffers2007.md
├── 02-atomics/
│   ├── concepts/
│   │   ├── atomic-001-dsr-definition.md
│   │   ├── atomic-002-dsr-phases.md
│   │   └── atomic-003-build-artifact.md
│   ├── relationships.yaml
│   └── graph-ready/
│       ├── nodes.yaml
│       └── relationships.yaml
├── 03-workbook/
│   ├── comparative-analysis.md
│   ├── workflow-patterns.md
│   ├── final-synthesis.md               ← ≥1500 words
│   └── framework-decision.md            ← ADR-style
├── 04-artifacts/
│   ├── scripts/
│   │   ├── load_to_neo4j.py
│   │   └── generate_embeddings.py
│   ├── cypher/
│   │   ├── create_nodes.cypher
│   │   └── create_relationships.cypher
│   ├── embeddings/
│   │   └── vectors.json
│   └── solution-spec.md                 ← ≥2000 lines
├── 05-evaluate/
│   ├── graph-validation.md
│   ├── hypothesis-validation.md
│   └── visualizations/
├── 06-lessons/
│   └── summary.yaml
└── .melquisedec/
    ├── hypatia_validation.yaml
    ├── salomon_validation.yaml
    ├── morpheus_validation.yaml
    └── alma_validation.yaml
```

---

## 🎛️ Configuración Avanzada

### Quality Metrics (config.yaml)

```yaml
quality:
  metrics:
    min_sources: 5                      # Mínimo fuentes para HYPATIA
    min_peer_reviewed: 3                # Mínimo papers peer-reviewed
    min_atomics: 20                     # Mínimo atomic concepts
    min_patterns: 5                     # Mínimo patterns identificados
    min_synthesis_words: 1500           # Mínimo palabras en síntesis
    min_solution_spec_lines: 2000       # Mínimo líneas en solution-spec
    min_test_coverage: 80               # Mínimo % test coverage
```

### MCP Tools Required (config.yaml)

```yaml
required_mcps:
  base:
    - neo4j              # Graph database
    - memory             # Context management
    - filesystem         # File operations

  specialized:
    - brave-search       # Web search
    - arxiv              # Academic papers
    - context7           # Library docs
    - perplexity         # Deep research

  thinking:
    - sequential-thinking  # Step-by-step analysis
    - smart-thinking       # Branch exploration

  optional:
    - github-search      # Code examples
    - markitdown         # Format conversion
```

---

## 🧪 Testing & Validation

### Task-level Validation

Cada task en [tasks.md](tasks.md) incluye:
- **MCP Workflow Strategy**: Thinking mode, parallel vs sequential, activations
- **Success Criteria**: Condiciones explícitas para PASS
- **Validation**: Comandos PowerShell para verificar output

---

## 📚 Documentation Reference

| File | Purpose | Audience |
|------|---------|----------|
| [config.yaml](config.yaml) | Single source of truth (parametrization) | All rostros |
| [requirements.md](requirements.md) | WHAT + WHY (requirements phase) | Stakeholders |
| [design.md](design.md) | HOW (architecture design + MCP patterns) | Developers |
| [tasks.md](tasks.md) | Detailed task breakdown + MCP workflows | Executors |
| [_meta/orchestrator.md](_meta/orchestrator.md) | Executable workflow automation | Operators |
| **README.md** (this file) | Usage guide + architecture diagrams | All users |

---

## 🔄 Autopoiesis (P2)

**Mejora Continua del Template**:

1. Cada investigación genera lessons learned (Task 5.1)
2. Lessons agregadas en `summary.yaml` (Task 5.2)
3. Template v2.0.0 incorpora mejoras (Task 5.3)

---

## 📞 Support

- **Issues**: Usar GitHub Issues del repositorio
- **Docs**: Ver `docs/guides/` para guías adicionales
- **Principios**: `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md`

---

**Template Version**: 1.1.0
**Last Updated**: 2026-01-09
**Maintainer**: MELQUISEDEC
**Status**: ✅ Production Ready
