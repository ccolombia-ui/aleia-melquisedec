# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-08

### Added
- **GitHub Actions Workflows**: 4 complete automation pipelines
  - CI/CD Pipeline: validation, security, tests, linting
  - Changelog Automation: auto-update on PR merge
  - Documentation Health Check: weekly validation + reports
  - Release Management: auto-create releases from tags
- **Branching Strategy**: Research-per-branch model documented
  - Each investigation = independent branch (`research/XX-nombre`)
  - Feature branches for infrastructure improvements
  - Hotfix branches for urgent corrections
- **Documentation Guides**:
  - `estrategia-branching.md`: Complete branching workflow
  - `workflows-github-actions.md`: Workflows explanation + "are they prompts?" analysis
  - `CONFIGURACION_COMPLETA.md`: Setup summary and next steps
- **Badges to README**: Release, Tests, Neo4j, Python, Conventional Commits

### Changed
- Enhanced `.gitignore`: Added Docker volumes, test apps pattern
- Upgraded CI workflow: 6 jobs (structure, docs, commits, branches, security, generators)

### Removed
- Test app `apps/01-test-reorganizacion/` after successful validation

### Infrastructure
- 4 GitHub Actions workflows totaling ~500 lines of automation
- Weekly scheduled documentation health checks (Mondays 9 AM)
- Automatic changelog updates on PR merge
- Security scanning for hardcoded credentials

---

## [1.0.0] - 2026-01-08

### Added
- Complete monorepo restructuring following professional best practices
- Modular architecture: `docs/`, `packages/`, `apps/`, `infrastructure/`, `tools/`
- Automated research generator (`new_research.py`)
- Structure validator (`validate_research.py`)
- Cleanup and maintenance scripts
- Comprehensive documentation suite (8 main documents)
- Docker MCP Toolkit integration with 19 servers
- Neo4j 5.15 + Ollama for knowledge graphs and embeddings
- CI/CD workflow preparation (GitHub Actions)
- ADR-001 for architectural decisions
- MIT License

### Changed
- Moved all documentation to centralized `docs/` directory
- Relocated MCP core components to `packages/core-mcp/`
- Reorganized scripts into categorized `tools/` directory
- Enhanced Docker Compose configuration in `infrastructure/docker/`
- Improved template structure in `apps/00-template/`
- Rewritten README.md with professional badges and structure

### Removed
- Old scattered structure (`bereshit/`, `nucleo-investigacion/`, `_templates/`)
- Redundant script locations

### Infrastructure
- Neo4j Community Edition 5.15 with APOC and GDS plugins
- Ollama for local embeddings (nomic-embed-text)
- Docker MCP Toolkit v0.28.0+
- Python 3.10+ environment

### Documentation
- README.md (main entry point)
- ARQUITECTURA_MONOREPO.md (complete architecture)
- REORGANIZACION_COMPLETA.md (reorganization summary)
- ESTRUCTURA_VISUAL.md (visual diagrams)
- QUICK_REFERENCE.md (quick commands)
- CONTRIBUTING.md (contribution guidelines)
- docs/architecture/ADR-001-monorepo-structure.md
- docs/guides/migracion-estructura.md
- docs/guides/docker-mcp-toolkit.md
- docs/guides/configuracion-completa.md

### Validation
- ✅ 100% MCP test success rate (16/19 active servers)
- ✅ Generator and validator fully tested
- ✅ All documentation cross-referenced
- ✅ Template structure validated

---

## [0.1.0] - 2026-01-07 (Pre-reorganization)

### Initial Setup
- Basic structure with `nucleo-investigacion/`
- Simple MCP configuration
- Manual research creation process
- Basic Docker setup for Neo4j

---

**Note**: This is the first official release after complete reorganization.
Future releases will follow semantic versioning.
