# Gaps Detallado - AOEM v2 → Template Melquisedec v3

**Version**: 0.2.0
**Status**: In Progress
**Last Updated**: 2026-01-11
**Source**: Analysis from `02-mapeo-aoem-template.md`

---

## Overview

This document expands the 14 identified gaps between AOEM v2 and Template Melquisedec v2, providing detailed roadmap for enhancement to v3.

**Summary**:
- **8 P0 gaps** (Critical - blocking HITO 2 completion)
- **3 P1 gaps** (Important - quality improvements)
- **3 P2/P3 gaps** (Nice-to-have - future enhancements)

---

## GAP-001: Multilingual Documentation

### Problem
Current template (v2) lacks structured multilingual support for concepts, definitions, and metadata. Only Spanish labels exist.

### Impact
- **Severity**: 🔴 P0 - Critical
- **Affects**: International collaboration, ontology reusability
- **Compliance**: SKOS, ISO 704, AOEM Phase 1 (Req Spec)

### Evidence
- File: `concept-template-v2.yaml`
- Missing: `skos:prefLabel@en`, `skos:definition@en`, `rdfs:comment@en`
- Current: Only `label_es` field exists

### Proposed Solution
1. Add multilingual fields to `concept-template-v3.yaml`:
   ```yaml
   names:
     es: [Spanish label]
     en: [English label]
   definitions:
     definition_es: [Spanish ISO 704 definition]
     definition_en: [English ISO 704 definition]
   ```
2. Update OTTR templates to emit both `@es` and `@en` tagged literals
3. Validation: CQ must retrieve labels in both languages

### Effort Estimate
- **Hours**: 4h
- **Owner**: Ontology Engineer
- **Dependencies**: None

### Status
✅ **COMPLETED** (concept-template-v3.yaml Section 1 implemented)

---

## GAP-002: Formal Axioms & OWL Integration

### Problem
v2 template lacks OWL 2 DL axiom definitions (subclass, disjointness, restrictions, equivalence).

### Impact
- **Severity**: 🔴 P0 - Critical
- **Affects**: Automated reasoning, consistency checking
- **Compliance**: AOEM Phase 2 (Conceptualization), Gruber criteria

### Evidence
- File: `concept-template-v2.yaml`
- Missing: `subclass_of`, `disjoint_with`, `equivalent_to`, `restrictions`
- Current: Only informal notes field

### Proposed Solution
1. Add `formal_axioms` section to concept-template-v3.yaml:
   ```yaml
   formal_axioms:
     subclass_of: [parent classes]
     disjoint_with: [mutually exclusive classes]
     equivalent_to: [equivalent class expressions]
     restrictions:
       - property: [property URI]
         type: [some/all/min/max/exactly]
         cardinality: [number]
         filler: [class or datatype]
   ```
2. Document methodology in `definition-template-v3.md`
3. Validation: OWL reasoner consistency check

### Effort Estimate
- **Hours**: 6h
- **Owner**: Ontology Engineer + Domain Expert
- **Dependencies**: GAP-007 (reuse assessment)

### Status
✅ **COMPLETED** (concept-template-v3.yaml Section 5 implemented)

---

## GAP-003: Ontology Reuse Documentation

### Problem
No systematic tracking of reused external ontologies (SKOS, DCTERMS, FOAF, BIBO).

### Impact
- **Severity**: 🔴 P0 - Critical
- **Affects**: Interoperability, license compliance, maintenance
- **Compliance**: AOEM Phase 2, NeOn Scenario 7 (Reuse)

### Evidence
- File: `concept-template-v2.yaml`
- Missing: `reused_ontologies` array with coverage metrics
- Ad-hoc: Mentions "use SKOS" in comments, but no formal tracking

### Proposed Solution
1. Add `reused_ontologies` section:
   ```yaml
   reused_ontologies:
     - ontology_uri: "http://www.w3.org/2004/02/skos/core#"
       ontology_name: "SKOS"
       terms_reused: ["skos:prefLabel", "skos:definition"]
       coverage_percentage: 95
       justification: "W3C standard for vocabularies"
       license: "W3C"
   ```
