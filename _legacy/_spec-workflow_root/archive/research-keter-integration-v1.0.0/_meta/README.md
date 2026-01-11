# Research App Integration v1.0.0

> 🎯 **Spec Purpose**: Establecer arquitectura multi-repositorio y evaluar integración de apps de investigación (caso: keter) en el ecosistema DAATH-ZEN MELQUISEDEC.

---

## 📊 Status

| Attribute | Value |
|-----------|-------|
| **Status** | 🟡 NOT STARTED |
| **Priority** | ⚡ HIGH (decisión arquitectónica fundamental) |
| **Version** | 1.0.0 |
| **Created** | 2026-01-08 |
| **Owner** | Architecture Team |
| **Type** | Strategic + Analysis |

---

## 🌐 Multi-Repository Context

**Repositories Affected**:
- 🏠 **Primary**: aleia-melquisedec (spec location, guidelines, ADRs)
- 🔗 **Secondary**: aleia-bereshit (keter analysis, potential changes)
- 🌱 **Future**: aleia-{nuevos-repos} (usarán guidelines creadas)

**Cross-Repo Tracking**: Implementación logs usarán tags `[REPO:nombre]` para claridad.

---

## 🎯 Core Question

> **"Como framework MELQUISEDEC, ¿cómo gestionamos aplicaciones de investigación como keter? ¿Dónde vive cada cosa?"**

### Sub-Questions
1. ¿Es keter (C:\proyectos\aleia-bereshit\apps\keter) candidato a package?
2. ¿Debería vivir en melquisedec o permanecer en bereshit?
3. ¿Qué criterios decisionales necesitamos para casos futuros?
4. ¿Cómo gestionamos specs multi-repositorio?
5. ¿Qué rol tiene apps/ en melquisedec si no contiene investigación real?

---

## 🧠 Pensamiento Complejo Aplicado

Este spec se generó usando análisis multinivel:

<details>
<summary><b>Ver Dimensiones Analizadas (12 niveles)</b></summary>

