---
id: ISSUE-004
title: Package daath-toolkit formally with pyproject.toml
type: enhancement
area: packages
priority: medium
status: open
created: 2026-01-08
assignee: null
tags: [packaging, python, distribution]
related_issues: [ISSUE-003]
---

# ISSUE-004: Package daath-toolkit formally with pyproject.toml

## 📌 Objetivo

Convertir `packages/daath-toolkit/` en un paquete Python instalable y distribuible, con metadata formal y configuración moderna usando `pyproject.toml`.

## 📖 Contexto

Actualmente, `daath-toolkit` tiene la siguiente estructura:
```
packages/daath-toolkit/
├── capture/
│   ├── __init__.py
│   └── chatlog_capture.py
├── storage/
│   ├── __init__.py
│   └── vector_store.py
├── generators/
│   └── new_research.py
├── validators/
│   └── validate_research.py
└── testing/
    └── (tests)
```

**Problemas**:
- No tiene `pyproject.toml` ni `setup.py` → no es instalable con pip
- No tiene metadata (versión, autor, dependencias, entry points)
- No tiene README propio explicando el paquete
- Imports requieren paths complejos: `from packages.daath_toolkit.capture...`
- No puede publicarse en PyPI ni instalarse en otros proyectos

**Solución**: Usar PEP 517/518 con `pyproject.toml` moderno.

## 💡 Solución Propuesta

Crear estructura de paquete Python moderna:

```
packages/daath-toolkit/
├── pyproject.toml           # ← Configuración principal (PEP 517/518)
├── README.md                # ← Documentación del paquete
├── LICENSE                  # ← Licencia (o link a raíz)
├── src/
│   └── daath_toolkit/       # ← Source layout (mejores prácticas)
│       ├── __init__.py
│       ├── capture/
│       ├── storage/
│       ├── generators/
│       └── validators/
└── tests/                   # ← Tests separados de src
    ├── test_capture.py
    ├── test_storage.py
    └── ...
```

**Nota**: Usar "src layout" es best practice para evitar import accidents durante desarrollo.

## 🛠️ Implementación

### Paso 1: Crear pyproject.toml

```toml
# packages/daath-toolkit/pyproject.toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "daath-toolkit"
version = "0.1.0"
description = "DAATH toolkit for autopoietic research capture and knowledge management"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "Aleia Team", email = "contact@example.com"}
]
keywords = ["research", "knowledge-management", "autopoiesis", "chatlog", "vector-store"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Researchers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]

dependencies = [
    "pyyaml>=6.0.0",
    "pinecone-client>=3.0.0",
    "openai>=1.0.0",
    "python-dateutil>=2.8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.12.0",
    "isort>=5.13.0",
    "flake8>=7.0.0",
    "mypy>=1.8.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/aleia-melquisedec"
Documentation = "https://github.com/yourusername/aleia-melquisedec/tree/main/docs"
Repository = "https://github.com/yourusername/aleia-melquisedec"
Issues = "https://github.com/yourusername/aleia-melquisedec/issues"

[project.scripts]
daath-capture = "daath_toolkit.capture.chatlog_capture:main"
daath-generate = "daath_toolkit.generators.new_research:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
include = ["daath_toolkit*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --cov=daath_toolkit --cov-report=term-missing"

[tool.black]
line-length = 100
target-version = ["py310"]

[tool.isort]
profile = "black"
line_length = 100

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true
```

### Paso 2: Crear README.md para el paquete

```markdown
# DAATH Toolkit

Toolkit para captura autopoiética de investigaciones y gestión de conocimiento.

## Características

- **Capture**: Captura de chatlogs con estructura DAATH por rostros
- **Storage**: Vector store domain-aware con Pinecone
- **Generators**: Generación de nuevas investigaciones desde templates
- **Validators**: Validación de estructura de investigaciones

## Instalación

### Desde source (desarrollo)
```bash
cd packages/daath-toolkit
pip install -e .[dev]
```

### Desde PyPI (futuro)
```bash
pip install daath-toolkit
```

## Uso Rápido

```python
from daath_toolkit.capture import ChatlogCapture
from daath_toolkit.storage import DomainAwareVectorStore

# Capturar chatlog
capture = ChatlogCapture(domain="physics", instance="quantum-computing")
capture.save_conversation(messages, metadata)

# Almacenar en vector store
store = DomainAwareVectorStore(domain="physics")
store.upsert_vectors(vectors, metadata)
```

## CLI

```bash
# Capturar chatlog
daath-capture --domain physics --instance quantum

# Generar nueva investigación
daath-generate --template daath --domain ai --instance agents
```

## Desarrollo

```bash
# Instalar con dependencias de desarrollo
pip install -e .[dev]

# Ejecutar tests
pytest

# Formatear código
black src/ tests/
isort src/ tests/

# Linting
flake8 src/ tests/
mypy src/
```

## Licencia

MIT - Ver LICENSE en la raíz del monorepo.
```

### Paso 3: Reorganizar a src layout

