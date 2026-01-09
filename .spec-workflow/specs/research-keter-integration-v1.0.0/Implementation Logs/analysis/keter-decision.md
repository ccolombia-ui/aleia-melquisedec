# Keter Decision: ComponentClassifier Decision Tree Analysis
**TASK-1.3** | **Sprint 1: Discovery & Analysis**
**Date**: 2026-01-08
**Analyst Model**: Claude Opus 4.5
**Input**: [keter-evaluation.md](keter-evaluation.md)
**Algorithm Source**: [design.md](../../design.md) - ComponentClassifier

---

## 1. Decision Tree Execution

### Algorithm Reference
```python
class ComponentClassifier:
    def classify(self, component: Component) -> Placement:
        # Nivel 1: Propósito
        if component.is_methodology_or_tooling():
            return Placement.PACKAGES_MELQUISEDEC

        # Nivel 2: Reusabilidad
        if component.is_reusable_library():
            return self.evaluate_reusability(component)

        # Nivel 3: Independencia
        if component.has_independent_lifecycle():
            return Placement.SEPARATE_PACKAGE

        # Nivel 4: Naturaleza
        if component.is_research_or_application():
            return Placement.ORIGIN_REPO

        return Placement.ORIGIN_REPO  # Default
```

---

## 2. Step-by-Step Traversal

### 🌳 LEVEL 1: Purpose Analysis

**Question**: Is Keter methodology or tooling for the framework itself?

**Evaluation**:
```
Keter Purpose: "Policy Engine & Backend Unificado para ALEIA-BERESHIT"

Is this methodology/tooling?
├─ Methodology: NO
│  └─ Keter no es una guía de proceso, es implementación
│
├─ Framework Tooling: PARTIAL
│  └─ MCP Server pattern = tooling
│  └─ Policy Engine pattern = tooling
│  └─ BUT: Backend Unificado = application code
│
└─ CONCLUSION: MIXED - Contains both tooling AND application
```

**Result**: `is_methodology_or_tooling() = PARTIAL`

**Decision**: Cannot return early. Must continue to Level 2.

---

### 🌳 LEVEL 2: Reusability Analysis

**Question**: Is Keter a reusable library without significant modification?

**Evaluation**:
```
Reusability Assessment:

Can Keter be used as-is in another project?
├─ Full Component: NO
│  ├─ Hard-coded references to DAATH, YESOD, AYIN
│  ├─ Supabase schemas with specific names (keter_core, ayin_config)
│  ├─ L0 product templates specific to ALEIA domain
│  └─ Tenant model tied to ALEIA business logic
│
├─ Subsystems: VARIES
│  ├─ Policy Engine core: YES (with abstraction)
│  │   └─ Interfaces are clean: IPolicyEngine, IValidator
│  │   └─ Mock implementations show pluggability
│  │
│  ├─ MCP Server: YES (as template)
│  │   └─ Tool pattern is generic
│  │   └─ Handler pattern is reusable
│  │   └─ Would need domain-specific tools removed
│  │
│  ├─ Multi-tenant Backend: NO
│  │   └─ Too tied to Supabase + ALEIA schemas
│  │   └─ RLS policies are specific
│  │
│  └─ Frontend (Next.js): NO
│      └─ Specific to ALEIA use cases
│      └─ Domain pages (concepto, estandares, ontologia)

Overall Reusability Score: 6/10 (from evaluation)
```

**Result**: `is_reusable_library() = PARTIAL (subsystems only)`

**Decision**: Branch to `evaluate_reusability(component)`

---

### 🌿 BRANCH: Evaluate Reusability

```python
def evaluate_reusability(self, component: Component) -> Placement:
    if component.reusability_score >= 8:
        return Placement.PACKAGES_MELQUISEDEC
    elif component.reusability_score >= 5:
        return self.evaluate_extraction_value(component)
    else:
        return Placement.ORIGIN_REPO
```

**Keter Reusability Score**: 6/10

