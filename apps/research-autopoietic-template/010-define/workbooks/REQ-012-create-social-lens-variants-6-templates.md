---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-012'
dc:title: 'REQ-012: Create Social Lens Variants (6 templates)'
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

# REQ-012: Crear Social variantes de lens (6 templates)

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: intermedio
- **associated_causes**: cause-keterdoc-lens-system
- **associated_features**: feat-social-templates
- **priority**: Medio
- **type**: Plantilla
- **effort**: 24 horas

---

## Resumen

Crear Social Science variantes de lens for qualitative research.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Crear Social variantes de lens (6 templates) como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Crear Social Science variantes de lens for qualitative research.

### 2.2 Criterios de Aceptación

- [ ] Carpeta: `artifact-templates/by-lens/social/`
- [ ] 6 files: concept-social-tpl.md, analysis-social-tpl.md, etc.
- [ ] Each Plantilla adapted for Social Science: Concept includes 'Social Context' and 'Stakeholder Perspectives', Analysis includes 'Qualitative Coding' section, Experiment includes 'Participant Demographics'
- [ ] README.md explains Social lens philosophy

## 3. Dependencias y Restricciones

**Dependencias**: REQ-002 hasta REQ-007

**Método de Validación**: Verify social science methods included

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