```powershell
# Crear estructura src
cd packages/daath-toolkit
New-Item -ItemType Directory -Force -Path "src/daath_toolkit"

# Mover módulos existentes a src
Move-Item capture/ src/daath_toolkit/
Move-Item storage/ src/daath_toolkit/
Move-Item generators/ src/daath_toolkit/
Move-Item validators/ src/daath_toolkit/

# Mover tests (si existen)
if (Test-Path testing/) {
    Move-Item testing/ tests/
}

# Crear __init__.py principal
@"
'''
DAATH Toolkit - Autopoietic Research Capture and Knowledge Management

Modules:
- capture: Chatlog capture with DAATH structure
- storage: Domain-aware vector storage
- generators: Research project generators
- validators: Research structure validators
'''

__version__ = '0.1.0'

from daath_toolkit.capture.chatlog_capture import ChatlogCapture
from daath_toolkit.storage.vector_store import DomainAwareVectorStore

__all__ = ['ChatlogCapture', 'DomainAwareVectorStore']
"@ | Out-File -Encoding utf8 src/daath_toolkit/__init__.py
```

### Paso 4: Actualizar imports en todo el proyecto

Buscar y reemplazar:
```powershell
# Antes:
from packages.daath_toolkit.capture.chatlog_capture import ChatlogCapture

# Después:
from daath_toolkit.capture import ChatlogCapture
```

### Paso 5: Instalar en modo desarrollo

```powershell
cd packages/daath-toolkit
pip install -e .[dev]
```

### Paso 6: Verificar instalación

```powershell
# Python interactivo
python -c "import daath_toolkit; print(daath_toolkit.__version__)"
# Output: 0.1.0

# CLI commands
daath-capture --help
daath-generate --help
```

## ✅ Criterios de Aceptación

1. ✅ **pyproject.toml completo**:
   - Metadata correcta (name, version, description)
   - Dependencies listadas
   - Optional dev dependencies
   - Scripts/entry points definidos

2. ✅ **Src layout implementado**:
   - Código en `src/daath_toolkit/`
   - Tests en `tests/`
   - README.md y LICENSE presentes

3. ✅ **Instalable con pip**:
   - `pip install -e .` funciona sin errores
   - `pip install -e .[dev]` instala deps de desarrollo

4. ✅ **Imports funcionan**:
   - `from daath_toolkit.capture import ChatlogCapture` funciona
   - CLI commands (`daath-capture`, `daath-generate`) funcionan

5. ✅ **Tests funcionan**:
   - `pytest` encuentra y ejecuta tests
   - Coverage reporta correctamente

6. ✅ **Documentación**:
   - README.md explica instalación y uso
   - docstrings en módulos principales

## 🧪 Testing

### Manual Testing
```powershell
# 1. Instalar paquete
cd packages/daath-toolkit
pip install -e .[dev]

# 2. Verificar versión
python -c "import daath_toolkit; print(daath_toolkit.__version__)"

# 3. Probar imports
python -c "from daath_toolkit.capture import ChatlogCapture; print('✅ Import OK')"

# 4. Probar CLI
daath-capture --help
daath-generate --help

# 5. Ejecutar tests
pytest -v

# 6. Verificar distribución
pip show daath-toolkit
```

### Build Testing
```powershell
# Construir distribución
python -m build

# Verificar que se crean dist/
ls dist/
# Debe mostrar: daath-toolkit-0.1.0.tar.gz, daath_toolkit-0.1.0-py3-none-any.whl
```

## 📚 Referencias

- **PEP 517**: Build system specification
- **PEP 518**: pyproject.toml specification
- **Setuptools docs**: https://setuptools.pypa.io/
- **Packaging guide**: https://packaging.python.org/
- **Src layout**: https://blog.ionelmc.ro/2014/05/25/python-packaging/

## 📝 Notas Adicionales

### Por qué src layout:
- Previene imports accidentales del desarrollo (imports deben venir de installed package)
- Separación clara entre source y tests
- Mejor aislamiento durante testing

### Versionado:
- Usar semantic versioning: MAJOR.MINOR.PATCH
- Mantener `__version__` sincronizado con pyproject.toml
- Considerar `setuptools_scm` para versioning automático desde git tags

### Publishing a PyPI (futuro):
```powershell
# Build
python -m build

# Upload a TestPyPI primero
twine upload --repository testpypi dist/*

# Luego a PyPI
twine upload dist/*
```

### Entry points adicionales a considerar:
```toml
[project.scripts]
daath-capture = "daath_toolkit.capture.chatlog_capture:main"
daath-generate = "daath_toolkit.generators.new_research:main"
daath-validate = "daath_toolkit.validators.validate_research:main"
daath-store = "daath_toolkit.storage.vector_store:cli_main"
```

### Integración con monorepo:
- Después de packaging, instalar desde `requirements.txt` en raíz:
  ```txt
  -e packages/daath-toolkit[dev]
  ```

---

**Estado**: 🔴 OPEN
**Estimación**: 2-3 horas
**Bloqueadores**: Ninguno
**Dependencias**: Se beneficia de ISSUE-003 (pre-commit para validar packaging)
