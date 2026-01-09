# Policy Engine Extraction Plan
**Parent**: research-keter-integration-v1.0.0
**Target**: `packages/policy-engine/`
**Source**: [REPO:aleia-bereshit] `apps/keter/packages/keter/core/`
**Status**: Planning
**Priority**: P1

---

## 1. Executive Summary

Extraer el patrón de Policy Engine de Keter como package independiente y reutilizable en MELQUISEDEC. El objetivo es abstraer las interfaces y lógica core de evaluación de políticas, dejando la implementación específica de ALEIA en bereshit.

**Timeline**: 2-3 días (Sprint 3)
**Confidence**: 80%
**Risk Level**: Medium (requiere abstracción cuidadosa)

---

## 2. Scope Definition

### 2.1 In Scope ✅

**Core Interfaces** (de `keter/core/interfaces/`):
```typescript
interface IPolicyEngine {
  evaluate(context: PolicyContext): Promise<Decision>;
  validatePolicy(policy: Policy): ValidationResult;
}

interface IValidator {
  validate(policy: Policy): ValidationResult;
  validateSyntax(policy: Policy): SyntaxResult;
}

interface IConflictDetector {
  detectConflicts(policies: Policy[]): Conflict[];
  resolveConflicts(conflicts: Conflict[]): Resolution;
}

interface IDeprecationEngine {
  markDeprecated(policy: Policy, reason: string): void;
  findDeprecated(criteria: DeprecationCriteria): Policy[];
}

interface IVersionManager {
  createVersion(policy: Policy): Version;
  getVersionHistory(policyId: string): Version[];
  rollback(policyId: string, version: number): Promise<Policy>;
}

interface ILifecycleManager {
  transition(policy: Policy, newState: PolicyState): Promise<void>;
  getState(policyId: string): PolicyState;
}
```

**Core Services** (abstraídos de `keter/core/services/`):
- `PolicyEngine.ts` - Core evaluation engine
- `PolicyValidator.ts` - Policy validation logic
- `ConflictDetector.ts` - Conflict detection algorithms
- `DeprecationEngine.ts` - Deprecation management
- `VersionManager.ts` - Version control logic
- `LifecycleManager.ts` - State transitions

**Test Patterns** (de `keter/tests/unit/`):
- Mock implementations pattern
- Test fixtures structure
- Coverage target: >90% (matching keter quality)

### 2.2 Out of Scope ❌

**ALEIA-Specific**:
- ❌ Supabase storage implementation
- ❌ DAATH knowledge graph validation
- ❌ YESOD contract integration
- ❌ L0 product templates
- ❌ Decree-specific logic
- ❌ Multi-tenant schemas

**Infrastructure**:
- ❌ MCP server (separate template)
- ❌ Frontend (Next.js pages)
- ❌ Blockchain service
- ❌ SemanticIndex (Neo4j specific)

---

## 3. Architecture Design

### 3.1 Package Structure

```
packages/policy-engine/
├── src/
│   ├── interfaces/
│   │   ├── IPolicyEngine.ts
│   │   ├── IValidator.ts
│   │   ├── IConflictDetector.ts
│   │   ├── IDeprecationEngine.ts
│   │   ├── IVersionManager.ts
│   │   └── ILifecycleManager.ts
│   ├── core/
│   │   ├── PolicyEngine.ts
│   │   ├── PolicyValidator.ts
│   │   ├── ConflictDetector.ts
│   │   └── types.ts
│   ├── lifecycle/
│   │   ├── DeprecationEngine.ts
│   │   ├── VersionManager.ts
│   │   └── LifecycleManager.ts
│   ├── storage/
│   │   └── IStorageAdapter.ts    # Abstract adapter pattern
│   └── index.ts
├── tests/
│   ├── unit/
│   │   ├── PolicyEngine.test.ts
│   │   ├── ConflictDetector.test.ts
│   │   └── mocks/
│   │       └── MockStorage.ts
│   └── integration/
│       └── end-to-end.test.ts
├── examples/
│   └── simple-policy-system.ts
├── README.md
├── CHANGELOG.md
├── package.json
└── tsconfig.json
```

### 3.2 Abstraction Strategy

