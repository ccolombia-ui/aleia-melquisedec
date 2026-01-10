---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-019'
dc:title: 'REQ-019: Script - Generate Artifact from Template'
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

# REQ-019: Script - Generar Artifact from Plantilla

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: inmediato
- **associated_causes**: cause-artifact-generation
- **associated_features**: feat-Plantilla-generator
- **priority**: Crítico
- **type**: Herramienta
- **effort**: 12 horas

---

## Resumen

Create tools/keterdoc/generate-artifact-from-template.py for quick artifact creation.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Script - Generar Artifact from Plantilla como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create tools/keterdoc/generate-artifact-from-template.py for quick artifact creation.

### 2.2 Criterios de Aceptación

- [ ] File: `tools/keterdoc/generate-artifact-from-template.py`
- [ ] CLI: `generate-artifact-from-template.py concept 'Graph Databases' --lens dsr --output 020-conceive/02-atomics/concept-graph-databases.md`
- [ ] Automatically: Selects Plantilla, Generates unique id, Populates dc.date, Creates Archivo
- [ ] Interactive mode: prompts for missing values
- [ ] Validation: checks KeterDoc cumplimiento before writing
- [ ] Pruebas unitarias: 8 Probar cases (Todos combinations: type × lens)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-002 hasta REQ-012

**Método de Validación**: Generates 10 Probar artifacts successfully

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
