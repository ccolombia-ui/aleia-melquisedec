# 4-canvas/ - Visual Models and Diagrams

## Purpose

This folder contains visual representations of the methodology: workflows, conceptual models, process flows, and relationship diagrams. Visualizations make complex concepts accessible and provide at-a-glance understanding.

## File Types

### Mermaid Diagrams (Preferred)
Use Mermaid markdown for version-controllable diagrams:
- **Flowcharts**: Process workflows, decision trees
- **Sequence diagrams**: Interactions over time
- **Class diagrams**: Concept structures and relationships
- **State diagrams**: State transitions
- **Entity-relationship diagrams**: Data models
- **Gantt charts**: Timeline visualizations

### Other Formats (if needed)
- **PNG/SVG**: Hand-drawn sketches or external diagrams
- **PlantUML**: Complex UML diagrams
- **Graphviz**: Graph structures

## Common Visualizations

### 1. workflow-overview.md
**Purpose:** Shows end-to-end methodology execution

```mermaid
flowchart TD
    A[Start: Define Research Scope] --> B[Collect Academic Sources]
    B --> C{Sufficient Sources?}
    C -->|No| B
    C -->|Yes| D[Extract Atomic Concepts]
    D --> E[Analyze Themes]
    E --> F[Create Visualizations]
    F --> G[Map Conceptual Bridges]
    G --> H[Synthesize Findings]
    H --> I[Write Specification]
    I --> J{Validation Pass?}
    J -->|No| K[Revise]
    K --> H
    J -->|Yes| L[End: Publish]
```

### 2. concept-map.md
**Purpose:** Shows how extracted concepts relate

```mermaid
graph TD
    ONT[Ontology] --> CLS[Class]
    ONT --> PROP[Property]
    CLS --> INST[Instance]
    CLS --> SUBC[Subclass]
    PROP --> OP[Object Property]
    PROP --> DP[Datatype Property]
    CLS --> AX[Axiom]
    PROP --> AX
    AX --> REAS[Reasoning]
```

### 3. step-dependencies.md
**Purpose:** Shows execution order and parallelism

```mermaid
graph LR
    S1[Step 1: Define Scope] --> S2[Step 2: Collect Sources]
    S2 --> S3[Step 3: Extract Atomics]
    S2 --> S4[Step 4: Analyze Themes]
    S3 --> S5[Step 5: Create Visualizations]
    S4 --> S5
    S3 --> S6[Step 6: Map Bridges]
    S4 --> S6
    S5 --> S7[Step 7: Synthesize]
    S6 --> S7
    S7 --> S8[Step 8: Specification]
```

### 4. data-flow.md
**Purpose:** Shows how information flows through methodology

```mermaid
sequenceDiagram
    participant HYPATIA as HYPATIA (Research)
    participant Sources as 1-literature/
    participant Atomics as 3-atomics/
    participant Analysis as 2-analysis/
    participant SALOMON as SALOMON (Synthesis)
    participant Outputs as 6-outputs/

    HYPATIA->>Sources: Collect sources
    Sources->>HYPATIA: Return papers
    HYPATIA->>Atomics: Extract concepts
    HYPATIA->>Analysis: Analyze themes
    Atomics->>SALOMON: Provide concepts
    Analysis->>SALOMON: Provide patterns
    SALOMON->>Outputs: Generate SPECIFICATION.yaml
```

### 5. conceptual-model.md
**Purpose:** Shows domain entities and relationships

```mermaid
classDiagram
    class Methodology {
        +String name
        +List~Step~ steps
        +List~Concept~ concepts
        +execute()
    }
    class Step {
        +String id
        +String name
        +List~Deliverable~ outputs
        +run()
    }
    class Concept {
        +String id
        +String definition
        +String source
        +List~Example~ examples
    }
    class Atomic {
        +String atomic_id
        +Category category
        +extract()
    }

    Methodology "1" --> "*" Step : contains
    Methodology "1" --> "*" Concept : defines
    Concept <|-- Atomic : is a
    Step "1" --> "*" Concept : uses
```

