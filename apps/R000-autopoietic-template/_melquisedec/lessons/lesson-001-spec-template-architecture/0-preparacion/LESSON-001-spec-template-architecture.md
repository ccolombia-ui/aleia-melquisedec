# Lesson 001: Spec Template Architecture Design

## Metadata

| Campo | Valor |
|-------|-------|
| **Lesson ID** | LESSON-001 |
| **Date** | 2026-01-10 |
| **Context** | SPEC-001 strategy definition |
| **Related Specs** | SPEC-001 (built-template-spec-workflow) |
| **Confidence** | 0.85 (High - based on theoretical analysis) |
| **Status** | To be validated in implementation |
| **Category** | Architecture / Meta-design |

---

## 📚 What We Learned

### 1. Meta-Specifications Are Foundational
**Learning**: Before implementing features, we must specify **how to specify**.

**Evidence**: User pivoted from S001 (basic folder structure) to SPEC-001 (template infrastructure) because without proper templates, all future specs would have:
- Duplicated content
- Inconsistent structure
- Poor traceability
- Difficult version management

**Implication**: In autopoietic systems, **meta-infrastructure precedes infrastructure**.

**Principle Applied**: **P2 (Autopoiesis)** - System must be designed to evolve before it can evolve.

---

### 2. Workbooks as Single Source of Truth
**Learning**: Separating **content (workbooks)** from **presentation (spec artifacts)** enables evolution without breaking specs.

**Architecture**:
```
Workbook (evolves) → Template (adapts) → Spec (compiled view)
```

**Evidence**:
- Workbooks can be updated as system learns
- Multiple specs can reference same workbook products
- Compilation ensures specs always reflect latest knowledge
- Obsidian provides natural editing environment

**Implication**: **Never write requirements.md directly**—write workbooks, compile to specs.

**Principle Applied**: **P9 (Inmutabilidad)** - Compiled specs are snapshots, workbooks are living documents.

---

### 3. RBM Integration Requires Structural Support
**Learning**: Results-Based Management (RBM) hierarchy must be **encoded in folder structure**, not just documentation.

**Structure**:
```
wb-rbm-spec/
├── resultado_final.md           # Final Result
├── ri-001-feature/              # Intermediate Result
│   ├── ri-feature.md
│   └── rinm-producto/           # Immediate Results
│       ├── REQ-001-story.md     # Product
│       ├── REQ-002-rule.md      # Product
│       └── REQ-003-contract.md  # Product
```

**Benefits**:
1. **Traceability**: File path encodes result hierarchy
2. **Metrics**: Each level has measurable outputs
3. **Navigation**: Obsidian graph shows causal chains
4. **Validation**: Scripts can verify coherence matrix

**Implication**: RBM is not just a "framework to apply"—it's an **architectural pattern**.

**Principle Applied**: **P7 (Recursión Fractal)** - Structure repeats at every scale.

---

### 4. Template Inheritance Reduces Duplication
**Learning**: Common elements (headers, metadata, protocols) should be **inherited**, not duplicated.

**Pattern**:
```yaml
template_hierarchy:
  base: daath-zen-base.md        # HKM + Dublin Core
  variants:
    requirements:
      extends: base
      sections: [overview, stories, functional]
    design:
      extends: base
      sections: [architecture, decisions, adr]
```

