---
id: ISSUE-002
title: Move root documentation files to docs/
type: maintenance
area: documentation
priority: medium
status: open
created: 2026-01-08
assignee: null
tags: [cleanup, documentation, structure]
related_issues: [ISSUE-001]
---

# ISSUE-002: Move root documentation files to docs/

## 📌 Objetivo

Mover archivos de documentación desde la raíz del proyecto a `docs/` para mantener una estructura limpia y predecible, siguiendo el principio de "organización por naturaleza".

## 📖 Contexto

Actualmente, la raíz del proyecto contiene varios archivos markdown que deberían estar en `docs/`:

```
/ (raíz)
├── QUICK_REFERENCE.md        → docs/guides/
├── ESTRUCTURA_VISUAL.md      → docs/architecture/
├── REORGANIZACION_COMPLETA.md → docs/guides/
├── 01-kanban-estados.md      → docs/_meta/ o docs/guides/
├── README.md                 → (mantener en raíz)
├── CONTRIBUTING.md           → (mantener en raíz)
├── LICENSE                   → (mantener en raíz)
├── CHANGELOG.md              → (mantener en raíz)
└── ARQUITECTURA_MONOREPO.md  → docs/architecture/
```

**Razón**: Siguiendo el principio minimalista de DAATH-ZEN:
- Raíz = solo archivos críticos para setup inicial (README, LICENSE, CONTRIBUTING, CHANGELOG)
- Docs auxiliares → `docs/` organizados por propósito

## 💡 Solución Propuesta

### Movimientos específicos:

1. **QUICK_REFERENCE.md** → `docs/guides/quick-reference.md`
   - Guía rápida de uso, pertenece a guides/

2. **ESTRUCTURA_VISUAL.md** → `docs/architecture/estructura-visual.md`
   - Documentación de arquitectura, pertenece a architecture/

3. **REORGANIZACION_COMPLETA.md** → `docs/guides/reorganizacion-completa.md`
   - Guía de reorganización histórica, pertenece a guides/

4. **01-kanban-estados.md** → `docs/guides/kanban-estados.md`
   - Documentación de workflow, pertenece a guides/

5. **ARQUITECTURA_MONOREPO.md** → `docs/architecture/arquitectura-monorepo.md`
   - Arquitectura general, pertenece a architecture/

### Archivos a MANTENER en raíz:
- ✅ README.md (entry point del proyecto)
- ✅ CONTRIBUTING.md (guía de contribución, estándar GitHub)
- ✅ LICENSE (licencia, requerido)
- ✅ CHANGELOG.md (historial de cambios, estándar)

## 🛠️ Implementación

### Paso 1: Mover archivos con Git
```powershell
# Preservar historial con git mv
git mv QUICK_REFERENCE.md docs/guides/quick-reference.md
git mv ESTRUCTURA_VISUAL.md docs/architecture/estructura-visual.md
git mv REORGANIZACION_COMPLETA.md docs/guides/reorganizacion-completa.md
git mv 01-kanban-estados.md docs/guides/kanban-estados.md
git mv ARQUITECTURA_MONOREPO.md docs/architecture/arquitectura-monorepo.md
```

### Paso 2: Actualizar referencias internas

Usar script de validación para encontrar links rotos:
```powershell
python tools/maintenance/validate_doc_links.py --report
```

Actualizar links en archivos que referencian estos documentos:
```powershell
# Buscar referencias a archivos movidos
grep -r "QUICK_REFERENCE\.md" docs/ README.md
grep -r "ESTRUCTURA_VISUAL\.md" docs/ README.md
grep -r "REORGANIZACION_COMPLETA\.md" docs/ README.md
grep -r "ARQUITECTURA_MONOREPO\.md" docs/ README.md
```

### Paso 3: Actualizar README.md principal

Si README.md linkea estos archivos, actualizar paths:
```markdown
<!-- Antes -->
Ver [Referencia Rápida](QUICK_REFERENCE.md)

<!-- Después -->
Ver [Referencia Rápida](docs/guides/quick-reference.md)
```

