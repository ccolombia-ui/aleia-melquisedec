---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/requirements/REQ-005-lesson-template'
dc:title: 'REQ-005: Create Base Template - Lesson Learned'
dc:created: '2026-01-10'
version: '0.1.0'
status: 'draft'
result_type: 'immediate'
associated_causes:
  - 'cause-005-autopoiesis'
associated_features:
  - 'feat-lessons-system'
outputs:
  immediate: 'artifact-templates/by-type/lesson-tpl.md'
  intermediate: 'lessons extraction automation'
  final: 'centralized lessons for future specs'
generated_from: '_templates/daath-zen-patterns/daath-zen-req-template.md'
template_root: '_templates/daath-zen-patterns/template-configurable_daath-zen-root.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '420-480'
    rationale: 'Lessons learned template required for autopoiesis.'
---

# REQ-005: Crear Base Plantilla - Lesson Learned

**Priority**: Crítico
**Type**: Plantilla
**Effort**: 8 horas

## 1. Planteamiento del Problema

Lessons extraction must siguen a Plantilla so they become machine-readable artifacts for future learning.

## 2. Resumen

Define a lesson Plantilla that captures context, gap, solution, validation, and confidence evolution so lessons are immediately usable for next-spec decisions.

## 3. Next Steps

- Provide an example lesson based on lesson-001
- Define confidence scoring guidance
- Automate extraction of lessons from chatlogs

---

*Generado via daath-zen-req-Plantilla (stub).*
