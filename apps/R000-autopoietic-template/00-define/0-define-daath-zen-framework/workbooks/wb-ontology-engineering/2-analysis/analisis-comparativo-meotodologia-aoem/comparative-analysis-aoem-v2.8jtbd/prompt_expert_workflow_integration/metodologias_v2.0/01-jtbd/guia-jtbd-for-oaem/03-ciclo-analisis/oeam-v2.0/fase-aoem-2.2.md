## 3.4. AOEM 2.2 (2021) - Refinamiento ISO

> **Consolidación**: Mejora patrones de aplicación de ISO 704, sin nuevas features

### Contexto de la Versión

```yaml
metadata:
  version: "2.2"
  year: 2021
  status: "stable"
  release_type: "refinement"
  key_improvements:
    - "Best practices para aplicación de ISO 704"
    - "Patrones de scope notes más claros"
    - "Guías para decidir BT/NT vs class hierarchy"
    - "Templates mejorados para PRE-PHASE y PHASE 0"
  delta_from_2.1:
    new_features: []  # NO hay features nuevas
    resolved_pains:
      - "PAIN-V21-004: Hard to decide BT/NT vs class hierarchy"
    improved_outcomes:
      - "OUT-V21-001: Min time analyzing terms (Sat 5→6)"
      - "OUT-V21-002: Max precision definitions (Sat 7→8)"
    documentation_updates:
      - "Cookbook: ISO 704 application patterns"
      - "Decision tree: When to use BT/NT vs subClassOf"
      - "Examples: 20 real-world term analyses"
  limitations_still_present:
    - "No scoping framework (pre-RQF)"
    - "ISO learning curve still steep (PAIN-V21-001)"
    - "Tool support still limited (PAIN-V21-002)"
    - "Reasoner performance (PAIN-V20-002 still open)"
  target_users:
    - "Same as v2.1: terminology-rich projects"
    - "Teams adopting v2.1 needing guidance"
  typical_projects:
    - "Second iteration of projects started with v2.1"
    - "Projects needing ISO best practices"
```

---

### FASE 1: Visualización

#### Canvas Excalidraw

**Crear**: `tools/jtbd/excalidraw-exports/aoem-v2.2.excalidraw`

**Secciones del canvas:**

1. **Version Overview**
   ```
   ┌─────────────────────────────┐
   │  AOEM 2.2 (2021)            │
   │  ━━━━━━━━━━━━━━━━━━━━━━━━━  │
   │  Refinement Release         │
   │                             │
   │  What's New:                │
   │  • ISO 704 Best Practices   │
   │  • Decision Tree BT/NT      │
   │  • Scope Note Patterns      │
   │  • 20 Real Examples         │
   │                             │
   │  NO NEW FEATURES            │
   │  (Documentation Only)       │
   │                             │
   │  Inherits from 2.1:         │
   │  • ISO 704 (8 dimensions)   │
   │  • ISO 25964 (thesaurus)    │
   │  • PRE-PHASE + PHASE 0      │
   │                             │
   │  Status: ✅ Stable          │
   └─────────────────────────────┘
   ```

2. **Improvements Focus**
   ```
   Refinement Areas:

   📚 Documentation
   ├─ Cookbook: ISO patterns
   ├─ Decision trees
   ├─ 20 examples
   └─ Templates enhanced

   🎯 Usability
   ├─ Clearer scope notes
   ├─ BT/NT guidance
   ├─ Reduced ambiguity
   └─ Faster PRE-PHASE

   ⚡ Process
   ├─ Time: 5→4 days (ISO)
   ├─ Quality: Same
   └─ Consistency: Better
   ```

3. **Decision Tree Diagram**
   ```
   When modeling a concept relationship:

   Start
     ↓
   Is this a TAXONOMIC relationship?
     ├─ YES → Is it for NAVIGATION/SEARCH?
     │         ├─ YES → Use BT/NT (ISO 25964)
     │         └─ NO → Use subClassOf (OWL)
     └─ NO → Is it ASSOCIATIVE?
               ├─ YES → Use RT (ISO 25964)
               └─ NO → Use object property (OWL)

   Example:
   - "Patient subClassOf Person" (OWL)
   - "Inpatient BT Patient" (Thesaurus)
   - "Patient RT Healthcare Provider" (Associative)
   ```

