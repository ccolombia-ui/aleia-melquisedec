# Definition Template v3 - ISO 704 + Gruber Axioms

**Version**: 0.1.0
**Status**: Draft
**Last Updated**: 2026-01-11
**Purpose**: Formal definition methodology combining ISO 704 intensional definitions with Gruber's formal axiomatization principles

---

## 1. Overview

This template guides the creation of rigorous concept definitions following:
- **ISO 704:2022** (Terminology work - Principles and methods)
- **Gruber (1995)** formal ontology axiomatization criteria
- **OWL 2 DL** formal semantics

### When to Use This Template
- Defining core domain concepts for ontologies
- Creating terminology with multilingual support
- Ensuring semantic precision and consistency
- Preparing concepts for automated reasoning

---

## 2. ISO 704 Intensional Definition

### 2.1 Definition Structure

```
[CONCEPT] = [GENUS] + [DIFFERENTIA_1] + [DIFFERENTIA_2] + ... + [DIFFERENTIA_N]
```

**Genus (Género próximo)**: Broader category to which the concept belongs
**Differentia (Diferencia específica)**: Characteristics that distinguish it from other concepts in the same genus

### 2.2 Step-by-Step Process

#### Step 1: Identify the Genus
- **Question**: ¿A qué categoría superior pertenece este concepto?
- **Example**: For "Libro", genus = "Recurso Bibliográfico"
- **Rule**: The genus must be a well-established concept in the domain

#### Step 2: List Essential Characteristics (Differentia)
- **Question**: ¿Qué distingue este concepto de otros en la misma categoría?
- **Format**: Create a list of 3-5 essential characteristics
- **Example for "Libro"**:
  1. Tiene autor(es)
  2. Contiene texto estructurado en capítulos
  3. Posee ISBN
  4. Puede prestarse físicamente

#### Step 3: Construct the Intensional Definition
- **Format**: `[Concept] es un/a [Genus] que [differentia_1], [differentia_2], y [differentia_3]`
- **Example**:
  ```
  Libro es un Recurso Bibliográfico que tiene uno o más autores,
  contiene texto estructurado en capítulos, posee un ISBN único,
  y puede prestarse físicamente a usuarios.
  ```

#### Step 4: Verify Completeness (ISO 704 Checklist)
- [ ] **Clarity**: Definition uses simple, unambiguous language
- [ ] **Brevity**: No unnecessary words
- [ ] **Non-circularity**: Does not define the term using itself
- [ ] **Positive statement**: States what it IS, not only what it ISN'T
- [ ] **Essential characteristics only**: No accidental properties
- [ ] **Differentia are sufficient**: Distinguishes from all siblings in genus

---

## 3. Gruber Formal Axioms

### 3.1 Five Design Criteria (Gruber 1995)

1. **Clarity**: Formal definitions with documented natural language
2. **Coherence**: Logical consistency (no contradictions)
3. **Extendibility**: Anticipates future extensions
4. **Minimal encoding bias**: Implementation-independent
5. **Minimal ontological commitment**: Minimal assumptions

### 3.2 OWL 2 DL Axiomatization

#### Axiom Type 1: Class Declaration + Label
```turtle
# Declare the concept as an OWL Class
lib:Libro rdf:type owl:Class ;
    rdfs:label "Libro"@es ;
    rdfs:label "Book"@en ;
    skos:definition "Un Recurso Bibliográfico que tiene autores..."@es .
```

#### Axiom Type 2: SubClass Hierarchy (Genus)
```turtle
# Place concept under its genus
lib:Libro rdfs:subClassOf lib:RecursoBibliografico .
```

#### Axiom Type 3: Necessary Properties (Differentia)
```turtle
# Define essential characteristics as restrictions
lib:Libro rdfs:subClassOf [
    rdf:type owl:Restriction ;
    owl:onProperty lib:hasAutor ;
    owl:minCardinality 1  # Must have at least 1 author
] .

lib:Libro rdfs:subClassOf [
    rdf:type owl:Restriction ;
    owl:onProperty lib:hasISBN ;
    owl:cardinality 1  # Exactly 1 ISBN
] .
```

#### Axiom Type 4: Disjointness (Negative Constraints)
```turtle
# Prevent logical contradictions
lib:Libro owl:disjointWith lib:Revista .
lib:Libro owl:disjointWith lib:ArticuloAcademico .
```

#### Axiom Type 5: Property Constraints
```turtle
# Domain and range restrictions
lib:hasAutor rdf:type owl:ObjectProperty ;
    rdfs:domain lib:Libro ;
    rdfs:range lib:Autor ;
    owl:inverseOf lib:authorOf .

lib:hasISBN rdf:type owl:DatatypeProperty ;
    rdfs:domain lib:Libro ;
    rdfs:range xsd:string ;
    rdf:type owl:FunctionalProperty .  # Max 1 ISBN per book
```

### 3.3 Gruber Clarity Checklist

For each axiom set, verify:
- [ ] **Natural language gloss**: Each axiom has a comment explaining intent
- [ ] **Minimal assumptions**: Only asserts what is strictly necessary
- [ ] **Documented rationale**: Why this axiom exists (e.g., business rule)
- [ ] **Testable**: Can be validated with SPARQL CQs
- [ ] **Consistent**: Does not contradict other axioms (reasoner check)

