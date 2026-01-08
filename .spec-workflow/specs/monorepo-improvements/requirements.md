# Monorepo Improvements v1.1.0 - Requirements

## Overview

Este spec agrupa 6 mejoras críticas identificadas durante la auditoría post-reorganización del monorepo DAATH-ZEN. El objetivo es establecer una base sólida para el desarrollo continuo con calidad automatizada.

## User Stories

### US-1: Como desarrollador, quiero que no existan referencias rotas a `nucleo-investigacion`
- Para evitar confusión sobre la estructura actual
- Para que los imports funcionen correctamente
- **Relacionado**: ISSUE-001

### US-2: Como mantenedor, quiero que la raíz del proyecto esté limpia
- Para encontrar archivos rápidamente
- Para seguir convenciones de monorepos profesionales
- **Relacionado**: ISSUE-002

### US-3: Como contribuidor, quiero que el código sea validado automáticamente antes de commits
- Para mantener calidad consistente
- Para evitar romper el build accidentalmente
- **Relacionado**: ISSUE-003

### US-4: Como desarrollador, quiero instalar daath-toolkit con pip
- Para usar el paquete en otros proyectos
- Para tener dependencias claras y versionadas
- **Relacionado**: ISSUE-004

### US-5: Como desarrollador, quiero tests que validen la funcionalidad crítica
- Para refactorizar con confianza
- Para documentar el comportamiento esperado
- **Relacionado**: ISSUE-005

### US-6: Como mantenedor, quiero detectar problemas estructurales automáticamente
- Para prevenir degradación de la estructura
- Para facilitar contribuciones
- **Relacionado**: ISSUE-006

## Functional Requirements

### REQ-1: Cleanup de referencias obsoletas
- Eliminar todas las referencias a `nucleo-investigacion/`
- Actualizar imports Python a `packages.daath_toolkit.*`
- Actualizar links markdown a nuevas ubicaciones
- **Validación**: `grep -r "nucleo-investigacion"` retorna 0 resultados

### REQ-2: Reorganización de documentos raíz
- Mover QUICK_REFERENCE.md → docs/guides/
- Mover ESTRUCTURA_VISUAL.md → docs/architecture/
- Mover REORGANIZACION_COMPLETA.md → docs/guides/
- Mover 01-kanban-estados.md → docs/guides/
- Mover ARQUITECTURA_MONOREPO.md → docs/architecture/
- **Validación**: Raíz tiene ≤10 archivos

### REQ-3: Pre-commit hooks
- Instalar pre-commit framework
- Configurar hooks: trailing-whitespace, end-of-file-fixer, check-yaml
- Configurar formatters: black, isort
- Configurar linter: flake8
- Custom hook para validate_doc_links.py
- **Validación**: `pre-commit run --all-files` pasa sin errores

### REQ-4: Packaging formal de daath-toolkit
- Crear pyproject.toml con metadata completa
- Reestructurar a src/ layout
- Definir dependencias y opcionales
- Crear README.md del paquete
- **Validación**: `pip install -e packages/daath-toolkit` funciona

### REQ-5: Suite de tests
- Tests para chatlog_capture.py (≥80% coverage)
- Tests para vector_store.py (≥80% coverage)
- Fixtures con datos de ejemplo
- Mocks para dependencias externas (Pinecone, OpenAI)
- **Validación**: `pytest --cov` muestra ≥80%

### REQ-6: Script de validación estructural
- Expandir cleanup_post_reorganization.py
- Detectar: orphan files, empty dirs, naming violations
- Detectar: legacy references, broken imports
- Modo --fix para correcciones automáticas
- **Validación**: Script ejecuta sin findings críticos

## Non-Functional Requirements

### NFR-1: Performance
- Pre-commit hooks deben ejecutar en <30 segundos
- Tests deben correr en <2 minutos

### NFR-2: Mantenibilidad
- Código debe ser idempotente (ejecutar múltiples veces = mismo resultado)
- Cambios deben preservar historial Git (usar `git mv`)

### NFR-3: Documentación
- Cada script debe tener docstring con usage
- Cambios deben reflejarse en CHANGELOG.md

## Priority Order

1. **Alta**: REQ-1 (fix refs), REQ-5 (tests) - bloquean desarrollo
2. **Media**: REQ-2 (move docs), REQ-3 (pre-commit), REQ-4 (packaging)
3. **Baja**: REQ-6 (validation script) - nice to have

## Success Criteria

- [ ] Todos los REQs implementados y validados
- [ ] Todos los NFRs cumplidos
- [ ] CHANGELOG.md actualizado con v1.1.0
- [ ] Dashboard spec-workflow muestra 100% completado