**Evidence**:
- If HKM header format changes, update only base template
- Version propagates automatically
- Consistency guaranteed
- DRY principle (Don't Repeat Yourself)

**Implication**: Use **config.yaml-ld** to define inheritance hierarchy.

**Principle Applied**: **P1 (Síntesis)** - Orchestrate, don't duplicate.

---

### 5. Keter-Doc Protocol Enables Semantic Interoperability
**Learning**: Using **JSON-LD** for document metadata enables:
1. Explicit semantics
2. Graph database ingestion
3. Cross-project linking
4. AI reasoning about relationships

**Example**:
```yaml
# issue.yaml-ld
"@context":
  "@vocab": "http://melquisedec.org/ontology#"
  dc: "http://purl.org/dc/terms/"

"@type": "ResearchIssue"
"@id": "urn:melquisedec:issue:spec-001"
dc:title: "Build daath-zen templates"
dc:created: "2026-01-10"
implementsPrinciple:
  - "@id": "urn:melquisedec:principle:P1"
  - "@id": "urn:melquisedec:principle:P2"
```

**Implication**: Every document must have **@context**, **@type**, **@id**.

**Principle Applied**: **P6 (Triple Persistence)** - Semantic graph layer.

---

### 6. Granularity Decision: Product = REQ-XXX
**Learning**: REQ-XXX should map to **Immediate Results (Products)**, not Intermediate Results (Features).

**Reasoning**:
- **Too coarse** (REQ-001 = entire authentication): Loses traceability
- **Too fine** (REQ-001-01-a-1 = one line of code): Unmanageable
- **Just right** (REQ-001-01 = user story "login with email"): Testable, traceable, measurable

**Numbering Scheme**:
```
REQ-RI-Rinm
REQ-001-01  = Intermediate Result 001, Immediate Result 01
REQ-001-02  = Intermediate Result 001, Immediate Result 02
REQ-002-01  = Intermediate Result 002, Immediate Result 01
```

**Implication**: Each REQ maps to one **measurable product** with clear success criteria.

**Principle Applied**: **P5 (Checkpoints)** - Validate at product level.

---

### 7. Hybrid Approach: Modular Content, Monolithic Artifacts
**Learning**: spec-workflow-mcp expects **single files** (requirements.md), but we need **modular content** (workbooks).

**Solution**: **Compilation step**
```
Workbook (modular) → compile_spec_from_workbook.py → Spec (monolithic)
```

**Process**:
1. User edits workbook in Obsidian
2. AI runs compilation script
3. Script processes transclusions `![[]]`
4. Generates requirements.md with coherence matrix
5. Validates against keter-doc protocol
6. Submits to spec-workflow-mcp

**Benefits**:
- Best of both worlds
- spec-workflow-mcp compatibility
- Workbook flexibility
- Automated consistency

**Implication**: Need **compile_spec_from_workbook.py** in SPEC-001.

**Principle Applied**: **P1 (Síntesis)** - Orchestrate existing tools.

---

### 8. Investigation Before Implementation
**Learning**: SPEC-001 requires **research phase** before writing requirements.

**Tasks to Research**:
1. Current spec-workflow-mcp format (what's mandatory?)
2. Keter-doc protocol design (JSON-LD schema)
3. Transclusion support (native or compiled?)
4. REQ-XXX numbering (how deep to nest?)
5. Obsidian compatibility (Neo4j sync strategy)

**Reasoning**:
- Can't design templates without understanding constraints
- Can't design protocol without studying ontologies
- Can't decide monolithic vs modular without testing tools

**Implication**: SPEC-001 has **Phase 0: Investigation** before Requirements.

**Principle Applied**: **P3 (Issue-Driven)** - Every investigation is an issue.

---

### 9. Coherence Matrix Must Be Computable
**Learning**: RBM coherence matrix should be **data**, not just narrative.

**Format**:
```yaml
# coherence-matrix.yaml
result_chain:
  - id: RF-001
    title: "Secure authentication system"
    intermediate_results:
      - id: RI-001
        title: "Login feature"
        immediate_results:
          - id: REQ-001-01
            title: "User story: login with email"
            metrics:
              - success_rate: ">95%"
              - response_time: "<500ms"
```

**Benefits**:
- Machine-readable
- Validation scripts
- Automatic diagram generation
- Neo4j ingestion

**Implication**: Templates include **coherence-matrix.yaml** section.

**Principle Applied**: **P6 (Triple Persistence)** - Structured data for graph.

---

### 10. Autopoiesis Requires Feedback Loops
**Learning**: System learns by **comparing design intent (workbook) with implementation reality (logs)**.

**Loop**:
```
1. Design in workbook (prediction)
2. Implement from tasks
3. Log actual results
4. Compare prediction vs reality
5. Update workbook with lessons
6. Increase confidence score
7. Propagate to other workbooks
```

**Example**:
- Workbook predicted: "Login API < 500ms"
- Implementation log: "Actual: 350ms avg"
- Lesson: "Prediction accurate, increase confidence 0.75 → 0.85"
- Propagate: Update related authentication workbooks

**Implication**: Need **compare_prediction_vs_reality.py** script.

**Principle Applied**: **P2 (Autopoiesis)** - System improves itself.

---

## 🎯 Patterns Discovered

### Pattern 1: Template-Workbook-Spec Triangle
```
   Template (structure)
      /  \
     /    \
Workbook  Spec
(content) (view)
```

- **Template**: Defines structure and inheritance
- **Workbook**: Contains evolving content
- **Spec**: Compiled snapshot for spec-workflow-mcp

### Pattern 2: Meta-Spec Before Feature-Spec
```
SPEC-001 (meta)  →  SPEC-002+ (features)
```

Build infrastructure for specifying before specifying features.

### Pattern 3: Compile-Validate-Submit
```
1. Edit workbook (manual)
2. Compile to spec (automatic)
3. Validate coherence (automatic)
4. Submit to dashboard (automatic)
5. Approve (manual)
```

Automation between manual steps.

### Pattern 4: RBM as File System
```
Folder structure = Results hierarchy
File name = Product ID
Content = Product specification
```

### Pattern 5: JSON-LD Everywhere
```
Every YAML → Add @context, @type, @id
```

Enables semantic web compatibility.

---

## 🚀 Recommended Actions

### Immediate (SPEC-001 Phase 0)
1. ✅ Create workbook `wb-rbm-spec-001/`
2. ⏳ Research current spec-workflow-mcp format
3. ⏳ Design keter-doc protocol (JSON-LD schema)
4. ⏳ Test Obsidian transclusions → Neo4j

### Short-term (SPEC-001 Implementation)
1. ⏳ Create base template `daath-zen-base.md`
2. ⏳ Create variant templates (requirements, design, tasks, steering)
3. ⏳ Implement `compile_spec_from_workbook.py`
4. ⏳ Implement coherence validators

### Long-term (Post-SPEC-001)
1. ⏳ Create SPEC-002 using SPEC-001 templates (validation)
2. ⏳ Implement autopoietic feedback loop
3. ⏳ Build confidence scoring system
4. ⏳ Create template recommendation engine

---

## 🔄 Evolution Strategy

### Version 1.0 (SPEC-001)
- Basic template inheritance
- Manual compilation
- Simple coherence validation

### Version 1.1 (After 3 specs)
- Automated compilation on file save
- Enhanced coherence matrix
- Pattern extraction from lessons

### Version 2.0 (After 10 specs)
- AI-suggested templates
- Confidence-based recommendations
- Self-updating workbooks

---

## ⚠️ Risks and Mitigations

### Risk 1: Over-Engineering
**Risk**: Templates too complex, users avoid them.
**Mitigation**: Start minimal, add features based on actual pain points.

### Risk 2: spec-workflow-mcp Incompatibility
**Risk**: Compiled specs don't work with dashboard.
**Mitigation**: Test compilation early, validate against tool's parser.

### Risk 3: Obsidian Lock-in
**Risk**: System only works with Obsidian.
**Mitigation**: Use standard Markdown, links as `[text](path)` fallback.

### Risk 4: Complexity Creep
**Risk**: Each spec adds new template features, system becomes unmaintainable.
**Mitigation**: Strict governance via config.yaml-ld versioning.

---

## 📊 Success Metrics

### Template Quality
- [ ] All 6 templates inherit from base
- [ ] No duplicated content across templates
- [ ] Version changes propagate in < 5 minutes

### Workbook Usability
- [ ] New spec workbook created in < 30 minutes
- [ ] Compilation succeeds on first try > 80%
- [ ] Coherence validation catches errors > 90%

### Autopoiesis Effectiveness
- [ ] Lessons captured after every spec
- [ ] Confidence scores increase over time
- [ ] Templates evolve based on lessons

---

## 🔗 Related Documents

- [CHATLOG-2026-01-10_125024-spec-001-strategy.md](../logs/CHATLOG-2026-01-10_125024-spec-001-strategy.md)
- [raw-manifiesto-melquisedec.md](../manifest/1-inputs/raw-manifiesto-melquisedec.md)
- SPEC-001 (to be created)

---

## 💡 Key Takeaway

> **"Don't specify features before you specify how to specify."**

SPEC-001 is not about building a system—it's about building the **language and grammar** for describing systems. Once that meta-layer exists, all future specs become:
- More consistent
- Less duplicated
- More traceable
- More evolvable

This is **linguistic architecture**: defining the vocabulary before writing the story.

---

**Lesson Extracted By**: GitHub Copilot (Claude Sonnet 4.5)
**Confidence**: 0.85 (High - based on theoretical analysis, to be validated)
**Next Validation**: After SPEC-001 implementation
**Status**: Active Learning
