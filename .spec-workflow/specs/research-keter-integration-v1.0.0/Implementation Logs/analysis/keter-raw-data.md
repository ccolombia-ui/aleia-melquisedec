# Keter Raw Data
**Date**: 2026-01-08
**Source**: [REPO:aleia-bereshit] C:\proyectos\aleia-bereshit\apps\keter
**Status**: Read-only access completed

---

## 1. Project Overview

**Name**: `@aleia/keter`
**Version**: 1.0.0
**Description**: Policy Engine & Backend Unificado para ALEIA-BERESHIT
**License**: MIT
**Author**: BERESHIT Team

**Hebrew Etymology**: כֶּתֶר (Keter) - "Corona"
**Role**: "QUÉ se permite" + Backend Multi-Tenant (VSM S5 Identidad)

---

## 2. Project Structure (High-Level)

```
keter/
├── packages/keter/            # Core package
│   ├── core/                  # Core business logic
│   │   ├── config/            # Blockchain config
│   │   ├── context/           # Tenant context management
│   │   ├── database/          # Database adapters
│   │   ├── interfaces/        # Core interfaces (IAuditLogger, IBlockchainService, etc.)
│   │   ├── repositories/      # Mock implementations
│   │   └── services/          # 15+ services (PolicyEngine, SemanticIndex, etc.)
│   ├── database/migrations/   # SQL migrations
│   ├── mcp/                   # MCP Server implementation
│   │   ├── server/            # keter-mcp-server.ts
│   │   ├── tools/             # 20+ MCP tools (decree-*, policy-*, bulk-operations)
│   │   └── performance/       # cache-manager.ts
│   ├── mcp-server/handlers/   # Validity handlers
│   ├── scripts/               # Utility scripts
│   ├── services/              # Additional services
│   └── tests/                 # 40+ test files (131 tests total)
├── scripts/                   # Top-level utility scripts
├── src/                       # Frontend/CLI source
│   ├── app/                   # Next.js app (4 pages: concepto, estandares, ontologia, plantillas)
│   ├── bin/                   # CLI (cli.ts)
│   ├── components/editor/     # Plate editor components
│   ├── core/                  # Core types and engine
│   ├── lib/                   # MDX serialization
│   ├── policies/              # Example policies (appointments, payments)
│   └── templates/             # YAML templates (productos, base, instances)
├── supabase/                  # Supabase config + 6 migrations
│   ├── migrations/            # 6 migration files
│   └── seed/                  # Seed data (tenants, mini_apps, knowledge_graphs)
├── templates/instances/       # Policy instances (TB Resolver + 87 L0 products)
└── tests/                     # Integration tests (ayin, geospatial, RLS)
```

---

## 3. Dependencies (package.json)

```json
{
  "dependencies": {
    "yaml": "^2.3.4"
  },
  "scripts": {
    "validate": "node scripts/validate-contracts.js",
    "generate-l0": "node scripts/generate-l0-contracts-v2.js",
    "generate-l0-legacy": "node scripts/generate-l0-contracts.js",
    "list": "[counts contracts]",
    "stats": "[shows L0 products by category]"
  },
  "keywords": ["policy", "opa", "rego", "keter", "validation"]
}
```

**Note**: Package.json is minimal (only `yaml` dependency), suggesting keter is part of a larger monorepo with dependencies managed at workspace level.

---

## 4. Purpose & Architecture

### Primary Responsibilities

1. **Policy Engine**: Define and evaluate declarative authorization rules
2. **Backend Unificado**: Supabase multi-tenant with scope-based access (global/vertical/tenant)

### Architecture Flow

```
KETER ──defines──▶ DAATH ──validates──▶ YESOD
  │                  │                    │
  ▼                  ▼                    ▼
Políticas       Knowledge Graph       Contratos
(Reglas)           (Neo4j)              (Zod)
  │
  └──stores in──▶ Supabase (PostgreSQL)
                      │
                      ├── keter_core (policies, decrees)
                      ├── ayin_config (view_configs, mini_apps)
                      └── shared_kg (knowledge_graphs, docs)
```

