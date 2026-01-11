# RQ2: Abstraction Layer Design - KICKOFF

**Status**: 🟡 IN PROGRESS (2025-01-23)
**Architect**: SALOMON
**Duration**: 5 days (estimated)
**Prerequisite**: ✅ RQ1 Complete

---

## 🎯 Research Question

**RQ2**: ¿Qué abstracciones necesita keter para ser independiente de ALEIA?

**Hypothesis H2** (from [hypothesis.md](../00-problem/hypothesis.md)):
> Se necesitan 5 abstraction patterns: IDaathAdapter (semantic graph), IYesodSSR (server rendering), IAyinSync (schema realtime), ITemplateProvider (plugin system), ITenantResolver (multi-tenancy)

**RQ1 Discovery**: ❌ **Hypothesis H2 INVALIDATED**
- NO se necesitan abstractions para dependencias externas (no existen)
- Keter YA tiene arquitectura modular interna
- Solo se necesita validar arquitectura existente

---

## 🔄 Revised Objective

**Original**: Diseñar 5 abstraction layers para desacoplar de ALEIA
**Revised**: Documentar y validar arquitectura modular existente

### Questions to Answer

1. **¿La arquitectura packages/keter/{core,mcp,services} es adecuada?**
   - ¿Separación de concerns correcta?
   - ¿Interfaces bien definidas?
   - ¿Acoplamiento interno bajo?

2. **¿Se necesita alguna abstraction adicional?**
   - Config management (¿centralizar 21 env vars?)
   - Schema access (¿abstraer 19 hardcoded strings?)
   - Template loading (¿interfaz para 62 YAML files?)

3. **¿Qué cambios mínimos optimizan portabilidad?**
   - Refactorings simples
   - Config consolidation
   - Path abstractions

4. **¿Cómo validamos la arquitectura?**
   - Dependency graph analysis
   - Coupling metrics
   - Test coverage per module