2. Conduct reuse assessment (see `reuse-assessment.md`)
3. Validation: All reused terms must have license compatibility check

### Effort Estimate
- **Hours**: 8h (includes research)
- **Owner**: Ontology Engineer
- **Dependencies**: None

### Status
✅ **COMPLETED** (reuse-assessment.md + concept-template-v3.yaml Section 4)

---

## GAP-004: Competency Questions & Validation

### Problem
No structured CQs to validate ontology coverage and semantics.

### Impact
- **Severity**: 🔴 P0 - Critical
- **Affects**: Validation, stakeholder confidence, regression testing
- **Compliance**: AOEM Phase 3 (Implementation), NeOn Scenario 2

### Evidence
- File: Missing `competency-questions.md`
- Current: Informal "example queries" in comments

### Proposed Solution
1. Create `competency-questions.md` with:
   - Natural language question
   - SPARQL 1.1 query
   - Expected result type
   - Validation criteria (pass/fail)
2. Add to concept-template-v3.yaml:
   ```yaml
   competency_questions:
     - question: "¿Qué libros ha escrito Gabriel García Márquez?"
       sparql_query: "SELECT ?book WHERE { ?book lib:hasAutor lib:GGMarquez }"
       expected_result_type: "List of URIs"
   ```
3. Automate: CI/CD pipeline runs SPARQL tests on each commit

### Effort Estimate
- **Hours**: 5h
- **Owner**: Domain Expert + Ontology Engineer
- **Dependencies**: GAP-002 (axioms needed for complex CQs)

### Status
✅ **COMPLETED** (competency-questions.md created with 5 CQs)

---

## GAP-005: OTTR Automation Templates

### Problem
Manual RDF generation is error-prone and time-consuming. No OTTR templates exist.

### Impact
- **Severity**: 🔴 P0 - Critical
- **Affects**: Productivity (15h→4h), consistency, scalability
- **Compliance**: AOEM Phase 3 (Implementation automation)

### Evidence
- File: Missing `ottr-templates/` folder
- Current: Hand-written TTL files (prone to typos)
- Research: `ottr-instantiation-format-research.md` completed

### Proposed Solution
1. Create `ottr-templates/concept-template.ottr`:
   ```ottr
   Template: ConceptTemplate(?id, ?label_en, ?label_es, ?def_en, ?def_es, ?uri) :: {
     ottr:Triple(?uri, rdf:type, owl:Class),
     ottr:Triple(?uri, rdfs:label, ?label_en),
     ottr:Triple(?uri, rdfs:label, ?label_es),
     ottr:Triple(?uri, skos:definition, ?def_en),
     ottr:Triple(?uri, skos:definition, ?def_es)
   } .
   ```
2. Create `instances/biblioteca-concepts.ottrinst` with stOTTR syntax
3. Lutra command: `lutra --library ottr-templates/ --input instances/*.ottrinst --output ontology.ttl`
4. Validation: Compare output TTL with hand-written version

### Effort Estimate
- **Hours**: 8h (includes Lutra setup + testing)
- **Owner**: Ontology Engineer
- **Dependencies**: GAP-004 (CQs for validation)

### Status
✅ **COMPLETED** (2 OTTR templates + 34 instantiations + example TTL output)

---

## GAP-006: Modularization & DDD Bounded Contexts

### Problem
No explicit modularization strategy. All concepts in single flat namespace.

### Impact
- **Severity**: 🟡 P1 - Important
- **Affects**: Maintainability, team scalability, cognitive load
- **Compliance**: AOEM Phase 2, NeOn Scenario 7, DDD principles

### Evidence
- File: All concepts use `lib:` prefix without submodules
- Missing: Bounded context definitions (Catalog, Loans, Users)