### Schemas Multi-Tenant

- **shared**: Tenant isolation base (tenants, users, user_tenants)
- **keter_core**: Policies and norms (policies, decrees, approvals)
- **ayin_config**: View + mini-apps (view_configs, dashboards, mini_apps with scope)
- **shared_kg**: Knowledge graphs (knowledge_graphs, standard_documents)

---

## 5. Quality Metrics (Certified by SonarQube)

- ✅ **Coverage**: 92.94% (>90% required)
- ✅ **Tests**: 131/131 passing (100%)
- ✅ **Bugs**: 0
- ✅ **Vulnerabilities**: 0
- ✅ **Security**: A+

**Quality Gate**: PASSED

---

## 6. MCP Server Implementation

Keter includes a full MCP (Model Context Protocol) server with:

**Tools** (20+ tools):
- `decree-create`, `decree-update`, `decree-delete`, `decree-list`, `decree-query`
- `decree-list-versions`, `decree-restore`
- `policy-create`, `policy-update`, `policy-delete`, `policy-list`, `policy-validate`, `policy-export`
- `bulk-operations` (batch processing)
- `keter-cmis-records-tools` (CMIS integration)

**Handlers**:
- Validity management: check, extend, find expiring, set validity
- Cache management for performance optimization

---

## 7. Core Services (15+ services)

Located in `packages/keter/core/services/`:
- **BlockchainService.ts**: Blockchain integration
- **CMISRepository.ts**: Content Management Interoperability Services
- **ConflictDetector.ts**: Policy conflict detection
- **DeprecationEngine.ts**: Policy deprecation management
- **DocumentEmbedder.ts**: Document embedding for semantic search
- **HealthMonitor.ts**: System health monitoring
- **LifecycleManager.ts**: Policy lifecycle management
- **PolicyEngine.ts**: Core policy evaluation engine
- **PolicyValidator.ts**: Policy validation
- **RecordsManager.ts**: Records management
- **RuleLearner.ts**: Machine learning for rule extraction
- **SemanticAPI.ts**: Semantic query interface
- **SemanticIndex.ts**: Semantic indexing
- **ValidityManager.ts**: Document validity management
- **VersionManager.ts**: Version control

---

## 8. Integration Points

### Database
- **Supabase** (PostgreSQL): Primary datastore with 4 schemas
- **Migrations**: 6 migration files in `supabase/migrations/`
- **Seed Data**: Multi-tenant seed (5 tenants, 7 mini-apps, 5 KGs)

### Knowledge Graph
- **Neo4j**: Referenced in architecture (DAATH validates via Neo4j)
- **shared_kg schema**: Stores knowledge graph metadata

### Blockchain
- **BlockchainService**: Integration with blockchain for audit trail
- Config: `packages/keter/core/config/blockchain.config.ts`

### Frontend
- **Next.js App**: 4 pages (concepto, estandares, ontologia, plantillas)
- **Plate Editor**: Rich text editor with MDX serialization

---

## 9. Testing Strategy

**Test Count**: 131 tests across 40+ test files

**Coverage**: 92.94%

**Test Types**:
1. **Unit Tests**:
   - `packages/keter/tests/unit/` (policy-engine, services)
   - Mock repositories for isolated testing
2. **MCP Tests**:
   - 20+ files testing each MCP tool (decree-*, policy-*)
   - E2E workflows test
   - Integration test
3. **Integration Tests**:
   - `tests/integration/` (ayin-realtime, RLS, geospatial)
   - Supabase integration
4. **Service Tests**:
   - blockchain-service.test.ts
   - cache-manager.test.ts
   - tenant-context.test.ts

---

## 10. Documentation Available

