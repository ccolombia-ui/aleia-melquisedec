---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-013'
dc:title: 'REQ-013: Document Lens Selection Guide'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot'
version: '0.1.0'
status: 'draft'
template_root: 'template-configurable_daath-zen-root.md'
artifact_template: 'daath-zen-req-template.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'Requirement follows KeterDoc standard with RBM-GAC mapping.'
---

# REQ-013: Documentar Lens Selection Guide

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: final
- **associated_causes**: cause-keterdoc-usability
- **associated_features**: feat-lens-guide
- **priority**: Alto
- **type**: Documentación
- **effort**: 8 horas

---

## Resumen

Create docs/guides/LENS-SELECTION-GUIDE.md to help choose appropriate lens.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Documentar Lens Selection Guide como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create docs/guides/LENS-SELECTION-GUIDE.md to help choose appropriate lens.

### 2.2 Criterios de Aceptación

- [ ] File: `docs/guides/LENS-SELECTION-GUIDE.md`
- [ ] Decision matrix: Project Type → Recommended Lens
- [ ] Examples: 'Building a Herramienta? Use DSR', 'Quantitative study? Use IMRAD'
- [ ] Comparison Tabla showing differences between lenses
- [ ] Can combine lenses (e.g., DSR+DDD for software artifacts)
- [ ] Enlaces a manifesto's lens Documentación

## 3. Dependencias y Restricciones

**Dependencias**: REQ-009 hasta REQ-012

**Método de Validación**: Developers can select correct lens for their project type

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
