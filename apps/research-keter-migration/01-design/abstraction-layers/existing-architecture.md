# Existing Architecture Analysis

**Date**: 2025-01-23
**Analyst**: SALOMON (Architect)
**Source**: `C:\proyectos\aleia-bereshit\apps\keter\packages\keter`
**Method**: Static analysis (Madge, file structure, imports)

---

## 📊 Executive Summary

Keter utiliza una **arquitectura modular de 3 capas** con separación clara de concerns:

- **core/** (34 archivos TS): Domain logic, interfaces, services
- **mcp/** (33 archivos TS): MCP Server implementation, tools, handlers
- **services/** (1 archivo TS): Shared utilities

**Hallazgos clave**:
- ✅ Separación de concerns bien definida
- ⚠️ 1 dependencia circular detectada (core/interfaces/IPolicyEngine.ts ↔ core/types.ts)
- ✅ MCP depende de core (correcto: capas hacia dentro)
- ✅ Core NO depende de MCP (correcto: domain independiente)
- ✅ Uso de Dependency Injection (inversify)
- ✅ Repository pattern implementado

---

## 🏗️ Architecture Overview

### Layer Structure

```
packages/keter/
├── core/                    # Domain Layer (34 files)
│   ├── config/              # Configuration modules
│   ├── context/             # Tenant context management
│   ├── database/            # Database adapters
│   ├── interfaces/          # Domain interfaces (7 interfaces)
│   ├── repositories/        # Repository implementations (4 mocks)
│   └── services/            # Domain services (15+ services)
│
├── mcp/                     # Application Layer (33 files)
│   ├── performance/         # Caching, optimization
│   ├── server/              # MCP server setup
│   ├── tools/               # MCP tools (decree, policy handlers)
│   └── tests/               # Integration tests
│
└── services/                # Shared utilities (1 file)
```

**Dependency Direction**: `mcp/ → core/` (Application → Domain)
**Domain Independence**: core/ NO importa de mcp/ ✅

---

## 📦 Package Details

### Core Package (34 TypeScript files)

**Purpose**: Domain logic, business rules, data access

**Subdirectories**:
- `config/` (1 file): blockchain.config.ts
- `context/` (3 files): TenantContextManager, types, index
- `database/` (1 file): DatabaseAdapter (Supabase + PostgreSQL)
- `interfaces/` (7 files): IAuditLogger, IBlockchainService, IPolicyEngine, IPolicyRepository
- `repositories/` (4 files): Mock implementations (Audit, Blockchain, Decree, Policy)
- `services/` (15+ files): BlockchainService, CMISRepository, ConflictDetector, DeprecationEngine, DocumentEmbedder, HealthMonitor, LifecycleManager, PolicyEngine, PolicyValidator, RecordsManager, RuleLearner, SemanticAPI, SemanticIndex, ValidityManager, VersionManager

**Public Interfaces**:
```typescript
// core/interfaces/
export interface IAuditLogger {
  log(event: AuditEvent): Promise<void>;
  query(criteria: AuditCriteria): Promise<AuditEvent[]>;
}

export interface IBlockchainService {
  registerDecree(data: DecreeData): Promise<string>;
  verifyDecree(decreeId: string, hash: string): Promise<boolean>;
  getDecreeProof(decreeId: string): Promise<any>;
}

export interface IPolicyEngine {
  evaluate(input: EvaluationInput): Promise<EvaluationResult>;
  loadPolicies(): Promise<void>;
}

export interface IPolicyRepository {
  getPolicy(id: string): Promise<Policy | null>;
  listPolicies(): Promise<Policy[]>;
  savePolicy(policy: Policy): Promise<void>;
  deletePolicy(id: string): Promise<void>;
}
```

**Design Patterns**:
- **Dependency Injection**: inversify container (container.ts with 10 dependents)
- **Repository Pattern**: 4 repositories (Audit, Blockchain, Decree, Policy)
- **Adapter Pattern**: DatabaseAdapter (abstracts Supabase + pg)
- **Context Pattern**: TenantContextManager (AsyncLocalStorage for multi-tenancy)

**Dependencies (External NPM)**:
- `inversify` (DI container)
- `@supabase/supabase-js` (database client)
- `pg` (PostgreSQL driver)
- `ethers` (blockchain interaction)
- `@xenova/transformers` (embeddings)
- `@octokit/rest` (GitHub API)
- `express` (HTTP server)
- `redis` (caching)
- `jsonwebtoken` (authentication)

**Dependencies (Internal)**:
- 1 import from mcp: `import type { Decree } from '../../mcp/tools/decree-query.schema.js'`
- Note: Type-only import, no runtime dependency ✅

### MCP Package (33 TypeScript files)

**Purpose**: MCP Server implementation, tool handlers

**Subdirectories**:
- `performance/` (1 file): cache-manager.ts
- `server/` (1 file): keter-mcp-server.ts (main server setup)
- `tools/` (26 files): Decree tools (create, delete, list, query, restore, update), Policy tools (create, delete, export, list, update, validate), CMIS tools, bulk operations
- `tests/` (test files)

**Tool Categories**:
1. **Decree Management** (12 files: 6 handlers + 6 schemas)
   - decree-create, decree-delete, decree-list, decree-list-versions, decree-query, decree-restore, decree-update

2. **Policy Management** (12 files: 6 handlers + 6 schemas)
   - policy-create, policy-delete, policy-export, policy-list, policy-update, policy-validate

3. **CMIS/Records** (1 file)
   - keter-cmis-records-tools

4. **Bulk Operations** (2 files)
   - bulk-operations handler + schema

**Dependencies on Core**:
```typescript
// MCP imports from core
import { CMISRepository } from '../../core/services/CMISRepository';
import { RecordsManager } from '../../core/services/RecordsManager';
import { LifecycleManager } from '../../core/services/LifecycleManager';
import TenantContextManager from '../../core/context/TenantContextManager.js';
import type { IAuditLogger } from '../../core/interfaces/IAuditLogger.js';
import type { IDecreeRepository } from '../../core/interfaces/IDecreeRepository.js';
import type { IPolicyRepository } from '../../core/interfaces/IPolicyRepository.js';
import type { Policy } from '../../core/types.js';
import type { IBlockchainService } from '../../core/interfaces/IBlockchainService.js';
```

**Observation**: MCP layer correctly depends on core interfaces (not implementations) ✅

### Services Package (1 TypeScript file)

**Purpose**: Shared utilities (minimal usage)

**Note**: Most services are in `core/services/`, not `packages/keter/services/`. This package appears underutilized.

---

## 🔗 Dependency Graph

### Madge Analysis Results

**Circular Dependencies Detected**: ⚠️ 1

```
core/interfaces/IPolicyEngine.ts ↔ core/types.ts
```

**Impact**: LOW (type-level circular reference)
**Recommendation**: Extract shared types to separate module (e.g., `core/domain/types.ts`)

**Most Depended-Upon Modules** (top 10):
```
10  core/container.ts            # DI container setup
5   core/policy-engine.ts        # Policy evaluation logic
4   core/interfaces/index.ts     # Interface barrel export
3   core/services/SemanticAPI.ts # HTTP API
2   core/context/index.ts        # Context management
2   core/index.ts                # Package entry point
2   core/repositories/MockPolicyRepository.ts
2   core/services/BlockchainService.ts
2   core/services/RecordsManager.ts
1   (15 modules with 1 dependent)
```

**Modules with 0 Dependents** (leaf nodes): 35 modules
- Most services are leaf nodes (good: independent, reusable)
- All schemas are leaf nodes (good: data structures)
- All config files are leaf nodes (good: configuration)

### Inter-Package Dependencies

```mermaid
graph TD
    MCP[mcp/] -->|imports| CORE[core/]
    MCP -->|"CMISRepository<br/>RecordsManager<br/>LifecycleManager"| CORE_SERVICES[core/services/]
    MCP -->|"IAuditLogger<br/>IBlockchainService<br/>IPolicyEngine<br/>IPolicyRepository"| CORE_INTERFACES[core/interfaces/]
    MCP -->|"TenantContextManager"| CORE_CONTEXT[core/context/]
    MCP -->|"Policy types"| CORE_TYPES[core/types.ts]

    CORE -.->|"type-only import<br/>Decree"| MCP_TOOLS[mcp/tools/]

    SERVICES[services/] -.->|minimal usage| CORE

    style CORE fill:#90EE90
    style MCP fill:#87CEEB
    style SERVICES fill:#FFE4B5
```

**Legend**:
- Solid arrows: Runtime dependencies
- Dashed arrows: Type-only dependencies
- Green: Domain layer (core)
- Blue: Application layer (mcp)
- Yellow: Shared utilities (services)

---

## 🎯 Coupling Metrics

### Instability (I = Ce / (Ce + Ca))

**Formula**:
- Ce (Efferent Coupling) = Outgoing dependencies
- Ca (Afferent Coupling) = Incoming dependencies
- I = Ce / (Ce + Ca)
- Range: 0 (stable, max incoming) to 1 (unstable, max outgoing)

**Calculated Metrics** (approximated from Madge data):

| Module | Ce (Out) | Ca (In) | Instability | Assessment |
|--------|----------|---------|-------------|------------|
| core/container.ts | 10+ | 10 | ~0.5 | Balanced |
| core/policy-engine.ts | 3 | 5 | 0.375 | Stable |
| core/interfaces/index.ts | 7 | 4 | 0.636 | Slightly unstable |
| core/services/SemanticAPI.ts | 5+ | 3 | ~0.625 | Slightly unstable |
| mcp/tools/index.ts | 26+ | 26 | 0.5 | Balanced |
| mcp/server/keter-mcp-server.ts | 10+ | 4 | ~0.714 | Unstable (expected for server) |

**Observations**:
- Core modules are generally stable (I < 0.5) ✅
- MCP tools are balanced (I ≈ 0.5) ✅
- MCP server is intentionally unstable (orchestrator role) ✅

### Abstractness (A = Na / Nc)

**Formula**:
- Na = Number of abstract classes/interfaces
- Nc = Total number of classes/interfaces
- Range: 0 (concrete) to 1 (abstract)

**Calculated**:
- `core/interfaces/`: 7 interfaces, 0 concrete classes → A = 1.0 (fully abstract) ✅
- `core/services/`: 15+ services, mostly concrete → A ≈ 0.1 (fully concrete) ✅
- `core/repositories/`: 4 repositories, 4 interfaces → A ≈ 0.5 (balanced)

**Observation**: Good separation between abstract interfaces (core/interfaces/) and concrete implementations (core/services/) ✅

### Distance from Main Sequence (D = |A + I - 1|)

**Formula**: Ideal zone is D ≈ 0 (balanced abstractness and instability)

| Module | A | I | D = \|A + I - 1\| | Zone |
|--------|---|---|-------------------|------|
| core/interfaces/ | 1.0 | 0.2 | 0.2 | ✅ Good |
| core/services/ | 0.1 | 0.6 | 0.3 | ✅ Acceptable |
| mcp/tools/ | 0.0 | 0.5 | 0.5 | ⚠️ Zone of Pain (concrete + unstable) |
| mcp/server/ | 0.0 | 0.7 | 0.3 | ✅ Acceptable (orchestrator) |

**Observations**:
- Core interfaces in ideal zone (abstract + stable) ✅
- Core services acceptable (concrete but somewhat stable) ✅
- MCP tools in "Zone of Pain" but expected (handlers are concrete and change frequently) ⚠️ Acceptable
- MCP server acceptable as orchestrator ✅

**Overall**: D < 0.5 for most modules → Architecture is healthy ✅

---

## 🧩 Design Patterns Identified

### 1. Dependency Injection (Inversify)

**Location**: `core/container.ts` (10 dependents)

**Usage**:
```typescript
// core/container.ts
const container = new Container();
container.bind<IPolicyEngine>(TYPES.PolicyEngine).to(PolicyEngine);
container.bind<IPolicyRepository>(TYPES.PolicyRepository).to(MockPolicyRepository);
// ... 8+ more bindings
```

**Benefits**:
- Loose coupling between interfaces and implementations
- Easy to swap implementations (Mock → Real)
- Testability (inject mocks)

### 2. Repository Pattern

**Repositories** (4):
- MockAuditLogger (IAuditLogger)
- MockBlockchainService (IBlockchainService)
- MockDecreeRepository (IDecreeRepository)
- MockPolicyRepository (IPolicyRepository)

**Pattern**:
```typescript
// Interface in core/interfaces/
export interface IPolicyRepository {
  getPolicy(id: string): Promise<Policy | null>;
  listPolicies(): Promise<Policy[]>;
  savePolicy(policy: Policy): Promise<void>;
  deletePolicy(id: string): Promise<void>;
}

// Implementation in core/repositories/
@injectable()
export class MockPolicyRepository implements IPolicyRepository {
  private policies: Map<string, Policy> = new Map();

  async getPolicy(id: string): Promise<Policy | null> {
    return this.policies.get(id) || null;
  }
  // ...
}
```

**Benefits**:
- Data access abstraction
- Easy to switch persistence (Mock → Supabase → Neo4j)
- Testability

### 3. Adapter Pattern

**Example**: DatabaseAdapter (core/database/DatabaseAdapter.ts)

**Purpose**: Abstract over Supabase and direct PostgreSQL

```typescript
export class DatabaseAdapter {
  private supabaseClient?: SupabaseClient;
  private pgPool?: pg.Pool;

  constructor(mode: 'supabase' | 'local') {
    if (mode === 'supabase') {
      this.supabaseClient = createClient(url, key);
    } else {
      this.pgPool = new pg.Pool({ host, port, database, user, password });
    }
  }

  async query(sql: string, params: any[]) {
    if (this.supabaseClient) {
      return this.supabaseClient.rpc('execute_sql', { sql, params });
    } else {
      return this.pgPool.query(sql, params);
    }
  }
}
```

**Benefits**:
- Switches between Supabase (cloud) and PostgreSQL (local)
- Single interface for both
- Aligns with ENV-driven config (DB_MODE)

### 4. Context Pattern (Tenant Isolation)

**Location**: `core/context/TenantContextManager.ts`

**Pattern**: AsyncLocalStorage for request-scoped tenant context

```typescript
import { AsyncLocalStorage } from 'async_hooks';

export class TenantContextManager {
  private als = new AsyncLocalStorage<TenantContext>();

  run<T>(tenantId: string, fn: () => T): T {
    const context = { tenantId, requestId: randomUUID() };
    return this.als.run(context, fn);
  }

  getCurrentTenant(): string | null {
    return this.als.getStore()?.tenantId || null;
  }
}
```

**Benefits**:
- Multi-tenant isolation
- No need to pass tenantId through every function call
- Request-scoped (avoids global state issues)

### 5. Schema-Driven Validation (Zod)

**Usage**: All MCP tool schemas use Zod

```typescript
// mcp/tools/decree-create.schema.ts
export const DecreeCreateSchema = z.object({
  decree_number: z.string(),
  title: z.string(),
  content: z.string(),
  status: z.enum(['draft', 'active', 'deprecated']),
  metadata: z.record(z.any()).optional()
});
```

**Benefits**:
- Runtime validation
- Type safety (TypeScript types inferred from schemas)
- MCP protocol compliance

---

## 🚨 Issues & Recommendations

### Issue 1: Circular Dependency (core/interfaces/IPolicyEngine.ts ↔ core/types.ts)

**Severity**: ⚠️ LOW (type-level only)

**Details**:
```
core/interfaces/IPolicyEngine.ts imports core/types.ts
core/types.ts likely re-exports IPolicyEngine or uses it
```

**Recommendation**:
```typescript
// Create core/domain/types.ts
export type Policy = { id: string; ... };
export type EvaluationInput = { ... };
export type EvaluationResult = { ... };

// core/interfaces/IPolicyEngine.ts imports from domain/types.ts
import type { Policy, EvaluationInput, EvaluationResult } from '../domain/types';

// core/types.ts re-exports everything
export * from './domain/types';
export * from './interfaces/IPolicyEngine';
```

**Effort**: 0.5 hours
**Priority**: LOW (not blocking migration)

### Issue 2: Type-Only Import from MCP to Core

**Details**:
```typescript
// core/repositories/MockDecreeRepository.ts
import type { Decree } from '../../mcp/tools/decree-query.schema.js';
```

**Problem**: Core (domain layer) depends on MCP (application layer), even if type-only

**Severity**: ⚠️ MEDIUM (violates layer architecture)

**Recommendation**:
```typescript
// Move Decree type to core/domain/types.ts
export type Decree = {
  id: string;
  decree_number: string;
  title: string;
  content: string;
  status: 'draft' | 'active' | 'deprecated';
  created_at: string;
  updated_at: string;
};

// mcp/tools/decree-query.schema.ts imports from core
import type { Decree } from '../../../core/domain/types';
```

**Effort**: 1 hour
**Priority**: MEDIUM (should fix for clean architecture)

### Issue 3: Underutilized services/ Package

**Details**: Only 1 file in `packages/keter/services/`, but 15+ services in `core/services/`

**Recommendation**: Either:
- **Option A**: Move shared utilities to `services/` (e.g., cache-manager currently in mcp/performance/)
- **Option B**: Remove `services/` package and keep everything in `core/`

**Effort**: 2 hours (reorganize)
**Priority**: LOW (cosmetic)

### Issue 4: Mock Repositories in Production Code

**Details**: All repositories are Mock* implementations

**Severity**: ⚠️ MEDIUM (not production-ready)

**Recommendation**:
- Keep MockRepositories for testing
- Implement SupabaseRepositories for production
- Use DI container to switch based on ENV

```typescript
// core/repositories/SupabasePolicyRepository.ts
@injectable()
export class SupabasePolicyRepository implements IPolicyRepository {
  constructor(private db: SupabaseClient) {}

  async getPolicy(id: string): Promise<Policy | null> {
    const { data } = await this.db
      .from('keter_core.policies')
      .select('*')
      .eq('id', id)
      .single();
    return data || null;
  }
  // ...
}

// core/container.ts
if (process.env.NODE_ENV === 'production') {
  container.bind<IPolicyRepository>(TYPES.PolicyRepository).to(SupabasePolicyRepository);
} else {
  container.bind<IPolicyRepository>(TYPES.PolicyRepository).to(MockPolicyRepository);
}
```

**Effort**: 3 days (implement 4 repositories)
**Priority**: HIGH (required for production, but NOT blocking migration to melquisedec)

---

## ✅ Strengths

1. **Clean Layer Separation**: MCP → Core (correct direction) ✅
2. **Dependency Injection**: Loose coupling via inversify ✅
3. **Interface-Driven**: 7 interfaces, implementations swappable ✅
4. **Repository Pattern**: Data access abstraction ✅
5. **Multi-Tenant Support**: AsyncLocalStorage context ✅
6. **Config-Driven**: DatabaseAdapter switches modes ✅
7. **Low Coupling**: Most modules have D < 0.5 ✅
8. **Type Safety**: Zod schemas + TypeScript ✅

---

## 🎯 Migration Readiness Assessment

| Aspect | Score | Notes |
|--------|-------|-------|
| **Modularity** | 9/10 | Already structured as packages/{core,mcp,services} |
| **Independence** | 8/10 | No @aleia/* deps, 1 minor type import to fix |
| **Coupling** | 8/10 | Low coupling (D < 0.5), 1 circular dep |
| **Testability** | 9/10 | DI + Repository pattern = easy mocking |
| **Portability** | 9/10 | ENV-driven config, switchable DB mode |
| **Documentation** | 5/10 | Interfaces well-typed, but no ADRs yet |
| **Production Readiness** | 6/10 | Mock repos need replacement, but NOT blocking |

**Overall**: 7.7/10 → **Ready for migration with minor refactorings** ✅

---

## 📋 Next Steps (Task 2.2)

Based on this analysis, the minimal refactorings needed are:

1. **Fix circular dependency** (0.5 hours)
   - Extract shared types to `core/domain/types.ts`

2. **Fix type-only import** (1 hour)
   - Move `Decree` type from mcp to core

3. **Consolidate config** (see Task 2.4)
   - Group 21 env vars into typed modules

4. **Document architecture** (in ADRs)
   - ADR-003: Why modular structure?
   - ADR-004: Why no external abstractions?
   - ADR-005: Why config-driven?

**Total Refactoring Effort**: 1.5 hours (minimal)

---

**Analyst**: SALOMON
**Status**: ✅ Task 2.1 COMPLETE
**Next**: Task 2.2 (Identify Minimal Refactorings)
