# Meta-Información del Monorepo

Esta carpeta contiene la gestión interna del monorepo `aleia-melquisedec`.

---

## 📂 Estructura

```
_meta/
├── inbox/           # Issues activos (specs, propuestas, bugs)
├── done/            # Issues completados (archivo histórico)
├── templates/       # Templates para crear nuevos issues
├── roadmap.md       # Roadmap general del monorepo
└── README.md        # Este archivo
```

---

## 🎯 ¿Qué son los Issues?

Los **issues** son especificaciones de trabajo para mejorar el monorepo. Incluyen:
- Bugs a corregir
- Features a implementar
- Mejoras de documentación
- Refactorings necesarios

---

## 📝 Crear un Nuevo Issue

### 1. Usar Template

```powershell
# Copiar template
cp docs/_meta/templates/issue-template.md docs/_meta/inbox/ISSUE-XXX-descripcion.md

# Editar
code docs/_meta/inbox/ISSUE-XXX-descripcion.md
```

### 2. Metadata Requerida

```yaml
---
id: "ISSUE-001"
title: "Título descriptivo"
type: "enhancement"              # bug, enhancement, documentation, infrastructure
area: "tools"                    # packages, tools, docs, infrastructure, ci-cd
priority: "high"                 # low, medium, high, critical
status: "open"                   # open, in-progress, blocked, done
created: "YYYY-MM-DD"
assignee: "MELQUISEDEC"
tags: 
  - "tag1"
  - "tag2"
---
```

### 3. Contenido Mínimo

- **Objetivo**: ¿Qué se quiere lograr?
- **Contexto**: ¿Por qué es necesario?
- **Solución Propuesta**: ¿Cómo se implementará?
- **Criterios de Aceptación**: ¿Cómo sabemos que está done?

---

## 🔄 Workflow Issue → Implementation

```
1. CREAR ISSUE
   └── Escribir en docs/_meta/inbox/ISSUE-XXX.md

2. IMPLEMENTAR (con LLM como asistente)
   ├── Usar issue como prompt/contexto
   ├── Generar código en packages/, tools/, etc.
   └── Documentar en docs/

3. VALIDAR
   ├── Tests manuales
   ├── CI/CD automático
   └── Review

4. CERRAR
   ├── Marcar status: "done" en metadata
   ├── Mover a docs/_meta/done/
   └── Referenciar en commit: "closes ISSUE-XXX"
```

---

## 📋 Organización de Issues

### Estructura Flat (Actual)

Todos los issues en `inbox/` con tags en metadata para filtrar.

**Filtrar por área:**
```powershell
# Ver issues de packages
grep -l "area: \"packages\"" docs/_meta/inbox/*.md

# Ver issues de alta prioridad
grep -l "priority: \"high\"" docs/_meta/inbox/*.md
```

### Cuando Reorganizar

Si `inbox/` crece más de 20 issues, considerar organizar por carpetas:
- `inbox/packages/`
- `inbox/tools/`
- `inbox/infrastructure/`
- `inbox/docs/`

---

## 🎯 Diferencia: Issues de Monorepo vs Apps

| Aspecto | Issues de Monorepo | Issues de Apps |
|---------|-------------------|----------------|
| **Ubicación** | `docs/_meta/inbox/` | `apps/XX-nombre/0-inbox/` |
| **Propósito** | Mejorar infraestructura | Investigación específica |
| **Resultado** | Código en packages/tools | Outputs en 5-outputs/ |
| **Workflow** | Issue → Code → PR | Issue → Research → Output |

---

## 📚 Referencias

- [CONTRIBUTING.md](../../CONTRIBUTING.md) - Guía de contribución completa
- [ARQUITECTURA_MONOREPO.md](../../ARQUITECTURA_MONOREPO.md) - Estructura del monorepo
- [roadmap.md](roadmap.md) - Roadmap y prioridades

---

**Última actualización**: 2026-01-08
