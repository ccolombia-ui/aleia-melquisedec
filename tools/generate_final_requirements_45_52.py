#!/usr/bin/env python3
"""
Generar REQ-045 a REQ-052 (8 requerimientos finales de Phase 7)
"""

from pathlib import Path

REQUIREMENTS_45_52 = [
    {
        "id": "045",
        "title": "Crear Especificaciones Módulo 03-workflow (4 specs)",
        "priority": "Alto",
        "type": "Especificación",
        "effort": "32 horas",
        "description": "Crear especificaciones de implementación para módulo del manifiesto 03-workflow: spec-011 hasta spec-014 (Integración Kanban, Visualizador de trazabilidad, Automatización de versionamiento, Guía de integración MCPs).",
        "acceptance_criteria": [
            "Carpeta: `.spec-workflow/specs/spec-011/` hasta `spec-014/`",
            "Cada uno tiene: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md usa formato YAML-LD + KeterDoc (como spec-001)",
            "Enlaces a secciones manifesto/03-workflow/"
        ],
        "dependencies": "REQ-036",
        "validation_method": "Todos las 4 specs creadas, siguen estructura plantilla",
        "result_type": "intermedio",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-workflow-specs"
    },
    {
        "id": "046",
        "title": "Crear Especificaciones Módulo 04-implementacion (3 specs)",
        "priority": "Medio",
        "type": "Especificación",
        "effort": "24 horas",
        "description": "Crear especificaciones de implementación para módulo del manifiesto 04-implementacion: spec-015 hasta spec-017 (Wizard flujo-completo, Automatización extracción de lecciones, Validador de checklist interactivo).",
        "acceptance_criteria": [
            "Carpeta: `.spec-workflow/specs/spec-015/` hasta `spec-017/`",
            "Cada uno tiene: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md usa formato YAML-LD + KeterDoc",
            "Enlaces a secciones manifesto/04-implementacion/"
        ],
        "dependencies": "REQ-045",
        "validation_method": "Todos las 3 specs creadas",
        "result_type": "intermedio",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-implementacion-specs"
    },
    {
        "id": "047",
        "title": "Crear Especificaciones Módulo 05-casos-estudio (2 specs)",
        "priority": "Bajo",
        "type": "Documentación",
        "effort": "16 horas",
        "description": "Crear especificaciones de documentación para módulo del manifiesto 05-casos-estudio: spec-018 (CASO-01-DDD), spec-019 (CASO-02-PROMPTS-DINAMICOS).",
        "acceptance_criteria": [
            "Carpeta: `.spec-workflow/specs/spec-018/` y `spec-019/`",
            "Cada uno tiene: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md usa formato YAML-LD + KeterDoc",
            "Enlaces a secciones manifesto/05-casos-estudio/"
        ],
        "dependencies": "REQ-046",
        "validation_method": "Todos las 2 specs creadas",
        "result_type": "intermedio",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-casos-specs"
    },
    {
        "id": "048",
        "title": "Crear Especificación Módulo 06-referencias (1 spec)",
        "priority": "Bajo",
        "type": "Herramienta",
        "effort": "8 horas",
        "description": "Crear especificación de herramienta para módulo del manifiesto 06-referencias: spec-020 (Glosario kabalístico con búsqueda).",
        "acceptance_criteria": [
            "Carpeta: `.spec-workflow/specs/spec-020/`",
            "Tiene: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md usa formato YAML-LD + KeterDoc",
            "Enlaces a secciones manifesto/06-referencias/"
        ],
        "dependencies": "REQ-047",
        "validation_method": "spec-020 creada",
        "result_type": "intermedio",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-referencias-spec"
    },
    {
        "id": "049",
        "title": "Crear Índice Maestro (spec-021)",
        "priority": "Crítico",
        "type": "Documentación + Arquitectura",
        "effort": "16 horas",
        "description": "Reconstruir docs/manifiesto/00-master-index.md con cadena de resultados y mapa de conceptualización.",
        "acceptance_criteria": [
            "Carpeta: `.spec-workflow/specs/spec-021-master-index-coherence/`",
            "Archivos: ISSUE.md (YAML-LD + KeterDoc), requirements.md, design.md",
            "Entregable: `docs/manifiesto/00-master-index.md` (NUEVO)",
            "Secciones: Cadena de Resultados (Mermaid), Mapa de Conceptualización, Estado de Implementación, Visión del Producto",
            "Entregable: `docs/manifiesto/00-conceptualization-map.mermaid`",
            "Validación: Todos las 20 specs previas referenciadas, sin specs huérfanas"
        ],
        "dependencies": "REQ-035 hasta REQ-048",
        "validation_method": "Índice maestro muestra coherencia completa del sistema, mapa de conceptualización visualiza interconexiones",
        "result_type": "final",
        "associated_causes": "cause-system-coherence",
        "associated_features": "feat-master-index"
    },
    {
        "id": "050",
        "title": "Generar Rastreador de Estado de Implementación",
        "priority": "Alto",
        "type": "Documentación",
        "effort": "8 horas",
        "description": "Crear docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md para seguimiento.",
        "acceptance_criteria": [
            "Archivo: `docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md`",
            "Tabla: Módulo | Specs | Estado | % Completado | Próximas Acciones",
            "Barras de progreso (visual)",
            "Enlaces a ISSUE.md de cada spec",
            "Auto-generado desde carpetas spec (script: generate-status.py)",
            "CI/CD: actualiza automáticamente ante cambios en specs"
        ],
        "dependencies": "REQ-035 hasta REQ-049",
        "validation_method": "Documento de estado preciso, actualiza automáticamente",
        "result_type": "final",
        "associated_causes": "cause-tracking",
        "associated_features": "feat-status-tracker"
    },
    {
        "id": "051",
        "title": "Validar Coherencia Completa del Sistema",
        "priority": "Crítico",
        "type": "Pruebas",
        "effort": "8 horas",
        "description": "Ejecutar validación comprehensiva a través de las 21 specs y 6 módulos.",
        "acceptance_criteria": [
            "Todos las 21 specs creadas (spec-001 hasta spec-021)",
            "Todos las specs usan formato YAML-LD + KeterDoc",
            "Todos las specs enlazan a secciones del manifiesto (seci.source)",
            "Sin documentación huérfana (cada sección del manifiesto → spec)",
            "Índice maestro muestra cadena de resultados completa",
            "Mapa de conceptualización visualiza sistema",
            "Rastreador de estado de implementación preciso"
        ],
        "dependencies": "REQ-049, REQ-050",
        "validation_method": "Script de validación de coherencia pasa al 100%",
        "result_type": "inmediato",
        "associated_causes": "cause-quality-assurance",
        "associated_features": "feat-system-validation"
    },
    {
        "id": "052",
        "title": "Extraer lesson-003-manifesto-coherence",
        "priority": "Alto",
        "type": "Autopoiesis",
        "effort": "8 horas",
        "description": "Documentar lecciones aprendidas de la Fase 7 (implementación del manifiesto completo).",
        "acceptance_criteria": [
            "Archivo: `060-reflect/lessons/lesson-003-manifesto-coherence.md`",
            "Frontmatter YAML-LD + KeterDoc",
            "seci.derives_from: chatlog de sesiones de Fase 7",
            "Secciones: Cómo el índice maestro mejora la comprensión, Desafíos creando 21 specs, Valor del mapa de conceptualización, Recomendaciones, Evolución de score de confianza",
            "Actualiza confianza del sistema MELQUISEDEC (general 0.00 → 0.90)"
        ],
        "dependencies": "REQ-051",
        "validation_method": "Lección valida, confianza del sistema justificada",
        "result_type": "final",
        "associated_causes": "cause-autopoiesis",
        "associated_features": "feat-manifesto-lesson"
    },
]

