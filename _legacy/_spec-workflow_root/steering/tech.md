# Technical Steering - monorepo-improvements-v1.1.0

## 📖 Referencias Técnicas (SSoT)

**Arquitectura del Monorepo**:
- **ADR-001 Monorepo Structure**: [[ADR-001-monorepo-structure]]
- **Arquitectura Visual**: [[ESTRUCTURA_VISUAL]]
- **Configuración Completa**: [[CONFIGURACION_COMPLETA]]

**MCPs y Tooling**:
- **MCPs Recomendados**: [[04-mcps-recomendados]]
- **Docker MCP Toolkit**: [[docker-mcp-toolkit]]
- **Workflows GitHub Actions**: [[workflows-github-actions]]

**Estrategia de Branching y Migración**:
- **Estrategia Branching**: [[estrategia-branching]]
- **Migración Estructura**: [[migracion-estructura]]

---

## 🛠️ Stack Técnico para este Spec

**Python**:
- Version: 3.10+
- Formatting: black + isort
- Linting: flake8
- Testing: pytest + pytest-cov
- Packaging: pyproject.toml (PEP 517/518)

**Pre-commit Hooks** (Task 1.3):
- trailing-whitespace, end-of-file-fixer
- check-yaml, check-json
- black, isort, flake8
- validate-doc-links.py (custom)

**Docker**:
- `infrastructure/docker/docker-compose.yml` para servicios
- Neo4j para knowledge graph (lessons)
- Redis para caché (opcional)

**Git Workflow**:
- Commits incrementales por task
- Mensajes siguiendo Conventional Commits
- git mv para preservar history (Task 1.2)
- Tag al finalizar: monorepo-improvements-v1.1.0
