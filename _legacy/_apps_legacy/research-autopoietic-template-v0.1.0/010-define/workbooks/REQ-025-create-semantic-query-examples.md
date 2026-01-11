---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-025'
dc:title: 'REQ-025: Create Semantic Query Examples'
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

# REQ-025: Crear Semantic Query Examples

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: final
- **associated_causes**: cause-knowledge-queries
- **associated_features**: feat-semantic-queries
- **priority**: Alto
- **type**: Documentación
- **effort**: 8 horas

---

## Resumen

Crear tools/neo4j/semantic-queries/ con 10 queries Cypher de ejemplo.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Crear Semantic Query Examples como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Crear tools/neo4j/semantic-queries/ con 10 queries Cypher de ejemplo.

### 2.2 Criterios de Aceptación

- [ ] Carpeta: `tools/neo4j/semantic-queries/`
- [ ] 10 files: query-01 hasta query-10 (.cypher extension)
- [ ] Queries cover: concept lineage, knowledge flow, orphaned concepts, artifact counts, collaboration, patterns, temporal evolution, circular Dependencias, trazabilidad reports
- [ ] Each query includes: Descripción, example usage, expected output
- [ ] README.md with query explanations

## 3. Dependencias y Restricciones

**Dependencias**: REQ-024

**Método de Validación**: Todos 10 queries Ejecutar successfully on Probar data

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
