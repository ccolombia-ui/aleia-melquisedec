# Structure Steering - Principios Organizacionales

## 📐 Principio Fundamental: DAATH-ZEN Minimalista

> "Organizar por naturaleza, flat cuando sea posible, profundo solo cuando sea necesario"

## 🎯 Reglas de Estructura

### 1. Raíz del Proyecto
Solo archivos **críticos para setup inicial**:
- `README.md` - Entry point
- `CONTRIBUTING.md` - Guía de contribución (estándar GitHub)
- `LICENSE` - Licencia
- `CHANGELOG.md` - Historial de cambios
- `.spec-workflow/` - Workflow de especificaciones (spec-workflow-mcp)
- `.pre-commit-config.yaml` - Hooks de calidad (cuando se implemente)

### 2. Documentación en `docs/`
Toda documentación va en `docs/` organizada por **propósito**:
- `docs/manifiesto/` - Fundamentos filosóficos (inmutable)
- `docs/guides/` - Guías prácticas (evoluciona)
- `docs/architecture/` - ADRs y decisiones técnicas
- `docs/_meta/` - Meta-información del monorepo (issues legacy, roadmap)

### 3. Código en `packages/`
Paquetes Python reutilizables:
- Cada paquete debe tener `pyproject.toml`
- Cada paquete debe tener su propio `README.md`
- Structure: `src/` layout es preferido para packaging limpio

### 4. Aplicaciones en `apps/`
Una carpeta por domain/instance de investigación:
- Seguir template de `_templates/_daath-template/`
- Incluir `chatlog/`, `lessons/`, metadata

### 5. Scripts en `tools/`
Scripts operacionales organizados por fase:
- `tools/setup/` - Instalación y configuración inicial
- `tools/maintenance/` - Limpieza, validación, mantenimiento
- `tools/deployment/` - Despliegue y releases
- `tools/testing/` - Scripts de pruebas manuales/integración

## ✅ Validaciones de Estructura

Un archivo está **bien ubicado** si:
1. Su path refleja su naturaleza (código, docs, config)
2. No duplica información con otros archivos
3. Tiene al menos una referencia desde otro archivo (no huérfano)
4. Sigue las convenciones de nomenclatura del tipo

Un directorio está **bien organizado** si:
1. No tiene más de 2 niveles de anidamiento (excepto code)
2. No está vacío (excepto por `__init__.py`)
3. Tiene un propósito claro documentado en README o estructura superior

## 🔄 Workflow de Cambios Estructurales

1. **Propuesta**: Crear spec en `.spec-workflow/specs/`
2. **Revisión**: Solicitar approval via dashboard
3. **Implementación**: Ejecutar cambios con `git mv`
4. **Validación**: Ejecutar `validate_doc_links.py`
5. **Documentación**: Actualizar CHANGELOG.md