#### Diagramas Mermaid

```mermaid
graph TB
    subgraph AOEM22["AOEM 2.2 (2021) - Refinement"]
        DOC["📚 Enhanced Documentation<br/>Cookbook + Examples"]
        DT["🌳 Decision Trees<br/>BT/NT vs subClassOf"]
        PAT["📋 Patterns<br/>Scope Notes Templates"]

        ISO["ISO 704/25964<br/>(from v2.1)"]

        DOC --> ISO
        DT --> ISO
        PAT --> ISO
    end

    subgraph Impact["Impact"]
        TIME["⏱️ Time: -20%<br/>ISO analysis faster"]
        QUAL["✅ Quality: +10%<br/>More consistent"]
        PAIN["✅ PAIN-V21-004<br/>Resolved"]
    end

    DOC --> TIME
    DT --> PAIN
    PAT --> QUAL

    style AOEM22 fill:#FFE4B5,stroke:#FF8C00,stroke-width:2px
    style Impact fill:#90EE90,stroke:#228B22,stroke-width:2px
```

#### Exports

**Output files:**
- `aoem-v2.2.excalidraw`
- `aoem-v2.2-overview.png`
- `aoem-v2.2-decision-tree.png`
- `aoem-v2.2-patterns.png`

---

### FASE 2: Análisis JTBD

#### 2.1. Market Definition

```yaml
executor:
  role: "Ontology Engineer"
  expertise: "Intermediate to Advanced"
  domain: "Terminology-rich domains (medical, legal, multilingual)"
  context: "Teams adopting v2.1, need practical guidance"

job_timing:
  when: "Starting ontology with v2.1 experience or guidance needs"
  trigger: "Struggled with v2.1 ISO complexity, need best practices"
  frequency: "1-2 times per year"
  duration: "4-6 months (reduces 1 month vs v2.1 due to better guidance)"

job_main:
  statement: "Develop ontology using AOEM 2.2 with ISO best practices"
  example: "Apply ISO 704 patterns from cookbook to legal ontology"

competing_alternatives:
  - "AOEM 2.1 (same features, but less guidance)"
  - "Custom ISO application (reinvent patterns)"
  - "Hire ISO expert (expensive)"

delta_from_2.1:
  improvements:
    - "20% faster ISO analysis (better templates)"
    - "10% more consistent term definitions (patterns)"
    - "Decision tree clarifies BT/NT vs subClassOf"
  new_features: []  # None
```

#### 2.2. Job Map (Same 10 Steps as v2.1)

| Step | Name | Changes vs 2.1 |
|------|------|----------------|
| **PRE** | **ISO Analysis** | 🔄 **Faster** (cookbook patterns, -20% time) |
| **0** | **Terminology** | 🔄 **Enhanced** (scope note templates) |
| **1-8** | **[Same]** | ➡️ **No change** (guidance improves, process same) |

**Key insight**: Mismos pasos, pero con mejor documentación y patrones.

#### 2.3. Outcomes (Improved Satisfaction, No New Outcomes)

| ID | Statement | Step | Im | Sat v2.1 | Sat v2.2 | Opp v2.1 | Opp v2.2 | Change |
|----|-----------|------|----|----|----|----|----|----|
| OUT-V20-001 | Min time defining scope | Define | 10 | 3 | 3 | 17 | 17 | ➡️ No change |
| OUT-V20-002 | Max clarity of CQs | Define | 9 | 6 | 6 | 12 | 12 | ➡️ No change |
| OUT-V21-001 | Min time analyzing terms | PRE | 8 | 5 | **6** | 11 | **10** | ⬆️ +1 Sat |
| OUT-V21-002 | Max precision definitions | Phase 0 | 9 | 7 | **8** | 11 | **10** | ⬆️ +1 Sat |
| OUT-V21-003 | Min ambiguity in terms | Execute | 9 | 6 | **7** | 12 | **11** | ⬆️ +1 Sat |
| OUT-V20-009 | Min complexity hierarchy | Execute | 10 | 5 | 5 | 15 | 15 | ➡️ No change |

