# ADR 002: Decisión de Integración de Keter

**Estado**: Aceptado
**Fecha**: 2026-01-08
**Autores**: Equipo MELQUISEDEC
**Relacionado con**: research-keter-integration-v1.0.0

---

## Contexto

Keter (`@aleia/keter`) es un componente maduro dentro del ecosistema ALEIA-BERESHIT que implementa:
- Policy Engine declarativo con evaluación de reglas
- Backend Multi-Tenant sobre Supabase (4 schemas)
- MCP Server con 20+ herramientas
- 15+ servicios core (BlockchainService, SemanticIndex, PolicyEngine, etc.)

Durante la evolución de MELQUISEDEC como framework, surgió la pregunta: **¿Debe Keter moverse a melquisedec como componente reutilizable?**

### Métricas de Calidad (Keter)
- **Test Coverage**: 92.94% (131/131 tests passing)
- **SonarQube**: PASSED (0 bugs, 0 vulnerabilities, A+ security)
- **Madurez**: STABLE (production-ready)
- **Tamaño**: ~500 archivos, 15+ servicios, 20+ MCP tools

### Scorecard Multidimensional (de análisis)
| Dimensión | Score | Justificación |
|-----------|-------|---------------|
| Reusabilidad | 6/10 | Interfaces limpias pero acoplado al ecosistema ALEIA |
| Madurez | 9/10 | 92.94% coverage, SonarQube certified |
| Independencia | 4/10 | Dependencias fuertes: DAATH, YESOD, AYIN, Supabase |
| Valor Framework | 7/10 | MCP Server + Policy Engine son patrones valiosos |
| **TOTAL** | **6.50/10** | Zona gris → requiere análisis profundo |

---

## Análisis de Decision Tree

Aplicamos el ComponentClassifier (4 niveles) de `design.md`:

### Nivel 1: Propósito
- **Pregunta**: ¿Es metodología o tooling del framework?
- **Respuesta**: PARCIAL - Contiene tooling (MCP, Policy Engine) Y aplicación (Backend Multi-Tenant)
- **Decisión**: Continuar a Nivel 2

### Nivel 2: Reusabilidad
- **Pregunta**: ¿Es librería reusable sin modificación significativa?
- **Respuesta**: NO (componente completo) / SÍ (subsistemas)
  - Full Keter: Referencias hard-coded a DAATH/YESOD/AYIN
  - Policy Engine: Interfaces limpias permiten abstracción
  - MCP Server: Template pattern es genérico
- **Decisión**: Evaluar subsistemas específicos

### Nivel 3: Independencia
- **Pregunta**: ¿Tiene ciclo de vida independiente?
- **Respuesta**: NO (componente completo) / PARCIAL (subsistemas)
  - Keter: Migrations y seed data específicos de bereshit
  - Policy Engine: Podría versionarse independientemente
- **Independencia Score**: 4/10
- **Decisión**: Continuar a Nivel 4

### Nivel 4: Naturaleza
- **Pregunta**: ¿Es investigación o aplicación de producción?
- **Respuesta**: APLICACIÓN DE PRODUCCIÓN
  - Test coverage > 90% (92.94%)
  - Multi-tenant real (5 tenants en seed)
  - 87 L0 product templates
  - SonarQube certified
- **Decisión Final**: ORIGIN_REPO para componente completo

---

## Opciones Consideradas

### Opción A: Mantener Keter Completo en aleia-bereshit ✅ SELECCIONADA
**Descripción**: No mover el componente completo. Permanece en su ubicación actual.

**Pros**:
- ✅ Preserva coherencia del ecosistema ALEIA
- ✅ No rompe dependencias existentes (DAATH/YESOD/AYIN)
- ✅ Mantiene contexto de negocio intacto
- ✅ Sin costo de migración ni riesgo de regresiones
- ✅ Schemas Supabase permanecen con su aplicación

**Contras**:
- ⚠️ No es directamente reutilizable por otros proyectos
- ⚠️ Patrones valiosos quedan "escondidos" en bereshit

