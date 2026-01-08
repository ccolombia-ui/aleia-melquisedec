# Monorepo Improvements v1.1.0 - Design

## Architecture Overview

Este spec no introduce nueva arquitectura, sino que **consolida** la estructura existente. Los cambios son principalmente de organización y tooling.

```
[ANTES]                              [DESPUÉS]
─────────────────────────────────────────────────
nucleo-investigacion/ (eliminado)    
├── scripts/ ──────────────────────→ packages/daath-toolkit/
├── docs/ ─────────────────────────→ docs/manifiesto/03-workflow/
└── setup_*.sh ────────────────────→ tools/setup/

QUICK_REFERENCE.md (raíz) ─────────→ docs/guides/quick-reference.md
ARQUITECTURA_MONOREPO.md (raíz) ───→ docs/architecture/arquitectura-monorepo.md
... otros docs raíz ───────────────→ docs/*/

(sin pre-commit) ──────────────────→ .pre-commit-config.yaml
(sin pyproject) ───────────────────→ packages/daath-toolkit/pyproject.toml
(sin tests) ───────────────────────→ packages/daath-toolkit/tests/
```

## Component Design

### 1. REQ-1: Fix nucleo-investigacion references

**Estrategia**: Search & Replace sistemático

```python
# Mapeo de paths obsoletos → nuevos
PATH_MAPPING = {
    "nucleo-investigacion/scripts/chatlog_capture.py": 
        "packages/daath-toolkit/capture/chatlog_capture.py",
    "nucleo-investigacion/scripts/vector_store.py": 
        "packages/daath-toolkit/storage/domain_aware_vector_store.py",
    "nucleo-investigacion/docs/workflow-autopoiesis.md":
        "docs/manifiesto/03-workflow/05-autopoiesis.md",
    # ... etc
}

# Imports Python
IMPORT_MAPPING = {
    "from nucleo_investigacion.": "from packages.daath_toolkit.",
    "import nucleo_investigacion.": "import packages.daath_toolkit.",
}
```

**Herramienta**: Script Python con regex, no sed (cross-platform)

### 2. REQ-2: Move root docs

**Estrategia**: Git mv para preservar historial

```powershell
# Secuencia de comandos
git mv QUICK_REFERENCE.md docs/guides/quick-reference.md
git mv ESTRUCTURA_VISUAL.md docs/architecture/estructura-visual.md
git mv REORGANIZACION_COMPLETA.md docs/guides/reorganizacion-completa.md
git mv 01-kanban-estados.md docs/guides/kanban-estados.md
git mv ARQUITECTURA_MONOREPO.md docs/architecture/arquitectura-monorepo.md
```

**Post-move**: Actualizar links en README.md y otros archivos que referencien

### 3. REQ-3: Pre-commit hooks

**Configuración**:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks: [trailing-whitespace, end-of-file-fixer, check-yaml, check-json]
  
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks: [black]
  
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks: [isort]
  
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks: [flake8]
  
  - repo: local
    hooks:
      - id: validate-doc-links
        name: Validate markdown links
        entry: python tools/maintenance/validate_doc_links.py
        language: python
        files: \.md$
```

### 4. REQ-4: Package daath-toolkit

**Estructura final**:
```
packages/daath-toolkit/
├── pyproject.toml
├── README.md
├── src/
│   └── daath_toolkit/
│       ├── __init__.py
│       ├── capture/
│       │   ├── __init__.py
│       │   └── chatlog_capture.py
│       ├── storage/
│       │   ├── __init__.py
│       │   └── domain_aware_vector_store.py
│       ├── generators/
│       │   ├── __init__.py
│       │   └── new_research.py
│       └── validators/
│           ├── __init__.py
│           └── validate_research.py
└── tests/
    └── ...
```

### 5. REQ-5: Test suite

**Framework**: pytest + pytest-cov + pytest-mock

**Test strategy**:
- Unit tests: funciones individuales con mocks
- Integration tests: flujos completos con fixtures
- Fixtures: datos de ejemplo en tests/fixtures/

### 6. REQ-6: Validation script

**Checks implementados**:
```python
CHECKS = {
    "orphans": detect_orphan_files,
    "empty": find_empty_directories,
    "naming": validate_naming_conventions,
    "structure": validate_directory_structure,
    "deps": check_broken_imports,
    "legacy": find_legacy_references,
}
```

## Data Flow

No aplica - este spec es de reorganización, no de features funcionales.

## API Design

No aplica - no hay nuevas APIs.

## Security Considerations

- Pre-commit hook `detect-private-key` previene leak de secrets
- No se introducen nuevas dependencias con riesgos conocidos

## Testing Strategy

Ver REQ-5 en requirements.md y Task 5 en tasks.md.

## Migration Plan

1. Crear branch `feat/monorepo-improvements-v1.1.0`
2. Ejecutar tasks en orden
3. Validar con scripts de validación
4. PR a main con squash merge
5. Tag release v1.1.0