From README.md mentions:
- `BOOTSTRAP_QUICKSTART.md` - Quick setup guide
- `AYIN_DATABASE_INTEGRATION.md` - Complete AYIN guide
- `MULTI_TENANT_IMPLEMENTATION_GUIDE.md` - Multi-tenant architecture
- `MVP_COMPLETION.md` - MVP status
- `../../docs/02-daath/CERTIFICATION_SUMMARY.md` - SonarQube certification

---

## 11. Key Observations

### Maturity Indicators
✅ **High Test Coverage**: 92.94% with 131 passing tests
✅ **Zero Bugs**: Clean codebase per SonarQube
✅ **Production-Ready Security**: A+ security rating
✅ **Comprehensive Documentation**: Multiple guides available
✅ **Structured Migrations**: 6 database migrations with seed data
✅ **MCP Implementation**: Full MCP server with 20+ tools

### Complexity Indicators
⚠️ **Multi-Concern Component**: Handles policy engine + backend + MCP server
⚠️ **Large Service Count**: 15+ core services
⚠️ **Multiple Integration Points**: Supabase, Neo4j, Blockchain, Next.js
⚠️ **Dual Frontend/Backend**: Both API services and Next.js pages

### Reusability Indicators
✅ **Well-Defined Interfaces**: IAuditLogger, IBlockchainService, IPolicyEngine, etc.
✅ **Mock Implementations**: Facilitates testing and pluggable architecture
✅ **MCP Standard**: Uses Model Context Protocol (industry standard)
⚠️ **Tight Coupling**: References to ALEIA-BERESHIT, DAATH, YESOD, AYIN (ecosystem-specific)

---

## 12. Stats Summary

| Metric | Value |
|--------|-------|
| **Total Files (estimate from tree)** | 500+ (including node_modules structure shown) |
| **Core TypeScript Files** | ~100+ (packages/keter + src/) |
| **Test Files** | 40+ |
| **Tests** | 131 |
| **MCP Tools** | 20+ |
| **Core Services** | 15+ |
| **Database Migrations** | 6 |
| **Database Schemas** | 4 (shared, keter_core, ayin_config, shared_kg) |
| **L0 Product Templates** | 87 (in templates/instances/l0/) |
| **Next.js Pages** | 4 (concepto, estandares, ontologia, plantillas) |
| **Dependencies (direct)** | 1 (yaml) - likely more at workspace level |
| **Test Coverage** | 92.94% |
| **Quality Gate** | PASSED ✅ |

---

## 13. Next Steps for Analysis

### For TASK-1.2 (Analyze Keter Structure):
1. Evaluate ComponentMetadata:
   - **Purpose**: Policy Engine + Backend Unificado
   - **Maturity**: High (92.94% coverage, 131 tests, certified)
   - **Reusability**: Medium-High (well-interfaced but ecosystem-coupled)
   - **Complexity**: High (multi-service, multi-integration)
   - **Independence**: Medium (part of ALEIA-BERESHIT ecosystem)

2. Generate Scorecard:
   - **Test Coverage**: 10/10 (92.94% > 90%)
   - **Documentation**: 9/10 (multiple guides, README)
   - **Architecture**: 8/10 (clear separation, well-structured)
   - **Dependencies**: 7/10 (minimal direct, ecosystem-coupled)
   - **Maintainability**: 9/10 (zero bugs, A+ security)

3. Identify Dependencies:
   - **Internal**: DAATH (validation), YESOD (contracts), AYIN (views)
   - **External**: Supabase, Neo4j, Blockchain
   - **Standards**: MCP (Model Context Protocol)

### For TASK-1.3 (Apply Decision Tree):
- Evaluate against 4 criteria: Purpose, Reusability, Independence, Nature
- Generate placement recommendation with confidence score
- Document rationale for each decision point

---

**End of Raw Data Collection**
**Status**: ✅ Complete - Ready for analysis phase