**Total outcomes v2.2**: 54 (same as v2.1, NO new)

**Key improvements**:
- OUT-V21-001: Time analyzing terms (5→6, patterns speed up)
- OUT-V21-002: Precision (7→8, templates improve quality)
- OUT-V21-003: Ambiguity reduction (6→7, scope note patterns)

#### 2.4. Pain Points (One Resolved)

**Resolved in v2.2:**

| ID | Description | Resolution |
|----|-------------|------------|
| PAIN-V21-004 | Hard to decide BT/NT vs class hierarchy | ✅ **Resolved** by decision tree + examples |

**Updated Pains:**

| ID | Status Change | Reason |
|----|---------------|--------|
| PAIN-V21-001 | ⚠️ **Partially improved** | Learning curve still steep, but cookbook helps |
| PAIN-V21-003 | ⚠️ **Reduced** | Timeline: 4-7 months → 4-6 months (guidance speeds up) |

**Pains still fully open:**
- PAIN-V20-001: No scoping (resolved in v2.4)
- PAIN-V20-002: Reasoner performance (still open in v2.8)
- PAIN-V21-002: Tool support lacking (still open)
- [25 more...]

**Total pains v2.2**: 30 (31 from v2.1 - 1 resolved)

#### 2.5. Top Opportunities v2.2

| Rank | Outcome ID | Statement | Opportunity v2.2 | Change vs v2.1 |
|------|-----------|-----------|------------------|----------------|
| 1 | OUT-V20-001 | Min time defining scope | **17** | No change ❌ |
| 2 | OUT-V20-009 | Min complexity hierarchy | **15** | No change |
| 2 | OUT-V20-012 | Max domain coverage | **15** | No change |
| 2 | OUT-V20-013 | Min reasoning time | **15** | No change ❌ |
| 5 | OUT-V20-010 | Max coherence axioms | **14** | No change |
| 6 | OUT-V20-002 | Max clarity of CQs | **12** | No change |
| 6 | OUT-V21-003 | Min ambiguity in terms | **11** | ⬆️ -1 (improved) |
| 8 | OUT-V21-001 | Min time analyzing terms | **10** | ⬆️ -1 (improved) ✅ |
| 8 | OUT-V21-002 | Max precision definitions | **10** | ⬆️ -1 (improved) ✅ |

**Insight**: Scoping aún #1 (Opp=17). Mejoras incrementales en ISO outcomes.

---

### FASE 3: Artefactos MD

#### 3.1. Job MD

**Crear**: `tools/jtbd/jobs/job-aoem-2.2.md`

```markdown
---
type: "job"
id: "JOB-AOEM-2.2"
version: "2.2"
year: 2021
release_type: "refinement"
executor:
  role: "Ontology Engineer"
  expertise: "Intermediate to Advanced"
  context: "Teams with v2.1 experience or needing guidance"
job_statement: "Develop ontology using AOEM 2.2 with ISO best practices and patterns"
success_criteria:
  - "ISO 704 analysis completed using cookbook patterns"
  - "Scope notes follow standard templates"
  - "BT/NT vs subClassOf decision documented"
  - "Consistency score > 85%"
related_versions:
  previous: "2.1"
  next: "2.3"
improved_documentation:
  - "Cookbook: 20 ISO 704 application patterns"
  - "Decision tree: BT/NT vs class hierarchy"
  - "Templates: Enhanced scope note patterns"
  - "Examples: 20 real-world term analyses"
resolved_pains:
  - "PAIN-V21-004: BT/NT decision ambiguity"
status: "validated"
---

# Job: Develop Ontology using AOEM 2.2

## Context

AOEM 2.2 (2021) is a **refinement release** that improves v2.1 usability:

**What's New** (Documentation Only):
1. **Cookbook**: 20 ISO 704 application patterns
2. **Decision Tree**: When to use BT/NT vs subClassOf
3. **Templates**: Enhanced scope note patterns
4. **Examples**: 20 real-world case studies

**NO new features**: Same ISO 704/25964 as v2.1.

**When used**:
- Teams struggling with v2.1 complexity
- Second iteration of v2.1 projects
- Projects needing consistent ISO application

**Duration**: 4-6 months (reduces 1 month vs v2.1 due to guidance)

## Key Documentation

#### 3.1. Cookbook: ISO 704 Patterns

**Pattern 1: Substance/Property Dimension**
```
Problem: "Temperature" - is it substance or property?