1. **Naturaleza de Apps**: ¿Framework vs Implementación?
2. **Framework/Consumidor**: Relación arquitectónica
3. **Paradoja apps/**: ¿Por qué existe si no debe tener investigaciones?
4. **Branches vs Repos**: Confusión conceptual resuelta
5. **Packages Architecture**: Niveles de abstracción
6. **Spec-Workflow Multi-Repo**: Gestión cruzada
7. **Análisis de Keter**: Sin acceso directo, proceso agnóstico
8. **Patrones de Decisión**: 4 criterios fundamentales
9. **Estructura del Spec**: 3 niveles (Analysis, Decision, Implementation)
10. **Nombrado del Spec**: "research-app-integration-v1.0.0"
11. **Propuesta Concreta**: Arquitectura de separación
12. **Síntesis Final**: Framework separado, implementaciones independientes

</details>

**Conclusión**: Separación clara framework/apps con guidelines reutilizables.

---

## 📦 Deliverables

### Architecture Decisions
- [ ] **ADR-002**: Multi-Repository Architecture Strategy
  - Location: `docs/architecture/ADR-002-multi-repo-strategy.md`
  - Defines: Framework vs Apps repos, package evolution path

### Guidelines & Templates
- [ ] **Component Placement Guidelines**: Decision tree + criteria
  - Location: `docs/guides/component-placement-guidelines.md`
  - Includes: Mermaid flowchart, examples, FAQ

- [ ] **New Research Repo Template**: Structure for new projects
  - Location: `docs/guides/new-research-repo-template.md`
  - Includes: pyproject.toml, pre-commit, GitHub Actions

- [ ] **Multi-Repo Spec Workflow**: Cross-repo management
  - Location: `docs/guides/multi-repo-spec-workflow.md`
  - Includes: Tracking conventions, examples

### Analysis & Decision
- [ ] **Keter Evaluation**: Structural + maturity analysis
  - Location: `Implementation Logs/analysis/keter-evaluation.md`
  - Includes: Scorecard, dependencies, recommendations

- [ ] **Keter Decision**: Final placement decision
  - Location: `Implementation Logs/analysis/keter-decision.md`
  - Options: Stay in bereshit / Package / Standalone / Toolkit

### Repository Updates
- [ ] **ARQUITECTURA_MONOREPO.md**: Add multi-repo strategy section
- [ ] **apps/ Clarification**: README or rename to examples/
- [ ] **CONTRIBUTING.md**: Add "Where to Contribute" section

---

## 🗺️ Phases

### Phase 1: Discovery 🔍
**Goal**: Understand keter and apply analysis framework
**Tasks**: 1.1-1.3 (Gather info, Analyze, Apply decision tree)
**Duration**: 1 session (~2h)

### Phase 2: Documentation 📐
**Goal**: Create architectural artifacts
**Tasks**: 2.1-2.4 (ADR, Guidelines, Template, Multi-repo workflow)
**Duration**: 1 session (~2.5h)

### Phase 3: Cleanup 🧹
**Goal**: Update melquisedec repo
**Tasks**: 3.1-3.2 (Clarify apps/, Update ARQUITECTURA)
**Duration**: 1 session (~1.5h)

### Phase 4: Finalization 🎯
**Goal**: Final decision and validation
**Tasks**: 4.1-4.3, 5.1-5.3 (Decision, Roadmap, Validation)
**Duration**: 1 session (~1.5h)

**Total Estimate**: 7.5 hours across 4 work sessions

---

## 🎯 Success Criteria

- ✅ **Criterio 1: Claridad Arquitectónica**
  - Cualquier dev decide dónde poner código nuevo en <5min
  - ADR-002 responde las 5 preguntas core

- ✅ **Criterio 2: Aplicabilidad**
  - Decision tree aplicado a keter → resultado claro
  - Template usado para crear mock repo

- ✅ **Criterio 3: Documentación**
  - 4 guidelines creadas + 1 análisis + 1 decisión
  - Todo referenciable y linkeable

- ✅ **Criterio 4: Meta-Compliance**
  - Este spec sigue sus propias guidelines multi-repo

---

## 🚀 Quick Start

### For User: Provide Keter Info
```powershell
# Navegar a keter
cd C:\proyectos\aleia-bereshit\apps\keter

# Obtener estructura
tree /F > keter-structure.txt
Get-Content keter-structure.txt

# Obtener dependencias
Get-Content requirements.txt  # o pyproject.toml

# Obtener descripción
Get-Content README.md  # o PROPOSITO.md
```

### For AI Agent: Start Implementation
1. Execute META-1: Setup folder structure
2. Execute TASK-1.1: Wait for user info
3. Execute TASK-1.2-1.3: Analyze keter
4. Proceed with documentation phases

---

## 📚 Related Documentation

- [ARQUITECTURA_MONOREPO.md](../../ARQUITECTURA_MONOREPO.md) - Current structure
- [bereshit-v3.0.0.md](../../docs/manifiesto/bereshit-v3.0.0.md) - DAATH-ZEN philosophy
- [spec-workflow README](../_spec-workflow-readme.md) - Spec methodology

---

## 📝 Key Decisions Made

<details>
<summary><b>Decision Log (updated as spec progresses)</b></summary>

### Decision 1: Multi-Repo Strategy
**Date**: 2026-01-08
**Decision**: Framework (melquisedec) y Apps (bereshit+) en repos separados
**Rationale**: [Pending ADR-002]
**Status**: 🟡 Proposed

### Decision 2: apps/ Purpose
**Date**: TBD
**Decision**: [Pending TASK-3.1]
**Options**: Rename to examples/ OR Keep with explicit README
**Status**: 🟡 Under Analysis

### Decision 3: Keter Placement
**Date**: TBD
**Decision**: [Pending TASK-4.1]
**Options**: A) Stay, B) Package, C) Standalone, D) Toolkit
**Status**: 🟡 Pending Analysis

</details>

---

## 🔗 Links

- [Requirements](requirements.md) - Detailed requirements (7 REQ-X)
- [Design](design.md) - Architecture & component design
- [Tasks](tasks.md) - Implementation task board
- [Implementation Logs](Implementation%20Logs/) - Session logs (cuando existan)

---

## 📊 Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Deliverables | 7 | 0 |
| Guidelines | 3 | 0 |
| Decisions | 3 | 0 (3 proposed) |
| Test Coverage | N/A (documentation spec) | - |
| Clarity Score | "Any dev decides in <5min" | TBD |

---

## 🏷️ Tags

`#architecture` `#multi-repo` `#decision-tree` `#keter` `#strategic` `#daath-zen` `#guidelines` `#adr`

---

## 🙏 Acknowledgments

Este spec fue generado usando **Sequential Thinking MCP** para análisis complejo multinivel, demostrando la capacidad de DAATH-ZEN para razonamiento arquitectónico profundo.

---

**Ready to Begin?** Execute TASK-1.1 para iniciar discovery phase. 🚀
