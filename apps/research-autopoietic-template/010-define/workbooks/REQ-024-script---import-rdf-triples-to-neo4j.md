---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-024'
dc:title: 'REQ-024: Script - Import RDF Triples to Neo4j'
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

# REQ-024: Script - Import RDF Triples to Neo4j

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: intermedio
- **associated_causes**: cause-neo4j-integration
- **associated_features**: feat-neo4j-importer
- **priority**: Crítico
- **type**: Herramienta
- **effort**: 16 horas

---

## Resumen

Create tools/neo4j/import-rdf-to-neo4j.py for RDF → Neo4j import.

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de Script - Import RDF Triples to Neo4j como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1 Descripción

Create tools/neo4j/import-rdf-to-neo4j.py for RDF → Neo4j import.

### 2.2 Criterios de Aceptación

- [ ] File: `tools/neo4j/import-rdf-to-neo4j.py`
- [ ] CLI: `import-rdf-to-neo4j.py --input concept.ttl --neo4j-uri bolt://localhost:7687`
- [ ] usa neosemantics (n10s) plugin for RDF import
- [ ] Creates nodes: (:Concept {id, title, version})
- [ ] Creates relationships: (:Concept)-[:DERIVES_FROM]->(:Paper)
- [ ] Batch import: processes directory of .ttl files
- [ ] Performance: imports 1000 artifacts in <5 minutes
- [ ] Dry-Ejecutar mode: shows Cypher queries without executing
- [ ] Pruebas unitarias: 8 Probar cases (simple, batch, error handling)

## 3. Dependencias y Restricciones

**Dependencias**: REQ-023

**Método de Validación**: Imports 100 Probar artifacts to Neo4j successfully

## 4. Guía de Implementación

This requirement should be implemented following the DAATH-ZEN configurable Plantilla pattern and validated against the Criterios de Aceptación listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