TEMPLATE = """---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-{req_id}'
dc:title: 'REQ-{req_id}: {title}'
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

# REQ-{req_id}: {title}

**Generado Desde:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadatos**:

- **result_type**: {result_type}
- **associated_causes**: {associated_causes}
- **associated_features**: {associated_features}
- **priority**: {priority}
- **type**: {req_type}
- **effort**: {effort}

---

## Resumen

{description}

---

## 1. Planteamiento del Problema

Este requerimiento aborda la necesidad de {title} como parte de la implementación de la arquitectura KeterDoc (spec-001).

## 2. Especificación del Requerimiento

### 2.1. Descripción

{description}

### 2.2. Criterios de Aceptación

{acceptance_criteria}

## 3. Dependencias y Restricciones

**Dependencias**: {dependencies}

**Método de Validación**: {validation_method}

## 4. Guía de Implementación

Este requerimiento debe implementarse siguiendo el patrón de plantilla configurable DAATH-ZEN y validarse contra los criterios de aceptación listados arriba.

---

*Generado: 2026-01-10 | Plantilla: daath-zen-req-template.md | Estado: draft*
"""

def generate_requirement(req_data):
    """Generar un archivo de requerimiento individual."""
    req_id = req_data["id"]
    acceptance_criteria_text = "\n".join([f"- [ ] {ac}" for ac in req_data["acceptance_criteria"]])
    
    content = TEMPLATE.format(
        req_id=req_id,
        title=req_data["title"],
        result_type=req_data["result_type"],
        associated_causes=req_data["associated_causes"],
        associated_features=req_data["associated_features"],
        priority=req_data["priority"],
        req_type=req_data["type"],
        effort=req_data["effort"],
        description=req_data["description"],
        acceptance_criteria=acceptance_criteria_text,
        dependencies=req_data["dependencies"],
        validation_method=req_data["validation_method"]
    )
    
    return content

def main():
    """Generar REQ-045 a REQ-052."""
    output_dir = Path(r"c:\proyectos\aleia-melquisedec\apps\research-autopoietic-template\010-define\workbooks")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Generando {len(REQUIREMENTS_45_52)} requerimientos finales (REQ-045 a REQ-052)...")
    
    for req in REQUIREMENTS_45_52:
        req_id = req["id"]
        # Crear nombre de archivo más corto
        title_slug = req['title'].lower().replace(' ', '-').replace('(', '').replace(')', '')[:50]
        filename = f"REQ-{req_id}-{title_slug}.md"
        filepath = output_dir / filename
        
        content = generate_requirement(req)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Creado {filename}")
    
    print(f"\n✅ Generados exitosamente {len(REQUIREMENTS_45_52)} requerimientos en {output_dir}")
    print(f"   REQ-045 hasta REQ-052")
    print(f"\n📊 TOTAL ACUMULADO: 52 requerimientos (REQ-001 a REQ-052)")

if __name__ == "__main__":
    main()
