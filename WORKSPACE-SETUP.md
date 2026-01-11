# 🎯 Workspace Multi-Root Configurado

## ✅ Archivo Creado

Se ha creado: `aleia-melquisedec.code-workspace`

Este archivo configura un workspace multi-root con:
- 🏠 **Root - Monorepo**: Proyecto principal con specs del root
- 🚀 **R000 - Autopoietic Template**: Tu proyecto con spec-001

---

## 🚀 Cómo Usar el Workspace Multi-Root

### Paso 1: Abrir el Workspace

**Opción A - Desde VS Code actual:**
1. **File** → **Open Workspace from File...** (o `Ctrl+K Ctrl+O`)
2. Navega a: `C:\proyectos\aleia-melquisedec\`
3. Selecciona: `aleia-melquisedec.code-workspace`
4. Click **"Open"**

**Opción B - Desde Windows Explorer:**
1. Navega a: `C:\proyectos\aleia-melquisedec\`
2. Doble click en: `aleia-melquisedec.code-workspace`
3. VS Code abrirá con ambos folders

**Opción C - Desde terminal:**
```bash
cd C:\proyectos\aleia-melquisedec
code aleia-melquisedec.code-workspace
```

### Paso 2: Verificar la Configuración

Después de abrir el workspace, verás en el **Explorer** (barra lateral):

```
📁 🏠 ROOT - MONOREPO
   ├── 📁 apps/
   ├── 📁 docs/
   ├── 📁 packages/
   ├── 📁 .spec-workflow/        ← Specs del root
   └── ...

📁 🚀 R000 - AUTOPOIETIC TEMPLATE
   ├── 📁 _melquisedec/
   ├── 📁 .spec-workflow/        ← Tu spec-001
   └── ...
```

### Paso 3: Ver los Specs en el Panel

Una vez abierto el workspace:

1. Abre el panel **Spec Workflow MCP** (Activity Bar izquierdo)
2. Deberías ver un selector para cambiar entre proyectos
3. O ambos specs aparecerán automáticamente

---

## 🎯 Ventajas del Workspace Multi-Root

✅ **Navegación**: Ambos proyectos en un solo workspace
✅ **Panel Spec Workflow**: Detecta automáticamente ambos `.spec-workflow/`
✅ **Búsquedas**: Puedes buscar en ambos proyectos simultáneamente
✅ **Terminal**: Contexto correcto para cada proyecto
✅ **Git**: Gestión independiente de cada folder
✅ **Configuración**: Settings específicos por proyecto

---

## 🔧 Configuración Incluida

### Settings Aplicados

```json
{
  "chat.mcp.defaultServer": "spec-workflow-R000-autopoietic-template",
  "telemetry.telemetryLevel": "off",
  "files.exclude": {
    "**/.git": true,
    "**/__pycache__": true,
    "**/node_modules": true
  }
}
```

### Extensiones Recomendadas

- **contextiq**: Context management para Copilot
- **mcp-explorer**: Explorador de servidores MCP
- **thinking-in-code**: Herramientas de razonamiento

---

## 🎨 Panel Spec Workflow Después de Abrir el Workspace

**ANTES** (workspace simple):
```
Especificación: [Monorepo Improvements ▼]
└── Solo ve specs del root
```

**DESPUÉS** (workspace multi-root):
```
Proyecto: [🚀 R000 - Autopoietic Template ▼]
Especificación: [spec-001-built-template-spec-workflow ▼]
└── Puedes cambiar entre ambos proyectos
```

---

## 📋 Comandos Útiles en Multi-Root Workspace

### Terminal Contextual
El terminal se abrirá en el contexto del folder seleccionado:

- Click derecho en `🚀 R000` → **"Open in Integrated Terminal"**
- Terminal abre en: `apps/R000-autopoietic-template/`

### Búsqueda Scoped
Puedes buscar solo en un folder específico:

1. Click derecho en el folder
2. **"Find in Folder..."**
3. Búsqueda limitada a ese folder

### Settings por Folder
Cada folder puede tener su propio `.vscode/settings.json`

---

## 🔄 Cambiar entre Specs

Una vez abierto el workspace multi-root:

### En el Panel Spec Workflow
- Si hay selector de proyecto, úsalo para cambiar
- O navega entre los specs listados

### En Copilot Chat
```
# Ver specs del root
@workspace /specs en Root

# Ver specs de R000
@workspace /specs en R000-autopoietic-template
```

### Spec Status por Proyecto
```bash
# Desde terminal en R000
spec-status --specName spec-001-built-template-spec-workflow

# O navega al folder en el Explorer y usa terminal contextual
```

---

## ⚠️ Notas Importantes

### Guardar el Workspace
Después de abrir el workspace, VS Code preguntará si quieres "Trust this workspace":
- ✅ Click "Trust" para habilitar todas las funciones

### MCP Servers
Ambos servidores MCP seguirán activos:
- `spec-workflow-root`
- `spec-workflow-R000-autopoietic-template`

El workspace no cambia esto, solo mejora la visibilidad.

### Git
Cada folder mantiene su propio contexto Git:
- Root: `feature/spec-001-implementation`
- R000: Mismo branch (es un subfolder)

---

## 🎯 Próximos Pasos

1. **Abre el workspace**: `File → Open Workspace from File...`
2. **Selecciona**: `aleia-melquisedec.code-workspace`
3. **Trust workspace** cuando VS Code lo pida
4. **Verifica Explorer**: Debes ver ambos folders
5. **Abre Panel Spec Workflow**: Tu spec debe ser visible

---

## 🌐 Dashboard Web Sigue Disponible

El workspace multi-root no reemplaza al dashboard web, son complementarios:

- **Dashboard Web**: http://localhost:5000 (más visual)
- **Panel VS Code**: Integrado con el editor

Usa ambos según tu preferencia.

---

## 🔧 Troubleshooting

### "No veo cambios en el panel"
1. Cierra y reabre el panel Spec Workflow
2. O recarga la ventana: `Ctrl+Shift+P` → `Developer: Reload Window`

### "Solo veo un folder"
- Verifica que el archivo `.code-workspace` tenga ambos folders
- Revisa que abriste el workspace (no el folder)

### "Los specs no aparecen"
- Los servidores MCP tardan unos segundos en iniciarse
- Espera 5-10 segundos después de abrir el workspace
- Si persiste, recarga la ventana

---

## ✅ Verificación Final

Después de abrir el workspace, verifica:

- [ ] Explorer muestra 2 folders (Root y R000)
- [ ] Panel Spec Workflow muestra specs de ambos proyectos
- [ ] Terminal contextual funciona por folder
- [ ] Búsqueda global funciona en ambos folders

---

**¡Listo!** Ahora tienes un workspace profesional multi-root configurado. 🎉

**Siguiente paso**: Abre el workspace y comienza a trabajar en tu spec-001.