**Decision**: `score >= 5` → Continue to `evaluate_extraction_value(component)`

---

### 🌿 BRANCH: Evaluate Extraction Value

**Question**: What value would extraction provide vs. cost?

**Evaluation Matrix**:
| Subsystem | Extraction Value | Extraction Cost | ROI |
|-----------|-----------------|-----------------|-----|
| Policy Engine Pattern | High | Medium | **Positive** |
| MCP Server Template | High | Low | **Very Positive** |
| Multi-tenant Pattern | Medium | High | Negative |
| Frontend Pages | Low | Low | Neutral |
| 15+ Services (full) | Low | Very High | **Very Negative** |

**Value Assessment**:
```
High Value Extractions:
┌─────────────────────────────────────────────────────────┐
│  @melquisedec/policy-engine                             │
│  ─────────────────────────────────────────────────────  │
│  - Generic policy evaluation pattern                    │
│  - Conflict detection abstraction                       │
│  - Deprecation management pattern                       │
│  - Version control pattern                              │
│  ─────────────────────────────────────────────────────  │
│  VALUE: Enables policy systems in any research project  │
│  COST: ~2-3 days to abstract from keter specifics       │
│  ROI: ★★★★☆ (4/5)                                       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  @melquisedec/mcp-server-template                       │
│  ─────────────────────────────────────────────────────  │
│  - MCP server skeleton                                  │
│  - Tool registration pattern                            │
│  - Handler architecture                                 │
│  - Cache management pattern                             │
│  ─────────────────────────────────────────────────────  │
│  VALUE: Quick MCP server creation for new projects      │
│  COST: ~1-2 days to extract as template                 │
│  ROI: ★★★★★ (5/5)                                       │
└─────────────────────────────────────────────────────────┘
```

**Result**: `extraction_value = HIGH (for subsystems)`

---

### 🌳 LEVEL 3: Independence Analysis

**Question**: Does Keter have an independent lifecycle?

**Evaluation**:
```
Lifecycle Analysis:

Can Keter be versioned/released independently?
├─ Currently: NO
│  └─ Part of aleia-bereshit monorepo
│  └─ Version tied to workspace (1.0.0)
│  └─ No independent npm publish
│
├─ Could it be independent?
│  ├─ Policy Engine core: YES
│  │   └─ Has own test suite (131 tests)
│  │   └─ Has own interfaces
│  │   └─ Could version separately
│  │
│  └─ Full Keter: DIFFICULT
│      └─ Migrations tied to bereshit
│      └─ Seed data is bereshit-specific
│      └─ Would require major refactoring

Independence Score: 4/10 (from evaluation)
```

**Result**: `has_independent_lifecycle() = PARTIAL`

**Decision**: Cannot cleanly extract full component. Continue to Level 4.

---

### 🌳 LEVEL 4: Nature Analysis

**Question**: Is Keter research/experimentation or production application?

**Evaluation**:
```
Nature Assessment:

Research/Experimentation Indicators:
├─ ✅ Part of ALEIA research ecosystem
├─ ✅ Experimental integrations (Blockchain, Neo4j)
├─ ✅ Evolving architecture (multiple guides suggest iteration)

Production Application Indicators:
├─ ✅ High test coverage (92.94%)
├─ ✅ SonarQube certified (production quality)
├─ ✅ Multi-tenant production features
├─ ✅ Real L0 products (87 templates)
├─ ✅ Real users implied (5 tenants in seed)

CONCLUSION: PRODUCTION APPLICATION with research heritage
```

**Result**: `is_research_or_application() = APPLICATION`

**Final Decision Point**: Since it's a production application...

```python
if component.is_application():
    return Placement.ORIGIN_REPO  # Stay in bereshit
```

---

## 3. Decision Tree Result

