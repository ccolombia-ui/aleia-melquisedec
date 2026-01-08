---
id: "implementacion-03-checklist-research-instance"
is_a: "implementation/checklist"
version: "4.0.0"
dc:
  title: "Checklist: Validación de Research Instance"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["Checklist", "Validación", "Quality Gate"]
seci:
  derives_from: ["../02-arquitectura/01-research-instance.md", "../03-workflow/02-trazabilidad.md"]
  informs: ["../04-implementacion/01-flujo-completo.md"]
---

# Checklist para Validar una Research Instance

- [ ] Carpetas `0-inbox/` a `5-outputs/` existen y son coherentes
- [ ] `_melquisedec/metadata.yaml` presente y válido
- [ ] Todos los `.md` tienen header HKM válido (`validate-metadata.py`)
- [ ] `seci.derives_from` apunta a artifacts existentes
- [ ] `seci.informs` actualizado cuando aplica
- [ ] Outputs están versieonados y tienen `git_tag`
- [ ] Tests y checks CI pasan
- [ ] Lessons learned documentadas (si aplica)
- [ ] Tracing (Neo4j) no reporta ciclos no-intencionados
- [ ] WIP y Kanban rules respetadas

## Gate de Publicación
La instancia puede publicarse si todos los checks anteriores son `true` y la revisión por pares está aprobada.

---

**Versión**: 4.0.0
**Última actualización**: 2026-01-08
