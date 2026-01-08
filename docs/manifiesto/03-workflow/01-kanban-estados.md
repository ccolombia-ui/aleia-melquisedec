---
id: "workflow-01-kanban-estados"
is_a: "workflow/spec"
version: "4.0.0"
dc:
  title: "Estados Kanban y Reglas de Transición"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["Kanban", "Workflow", "Gestión de Issues"]
seci:
  derives_from: ["../01-fundamentos/04-principios-fundacionales.md"]
  informs: ["../02-arquitectura/01-research-instance.md", "../04-implementacion/01-flujo-completo.md"]
---

# Kanban: Estados y Reglas de Transición

## Objetivo
Definir el conjunto de estados y las reglas mínimas para gestionar issues e items en `0-inbox/` y Kanban de MELQUISEDEC.

## Estados Definidos
- **backlog**: Items identificados pero no priorizados.
- **todo**: Seleccionados para ejecución próxima.
- **in-progress**: Trabajo activo; asignado a un rostro.
- **review**: Revisión por pares o por rostro responsable.
- **blocked**: Bloqueado por dependencia externa o requisito faltante.
- **done**: Trabajo completado y preparado para publicación.
- **archived**: Histórico, no activo.

## Reglas de Transición (Principales)
1. Todo item nace en `backlog` dentro de `0-inbox/`.
2. Solo el *lead* (MELQUISEDEC) puede mover un item de `backlog` → `todo` tras priorizar.
3. `todo` → `in-progress` ocurre cuando un rostro se asigna al item.
4. `in-progress` → `review` cuando todas las subtareas y criterios de aceptación están cumplidos.
5. `review` → `done` cuando la revisión esté aprobada; si no, regresa a `in-progress` con comentarios.
6. Cualquier estado → `blocked` si hay una dependencia o impedimento.
7. `done` → `archived` por rutina de limpieza o al publicar output.

## WIP (Work In Progress) Limits
- Por rostro: máximo 3 items `in-progress` simultáneos.
- Por proyecto: configurable según tamaño, ejemplo 8.

## Automatizaciones recomendadas
- Integración con CI para mover a `review` cuando todos los checks pasen.
- Scripts que detecten `blocked` por dependencias no resueltas.
- Webhooks que actualicen `seci.informs` cuando un output se publique.

## Mapping a HKM Issues
Todos los estados deben reflejarse en `status` dentro del header HKM:
```
status: "in-progress"  # uno de backlog|todo|in-progress|review|blocked|done|archived
```

## Buenas Prácticas
- Mantener `description` y `acceptance_criteria` en cada issue.
- Registrar dependencias explícitas en `dependencies`.
- Usar labels con `rostro` y `domain` para filtrado.

## Ejemplo de Issue (Resumen)
```yaml
---
id: "ISSUE-101"
is_a: "issue"
version: "1.0.0"
dc:
  title: "Investigar integración CI para pipelines"
  creator: ["MELQUISEDEC"]
  date: "2026-01-08"
seci:
  derives_from: []
status: "in-progress"
assigned_to: "SALOMON"
dependencies: ["ISSUE-099"]
---
```

---

**Referencias**: `01-kanban-estados.md` → `02-trazabilidad.md`, `03-versionamiento.md`

**Versión**: 4.0.0
**Última actualización**: 2026-01-08
