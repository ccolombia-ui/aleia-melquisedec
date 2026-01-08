# _daath Template

Esta carpeta es un **template** para la estructura `_daath/` que debe existir en cada output generado por MELQUISEDEC.

## Propósito

Cada output (carpeta en `5-outputs/`) debe contener:
- El contenido principal (MD, assets, etc.)
- `_daath/` con la memoria episódica completa:
  - **chatlog**: Conversación completa que generó el output
  - **lessons**: Conocimiento destilado del chatlog

## Estructura

```
5-outputs/
└── {OUTPUT_NAME}_v{x.y.z}/
    ├── _daath/                    # Memoria episódica
    │   ├── chatlog/
    │   │   ├── metadata.yaml       # Metadatos de la instance
    │   │   ├── full-transcript.md  # Transcript cronológico completo
    │   │   ├── by-rostro/          # Conversaciones por rostro
    │   │   │   ├── 01-melquisedec.md
    │   │   │   ├── 02-hypatia.md
    │   │   │   ├── 03-salomon.md
    │   │   │   ├── 04-morpheus.md
    │   │   │   └── 05-alma.md
    │   │   └── by-phase/           # Conversaciones por fase
    │   │       ├── 01-classification.md
    │   │       ├── 02-research.md
    │   │       ├── 03-analysis.md
    │   │       ├── 04-design.md
    │   │       └── 05-publishing.md
    │   └── lessons/
    │       ├── lesson-001-{rostro}-{topic}.md
    │       ├── lesson-002-{rostro}-{topic}.md
    │       └── summary.yaml         # Agregado de lessons
    ├── {OUTPUT_CONTENT}.md          # Contenido principal
    └── [otros archivos del output]
```

## Uso

1. **Al iniciar una research instance**: Copiar esta template a `5-outputs/{OUTPUT_NAME}_v1.0.0/_daath/`
2. **Durante ejecución**: Rostros escriben en chatlog
3. **Al completar (ALMA)**: Extraer lessons + generar summary.yaml

## Trazabilidad

Cada archivo en `_daath/` está versionado en Git junto con el output:
- Git commit del output incluye _daath/
- Tag de versión apunta a output + _daath/ juntos
- No se puede separar el conocimiento de su historia

## Referencias

- [Sistema de Autopoiesis](../../docs/manifiesto/02-arquitectura/05-autopoiesis-system.md)
- [Principio P6: Trazabilidad](../../docs/manifiesto/01-fundamentos/04-principios-fundacionales.md#p6)
- [Principio P9: Inmutabilidad](../../docs/manifiesto/01-fundamentos/04-principios-fundacionales.md#p9)
