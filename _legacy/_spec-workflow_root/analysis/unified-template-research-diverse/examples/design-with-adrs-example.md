# Ejemplo: design.md con ADRs, Guías y Templates

> **Concepto clave**: `design.md` es donde viven las decisiones de arquitectura,
> referencias a guías, y conexiones con artifact-templates.

---

## 📋 Formato spec-workflow-mcp Oficial

```markdown
# [Spec-Name] Design Document

## Overview
How this feature will be built, referencing approved requirements.

**Prerequisites:**
- [Requirements](./requirements.md) - Must be approved first

**Steering References:**
- [Tech Steering](../../../steering/tech.md)
- [Structure Steering](../../../steering/structure.md)

## Architecture

### Component Diagram
[Descripción de componentes]

### Data Flow
[Flujo de datos]

## ADRs (Architecture Decision Records)

### ADR-001: [Decision Title]
- **Status**: accepted | proposed | deprecated
- **Context**: Why this decision is needed
- **Decision**: What was decided
- **Consequences**: Positive and negative impacts
- **References**: Links to guides, external docs

## Implementation References

### Templates
- `artifact-templates/template-name.md` - For artifact X

### Guides
- `docs/guides/guide-name.md` - How to implement Y

### Patterns
- `task-patterns/pattern-name.md` - Reusable task pattern
```

---

## 🎯 Ejemplo Concreto: design.md para DAATH-ZEN-CONCEPTO

### `.spec-workflow/specs/daath-zen-concepto/design.md`

```markdown
# DAATH-ZEN-CONCEPTO Design Document

## Overview
Diseño del artefacto CONCEPTO para la metodología DAATH-ZEN.
Este documento define CÓMO se construye, basado en los requisitos aprobados.

**Prerequisites:**
- [Requirements](./requirements.md) ✓ Approved 2025-01-09

**Steering References:**
- [Tech Steering](../../../steering/tech.md) - Neo4j + Python stack
- [Structure Steering](../../../steering/structure.md) - Folder organization

---

## Architecture

### Artifact Structure
```
outputs/concepts/{concept-name}/
├── document.md      # Human-readable concept definition
├── metadata.yaml-ld # Linked Data metadata (JSON-LD compatible)
├── graph.cypher     # Neo4j graph representation
└── README.md        # Generated summary
```

### Data Flow
```
1. Input: Concept definition (natural language)
         ↓
2. Template Processing (microprompt)
         ↓
3. Outputs Generation:
   - document.md (Markdown)
   - metadata.yaml-ld (Structured data)
   - graph.cypher (Graph DB)
