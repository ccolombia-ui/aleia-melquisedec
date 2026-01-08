---
id: ISSUE-001
title: Fix all nucleo-investigacion references
type: maintenance
area: codebase
priority: high
status: open
created: 2026-01-08
assignee: null
tags: [cleanup, refactoring, post-reorganization]
related_issues: []
---

# ISSUE-001: Fix all nucleo-investigacion references

## 📌 Objetivo

Actualizar todas las referencias al antiguo directorio `nucleo-investigacion/` en scripts y documentación, ya que fue eliminado durante la reorganización.

## 📖 Contexto

Durante la reorganización del monorepo, eliminamos `nucleo-investigacion/` y redistribuimos su contenido:
- Scripts → `packages/daath-toolkit/` (capture/, storage/)
- Docs → `docs/manifiesto/03-workflow/`
- Setup scripts → `tools/setup/`

Sin embargo, pueden existir referencias antiguas en:
- Archivos markdown que documentan la estructura antigua
- Scripts que importan desde paths antiguos
- Configuraciones de Docker/Docker Compose
- Archivos de ejemplo o templates

## 💡 Solución Propuesta

1. Usar `grep` para encontrar todas las referencias:
   ```powershell
   grep -r "nucleo-investigacion" --include="*.md" --include="*.py" --include="*.yml" --include="*.yaml"
   ```

2. Actualizar según el tipo de archivo:
   - **Markdown**: Actualizar paths y ejemplos
   - **Python**: Cambiar imports a `packages.daath_toolkit.capture` / `.storage`
   - **Docker**: Actualizar volume mounts si existen
   - **Configs**: Actualizar rutas en YAML/JSON

3. Verificar con script de validación:
   ```powershell
   python tools/maintenance/validate_doc_links.py --report
   ```

## 🛠️ Implementación

### Paso 1: Búsqueda completa
```powershell
# Buscar en todo el workspace
cd c:\proyectos\aleia-melquisedec
grep -r "nucleo-investigacion" . --exclude-dir=".git" --exclude-dir="__pycache__"
```

### Paso 2: Categorizar referencias
- Crear lista de archivos afectados
- Clasificar por tipo (import, path, doc reference, config)
- Priorizar por impacto (código > docs > ejemplos)

### Paso 3: Actualización sistemática
```python
# Imports antiguos:
from nucleo_investigacion.scripts.chatlog_capture import ChatlogCapture

# Nuevos imports:
from packages.daath_toolkit.capture.chatlog_capture import ChatlogCapture
```

```markdown
<!-- Path antiguo -->
Ver [nucleo-investigacion/docs/workflow-autopoiesis.md](nucleo-investigacion/docs/workflow-autopoiesis.md)

<!-- Nuevo path -->
Ver [docs/manifiesto/03-workflow/05-autopoiesis.md](../../manifiesto/03-workflow/05-autopoiesis.md)
```

### Paso 4: Validación
- Ejecutar tests (si existen): `pytest packages/daath-toolkit/testing/`
- Validar links: `python tools/maintenance/validate_doc_links.py`
- Revisar imports: `python tools/maintenance/check_imports.py` (si existe)

## ✅ Criterios de Aceptación

1. ✅ **Búsqueda completa**:
   - `grep -r "nucleo-investigacion"` no devuelve resultados

2. ✅ **Imports funcionan**:
   - Todos los imports de `packages.daath_toolkit` se resuelven correctamente
   - No hay `ModuleNotFoundError` al ejecutar scripts

3. ✅ **Links válidos**:
   - `validate_doc_links.py` no reporta links rotos relacionados con nucleo-investigacion

4. ✅ **Documentación actualizada**:
   - README files reflejan nueva estructura
   - Diagramas de arquitectura actualizados (si existen)

## 🧪 Testing

### Manual Testing
```powershell
# 1. Verificar imports
python -c "from packages.daath_toolkit.capture.chatlog_capture import ChatlogCapture; print('✅ Import OK')"

# 2. Validar links en docs
python tools/maintenance/validate_doc_links.py --path docs/ --verbose

# 3. Buscar referencias restantes
grep -r "nucleo-investigacion" . --exclude-dir=".git" | wc -l  # Debe ser 0
```

### Automated Testing
```powershell
# Si existen tests unitarios
pytest packages/daath-toolkit/testing/ -v

# Ejecutar pre-commit hooks (cuando se implementen)
pre-commit run --all-files
```

## 📚 Referencias

- **Reorganización original**: [[reorganizacion-completa]]
- **Nueva estructura**: [[arquitectura-monorepo]]
- **Conversación**: Chatlog 2026-01-08 sobre eliminación de nucleo-investigacion

## 📝 Notas Adicionales

### Archivos críticos a revisar primero:
1. `docs/manifiesto/03-workflow/05-autopoiesis.md` (ya actualizado)
2. `ARQUITECTURA_MONOREPO.md` (puede mencionar estructura antigua)
3. `README.md` (puede tener ejemplos con paths antiguos)
4. `infrastructure/docker/docker-compose.yml` (puede tener volumes con paths antiguos)

### Riesgo bajo pero verificar:
- Templates en `_templates/` pueden tener ejemplos de la estructura antigua
- Configs en `packages/core-mcp/config/` pueden referenciar paths

---

**Estado**: 🔴 OPEN
**Estimación**: 1-2 horas
**Bloqueadores**: Ninguno
**Dependencias**: ISSUE-002 (mejora la validación de links)
