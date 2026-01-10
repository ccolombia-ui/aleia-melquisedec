---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/requirements/REQ-006-output-tpl'
dc:title: 'REQ-006: Create Base Template - Output Artifact'
dc:created: '2026-01-10'
version: '0.1.0'
status: 'draft'
result_type: 'final'
associated_causes:
  - 'cause-006-deliverables'
associated_features:
  - 'feat-output-artifacts'
outputs:
  immediate: 'artifact-templates/by-type/output-tpl.md'
  intermediate: 'Output examples (datasets, tools)'
  final: 'Published outputs and documentation'
generated_from: '_templates/daath-zen-patterns/daath-zen-req-template.md'
template_root: '_templates/daath-zen-patterns/template-configurable_daath-zen-root.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '380-420'
    rationale: 'Output template for deliverables.'
---

# REQ-006: Crear Base Plantilla - Output Artifact

**Priority**: Alto
**Type**: Plantilla
**Effort**: 8 horas

## 1. Planteamiento del Problema

Entregable outputs must conform to a Plantilla to enable consistent publication, indexing, and ingestion.

## 2. Resumen

An output Plantilla will standardize Metadatos and secciones for datasets, tools, and papers to make them easier to index and reuse.

## 3. Next Steps

- Crear example output artifacts
- Add guidance on licensing and provenance fields
- Ensure outputs include `generated_from` and `template_root` for traceability

---

*Generado via daath-zen-req-Plantilla (stub).*
