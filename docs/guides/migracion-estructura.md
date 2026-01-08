# Guía de Migración: Estructura Antigua → Nueva

Esta guía documenta cómo migrar proyectos existentes de la estructura antigua a la nueva arquitectura DAATH-ZEN.

---

## 🔄 Mapa de Migración

### Archivos del Sistema

| Antes | Después | Acción |
|-------|---------|--------|
| `bereshit/manifiesto-melquisedec-v3.0.0.md` | `docs/manifiesto/bereshit-v3.0.0.md` | ✅ Movido |
| `nucleo-investigacion/docker-compose.yml` | `infrastructure/docker/docker-compose.yml` | ✅ Movido |
| `nucleo-investigacion/Dockerfile` | `packages/core-mcp/docker/Dockerfile` | ✅ Movido |
| `nucleo-investigacion/server.py` | `packages/core-mcp/server.py` | ✅ Movido |
| `nucleo-investigacion/requirements.txt` | `packages/core-mcp/requirements.txt` | ✅ Movido |

### Scripts

| Antes | Después | Acción |
|-------|---------|--------|
| `nucleo-investigacion/scripts/test_mcps.py` | `tools/testing/test_mcps.py` | ✅ Movido |
| `nucleo-investigacion/scripts/test_docker_mcp_toolkit.py` | `tools/testing/test_mcp_toolkit.py` | ✅ Movido |
| `nucleo-investigacion/scripts/setup_neo4j_simple.ps1` | `tools/setup/setup_neo4j_simple.ps1` | ✅ Movido |
| `nucleo-investigacion/scripts/setup_neo4j_mcp.ps1` | `tools/setup/setup_neo4j_mcp.ps1` | ✅ Movido |
| `nucleo-investigacion/scripts/setup_neo4j_mcp.sh` | `tools/setup/setup_neo4j_mcp.sh` | ✅ Movido |

### Documentación

| Antes | Después | Acción |
|-------|---------|--------|
| `nucleo-investigacion/docs/DOCKER_MCP_TOOLKIT_GUIDE.md` | `docs/guides/docker-mcp-toolkit.md` | ✅ Movido |
| `nucleo-investigacion/CONFIGURACION_COMPLETA.md` | `docs/guides/configuracion-completa.md` | ✅ Movido |
| `README.md` (antiguo) | `README.md` (nuevo) | ✅ Reescrito |

### Templates

| Antes | Después | Acción |
|-------|---------|--------|
| `_templates/app-melquisedec/` | `apps/00-template/` | ✅ Movido y mejorado |

---

## 🎯 Impacto en Comandos

### Docker Compose

```diff
# ANTES
- cd nucleo-investigacion
- docker-compose up -d

# DESPUÉS
+ cd infrastructure/docker
+ docker-compose up -d
```

### Scripts de Setup

```diff
# ANTES
- cd nucleo-investigacion/scripts
- .\setup_neo4j_simple.ps1

# DESPUÉS
+ cd tools/setup
+ .\setup_neo4j_simple.ps1
```

### Testing

```diff
# ANTES
- cd nucleo-investigacion/scripts
- python test_docker_mcp_toolkit.py --verbose

# DESPUÉS
+ cd tools/testing
+ python test_mcp_toolkit.py --verbose
```

### Crear Nueva Investigación

```diff
# ANTES (manual)
- cp -r _templates/app-melquisedec apps/mi-app
- cd apps/mi-app
- code PROPOSITO.md  # Editar manualmente

# DESPUÉS (automatizado)
+ python packages/daath-toolkit/generators/new_research.py mi-app \
+   --purpose "Descripción" \
+   --initiated-by MELQUISEDEC
```

---

## 📝 Actualizar Referencias en Código

### Imports de Python

```diff
# Si tenías imports absolutos
- from nucleo_investigacion.scripts.test_mcps import *
+ from tools.testing.test_mcps import *

- from nucleo_investigacion.server import *
+ from packages.core_mcp.server import *
```

### Paths en Scripts

```diff
# PowerShell
- $scriptPath = "nucleo-investigacion/scripts/test_mcps.py"
+ $scriptPath = "tools/testing/test_mcps.py"

# Bash
- DOCKER_COMPOSE_FILE="nucleo-investigacion/docker-compose.yml"
+ DOCKER_COMPOSE_FILE="infrastructure/docker/docker-compose.yml"
```

