# Arquitectura Monorepo: DAATH-ZEN MELQUISEDEC

## Filosofía de Diseño

**Principio DAATH (Conocimiento)**: Organización modular que facilita la emergencia de conocimiento a través de componentes interconectados.

**Principio ZEN**: Minimalismo funcional - solo lo necesario existe, todo tiene propósito claro.

---

## Estructura Optimizada

```
aleia-melquisedec/
│
├── 📜 docs/                              # Documentación centralizada
│   ├── architecture/                     # Decisiones arquitectónicas
│   ├── guides/                          # Guías de uso
│   └── manifiesto/                      # Filosofía MELQUISEDEC
│       └── bereshit-v3.0.0.md          # Versión actual del manifiesto
│
├── 🔧 packages/                          # Componentes reutilizables
│   ├── core-mcp/                        # Núcleo MCP (Neo4j, Ollama)
│   │   ├── docker/                      # Configuraciones Docker
│   │   ├── config/                      # Configuraciones MCP
│   │   └── scripts/                     # Scripts de gestión
│   │
│   └── daath-toolkit/                   # Herramientas compartidas
│       ├── capture/                     # Captura de chatlogs
│       ├── storage/                     # Vector store domain-aware
│       ├── validators/                  # Validadores de estructura
│       ├── generators/                  # Generadores de apps
│       └── testing/                     # Frameworks de testing
│
├── 🚀 apps/                              # Aplicaciones de investigación
│   │
│   ├── 00-template/                     # Plantilla base (MELQUISEDEC)
│   │   ├── PROPOSITO.md
│   │   ├── README.md
│   │   └── .gitignore
│   │
│   └── {investigacion-nombre}/          # Apps específicas (se crean bajo demanda)
│       ├── PROPOSITO.md                 # Manifiesto de la investigación
│       ├── 0-inbox/                     # Issues y requests
│       ├── 1-literature/                # Fuentes y referencias
│       ├── 2-atomic/                    # Conceptos destilados
│       ├── 3-workbook/                  # Análisis y síntesis
│       ├── 4-dataset/                   # Datos estructurados
│       ├── 5-outputs/                   # Entregables finales
│       └── _daath/                      # Metadata y aprendizajes
│
├── 🏗️ infrastructure/                    # Infraestructura compartida
│   ├── docker/                          # Docker Compose global
│   │   ├── docker-compose.yml
│   │   ├── docker-compose.dev.yml
│   │   └── docker-compose.prod.yml
│   │
│   ├── kubernetes/                      # Configuraciones K8s (futuro)
│   └── terraform/                       # IaC (futuro)
│
├── 🛠️ tools/                             # Scripts de desarrollo
│   ├── setup/                           # Scripts de instalación
│   ├── testing/                         # Scripts de testing
│   ├── deployment/                      # Scripts de despliegue
│   └── maintenance/                     # Scripts de mantenimiento
│
├── 📊 .vscode/                           # Configuración VS Code
│   ├── settings.json                    # Settings del workspace
│   ├── extensions.json                  # Extensiones recomendadas
│   └── mcp.json                         # Configuración MCP (si aplica)
│
├── 📦 .github/                           # CI/CD y automatizaciones
│   ├── workflows/                       # GitHub Actions
│   └── ISSUE_TEMPLATE/                  # Templates de issues
│
├── 🔒 .env.example                       # Variables de entorno template
├── .gitignore                           # Reglas de ignorado
├── README.md                            # Punto de entrada principal
└── package.json / pnpm-workspace.yaml   # Gestión del monorepo (si aplica)
```

---

## Principios de Organización

### 1. **Separación de Concerns**
- `docs/`: Conocimiento estático
- `packages/`: Código reutilizable
- `apps/`: Investigaciones específicas
- `infrastructure/`: Recursos de infraestructura
- `tools/`: Automatización y DevOps

