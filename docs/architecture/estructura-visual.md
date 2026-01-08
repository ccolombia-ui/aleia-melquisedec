# Estructura Visual del Monorepo DAATH-ZEN

```
aleia-melquisedec/
│
├── 📜 docs/                              # Documentación Centralizada
│   ├── architecture/                     # ADRs - Architecture Decision Records
│   │   └── ADR-001-monorepo-structure.md
│   ├── guides/                          # Guías y Tutoriales
│   │   ├── docker-mcp-toolkit.md
│   │   └── configuracion-completa.md
│   └── manifiesto/                      # Filosofía MELQUISEDEC
│       └── bereshit-v3.0.0.md
│
├── 🔧 packages/                          # Código Reutilizable
│   ├── core-mcp/                        # Núcleo MCP
│   │   ├── docker/
│   │   │   └── Dockerfile
│   │   ├── config/
│   │   ├── scripts/
│   │   ├── server.py
│   │   └── requirements.txt
│   │
│   └── daath-toolkit/                   # Herramientas DAATH
│       ├── validators/
│       │   └── validate_research.py     # Valida estructura de apps
│       ├── generators/
│       │   └── new_research.py          # Genera nuevas investigaciones
│       └── testing/
│
├── 🚀 apps/                              # Investigaciones Activas
│   ├── 00-template/                     # Template Base
│   │   ├── PROPOSITO.md
│   │   ├── README.md
│   │   └── .gitignore
│   │
│   └── 01-test-reorganizacion/          # Ejemplo (eliminar después)
│       ├── PROPOSITO.md
│       ├── README.md
│       └── 0-inbox/                     # Crece orgánicamente
│           └── README.md
│
├── 🏗️ infrastructure/                    # Infraestructura
│   └── docker/
│       └── docker-compose.yml           # Neo4j, Ollama, MCP Gateway
│
├── 🛠️ tools/                             # Scripts de Desarrollo
│   ├── setup/                           # Scripts de Instalación
│   │   ├── setup_neo4j_simple.ps1
│   │   ├── setup_neo4j_mcp.ps1
│   │   └── setup_neo4j_mcp.sh
│   ├── testing/                         # Scripts de Testing
│   │   ├── test_mcp_toolkit.py
│   │   └── test_mcps.py
│   ├── deployment/                      # Scripts de Despliegue (futuro)
│   └── maintenance/                     # Scripts de Mantenimiento (futuro)
│
├── 📦 .vscode/                           # Configuración VS Code
│   ├── settings.json
│   ├── extensions.json
│   └── mcp.json
│
├── 🔧 .github/                           # CI/CD (preparado para futuro)
│   └── workflows/
│
├── 📄 Archivos Raíz
│   ├── README.md                        # 🌟 Punto de entrada principal
│   ├── ARQUITECTURA_MONOREPO.md         # Diseño completo
│   ├── REORGANIZACION_COMPLETA.md       # Este documento
│   ├── CONTRIBUTING.md                  # Guía de contribución
│   ├── .env.example                     # Template de variables
│   ├── .gitignore                       # Reglas de ignorado
│   └── .env                             # Variables de entorno (no versionado)
│
└── 🗑️ Para eliminar después de validar
    └── apps/01-test-reorganizacion/     # App de prueba
```

---

## 🎯 Flujos de Trabajo

### 1. Crear Nueva Investigación

```
Usuario
   │
   ├─> python packages/daath-toolkit/generators/new_research.py nombre-investigacion
   │
   └─> apps/0X-nombre-investigacion/
         ├── PROPOSITO.md (auto-generado)
         ├── README.md (auto-generado)
         ├── .gitignore (auto-generado)
         └── 0-inbox/ (creado automáticamente)
```

### 2. Validar Investigación

```
Usuario
   │
   ├─> python packages/daath-toolkit/validators/validate_research.py apps/0X-nombre/
   │
   └─> Reporte de Validación
         ├── ✅ PROPOSITO.md con YAML válido
         ├── ✅ Carpetas según convención
         └── ⚠️ Advertencias (si aplica)
```

### 3. Usar MCP Servers

```
GitHub Copilot
   │
   ├─> @workspace "Usando neo4j-cypher, crea un grafo..."
   │
   └─> Docker MCP Toolkit
         ├── neo4j-cypher
         ├── neo4j-memory
         ├── arxiv
         ├── perplexity-ask
         └── [16 MCPs más]
```

### 4. Desarrollo Local

```
Developer
   │
   ├─> cd infrastructure/docker
   │   docker-compose up -d
   │
   ├─> cd ../../tools/setup
   │   .\setup_neo4j_simple.ps1
   │
   ├─> cd ../testing
   │   python test_mcp_toolkit.py --verbose
   │
   └─> ✅ Tasa de éxito: 100.0%
```

---

## 📊 Capas de Abstracción

