# Minimal Refactorings for Portability

**Date**: 2025-01-23
**Architect**: SALOMON
**Prerequisite**: Task 2.1 (Existing Architecture Analysis) ✅
**Goal**: Identify smallest changes to maximize portability

---

## 🎯 Executive Summary

Based on RQ1 (Dependency Audit) and Task 2.1 (Architecture Analysis), keter needs **only 4 minimal refactorings** to be fully portable:

1. **Schema Names** (19 refs) → Config module (0.5 hours)
2. **Circular Dependency** → Extract domain types (0.5 hours)
3. **Type Import** → Move Decree type to core (1 hour)
4. **Template Paths** → Relative path config (0.5 hours)

**Total Effort**: 2.5 hours
**Impact**: ✅ Zero runtime dependencies, ✅ Clean architecture, ✅ Fully portable

---

## 🔧 Refactoring 1: Schema Names → Config Module

### Problem

**From RQ1**: 19 hardcoded schema name strings found:
```typescript
// database/types.ts
export type SchemaName = 'ayin_config' | 'keter_core' | 'shared_kg';

// tests/integration/ayin-realtime.test.ts
const { data, error } = await supabase.from('ayin_config.decrees')
const { data, error } = await supabase.from('keter_core.policies')
```

**Issue**: Hardcoded strings → Cannot switch schemas per environment

### Solution

Create `core/config/schemas.ts`:

```typescript
/**
 * Schema Configuration
 *
 * Centralizes all database schema names for easy switching
 * per environment (dev, staging, prod, multi-tenant)
 */

export interface SchemaConfig {
  /** Configuration schema (user settings, app config) */
  readonly config: string;

  /** Core business logic schema (decrees, policies) */
  readonly core: string;

  /** Shared knowledge graph schema */
  readonly sharedKg: string;
}

/**
 * Default schema names (ALEIA-specific)
 * Override via environment variables
 */
const DEFAULT_SCHEMAS: SchemaConfig = {
  config: 'ayin_config',
  core: 'keter_core',
  sharedKg: 'shared_kg'
};

/**
 * Load schema configuration from environment
 * Falls back to defaults if not specified
 */
export const SCHEMAS: SchemaConfig = {
  config: process.env.SCHEMA_CONFIG || DEFAULT_SCHEMAS.config,
  core: process.env.SCHEMA_CORE || DEFAULT_SCHEMAS.core,
  sharedKg: process.env.SCHEMA_SHARED_KG || DEFAULT_SCHEMAS.sharedKg
};

/**
 * Utility: Fully qualified table name
 * @example getTable('decrees') → 'keter_core.decrees'
 */
export function getTable(tableName: string, schema: keyof SchemaConfig = 'core'): string {
  return `${SCHEMAS[schema]}.${tableName}`;
}
```

### Changes Required

**File 1**: Update `database/types.ts`
```typescript
// BEFORE
export type SchemaName = 'ayin_config' | 'keter_core' | 'shared_kg';

// AFTER
import { SCHEMAS } from '../config/schemas';
export type SchemaName = keyof typeof SCHEMAS; // 'config' | 'core' | 'sharedKg'
```

**File 2**: Update `tests/integration/ayin-realtime.test.ts` (12 refs)
```typescript
// BEFORE
const { data } = await supabase.from('ayin_config.decrees').select('*');
const { data } = await supabase.from('keter_core.policies').select('*');

// AFTER
import { getTable } from '../../core/config/schemas';
const { data } = await supabase.from(getTable('decrees', 'core')).select('*');
const { data } = await supabase.from(getTable('policies', 'core')).select('*');
```

**File 3**: Update remaining 4 references in other files

### .env.example Update

```bash
# === Database Schema Names ===
# Override default schema names per environment
# Useful for multi-tenant, staging, or custom deployments
SCHEMA_CONFIG=ayin_config        # Configuration schema (default)
SCHEMA_CORE=keter_core           # Core business logic schema (default)
SCHEMA_SHARED_KG=shared_kg       # Shared knowledge graph (default)
```

### Benefits

- ✅ Single source of truth for schema names
- ✅ Environment-specific schemas (dev/staging/prod)
- ✅ Multi-tenant support (different schemas per tenant)
- ✅ Easy to test (override in test env)
- ✅ Portable (no ALEIA-specific hardcoding)

### Effort

