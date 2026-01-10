# 01-literature/ - HYPATIA (Recopilación de Literatura)

Esta carpeta contiene las fuentes primarias recopiladas durante la fase de investigación.

## Estructura

```
01-literature/
├── sources/             # Papers, artículos, documentación técnica
│   ├── paper-XYZ.md
│   ├── article-ABC.md
│   └── doc-DEF.md
└── references.bib       # BibTeX references (opcional)
```

## Rostro DAATH-ZEN

**HYPATIA** (Investigación): Busca, recopila y organiza conocimiento externo.

## Checkpoint

**CK-02**: Validar que se ha recopilado suficiente literatura de calidad.

## HKM Type

Todos los archivos en esta carpeta deben tener `hkm_type: source` (entrada original, referencia externa).

## Criterios de Validación

- [ ] Mínimo [N] fuentes primarias de alta calidad
- [ ] Cada archivo tiene HKM header válido
- [ ] Referencias bibliográficas completas
- [ ] Cobertura de objetivos ≥80%

## Template para Sources

```markdown
---
hkm_type: source
epistemic_level: source
title: "[TÍTULO_FUENTE]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [literature, source, hypatia]
source_type: paper | article | documentation | book | blog
source_url: "https://..."
authors: ["Autor 1", "Autor 2"]
year: YYYY
---

## Resumen

[Resumen ejecutivo de la fuente]

## Conceptos Clave

- **Concepto 1**: [Descripción]
- **Concepto 2**: [Descripción]
- **Concepto 3**: [Descripción]

## Relevancia para la Investigación

[Por qué es relevante esta fuente para el problema]

## Citas Importantes

> "[Cita textual importante]"
> — [Autor], p. [página]

## Referencias

[BibTeX o formato de citación]
```

## MCPs Recomendados

- **brave-search**: Buscar papers académicos y artículos técnicos
- **fetch-webpage**: Descargar contenido de artículos web
- **firecrawl**: Scraping avanzado de blogs técnicos
- **markitdown**: Convertir PDFs a Markdown
- **context7**: Buscar documentación de librerías

## Workflow

1. Usar `brave-search` para identificar fuentes relevantes
2. Descargar contenido con `fetch-webpage` o `firecrawl`
3. Convertir PDFs a MD con `markitdown`
4. Crear archivo .md con HKM header
5. Extraer conceptos clave → alimentan 02-atomics/

---

**Ver**: [requirements.md](../requirements.md) § 3.1, [tasks.md](../tasks.md) § PHASE 2