5. **¿Qué ADRs documentan las decisiones?**
   - ADR-003: Keter Modular Architecture (why packages/ structure?)
   - ADR-004: No External Abstractions Needed (why 0 @aleia/* deps?)
   - ADR-005: Config-Driven Design (why .env.example approach?)

---

## 📋 RQ2 Tasks (Revised)

### Task 2.1: Analyze Existing Architecture (1 day)

**Objective**: Entender la arquitectura packages/keter/ actual

**Actions**:
1. Map dependencies entre packages/keter/{core,mcp,services}
2. Identify interfaces públicas vs internas
3. Calculate coupling metrics (instability, abstractness)
4. Identify circular dependencies (if any)
5. Document design patterns used (DI, Repository, Adapter, etc.)

**Tools**:
- Madge: `madge --circular --image graph.svg src/`
- ts-morph: Extract interfaces and exports
- SonarQube: Calculate coupling metrics

**Deliverable**: `01-design/abstraction-layers/existing-architecture.md`

### Task 2.2: Identify Minimal Refactorings (0.5 days)

**Objective**: Qué cambios simples mejoran portabilidad

**Actions**:
1. Schema names: Create `config/schemas.ts` (19 strings → 1 module)
2. Template paths: Create `config/paths.ts` (hardcoded paths → config)
3. ENV vars: Group by domain (Database, Blockchain, APIs, etc.)
4. Service factories: Extract instantiation logic (if hardcoded)

**Deliverable**: `01-design/abstraction-layers/minimal-refactorings.md`

### Task 2.3: Validate No External Abstractions Needed (0.5 days)

**Objective**: Confirmar que NO se necesitan IDaathAdapter, etc.

**Actions**:
1. Re-verify: No @aleia/daath runtime dependencies
2. Re-verify: No @aleia/yesod SSR assumptions
3. Re-verify: No @aleia/ayin schema sync logic
4. Document: Why keter is already independent

**Deliverable**: `01-design/abstraction-layers/no-external-abstractions.md`

### Task 2.4: Design Config Consolidation (1 day)

**Objective**: Centralizar 21 env vars en config coherente

**Actions**:
1. Group vars by domain:
   ```typescript
   // config/database.config.ts
   export const DatabaseConfig = {
     mode: process.env.DB_MODE as 'local' | 'supabase',
     postgres: { ... },
     supabase: { ... }
   };

   // config/blockchain.config.ts (ya existe)

   // config/integrations.config.ts
   export const IntegrationsConfig = {
     redis: { url: process.env.REDIS_URL },
     github: { token: process.env.GITHUB_TOKEN },
     googleDrive: { ... }
   };
   ```

2. Create config validation (zod schemas)
3. Create config loading strategy (env → validated config)
4. Document config architecture

**Deliverable**: `01-design/abstraction-layers/config-consolidation.md`

### Task 2.5: Design Interface Contracts (1 day)

**Objective**: Documentar interfaces públicas de packages/keter/

**Actions**:
1. Extract public APIs from packages/keter/core/
2. Extract public APIs from packages/keter/mcp/
3. Extract public APIs from packages/keter/services/
4. Document interface contracts (inputs, outputs, errors)
5. Identify breaking changes if moved to melquisedec

**Deliverable**: `01-design/abstraction-layers/interface-contracts.md`

### Task 2.6: Write ADRs (1 day)

**Objective**: Documentar decisiones arquitectónicas

**ADRs to Write**:

1. **ADR-003: Keter Modular Architecture**
   - Context: Why packages/keter/{core,mcp,services}?
   - Decision: Modular monorepo structure
   - Consequences: High cohesion, low coupling
   - Status: Accepted (already implemented)

2. **ADR-004: No External Abstractions Needed**
   - Context: RQ1 found 0 @aleia/* dependencies
   - Decision: NO IDaathAdapter, IYesodSSR, etc.
   - Consequences: Simpler migration, less code
   - Status: Accepted (validated by RQ1)

3. **ADR-005: Config-Driven Design**
   - Context: 21 env vars, DB_MODE switchable
   - Decision: ENV-driven configuration (not hardcoded)
   - Consequences: Tenant-agnostic, portable
   - Status: Accepted (already implemented)

**Deliverable**: `01-design/architecture/ADR-003.md`, `ADR-004.md`, `ADR-005.md`

---

## 📊 Success Criteria

RQ2 complete when:
- [ ] Existing architecture documented (dependency graph, coupling metrics)
- [ ] Minimal refactorings identified (schema strings, template paths, config)
- [ ] Confirmed: No external abstractions needed (validation checklist)
- [ ] Config consolidation designed (config/\*.ts modules)
- [ ] Interface contracts documented (public APIs per package)
- [ ] 3 ADRs written (ADR-003, ADR-004, ADR-005)
- [ ] SALOMON validation: 100% PASSED

**Estimated Effort**: 5 days → **REVISED to 3 days** (no complex abstractions)

---

## 🔄 Handoff from HYPATIA (Researcher)

### RQ1 Key Findings

1. **NO external dependencies**: 0 @aleia/* imports found
2. **Modular structure exists**: packages/keter/{core,mcp,services}
3. **Config-driven**: 21 env vars, DB_MODE switchable
4. **Templates portable**: 62 YAML files self-contained
5. **Minimal hardcoding**: Only 19 schema name strings

### Questions for SALOMON

1. **Why was keter already modular?**
   - Was it designed for portability?
   - Prior migration attempt?

2. **Are there hidden runtime dependencies?**
   - Database schema interdependencies?
   - External service assumptions (Neo4j, Blockchain)?

3. **Should we consolidate config?**
   - 21 env vars → typed config modules?
   - Validation layer (zod)?

4. **What's the coupling between core/mcp/services?**
   - Circular dependencies?
   - Tight coupling points?

5. **What interfaces are public vs internal?**
   - What can melquisedec consumers use?
   - What's implementation detail?

---

## 🎯 Expected Deliverables

### 01-design/abstraction-layers/
1. `existing-architecture.md` - Current packages/keter/ structure
2. `minimal-refactorings.md` - Simple changes for portability
3. `no-external-abstractions.md` - Why we don't need IDaathAdapter, etc.
4. `config-consolidation.md` - Design for config/\*.ts modules
5. `interface-contracts.md` - Public APIs documentation

### 01-design/architecture/
1. `ADR-003-keter-modular-architecture.md`
2. `ADR-004-no-external-abstractions.md`
3. `ADR-005-config-driven-design.md`

### 01-design/contracts/
1. `IKeterCore.ts` - Core functionality contract
2. `IKeterMCP.ts` - MCP server contract
3. `IKeterServices.ts` - Shared services contract

---

## 🔧 Tools & Resources

### Analysis Tools
- **Madge**: Dependency graph visualization
  ```bash
  npm install -g madge
  cd ~/aleia-bereshit/apps/keter/packages/keter
  madge --circular --extensions ts --image graph.svg core/
  ```

- **ts-morph**: TypeScript AST analysis
  ```typescript
  import { Project } from "ts-morph";
  const project = new Project({ tsConfigFilePath: "tsconfig.json" });
  const sourceFiles = project.getSourceFiles("packages/keter/**/*.ts");
  // Extract exports, interfaces, etc.
  ```

- **SonarQube**: Code metrics
  ```bash
  sonar-scanner -Dsonar.projectKey=keter -Dsonar.sources=packages/keter
  # View coupling, complexity, duplication metrics
  ```

### Reference Docs
- [Clean Architecture (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [TypeScript Module Resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
- [Dependency Inversion Principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

---

## 📅 Next Steps (Immediate)

1. [ ] Execute Task 2.1: Analyze existing architecture
   - Generate dependency graph with Madge
   - Calculate coupling metrics
   - Document packages/keter/ structure

2. [ ] Execute Task 2.2: Identify minimal refactorings
   - Schema names → config/schemas.ts
   - Template paths → config/paths.ts
   - ENV vars → typed config modules

3. [ ] Execute Task 2.3: Validate no external abstractions
   - Confirm 0 runtime dependencies
   - Document why keter is independent

4. [ ] Update hypothesis.md with RQ2 findings
   - Mark H2 as PARTIALLY INVALIDATED
   - Document actual architecture vs predicted

---

## ⚠️ Important Notes

1. **RQ2 scope reduced**: 5 days → 3 days (no complex abstractions needed)
2. **Focus**: Document existing architecture, not design new one
3. **Outcome**: ADRs that explain current design + minimal refactorings
4. **Validation**: SALOMON checklist in `.melquisedec/salomon_validation.yaml`

---

**Architect**: SALOMON
**Date**: 2025-01-23
**Duration**: 3 days (revised from 5 days)
**Next**: Execute Task 2.1 (Analyze Existing Architecture)
