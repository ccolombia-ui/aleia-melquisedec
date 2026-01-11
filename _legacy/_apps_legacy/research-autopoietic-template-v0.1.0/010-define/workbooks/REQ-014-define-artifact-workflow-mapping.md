---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-014'
dc:title: 'REQ-014: Define Artifact-Workflow Mapping'
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

# REQ-014: Define Artifact-Workflow Mapping

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: inmediato
- **associated_causes**: cause-workflow-automatización
- **associated_features**: feat-pattern-mapping
- **priority**: Crítico
- **type**: Configuración
- **effort**: 8 horas

---

## Resumen

Create config/artifact-workflows.yaml mapping artifact types to workflow patterns.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Define Artifact-Workflow Mapping como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create config/artifact-workflows.yaml mapping artifact types to workflow patterns.

### 2.2 Criterios de Aceptación

- [ ] File: `config/artifact-workflows.yaml`
- [ ] Maps 28+ artifact types to patterns (e.g., concept → PATTERN-003-Conceptualize)
- [ ] Includes lens overrides (e.g., concept + DSR → PATTERN-003-DSR variant)
- [ ] Documents confidence score initialization (0.50 for new patterns)
- [ ] Version tracking (patterns can evolve v1.0.0 → v1.1.0)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-002 hasta REQ-007

**Método de Validación**: Todos artifact types have assigned pattern

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
