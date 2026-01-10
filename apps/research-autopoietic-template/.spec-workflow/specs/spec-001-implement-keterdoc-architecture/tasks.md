# Tareas: spec-001-implement-keterdoc-architecture

## Fase 1: Fundamentos (REQ-001..REQ-010)

### REQ-001: Definir Vocabulario YAML-LD @context
- [x] **Tarea 1.1**: Crear `apps/research-autopoietic-template/.spec-workflow/context.jsonld`
    - [x] Definir espacios de nombres: `mel`, `dc`, `rdf`, `rdfs`, `xsd`
    - [x] Definir mapeos de términos: `seci`, `derives_from`, `informs`, etc.
    - [x] Definir propiedades `artifact_template` y `lens`
    - [x] **Verificación**: Validar sintaxis JSON
- [x] **Tarea 1.2**: Crear ejemplo de validación en línea (JSON-LD Playground)
    - [x] Crear snippet `examples/req-001-example.jsonld` (Se crearon 3 artefactos en su lugar)
    - [ ] Documentar pasos de validación en `Implementation Logs`
- [x] **Tarea 1.3**: Actualizar Plantilla Raíz con referencia local @context
    - [x] Modificar `_templates/daath-zen-patterns/template-configurable_daath-zen-root.md`
    - [x] Asegurar que `@context` apunte al archivo local (por ahora) o URL

### REQ-002: Plantilla Base y Generador
- [ ] **Tarea 2.1**: Refinar `tools/generate_from_daath_template.py`
    - [ ] Implementar análisis de argumentos (FILE, ID, TITLE)
    - [ ] Implementar reemplazo de variables tipo Jinja2 o Regex
    - [ ] Manejar mapeo de `result_type`
- [ ] **Tarea 2.2**: Crear `daath-zen-req-template.md` (¿Ya hecho? Verificar)
    - [ ] Asegurar que use el nuevo `@context`
    - [ ] Validar herencia de `template-configurable_daath-zen-root.md`

### REQ-003: Enriquecimiento de Metadatos
- [ ] **Tarea 3.1**: Definir métricas de "Calidad de Metadatos"
    - [ ] ¿Agregar `quality_score` al frontmatter?
    - [ ] Verificar mapeo a `associated_causes`

---

## Fase 2: Patrones y Herramientas (REQ-011..)
*Por expandir después de la Fase 1*