**Storage Abstraction**:
```typescript
// src/storage/IStorageAdapter.ts
export interface IStorageAdapter {
  save(policy: Policy): Promise<void>;
  load(policyId: string): Promise<Policy>;
  delete(policyId: string): Promise<void>;
  query(criteria: QueryCriteria): Promise<Policy[]>;
}

// Implementation examples (not in package):
// - SupabaseStorageAdapter (stays in keter)
// - InMemoryStorageAdapter (for testing)
// - FileSystemStorageAdapter (for simple use cases)
```

**Configuration Injection**:
```typescript
// src/core/PolicyEngine.ts
export class PolicyEngine implements IPolicyEngine {
  constructor(
    private storage: IStorageAdapter,
    private validator: IValidator,
    private conflictDetector: IConflictDetector,
    private config: PolicyEngineConfig = defaultConfig
  ) {}

  async evaluate(context: PolicyContext): Promise<Decision> {
    // Generic evaluation logic (no ALEIA specifics)
  }
}
```

---

## 4. Migration Steps

### Phase 1: Setup (1 hour)
1. Create `packages/policy-engine/` directory structure
2. Initialize `package.json` with dependencies
3. Setup `tsconfig.json` (strict mode)
4. Configure test framework (vitest or jest)

### Phase 2: Interface Extraction (2 hours)
1. Copy interfaces from `keter/core/interfaces/`
2. Remove ALEIA-specific types (keep generic)
3. Add JSDoc documentation
4. Review for backward compatibility

### Phase 3: Core Logic Extraction (1 day)
1. Copy core service files:
   - PolicyEngine.ts
   - PolicyValidator.ts
   - ConflictDetector.ts
2. Replace concrete dependencies with interfaces:
   ```typescript
   // Before (in keter)
   import { SupabaseClient } from '@supabase/supabase-js';
   private supabase: SupabaseClient;

   // After (in package)
   import { IStorageAdapter } from '../storage';
   private storage: IStorageAdapter;
   ```
3. Remove DAATH/YESOD integrations
4. Make configuration injectable

### Phase 4: Lifecycle Extraction (4 hours)
1. Copy lifecycle services:
   - DeprecationEngine.ts
   - VersionManager.ts
   - LifecycleManager.ts
2. Abstract storage calls
3. Remove tenant-specific logic

### Phase 5: Testing (1 day)
1. Port test structure from keter
2. Create MockStorageAdapter
3. Write unit tests for each service (target >90% coverage)
4. Create integration test example
5. Run test suite and fix issues

### Phase 6: Documentation (4 hours)
1. Write comprehensive README:
   - Installation
   - Quick start
   - API reference
   - Examples
   - Reference to keter as production impl
2. Add inline JSDoc for all public APIs
3. Create example usage file
4. Write CHANGELOG.md

---

## 5. Dependencies

### 5.1 Runtime Dependencies (Minimal)
```json
{
  "dependencies": {
    "zod": "^3.22.0"  // For schema validation (already in keter)
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "vitest": "^1.0.0",
    "@types/node": "^20.0.0"
  }
}
```

### 5.2 Peer Dependencies (Optional)
```json
{
  "peerDependencies": {
    "@supabase/supabase-js": "^2.0.0"  // If user wants SupabaseAdapter example
  },
  "peerDependenciesMeta": {
    "@supabase/supabase-js": {
      "optional": true
    }
  }
}
```

---

## 6. Testing Strategy

### 6.1 Coverage Targets
- **Overall**: >90% (matching keter quality)
- **Core Logic**: >95%
- **Interfaces**: 100%

### 6.2 Test Structure
```typescript
// tests/unit/PolicyEngine.test.ts
describe('PolicyEngine', () => {
  let engine: PolicyEngine;
  let mockStorage: MockStorageAdapter;

  beforeEach(() => {
    mockStorage = new MockStorageAdapter();
    engine = new PolicyEngine(
      mockStorage,
      new PolicyValidator(),
      new ConflictDetector()
    );
  });

  describe('evaluate', () => {
    it('should evaluate simple policy', async () => {
      // Test case from keter adapted
    });

    it('should handle conflicts', async () => {
      // Conflict detection test
    });
  });
});
```