### 2. **Convención de Nombrado**
```yaml
apps:
  formato: "{número}-{nombre-descriptivo}"
  ejemplo: "01-knowledge-graph-research"
  
packages:
  formato: "{purpose}-{component}"
  ejemplo: "core-mcp", "daath-toolkit"
  
tools:
  formato: "{action}_{target}.{ext}"
  ejemplo: "setup_neo4j.ps1", "test_mcps.py"
```

### 3. **Versionado Semántico**
- Manifiesto: `bereshit-v3.0.0.md`
- Apps: `PROPOSITO.md` con campo `version: "0.1.0"`
- Packages: `package.json` o `pyproject.toml` con versión

### 4. **Documentación como Código**
- Toda decisión arquitectónica en `docs/architecture/ADR-{número}-{título}.md`
- Guías en formato markdown en `docs/guides/`
- Manifiesto versionado en `docs/manifiesto/`

---

## Mejoras vs Estructura Anterior

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Documentación** | Dispersa (raíz, carpetas varias) | Centralizada en `docs/` |
| **Scripts** | Mezclados en múltiples ubicaciones | Separados por propósito en `tools/` |
| **Infraestructura** | Dispersa | Separada en `infrastructure/` |
| **Reutilización** | No había componentes compartidos | `packages/` con código común |
| **Templates** | _templates/app-melquisedec | apps/00-template (más intuitivo) |
| **Testing** | Scripts sueltos | Framework en packages/daath-toolkit/testing |
| **Capture/Storage** | No existía | packages/daath-toolkit/capture/ y storage/ |
| **CI/CD** | No existía | .github/workflows/ preparado |

---

## Flujos de Trabajo

### Crear Nueva Investigación
```powershell
# Usando el toolkit
python tools/generators/new-research.py "knowledge-graph-analysis"

# O manualmente
cp -r apps/00-template apps/01-knowledge-graph-analysis
cd apps/01-knowledge-graph-analysis
# Editar PROPOSITO.md
```

### Gestionar Infraestructura
```powershell
# Levantar todos los servicios
cd infrastructure/docker
docker-compose up -d

# Solo Neo4j para desarrollo
docker-compose up -d neo4j

# Configurar MCP servers
.\tools\setup\configure_mcp_servers.ps1
```

### Testing Integral
```powershell
# Test de MCPs
python tools/testing/test_mcp_toolkit.py --verbose

# Test de apps específicas
python tools/testing/validate_research_structure.py apps/01-knowledge-graph
```

---

## Tecnologías y Herramientas

### Gestión del Monorepo
- **npm/pnpm workspaces** (si hay componentes Node.js)
- **Poetry** (para paquetes Python compartidos)
- **Turborepo** (para builds optimizados - futuro)

### Infraestructura
- **Docker Compose**: Desarrollo local
- **GitHub Actions**: CI/CD
- **Pre-commit hooks**: Validación automática

### MCP Servers
- Docker MCP Toolkit v0.28.0 (gateway centralizado)
- Neo4j 5.15 Community (grafos de conocimiento)
- Ollama (embeddings con nomic-embed-text)

---

## Roadmap de Implementación

### Fase 1: Reorganización ✅ (actual)
- [x] Diseñar estructura
- [ ] Mover archivos existentes
- [ ] Actualizar referencias
- [ ] Validar funcionamiento

### Fase 2: Automatización (siguiente)
- [ ] Scripts de generación de apps
- [ ] CI/CD básico
- [ ] Pre-commit hooks
- [ ] Testing automatizado

### Fase 3: Escala (futuro)
- [ ] Gestión de dependencias entre packages
- [ ] Caching distribuido con Turborepo
- [ ] Deployment automatizado
- [ ] Kubernetes para producción

---

## Referencias

- [Manifiesto MELQUISEDEC v3.0.0](docs/manifiesto/bereshit-v3.0.0.md)
- [Docker MCP Toolkit Guide](docs/guides/docker-mcp-toolkit.md)
- [ADR: Estructura de Monorepo](docs/architecture/ADR-001-monorepo-structure.md)
