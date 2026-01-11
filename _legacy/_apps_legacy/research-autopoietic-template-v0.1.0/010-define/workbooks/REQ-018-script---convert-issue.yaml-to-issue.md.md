---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-018'
dc:title: 'REQ-018: Script - Convert ISSUE.yaml to ISSUE.md'
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

# REQ-018: Script - Convert ISSUE.yaml to ISSUE.md

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: inmediato
- **associated_causes**: cause-Migración-automatización
- **associated_features**: feat-yaml-converter
- **priority**: Crítico
- **type**: Herramienta
- **effort**: 12 horas

---

## Resumen

Create tools/keterdoc/convert-issue-yaml-to-md.py for automated migration.

---

## 1. Planteamiento del Problema

This requirement addresses the need for Script - Convert ISSUE.yaml to ISSUE.md as part of the KeterDoc architecture implementation (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create tools/keterdoc/convert-issue-yaml-to-md.py for automated migration.

### 2.2 Criterios de Aceptación

- [ ] File: `tools/keterdoc/convert-issue-yaml-to-md.py`
- [ ] Reads ISSUE.yaml, outputs ISSUE.md with YAML-LD frontmatter
- [ ] Preserves Todos data (problem, gap, goal → Markdown secciones)
- [ ] Adds KeterDoc Metadatos (id, is_a, dc, seci)
- [ ] CLI: `convert-issue-yaml-to-md.py --input ISSUE.yaml --output ISSUE.md --dry-run`
- [ ] Includes validation: warns if required fields missing
- [ ] Pruebas unitarias: 5 Probar cases (complete YAML, partial, invalid, etc.)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-001

**Validation Method**: Converts 5 test ISSUE.yaml files successfully

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
