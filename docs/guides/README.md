# Guías del Proyecto

Guías prácticas para setup, configuración y workflows del monorepo.

## 📄 Guías Disponibles

### Setup y Configuración
- [[configuracion-completa]] - **Guía completa de configuración**
  - Instalación de dependencias
  - Setup de MCP servers
  - Configuración de Neo4j
  - Testing y validación

- [[docker-mcp-toolkit]] - **Docker MCP Toolkit**
  - Arquitectura del sistema
  - 19 MCP servers disponibles
  - Métricas y troubleshooting

### Workflows
- [[estrategia-branching]] - **Estrategia de Git branching**
  - Feature branches
  - Release workflow
  - Hotfix process

- [[git-push-workflow]] - **Workflow de Git Push**
  - Automated push con .gitpush.yml
  - Configuración y templates

- [[workflows-github-actions]] - **GitHub Actions CI/CD**
  - Pipelines de testing
  - Deployment automation

### Migraciones y Reorganización
- [[migracion-estructura]] - **Tabla de migración de archivos**
  - Mapping ANTES → DESPUÉS
  - Estado de cada archivo movido

- [[reorganizacion-completa]] - **Resumen de reorganización** (movido desde raíz en 2026-01-08)
  - Motivación y contexto
  - Cambios estructurales
  - Impacto y validación

### Referencias Rápidas
- [[quick-reference]] - **Quick Reference** (movido desde raíz en 2026-01-08)
  - Comandos frecuentes
  - Cheatsheet de MCP servers
  - Shortcuts útiles

- [[kanban-estados]] - **Estados del Kanban** (movido desde raíz en 2026-01-08)
  - Definición de estados
  - Transiciones permitidas
  - Criterios de aceptación

## 🎯 Archivos Movidos en Task 1.2 (2026-01-08)

- ✅ `QUICK_REFERENCE.md` → `guides/quick-reference.md`
- ✅ `REORGANIZACION_COMPLETA.md` → `guides/reorganizacion-completa.md`
- ✅ `01-kanban-estados.md` → `guides/kanban-estados.md`

**Historial Git preservado** mediante `git mv`.

## 🔗 Enlaces Relacionados

- **Arquitectura**: [../architecture/](../architecture/)
- **Manifiesto**: [../manifiesto/](../manifiesto/)
- **Root README**: [[README]]
