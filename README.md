# DAATH-ZEN MELQUISEDEC

> Monorepo de investigación autopoiético para el desarrollo de sistemas de conocimiento augmentado

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release](https://img.shields.io/github/v/release/ccolombia-ui/aleia-melquisedec?include_prereleases)](https://github.com/ccolombia-ui/aleia-melquisedec/releases)
[![Tests](https://github.com/ccolombia-ui/aleia-melquisedec/actions/workflows/test.yml/badge.svg)](https://github.com/ccolombia-ui/aleia-melquisedec/actions)
[![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)](https://www.docker.com/)
[![MCP](https://img.shields.io/badge/MCP-Toolkit-green.svg)](https://github.com/docker/mcp-toolkit)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.15-008CC1.svg)](https://neo4j.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg)](https://www.python.org/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

---

## 🎯 Visión

**DAATH-ZEN** es un framework de investigación basado en el [Manifiesto MELQUISEDEC v3.0.0](docs/manifiesto/bereshit-v3.0.0.md) que combina:

- 🧠 **Autopoiesis**: El sistema se mejora a sí mismo
- 🌊 **Síntesis Metodológica**: Orquesta metodologías existentes (no inventa)
- 🎭 **5 Rostros**: MELQUISEDEC → HYPATIA → SALOMON → MORPHEUS → ALMA
- 🌱 **Crecimiento Orgánico**: La estructura emerge según necesidad

---

## 📁 Estructura del Monorepo

```
aleia-melquisedec/
├── 📜 docs/                    # Documentación centralizada
│   ├── architecture/           # ADRs y decisiones
│   ├── guides/                # Guías de uso
│   └── manifiesto/            # Filosofía MELQUISEDEC
│
├── 🔧 packages/                # Componentes reutilizables
│   ├── core-mcp/              # Núcleo MCP (Neo4j + Ollama)
│   └── daath-toolkit/         # Herramientas compartidas
│
├── 🚀 apps/                    # Investigaciones activas
│   └── 00-template/           # Plantilla MELQUISEDEC
│
├── 🏗️ infrastructure/          # Docker, K8s, IaC
│   └── docker/                # Compose files
│
└── 🛠️ tools/                   # Scripts de desarrollo
    ├── setup/                 # Instalación
    ├── testing/               # Testing
    └── deployment/            # Despliegue
```

**Ver arquitectura completa**: [[arquitectura-monorepo]]

---

## 🚀 Inicio Rápido

### Prerequisitos

- Docker Desktop 20.10+
- Docker MCP Toolkit v0.28.0+
- Python 3.10+
- VS Code con GitHub Copilot

### Instalación

```powershell
# 1. Clonar repositorio
git clone https://github.com/tu-org/aleia-melquisedec.git
cd aleia-melquisedec

# 2. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# 3. Levantar infraestructura
cd infrastructure/docker
docker-compose up -d

# 4. Configurar MCP servers
cd ../../tools/setup
.\setup_neo4j_simple.ps1

# 5. Validar instalación
cd ../testing
python test_mcp_toolkit.py --verbose
```

**Salida esperada**: ✓ Tasa de éxito: 100.0%

---

## 📚 Guías

### Crear Nueva Investigación

```powershell
# Usando el generador
python packages/daath-toolkit/generators/new_research.py knowledge-graph-research --purpose "Analizar grafos de conocimiento"

# O manualmente
cp -r apps/00-template apps/01-mi-investigacion
cd apps/01-mi-investigacion
code PROPOSITO.md
```

La estructura crece orgánicamente:

- `0-inbox/` → Issues y requests
- `1-literature/` → Fuentes cuando se necesiten
- `2-atomic/` → Conceptos destilados
- `3-workbook/` → Análisis y síntesis
- `4-dataset/` → Datos estructurados
- `5-outputs/` → Entregables finales
- `_daath/` → Metadata y aprendizajes

### Trabajar con MCP Servers

```powershell
# Listar servers disponibles
docker mcp server ls

# Probar funcionalidad
python tools/testing/test_mcp_toolkit.py

# Configurar nuevo server
docker mcp config set <server> <key> <value>
docker mcp secret set <server> <key> <value>
```

**Ver guía completa**: [Docker MCP Toolkit](docs/guides/docker-mcp-toolkit.md)

---

## 🧠 Componentes Principales

### Core MCP

Núcleo de conectividad con servicios de IA:

- **Neo4j 5.15**: Grafos de conocimiento
- **Ollama**: Embeddings (nomic-embed-text)
- **19 MCP Servers**: arxiv, brave, filesystem, neo4j, perplexity, etc.

### DAATH Toolkit

Herramientas para gestión del monorepo:

- Validadores de estructura
- Generadores de apps
- Framework de testing

---

## 🎭 Los 5 Rostros de MELQUISEDEC

| Rostro                | Función      | Uso                                |
| --------------------- | ------------- | ---------------------------------- |
| **MELQUISEDEC** | Orquestador   | Define arquitectura y flujos       |
| **HYPATIA**     | Investigadora | Busca fuentes y analiza literatura |
| **SALOMON**     | Sintetizador  | Destila conocimiento atómico      |
| **MORPHEUS**    | Transformador | Genera datasets y estructuras      |
| **ALMA**        | Narrador      | Crea outputs finales               |

---

## 🔧 Tecnologías

- **Infraestructura**: Docker, Docker Compose
- **Bases de Datos**: Neo4j 5.15, Redis
- **IA/ML**: Ollama, OpenAI, Perplexity
- **Testing**: pytest, custom validators
- **CI/CD**: GitHub Actions
- **Docs**: Markdown, Mermaid

---

## 📊 Estado del Proyecto

- ✅ Arquitectura base definida
- ✅ MCP Toolkit configurado (16/19 servers activos)
- ✅ Neo4j + Ollama integrados
- ✅ Framework de testing funcional
- ✅ Generadores y validadores automatizados
- ✅ Reorganización completa del monorepo
- ✅ Documentación exhaustiva (6 docs principales)
- 🚧 CI/CD pipeline
- 📅 Kubernetes deployment (futuro)

---

## 🎉 Reorganización Completada

**Fecha**: 2026-01-07

El proyecto ha sido reorganizado siguiendo mejores prácticas de monorepo:

- 📁 **Estructura modular**: `docs/`, `packages/`, `apps/`, `infrastructure/`, `tools/`
- 🤖 **Automatización**: Generadores y validadores de investigaciones
- 📚 **Documentación completa**: ADRs, guías, referencias rápidas
- ✅ **100% validado**: Todos los tests pasan, estructura verificada

Ver detalles completos:

- [[reorganizacion-completa]]
- [[estructura-visual]]
- [[quick-reference]]

---

## 🤝 Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para guías de contribución.

**Filosofía**: Las contribuciones deben alinearse con los principios del [Manifiesto MELQUISEDEC](docs/manifiesto/bereshit-v3.0.0.md).

---

## 📖 Documentación

- [[arquitectura-monorepo]]
- [Manifiesto MELQUISEDEC v3.0.0](docs/manifiesto/bereshit-v3.0.0.md)
- [Guía Docker MCP Toolkit](docs/guides/docker-mcp-toolkit.md)
- [Configuración Completa](docs/guides/configuracion-completa.md)

---

## 📜 Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles.

---

## 🙏 Reconocimientos

Inspirado por:

- **Zettelkasten**: Niklas Luhmann
- **Building a Second Brain**: Tiago Forte
- **Autopoiesis**: Humberto Maturana & Francisco Varela
- **Model Context Protocol**: Anthropic

---

**"En el principio era el Verbo... y el Verbo se hizo código"** - Bereshit MELQUISEDEC v3.0.0

```bash
   git clone <tu-repo>
   cd aleia-melquisedec
```

2. **Los MCP Servers ya están configurados:**

   Los MCPs están configurados globalmente en VS Code (`User Settings`) y se cargan automáticamente al iniciar GitHub Copilot Chat.

   **Verificar configuración actual:**

   - Presiona `Ctrl+Shift+P`
   - Ejecuta: `Preferences: Open User Settings (JSON)`
   - Busca la sección `"mcp.servers"`
3. **Requisitos:**

   - Node.js (v16+) y npm - Para MCPs de Filesystem y Memory
   - Python 3.10+ y uv - Para MCP de Fetch

   ```bash
   # Verificar instalaciones
   node --version
   npm --version
   uv --version
   ```

### Verificar MCPs Activos

**Para GitHub Copilot Chat (Limitación Actual):**

Los MCPs configurados en `settings.json` **no aparecerán como herramientas personalizadas** en GitHub Copilot Chat. GitHub Copilot viene con MCPs preconfigurados a nivel de plataforma:

- ✅ GitHub MCP
- ✅ GitKraken MCP
- ✅ Playwright MCP
- ✅ Markdown MCP
- ✅ Apify MCP
- ✅ Context7/UPS MCP
- ✅ Pylance MCP

Los MCPs locales (filesystem, fetch, memory) que configuraste funcionarán en:

- **Claude Desktop** (app nativa de Anthropic)
- **Cline** (extensión alternativa)
- Otros clientes MCP que soporten configuración local

**Para verificar logs de MCP en VS Code:**

1. `View` → `Output`
2. Selecciona `"MCP Servers"` en el dropdown

```bash
# En el chat de Copilot, pregunta:
"¿Qué MCPs están activos?"
```

## 🔒 Privacidad y Seguridad

- ✅ Telemetría desactivada
- ✅ Todos los MCPs procesamiento local
- ✅ Sin filtración de código a servicios externos (excepto Fetch MCP cuando lo uses)
- ✅ Configuración incluida en `.gitignore`

## 📁 Estructura del Proyecto

```
aleia-melquisedec/
├── .vscode/
│   ├── settings.json           # Configuración local (no versionada)
│   ├── settings.example.json   # Ejemplo de configuración (versionada)
│   └── extensions.json         # Extensiones recomendadas
├── README.md
└── .gitignore
```

## 🔧 Configuración del Perfil "melquisedec"

Para que los MCPs estén siempre disponibles en el perfil "melquisedec":

### Configuración Global del Perfil

1. Abre VS Code con el perfil "melquisedec"
2. `Ctrl+Shift+P` → "Preferences: Open User Settings (JSON)"
3. Agrega la misma configuración de MCP servers

### Configuración por Workspace (Recomendado)

La configuración en `.vscode/settings.json` aplica solo a este workspace y tiene prioridad sobre la configuración global.

## 📦 Control de Versiones

### ¿Qué incluir en el repositorio (main)?

**✅ SÍ incluir:**

- `.vscode/extensions.json` - Extensiones recomendadas
- `.vscode/settings.example.json` - Plantilla de configuración
- `README.md` - Documentación
- `.gitignore` - Exclusiones de Git

**❌ NO incluir:**

- `.vscode/settings.json` - Configuración personal (paths absolutos)
- `node_modules/` - Dependencias
- `data/*.db` - Bases de datos locales
- `.mcp-memory/` - Memoria persistente de MCP

## 🛠️ Uso de MCPs

### Filesystem MCP

```
"Lee todos los archivos .ts del directorio src/"
```

### Fetch MCP

```
"Haz una petición GET a https://api.ejemplo.com/datos"
```

### Memory MCP

```
"Recuerda que usamos TypeScript estricto en este proyecto"
```

### Python MCP

```
"Ejecuta este script de análisis de datos: [código]"
```

## 📝 Notas

- Los MCP servers se descargan automáticamente vía `npx` la primera vez
- No requieren instalación global
- Se ejecutan en background mientras el workspace está abierto

## 🤝 Contribuir

[Por definir]

## 📄 Licencia

[Por definir]
