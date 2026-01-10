---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-028'
dc:title: 'REQ-028: Migrate ISSUE.yaml to ISSUE.md'
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

# REQ-028: Migrate ISSUE.yaml to ISSUE.md

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: intermedio
- **associated_causes**: cause-Migración
- **associated_features**: feat-issue-Migración
- **priority**: Crítico
- **type**: Migración
- **effort**: 4 horas

---

## Resumen

Convert research-autopoietic-template/ISSUE.yaml → ISSUE.md.

---

## 1. Planteamiento del Problema

This requirement addresses the need for Migrate ISSUE.yaml to ISSUE.md as part of the KeterDoc architecture implementation (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Convert research-autopoietic-template/ISSUE.yaml → ISSUE.md.

### 2.2 Criterios de Aceptación

- [ ] File: `research-autopoietic-template/ISSUE.md` (NEW)
- [ ] Contains YAML-LD frontmatter with KeterDoc Metadatos
- [ ] All ISSUE.yaml data preserved in Markdown body
- [ ] Validation: passes validate-keterdoc-compliance.py
- [ ] ISSUE.yaml renamed to ISSUE.yaml.deprecated (not deleted)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-018, REQ-020, REQ-027

**Validation Method**: ISSUE.md validates, spec-workflow-mcp reads it successfully

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
