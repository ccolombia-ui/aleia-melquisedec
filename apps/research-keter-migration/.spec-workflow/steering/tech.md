# Tech Steering - Research Keter Migration

> **Stack Principal**: Python 3.11+ | TypeScript 5.x | Neo4j 5.x
> **Testing**: pytest + TDD obligatorio
> **CI/CD**: GitHub Actions

## 🏗️ Stack Tecnológico

### Backend (Python)
```yaml
runtime: python >= 3.11
frameworks:
  - FastAPI (async HTTP)
  - Pydantic v2 (validation)
  - SQLAlchemy 2.0 (ORM)
testing:
  - pytest >= 8.0
  - pytest-cov >= 4.0
  - pytest-asyncio
quality:
  - ruff (linting)
  - mypy (type checking)
  - coverage >= 92%
```

### Frontend (TypeScript)
```yaml
runtime: node >= 20
frameworks:
  - Next.js 14 (App Router)
  - React 18
  - TypeScript 5.x
testing:
  - vitest
  - @testing-library/react
```

### Databases
```yaml
primary:
  - Supabase (PostgreSQL)
  - 4 schemas: public, keter, templates, audit
graph:
  - Neo4j 5.x
  - Cypher queries
blockchain:
  - Integration via Policy Engine
```

## 📐 Patrones Arquitectónicos

### Obligatorios
- **Hexagonal Architecture**: Ports & Adapters
- **Dependency Injection**: Configuración externa
- **Repository Pattern**: Abstracción de storage
- **CQRS**: Separación read/write donde aplique

### Prohibidos
- ❌ Hardcoded imports entre paquetes
- ❌ Dependencias circulares
- ❌ God classes (>300 líneas)
- ❌ Tests sin assertions

## 🧪 Testing Strategy

```
Unit Tests (70%)
├── Cada función pública
├── Edge cases
└── Mocks para deps externas

Integration Tests (20%)
├── API endpoints
├── Database operations
└── Service interactions

E2E Tests (10%)
├── Critical user flows
└── Regression suite
```

### TDD Workflow
```
1. RED   → Escribir test que falla
2. GREEN → Mínimo código para pasar
3. REFACTOR → Mejorar sin romper tests
```

## 🔌 Interfaces Requeridas (Ports)

| Port | Propósito | Implementación Actual |
|------|-----------|----------------------|
| `IKnowledgeGraph` | Acceso a DAATH/KG | Neo4j adapter |
| `ISchemaRegistry` | Schemas YESOD | Supabase adapter |
| `IConfigProvider` | Config AYIN | Environment adapter |
| `ITemplateEngine` | Templates L0 | JSON loader |
| `IPolicyEngine` | Business rules | Keter core |
| `IAuditLogger` | Audit trail | Supabase audit schema |
| `IBlockchain` | Integrity proofs | Blockchain adapter |
| `ITenantManager` | Multi-tenancy | Supabase tenant schema |

## 🚀 CI/CD Requirements

```yaml
on: [push, pull_request]
jobs:
  test:
    - lint (ruff)
    - type-check (mypy)
    - unit-tests (pytest)
    - coverage-check (>= 92%)

  build:
    - docker build
    - security scan

  deploy:
    - staging (auto on main)
    - production (manual approval)
```

## 🔗 Referencias

- [Python Best Practices](../../docs/guides/python-standards.md)
- [Testing Guide](../../docs/guides/testing-guide.md)
