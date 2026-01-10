---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'TemplateRoot'
'@id': 'https://melquisedec.org/templates/daath-zen-root'
dc:title: 'template-configurable_daath-zen-root'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot'
version: '1.0.0'
status: 'draft'
---

# DAATH-ZEN Root Template (Configurable)

**Purpose:** Define the root-level configuration and governance for DAATH-ZEN configurable templates (versioning, applies_to patterns, validation rules, manifesto coherence checks).

**Usage:** Every `daath-zen-*` template must reference this root via `template_root: template-configurable_daath-zen-root.md` in its metadata.

## Fields & Policy

- `applies_to`: pattern like `daath-zen-{domain}-v{x.y.z}`. Use semver for versions.
- `recommended_versions`: list of template variants (stable, experimental, legacy).
- `manifesto_reference`: pointer to relevant Manifesto sections (e.g., `docs/manifiesto/02-arquitectura/03-templates-hkm.md`).
- `validation_scripts`: list of scripts to validate frontmatter, JSON-LD, and required result mappings.
- `purpose`: concise statement of the template's intended artifact and lifecycle stage (e.g., requirement artifact, analysis, lesson).

## Versioning Guidance

- Use semver (MAJOR.MINOR.PATCH) for templates.
- `stable` is recommended for production artifacts; `experimental` for prototypes.
- Include migration notes when bumping MAJOR.

## Coherence with Manifesto

Templates must include a `manifesto_coherence` section that references the manifesto paragraphs (file and line range) that justify structure and fields. Example:

```yaml
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'YAML-LD frontmatter required for KeterDoc metadata.'
```

## Root Validation

Recommended checks:
- JSON-LD validation of frontmatter
- Required fields present: `@context`, `@type`, `@id`, `dc:title`, `dc:created`
- `applies_to` pattern validity
- `result_type` ontology compliance (`immediate`, `intermediate`, `final`)

---

*Created as part of spec-001 template work (2026-01-10).*