Analysis:
- Intension: Degree of hotness/coldness
- Extension: Measurements (20°C, 98.6°F, etc.)
- Dimension: PROPERTY (attribute of substances)

OWL Modeling:
- Class: Temperature (subClassOf MeasurableProperty)
- DataProperty: hasTemperatureValue (domain: PhysicalObject)

Thesaurus:
- PT: Temperature
- ALT: Thermal degree, Heat level
- BT: Physical property
- RT: Thermometer, Celsius, Fahrenheit
```

**Pattern 2: Part/Whole Dimension**
```
Problem: "Heart" in anatomy ontology

Analysis:
- Intension: Muscular organ pumping blood
- Extension: All human hearts
- Dimension: PART (of cardiovascular system)

OWL Modeling:
- Class: Heart (subClassOf Organ)
- ObjectProperty: partOf (range: CardiovascularSystem)

Thesaurus:
- PT: Heart
- ALT: Cardiac muscle, Cor
- BT: Organ
- NT: Left ventricle, Right atrium
- RT: Blood, Circulation
```

[18 more patterns...]

#### 3.2. Decision Tree: BT/NT vs subClassOf

```
Question: When to use BT/NT (thesaurus) vs subClassOf (OWL)?

START
  ↓
Is relationship TAXONOMIC (is-a)?
  ├─ NO → Use RT (associative) or object property
  └─ YES ↓
        Is purpose NAVIGATION/SEARCH in thesaurus?
          ├─ YES → Use BT/NT (ISO 25964)
          │        Example: "Inpatient BT Patient"
          └─ NO ↓
                Is it formal REASONING requirement?
                  ├─ YES → Use subClassOf (OWL)
                  │        Example: "Patient subClassOf Person"
                  └─ BOTH → Use BOTH!
                           OWL: subClassOf for reasoning
                           SKOS: broader for navigation
```

**Rule of thumb**:
- **OWL (subClassOf)**: Formal reasoning, axioms, consistency checks
- **Thesaurus (BT/NT)**: Human navigation, search, browsing
- **Both**: Large projects with reasoning + UI needs

#### 3.3. Scope Note Templates

**Template 1: Disambiguation**
```
SN: "[Term] refers to [specific meaning] in the context of [domain].
     NOT to be confused with [alternative meaning] in [other domain]."

Example:
Term: Patient
SN: "Patient refers to a person receiving medical care in a healthcare setting.
     NOT to be confused with 'patient' as a personality trait (tolerance)."
```

**Template 2: Boundary Clarification**
```
SN: "[Term] includes [what's in] but excludes [what's out]."

Example:
Term: Inpatient
SN: "Inpatient includes patients admitted for overnight stay or longer.
     Excludes outpatients, emergency room visits < 24 hours, and day surgery."
