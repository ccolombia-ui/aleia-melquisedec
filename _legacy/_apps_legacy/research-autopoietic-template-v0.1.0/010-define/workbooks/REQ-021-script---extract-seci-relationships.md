---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-021'
dc:title: 'REQ-021: Script - Extract SECI Relationships'
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

# REQ-021: Script - Extraer SECI Relationships

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: intermedio
- **associated_causes**: cause-knowledge-graph
- **associated_features**: feat-seci-extractor
- **priority**: Alto
- **type**: Herramienta
- **effort**: 8 horas

---

## Resumen

Create tools/keterdoc/extract-seci-relationships.py to build dependency graph.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Script - Extraer SECI Relationships como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create tools/keterdoc/extract-seci-relationships.py to build dependency graph.

### 2.2 Criterios de Aceptación

- [ ] File: `tools/keterdoc/extract-seci-relationships.py`
- [ ] CLI: `extract-seci-relationships.py --path apps/ --output seci-graph.json`
- [ ] Parses Todos artifacts, extracts seci.derives_from and seci.informs
- [ ] Outputs graph JSON: nodes (artifacts) + edges (relationships)
- [ ] Detects cycles: warns if circular Dependencias found
- [ ] Generates Mermaid diagram: `--formato mermaid` option
- [ ] Pruebas unitarias: 5 Probar cases (simple graph, cycles, orphaned nodes)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-001, REQ-002

**Método de Validación**: Generates graph from 50 Probar artifacts

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
