# Smart-Thinking Docker Container

**Versión**: 11.0.6
**Tipo**: MCP Server (stdio)
**Persistencia**: 100% local en `.daath/smart-thinking-sessions/`

## 🐳 Opción 1: Docker Container (RECOMENDADO)

### Build + Run

```powershell
cd C:\proyectos\aleia-melquisedec\.daath\smart-thinking-docker

# Build imagen
docker build -t daath-zen/smart-thinking:latest .

# Run container
docker-compose up -d

# Ver logs
docker logs smart-thinking-mcp -f

# Detener
docker-compose down
```

### Configuración en settings.json

```json
{
  "claudeCode.mcpServers": {
    "smart-thinking": {
      "command": "docker",
      "args": [
        "exec",
        "-i",
        "smart-thinking-mcp",
        "smart-thinking-mcp"
      ],
      "env": {
        "DISABLE_TELEMETRY": "true"
      }
    }
  }
}
```

## 📦 Opción 2: NPX Local (ACTUAL - con problemas)

**Problema detectado**: Claude Code falla al iniciar el servidor NPX en Windows.

```json
{
  "claudeCode.mcpServers": {
    "smart-thinking": {
      "command": "npx",
      "args": ["-y", "smart-thinking-mcp"],
      "env": {
        "DISABLE_TELEMETRY": "true",
        "SMART_THINKING_DATA_DIR": "C:/proyectos/aleia-melquisedec/.daath/smart-thinking-sessions"
      }
    }
  }
}
```

## 🔍 Diagnóstico

**El paquete SÍ funciona**:
```powershell
npx -y smart-thinking-mcp
# ✅ Inicia correctamente (logs en francés son normales)
```

**Pero Claude Code no puede iniciarlo** (problema de stdio en Windows).

## ✅ Solución Recomendada

**Usar Docker** porque:
- ✅ Aísla el proceso (no conflictos stdio)
- ✅ Reinicio automático
- ✅ Misma persistencia local
- ✅ Más confiable en Windows
- ✅ Telemetría 100% desactivada

## 🚀 Setup Rápido

```powershell
# 1. Build
cd .daath\smart-thinking-docker
docker build -t daath-zen/smart-thinking:latest .

# 2. Actualizar settings.json (User Settings)
# Ver configuración arriba

# 3. Reiniciar VS Code
```

---

**Autor**: DAATH-ZEN MELQUISEDEC
**Fecha**: 2026-01-09