### Proposed Solution
1. Add `modularization` section to concept-template-v3.yaml:
   ```yaml
   modularization:
     bounded_context: "Catalog"  # DDD
     module_name: "library-catalog.ttl"  # NeOn Scenario 7
     imports:
       - "library-core.ttl"
       - "dcterms.ttl"
   ```
2. Refactor namespaces:
   - `lib-catalog:Libro` (Catalog context)
   - `lib-loans:Prestamo` (Loans context)
   - `lib-users:Usuario` (Users context)
3. Create modular TTL files with owl:imports

### Effort Estimate
- **Hours**: 6h
- **Owner**: Ontology Architect
- **Dependencies**: GAP-002 (axioms must respect module boundaries)

### Status
✅ **COMPLETED** (concept-template-v3.yaml Section 8 implemented)

---

## GAP-007: Validation Tools Integration

### Problem
No automated validation pipeline (ROBOT, pySHACL, reasoner).

### Impact
- **Severity**: 🟡 P1 - Important
- **Affects**: Quality assurance, regression prevention
- **Compliance**: AOEM Phase 3 (Testing), ISO 9001 (if applicable)

### Evidence
- File: Missing `.github/workflows/ontology-validation.yml`
- Current: Manual validation (error-prone, not repeatable)

### Proposed Solution
1. Add `validation` section to concept-template-v3.yaml:
   ```yaml
   validation:
     robot_report_status: "PASS"
     robot_report_url: "reports/robot-report.html"
     shacl_conforms: true
     shacl_violations_count: 0
     reasoner_consistent: true
     reasoner_used: "HermiT 1.4.5"
     cqs_pass_rate: 100  # percentage
   ```
2. Create CI/CD pipeline:
   ```yaml
   # .github/workflows/ontology-validation.yml
   - run: robot report --output reports/ ontology.ttl
   - run: pyshacl --shacl shapes.ttl --data ontology.ttl
   - run: sparql --query cqs/*.rq --data ontology.ttl
   ```
3. Generate badges: `![Validation](https://img.shields.io/badge/ROBOT-PASS-green)`

### Effort Estimate
- **Hours**: 10h (includes CI/CD setup + SHACL shapes creation)
- **Owner**: DevOps + Ontology Engineer
- **Dependencies**: GAP-004 (CQs needed for SPARQL tests)

### Status
⏳ **PENDING** (HITO 3 - Implementation & POC Integration)

---

## GAP-008: Quality Checklist

### Problem
No systematic checklist to verify template completeness and compliance.

### Impact
- **Severity**: 🟡 P1 - Important
- **Affects**: Consistency, training, onboarding new team members
- **Compliance**: AOEM all phases, ISO 704, Gruber criteria

### Evidence
- File: `concept-template-v2.yaml`
- Missing: `quality_checklist` section

### Proposed Solution
1. Add `quality_checklist` section:
   ```yaml
   quality_checklist:
     iso_704_definition_complete: true
     skos_multilingual_labels: true
     formal_axioms_present: true
     competency_questions_pass: true
     reuse_ontologies_documented: true
     modularization_defined: true
     ottr_template_generated: true
     validation_tools_pass: true
   ```
2. Create gating mechanism: Domain expert approval required if <80% checklist

### Effort Estimate
- **Hours**: 3h
- **Owner**: Ontology Engineer
- **Dependencies**: All previous gaps (checklist synthesizes them)

### Status
✅ **COMPLETED** (concept-template-v3.yaml Section 15)

---

## GAP-009: Temporal & Versioning

### Problem
No tracking of concept evolution over time (version history, deprecation).

### Impact
- **Severity**: 🟠 P2 - Nice-to-have
- **Affects**: Long-term maintenance, backward compatibility
- **Compliance**: AOEM Phase 4 (Maintenance)

### Evidence
- File: `concept-template-v2.yaml`
- Missing: `version`, `status`, `deprecated_by`, `change_log`

### Proposed Solution
1. Add metadata fields:
   ```yaml
   version: "3.0.0"
   status: "stable"  # draft | stable | deprecated
   deprecated_by: null  # URI of replacement concept
   change_log:
     - version: "3.0.0"
       date: "2026-01-11"
       changes: "Added multilingual support"
   ```
