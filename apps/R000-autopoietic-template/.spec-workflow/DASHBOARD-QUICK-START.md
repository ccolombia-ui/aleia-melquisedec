# 🚀 Dashboard Quick Start - R000-autopoietic-template

## 📍 Ubicación del Spec

**Proyecto**: R000-autopoietic-template
**Spec**: spec-001-built-template-spec-workflow
**Tareas**: 26 detectadas ✅
**Estado**: Ready for Implementation

---

## 🌐 Opción 1: Dashboard Web (RECOMENDADO)

### Acceso Directo
**URL**: http://localhost:5000

### Cómo Usar
1. ✅ **Ya está corriendo** - El dashboard detectó automáticamente 2 proyectos
2. En la parte superior, selecciona **"R000-autopoietic-template"** del dropdown
3. Verás tu spec: **spec-001-built-template-spec-workflow**
4. Click en el spec para ver las 26 tareas organizadas por fases

### Navegación
- **Panel izquierdo**: Lista de specs del proyecto seleccionado
- **Panel central**: Detalles del spec (requirements, design, tasks)
- **Panel derecho**: Progreso y métricas

### Acciones Disponibles
- ✅ Ver todas las tareas con su estado
- ✅ Ver detalles de cada tarea (File, Requirements, _Prompt)
- ✅ Marcar tareas como In Progress o Completed
- ✅ Ver progreso general (0/26 completadas)

---

## 🎨 Opción 2: Panel de VS Code

### Problema Actual
El panel lateral de VS Code muestra **"Monorepo Improvements"** porque está conectado al servidor MCP del proyecto **root**, no al servidor de R000-autopoietic-template.

### Solución: Cambiar de Servidor MCP

#### Método A: Command Palette
1. Presiona **Ctrl+Shift+P**
2. Busca: `MCP: Select Server` o `GitHub Copilot: Select MCP Server`
3. Selecciona: **`spec-workflow-R000-autopoietic-template`**
4. El dropdown "Especificación" ahora mostrará tu spec

#### Método B: Reiniciar Extensión
1. Presiona **Ctrl+Shift+P**
2. Busca: `Developer: Reload Window`
3. Al recargar, el panel debería detectar ambos servidores

#### Método C: Usar MCP Explorer (Recomendado)
Si tienes instalada la extensión **MCP Explorer** (`moonolgerd.mcp-explorer`):
1. Abre el panel de MCP Explorer desde el Activity Bar
2. Verás todos los servidores MCP disponibles:
   - `spec-workflow-root`
   - `spec-workflow-R000-autopoietic-template` ← Selecciona este
3. Expande el servidor para ver los specs

---

## 🔧 Configuración Técnica

### Servidores MCP Configurados

**Archivo**: `.vscode/mcp.json`

```json
{
  "servers": {
    "spec-workflow-root": {
      "command": "npx",
      "args": ["-y", "@pimzino/spec-workflow-mcp@latest",
               "c:/proyectos/aleia-melquisedec"]
    },
    "spec-workflow-R000-autopoietic-template": {
      "command": "npx",
      "args": ["-y", "@pimzino/spec-workflow-mcp@latest",
               "C:/proyectos/aleia-melquisedec/apps/R000-autopoietic-template"]
    }
  }
}
```

### Por Qué Hay 2 Servidores
- **Root**: Para specs del monorepo principal (Monorepo Improvements)
- **R000**: Para specs específicos de la app R000-autopoietic-template
- Ambos son independientes y pueden correr simultáneamente

---

## 📊 Verificar que Tu Spec Está Detectado

### Desde Terminal
```bash
# Cambiar al directorio del proyecto
cd C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template

# Ver estado del spec
npx -y @pimzino/spec-workflow-mcp@latest spec-status \
  --specName spec-001-built-template-spec-workflow
```

**Salida Esperada:**
```
✅ Specification 'spec-001-built-template-spec-workflow' status: implementing
   Phases: Requirements (created), Design (created), Tasks (created)
   Implementation: 0/26 completed, 26 pending
```

