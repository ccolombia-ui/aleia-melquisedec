---
id: ISSUE-003
title: Add pre-commit hooks configuration
type: enhancement
area: automation
priority: medium
status: open
created: 2026-01-08
assignee: null
tags: [automation, quality, ci-cd]
related_issues: [ISSUE-001, ISSUE-004]
---

# ISSUE-003: Add pre-commit hooks configuration

## 📌 Objetivo

Implementar pre-commit hooks para automatizar validaciones de código y mantener la calidad del monorepo antes de cada commit.

## 📖 Contexto

Actualmente no hay validaciones automáticas antes de commits, lo que puede llevar a:
- Commits con imports rotos
- Código Python sin formatear (inconsistente PEP8)
- Links markdown rotos en documentación
- Archivos con trailing whitespace
- Secrets accidentalmente commiteados

**Solución**: Implementar [pre-commit](https://pre-commit.com/) con hooks que validen calidad antes de permitir commits.

## 💡 Solución Propuesta

Crear `.pre-commit-config.yaml` en la raíz con hooks para:

### 1. Validaciones generales
- `trailing-whitespace`: Eliminar espacios al final de líneas
- `end-of-file-fixer`: Asegurar newline al final de archivos
- `check-yaml`: Validar sintaxis de YAML
- `check-json`: Validar sintaxis de JSON
- `check-added-large-files`: Prevenir commits de archivos >500KB
- `detect-private-key`: Detectar claves privadas accidentales

### 2. Python
- `black`: Auto-formatear código Python
- `isort`: Ordenar imports automáticamente
- `flake8`: Linting (PEP8 compliance)
- `mypy`: Type checking (opcional, si usamos type hints)

### 3. Documentación
- Custom hook para `validate_doc_links.py`: Validar links markdown
- `markdownlint`: Validar sintaxis markdown

### 4. Git
- `check-merge-conflict`: Detectar markers de merge conflicts
- `no-commit-to-branch`: Prevenir commits directos a `main`

## 🛠️ Implementación

### Paso 1: Instalar pre-commit
```powershell
# Instalar pre-commit globalmente
pip install pre-commit

# O agregarlo a requirements.txt del proyecto
echo "pre-commit>=3.5.0" >> requirements.txt
```

### Paso 2: Crear .pre-commit-config.yaml
```yaml
# .pre-commit-config.yaml
repos:
  # Hooks generales
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
        args: ['--maxkb=500']
      - id: detect-private-key
      - id: check-merge-conflict
      - id: no-commit-to-branch
        args: ['--branch', 'main']

  # Python formatting
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3
        args: ['--line-length=100']

  # Import sorting
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ['--profile', 'black', '--line-length=100']

  # Python linting
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=100', '--extend-ignore=E203,W503']

  # Markdown linting (opcional)
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.38.0
    hooks:
      - id: markdownlint
        args: ['--fix']

  # Custom: Validate doc links
  - repo: local
    hooks:
      - id: validate-doc-links
        name: Validate Markdown Links
        entry: python tools/maintenance/validate_doc_links.py
        language: system
        files: \.md$
        pass_filenames: false
```

### Paso 3: Instalar hooks
```powershell
# Instalar hooks en el repositorio local
pre-commit install

# Probar en todos los archivos
pre-commit run --all-files
```

### Paso 4: Configurar pyproject.toml (para black/isort)
```toml
# pyproject.toml (crear en raíz si no existe)
[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directorios a excluir
  \.git
  | \.venv
  | venv
  | __pycache__
  | build
  | dist
)/
'''

[tool.isort]
profile = "black"
line_length = 100
skip_gitignore = true
```

### Paso 5: Crear flake8 config
```ini
# .flake8 (crear en raíz)
[flake8]
max-line-length = 100
extend-ignore = E203, W503
exclude =
    .git,
    __pycache__,
    .venv,
    venv,
    build,
    dist
```

### Paso 6: Actualizar CONTRIBUTING.md
Agregar sección sobre pre-commit hooks:
```markdown
## Pre-commit Hooks

Este proyecto usa pre-commit hooks para mantener calidad de código.

### Setup
```bash
pip install pre-commit
pre-commit install
```

### Uso
Los hooks se ejecutan automáticamente en cada commit.

Para ejecutar manualmente:
```bash
pre-commit run --all-files
```

Para saltar hooks (no recomendado):
```bash
git commit --no-verify
```
```

## ✅ Criterios de Aceptación

1. ✅ **Archivo de configuración creado**:
   - `.pre-commit-config.yaml` existe en raíz
   - Incluye hooks para Python, YAML, markdown, y custom

2. ✅ **Configuraciones adicionales**:
   - `pyproject.toml` configurado para black/isort
   - `.flake8` configurado con reglas del proyecto

3. ✅ **Hooks instalados**:
   - `pre-commit install` ejecutado exitosamente
   - `.git/hooks/pre-commit` existe

4. ✅ **Validación funciona**:
   - `pre-commit run --all-files` se ejecuta sin errores críticos
   - Hooks detectan problemas comunes (trailing whitespace, formato, etc.)

5. ✅ **Documentación actualizada**:
   - CONTRIBUTING.md explica cómo usar pre-commit
   - README menciona pre-commit como parte del setup

## 🧪 Testing

### Manual Testing
```powershell
# 1. Instalar y configurar
pip install pre-commit
pre-commit install

# 2. Ejecutar en todos los archivos
pre-commit run --all-files

# 3. Probar con commit de prueba
echo "test  " > test_trailing.txt  # Trailing whitespace intencional
git add test_trailing.txt
git commit -m "test: trailing whitespace"
# Debe fallar y auto-fix

# 4. Verificar hooks instalados
cat .git/hooks/pre-commit  # Debe contener script de pre-commit

# 5. Limpiar test
git reset HEAD test_trailing.txt
rm test_trailing.txt
```

### Automated Testing (CI)
```yaml
# En .github/workflows/pre-commit.yml (futuro)
name: Pre-commit Checks
on: [push, pull_request]
jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - uses: pre-commit/action@v3.0.0
```

## 📚 Referencias

- **Pre-commit docs**: https://pre-commit.com/
- **Black formatter**: https://black.readthedocs.io/
- **isort**: https://pycqa.github.io/isort/
- **flake8**: https://flake8.pycqa.org/
- **Hooks repository**: https://github.com/pre-commit/pre-commit-hooks

## 📝 Notas Adicionales

### Hooks opcionales a considerar después:
- `mypy`: Type checking (requiere type hints en código)
- `bandit`: Security linting para Python
- `commitizen`: Validar conventional commits
- `prettier`: Formatear JSON/YAML/MD

### Estrategia de adopción gradual:
1. **Fase 1** (este issue): Hooks básicos (trailing whitespace, end-of-file, check-yaml)
2. **Fase 2**: Python formatting (black, isort) - puede requerir reformatear codebase
3. **Fase 3**: Linting estricto (flake8, mypy) - puede requerir fixes extensos
4. **Fase 4**: Custom hooks (validate_doc_links, etc.)

### Manejo de reformateo masivo:
Si black/isort cambian muchos archivos:
```powershell
# Ejecutar y auto-fix todo
pre-commit run --all-files

# Revisar cambios
git diff

# Commit reformateo en commit separado
git add .
git commit -m "style: apply black and isort formatting

Applied automatic code formatting with black and isort
to entire codebase. No functional changes.

Refs: ISSUE-003"
```

### Configuración recomendada para equipos:
- `--no-verify` solo para emergencias
- CI debe ejecutar pre-commit en PRs
- Documentar excepciones en CONTRIBUTING.md

---

**Estado**: 🔴 OPEN  
**Estimación**: 1-2 horas (setup) + tiempo de reformateo si es necesario  
**Bloqueadores**: Ninguno  
**Dependencias**: Se beneficia de ISSUE-001 (validate_doc_links.py debe existir)
