# 05-outputs/ - ALMA (Publicación)

Esta carpeta contiene los outputs listos para publicación.

## ⚠️ ESTRUCTURA DIVERGENTE

El contenido de esta carpeta **diverge según `type` en ISSUE.yaml**:

- **research** → papers, reportes, visualizaciones
- **app** → documentación de usuario, releases, API docs
- **social-project** → informes, capacitación, difusión

Ver secciones específicas abajo.

---

## Rostro DAATH-ZEN

**ALMA** (Publicación): Transforma artifacts en outputs publicables para audiencias específicas.

## Checkpoint

**CK-04**: Validar que outputs están listos para publicación antes de archivar.

## HKM Type

Todos los archivos en esta carpeta deben tener `hkm_type: output` (publicación).

---

## 5A. Research Type

```
05-outputs/
├── papers/              # Artículos académicos
│   ├── paper-draft-v1.md
│   └── paper-final.pdf
├── reports/             # Reportes técnicos
│   ├── technical-report.md
│   └── technical-report.pdf
├── visualizations/      # Gráficas publication-ready
│   ├── figure-1-architecture.png
│   └── figure-2-results.png
└── presentations/       # Slides
    ├── conference-talk.pptx
    └── defense-slides.pdf
```

### Template para Technical Report

```markdown
---
hkm_type: output
epistemic_level: output
title: "[TÍTULO_REPORTE]"
created: YYYY-MM-DD
tags: [report, research, publication, alma]
synthesis_from:
  - ../../04-artifacts/notebooks/*.ipynb
  - ../../03-workbook/analysis/*.md
---

# [TÍTULO_REPORTE]

**Authors**: [Nombres]
**Date**: [YYYY-MM-DD]
**Version**: 1.0.0

## Abstract

[Resumen ejecutivo 150-250 palabras]

## 1. Introduction

### 1.1. Background
[Contexto del problema]

### 1.2. Research Questions
[Preguntas de investigación]

### 1.3. Contributions
[Qué aporta este trabajo]

## 2. Related Work

[Estado del arte basado en 01-literature/]

## 3. Methodology

[Metodología basada en 03-workbook/design/]

## 4. Results

### 4.1. Experimental Setup
[Configuración de experimentos]

### 4.2. Findings
[Resultados de 04-artifacts/notebooks/]

![Figure 1: Architecture](../visualizations/figure-1-architecture.png)

## 5. Discussion

[Interpretación de resultados]

## 6. Conclusions

[Conclusiones y trabajo futuro]

## References

[Bibliografía de 01-literature/references.bib]
```

### MCPs Recomendados (Research)

- **filesystem**: Generar archivos MD/PDF
- **python-env**: Ejecutar scripts de visualización

---

## 5B. App Type

```
05-outputs/
├── user-docs/           # Documentación de usuario
│   ├── getting-started.md
│   ├── user-guide.md
│   └── troubleshooting.md
├── releases/            # Release notes, binarios
│   ├── CHANGELOG.md
│   └── release-v1.0.0.md
├── demos/               # Material demo
│   ├── demo-video.mp4
│   └── screenshots/
└── api-docs/            # API reference
    └── index.html (auto-generado)
```

### Template para User Documentation

```markdown
---
hkm_type: output
epistemic_level: output
title: "User Guide - [APP_NAME]"
created: YYYY-MM-DD
tags: [user-docs, app, publication, alma]
synthesis_from:
  - ../../04-artifacts/src/
---

# [APP_NAME] User Guide

## 1. Introduction

[Qué hace la aplicación]

## 2. Installation

### Prerequisites
- [Requisito 1]
- [Requisito 2]

### Steps
```bash
# Paso 1
command-1

# Paso 2
command-2
```

## 3. Getting Started

### Quick Start
```bash
# Comando básico
app-command --help
```

### Your First Workflow
[Tutorial paso a paso con screenshots]

## 4. Features

### Feature 1
[Descripción y ejemplos]

### Feature 2
[Descripción y ejemplos]

## 5. Troubleshooting

**Problem**: [Descripción]
**Solution**: [Solución paso a paso]

## 6. FAQ

**Q: [Pregunta]?**
A: [Respuesta]
```

### MCPs Recomendados (App)

- **filesystem**: Generar documentación
- **python-refactoring**: Auto-generar API docs (Sphinx/MkDocs)

---

## 5C. Social-Project Type

```
05-outputs/
├── reports/             # Informes de proyecto
│   ├── final-report.md
│   └── impact-report.pdf
├── training/            # Material de capacitación
│   ├── facilitator-manual.md
│   └── participant-workbook.pdf
├── outreach/            # Material de difusión
│   ├── infographic.png
│   ├── social-media-posts.md
│   └── video-script.md
└── impact/              # Métricas de impacto
    └── impact-metrics.md
```

### Template para Final Report

```markdown
---
hkm_type: output
epistemic_level: output
title: "Final Report - [PROJECT_NAME]"
created: YYYY-MM-DD
tags: [report, social-project, publication, alma]
synthesis_from:
  - ../../04-artifacts/methodologies/*.md
  - ../../03-workbook/analysis/*.md
---

# [PROJECT_NAME] Final Report

**Project Period**: [Start] - [End]
**Organization**: [Nombre]
**Team**: [Nombres]

## Executive Summary

[Resumen ejecutivo 1-2 páginas]

## 1. Context and Justification

[Por qué se hizo este proyecto]

## 2. Objectives

### General Objective
[Objetivo general]

### Specific Objectives
1. [Objetivo 1] - ✅ Achieved / ⚠️ Partial / ❌ Not Achieved
2. [Objetivo 2] - Status
3. [Objetivo 3] - Status

## 3. Methodology

[Metodología aplicada de 04-artifacts/methodologies/]

## 4. Activities Implemented

### Activity 1: [Título]
- **When**: [Fecha]
- **Participants**: [N personas]
- **Results**: [Descripción]

## 5. Results and Impact

### Quantitative Metrics
| Metric | Target | Achieved | % |
|--------|--------|----------|---|
| [Métrica 1] | [Target] | [Real] | [%] |

### Qualitative Impact
[Testimonios, cambios observados]

## 6. Lessons Learned

[De 06-lessons/]

## 7. Recommendations

[Recomendaciones para futuros proyectos]

## 8. Sustainability Plan

[Cómo se sostendrá el proyecto]

## Appendices

- Appendix A: Instrumentos utilizados
- Appendix B: Listados de participantes
```

### MCPs Recomendados (Social-Project)

- **filesystem**: Generar informes y material
- **markitdown**: Convertir a PDF

---

## Criterios de Validación (Común a Todos)

- [ ] Outputs están completos y revisados
- [ ] Cada output tiene HKM header válido
- [ ] Outputs listos para audiencia target
- [ ] Referencias a artifacts y análisis

## Quality Checklist

### Research
- [ ] Reporte técnico ≥20 páginas
- [ ] ≥5 visualizaciones publication-ready
- [ ] Bibliografía completa
- [ ] Resultados reproducibles

### App
- [ ] User docs completa y testeable
- [ ] API docs auto-generadas
- [ ] Release notes con changelog
- [ ] Demos funcionales

### Social-Project
- [ ] Informe con métricas de impacto
- [ ] Material de capacitación validado
- [ ] Material de difusión diseñado
- [ ] Plan de sostenibilidad documentado

---

**Ver**: [requirements.md](../requirements.md) § 3.4, [tasks.md](../tasks.md) § PHASE 4, [design.md](../design.md) § 5.3