### Paso 4: Actualizar índices de documentación

Asegurar que `docs/README.md` (si existe) o índices en `docs/guides/README.md` y `docs/architecture/README.md` incluyan los archivos movidos.

## ✅ Criterios de Aceptación

1. ✅ **Archivos movidos correctamente**:
   - Todos los archivos listados están en sus nuevas ubicaciones
   - Historial Git preservado (usar `git mv`)

2. ✅ **Links actualizados**:
   - `validate_doc_links.py` no reporta links rotos
   - Todos los links desde README.md funcionan

3. ✅ **Raíz limpia**:
   - Solo quedan: README, CONTRIBUTING, LICENSE, CHANGELOG, directorios principales
   - No quedan archivos .md huérfanos

4. ✅ **Índices actualizados**:
   - `docs/guides/README.md` lista los nuevos archivos (si el índice existe)
   - `docs/architecture/README.md` lista los nuevos archivos (si existe)

5. ✅ **Naming conventions**:
   - Archivos renombrados a lowercase-kebab-case
   - Nombres descriptivos y consistentes

## 🧪 Testing

### Manual Testing
```powershell
# 1. Verificar que archivos existen en nueva ubicación
Test-Path docs/guides/quick-reference.md        # True
Test-Path docs/architecture/estructura-visual.md # True

# 2. Verificar que NO existen en raíz
Test-Path QUICK_REFERENCE.md                     # False
Test-Path ESTRUCTURA_VISUAL.md                   # False

# 3. Validar links
python tools/maintenance/validate_doc_links.py --verbose

# 4. Verificar historial Git preservado
git log --follow docs/guides/quick-reference.md  # Debe mostrar historial completo
```

### Automated Testing
```powershell
# Script de validación post-movimiento
python tools/maintenance/validate_structure.py --check-root-clean
```

## 📚 Referencias

- **Principio minimalista**: [docs/manifiesto/01-fundamentos/04-principios-fundacionales.md](../../manifiesto/01-fundamentos/04-principios-fundacionales.md)
- **Estructura target**: [docs/architecture/ADR-001-monorepo-structure.md](../../architecture/ADR-001-monorepo-structure.md)
- **Issue relacionado**: [ISSUE-001](ISSUE-001-fix-nucleo-refs.md) (actualizar referencias)

## 📝 Notas Adicionales

### Impacto en Obsidian:
- Si usas Obsidian con `c:\proyectos\aleia-melquisedec` como vault, los [[wikilinks]] se actualizarán automáticamente
- Si usas markdown links `[texto](path)`, necesitas actualizar manualmente o usar script

### Orden recomendado:
1. Primero mover archivos con `git mv`
2. Luego ejecutar `validate_doc_links.py --fix` para auto-corregir links simples
3. Revisar manualmente links complejos (con anchors, multi-hop, etc.)
4. Commit con mensaje descriptivo

### Mensaje de commit sugerido:
```
docs: reorganize root documentation files

Move auxiliary documentation from root to docs/ following
minimalist principle. Only README, CONTRIBUTING, LICENSE,
and CHANGELOG remain in root.

- QUICK_REFERENCE.md → docs/guides/quick-reference.md
- ESTRUCTURA_VISUAL.md → docs/architecture/estructura-visual.md
- REORGANIZACION_COMPLETA.md → docs/guides/reorganizacion-completa.md
- 01-kanban-estados.md → docs/guides/kanban-estados.md
- ARQUITECTURA_MONOREPO.md → docs/architecture/arquitectura-monorepo.md

All internal links updated accordingly.

Refs: ISSUE-002
```

---

**Estado**: 🔴 OPEN
**Estimación**: 30-45 minutos
**Bloqueadores**: Ninguno
**Dependencias**: Se beneficia de ISSUE-001 (script validate_doc_links.py)