### Desde Copilot Chat
```
@workspace /spec-status spec-001-built-template-spec-workflow
```

---

## 🎯 Iniciar Trabajo en una Tarea

### Paso 1: Revisar la Tarea
**Dashboard Web**: http://localhost:5000
- Selecciona proyecto: R000-autopoietic-template
- Click en spec: spec-001-built-template-spec-workflow
- Click en "Tasks" para ver la lista completa
- Selecciona **Task 1.1**: "Crear Schema JSON-LD Keter-Doc"

### Paso 2: Marcar como In Progress
**Opción A - Dashboard Web:**
- Click en el botón "Start" o cambiar estado a "In Progress"

**Opción B - Editar tasks.md directamente:**
```markdown
# ANTES
- [ ] 1.1. Crear Schema JSON-LD Keter-Doc

# DESPUÉS
- [-] 1.1. Crear Schema JSON-LD Keter-Doc
```

### Paso 3: Implementar
Lee el campo **_Prompt** de la tarea para guía detallada:
```
Role: Schema Architect
Task: Create JSON-LD schema v1.0.0 with MELQUISEDEC ontology
Restrictions: Must validate against JSON-LD 1.1 spec
Success: Schema validates, all vocabularies included
```

### Paso 4: Loguear Implementación
Después de completar la tarea:
```bash
log-implementation \
  --specName spec-001-built-template-spec-workflow \
  --taskId 1.1 \
  --summary "Created JSON-LD schema with MELQUISEDEC ontology" \
  --artifacts '{"schemas": [...]}' \
  --filesCreated "[\"packages/core-mcp/schemas/keter-doc-protocol-v1.0.0.jsonld\"]" \
  --statistics '{"linesAdded": 150, "linesRemoved": 0}'
```

### Paso 5: Marcar como Completada
```markdown
# tasks.md
- [x] 1.1. Crear Schema JSON-LD Keter-Doc
```

---

## 🔍 Troubleshooting

### "No veo mi spec en el dropdown"
✅ **Solución**: Estás viendo el servidor MCP incorrecto
- Dashboard web: Cambia el selector de proyecto en la parte superior
- Panel VS Code: Cambia de servidor MCP (ver métodos arriba)

### "El dashboard no carga"
✅ **Verificar**: ¿Está corriendo el servidor?
```bash
# Iniciar dashboard si no está corriendo
cd C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template
npx -y @pimzino/spec-workflow-mcp@latest --dashboard
```

### "Las tareas no se detectan"
✅ **Verificar formato**: El formato debe ser:
```markdown
- [ ] X.Y. Task Title    ← CORRECTO (punto después del número)
- [ ] X.Y Task Title     ← INCORRECTO (sin punto)
#### TASK-X.Y:          ← INCORRECTO (formato antiguo)
```

### "Cambios en tasks.md no se reflejan"
✅ **Refrescar**: El dashboard actualiza automáticamente, pero puedes forzar:
- Dashboard web: F5 para recargar
- Panel VS Code: Recargar ventana (Ctrl+Shift+P → Reload Window)

---

## 📚 Referencias

- **Spec Location**: `apps/R000-autopoietic-template/.spec-workflow/specs/spec-001-built-template-spec-workflow/`
- **Tasks File**: `tasks.md` (26 tareas en formato spec-workflow-mcp)
- **Backup Original**: `tasks.md.backup` (formato antiguo incompatible)
- **Dashboard**: http://localhost:5000
- **MCP Config**: `.vscode/mcp.json`

---

## ✅ Status Actual

- ✅ Dashboard corriendo en http://localhost:5000
- ✅ 2 proyectos detectados (root + R000)
- ✅ 26 tareas parseadas correctamente
- ✅ Formato compatible con spec-workflow-mcp
- ✅ Listo para iniciar implementación

---

**Próximo paso**: Abre http://localhost:5000, selecciona "R000-autopoietic-template", y comienza con la tarea 1.1 🚀
