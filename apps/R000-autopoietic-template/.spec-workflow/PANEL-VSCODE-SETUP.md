# 🎨 Cómo Ver el Spec en el Panel de VS Code

## ⚠️ Problema Actual

El panel lateral "SPEC WORKFLOW: DASHBOARD" está mostrando **"Monorepo Improvements"** del proyecto root, pero tu spec está en **R000-autopoietic-template**.

---

## ✅ Solución: Cambiar Servidor MCP Activo

### 🔧 Método 1: Command Palette (MÁS DIRECTO)

1. **Abrir Command Palette**:
   - Windows/Linux: `Ctrl+Shift+P`
   - Mac: `Cmd+Shift+P`

2. **Buscar comando MCP**:
   Escribe una de estas opciones:
   - `MCP: Select Server`
   - `GitHub Copilot: Select MCP Server`
   - `Copilot: Change MCP Context`

3. **Seleccionar servidor**:
   ```
   ✅ spec-workflow-R000-autopoietic-template
   ❌ spec-workflow-root (este es el que está activo ahora)
   ```

4. **Verificar cambio**:
   El dropdown "Especificación:" ahora debe mostrar:
   - `spec-001-built-template-spec-workflow`

---

### 🔄 Método 2: Recargar Extensión

1. **Command Palette**: `Ctrl+Shift+P`

2. **Buscar**: `Developer: Reload Window`

3. **Al recargar**, el panel debe detectar ambos servidores

4. **Si hay selector de contexto**, elige: `R000-autopoietic-template`

---

### 📦 Método 3: MCP Explorer (Si está instalado)

Si tienes la extensión **MCP Explorer** (`moonolgerd.mcp-explorer`):

1. **Abrir MCP Explorer** desde el Activity Bar (barra lateral izquierda)

2. **Ver servidores disponibles**:
   ```
   📁 spec-workflow-root
      └── specs/
          └── monorepo-improvements/

   📁 spec-workflow-R000-autopoietic-template  ← ESTE
      └── specs/
          └── spec-001-built-template-spec-workflow/  ← TU SPEC
   ```

3. **Click derecho** en `spec-workflow-R000-autopoietic-template`

4. **Seleccionar**: "Set as Active Server" o "Use This Server"

---

### 🔍 Método 4: Verificar Contexto del Chat

En **GitHub Copilot Chat**:

```
@workspace ¿qué servidor MCP estoy usando?
```

O prueba ejecutar:

```
spec-status --specName spec-001-built-template-spec-workflow
```

Si responde correctamente con 26 tareas, estás en el servidor correcto.

---

## 🎯 Cómo Debe Verse Cuando Está Correcto

### Panel "SPEC WORKFLOW: DASHBOARD"

```
╔════════════════════════════════════════╗
║  SPEC WORKFLOW: DASHBOARD              ║
╠════════════════════════════════════════╣
║                                        ║
║  Especificación: [spec-001-built... ▼]║  ← DEBE MOSTRAR TU SPEC
║                                        ║
║  ┌─────────────────────────────────┐  ║
║  │  26        0          26         │  ║
║  │ Total  Completadas  Restantes   │  ║
║  │                                  │  ║
║  │  Progreso General: 0%            │  ║
║  └─────────────────────────────────┘  ║
║                                        ║
║  Tarea 1.1 [Completada ▼]             ║
║  Crear Schema JSON-LD Keter-Doc        ║
║                                        ║
║  Archivos:                             ║
║  • packages/core-mcp/schemas/...      ║
║                                        ║
║  Implementación:                       ║
║  • _Rostro: Schema Architect          ║
║  • _MCPs: [...]                        ║
║                                        ║
║  Requisitos: REQ-001-01                ║
║                                        ║
╚════════════════════════════════════════╝
```

---

## 🚨 Si Nada Funciona

### Verificar Servidores MCP Activos

**Método A - Ver logs de extensión**:

1. `Ctrl+Shift+P` → `Developer: Show Logs`
2. Selecciona: `Extension Host`
3. Busca logs de "MCP" o "spec-workflow"
4. Debe mostrar ambos servidores iniciados

**Método B - Reiniciar VS Code completamente**:

1. Cerrar VS Code completamente (no solo la ventana)
2. Abrir nuevamente
3. Los servidores MCP se iniciarán automáticamente
4. Selecciona el servidor correcto cuando el panel se active

---

## 🌐 Alternativa: Usar Dashboard Web

Si el panel de VS Code sigue sin funcionar, **usa el Dashboard Web**:

### ✅ Dashboard Web (100% funcional)

**URL**: http://localhost:5000

**Ventajas**:
- ✅ Muestra **ambos proyectos** en un solo lugar
- ✅ Cambia entre proyectos con un dropdown
- ✅ Interfaz más completa y visual
- ✅ No depende del contexto MCP de VS Code
- ✅ Se actualiza automáticamente

**Cómo acceder**:
1. El dashboard ya está corriendo (ventana PowerShell abierta)
2. Abre http://localhost:5000 en tu navegador
3. O usa el Simple Browser de VS Code (ya abierto)

**Selector de proyecto**:
```
┌─────────────────────────────────────┐
│ Proyecto: [R000-autopoietic-... ▼] │ ← Click aquí
└─────────────────────────────────────┘

Opciones:
• R000-autopoietic-template     ← SELECCIONA ESTE
• aleia-melquisedec (root)
```

---

## 📋 Resumen de Opciones

| Método | Dificultad | Recomendación |
|--------|-----------|---------------|
| 🌐 **Dashboard Web** | ⭐ Fácil | ✅ **RECOMENDADO** - Siempre funciona |
| 🎨 **Panel VS Code** | ⭐⭐ Media | Útil para integración con editor |
| 💬 **Copilot Chat** | ⭐ Fácil | Bueno para comandos rápidos |
| 📦 **MCP Explorer** | ⭐⭐ Media | Si tienes la extensión instalada |

---

## ✅ Verificación Final

### Tu spec ESTÁ funcionando correctamente:

```
✅ Nombre: spec-001-built-template-spec-workflow
✅ Ubicación: apps/R000-autopoietic-template/.spec-workflow/specs/
✅ Tareas: 26 detectadas
✅ Formato: Compatible con spec-workflow-mcp
✅ Estado: Ready for Implementation
✅ Dashboard: http://localhost:5000 (activo)
✅ Servidor MCP: spec-workflow-R000-autopoietic-template (configurado)
```

**El único problema es que el panel de VS Code está conectado al servidor MCP del proyecto root en lugar del servidor de R000.**

**Solución más simple**: Usa el Dashboard Web en http://localhost:5000 mientras trabajas, es más visual y completo.

---

**Siguiente paso**: Abre http://localhost:5000, selecciona "R000-autopoietic-template", y empieza a trabajar en las tareas 🚀
