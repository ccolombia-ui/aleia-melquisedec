# .spec-workflow - Research Keter Migration

> **spec-workflow-mcp** configuration for DSR + DAATH-ZEN methodology

## 📂 Estructura (Formato Oficial)

```
.spec-workflow/
├── config.toml              # Configuración (opcional)
├── steering/                # Documentos de dirección
│   ├── product.md           # Visión del producto
│   ├── tech.md              # Stack técnico
│   └── structure.md         # Estructura del proyecto
├── specs/                   # Especificaciones (CADA SPEC ES UN FOLDER)
│   └── dependency-audit/    # ← FOLDER, no archivo
│       ├── requirements.md  # Requisitos
│       ├── design.md        # Diseño
│       └── tasks.md         # Tareas (formato específico)
├── approvals/               # (auto-generado) Aprobaciones pendientes
├── archive/                 # (auto-generado) Specs archivadas
└── README.md                # Este archivo
```

## ⚠️ IMPORTANTE: Formato de tasks.md

El archivo `tasks.md` debe seguir este formato específico:

```markdown
# Feature Tasks

## Section 1: Nombre de la sección

### 1.1 Nombre de la tarea
- [ ] Subtarea 1
- [ ] Subtarea 2

**Files**: `path/to/file.py`
**Requirements**: REQ-1, REQ-2

### 1.2 Otra tarea
- [x] Subtarea completada
- [ ] Subtarea pendiente

**Files**: `path/to/file.ts`
**Requirements**: REQ-3
```

## 🚀 Cómo Activar

### Opción 1: Dashboard + MCP Server (Recomendado)

```bash
# Terminal 1: Dashboard (una vez para todo)
npx -y @pimzino/spec-workflow-mcp@latest --dashboard

# Terminal 2: MCP Server para ESTE proyecto
cd C:\proyectos\aleia-melquisedec\apps\research-keter-migration
npx -y @pimzino/spec-workflow-mcp@latest .
```

Dashboard disponible en: http://localhost:5000

### Opción 2: Configuración MCP para VS Code

En tu archivo `mcp_settings.json` o configuración del cliente MCP:

```json
{
  "mcpServers": {
    "spec-keter-migration": {
      "command": "npx",
      "args": [
        "-y",
        "@pimzino/spec-workflow-mcp@latest",
        "C:/proyectos/aleia-melquisedec/apps/research-keter-migration"
      ]
    }
  }
}
```

### Opción 3: Multi-proyecto (Monorepo)

```bash
# Dashboard único
npx -y @pimzino/spec-workflow-mcp@latest --dashboard

# Cada proyecto en terminal separada
npx -y @pimzino/spec-workflow-mcp@latest C:/proyectos/aleia-melquisedec/apps/research-keter-migration
npx -y @pimzino/spec-workflow-mcp@latest C:/proyectos/aleia-melquisedec/apps/research-neo4j-llamaindex
```

Todos aparecerán en el mismo dashboard.

## 📋 Crear Nueva Spec

1. Crear folder en `specs/`:
   ```
   specs/nueva-spec/
   ```

2. Crear los 3 archivos obligatorios:
   - `requirements.md` - Qué se necesita
   - `design.md` - Cómo se hará
   - `tasks.md` - Tareas específicas

3. El MCP detectará automáticamente la nueva spec

## 🔄 Workflow de Aprobaciones

1. **Crear documento** → Se genera approval pendiente
2. **Aprobar en Dashboard/Extension** → Documento aprobado
3. **Siguiente documento** → Requiere aprobación del anterior

Orden obligatorio: `requirements` → `design` → `tasks`

## 🔗 Integración con DSR

| spec-workflow | DSR Phase | Ubicación en Proyecto |
|---------------|-----------|----------------------|
| `requirements.md` | Problem | También en `00-problem/` |
| `design.md` | Design | También en `01-design/` |
| `tasks.md` | Build/Evaluate | Referencia a `02-build/`, `03-evaluate/` |

## 🧘 Integración con DAATH-ZEN

Las validaciones de los 5 Rostros están en `.melquisedec/`:

```
.melquisedec/
├── hypatia_validation.yaml   # Research rigor
├── salomon_validation.yaml   # Architecture review
├── morpheus_validation.yaml  # Implementation quality
└── alma_validation.yaml      # Integration harmony
```

## 📊 Verificar Estado

```bash
# Ver specs detectadas (via MCP tool)
spec-list

# Ver estado de una spec
spec-status --specName dependency-audit

# Ver tareas
manage-tasks --specName dependency-audit --action list
```