```
┌─────────────────────────────────────────────────────────────────┐
│                    DECISION TREE RESULT                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FULL KETER COMPONENT:                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Placement: ORIGIN_REPO (aleia-bereshit)                 │   │
│  │  Confidence: 95%                                          │   │
│  │  Rationale: Production app, low independence, ecosystem   │   │
│  │             coupling prevents clean extraction            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  EXTRACTABLE SUBSYSTEMS:                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Policy Engine Pattern → PACKAGES_MELQUISEDEC            │   │
│  │  Confidence: 80%                                          │   │
│  │  As: @melquisedec/policy-engine                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  MCP Server Template → TEMPLATES_MELQUISEDEC             │   │
│  │  Confidence: 90%                                          │   │
│  │  As: _templates/mcp-server-template/                     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Formal PlacementDecision Records

### 4.1 Full Keter Component

```yaml
PlacementDecision:
  component:
    name: "@aleia/keter"
    location: "aleia-bereshit/apps/keter"
    purpose: "Policy Engine & Backend Unificado"
    maturity_level: STABLE
    reusability_score: 6
    is_framework_core: false

  recommended_placement: ORIGIN_REPO
  confidence: 0.95

  rationale: |
    Keter es una aplicación de producción con integración profunda al
    ecosistema ALEIA-BERESHIT (DAATH, YESOD, AYIN). Su arquitectura
    multi-tenant, esquemas Supabase específicos, y dependencias de
    negocio impiden una extracción limpia. Mantenerlo en su repo de
    origen preserva la coherencia del ecosistema.

  action_items:
    - Document keter architecture in melquisedec ADR-002
    - Create case study in docs/manifiesto/05-casos-estudio/
    - Reference keter as implementation example of patterns
```

### 4.2 Policy Engine Extraction

```yaml
PlacementDecision:
  component:
    name: "Policy Engine Pattern"
    location: "aleia-bereshit/apps/keter/packages/keter/core/services/"
    purpose: "Generic policy evaluation and lifecycle management"
    maturity_level: STABLE
    reusability_score: 8
    is_framework_core: true  # Could be framework utility

  recommended_placement: PACKAGES_MELQUISEDEC
  confidence: 0.80

  rationale: |
    El patrón de Policy Engine es genérico y valioso. Las interfaces
    (IPolicyEngine, IValidator) y servicios core (PolicyEngine,
    ConflictDetector, DeprecationEngine, VersionManager) pueden
    abstraerse del contexto ALEIA para crear un package reusable.

  action_items:
    - Create packages/policy-engine/ in melquisedec
    - Extract abstract interfaces from keter
    - Implement generic version without ALEIA specifics
    - Add tests based on keter's test patterns
    - Document as REF-keter in package README
```

### 4.3 MCP Server Template

```yaml
PlacementDecision:
  component:
    name: "MCP Server Template"
    location: "aleia-bereshit/apps/keter/packages/keter/mcp/"
    purpose: "Template for creating MCP servers with common patterns"
    maturity_level: STABLE
    reusability_score: 9
    is_framework_core: true  # DAATH-ZEN tooling

  recommended_placement: TEMPLATES_MELQUISEDEC
  confidence: 0.90

  rationale: |
    El patrón MCP Server de keter es un excelente template. Con 20+
    tools implementados, handlers de validez, y cache management,
    provee una base sólida para nuevos MCP servers. La extracción
    como template tiene bajo costo y alto valor.

  action_items:
    - Create _templates/mcp-server-template/ in melquisedec
    - Extract server skeleton from keter
    - Include: tool registration, handlers, cache patterns
    - Remove domain-specific tools (decree-*, policy-*)
    - Add placeholder tools as examples
    - Document setup and customization