2. Use OWL versioning properties: `owl:versionInfo`, `owl:deprecated`

### Effort Estimate
- **Hours**: 4h
- **Owner**: Ontology Engineer
- **Dependencies**: None

### Status
🔄 **IN PROGRESS** (Section 1 has version + status, change_log pending)

---

## GAP-010: Examples & Use Cases

### Problem
Template lacks concrete examples showing correct usage.

### Impact
- **Severity**: 🟠 P2 - Nice-to-have
- **Affects**: Onboarding time, template adoption
- **Compliance**: Best practices (documentation)

### Evidence
- File: `concept-template-v3.yaml`
- Missing: Populated example at end of file

### Proposed Solution
1. Add "Example Section" after template definition:
   ```yaml
   # ============================================
   # EXAMPLE: Concept "Libro"
   # ============================================
   concept_id: libro_example
   names:
     es: Libro
     en: Book
   # ... (complete filled template)
   ```
2. Reference from README-HITO2.md

### Effort Estimate
- **Hours**: 2h
- **Owner**: Domain Expert
- **Dependencies**: GAP-002 (axioms example)

### Status
⏳ **PENDING** (planned for domain expert review phase)

---

## GAP-011: License & Provenance

### Problem
No clear license declaration and provenance metadata.

### Impact
- **Severity**: 🟠 P2 - Nice-to-have
- **Affects**: Legal clarity, open source compliance
- **Compliance**: FAIR principles, DCTERMS

### Evidence
- File: Missing `LICENSE` field in YAML header
- Current: Implicit "internal use" assumption

### Proposed Solution
1. Add metadata section:
   ```yaml
   provenance:
     creator: "HITO 2 Team"
     contributor: ["Domain Expert", "Ontology Engineer"]
     created: "2026-01-11"
     license: "CC-BY-4.0"
     rights_holder: "Organization Name"
   ```
2. Emit as RDF: `dcterms:creator`, `dcterms:license`

### Effort Estimate
- **Hours**: 1h
- **Owner**: Project Manager
- **Dependencies**: None

### Status
⏳ **PENDING** (legal review needed)

---

## GAP-012: Embedding Experiment Metadata

### Problem
No metadata for semantic similarity experiments (embeddings, link prediction).

### Impact
- **Severity**: 🔵 P3 - Future enhancement
- **Affects**: Research reproducibility, experiment tracking
- **Compliance**: AOEM Phase 3 (optional experiments)

### Evidence
- File: No `embeddings` section in concept-template
- Plan: HITO 3 includes PyKEEN/RDF2Vec experiment

### Proposed Solution
1. Add optional `embeddings` section:
   ```yaml
   embeddings:
     experiment_id: "pykeen-transe-001"
     model_type: "TransE"
     vector_dimension: 100
     training_triples_count: 1247
     evaluation_metrics:
       hits_at_10: 0.87
       mean_rank: 23
   ```
2. Generate visualizations: t-SNE plots

### Effort Estimate
- **Hours**: 12h (includes PyKEEN setup)
- **Owner**: Data Scientist + Ontology Engineer
- **Dependencies**: GAP-005 (need TTL ontology as input)

### Status
⏳ **PENDING** (HITO 3 - Experimentation phase)

---

## GAP-013: SHACL Shapes Generation

### Problem
SHACL constraints not auto-generated from OTTR templates.

### Impact
- **Severity**: 🔵 P3 - Future enhancement
- **Affects**: Instance validation automation
- **Compliance**: W3C SHACL standard

### Evidence
- File: Missing `shapes/` folder
- Current: Manual SHACL shapes creation

### Proposed Solution
1. Extend OTTR templates to emit SHACL shapes:
   ```ottr
   Template: ConceptShapeTemplate(?class_uri, ?property_uri, ?cardinality) :: {
     ottr:Triple(?shape, sh:targetClass, ?class_uri),
     ottr:Triple(?shape, sh:property, ?prop_shape),
     ottr:Triple(?prop_shape, sh:path, ?property_uri),
     ottr:Triple(?prop_shape, sh:minCount, ?cardinality)
   } .
   ```