```
┌─────────────────────────────────────────────────────────┐
│  CAPA 1: APLICACIONES                                   │
│  apps/0X-investigacion/                                 │
│  ├── Investigaciones específicas                        │
│  └── Crecimiento orgánico según MELQUISEDEC             │
└─────────────────────────────────────────────────────────┘
              │
              │ usa
              ▼
┌─────────────────────────────────────────────────────────┐
│  CAPA 2: HERRAMIENTAS                                   │
│  packages/daath-toolkit/                                │
│  ├── Generadores (new_research.py)                      │
│  ├── Validadores (validate_research.py)                 │
│  └── Testing frameworks                                 │
└─────────────────────────────────────────────────────────┘
              │
              │ usa
              ▼
┌─────────────────────────────────────────────────────────┐
│  CAPA 3: CORE                                           │
│  packages/core-mcp/                                     │
│  ├── Servidor MCP                                       │
│  ├── Configuraciones                                    │
│  └── Scripts de gestión                                 │
└─────────────────────────────────────────────────────────┘
              │
              │ usa
              ▼
┌─────────────────────────────────────────────────────────┐
│  CAPA 4: INFRAESTRUCTURA                                │
│  infrastructure/docker/                                 │
│  ├── Neo4j 5.15 (grafos)                                │
│  ├── Ollama (embeddings)                                │
│  └── Docker MCP Toolkit (19 servers)                    │
└─────────────────────────────────────────────────────────┘
```

---

## 🎭 Principios MELQUISEDEC en la Estructura

```
MELQUISEDEC (Orquestador)
   ├── docs/architecture/         → Define estructura
   ├── ARQUITECTURA_MONOREPO.md   → Visión general
   └── tools/                     → Automatización

HYPATIA (Investigadora)
   ├── apps/0X-*/1-literature/    → Fuentes y referencias
   ├── packages/daath-toolkit/    → Herramientas de búsqueda
   └── docs/guides/               → Guías de investigación

SALOMON (Sintetizador)
   ├── apps/0X-*/2-atomic/        → Conceptos destilados
   ├── packages/core-mcp/         → Lógica central
   └── docs/manifiesto/           → Filosofía sintetizada

MORPHEUS (Transformador)
   ├── apps/0X-*/4-dataset/       → Datos estructurados
   ├── infrastructure/docker/     → Transformación de servicios
   └── packages/daath-toolkit/    → Generadores

ALMA (Narrador)
   ├── apps/0X-*/5-outputs/       → Entregables finales
   ├── README.md                  → Historia del proyecto
   └── docs/                      → Narrativa documentada
```

---

## 🔄 Ciclo de Vida de una Investigación

```
1. INCEPTION
   │
   ├─> python generators/new_research.py mi-investigacion
   │
   └─> apps/0X-mi-investigacion/
       ├── PROPOSITO.md (version: 0.1.0, status: inception)
       └── 0-inbox/

2. RESEARCH
   │
   ├─> Crear 1-literature/
   ├─> Usar arxiv, brave, perplexity MCPs
   │
   └─> apps/0X-mi-investigacion/
       ├── 1-literature/
       │   ├── papers/
       │   └── articles/
       └── PROPOSITO.md (status: active)

3. SYNTHESIS
   │
   ├─> Crear 2-atomic/
   ├─> Destilar conceptos clave
   │
   └─> apps/0X-mi-investigacion/
       ├── 2-atomic/
       │   ├── concept-001.md
       │   └── concept-002.md
       └── 3-workbook/
           └── analysis.ipynb

4. STRUCTURING
   │
   ├─> Crear 4-dataset/
   ├─> Usar neo4j-cypher para grafos
   │
   └─> apps/0X-mi-investigacion/
       ├── 4-dataset/
       │   ├── knowledge-graph/
       │   └── processed/
       └── PROPOSITO.md (status: synthesis)

5. OUTPUT
   │
   ├─> Crear 5-outputs/
   ├─> Generar entregables
   │
   └─> apps/0X-mi-investigacion/
       ├── 5-outputs/
       │   ├── report.md
       │   └── visualizations/
       ├── _daath/
       │   └── metrics.json
       └── PROPOSITO.md (status: completed, version: 1.0.0)
```

---

## 🌐 Ecosistema de Herramientas

```
                    ┌──────────────────┐
                    │   GitHub Copilot │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Docker MCP      │
                    │  Toolkit Gateway │
                    └────────┬─────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐       ┌──────▼──────┐      ┌────▼────┐
    │  Neo4j  │       │   Ollama    │      │  19 MCP │
    │  Grafos │       │  Embeddings │      │ Servers │
    └─────────┘       └─────────────┘      └─────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                    ┌────────▼─────────┐
                    │  Investigaciones │
                    │  apps/0X-*/      │
                    └──────────────────┘
```

---

## 📈 Evolución del Proyecto

```
v0.1.0 (Antes)          v1.0.0 (Ahora)          v2.0.0 (Futuro)
───────────────────────────────────────────────────────────────
│                       │                       │
├── Simple              ├── Modular            ├── Automatizado
├── Manual              ├── Semi-automatizado  ├── Full CI/CD
├── Sin estructura      ├── Bien organizado    ├── Kubernetes
└── 1 investigación     └── N investigaciones  └── Multi-tenant
```

---

**Esta es la estructura viva de DAATH-ZEN MELQUISEDEC** 🌱