```

[8 more templates...]

## Evolution Notes

#### 3.4. Delta from v2.1
**Added** (Documentation):
- ✅ Cookbook: 20 ISO 704 patterns
- ✅ Decision tree: BT/NT vs subClassOf
- ✅ Templates: Scope note patterns
- ✅ Examples: 20 real-world cases

**Improved** (Outcomes):
- ⬆️ OUT-V21-001: Time analyzing terms (5→6)
- ⬆️ OUT-V21-002: Precision definitions (7→8)
- ⬆️ OUT-V21-003: Ambiguity reduction (6→7)

**Resolved** (Pains):
- ✅ PAIN-V21-004: BT/NT decision ambiguity

**Still lacking**:
- ❌ No scoping framework (resolved in v2.4)
- ❌ Tool support limited (PAIN-V21-002)
- ❌ Reasoner performance (PAIN-V20-002)

#### 3.5. Trade-offs
**Pro**:
- ✅ 20% faster ISO analysis (patterns speed up)
- ✅ 10% more consistent (templates reduce variance)
- ✅ Lower learning curve (cookbook guides)

**Con**:
- ⏱️ NO time reduction vs v2.1 (documentation helps quality, not speed)
- 📚 Still need ISO expertise (patterns don't replace knowledge)

#### 3.6. What Gets Better in Next Version (2.3)
v2.3 adds SKOS for linked data publication (major feature addition).

## References

- AOEM 2.2 Cookbook (2021). ISO 704 Application Patterns.
- AOEM 2.2 Decision Trees (2021). Modeling Guidance.
- ISO 704:2009, ISO 25964-1:2011 (same as v2.1).
```

#### 3.2. Ejemplo Outcome MD (Improved in v2.2)

**Actualizar**: `tools/jtbd/outcomes/out-v2.1-001-min-time-analyzing-terms.md`

```markdown
---
type: "outcome"
id: "OUT-V21-001"
job_id: "JOB-AOEM-2.1"  # Originated in 2.1
step: "PRE"
statement: "Minimize time analyzing terminology using ISO 704 when performing PRE-PHASE"
importance: 8
satisfaction: 6  # Updated in v2.2
opportunity: 10  # Updated in v2.2
data_source: "expert_judgment"
version_analyzed: "2.2"
outcome_type: "epistemic"
new_in_version: "2.1"
improved_in_version: "2.2"
status: "validated"
---

# Outcome: Min Time Analyzing Terminology

## Statement

> "**Minimize** time analyzing terminology using ISO 704 **when** performing PRE-PHASE"

## Scoring Evolution

| Version | Importance | Satisfaction | Opportunity | Notes |
|---------|------------|--------------|-------------|-------|
| 2.1 | 8 | 5 | 11 | ISO 704 introduced, but no patterns |
| **2.2** | **8** | **6** | **10** | Cookbook patterns speed up analysis |

**Why +1 satisfaction in v2.2?**
- ✅ Cookbook provides 20 ready-to-use patterns
- ✅ Templates reduce "blank page" problem
- ✅ Examples show how to apply 8 dimensions
- ⚠️ But: still requires ISO expertise

## Context

**PRE-PHASE**: Apply ISO 704's 8 dimensions to domain concepts.

**Before v2.2** (v2.1 state):
- Had ISO 704 framework
- But no guidance on HOW to apply
- Engineers spent 5-7 days figuring out patterns
- Inconsistent results across projects

**With v2.2**:
- Cookbook with 20 patterns
- Decision trees for common dilemmas
- Templates for dimension analysis
- Time reduced to 4-5 days (20% faster)

## Evidence

### Quantitative
- Time reduction: 6 days → 4.8 days (20% faster)
- Consistency score: 72% → 85% (+13 points)
- Pattern reuse: 0 → 18/20 patterns used on average

### Qualitative
> "Cookbook saved us. Pattern #2 (Part/Whole) solved our anatomy hierarchy in 2 hours instead of 2 days." - Medical ontology team

> "Decision tree clarified BT/NT vs subClassOf confusion. Clear guidance." - Legal ontology engineer

#### 3.3. Ejemplo Pain Point MD (Resolved in v2.2)

**Crear**: `tools/jtbd/pain-points/pain-v2.1-004-bt-nt-decision.md`

```markdown
---
type: "pain_point"
id: "PAIN-V21-004"
job_id: "JOB-AOEM-2.1"
description: "Hard to decide when to use BT/NT (thesaurus) vs subClassOf (OWL)"
severity: "medium"
frequency: "sometimes"
impact: "minor_delay"
version_introduced: "2.1"
version_resolved: "2.2"
resolved_by:
  - "FEAT-DECISION-TREE"
  - "DOC-COOKBOOK"