### 6. timeline-gantt.md
**Purpose:** Shows research timeline and milestones

```mermaid
gantt
    title Academic Research Timeline
    dateFormat YYYY-MM-DD
    section Phase 0: Context
    Define Scope           :done, p0, 2026-01-11, 2h
    Research Questions     :done, p0a, after p0, 2h
    section Phase 1: Collection
    Collect Sources        :active, p1, 2026-01-12, 2d
    Document Sources       :p1a, after p1, 1d
    section Phase 2: Analysis
    Extract Atomics        :p2, 2026-01-15, 2d
    Analyze Themes         :p2a, 2026-01-15, 2d
    section Phase 3: Synthesis
    Create Visualizations  :p3, 2026-01-17, 1d
    Map Bridges            :p3a, 2026-01-17, 1d
    Synthesize             :p3b, 2026-01-18, 1d
    Write Specification    :p3c, 2026-01-19, 1d
```

## Diagram Template

```markdown
---
diagram_id: "VIZ-{number}"
diagram_name: "{Diagram Title}"
type: "{flowchart|sequence|class|state|er|gantt}"
purpose: "{Why this visualization exists}"
related_concepts: ["atomic-{n}", "atomic-{m}"]
related_steps: ["step-{x}", "step-{y}"]
---

# {Diagram Title}

## Purpose

{Why this visualization is needed and what it clarifies}

## Legend (if needed)

- **{Symbol}**: {Meaning}
- **{Color}**: {Significance}
- **{Shape}**: {Represents what}

## Diagram

\`\`\`mermaid
{diagram-type} {orientation}
    {nodes and relationships}
\`\`\`

## Explanation

### Key Elements

1. **{Element 1}**: {What it represents and why it matters}
2. **{Element 2}**: {Explanation}
3. **{Element 3}**: {Explanation}

### Flows / Relationships

- **{Relationship 1}**: {What this connection means}
- **{Relationship 2}**: {Explanation}

### Decision Points (if applicable)

- **At {Node}**: {What decision is made and why}

## Insights from Diagram

{What becomes clearer through this visualization that wasn't obvious in text}

## Related Documentation

- **Concepts**: [[atomic-{n}-{concept}]], [[atomic-{m}-{another}]]
- **Steps**: `3-steps/step-{x}-{action}.md`
- **Analysis**: `2-analysis/themes-{topic}.md`
```

## Mermaid Syntax Reference

### Flowchart
```mermaid
flowchart TD
    A[Rectangle] --> B(Rounded)
    B --> C{Diamond}
    C -->|Yes| D[Result 1]
    C -->|No| E[Result 2]
```

### Sequence Diagram
```mermaid
sequenceDiagram
    Actor1->>Actor2: Message
    Actor2-->>Actor1: Response
    Actor1->>+Actor3: Request
    Actor3-->>-Actor1: Reply
```

### Class Diagram
```mermaid
classDiagram
    Animal <|-- Duck
    Animal : +int age
    Animal : +isMammal()
    class Duck{
        +String beakColor
        +swim()
    }
```

## Quality Criteria

- **3-5 diagrams minimum** for comprehensive visualization
- **Self-explanatory**: Diagrams understandable without extensive text
- **Consistent notation**: Use same symbols/colors for same concepts
- **Cross-referenced**: Link to concepts, steps, analyses
- **Version-controlled**: Mermaid preferred over binary images

## Validation Checklist

- [ ] At least 3 visualization documents exist
- [ ] Each visualization has:
  - [ ] Purpose statement
  - [ ] Complete diagram (Mermaid or other format)
  - [ ] Explanation of key elements
  - [ ] Cross-references to related concepts/steps
- [ ] Mermaid syntax is valid (renders correctly in Markdown previews)
- [ ] Legend provided for non-obvious symbols
- [ ] Diagrams complement text (don't just repeat information)

---

**Maintained by:** HYPATIA (Research Lead) + SALOMON (Synthesis)
**Last Updated:** 2026-01-11
