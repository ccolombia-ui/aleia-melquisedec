---
# HKM Header - Keter-Doc Protocol Metadata
# ==========================================
# This YAML frontmatter contains structured metadata for the document
# following the Keter-Doc Protocol v1.0.0 specification.
#
# Required Fields:
#   - spec_id: Specification identifier (e.g., SPEC-001)
#   - title: Document title
#   - phase: Workflow phase (requirements|design|tasks|implementation|completed|steering)
#   - version: Semantic version (MAJOR.MINOR.PATCH)
#   - created: ISO8601 creation timestamp
#   - author: Creator name or agent
#   - rostro_primary: Primary Rostro archetype
#   - status: Document status (draft|pending-approval|approved|needs-revision|implemented|deprecated)
#   - approval_required: Boolean indicating if approval is needed
#
# Optional Fields:
#   - modified: ISO8601 last modification timestamp
#   - parent_issue: URN of parent issue
#   - related_specs: Array of related spec URNs
#   - dependencies: Array of external dependencies

spec_id: "{{SPEC_ID}}"
title: "{{DOCUMENT_TITLE}}"
phase: "{{PHASE}}"
version: "{{VERSION}}"
created: "{{CREATED_TIMESTAMP}}"
modified: "{{MODIFIED_TIMESTAMP}}"
author: "{{AUTHOR}}"
rostro_primary: "{{ROSTRO_PRIMARY}}"
status: "{{STATUS}}"
approval_required: {{APPROVAL_REQUIRED}}

# Principios MELQUISEDEC Aplicados
# Array de principios que guían este documento (P1-P10)
principles:
{{PRINCIPLES_LIST}}

# Metadata Dublin Core
# Campos de Dublin Core para interoperabilidad
dc_title: "{{DC_TITLE}}"
dc_description: "{{DC_DESCRIPTION}}"
dc_subject: {{DC_SUBJECT}}
dc_language: "{{DC_LANGUAGE}}"
dc_rights: "{{DC_RIGHTS}}"

# Trazabilidad
# Enlaces a issues y specs relacionados
parent_issue: "{{PARENT_ISSUE}}"
related_specs: {{RELATED_SPECS}}
dependencies: {{DEPENDENCIES}}
---

```jsonld
{
  "@context": "urn:melquisedec:schema:keter-doc-protocol:v1.0.0",
  "@type": "{{DOCUMENT_TYPE}}",
  "@id": "{{DOCUMENT_URN}}",
  "title": "{{DOCUMENT_TITLE}}",
  "description": "{{DOCUMENT_DESCRIPTION}}",
  "creator": {
    "@type": "foaf:Agent",
    "name": "{{AUTHOR}}"
  },
  "created": "{{CREATED_TIMESTAMP}}",
  "modified": "{{MODIFIED_TIMESTAMP}}",
  "subject": {{DC_SUBJECT}},
  "language": "{{DC_LANGUAGE}}",
  "format": "text/markdown",
  "type": "Documentation",
  "rights": "{{DC_RIGHTS}}",
  "specId": "{{SPEC_ID}}",
  "phase": "{{PHASE}}",
  "version": "{{VERSION}}",
  "status": "{{STATUS}}",
  "approvalRequired": {{APPROVAL_REQUIRED}},
  "rostroPrimary": "{{ROSTRO_PRIMARY}}",
  "parentIssue": "{{PARENT_ISSUE}}",
  "relatedSpecs": {{RELATED_SPECS}},
  "dependencies": {{DEPENDENCIES}},
  "principles": {{PRINCIPLES_ARRAY}},
  "compiledFrom": "{{WORKBOOK_URN}}",
  "compilationTimestamp": "{{COMPILATION_TIMESTAMP}}",
  "compilerVersion": "{{COMPILER_VERSION}}",
  "workbookPath": "{{WORKBOOK_PATH}}"
}
```

---

# {{DOCUMENT_TITLE}}

## Metadatos

| Campo | Valor |
|-------|-------|
| **Spec ID** | {{SPEC_ID}} |
| **Nombre** | {{DOCUMENT_NAME}} |
| **Versión** | {{VERSION}} |
| **Fecha** | {{CREATED_DATE}} |
| **Estado** | {{STATUS_DISPLAY}} |
| **Autor** | {{AUTHOR}} |
| **Propósito** | {{PURPOSE}} |

---

## Overview

{{OVERVIEW_CONTENT}}

### Problema Central

{{PROBLEM_STATEMENT}}

### Insight Crítico

{{CRITICAL_INSIGHT}}

---

## Principios MELQUISEDEC Aplicados

{{PRINCIPLES_APPLIED}}

---

{{BODY_SECTIONS}}

---

## Referencias

{{REFERENCES}}

---