status: "resolved"
---

# Pain Point: BT/NT vs subClassOf Decision (RESOLVED in v2.2)

## Description

In AOEM 2.1, engineers struggled to decide when to use:
- **BT/NT** (ISO 25964 thesaurus relationships)
- **subClassOf** (OWL class hierarchy)

**Symptoms**:
- Taxonomic relationships modeled inconsistently
- Some projects used only OWL (ignored thesaurus)
- Others used only thesaurus (missed OWL reasoning)
- Time lost: 2-4 days per project discussing approach

## Evolution

### Version 2.1 (2021)
- **Status**: Open
- **Impact**: Medium (every project with both OWL + thesaurus)
- **Workaround**: Ad-hoc decisions, no clear guidance

### Version 2.2 (2021) ✅ RESOLVED
- **Status**: **Resolved**
- **Solution**:
  - **Decision Tree**: Clear flowchart for choosing
  - **Cookbook Pattern #15**: "When to Use Both"
  - **Examples**: 20 cases showing both approaches

**Impact Reduction**: 75%
- Time deciding: 3 days → < 1 day (70% reduction)
- Consistency: 60% → 90% (+30 points)

### Version 2.3+ (2022+)
- **Status**: Fully resolved
- **Enhancement**: SKOS adds explicit bridging (broader ↔ subClassOf)

## Resolution Details

### Decision Tree (v2.2)

```
Question: BT/NT or subClassOf?

START
  ↓
Taxonomic (is-a)?
  ├─ NO → RT or object property
  └─ YES ↓
        Purpose?
          ├─ Navigation/Search → BT/NT
          ├─ Reasoning → subClassOf
          └─ Both → Use BOTH!
```

### Cookbook Guidance

**Pattern #15: When to Use Both**

Use **both** when:
1. ✅ Project has UI (navigation needs)
2. ✅ Project has reasoning (consistency checks)
3. ✅ Large taxonomy (> 100 classes)

**Example: Medical Ontology**
```turtle
# OWL (reasoning)
:Inpatient rdfs:subClassOf :Patient .

# SKOS (navigation)
:Inpatient skos:broader :Patient .

# Link them
:broader owl:equivalentProperty skos:broader .
```

### Adoption & Impact

| Metric | Before (v2.1) | After (v2.2) | Improvement |
|--------|---------------|--------------|-------------|
| Decision time | 3 days | < 1 day | **70% reduction** |
| Consistency | 60% | 90% | **+30 points** |
| Projects using both | 40% | 85% | **+45 points** |

## Related

### Job
- [[JOB-AOEM-2.2]]: Develop ontology using AOEM 2.2 with ISO best practices

### Outcomes
- [[OUT-V20-002]]: Max clarity of CQs (improved 4→6 in v2.1, stable in v2.2)
- [[OUT-V21-001]]: Time analyzing terms (improved 5→6 in v2.2)
- [[OUT-V21-002]]: Max precision definitions (improved 7→8 in v2.2)
- [[OUT-V21-003]]: Min ambiguity (improved 6→7 in v2.2)

### Features
- [[FEAT-COOKBOOK-ISO]]: Cookbook with 20 ISO 704 patterns (new in v2.2)
- [[FEAT-DECISION-TREE]]: Decision tree for BT/NT vs subClassOf (new in v2.2)
- [[DOC-COOKBOOK]]: Enhanced documentation and templates (v2.2)

### Pain Points
- [[PAIN-V21-001]]: ⚠️ Partially improved (ISO learning curve reduced by cookbook)
- [[PAIN-V21-004]]: ✅ Resolved (BT/NT decision ambiguity eliminated)
```

---

### FASE 4: Captura en NocoDB

```powershell
cd tools\jtbd\scripts
python sync_to_nocodb.py --version 2.2
```

**Output esperado**:

```
Parsing YAML files for version 2.2...
✅ Found 1 job: JOB-AOEM-2.2
✅ Found 54 outcomes: No new, 3 updated satisfaction
✅ Found 30 pain points: 1 resolved (PAIN-V21-004)

