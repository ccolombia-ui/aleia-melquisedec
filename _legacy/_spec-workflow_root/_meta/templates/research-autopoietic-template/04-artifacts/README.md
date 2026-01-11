# 04-artifacts/ - MORPHEUS (Implementación)

Esta carpeta contiene los artifacts implementados según el tipo de proyecto.

## ⚠️ ESTRUCTURA DIVERGENTE

El contenido de esta carpeta **diverge según `type` en ISSUE.yaml**:

- **research** → notebooks, scripts, modelos ML
- **app** → código fuente, tests, infraestructura
- **social-project** → metodologías, instrumentos, herramientas

Ver secciones específicas abajo.

---

## Rostro DAATH-ZEN

**MORPHEUS** (Implementación): Implementa diseño de 03-workbook/ en artifacts funcionales.

## Checkpoint

**CK-04**: Validar que artifacts están completos y funcionales antes de archivar.

## HKM Type

Todos los archivos en esta carpeta deben tener `hkm_type: artifact` (implementación).

---

## 4A. Research Type

```
04-artifacts/
├── notebooks/           # Jupyter notebooks de análisis
│   ├── 01-exploratory-analysis.ipynb
│   ├── 02-model-training.ipynb
│   └── 03-evaluation.ipynb
├── scripts/             # Scripts Python/R reutilizables
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── evaluation_metrics.py
├── models/              # Modelos ML/estadísticos entrenados
│   ├── model_v1.pkl
│   └── model_v2.onnx
└── data/                # Datasets procesados
    ├── processed/
    └── interim/
```

### Template para Notebook

```markdown
# [TÍTULO_NOTEBOOK]

**HKM Metadata** (como primera celda Markdown):
```yaml
---
hkm_type: artifact
epistemic_level: artifact
title: "[TÍTULO_NOTEBOOK]"
created: YYYY-MM-DD
tags: [notebook, analysis, research, morpheus]
synthesis_from:
  - ../../03-workbook/design/architecture.md
---
```

## 1. Objetivo

[Qué análisis realiza este notebook]

## 2. Setup

```python
import pandas as pd
import numpy as np
# ... imports
```

## 3. Análisis

[Celdas de código con análisis]

## 4. Resultados

[Interpretación de resultados]

## 5. Conclusiones

[Conclusiones del análisis]
```

### MCPs Recomendados (Research)

- **python-env**: Gestionar entorno Python
- **activate-python-environment-tools**: Activar entorno correcto
- **activate-notebook-configuration-tools**: Configurar notebooks

---

## 4B. App Type

```
04-artifacts/
├── src/                 # Código fuente
│   ├── domain/            # Entidades de dominio
│   ├── application/       # Use cases
│   ├── infrastructure/    # Adapters
│   └── interfaces/        # APIs, CLI
├── tests/               # Test suite
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                # Documentación técnica
│   └── api/
└── infrastructure/      # Docker, K8s, CI/CD
    ├── docker/
    └── k8s/
```

### Template para Source Code

```python
"""
Module: [nombre_modulo].py

HKM Metadata:
---
hkm_type: artifact
epistemic_level: artifact
title: "[MÓDULO]"
created: YYYY-MM-DD
tags: [code, app, morpheus]
synthesis_from:
  - ../../03-workbook/design/architecture.md
---
"""

from typing import Protocol

class MyPort(Protocol):
    """Port definition following design."""

    def method(self, param: str) -> str:
        """Method docstring."""
        ...
```

### MCPs Recomendados (App)

- **python-refactoring**: Refactorizar código
- **python-env**: Gestionar dependencias
- **activate-python-code-validation-and-execution**: Validar sintaxis

---

## 4C. Social-Project Type

```
04-artifacts/
├── methodologies/       # Guías metodológicas
│   ├── implementation-guide.md
│   └── facilitation-manual.md
├── instruments/         # Instrumentos de recopilación
│   ├── survey-template.md
│   ├── interview-guide.md
│   └── observation-form.md
├── tools/               # Herramientas de facilitación
│   ├── workshop-canvas.pdf
│   └── activity-cards.md
└── resources/           # Material educativo
    ├── presentations/
    └── handouts/
```

### Template para Methodology

```markdown
---
hkm_type: artifact
epistemic_level: artifact
title: "[TÍTULO_METODOLOGÍA]"
created: YYYY-MM-DD
tags: [methodology, social-project, morpheus]
synthesis_from:
  - ../../03-workbook/design/architecture.md
---

# [TÍTULO_METODOLOGÍA]

## 1. Objetivo

[Para qué sirve esta metodología]

## 2. Participantes

- **Target**: [Quiénes]
- **Facilitadores**: [Roles]

## 3. Duración

[Tiempo estimado]

## 4. Materiales Necesarios

- [Material 1]
- [Material 2]

## 5. Pasos

### Paso 1: [Título]
[Descripción detallada]

### Paso 2: [Título]
[Descripción detallada]

## 6. Resultados Esperados

[Qué se obtiene al final]

## 7. Tips y Recomendaciones

[Mejores prácticas]
```

### MCPs Recomendados (Social-Project)

- **filesystem**: Crear/editar archivos
- **markitdown**: Convertir formatos

---

## Criterios de Validación (Común a Todos)

- [ ] Artifacts implementan diseño de 03-workbook/
- [ ] Cada artifact tiene HKM header válido
- [ ] Artifacts son funcionales (ejecutables/aplicables)
- [ ] Documentación inline completa

## Testing Requirements

### Research
- [ ] Notebooks ejecutables sin errores
- [ ] Scripts tienen docstrings y ejemplos
- [ ] Resultados reproducibles

### App
- [ ] Tests unitarios coverage ≥80%
- [ ] Tests de integración pasan
- [ ] SonarQube quality gates ✅

### Social-Project
- [ ] Metodologías validadas con piloto
- [ ] Instrumentos revisados por expertos
- [ ] Material educativo probado

---

**Ver**: [requirements.md](../requirements.md) § 3.3, [tasks.md](../tasks.md) § PHASE 4, [design.md](../design.md) § 5.3