### 6.3 Integration Tests
```typescript
// tests/integration/end-to-end.test.ts
describe('Policy Engine E2E', () => {
  it('should handle full policy lifecycle', async () => {
    const storage = new InMemoryStorageAdapter();
    const engine = createPolicyEngine({ storage });

    // 1. Create policy
    const policy = await engine.createPolicy({ ... });

    // 2. Validate
    const validation = await engine.validatePolicy(policy);

    // 3. Evaluate
    const decision = await engine.evaluate({ policy, context: {} });

    // 4. Deprecate
    await engine.markDeprecated(policy.id, 'outdated');

    expect(decision.allowed).toBe(true);
  });
});
```

---

## 7. Documentation Outline

### README.md Structure
```markdown
# @melquisedec/policy-engine

Generic policy evaluation engine with lifecycle management.

## Features
- Declarative policy evaluation
- Conflict detection
- Version management
- Deprecation handling
- Storage adapter pattern

## Installation
\`\`\`bash
npm install @melquisedec/policy-engine
\`\`\`

## Quick Start
\`\`\`typescript
import { PolicyEngine, InMemoryStorageAdapter } from '@melquisedec/policy-engine';

const storage = new InMemoryStorageAdapter();
const engine = new PolicyEngine(storage);

const decision = await engine.evaluate({
  policy: myPolicy,
  context: { user: 'alice' }
});
\`\`\`

## API Reference
[Generated from interfaces]

## Storage Adapters
- InMemoryStorageAdapter (included)
- FileSystemStorageAdapter (example)
- Custom adapters: implement IStorageAdapter

## Examples
See examples/ directory

## Reference Implementation
This package is abstracted from @aleia/keter (production system).
See: [REPO:aleia-bereshit] apps/keter/

## Contributing
[CONTRIBUTING.md]

## License
MIT
```

---

## 8. Success Criteria

### 8.1 Functional
- [ ] All interfaces extracted and documented
- [ ] Core services work without ALEIA dependencies
- [ ] Storage adapter pattern allows pluggable backends
- [ ] Test coverage >90%
- [ ] Zero TypeScript errors

### 8.2 Quality
- [ ] No hard-coded ALEIA references (DAATH, YESOD, decree, etc.)
- [ ] Clean dependency injection
- [ ] Comprehensive JSDoc on public APIs
- [ ] README with clear examples

### 8.3 Validation
- [ ] Can install package in fresh project
- [ ] Example code runs without errors
- [ ] Mock storage adapter works in tests
- [ ] Lint and format pass

---

## 9. Rollback Plan

If extraction proves too complex:

**Plan B**: Document pattern only
- Create ADR documenting policy engine pattern
- Reference keter as implementation
- Provide architectural guidance instead of code package

**Trigger**: If >4 days effort or <80% coverage achieved

---

## 10. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Over-abstraction (too generic) | 30% | Medium | Keep keter tests as validation suite |
| Missing edge cases | 40% | Medium | Port full keter test suite patterns |
| Breaking changes to keter | 10% | Low | Read-only extraction, no modification |
| Insufficient documentation | 20% | Medium | Allocate 4 hours for docs explicitly |

---

## 11. Post-Extraction

### 11.1 Maintenance
- **Owner**: Framework team
- **Sync with keter**: Quarterly reviews
- **Versioning**: Semantic versioning (start at 0.1.0)

### 11.2 Future Enhancements
- [ ] Add GraphQL policy format support
- [ ] Add YAML policy parser
- [ ] Add policy migration tools
- [ ] Performance benchmarks

---

## 12. References

- **Source Code**: [REPO:aleia-bereshit] `apps/keter/packages/keter/core/`
- **Test Suite**: [REPO:aleia-bereshit] `apps/keter/tests/unit/`
- **ADR-002**: [ADR-002-keter-integration-decision.md](../architecture/ADR-002-keter-integration-decision.md)
- **Keter Evaluation**: `.spec-workflow/specs/research-keter-integration-v1.0.0/Implementation Logs/analysis/keter-evaluation.md`

---

**End of Extraction Plan**
**Status**: ✅ Ready for Sprint 3 execution
**Estimated Duration**: 2-3 días
**Next**: MCP Server Template extraction plan