### Documentación Internal Links

```diff
# Markdown
- [Ver configuración](nucleo-investigacion/CONFIGURACION_COMPLETA.md)
+ [Ver configuración](docs/guides/configuracion-completa.md)

- [Docker MCP Guide](nucleo-investigacion/docs/DOCKER_MCP_TOOLKIT_GUIDE.md)
+ [Docker MCP Guide](docs/guides/docker-mcp-toolkit.md)

- [Manifiesto](bereshit/manifiesto-melquisedec-v3.0.0.md)
+ [Manifiesto](docs/manifiesto/bereshit-v3.0.0.md)
```

---

## 🔧 Cambios en .gitignore

```diff
# Antigua estructura
- nucleo-investigacion/scripts/*.json
- nucleo-investigacion/scripts/*.log

# Nueva estructura
+ tools/testing/*.json
+ tools/testing/*.log
+ packages/**/__pycache__
+ apps/**/4-dataset/raw/*
+ apps/**/5-outputs/reports/*.pdf
```

---

## 🚀 Migración de Apps Existentes

Si tenías apps en desarrollo bajo la estructura antigua:

### Paso 1: Identificar Apps

```powershell
# Listar apps que no son el template
Get-ChildItem apps -Directory | Where-Object { $_.Name -ne '00-template' }
```

### Paso 2: Validar Estructura

```powershell
# Para cada app
python packages/daath-toolkit/validators/validate_research.py apps/mi-app
```

### Paso 3: Actualizar PROPOSITO.md

Asegurarse que tiene metadata YAML:

```yaml
---
id: "app-mi-app"
version: "0.1.0"
created: "YYYY-MM-DD"
status: "inception"
purpose: |
  Descripción del propósito

initiated_by: "MELQUISEDEC"
methodologies:
  - "Zettelkasten"
learning_mode: "active"
tags:
  - "investigacion"
---
```

### Paso 4: Actualizar README

Seguir template de `apps/00-template/README.md`

---

## ⚠️ Warnings y Deprecaciones

### Deprecado

- ❌ `_templates/` - Usar `apps/00-template/`
- ❌ `bereshit/` - Ahora en `docs/manifiesto/`
- ❌ `nucleo-investigacion/` - Separado en `packages/`, `infrastructure/`, `tools/`

### Aún Funcional (pero cambiará)

- ⚠️ Crear apps manualmente - Usar generador en su lugar
- ⚠️ `.vscode/mcp.json` - Migrar a Docker MCP Toolkit

---

## 🧪 Validación Post-Migración

```powershell
# 1. Verificar que servicios funcionan
cd infrastructure/docker
docker-compose up -d
docker-compose ps  # Todos deben estar "Up"

# 2. Validar MCPs
cd ../../tools/testing
python test_mcp_toolkit.py --verbose
# Esperado: Tasa de éxito: 100.0%

# 3. Validar apps
cd ../../packages/daath-toolkit/validators
python validate_research.py ../../apps/01-mi-app
# Esperado: Estado: ✅ VÁLIDO

# 4. Verificar documentación
cd ../../../
ls docs/**/*.md  # Debe listar todos los docs
```

---

## 📚 Recursos Adicionales

- [Arquitectura Completa](../../ARQUITECTURA_MONOREPO.md)
- [ADR-001: Decisión de Monorepo](../architecture/ADR-001-monorepo-structure.md)
- [Resumen de Reorganización](../../REORGANIZACION_COMPLETA.md)
- [Quick Reference](../../QUICK_REFERENCE.md)

---

## 🆘 Troubleshooting

### "No se encuentra docker-compose.yml"

```powershell
# Verificar ubicación actual
pwd
# Debe ser: C:\proyectos\aleia-melquisedec\infrastructure\docker

# Si no, navegar
cd infrastructure/docker
```

### "Module not found" en imports

```powershell
# Verificar PYTHONPATH
$env:PYTHONPATH = "C:\proyectos\aleia-melquisedec"

# O usar paths absolutos
cd C:\proyectos\aleia-melquisedec
python tools/testing/test_mcp_toolkit.py
```

### "No se encuentra template"

```powershell
# Verificar ubicación del template
Test-Path apps/00-template
# Debe devolver: True

# Si no existe, fue eliminado accidentalmente
# Restaurar desde Git
git checkout HEAD -- apps/00-template/
```

---

**Migración completada con éxito** ✅