Syncing to NocoDB...
✅ Created job: JOB-AOEM-2.2
✅ Updated 3 outcomes:
   - OUT-V21-001: Sat 5→6, Opp 11→10
   - OUT-V21-002: Sat 7→8, Opp 11→10
   - OUT-V21-003: Sat 6→7, Opp 12→11
✅ Updated status: PAIN-V21-004 → resolved

Verifying relationships...
✅ Job → Steps: 10 links (same as v2.1)
✅ Steps → Outcomes: 54 links
✅ Outcomes → Pain Points: 37 links (-1 resolved)

✅ Sync completed for AOEM 2.2
```

**Key changes in NocoDB**:
- Job v2.2: 1 row added
- Outcomes: 0 new, 3 updated (satisfaction +1 each)
- PainPoints: PAIN-V21-004 status → "resolved"

---

### FASE 5: Síntesis en Neo4j

```powershell
cd tools\jtbd\scripts
python sync_to_neo4j.py --version 2.2
```

#### Query 1: Incremental Improvements (v2.2 vs v2.1)

```cypher
// tools/jtbd/neo4j-queries/improvements-v2.2.cypher
MATCH (j1:Job {version: '2.1'})-[:HAS_OUTCOME]->(o1:Outcome)
MATCH (j2:Job {version: '2.2'})-[:HAS_OUTCOME]->(o2:Outcome)
WHERE o1.id = o2.id AND o2.satisfaction > o1.satisfaction
RETURN
  o2.id AS outcome_id,
  o2.statement AS outcome,
  o1.satisfaction AS sat_v21,
  o2.satisfaction AS sat_v22,
  (o2.satisfaction - o1.satisfaction) AS improvement,
  o2.step AS step
ORDER BY improvement DESC
```

**Resultado**:

| Outcome ID | Outcome | Sat v2.1 | Sat v2.2 | Improvement | Step |
|------------|---------|----------|----------|-------------|------|
| OUT-V21-001 | Min time analyzing terms | 5 | 6 | **+1** | PRE |
| OUT-V21-002 | Max precision definitions | 7 | 8 | **+1** | Phase 0 |
| OUT-V21-003 | Min ambiguity in terms | 6 | 7 | **+1** | Execute |

**Insight**: 3 outcomes mejorados, todos relacionados a ISO (cookbook effect).

#### Query 2: Resolution Analysis

```cypher
// tools/jtbd/neo4j-queries/resolutions-v2.2.cypher
MATCH (p:PainPoint {version_resolved: '2.2'})
OPTIONAL MATCH (p)-[:RESOLVED_BY]->(f:Feature)
RETURN
  p.id AS pain_id,
  p.description AS description,
  p.severity AS severity,
  collect(f.name) AS resolved_by_features
```

**Resultado**:

| Pain ID | Description | Severity | Resolved By |
|---------|-------------|----------|-------------|
| PAIN-V21-004 | Hard to decide BT/NT vs subClassOf | Medium | [FEAT-DECISION-TREE, DOC-COOKBOOK] |

#### Query 3: Cumulative Improvements (2.0 → 2.2)

```cypher
// tools/jtbd/neo4j-queries/cumulative-improvements-2.0-to-2.2.cypher
MATCH (j0:Job {version: '2.0'})-[:HAS_OUTCOME]->(o0:Outcome)
MATCH (j2:Job {version: '2.2'})-[:HAS_OUTCOME]->(o2:Outcome)
WHERE o0.id = o2.id
RETURN
  o2.statement AS outcome,
  o0.satisfaction AS sat_v20,
  o2.satisfaction AS sat_v22,
  (o2.satisfaction - o0.satisfaction) AS total_improvement,
  CASE
    WHEN o2.satisfaction > o0.satisfaction THEN '⬆️ Improved'
    ELSE '➡️ No change'
  END AS status
