# Roadmap - Monorepo DAATH-ZEN MELQUISEDEC

> **Versión**: 1.0.0  
> **Última actualización**: 2026-01-08

---

## 🎯 Visión General

Este roadmap describe las mejoras planificadas para el monorepo `aleia-melquisedec`, organizado por fases y prioridades.

---

## 📊 Estado Actual

### ✅ Completado (v1.0.0)

- [x] Reorganización completa de estructura
- [x] Eliminación de `nucleo-investigacion/`
- [x] Creación de `packages/daath-toolkit/` con capture/ y storage/
- [x] Movimiento de scripts a `tools/`
- [x] Centralización de docs en `docs/`
- [x] Sistema de issues en `docs/_meta/inbox/`

### 🚧 En Progreso (v1.1.0)

- [ ] Actualizar referencias a `nucleo-investigacion` ([ISSUE-001](inbox/ISSUE-001-fix-nucleo-refs.md))
- [ ] Mover docs de raíz a `docs/` ([ISSUE-002](inbox/ISSUE-002-move-root-docs.md))
- [ ] Agregar pre-commit hooks ([ISSUE-003](inbox/ISSUE-003-add-precommit.md))

---

## 🗓️ Fases Planificadas

### Fase 1: Limpieza y Consolidación (v1.1.0) - Enero 2026

**Objetivo**: Completar la reorganización minimalista

**Issues:**
- ISSUE-001: Fix nucleo-investigacion references
- ISSUE-002: Move root docs to docs/
- ISSUE-003: Add pre-commit hooks
- ISSUE-004: Package daath-toolkit formally

**Criterio de Éxito**: Estructura 100% limpia, sin referencias antiguas

---

### Fase 2: Testing y CI/CD (v1.2.0) - Febrero 2026

**Objetivo**: Automatizar calidad de código

**Issues Planificados:**
- ISSUE-005: Add unit tests for capture/
- ISSUE-006: Add unit tests for storage/
- ISSUE-007: Add CI job for pre-commit
- ISSUE-008: Add coverage reporting

**Criterio de Éxito**: Coverage >80%, CI verde

---

### Fase 3: Packaging y Publishing (v2.0.0) - Q1 2026

**Objetivo**: Publicar packages reutilizables

**Issues Planificados:**
- ISSUE-009: Add pyproject.toml for daath-toolkit
- ISSUE-010: Add pyproject.toml for core-mcp
- ISSUE-011: Setup PyPI publishing workflow
- ISSUE-012: Add package documentation

**Criterio de Éxito**: Packages publicados en PyPI

---

### Fase 4: Infraestructura Avanzada (v2.1.0) - Q2 2026

**Objetivo**: Escalar para múltiples usuarios

**Issues Planificados:**
- ISSUE-013: Add Kubernetes configs
- ISSUE-014: Add Terraform IaC
- ISSUE-015: Setup monitoring (Prometheus/Grafana)
- ISSUE-016: Add backup/restore scripts

**Criterio de Éxito**: Deployment automatizado a cloud

---

## 📋 Backlog (Sin Prioridad Definida)

- [ ] Migrar a Poetry para gestión de dependencias
- [ ] Agregar Turborepo para builds optimizados
- [ ] Crear dashboard web para visualizar investigaciones
- [ ] Integrar con Notion API para sincronización
- [ ] Agregar support para multi-idioma en docs

---

## 🚀 Quick Wins (Pueden implementarse en cualquier momento)

- [ ] Agregar badges adicionales a README
- [ ] Crear video tutorial de setup
- [ ] Agregar ejemplos en `apps/` de investigaciones reales
- [ ] Mejorar templates con más opciones

---

## 🎯 Métricas de Éxito

### Calidad de Código
- Coverage: >80%
- Lint: 0 errores
- Type hints: >90%

### Documentación
- Orphan files: 0
- Broken links: 0
- Guías: >10

### Eficiencia
- Tiempo de setup: <10 min
- Tiempo de crear research: <1 min
- Tiempo de CI: <5 min

---

## 📊 Prioridades por Área

| Área | Prioridad | Issues |
|------|-----------|--------|
| **Limpieza** | 🔴 Alta | 001, 002 |
| **Automatización** | 🟡 Media | 003, 007 |
| **Testing** | 🟡 Media | 005, 006, 008 |
| **Packaging** | 🟢 Baja | 004, 009, 010 |
| **Infraestructura** | 🟢 Baja | 013-016 |

---

## 🔄 Proceso de Actualización

Este roadmap se actualiza:
- **Después de cada release**: Mover items completados
- **Mensualmente**: Re-priorizar según necesidades
- **Ad-hoc**: Cuando surgen issues críticos

---

## 📞 Feedback

Para sugerir cambios al roadmap, crear issue en `docs/_meta/inbox/` con:
- Tipo: `enhancement`
- Área: `roadmap`
- Tag: `roadmap-suggestion`

---

**Última revisión**: 2026-01-08  
**Próxima revisión**: 2026-02-01
