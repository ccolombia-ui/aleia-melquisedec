---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-023'
dc:title: 'REQ-023: Script - YAML-LD to RDF Triples'
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

# REQ-023: Script - YAML-LD to RDF Triples

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: inmediato
- **associated_causes**: cause-rdf-generation
- **associated_features**: feat-rdf-converter
- **priority**: Crítico
- **type**: Herramienta
- **effort**: 16 horas

---

## Resumen

Create tools/neo4j/yaml-ld-to-rdf-triples.py to convert YAML-LD to RDF.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Script - YAML-LD to RDF Triples como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create tools/neo4j/yaml-ld-to-rdf-triples.py to convert YAML-LD to RDF.

### 2.2 Criterios de Aceptación

- [ ] File: `tools/neo4j/yaml-ld-to-rdf-triples.py`
- [ ] usa rdflib library for RDF generation
- [ ] CLI: `yaml-ld-to-rdf-triples.py --input concept.md --output concept.ttl --format turtle`
- [ ] Supports formats: turtle, n-triples, json-ld, xml
- [ ] Batch mode: processes entire directory
- [ ] Validates @context against context.jsonld
- [ ] Generates triples for: dc fields, seci relationships, artifact typing
- [ ] Pruebas unitarias: 10 Probar cases (simple, complex, invalid)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-001, REQ-002

**Método de Validación**: Generates valid RDF triples for 20 Probar artifacts

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
