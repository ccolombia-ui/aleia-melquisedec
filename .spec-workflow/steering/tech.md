# Technical Steering - monorepo-improvements-v1.1.0

## 📖 Referencias Técnicas (SSoT)

**Arquitectura del Monorepo**:
- **ADR-001 Monorepo Structure**: [docs/architecture/ADR-001-monorepo-structure.md](../../docs/architecture/ADR-001-monorepo-structure.md)
- **Arquitectura Visual**: [docs/architecture/estructura-visual.md](../../docs/architecture/estructura-visual.md)
- **Configuración Completa**: [docs/guides/CONFIGURACION_COMPLETA.md](../../docs/guides/CONFIGURACION_COMPLETA.md)

**MCPs y Tooling**:
- **MCPs Recomendados**: [docs/manifiesto/03-workflow/04-mcps-recomendados.md](../../docs/manifiesto/03-workflow/04-mcps-recomendados.md)
- **Docker MCP Toolkit**: [docs/guides/docker-mcp-toolkit.md](../../docs/guides/docker-mcp-toolkit.md)
- **Workflows GitHub Actions**: [docs/guides/workflows-github-actions.md](../../docs/guides/workflows-github-actions.md)

**Estrategia de Branching y Migración**:
- **Estrategia Branching**: [docs/guides/estrategia-branching.md](../../docs/guides/estrategia-branching.md)
- **Migración Estructura**: [docs/guides/migracion-estructura.md](../../docs/guides/migracion-estructura.md)

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