- **Time**: 0.5 hours
- **Files**: 3 (schemas.ts + 2 updates)
- **Lines**: ~80 lines added, 19 lines changed
- **Risk**: LOW (refactor strings, tests validate)

### Validation

```bash
# Run tests with custom schema
SCHEMA_CORE=test_keter_core npm test

# Verify all 19 references updated
grep -r "ayin_config\|keter_core\|shared_kg" --include="*.ts" packages/keter/core packages/keter/mcp
# Should return 0 matches (all replaced by SCHEMAS.*)
```

---

## 🔧 Refactoring 2: Fix Circular Dependency

### Problem

**From Task 2.1**: Madge detected circular dependency:
```
core/interfaces/IPolicyEngine.ts ↔ core/types.ts
```

**Issue**:
- `IPolicyEngine.ts` imports types from `types.ts`
- `types.ts` re-exports or uses `IPolicyEngine`
- Creates circular reference (TypeScript allows, but bad practice)

### Solution

Extract shared domain types to `core/domain/types.ts`:

```typescript
/**
 * Domain Types
 *
 * Core business entities and value objects.
 * These types are shared across interfaces, services, and repositories.
 * NO imports from other modules (leaf node in dependency graph).
 */

export interface Policy {
  id: string;
  name: string;
  description: string;
  rules: Rule[];
  version: number;
  status: 'draft' | 'active' | 'deprecated';
  created_at: string;
  updated_at: string;
  metadata?: Record<string, any>;
}

export interface Rule {
  id: string;
  condition: string;
  action: string;
  priority: number;
}

export interface EvaluationInput {
  policyId: string;
  context: Record<string, any>;
  timestamp?: string;
}

export interface EvaluationResult {
  allowed: boolean;
  matchedRules: string[];
  reason?: string;
  metadata?: Record<string, any>;
}

export interface Decree {
  id: string;
  decree_number: string;
  title: string;
  content: string;
  status: 'draft' | 'active' | 'deprecated';
  blockchain_hash?: string;
  created_at: string;
  updated_at: string;
  metadata?: Record<string, any>;
}

// ... other domain types
```

### Changes Required

**File 1**: Create `core/domain/types.ts` (new file)

**File 2**: Update `core/interfaces/IPolicyEngine.ts`
```typescript
// BEFORE
import type { Policy, EvaluationInput, EvaluationResult } from '../types';

// AFTER
import type { Policy, EvaluationInput, EvaluationResult } from '../domain/types';
```

**File 3**: Update `core/types.ts` to re-export
```typescript
// core/types.ts becomes a barrel export
export * from './domain/types';
export * from './interfaces/IPolicyEngine';
export * from './interfaces/IPolicyRepository';
// ... other interface re-exports
```

**File 4**: Update `core/repositories/MockDecreeRepository.ts`
```typescript
// BEFORE (also fixes Refactoring 3)
import type { Decree } from '../../mcp/tools/decree-query.schema.js';

// AFTER
import type { Decree } from '../domain/types';
```

### Benefits

- ✅ Breaks circular dependency
- ✅ Domain types in single location
- ✅ Leaf node (0 dependencies)
- ✅ Clear separation of concerns

### Effort

- **Time**: 0.5 hours
- **Files**: 4 (1 new + 3 updates)
- **Lines**: ~100 lines new, 10 lines changed
- **Risk**: LOW (type-only refactor)

### Validation

```bash
madge --circular --extensions ts packages/keter/core packages/keter/mcp
# Should return 0 circular dependencies
```

---

## 🔧 Refactoring 3: Move Decree Type to Core

### Problem

**From Task 2.1**: Core depends on MCP (violates layer architecture)
```typescript
// core/repositories/MockDecreeRepository.ts
import type { Decree } from '../../mcp/tools/decree-query.schema.js';
```

**Issue**: Domain layer (core) should NOT depend on application layer (mcp)

### Solution

Move `Decree` type to `core/domain/types.ts` (done in Refactoring 2)

### Changes Required

**File 1**: `core/domain/types.ts` (already created in Refactoring 2)
```typescript
export interface Decree {
  id: string;
  decree_number: string;
  title: string;
  content: string;
  status: 'draft' | 'active' | 'deprecated';
  blockchain_hash?: string;
  created_at: string;
  updated_at: string;
  metadata?: Record<string, any>;
}
```

