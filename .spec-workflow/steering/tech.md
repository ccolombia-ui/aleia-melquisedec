# Technical Steering - Monorepo Stack

## 🏗️ Arquitectura General

```
aleia-melquisedec/
├── apps/                    # Research applications (one per domain/instance)
├── packages/                # Shared Python packages
│   ├── core-mcp/           # MCP server para interacción con Claude/GPT
│   └── daath-toolkit/      # Toolkit de captura y almacenamiento
├── docs/                    # Documentación organizada por tipo
│   ├── manifiesto/         # Fundamentos filosóficos y workflow
│   ├── guides/             # Guías prácticas
│   ├── architecture/       # ADRs y decisiones técnicas
│   └── _meta/              # Issues y roadmap local
├── tools/                   # Scripts operacionales
│   ├── setup/              # Scripts de instalación
│   ├── maintenance/        # Scripts de limpieza y validación
│   ├── deployment/         # Scripts de despliegue
│   └── testing/            # Scripts de pruebas
├── infrastructure/          # Docker, CI/CD configs
└── _templates/             # Templates para nuevos proyectos/research
```

## 🐍 Python Stack

- **Version**: Python 3.10+
- **Package Manager**: pip con requirements.txt
- **Packaging**: pyproject.toml (PEP 517/518)
- **Testing**: pytest + pytest-cov
- **Formatting**: black + isort
- **Linting**: flake8, mypy (opcional)

## 📦 Dependencias Principales

### packages/daath-toolkit/
```
- pinecone-client>=2.2.0    # Vector database
- openai>=1.0.0             # Embeddings API
- pyyaml>=6.0               # YAML parsing
- python-frontmatter>=1.0   # Markdown frontmatter
```

### packages/core-mcp/
```
- mcp>=0.9.0                # Model Context Protocol SDK
- fastapi>=0.100.0          # API framework
- uvicorn>=0.23.0           # ASGI server
```

## 🔧 Herramientas de Desarrollo

- **Editor**: VS Code con extensiones Python, spec-workflow-mcp
- **Version Control**: Git + GitHub
- **Pre-commit**: hooks para calidad
- **CI/CD**: GitHub Actions (configuración pendiente)

## 🐳 Docker

- `infrastructure/docker/docker-compose.yml` para servicios locales
- Redis para caché/sessions
- Neo4j para knowledge graph (opcional)

## 📁 Convenciones de Nomenclatura

- **Python files**: `snake_case.py`
- **Python packages**: `snake_case/`
- **Markdown docs**: `kebab-case.md`
- **YAML configs**: `kebab-case.yaml`
- **Directories**: `kebab-case/` para docs, `snake_case/` para código