---

## 4. Examples

### Example 1: Complete Definition for "Libro"

#### ISO 704 Intensional Definition
```yaml
concept_id: libro
names:
  es: Libro
  en: Book

iso_704_definition:
  genus:
    term: RecursoBibliografico
    label_es: Recurso Bibliográfico
  differentia:
    - characteristic: "tiene uno o más autores"
      formal_property: lib:hasAutor
      cardinality: "1..*"
    - characteristic: "contiene texto estructurado en capítulos"
      formal_property: lib:hasCapitulo
      cardinality: "1..*"
    - characteristic: "posee un ISBN único"
      formal_property: lib:hasISBN
      cardinality: "1"

  intensional_definition_es: >
    Un Libro es un Recurso Bibliográfico que tiene uno o más autores,
    contiene texto estructurado en capítulos, y posee un ISBN único.
```

#### Gruber Formal Axioms (OWL 2 DL)
```turtle
# Axiom Set 1: Declaration
lib:Libro rdf:type owl:Class ;
    rdfs:label "Libro"@es, "Book"@en ;
    rdfs:comment "Recurso bibliográfico con autor, capítulos e ISBN"@es .

# Axiom Set 2: Hierarchy
lib:Libro rdfs:subClassOf lib:RecursoBibliografico .

# Axiom Set 3: Necessary conditions
lib:Libro rdfs:subClassOf [
    rdf:type owl:Restriction ;
    owl:onProperty lib:hasAutor ;
    owl:minCardinality 1
] , [
    rdf:type owl:Restriction ;
    owl:onProperty lib:hasISBN ;
    owl:cardinality 1
] , [
    rdf:type owl:Restriction ;
    owl:onProperty lib:hasCapitulo ;
    owl:minCardinality 1
] .

# Axiom Set 4: Disjointness
lib:Libro owl:disjointWith lib:Revista, lib:ArticuloAcademico .
```

### Example 2: Complete Definition for "Préstamo"

#### ISO 704 Intensional Definition
```yaml
iso_704_definition:
  genus:
    term: Transaccion
    label_es: Transacción
  differentia:
    - characteristic: "vincula un Usuario con un Libro"
      formal_property: lib:borrowedBy, lib:borrowedItem
    - characteristic: "tiene fecha de inicio y fin"
      formal_property: lib:startDate, lib:endDate
    - characteristic: "estado activo o completado"
      formal_property: lib:status

  intensional_definition_es: >
    Un Préstamo es una Transacción que vincula un Usuario con un Libro,
    tiene fecha de inicio y fecha de fin, y posee un estado (activo/completado).
```

---

## 5. Methodological Notes

### 5.1 Integration with concept-template-v3.yaml

This definition template **complements** the YAML template:
- **YAML Section 2** (Definiciones): References this methodology
- **YAML Section 5** (Formal Axioms): Populated using Gruber guidelines
- **YAML Section 15** (Quality Checklist): Includes ISO 704 compliance check

### 5.2 Workflow Position

```
[Domain Expert] → Intensional Definition (ISO 704)
       ↓
[Ontology Engineer] → Formal Axioms (Gruber/OWL)
       ↓
[OTTR Templates] → Automated Instantiation
       ↓
[Reasoner] → Consistency Check
```

### 5.3 Common Pitfalls

| Pitfall | Example (BAD) | Correction (GOOD) |
|---------|---------------|-------------------|
| **Circular definition** | "Un Libro es un libro impreso" | "Un Libro es un RecursoBibliografico con..." |
| **Too vague** | "Un Libro es un objeto con páginas" | "...con capítulos, autor e ISBN" |
| **Negative only** | "Un Libro no es una revista" | Start with positive statement, then disjointness |
| **Accidental properties** | "Un Libro siempre tiene tapa dura" | Omit (some books are paperback) |
| **Over-specification** | "Un Libro tiene exactamente 300 páginas" | Too specific, not essential |

### 5.4 Validation Process

1. **Peer review**: Domain expert validates ISO 704 definition
2. **Reasoner check**: OWL reasoner verifies axiom consistency
3. **CQ testing**: SPARQL queries confirm intended semantics
4. **SHACL validation**: Constraint validation for instances

### 5.5 Multilingual Considerations

- ISO 704 definition must exist in **both** Spanish and English
- Differentia characteristics should be culturally neutral
- OWL axioms are language-independent (formal semantics)

---

## 6. References

1. **ISO 704:2022** - Terminology work - Principles and methods
2. **Gruber, T. (1995)** - Toward Principles for the Design of Ontologies Used for Knowledge Sharing
3. **OWL 2 Web Ontology Language Primer** - W3C Recommendation
4. **Seppälä et al. (2017)** - Intensional Definitions for Ontologies

---

## 7. Template Metadata

```yaml
template_id: definition-template-v3
version: 0.1.0
authors: [HITO 2 Team]
license: CC-BY-4.0
related_templates:
  - concept-template-v3.yaml
  - relation-pattern.ottr
compliance:
  - ISO 704:2022
  - Gruber 1995 criteria
  - OWL 2 DL
```

---

**Next Steps**: Use this template when filling `concept-template-v3.yaml` Section 2 (Definiciones) and Section 5 (Formal Axioms).