```

---

## 5. ADR-002 Input Summary

### Decision Summary for ADR

**QUESTION**: Should Keter move to melquisedec?

**ANSWER**: NO for full component, YES for patterns

**DECISION OPTIONS EVALUATED**:

| Option | Description | Verdict |
|--------|-------------|---------|
| A | Keep entirely in bereshit | ✅ **SELECTED** (full component) |
| B | Extract to melquisedec package | ✅ **SELECTED** (subsystems only) |
| C | Create separate repo | ❌ REJECTED |
| D | Integrate into daath-toolkit | ❌ REJECTED |

**RATIONALE**:

1. **Keter Full Component** → Option A (stay in bereshit)
   - Production application with ecosystem dependencies
   - Score 6.50/10 = zona gris, pero análisis detallado indica permanencia
   - Independence score 4/10 es muy bajo para migración

2. **Policy Engine Pattern** → Option B (extract to packages/)
   - Reusability score 8/10 para subsistema específico
   - Interfaces limpias permiten abstracción
   - Valor para otros proyectos de investigación

3. **MCP Server Template** → Option B (extract to _templates/)
   - Reusability score 9/10 como template
   - Bajo costo de extracción
   - Alto valor como acelerador de desarrollo

---

## 6. Confidence Analysis

### Overall Confidence: 88%

**Confidence Breakdown**:
```
Full Keter → ORIGIN_REPO:       95% ████████████████████░░░░
Policy Engine → PACKAGES:        80% ████████████████░░░░░░░░
MCP Template → TEMPLATES:        90% ██████████████████░░░░░░

Weighted Average: (0.95×50%) + (0.80×25%) + (0.90×25%) = 88%
```

**Uncertainty Sources**:
- Policy Engine extraction complexity (might need more abstraction)
- MCP template scope (how much domain logic to strip)
- Future keter evolution (might become more/less coupled)

---

## 7. Dissenting Views

### Alternative: Full Extraction to Separate Repo

**Argument**: Keter is mature enough (92.94% coverage) to be its own package in a separate repo.

**Counter-Arguments**:
- ❌ Would orphan it from ALEIA ecosystem support
- ❌ Breaks DAATH validation pipeline
- ❌ Requires duplicating Supabase infrastructure docs
- ❌ No clear user base outside ALEIA

**Verdict**: REJECTED - benefits don't outweigh costs

### Alternative: Full Integration into daath-toolkit

**Argument**: Policy engine could be part of daath-toolkit validators.

**Counter-Arguments**:
- ❌ daath-toolkit is Python, keter is TypeScript
- ❌ Different architectural paradigms
- ❌ Would bloat daath-toolkit with foreign concerns

**Verdict**: REJECTED - language mismatch alone disqualifies

---

## 8. Final Recommendation

### Decision Matrix

| Component | Placement | Confidence | Priority |
|-----------|-----------|------------|----------|
| **Keter (full)** | aleia-bereshit (no change) | 95% | N/A |
| **Policy Engine Pattern** | packages/policy-engine | 80% | P1 |
| **MCP Server Template** | _templates/mcp-server-template | 90% | P1 |
| **Multi-tenant Pattern** | docs/architecture/ADR-* (doc only) | 85% | P2 |
| **Keter Case Study** | docs/manifiesto/05-casos-estudio | 90% | P2 |

### Execution Sequence (Sprint 2 Preview)

```
TASK-2.1: Draft ADR-002 with decision
TASK-2.2: Document extraction plan for Policy Engine
TASK-2.3: Document extraction plan for MCP Template
TASK-2.4: Update case studies with keter reference
```

---

## 9. Conclusion

**The ComponentClassifier Decision Tree has been fully executed.**

### Key Findings:

1. **Keter is a production application** that should remain in its origin repository (aleia-bereshit) to preserve ecosystem coherence.

2. **Two high-value subsystems** are candidates for extraction:
   - Policy Engine Pattern → `@melquisedec/policy-engine`
   - MCP Server Pattern → `_templates/mcp-server-template/`

3. **The hybrid approach** (keep origin, extract patterns) maximizes value while minimizing risk.

4. **Confidence level of 88%** indicates high certainty in the recommendation.

---

**End of Decision Analysis**
**Status**: ✅ TASK-1.3 Complete
**Model**: Claude Opus 4.5
**Duration**: ~25 minutes

**Next**: Sprint 2 - Documentation (TASK-2.1: Draft ADR-002)