**Confianza**: 95%

---

### Opción B: Extraer Patrones a Packages de melquisedec ✅ SELECCIONADA (SUBSISTEMAS)
**Descripción**: Mantener Keter en bereshit pero extraer subsistemas genéricos como packages independientes.

#### B.1: Policy Engine Pattern → `packages/policy-engine`
**Scope**: Abstraer patrón de Policy Engine a package reutilizable

**Componentes a Extraer**:
```typescript
// Interfaces (de keter/core/interfaces/)
interface IPolicyEngine { evaluate(context): Decision }
interface IValidator { validate(policy): ValidationResult }
interface IConflictDetector { detectConflicts(policies): Conflict[] }

// Services (abstraídos de keter/core/services/)
class PolicyEngine implements IPolicyEngine
class ConflictDetector implements IConflictDetector
class DeprecationEngine
class VersionManager
class LifecycleManager
```

**Esfuerzo de Extracción**: Medio (~2-3 días)
- Remover dependencias específicas de ALEIA
- Abstraer storage backend (no asumir Supabase)
- Tests basados en mocks (patrón ya existe en keter)

**Valor**:
- ✅ Permite policy systems en cualquier proyecto de investigación
- ✅ Patrón validado en producción (92.94% coverage)
- ✅ Interfaces ya están bien definidas

**Confianza**: 80%

#### B.2: MCP Server Template → `_templates/mcp-server-template`
**Scope**: Template para crear nuevos MCP servers rápidamente

**Componentes a Extraer**:
```
_templates/mcp-server-template/
├── server/
│   └── template-mcp-server.ts    # Skeleton server
├── tools/
│   └── example-tool.ts            # Tool registration pattern
├── handlers/
│   └── base-handler.ts            # Handler architecture
├── performance/
│   └── cache-manager.ts           # Cache pattern
├── tests/
│   └── template.test.ts           # Test structure
├── README.md                      # Setup guide
└── package.json                   # Dependencies
```

**Esfuerzo de Extracción**: Bajo (~1-2 días)
- Keter ya tiene arquitectura limpia
- Remover domain-specific tools (decree-*, policy-*)
- Incluir placeholder tools como ejemplos
- Documentar customization points

**Valor**:
- ✅ Acelera creación de MCP servers en nuevos proyectos
- ✅ Patrón probado con 20+ tools implementados
- ✅ Cache management incluido
- ✅ Test patterns incluidos

**Confianza**: 90%

**Pros (General Opción B)**:
- ✅ Maximiza reusabilidad sin romper bereshit
- ✅ Patrones validados en producción
- ✅ Bajo riesgo (extracciones independientes)
- ✅ Incrementa valor de melquisedec como framework

**Contras**:
- ⚠️ Requiere esfuerzo de abstracción
- ⚠️ Mantenimiento dividido entre repos
- ⚠️ Necesita sincronización si keter evoluciona

---

### Opción C: Extraer Keter a Repo Separado ❌ RECHAZADA
**Descripción**: Crear repo independiente `aleia-keter`

**Por qué se rechaza**:
- ❌ Rompería pipeline de validación DAATH → Keter → YESOD
- ❌ Requiere duplicar documentación de Supabase
- ❌ No hay user base fuera del ecosistema ALEIA
- ❌ Overhead de mantenimiento sin beneficio claro
- ❌ Migrations y seed data perderían contexto

---

### Opción D: Integrar Keter en daath-toolkit ❌ RECHAZADA
**Descripción**: Mover Keter a `packages/daath-toolkit`

**Por qué se rechaza**:
- ❌ Language mismatch: daath-toolkit es Python, Keter es TypeScript
- ❌ Paradigmas diferentes (validation vs policy engine)
- ❌ Bloatearía daath-toolkit con concerns no relacionados
- ❌ Keter incluye frontend (Next.js) que no tiene sentido en toolkit

---

## Decisión

**HYBRID APPROACH**: Combinación de Opción A + Opción B