```

---

## ADRs (Architecture Decision Records)

### ADR-001: Triple Output Format
- **Status**: accepted
- **Context**: Necesitamos outputs que sean legibles por humanos,
  procesables por máquinas, y persistibles en grafo.
- **Decision**: Cada artefacto genera 3 formatos: Markdown, YAML-LD, Cypher.
- **Consequences**:
  - ✅ Trazabilidad completa
  - ✅ Integración con Neo4j
  - ⚠️ Mayor complejidad en templates
- **References**:
  - [docs/guides/triple-output-guide.md](../../docs/guides/triple-output-guide.md)

### ADR-002: YAML-LD over JSON-LD
- **Status**: accepted
- **Context**: JSON-LD es estándar pero verboso. YAML es más legible.
- **Decision**: Usar YAML con contexto @context para compatibilidad JSON-LD.
- **Consequences**:
  - ✅ Human-readable
  - ✅ Convertible a JSON-LD
  - ⚠️ Requiere conversión para algunas herramientas
- **References**:
  - [W3C JSON-LD Spec](https://www.w3.org/TR/json-ld/)

### ADR-003: Microprompt Architecture
- **Status**: accepted
- **Context**: Templates complejos necesitan ser configurables y composables.
- **Decision**: Usar microprompts que reciben configuración y generan outputs.
- **Consequences**:
  - ✅ Reutilización entre spec-types
  - ✅ Propagación de cambios centralizada
  - ⚠️ Learning curve inicial
- **References**:
  - [artifact-templates/README.md](../../artifact-templates/README.md)

---

## Implementation References

### Artifact Templates (Microprompts)
| Template | Propósito | Outputs |
|----------|-----------|---------|
| [daath-zen-concepto-tpl.md](../../artifact-templates/daath-zen-concepto-tpl.md) | Genera artefacto CONCEPTO | document.md, yaml-ld, cypher |
| [document-section-tpl.md](../../artifact-templates/document-section-tpl.md) | Genera sección de documento | markdown |
| [cypher-node-tpl.md](../../artifact-templates/cypher-node-tpl.md) | Genera nodos Cypher | cypher |

### Guides
| Guide | Cuándo Usar |
|-------|-------------|
| [triple-output-guide.md](../../docs/guides/triple-output-guide.md) | Implementar nuevo artefacto |
| [yaml-ld-guide.md](../../docs/guides/yaml-ld-guide.md) | Estructurar metadata |
| [neo4j-schema-guide.md](../../docs/guides/neo4j-schema-guide.md) | Definir schema de grafo |

### Task Patterns (Reusables)
| Pattern | Descripción |
|---------|-------------|
| [analyze-existing-pattern.md](../../task-patterns/analyze-existing-pattern.md) | Analizar artefactos existentes |
| [generate-outputs-pattern.md](../../task-patterns/generate-outputs-pattern.md) | Generar triple output |
| [validate-coherence-pattern.md](../../task-patterns/validate-coherence-pattern.md) | Validar contra ontología |

---

## Neo4j Schema

### Node Labels
```cypher
// Concepto node structure
(:Concepto {
  id: string,           // UUID
  name: string,         // Nombre del concepto
  definition: string,   // Definición breve
  source_spec: string,  // Spec que lo generó
  created_at: datetime,
  updated_at: datetime
})
```

### Relationships
```cypher
// Concepto relationships
(c1:Concepto)-[:RELATES_TO {type: string}]->(c2:Concepto)
(c:Concepto)-[:BELONGS_TO]->(m:Metodologia)
(c:Concepto)-[:GENERATED_BY]->(s:Spec)
```

---

## Validation Rules

| Rule ID | Descripción | Validator |
|---------|-------------|-----------|
| VAL-C01 | document.md tiene secciones requeridas | `validators/document-validator.py` |
| VAL-C02 | yaml-ld tiene @context válido | `validators/yaml-ld-validator.py` |
| VAL-C03 | cypher es sintácticamente correcto | `validators/cypher-validator.py` |
| VAL-C04 | IDs son únicos en el grafo | `validators/uniqueness-validator.py` |
```

---

## 🔑 Puntos Clave

### 1. ADRs viven en design.md
Los Architecture Decision Records documentan el "por qué" de las decisiones técnicas.

### 2. Referencias a Templates/Guides
El design.md es el "hub" que conecta con:
- `artifact-templates/` - Microprompts
- `docs/guides/` - Guías de implementación
- `task-patterns/` - Patrones reutilizables

### 3. Schema de Datos
Define estructuras (Neo4j, YAML-LD) que los templates usarán.

### 4. Validation Rules
Define reglas que los validators verificarán post-generación.

---

## ⚡ Beneficio de Esta Separación

| Antes | Después |
|-------|---------|
| tasks.md contenía el schema Neo4j | design.md#neo4j-schema |
| tasks.md contenía decisiones de arquitectura | design.md#adrs |
| tasks.md referenciaba guías inline | design.md#implementation-references |
| tasks.md tenía 1551 líneas | tasks.md tiene ~50 líneas + refs |

---

## 🎯 Arquitectura Correcta: .spec-workflow por App

> "Cada app/metodología tiene su propio `.spec-workflow/` con steering docs específicos"

### Estructura del Monorepo
```
aleia-melquisedec/                    # MONOREPO
├── .spec-workflow/                   # Specs de infraestructura global
│   └── steering/                     # Steering del MONOREPO
│
└── apps/
    └── {mi-metodologia}/
        └── .spec-workflow/           # Specs de ESTA app
            ├── steering/
            │   ├── product.md        # Visión de ESTA app
            │   ├── tech.md           # Stack de ESTA app
            │   └── structure.md      # Estructura de ESTA app
            ├── artifact-templates/
            ├── spec-types/
            └── specs/
```

### Beneficios
1. **Cada app es autónoma** - Su propio product/tech/structure
2. **Contexto específico** - El AI entiende ESTE producto
3. **Escalabilidad** - Nuevas apps no afectan a las existentes
4. **Independencia** - Cada equipo gestiona su spec-workflow
