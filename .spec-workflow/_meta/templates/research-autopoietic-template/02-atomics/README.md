# 02-atomics/ - HYPATIA (Conceptos Atómicos - SECI Model)

Esta carpeta contiene notas atómicas organizadas según el SECI Model de creación de conocimiento.

## Estructura

```
02-atomics/
├── socialization/       # SECI-S: Tácito → Tácito
│   └── observation-X.md   # Observaciones, experiencias directas
├── externalization/     # SECI-E: Tácito → Explícito
│   └── concept-X.md       # Conceptos articulados desde intuición
├── combination/         # SECI-C: Explícito → Explícito
│   └── synthesis-X.md     # Síntesis de conceptos explícitos
└── internalization/     # SECI-I: Explícito → Tácito
    └── lesson-X.md        # Aprendizajes incorporados (práctica)
```

## Rostro DAATH-ZEN

**HYPATIA** (Investigación): Extrae conceptos atómicos de literatura, sintetiza conocimiento.

## Checkpoint

**CK-02**: Validar que se han creado suficientes atomics con conexiones significativas.

## HKM Type

Todos los archivos en esta carpeta deben tener `hkm_type: concept` (conocimiento sintetizado).

## SECI Model Explained

### Socialization (Tácito → Tácito)
**Observaciones directas, experiencias compartidas**
- Experimentos realizados
- Observaciones de campo
- Interacciones con sistemas

### Externalization (Tácito → Explícito)
**Conceptos articulados desde conocimiento implícito**
- Intuiciones formalizadas
- Patrones identificados
- Metáforas y analogías

### Combination (Explícito → Explícito)
**Síntesis de múltiples conceptos explícitos**
- Combinación de teorías
- Frameworks integrados
- Análisis comparativos

### Internalization (Explícito → Tácito)
**Aprendizajes incorporados a la práctica**
- Lecciones aprendidas aplicadas
- Habilidades desarrolladas
- Conocimiento embodied

## Criterios de Validación

- [ ] Mínimo [N] notas atómicas
- [ ] Cada nota representa UN concepto
- [ ] `synthesis_from` apunta a fuentes válidas
- [ ] Smart-thinking connections ≥[N]
- [ ] validate-metadata.py pasa

## Template para Atomics

```markdown
---
hkm_type: concept
epistemic_level: concept
title: "[CONCEPTO_ATÓMICO]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [atomic, concept, seci-X, hypatia]
synthesis_from:
  - ../01-literature/source1.md
  - ../01-literature/source2.md
---

## Definición

[Definición clara del concepto en 1-2 oraciones]

## Contexto

[¿De dónde viene este concepto? ¿Por qué es relevante?]

## Explicación Detallada

[Desarrollo del concepto con ejemplos]

## Relaciones con Otros Conceptos

- **Supports**: [[otro-concepto.md]] - [Por qué lo apoya]
- **Refines**: [[concepto-base.md]] - [Cómo lo refina]
- **Contradicts**: [[concepto-opuesto.md]] - [Por qué contradice]

## Aplicabilidad

[¿Cómo se puede aplicar este concepto al problema?]

## Referencias

- [Fuente 1] - Página X
- [Fuente 2] - Sección Y
```

## Principio Zettelkasten

**Atomicidad**: Cada nota = 1 concepto
**Conexiones**: Smart-thinking genera connections en graph
**Emergencia**: Synthesis emerge de conexiones (no planificación top-down)

## MCPs Recomendados

- **smart-thinking**: Crear conexiones entre conceptos, generar thought graph
- **filesystem**: Leer/escribir archivos
- **memory**: Mantener contexto de sesión

## Workflow con Smart-Thinking

1. Leer fuentes de 01-literature/
2. Extraer concepto atómico
3. Crear nota en carpeta SECI apropiada
4. Usar `smart-thinking` para conectar con otros atomics
5. Documentar connections en `.spec-workflow/context/`

```yaml
# Ejemplo de connection en smart-thinking
{
  "targetId": "otro-concepto-id",
  "type": "supports",
  "strength": 0.85,
  "description": "Este concepto apoya X porque..."
}
```

## Cuándo Usar Cada Carpeta SECI

| Carpeta | Cuándo Usar | Ejemplo |
|---------|-------------|---------|
| **socialization/** | Experiencias directas, observaciones | "Observación: Neo4j HNSW es 2x más rápido que flat index en queries top-k=10" |
| **externalization/** | Formalizar intuiciones | "Concepto: Hybrid retrieval combina similaridad vectorial con grafo semántico" |
| **combination/** | Sintetizar múltiples fuentes | "Síntesis: Comparativa LlamaIndex vs LangChain para Neo4j integration" |
| **internalization/** | Aprendizajes aplicados | "Lesson: Usar testcontainers para tests de Neo4j evita setup manual" |

---

**Ver**: [requirements.md](../requirements.md) § 3.1, [tasks.md](../tasks.md) § PHASE 2, [design.md](../design.md) § 4.2
