# Lesson {XXX}: {Título Descriptivo}

```yaml
---
id: "lesson-XXX-{rostro}-{topic}"
instance_id: "instance-XXX-{main-topic}"
domain_id: "DD-XXX"
rostro: "{ROSTRO}"                           # MELQUISEDEC | HYPATIA | SALOMON | MORPHEUS | ALMA
confidence: 0.XX                             # 0.0 - 1.0 (basado en validación)
status: "proposed"                           # proposed | validated | rejected
applies_to_prompt: "daath-zen-{domain}"      # A qué prompt TYPE aplica
version_applied: null                        # Se llena cuando se incorpora: v{x.y.z}
date_extracted: "YYYY-MM-DD"
validated_in_instances: []                   # Se llena al validar en otras instances
rejection_reason: null                       # Se llena si status=rejected
scope: "domain"                              # domain | universal
---
```

---

## Contexto

**Situación**: [Descripción del problema o situación que motivó esta lesson]

**Problema específico**: [¿Qué problema se encontró?]

**Momento en el chatlog**: Ver `_daath/chatlog/by-rostro/{XX}-{rostro}.md` línea XXX

---

## Solución Aplicada

**Descripción**: [Qué se hizo para resolver el problema]

**Pasos específicos**:
1. [Paso 1]
2. [Paso 2]
3. [...]

**Resultado**: [Qué resultado se obtuvo]

---

## Cambio en Prompt TYPE

**Prompt anterior (vX.Y.Z)**:
```markdown
[Texto relevante del prompt anterior]
```

**Prompt mejorado (vX.Y+1.Z)** (propuesto):
```markdown
[Texto mejorado propuesto para el prompt]

> **Lesson {XXX}** (confidence: 0.XX): [Referencia a esta lesson]
> Ver: _daath/lessons/instance-XXX/lesson-XXX.md
```

---

## Validación

| Instance | Aplicado | Resultado | Notas |
|----------|----------|-----------|-------|
| instance-XXX-{original} | ✅ | ⭐⭐⭐⭐⭐ | Instance original |
| instance-XXX-{validacion-1} | ⏳ | Pendiente | Por validar |
| instance-XXX-{validacion-2} | ⏳ | Pendiente | Por validar |

**Confidence calculation**:
- Initial: 0.XX (basado en contexto y evidencia)
- After 1 validation: Recalcular basado en éxito
- After 2+ validations: Ajustar hasta estabilizar

**Threshold para incorporar a prompt**: confidence >= 0.80

---

## Metadata para Neo4j

```cypher
CREATE (l:Lesson {
  id: "lesson-XXX-{rostro}-{topic}",
  instance_id: "instance-XXX-{main-topic}",
  domain_id: "DD-XXX",
  rostro: "{ROSTRO}",
  confidence: 0.XX,
  text: "[Texto breve de la lesson]",
  status: "proposed",
  scope: "domain"
})

// Relación: Lesson fue extraída de Instance
MATCH (i:ResearchInstance {id: "instance-XXX-{main-topic}"})
MATCH (l:Lesson {id: "lesson-XXX-{rostro}-{topic}"})
CREATE (i)-[:LEARNED]->(l)

// Relación: Lesson mejora PromptType (cuando se incorpore)
MATCH (l:Lesson {id: "lesson-XXX-{rostro}-{topic}"})
MATCH (p:PromptType {id: "daath-zen-{domain}-vX.Y.Z"})
CREATE (l)-[:IMPROVES {
  from_version: "X.Y.Z",
  to_version: "X.Y+1.Z",
  incorporated_at: "YYYY-MM-DD"
}]->(p)

// Relación: Lesson validada en otra instance (después de validar)
MATCH (l:Lesson {id: "lesson-XXX-{rostro}-{topic}"})
MATCH (i2:ResearchInstance {id: "instance-YYY-{otro-topic}"})
CREATE (l)-[:VALIDATED_IN {
  validated_at: "YYYY-MM-DD",
  result: "success"  // success | failed | partial
}]->(i2)
```

---

## Notas

**Aplicabilidad**:
- ✅ Aplicable a: [Dominios/contexts donde aplica]
- ❌ NO aplicable a: [Dominios/contexts donde NO aplica]

**Advertencias**:
- [Advertencia 1 sobre uso de esta lesson]
- [...]

**Referencias**:
- Chatlog completo: `_daath/chatlog/full-transcript.md`
- Conversación por rostro: `_daath/chatlog/by-rostro/{XX}-{rostro}.md`
- Instance metadata: `_daath/chatlog/metadata.yaml`

---

**Creado**: YYYY-MM-DD | **Última actualización**: YYYY-MM-DD
**Autor**: ALMA (extractora) + Usuario (validador)