2. Lutra generates both OWL axioms AND SHACL shapes

### Effort Estimate
- **Hours**: 15h (research + implementation)
- **Owner**: Ontology Engineer
- **Dependencies**: GAP-005 (OTTR infrastructure)

### Status
⏳ **PENDING** (Future work, post-HITO 3)

---

## GAP-014: Natural Language Generation (NLG)

### Problem
No automated generation of layperson-friendly descriptions from formal axioms.

### Impact
- **Severity**: 🔵 P3 - Future enhancement
- **Affects**: Non-technical stakeholder communication
- **Compliance**: Accessibility, ISO 704 (layperson definition)

### Evidence
- File: `concept-template-v3.yaml` has `layperson_definition` field (manual)
- Opportunity: Auto-generate from OWL axioms using NLG

### Proposed Solution
1. Create NLG pipeline:
   ```python
   # Pseudocode
   axiom = "lib:Libro rdfs:subClassOf [ owl:onProperty lib:hasAutor ; owl:minCardinality 1 ]"
   nlg_output = "Un Libro siempre tiene al menos un autor"
   ```
2. Use template-based NLG (e.g., SimpleNLG, Python `inflect`)
3. Validation: Domain expert review of generated text

### Effort Estimate
- **Hours**: 20h (NLG research + integration)
- **Owner**: NLP Specialist + Ontology Engineer
- **Dependencies**: GAP-002 (formal axioms as input)

### Status
⏳ **PENDING** (Research phase, post-POC)

---

## Summary Matrix

| Gap ID | Title | Priority | Status | Effort (h) | Owner |
|--------|-------|----------|--------|------------|-------|
| GAP-001 | Multilingual Documentation | P0 | ✅ COMPLETED | 4 | Ontology Eng |
| GAP-002 | Formal Axioms & OWL | P0 | ✅ COMPLETED | 6 | Ontology Eng |
| GAP-003 | Ontology Reuse Docs | P0 | ✅ COMPLETED | 8 | Ontology Eng |
| GAP-004 | Competency Questions | P0 | ✅ COMPLETED | 5 | Domain Expert |
| GAP-005 | OTTR Automation | P0 | ✅ COMPLETED | 8 | Ontology Eng |
| GAP-006 | Modularization (DDD) | P1 | ✅ COMPLETED | 6 | Ontology Arch |
| GAP-007 | Validation Tools | P1 | ⏳ PENDING | 10 | DevOps |
| GAP-008 | Quality Checklist | P1 | ✅ COMPLETED | 3 | Ontology Eng |
| GAP-009 | Temporal & Versioning | P2 | 🔄 IN PROGRESS | 4 | Ontology Eng |
| GAP-010 | Examples & Use Cases | P2 | ⏳ PENDING | 2 | Domain Expert |
| GAP-011 | License & Provenance | P2 | ⏳ PENDING | 1 | PM |
| GAP-012 | Embedding Metadata | P3 | ⏳ PENDING | 12 | Data Scientist |
| GAP-013 | SHACL Auto-generation | P3 | ⏳ PENDING | 15 | Ontology Eng |
| GAP-014 | NLG for Axioms | P3 | ⏳ PENDING | 20 | NLP Specialist |

**Progress**: 6/14 completed (43%), 1/14 in progress (7%), 7/14 pending (50%)

**HITO 2 Blockers**: All P0 gaps completed ✅
**Next Milestone**: Domain Expert Sign-off → HITO 3 (CI/CD + Experiments)

---

## References

1. `02-mapeo-aoem-template.md` - Source gap analysis
2. `concept-template-v3.yaml` - Enhanced template addressing gaps
3. `reuse-assessment.md` - GAP-003 solution
4. `competency-questions.md` - GAP-004 solution
5. `definition-template-v3.md` - GAP-002 methodology