**File 2**: Update `mcp/tools/decree-query.schema.ts`
```typescript
// BEFORE
export const DecreeSchema = z.object({
  id: z.string(),
  decree_number: z.string(),
  // ... field definitions
});

export type Decree = z.infer<typeof DecreeSchema>;

// AFTER
import type { Decree } from '../../../core/domain/types';

export const DecreeSchema = z.object({
  id: z.string(),
  decree_number: z.string(),
  // ... field definitions
}) satisfies z.ZodType<Decree>; // Validate schema matches Decree type
```

**File 3**: Update `core/repositories/MockDecreeRepository.ts`
```typescript
// BEFORE
import type { Decree } from '../../mcp/tools/decree-query.schema.js';

// AFTER
import type { Decree } from '../domain/types';
```

### Benefits

- ✅ Fixes layer violation (core no longer depends on mcp)
- ✅ Domain types in core (correct location)
- ✅ MCP schema validates against domain type (type safety)
- ✅ Clean architecture (dependencies point inward)

### Effort

- **Time**: 1 hour
- **Files**: 3 (1 shared with Refactoring 2)
- **Lines**: ~20 lines changed
- **Risk**: LOW (type-only, tests validate)

### Validation

```bash
# Verify no imports from mcp to core
grep -r "from '../../mcp" packages/keter/core
# Should return 0 matches

# Verify tests pass
npm test
```

---

## 🔧 Refactoring 4: Template Paths → Config

### Problem

**From RQ1**: Templates located at hardcoded path
```typescript
// scripts/generate-l0-contracts-v2.js
const templatesDir = './templates/instances/l0';
```

**Issue**: Hardcoded paths break when keter moves to melquisedec

### Solution

Create `core/config/paths.ts`:

```typescript
/**
 * Path Configuration
 *
 * Centralizes all file system paths for portability.
 * Override via environment variables or pass to functions.
 */

import path from 'path';

/**
 * Root directory (package root)
 * Defaults to this file's grandparent directory
 */
const ROOT_DIR = process.env.KETER_ROOT_DIR || path.resolve(__dirname, '../..');

/**
 * Template directories
 */
export const PATHS = {
  /** Root directory of keter package */
  root: ROOT_DIR,

  /** Templates directory */
  templates: path.join(ROOT_DIR, 'templates'),

  /** L0 product templates */
  templatesL0: path.join(ROOT_DIR, 'templates', 'instances', 'l0'),

  /** Scripts directory */
  scripts: path.join(ROOT_DIR, 'scripts'),

  /** Output directory for generated contracts */
  output: path.join(ROOT_DIR, 'output'),
} as const;

/**
 * Utility: Resolve path relative to keter root
 * @example resolve('templates/instances/l0') → '/path/to/keter/templates/instances/l0'
 */
export function resolve(...segments: string[]): string {
  return path.join(PATHS.root, ...segments);
}
```

### Changes Required

**File 1**: Create `core/config/paths.ts` (new file)

**File 2**: Update `scripts/generate-l0-contracts-v2.js`
```javascript
// BEFORE
const fs = require('fs');
const path = require('path');
const templatesDir = './templates/instances/l0';
const files = fs.readdirSync(templatesDir);

// AFTER
const fs = require('fs');
const { PATHS } = require('../packages/keter/core/config/paths');
const files = fs.readdirSync(PATHS.templatesL0);
```

**File 3**: Update `package.json` scripts
```json
{
  "scripts": {
    "list": "node -e \"const fs=require('fs'); const { PATHS }=require('./packages/keter/core/config/paths'); console.log('L0 Products:', fs.readdirSync(PATHS.templatesL0).filter(f=>f.endsWith('.yaml')).length)\""
  }
}
```

### .env.example Update

```bash
# === Path Configuration ===
# Override root directory if keter moves
KETER_ROOT_DIR=/path/to/melquisedec/packages/keter  # Optional
```

### Benefits

- ✅ Portable paths (no hardcoded './templates')
- ✅ Works when moved to melquisedec
- ✅ Environment override for custom deployments
- ✅ Single source of truth for paths

### Effort

- **Time**: 0.5 hours
- **Files**: 3 (1 new + 2 updates)
- **Lines**: ~40 lines new, 5 lines changed
- **Risk**: LOW (path resolution)

### Validation

```bash
# Test scripts still work
npm run generate-l0
npm run list
npm run stats

# Verify paths resolve correctly
node -e "const { PATHS } = require('./packages/keter/core/config/paths'); console.log(PATHS)"
```

---

## 📊 Summary Matrix

