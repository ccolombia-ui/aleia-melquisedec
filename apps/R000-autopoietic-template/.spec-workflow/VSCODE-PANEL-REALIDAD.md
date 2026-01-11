# 🎯 SOLUCIONES PRÁCTICAS - Ver Spec en VS Code

## ⚠️ Problema Real

Los comandos MCP de VS Code que viste **NO incluyen** una opción para "cambiar de servidor" porque **el panel Spec Workflow usa el contexto del workspace actual**.

**Situación**:
- ✅ Workspace abierto: `aleia-melquisedec` (ROOT)
- ❌ Panel muestra: Specs del proyecto ROOT ("Monorepo Improvements")
- ✅ Tu spec está en: `apps/R000-autopoietic-template/`

**Por qué pasa**: El panel Spec Workflow MCP detecta automáticamente el `.spec-workflow` del directorio raíz del workspace.

---

## ✅ SOLUCIÓN 1: Usar Dashboard Web (MÁS FÁCIL)

### El dashboard web SÍ muestra ambos proyectos

**URL**: http://localhost:5000

**Por qué es mejor**:
- ✅ Muestra TODOS los proyectos automáticamente
- ✅ Cambia entre proyectos con un dropdown
- ✅ Interfaz más completa que el panel de VS Code
- ✅ No requiere cambiar workspace

**Cómo usar**:
1. Abre http://localhost:5000 (ya está corriendo)
2. En la parte superior, click en el selector de proyecto
3. Selecciona: **"R000-autopoietic-template"**
4. Verás tu spec con las 26 tareas

---

## ✅ SOLUCIÓN 2: Abrir R000 como Workspace (Panel VS Code)

Si quieres usar el panel lateral de VS Code, necesitas **abrir el proyecto R000 como workspace**:

### Opción A: Agregar a Workspace Multi-Root

1. **Command Palette**: `Ctrl+Shift+P`
2. Busca: `Workspaces: Add Folder to Workspace...`
3. Navega a: `C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template`
4. Agrégalo al workspace actual

**Resultado**: Ahora tendrás 2 carpetas en el workspace:
- `aleia-melquisedec` (root)
- `R000-autopoietic-template` ← Tu spec

El panel detectará automáticamente ambos `.spec-workflow` folders.

### Opción B: Abrir R000 en Nueva Ventana

1. **Command Palette**: `Ctrl+Shift+P`
2. Busca: `File: Open Folder...`
3. Selecciona: `C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template`
4. Click en **"Open"**

**Resultado**: Nueva ventana de VS Code abierta con R000 como workspace root. El panel Spec Workflow mostrará automáticamente tu spec.

### Opción C: Workspace File (Permanente)

Crear un archivo de workspace que incluya ambos proyectos:

**Archivo**: `aleia-melquisedec.code-workspace`

```json
{
  "folders": [
    {
      "name": "Root",
      "path": "."
    },
    {
      "name": "R000-autopoietic-template",
      "path": "apps/R000-autopoietic-template"
    }
  ],
  "settings": {
    "chat.mcp.defaultServer": "spec-workflow-R000-autopoietic-template"
  }
}
```

**Usar**:
1. Guarda este archivo en `C:\proyectos\aleia-melquisedec\aleia-melquisedec.code-workspace`
2. **File** → **Open Workspace from File...**
3. Selecciona el archivo `.code-workspace`
4. VS Code reabrirá con ambos folders

---

## ✅ SOLUCIÓN 3: Usar Comandos MCP Disponibles

Los comandos que SÍ tienes disponibles:

### `MCP: List Servers`
Muestra todos los servidores MCP configurados y su estado:

1. **Command Palette**: `Ctrl+Shift+P`
2. `MCP: List Servers`
3. Verás algo como:
   ```
   ✓ spec-workflow-root (activo)
   ✓ spec-workflow-R000-autopoietic-template (activo)
   ✓ filesystem
   ✓ playwright
   ... etc
   ```

**Limitación**: Este comando solo **muestra** los servidores, no te permite cambiar entre ellos para el panel.

### `Copilot MCP: Focus on Copilot MCP Panel View`
Abre/enfoca el panel MCP:

1. **Command Palette**: `Ctrl+Shift+P`
2. `Copilot MCP: Focus on Copilot MCP Panel View`

**Resultado**: Abre el panel lateral, pero seguirá mostrando el contexto del workspace actual.

### `MCP: Open Workspace Folder MCP Configuration`
Abre tu archivo `mcp.json` para edición:

**Útil para**:
- Ver/editar los servidores MCP configurados
- Verificar que `spec-workflow-R000-autopoietic-template` esté configurado

---

## 🎯 RECOMENDACIÓN FINAL

### Para Trabajar HOY (más rápido):

**Usa el Dashboard Web**: http://localhost:5000
- ✅ Ya funciona perfecto
- ✅ Muestra ambos proyectos
- ✅ Interfaz más visual
- ✅ No requiere cambios

### Para Configurar VS Code Definitivamente (mejor a largo plazo):

**Crea el archivo de workspace multi-root**:

1. Crea: `aleia-melquisedec.code-workspace` con el contenido de arriba
2. Abre ese workspace en lugar del folder
3. Ambos proyectos estarán disponibles en el panel

---

## 📋 Comparación de Opciones

| Solución | Dificultad | Tiempo | Persistente |
|----------|------------|--------|-------------|
| 🌐 **Dashboard Web** | ⭐ Fácil | 0 min | Mientras corra el servidor |
| 📁 **Multi-root Workspace** | ⭐⭐ Media | 5 min | ✅ Sí (permanente) |
| 🪟 **Nueva Ventana** | ⭐ Fácil | 1 min | ❌ No (cada vez que abres) |
| 📝 **Workspace File** | ⭐⭐ Media | 3 min | ✅ Sí (permanente) |

---

## ✅ Verificación Rápida

Tu spec **SÍ está funcionando**, solo no es visible en el panel porque:
- ❌ El panel usa contexto del workspace
- ❌ Workspace actual = proyecto root
- ✅ Tu spec = subproyecto R000

**Prueba desde Copilot Chat**:
```
¿Cuál es el estado del spec-001-built-template-spec-workflow?
```

Si responde con "26 tareas, 0 completadas", significa que el MCP server de R000 **SÍ está activo**, solo que el panel no lo muestra.

---

## 🚀 Acción Inmediata

**AHORA MISMO**:
1. Abre http://localhost:5000
2. Selector superior → "R000-autopoietic-template"
3. Click en "spec-001-built-template-spec-workflow"
4. ¡A trabajar! 🎉

**DESPUÉS (opcional)**:
- Configura workspace multi-root para tenerlo en el panel de VS Code

---

**La solución más simple**: Usa el dashboard web, es más potente que el panel de VS Code de todas formas.
