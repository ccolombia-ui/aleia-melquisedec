# DAATH-ZEN Patterns Library

```yaml
---
id: "daath-zen-patterns"
version: "1.0.0"
date: "2026-01-08"
purpose: "Reusable spec patterns extracted from validated lessons"
---
```

---

## ¿Qué son los Patrones DAATH-ZEN?

Los patrones DAATH-ZEN son **plantillas reutilizables** de specs que emergen de múltiples iteraciones exitosas. Son el resultado del ciclo autopoiético:

```
Spec → Task → Rostro → Output Triple → Lesson → Pattern → Better Spec
```

### Criterios para Crear un Patrón

Un patrón DAATH-ZEN debe cumplir:

1. ✅ **Validación múltiple**: Usado exitosamente en **3+ specs diferentes**
2. ✅ **Alta confianza**: Lessons agregadas con `confidence >= 0.80`
3. ✅ **Generalizable**: Aplica a múltiples dominios, no solo uno específico
4. ✅ **Reduce tiempo**: Acelera ejecución en **30%+** vs. spec desde cero
5. ✅ **Documenta MCPs**: Lista clara de MCPs base + especializados por rostro

---

## Patrones Disponibles

### 1. daath-zen-refactoring
**Dominio**: Code refactoring, structural improvements
**Rostros clave**: MELQUISEDEC, MORPHEUS, SALOMON
**Casos de uso**:
- Reorganizar monorepo
- Fixing broken references
- Migrating package structure

**Template**: [daath-zen-refactoring.md](./daath-zen-refactoring.md)

---

### 2. daath-zen-git-workflow
**Dominio**: Git operations, CI/CD, deployment
**Rostros clave**: MORPHEUS, ALMA
**Casos de uso**:
- Push workflows
- PR creation
- Release management
- Branch strategies

**Template**: [daath-zen-git-workflow.md](./daath-zen-git-workflow.md)

---

### 3. daath-zen-research (En desarrollo)
**Dominio**: Academic research, literature review, concept extraction
**Rostros clave**: HYPATIA, SALOMON
**Casos de uso**:
- Researching new technologies
- Academic paper analysis
- Domain concept mapping

**Template**: [daath-zen-research.md](./daath-zen-research.md)

---

### 4. daath-zen-testing (En desarrollo)
**Dominio**: Test creation, validation, quality assurance
**Rostros clave**: MORPHEUS, SALOMON
**Casos de uso**:
- Unit test generation
- Integration testing
- Coverage improvement

**Template**: [daath-zen-testing.md](./daath-zen-testing.md)

---

## Cómo Usar un Patrón

### Paso 1: Seleccionar Patrón
Identifica el patrón que mejor se ajusta a tu issue:

```bash
# Buscar patrón por dominio
ls _templates/daath-zen-patterns/daath-zen-*.md
```

### Paso 2: Copiar Template
Crea un nuevo spec basado en el patrón:

```bash
# Ejemplo: Crear spec de refactoring
cp _templates/daath-zen-patterns/daath-zen-refactoring.md \
   .spec-workflow/specs/my-refactoring-v1.0.0/requirements.md
```

### Paso 3: Personalizar
Edita las secciones específicas de tu caso:
- User stories
- File paths
- Acceptance criteria
- Task descriptions

### Paso 4: Mantener Estructura
**NO CAMBIES**:
- Secciones de requirements.md
- Formato de tasks.md (rostros, MCPs)
- Estructura de lessons-learned/

---

## Evolución de Patrones

### Ciclo de Vida

```
proposed → validated → consolidated → canonical
```

**proposed** (v0.x.x):
- Primera versión del patrón
- Usado en 1-2 specs
- Confidence < 0.70
- En evaluación

**validated** (v1.x.x):
- Usado en 3+ specs exitosamente
- Confidence >= 0.80
- Documentación completa
- Recomendado para uso

**consolidated** (v2.x.x):
- Usado en 10+ specs
- Confidence >= 0.90
- Integrado en guías oficiales
- Optimizado y probado

**canonical** (v3.x.x):
- Patrón de referencia del dominio
- Usado en 50+ specs
- Confidence >= 0.95
- Base para herramientas automáticas

### Versionado Semántico

- **Major** (X.0.0): Cambios estructurales (rompen compatibilidad)
- **Minor** (x.Y.0): Nuevas tareas o secciones (compatible)
- **Patch** (x.y.Z): Mejoras de texto, fixes (compatible)

---

## Contribuir con Nuevo Patrón

### Checklist Pre-Proposal

Antes de proponer un nuevo patrón:

- [ ] He completado **3+ specs similares** exitosamente
- [ ] Las lessons agregadas tienen `confidence >= 0.80`
- [ ] El patrón es **generalizable** (no domain-specific)
- [ ] He documentado **rostros y MCPs** claramente
- [ ] He medido **mejora de tiempo** vs. spec desde cero (>30%)

### Proceso de Creación

1. **Extraer estructura común** de los 3+ specs completados
2. **Agregar lessons** en sección de best practices
3. **Documentar MCPs** por rostro
4. **Crear template** en `_templates/daath-zen-patterns/daath-zen-{name}.md`
5. **Actualizar README** con nuevo patrón
6. **Tag** como `pattern-v0.1.0` (proposed)
7. **Compartir** con equipo para validación

---

## Métricas de Éxito de Patrones

Por patrón, tracking:

| Métrica | Target | Descripción |
|---------|--------|-------------|
| **Usage** | 3+ specs | Número de specs que usan el patrón |
| **Success Rate** | >90% | % de specs completados exitosamente |
| **Time Reduction** | >30% | Reducción de tiempo vs. spec custom |
| **Lesson Confidence** | >=0.80 | Promedio de confidence de lessons |
| **Rostro Coverage** | All 5 | Diversidad de rostros involucrados |

---

## Patrones vs. Templates

| | **Template** | **Patrón DAATH-ZEN** |
|---|---|---|
| **Propósito** | Estructura inicial | Estructura probada + best practices |
| **Origen** | Diseño teórico | Experiencia práctica validada |
| **Validación** | No requerida | 3+ specs exitosos |
| **Confidence** | N/A | >= 0.80 |
| **Evolución** | Estático | Versionado semántico |
| **Documentación** | Básica | Lessons + MCPs + prompts |

---

## Próximos Pasos

1. **Completar specs actuales** (monorepo-improvements, git-push-workflow)
2. **Extraer lessons** de alta confianza
3. **Consolidar primer patrón** (daath-zen-refactoring)
4. **Iterar y validar** en nuevos specs
5. **Evolucionar a v2.x.x** con mejoras

---

## Referencias

- [Best Practices: Spec Workflow](../../.spec-workflow/_meta/best-practices.md)
- [Lesson Template](../_daath-template/lessons/lesson-template.md)
- [MCPs Recomendados](../../docs/manifiesto/03-workflow/04-mcps-recomendados.md)