ORDER BY total_improvement DESC
LIMIT 10
```

**Resultado**:

| Outcome | Sat v2.0 | Sat v2.2 | Improvement | Status |
|---------|----------|----------|-------------|--------|
| Max clarity of CQs | 4 | 6 | **+2** | ⬆️ Improved (v2.1) |
| Max coherence axioms | 5 | 6 | **+1** | ⬆️ Improved (v2.1) |
| Min complexity hierarchy | 4 | 5 | **+1** | ⬆️ Improved (v2.1) |
| [All ISO outcomes] | N/A | 6-8 | **New** | ✨ New (v2.1-2.2) |
| [Scoping outcomes] | 3 | 3 | **0** | ➡️ No change (need v2.4) |

**Insight**: Acumulativo desde v2.0, ISO branch (v2.1-2.2) mejora terminology, pero NO scoping.

---

### Checklist AOEM 2.2

```yaml
fase_1_visualizacion:
  - [x] Canvas Excalidraw creado (refinement focus)
  - [x] Diagramas Mermaid (decision tree, patterns)
  - [x] 4 PNGs exportados
  - [x] aoem-v2.2.excalidraw guardado

fase_2_analisis:
  - [x] Market definition (same as v2.1, emphasis on guidance)
  - [x] Job map (10 steps, same as v2.1)
  - [x] 54 outcomes (0 new, 3 updated satisfaction)
  - [x] 30 pain points (1 resolved: PAIN-V21-004)
  - [x] Top Opportunities: Still OUT-V20-001 (Opp=17)

fase_3_artefactos:
  - [x] job-aoem-2.2.md creado (with cookbook/decision tree)
  - [x] 0 archivos out-v2.2-*.md (no new outcomes)
  - [x] 3 archivos out-v2.1-*.md actualizados (sat +1)
  - [x] 1 archivo pain-v2.1-004.md actualizado (resolved)

fase_4_nocodb:
  - [x] Synced: 1 job, 54 outcomes (3 updated), 30 pains
  - [x] Updated: PAIN-V21-004 status → resolved
  - [x] View "AOEM 2.2 - Improvements" creada (shows +1 sat changes)

fase_5_neo4j:
  - [x] Nodos v2.2 creados
  - [x] Incremental improvements query (v2.2 vs v2.1)
  - [x] Resolution analysis query
  - [x] Cumulative improvements query (v2.0 → v2.2)

tiempo_invertido: "~10 horas (menos que v2.1, release pequeño)"
```

---

### Key Insights AOEM 2.2

1. **Release Type**: **Refinement** (no new features, only documentation)
   - Cookbook: 20 ISO 704 patterns
   - Decision tree: BT/NT vs subClassOf
   - Templates: Scope note patterns

2. **Mejoras incrementales**: 3 outcomes (+1 satisfaction each)
   - OUT-V21-001: Time analyzing terms (5→6)
   - OUT-V21-002: Precision definitions (7→8)
   - OUT-V21-003: Ambiguity reduction (6→7)

3. **Pain resuelto**: PAIN-V21-004 (BT/NT decision)
   - Impact reduction: 75%
   - Time saved: 2-3 days per project

4. **Top Opportunity sin cambio**: OUT-V20-001 (Scoping, Opp=17)
   - Documentation NO resuelve scoping
   - Need structural solution → RQF in v2.4

5. **Tiempo de proyecto**: 4-6 months (reduce 1 month vs v2.1)
   - Cookbook speeds up ISO analysis 20%
   - But quality improved, not speed (trade-off)

6. **Cumulative progress** (v2.0 → v2.2):
   - Term clarity: +2 satisfaction
   - Axiom coherence: +1 satisfaction
   - NEW: ISO branch (7 outcomes, 6-8 satisfaction)
   - Scoping: **0** progress (need different approach)

7. **Strategic insight**:
   - ISO branch (v2.1-2.2) optimized terminology
   - But scoping requires structural change (RQF in v2.4)
   - Next version (v2.3) adds SKOS for linked data

---

**✅ AOEM 2.2 completado.**

---
