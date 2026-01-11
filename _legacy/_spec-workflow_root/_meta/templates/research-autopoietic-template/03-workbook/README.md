# 03-workbook/ - SALOMON (Análisis y Diseño)

Esta carpeta contiene análisis, diseños y decisiones arquitectónicas.

## Estructura

```
03-workbook/
├── analysis/                # Análisis comparativos, evaluaciones
│   └── comparative-analysis.md
├── design/                  # Arquitecturas, modelos, diagramas
│   └── architecture.md
├── decisions/               # ADRs (Architecture Decision Records)
│   ├── ADR-001-*.md
│   └── ADR-002-*.md
└── validation/              # Validaciones de diseño
    └── design-validation.md
```

## Rostro DAATH-ZEN

**SALOMON** (Análisis): Analiza alternativas, diseña arquitectura, documenta decisiones.

## Checkpoint

**CK-03**: Validar que el diseño está completo y validado antes de implementar.

## HKM Type

Todos los archivos en esta carpeta deben tener `hkm_type: workbook` (análisis y diseño).

## Criterios de Validación

- [ ] Análisis comparativo completo
- [ ] Arquitectura con ≥3 diagramas
- [ ] [N] ADRs documentados
- [ ] Design validation pasa
- [ ] Diseño alineado con requirements

## 3.1. Analysis/

### comparative-analysis.md

```markdown
---
hkm_type: workbook
epistemic_level: workbook
title: "Comparative Analysis - [TEMA]"
created: YYYY-MM-DD
tags: [analysis, comparison, salomon]
synthesis_from:
  - ../02-atomics/combination/*.md
---

## 1. Objetivo del Análisis

[Qué alternativas se comparan y por qué]

## 2. Criterios de Evaluación

| Criterio | Peso | Justificación |
|----------|------|---------------|
| Performance | 30% | [Razón] |
| Mantenibilidad | 25% | [Razón] |
| Complejidad | 20% | [Razón] |
| Costos | 15% | [Razón] |
| Comunidad | 10% | [Razón] |

## 3. Alternativas Analizadas

### Alternativa A
- **Pros**: [Lista]
- **Cons**: [Lista]
- **Score**: [X/10]

### Alternativa B
- **Pros**: [Lista]
- **Cons**: [Lista]
- **Score**: [Y/10]

## 4. Matriz de Decisión

[Tabla comparativa con scores por criterio]

## 5. Recomendación

[Alternativa elegida con justificación basada en evidencia]
```

## 3.2. Design/

### architecture.md

```markdown
---
hkm_type: workbook
epistemic_level: workbook
title: "Architecture - [TÍTULO]"
created: YYYY-MM-DD
tags: [architecture, design, salomon]
synthesis_from:
  - ../03-workbook/analysis/*.md
  - ../02-atomics/combination/*.md
---

## 1. Arquitectura Conceptual

```mermaid
graph TD
    [Diagrama C4 Level 1 - Context]
```

## 2. Componentes Principales

### Componente A
- **Responsabilidad**: [Descripción]
- **Interfaces**: [Lista]
- **Tecnologías**: [Lista]

## 3. Diagramas

### C4 Level 2 - Container
```mermaid
[Diagrama de containers]
```

### C4 Level 3 - Component
```mermaid
[Diagrama de componentes internos]
```

### Secuencia
```mermaid
sequenceDiagram
    [Flujo de interacciones]
```

## 4. Patrones Aplicados

- **Patrón 1**: [Descripción y justificación]
- **Patrón 2**: [Descripción y justificación]

## 5. Consideraciones de Implementación

[Guías para implementadores]
```

## 3.3. Decisions/

### ADR Template

```markdown
---
hkm_type: workbook
epistemic_level: workbook
title: "ADR-XXX: [TÍTULO_DECISIÓN]"
created: YYYY-MM-DD
status: proposed | accepted | deprecated | superseded
tags: [adr, decision, salomon]
---

# ADR-XXX: [TÍTULO_DECISIÓN]

## Status

[Proposed | Accepted | Deprecated | Superseded by ADR-YYY]

## Context

[Qué problema/situación motivó esta decisión]

## Decision

[Decisión tomada - debe ser específica y clara]

## Consequences

### Positive
- [Consecuencia positiva 1]
- [Consecuencia positiva 2]

### Negative
- [Consecuencia negativa 1]
- [Trade-off aceptado]

## Alternatives Considered

### Alternativa A
- **Pros**: [Lista]
- **Cons**: [Lista]
- **Razón de descarte**: [Explicación]

### Alternativa B
- **Pros**: [Lista]
- **Cons**: [Lista]
- **Razón de descarte**: [Explicación]

## References

- [Link a análisis comparativo]
- [Link a documentación técnica]
```

## 3.4. Validation/

### design-validation.md

```markdown
---
hkm_type: workbook
epistemic_level: workbook
title: "Design Validation - [TÍTULO]"
created: YYYY-MM-DD
tags: [validation, design, salomon]
---

## 1. Checklist de Validación

### Completitud
- [ ] Arquitectura documentada con diagramas
- [ ] Componentes principales identificados
- [ ] Interfaces definidas
- [ ] ADRs documentando decisiones críticas

### Alineación con Requirements
- [ ] Diseño resuelve problem statement
- [ ] Success criteria alcanzables con arquitectura
- [ ] Constraints respetados

### Implementabilidad
- [ ] Tecnologías disponibles
- [ ] Recursos suficientes
- [ ] Timeline realista

## 2. Riesgos Identificados

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|----|--------|--------------|---------|------------|
| R-01 | [Riesgo] | Alta | Alto | [Estrategia] |

## 3. Aprobación

**Revisor**: [Nombre]
**Fecha**: [YYYY-MM-DD]
**Status**: ✅ Aprobado | ⚠️ Needs Revision | ❌ Rechazado
```

## MCPs Recomendados

- **sequential-thinking**: Análisis paso a paso estructurado
- **reasoning-branches**: Explorar alternativas de diseño en paralelo
- **filesystem**: Leer/escribir archivos
- **memory**: Mantener contexto de análisis

## Workflow con Sequential Thinking

```python
# Ejemplo de análisis estructurado con sequential-thinking
{
  "thought": "Comparando LlamaIndex vs LangChain para Neo4j...",
  "thoughtNumber": 1,
  "totalThoughts": 5,
  "nextThoughtNeeded": true
}
```

## Workflow con Reasoning Branches

Usar cuando necesites explorar múltiples diseños arquitectónicos:

```yaml
# Branch principal: Hexagonal Architecture
# Branch alt-stack: Alternativa con stack diferente
# Branch alt-method: Alternativa metodológica

# Al final: Merge mejor alternativa a main
```

---

**Ver**: [requirements.md](../requirements.md) § 3.2, [tasks.md](../tasks.md) § PHASE 3, [design.md](../design.md) § 3-5