```
┌──────────────────────────────────────────────────────────────┐
│                   DECISIÓN FINAL                             │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  KETER (FULL COMPONENT)                                      │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Location: aleia-bereshit/apps/keter                   │  │
│  │  Status: NO CHANGE                                     │  │
│  │  Rationale: Production app con ecosystem dependencies  │  │
│  │  Confidence: 95%                                       │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  EXTRACTABLE PATTERNS                                        │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Policy Engine Pattern                                 │  │
│  │  → packages/policy-engine/                             │  │
│  │  Confidence: 80% | Priority: P1                        │  │
│  └────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  MCP Server Template                                   │  │
│  │  → _templates/mcp-server-template/                     │  │
│  │  Confidence: 90% | Priority: P1                        │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  DOCUMENTATION                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Multi-tenant Pattern → ADR (doc only)                 │  │
│  │  Keter Case Study → docs/manifiesto/05-casos-estudio  │  │
│  │  Priority: P2                                          │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Rationale

1. **Keter permanece en bereshit** porque:
   - Es aplicación de producción con usuarios reales
   - Dependencias arquitecturales (DAATH/YESOD/AYIN) son fundamentales
   - Schemas multi-tenant son específicos del dominio ALEIA
   - Score de independencia (4/10) es demasiado bajo para migración

2. **Extraemos patrones valiosos** porque:
   - Policy Engine es genérico y reutilizable (interfaces limpias)
   - MCP Server template acelera desarrollo de nuevos proyectos
   - Patterns están validados en producción (92.94% coverage)
   - Bajo riesgo: extracciones no afectan funcionamiento de keter

3. **No creamos repo separado** porque:
   - No hay justificación para overhead de mantenimiento
   - Keter depende del ecosistema ALEIA completo

---

## Consecuencias

### Positivas ✅

#### Para MELQUISEDEC:
- ✅ **Valor Inmediato**: Policy Engine + MCP Template enriquecen framework
- ✅ **Patterns Validados**: Código probado en producción (92.94% coverage)
- ✅ **Aceleración de Desarrollo**: Templates reducen tiempo de setup
- ✅ **Documentación**: Keter como caso de estudio ejemplifica buenas prácticas

#### Para ALEIA-BERESHIT:
- ✅ **Estabilidad**: Keter no sufre disrupciones por migración
- ✅ **Coherencia**: Ecosistema DAATH/Keter/YESOD permanece intacto
- ✅ **Performance**: Multi-tenant backend optimizado permanece localizado
- ✅ **Recognition**: Keter documentado como reference implementation

#### Para Ecosistema General:
- ✅ **Multi-Repo Strategy Validated**: Demuestra que no todo debe centralizarse
- ✅ **Pattern Extraction Workflow**: Establece proceso replicable
- ✅ **Clear Boundaries**: Define qué es framework vs qué es aplicación

### Negativas / Mitigaciones ⚠️

| Consecuencia Negativa | Severidad | Mitigación |
|----------------------|-----------|------------|
| Mantenimiento dividido entre repos | Media | Clear ownership: keter team owns origin, framework team owns extracted patterns |
| Drift entre keter y extracted patterns | Media | Document keter as "reference impl" en package READMEs |
| Duplicación de esfuerzo si keter evoluciona | Baja | Sync meetings trimestrales entre teams |
| Policy Engine abstraction might miss edge cases | Media | Extensive tests basados en keter test suite |

### Riesgos Aceptados

| Riesgo | Probabilidad | Impacto | Justificación |
|--------|--------------|---------|---------------|
| Extracted patterns deviate from keter | 30% | Bajo | Aceptable - patterns evolucionan independientemente |
| MCP template becomes outdated | 20% | Bajo | Template es punto de partida, no dependency |
| Policy Engine no cubre todos los casos de keter | 40% | Medio | Se documenta scope explícitamente |

---

## Plan de Implementación

### Phase 1: Documentation (Sprint 2) - CURRENT
- [ ] **TASK-2.1**: Este ADR (ADR-002-keter-integration-decision.md) ✅
- [ ] **TASK-2.2**: Extraction plans detallados
- [ ] **TASK-2.3**: Case study en `docs/manifiesto/05-casos-estudio/keter-analysis.md`

### Phase 2: Policy Engine Extraction (Sprint 3)
- [ ] Create `packages/policy-engine/` structure
- [ ] Extract interfaces: IPolicyEngine, IValidator, IConflictDetector
- [ ] Implement abstract PolicyEngine (no ALEIA specifics)
- [ ] Port test patterns from keter (target: >90% coverage)
- [ ] Document: README with "REF: keter implementation"

**Estimated Effort**: 2-3 días
**Assignee**: TBD

### Phase 3: MCP Server Template (Sprint 3)
- [ ] Create `_templates/mcp-server-template/` structure
- [ ] Extract server skeleton from keter MCP
- [ ] Include: tool registration, handlers, cache patterns
- [ ] Add placeholder example tools
- [ ] Document: Setup guide + customization points

**Estimated Effort**: 1-2 días
**Assignee**: TBD

### Phase 4: Case Study Documentation (Sprint 4)
- [ ] Write keter case study with architecture diagrams
- [ ] Document multi-tenant pattern as ADR
- [ ] Create cross-references between melquisedec docs and keter
- [ ] Add to `docs/manifiesto/05-casos-estudio/`

**Estimated Effort**: 1 día
**Assignee**: TBD

---

## Referencias

### Documentos de Análisis
- `.spec-workflow/specs/research-keter-integration-v1.0.0/Implementation Logs/analysis/keter-raw-data.md` - Datos crudos de keter
- `.spec-workflow/specs/research-keter-integration-v1.0.0/Implementation Logs/analysis/keter-evaluation.md` - Scorecard y evaluación
- `.spec-workflow/specs/research-keter-integration-v1.0.0/Implementation Logs/analysis/keter-decision.md` - Decision tree completo

### Código Fuente (Read-Only)
- `[REPO:aleia-bereshit] apps/keter/` - Keter source code
- `[REPO:aleia-bereshit] apps/keter/packages/keter/core/interfaces/` - Interfaces to abstract
- `[REPO:aleia-bereshit] apps/keter/packages/keter/mcp/` - MCP server implementation

### Documentación Relacionada
- [ADR-001: Estructura de Monorepo](ADR-001-monorepo-structure.md) - Define arquitectura general
- `docs/manifiesto/02-arquitectura/` - Arquitectura ALEIA-BERESHIT

---

## Aprobaciones

| Rol | Nombre | Fecha | Decisión |
|-----|--------|-------|----------|
| Architect | Claude Opus 4.5 | 2026-01-08 | ✅ Aprobado |
| Framework Lead | - | - | Pending |
| Bereshit Lead | - | - | Pending |

---

## Changelog

- **2026-01-08**: ADR creado basado en análisis completo de Sprint 1
- **2026-01-08**: Decision tree execution completed con 88% confidence

---

## Notas

### ¿Por qué este enfoque es DAATH-ZEN?

Este ADR ejemplifica los principios DAATH-ZEN:
1. **Evidencia sobre intuición**: Decision tree con métricas cuantificables
2. **Iterativo**: Sprint-based analysis con refinamiento continuo
3. **Documentación como código**: Todo versionado y traceable
4. **Multi-concern awareness**: Reconoce que un componente puede tener múltiples naturalezas
5. **Pragmatismo**: Hybrid approach en vez de decisión binaria

### Model Strategy Validation

- **Sonnet 4.5**: Gathering raw data (TASK-1.1) ✅ Efectivo
- **Opus 4.5**: Deep analysis (TASK-1.2, 1.3) ✅ Excelente depth
- **Sonnet 4.5**: Documentation (este ADR) ✅ Cost-effective para síntesis

**Cost-Benefit**: Usar Opus para análisis crítico, Sonnet para docs = optimal ROI