<!-- COMPILATION FOOTER -->
<!-- ==================== -->
<!-- ⚠️ ADVERTENCIA: Este archivo es generado automáticamente -->
<!-- No editar manualmente. Para cambios, editar workbook fuente. -->

**Compilado desde**: `{{WORKBOOK_PATH}}`
**Fecha de compilación**: `{{COMPILATION_TIMESTAMP}}`
**Versión de compilador**: `{{COMPILER_VERSION}}`
**Schema**: `keter-doc-protocol-v1.0.0`

---

<!-- PLACEHOLDER DOCUMENTATION -->
<!-- ========================= -->
<!--
Available Placeholders:

## Header Metadata
- {{SPEC_ID}}: Specification ID (e.g., SPEC-001)
- {{DOCUMENT_TITLE}}: Full document title
- {{DOCUMENT_NAME}}: Short document name
- {{DOCUMENT_TYPE}}: JSON-LD document type (ResearchSpecification, RequirementsDocument, etc.)
- {{DOCUMENT_URN}}: Unique document URN (urn:melquisedec:spec:{name})
- {{DOCUMENT_DESCRIPTION}}: Brief document description
- {{PHASE}}: Workflow phase (requirements|design|tasks|implementation|completed|steering)
- {{VERSION}}: Semantic version (1.0.0)
- {{STATUS}}: Document status (draft|pending-approval|approved|needs-revision|implemented|deprecated)
- {{STATUS_DISPLAY}}: Human-readable status display
- {{APPROVAL_REQUIRED}}: Boolean (true|false)
- {{ROSTRO_PRIMARY}}: Primary Rostro archetype (Rostro_Melquisedec, etc.)
- {{AUTHOR}}: Document author/creator
- {{PURPOSE}}: Document purpose statement

## Timestamps
- {{CREATED_TIMESTAMP}}: ISO8601 creation timestamp (2026-01-10T12:00:00Z)
- {{MODIFIED_TIMESTAMP}}: ISO8601 modification timestamp
- {{CREATED_DATE}}: Human-readable creation date (2026-01-10)
- {{COMPILATION_TIMESTAMP}}: When document was compiled
- {{COMPILER_VERSION}}: Version of compilation tool

## Dublin Core
- {{DC_TITLE}}: Dublin Core title
- {{DC_DESCRIPTION}}: Dublin Core description
- {{DC_SUBJECT}}: Array of keywords (["keyword1", "keyword2"])
- {{DC_LANGUAGE}}: Language code (es-MX, en-US)
- {{DC_RIGHTS}}: License (MIT License)

## Traceability
- {{PARENT_ISSUE}}: Parent issue URN (urn:melquisedec:issue:{name})
- {{RELATED_SPECS}}: Array of related spec URNs
- {{DEPENDENCIES}}: Array of dependencies (["package>=version"])
- {{PRINCIPLES_LIST}}: YAML list of principles applied (- P1\n  - P2)
- {{PRINCIPLES_ARRAY}}: JSON array of principles (["P1", "P2"])
- {{PRINCIPLES_APPLIED}}: Rendered list of principles with descriptions

## Content Sections
- {{OVERVIEW_CONTENT}}: Main overview text
- {{PROBLEM_STATEMENT}}: Problem description
- {{CRITICAL_INSIGHT}}: Key insight statement
- {{BODY_SECTIONS}}: Template-specific content sections (varies by variant)
- {{REFERENCES}}: References section content

## Workbook Metadata
- {{WORKBOOK_PATH}}: Filesystem path to source workbook
- {{WORKBOOK_URN}}: Workbook URN (urn:melquisedec:workbook:{name})

## Variant-Specific
These are populated by template variants (requirements, design, tasks, etc.):
- {{COHERENCE_MATRIX}}: RBM coherence matrix (Mermaid diagram + table)
- {{USER_STORIES}}: User stories from workbook
- {{FUNCTIONAL_REQUIREMENTS}}: Functional requirements
- {{NON_FUNCTIONAL_REQUIREMENTS}}: Non-functional requirements
- {{ARCHITECTURE_DIAGRAMS}}: Architecture diagrams
- {{ADR_DECISIONS}}: Architecture Decision Records
- {{COMPONENT_SPECIFICATIONS}}: Component specs
- {{TASK_LIST}}: Implementation task list
- {{GANTT_CHART}}: Gantt chart (Mermaid)
- {{VISION_STATEMENT}}: Product vision
- {{STAKEHOLDERS}}: Stakeholder list
- {{TECH_STACK}}: Technology stack
- {{FOLDER_STRUCTURE}}: Project folder structure

## Transclusion Syntax (for workbook references)
Use Obsidian-style transclusions in templates:
- ![[path/to/file]]: Include entire file
- ![[path/to/file#Section]]: Include specific section
- ![[ri-001/rinm-001/*.md]]: Include all matching files (glob pattern)

These are resolved during compilation.
-->