| Refactoring | Problem | Solution | Effort | Risk | Priority |
|-------------|---------|----------|--------|------|----------|
| **1. Schema Names** | 19 hardcoded strings | config/schemas.ts | 0.5h | LOW | HIGH |
| **2. Circular Dep** | IPolicyEngine ↔ types.ts | domain/types.ts | 0.5h | LOW | MEDIUM |
| **3. Type Import** | Core depends on MCP | Move Decree to core | 1h | LOW | HIGH |
| **4. Template Paths** | Hardcoded './templates' | config/paths.ts | 0.5h | LOW | MEDIUM |
| **TOTAL** | | | **2.5h** | **LOW** | |

---

## 🎯 Implementation Order

### Phase 1: Domain Types (1 hour)
1. Create `core/domain/types.ts` (Refactoring 2 + 3)
   - Extract Policy, Decree, EvaluationInput, etc.
2. Update all imports to use `../domain/types`
3. Verify: `madge --circular` returns 0

### Phase 2: Config Modules (1 hour)
1. Create `core/config/schemas.ts` (Refactoring 1)
   - Add SCHEMAS config with env overrides
2. Create `core/config/paths.ts` (Refactoring 4)
   - Add PATHS config with root directory
3. Update .env.example

### Phase 3: Update Consumers (0.5 hours)
1. Replace 19 schema string references
2. Update 2 script files for paths
3. Update package.json scripts

### Phase 4: Validation (0.1 hours)
1. Run madge --circular (expect 0)
2. Run npm test (expect 131/131 pass)
3. Run npm run generate-l0 (expect success)
4. Grep for remaining hardcoded refs (expect 0)

---

## ✅ Expected Outcomes

After these 4 minimal refactorings:

1. **Zero hardcoded dependencies** ✅
   - No schema name strings
   - No hardcoded paths
   - No circular dependencies
   - No layer violations

2. **Fully config-driven** ✅
   - SCHEMAS from env
   - PATHS from env
   - DB_MODE from env (already exists)
   - Blockchain config from env (already exists)

3. **Clean architecture** ✅
   - Domain types in core/domain/
   - Config in core/config/
   - Interfaces in core/interfaces/
   - MCP depends on core (not vice versa)

4. **Migration-ready** ✅
   - Move packages/keter → melquisedec/packages/keter
   - Update KETER_ROOT_DIR env var
   - Update imports (../.. → relative)
   - Done! ✅

---

## 🔍 Alternatives Considered

### Alternative 1: Skip Refactorings, Move As-Is

**Pros**: Zero effort
**Cons**:
- 19 schema strings remain ALEIA-specific
- Circular dependency persists
- Layer violation remains
- Hardcoded paths break

**Decision**: ❌ Rejected (technical debt)

### Alternative 2: Major Refactoring (All Mock→Real Repos)

**Pros**: Production-ready
**Cons**: 3+ days effort, NOT needed for migration

**Decision**: ❌ Deferred to post-migration (RQ4)

### Alternative 3: Consolidate All Config (21 env vars → 1 module)

**Pros**: Single config module
**Cons**: 1 day effort vs 0.5 hours

**Decision**: ⚠️ Partial (do schemas + paths now, defer full consolidation to Task 2.4)

---

## 📝 Validation Checklist

After completing all 4 refactorings:

- [ ] **Circular dependency fixed**
  ```bash
  madge --circular --extensions ts packages/keter/core packages/keter/mcp
  # Expect: ✓ No circular dependency found!
  ```

- [ ] **No hardcoded schema names**
  ```bash
  grep -r "'ayin_config'\|'keter_core'\|'shared_kg'" --include="*.ts" packages/keter
  # Expect: 0 matches
  ```

- [ ] **No core→mcp imports**
  ```bash
  grep -r "from '../../mcp" packages/keter/core
  # Expect: 0 matches
  ```

- [ ] **No hardcoded template paths**
  ```bash
  grep -r "./templates" scripts/ --include="*.js"
  # Expect: 0 matches
  ```

- [ ] **Tests pass**
  ```bash
  npm test
  # Expect: 131/131 tests passing
  ```

- [ ] **Scripts work**
  ```bash
  npm run generate-l0
  npm run list
  # Expect: No errors
  ```

---

**Architect**: SALOMON
**Status**: ✅ Task 2.2 COMPLETE
**Next**: Task 2.3 (Validate No External Abstractions Needed)
**Total Refactoring Effort**: 2.5 hours
