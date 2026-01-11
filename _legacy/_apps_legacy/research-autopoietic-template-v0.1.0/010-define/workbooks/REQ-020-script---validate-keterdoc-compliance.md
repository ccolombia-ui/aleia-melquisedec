---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-020'
dc:title: 'REQ-020: Script - Validate KeterDoc Compliance'
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

# REQ-020: Script - Validar KeterDoc cumplimiento

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: inmediato
- **associated_causes**: cause-quality-assurance
- **associated_features**: feat-validation-Herramienta
- **priority**: Crítico
- **type**: Herramienta
- **effort**: 12 horas

---

## Resumen

Create tools/keterdoc/validate-keterdoc-compliance.py for CI/CD validation.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Script - Validar KeterDoc cumplimiento como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create tools/keterdoc/validate-keterdoc-compliance.py for CI/CD validation.

### 2.2 Criterios de Aceptación

- [ ] File: `tools/keterdoc/validate-keterdoc-compliance.py`
- [ ] CLI: `validate-keterdoc-compliance.py --path apps/research-autopoietic-template/ --recursive`
- [ ] Validates: YAML-LD frontmatter present, KeterDoc fields present, dc.date formato (ISO 8601), seci.derives_from paths exist, artifact_template reference valid
- [ ] Output: JSON report with pass/fail + detailed errors
- [ ] Exit code 0 (pass) or 1 (fail) for CI/CD
- [ ] Pruebas unitarias: 10 Probar cases (valid, missing fields, invalid dates, etc.)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-001, REQ-002

**Método de Validación**: Validates 20 Probar artifacts, catches Todos intentional errors

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
