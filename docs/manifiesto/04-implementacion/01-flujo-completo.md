---
id: "implementacion-01-flujo-completo"
is_a: "implementation/guide"
version: "4.0.0"
dc:
  title: "Flujo Completo de Implementación: De Issue a Output"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["Flujo", "Implementación", "Checklist"]
seci:
  derives_from: ["../02-arquitectura/01-research-instance.md", "../03-workflow/01-kanban-estados.md"]
  informs: ["../04-implementacion/02-lessons-learned.md", "../04-implementacion/03-checklist-research-instance.md"]
---

# Flujo Completo de Implementación

Breve guía paso a paso desde la creación de un issue hasta la publicación de un output.

## Pasos Principales
1. **Creación** (MELQUISEDEC)
   - Issue creado en `0-inbox/` con HKM header y `status: backlog`.
2. **Priorización** (MELQUISEDEC)
   - Mover a `todo` y asignar rostro.
3. **Investigación** (HYPATIA)
   - Llenar `1-literature/` y `2-atomic/` con sources y conceptos.
4. **Análisis** (SALOMON)
   - Productos en `3-workbook/`: decisiones, comparaciones, experimentos.
5. **Diseño** (MORPHEUS)
   - Templates y schemas en `4-dataset/`.
6. **Implementación & QA** (Equipo)
   - Tests, revisión (`review`), y resolución de dependencias.
7. **Publicación** (ALMA)
   - Crear folder versionado en `5-outputs/` y tag en Git.
8. **Retroalimentación**
   - Registrar lecciones en `02-lessons-learned.md` y actualizar metadata.

## Integraciones recomendadas
- CI para ejecutar checks y automatizar `review` → `done` cuando pasan tests.
- Validaciones de trazabilidad y metadata antes de publicar.

---

**Referencias**: `01-research-instance.md`, `03-versionamiento.md`, `03-checklist-research-instance.md`

**Versión**: 4.0.0
**Última actualización**: 2026-01-08
