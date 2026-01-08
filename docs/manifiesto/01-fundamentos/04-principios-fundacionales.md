# 4. Principios Fundacionales (P1-P10)

```yaml
---
id: "fundamentos-04-principios"
is_a: "doctrine/principles"
version: "4.0.0"
dc:
  title: "Los 10 Principios Fundacionales de MELQUISEDEC"
  date: "2026-01-08"
  subject: ["Principios", "Doctrina", "Reglas Operacionales"]
seci:
  derives_from: ["01-que-es-melquisedec.md", "02-fundamento-kabalistico.md"]
  informs: ["../02-arquitectura/", "../03-workflow/", "../04-implementacion/"]
---
```

---

## Los 10 Principios

| # | Principio | Esencia |
|---|-----------|---------|
| **P1** | Síntesis Metodológica | MELQUISEDEC SINTETIZA y ORQUESTA metodologías existentes |
| **P2** | Autopoiesis por Diseño | La metodología se auto-mejora mediante lessons learned |
| **P3** | Issue-Driven Everything | Todo trabajo parte de un ISSUE explícito con metadata HKM |
| **P4** | Arquitectura de Prompts por Capas | Prompts jerarquizados: root → type → instance |
| **P5** | Validación Continua | Cada rostro valida su salida (checkpoints) |
| **P6** | Trazabilidad Explícita | Toda decisión/concepto/output es trazable hasta su fuente |
| **P7** | Recursión Fractal | La estructura se repite a diferentes escalas |
| **P8** | Tzimtzum (Dependency Blocking) | Cada etapa espera dependencias antes de ejecutar |
| **P9** | Outputs como Snapshots Inmutables | Los outputs publicados son inmutables, cambios = nueva versión |
| **P10** | Feedback Loops via Inbox Multinivel | Los outputs generan nuevos issues (retroalimentación) |

---

## P1: Síntesis Metodológica

**Enunciado**: MELQUISEDEC NO inventa metodologías. SINTETIZA y ORQUESTA metodologías existentes.

### Ejemplos

- Usa **CRISP-DM** para proyectos de datos
- Usa **Scrum** para desarrollo ágil
- Usa **DDD** para diseño de software
- Usa **IMRAD** para papers académicos

### ❌ Anti-patrón

Crear "metodología MELQUISEDEC propia" ignorando estándares.

### ✅ Validación

Toda metodología aplicada debe tener fuente canónica citada.

---

## P2: Autopoiesis por Diseño

**Enunciado**: La metodología se auto-mejora mediante lessons learned y versionamiento de prompts.

### Mecanismos

1. `_daath/chatlog/` registra ejecuciones
2. `_daath/lessons/` extrae aprendizajes
3. `MORPHEUS` mejora prompts con lecciones
4. Prompts versionados (v1.0.0 → v1.1.0)

### Ciclo

```mermaid
graph LR
    E["Ejecutar<br/>Research Instance"]
    L["Extraer<br/>Lessons"]
    M["Mejorar<br/>Prompts"]
    V["Validar<br/>Mejoras"]

    E --> L
    L --> M
    M --> V
    V --> E
```

### ❌ Anti-patrón

Prompts estáticos que nunca evolucionan.

### ✅ Validación

Cada research instance debe generar al menos 1 lesson learned.

---

## P3: Issue-Driven Everything

**Enunciado**: Todo trabajo parte de un **ISSUE** explícito con metadata HKM.

### Issue Mínimo

```yaml
---
# HKM HEADER
id: "issue-001-{tipo}-{nombre}"
is_a: "{tipo}"  # literature, research, feature, bug
permalink: "{path}"

# DUBLIN CORE
title: "{título}"
creator: ["{autor}"]
date: "{YYYY-MM-DD}"
subject: ["{keywords}"]

# MELQUISEDEC WORKFLOW
estado: "{inbox|literature|atomic|workbook|dataset|outputs}"
cascada_siguiente: "{siguiente paso}"
---
```

### ❌ Anti-patrón

Trabajo ad-hoc sin issue rastreable.

### ✅ Validación

Cada carpeta de investigación debe tener `ISSUE.yaml`.

---

## P4: Arquitectura de Prompts por Capas

**Enunciado**: Los prompts se organizan jerárquicamente:

```
daath-zen-root (universal)
  ↓
daath-zen-type (dominio: research, software, bim)
  ↓
daath-zen-instance (proyecto concreto)
```

### Ejemplo

- **Root**: `daath-zen-root.yaml` (orquestación universal)
- **Type**: `daath-zen-research.yaml` (investigación académica)
- **Instance**: `daath-zen-crisp-dm.yaml` (CRISP-DM específico)

### ❌ Anti-patrón

Un solo prompt monolítico para todo.

### ✅ Validación

Prompts deben heredar y extender, no duplicar.

---

## P5: Validación Continua (Checkpoints)

**Enunciado**: Cada rostro valida su salida antes de pasar a la siguiente cascada.

### Checkpoints por Rostro

| Rostro | Checkpoint | Archivo |
|--------|-----------|---------|
| MELQUISEDEC | Clasificación correcta | `0-inbox/ISSUE.yaml` |
| HYPATIA | Fuentes canónicas verificadas | `_melquisedec/hypatia_ok.yaml` |
| SALOMON | Análisis equilibrado | `_melquisedec/salomon_ok.yaml` |
| MORPHEUS | Arquitectura viable | `_melquisedec/morpheus_ok.yaml` |
| ALMA | Outputs coherentes | `_melquisedec/alma_ok.yaml` |

### ❌ Anti-patrón

Pasar a la siguiente etapa sin validar la actual.

### ✅ Validación

Cada checkpoint debe tener `status: pass` antes de continuar.

---

## P6: Trazabilidad Explícita

**Enunciado**: Toda decisión, concepto o output debe ser trazable hasta su fuente.

### Mecanismos

- **HKM Header**: `id`, `is_a`, `permalink`
- **Dublin Core**: `creator`, `source`, `date`
- **SECI Model**: `derives_from`, `informs`

### Ejemplo de Trazabilidad

```
ISSUE → Literatura → Concepto Atómico → Workbook → Output

issue-003-book-ddd
  ↓ derives_from
1-literature/book/domain-driven-design/
  ↓ informs
2-atomic/concepts/bounded-context.md
  ↓ informs
3-workbook/WB-ASC-001/02-methods.md
  ↓ informs
5-outputs/CALE_ARCHITECTURE.md
```

### ❌ Anti-patrón

Outputs sin referencias a fuentes primarias.

### ✅ Validación

Grafo de trazabilidad debe ser acíclico dirigido (DAG).

---

## P7: Recursión Fractal

**Enunciado**: La estructura de research instance se repite a diferentes escalas.

### Niveles Fractales

```
Organización/
├── Proyecto A/  # Research instance nivel 1
│   ├── 0-inbox/
│   ├── 1-literature/
│   │   └── book/ddd/  # Research instance nivel 2
│   │       ├── 0-inbox/
│   │       ├── 2-atomic/
│   │       └── 5-outputs/
│   └── 5-outputs/
```

### Regla

Cualquier artefacto en `1-literature/` puede convertirse en research instance independiente si requiere profundidad.

### ❌ Anti-patrón

Forzar todo a un solo nivel.

### ✅ Validación

Estructura `0-inbox/` → `5-outputs/` debe repetirse en cada nivel.

---

## P8: Tzimtzum (Dependency Blocking)

**Enunciado**: Cada etapa espera dependencias antes de ejecutar (contracción antes de expansión).

### Inspiración Kabalística

**Tzimtzum** = Contracción de Dios para crear espacio al universo.

### Aplicación MELQUISEDEC

- HYPATIA NO ejecuta hasta que MELQUISEDEC termine clasificación
- SALOMON NO ejecuta hasta que HYPATIA termine búsqueda
- MORPHEUS NO ejecuta hasta que SALOMON termine análisis
- ALMA NO ejecuta hasta que MORPHEUS termine diseño

### ❌ Anti-patrón

Ejecutar etapas en paralelo sin validar dependencias.

### ✅ Validación

Cascade waterfall explícito en `ISSUE.yaml`:

```yaml
cascada_siguiente: "HYPATIA → SALOMON → MORPHEUS → ALMA"
```

---

## P9: Outputs como Snapshots Inmutables

**Enunciado**: Los outputs publicados son **inmutables**. Cambios requieren nueva versión.

### Versionamiento Semántico

```
MAJOR.MINOR.PATCH

MAJOR: Breaking changes (incompatibilidad)
MINOR: Nuevas features (compatible)
PATCH: Bug fixes
```

### Ejemplo

```
5-outputs/CALE_ARCHITECTURE_v1.0.0.md  ← Inmutable
5-outputs/CALE_ARCHITECTURE_v1.1.0.md  ← Nueva versión
```

### ❌ Anti-patrón

Editar outputs publicados sin cambiar versión.

### ✅ Validación

Git tags en outputs: `git tag output-v1.0.0`.

---

## P10: Feedback Loops via Inbox Multinivel

**Enunciado**: Los outputs pueden generar nuevos issues que retroalimentan el sistema.

### Flujo de Feedback

```mermaid
graph LR
    Output["5-outputs/GUIA_v1.0.0.md"]
    Inbox["0-inbox/ISSUE-nuevo"]
    Literature["1-literature/feedback/"]

    Output -->|"Usuario detecta gap"| Inbox
    Inbox -->|"Nueva investigación"| Literature
    Literature -->|"Mejora GUIA_v2.0.0"| Output

    style Output fill:#90EE90
    style Inbox fill:#FFD700
```

### Mecanismos

- `0-inbox/` acepta issues desde outputs
- `_daath/lessons/` retroalimenta prompts
- Versionamiento de prompts (`v1.0.0` → `v2.0.0`)

### ❌ Anti-patrón

Sistema cerrado sin feedback.

### ✅ Validación

Cada output debe tener link a "Reportar issue" → `0-inbox/`.

---

## Matriz de Aplicación de Principios

| Principio | Caso 1A (Literatura) | Caso 1B (Investigación) | Caso 2 (Prompts) |
|-----------|---------------------|------------------------|------------------|
| **P1** | Cita DDD como metodología externa | Estudia DDD en profundidad | Sintetiza best practices |
| **P2** | Lessons de extracción → mejores prompts | Lessons → DUAL_GUIDE | Investiga la propia metodología |
| **P3** | `issue-003-book-ddd` | `RES_C.2.2_SPECIFICATION.yaml` | `Q001-Q004` como issues formales |
| **P4** | Usa `daath-zen-root-research` | Usa `daath-zen-root-methodology` | Define arquitectura hybrid |
| **P5** | Checkpoint HYPATIA | 5 checkpoints (M, H, S, Mo, A) | Experimentos validan |
| **P6** | `derives_from: issue-003` | Grafo Neo4j con 70+ nodos | SECI mode en cada question |
| **P7** | DDD puede ser instance independiente | C.2.2_DDD ES research instance | Q001-Q004 pueden ser sub-investigaciones |
| **P8** | SALOMON espera extractos | Cascada estricta H→S→Mo→A | Experimentos secuenciales |
| **P9** | `bounded-context-v1.0.md` inmutable | `DUAL_GUIDE-v1.0.md` versionado | `GUIA_v2.0.0.md` (nueva versión) |
| **P10** | Gap en WB → nuevo issue | DUAL_GUIDE genera issues | Q004 retroalimenta pattern registry |

---

## Resumen Ejecutivo

**Los 10 Principios garantizan que MELQUISEDEC sea**:

- ✅ **Sintético** (P1): Orquesta, no inventa
- ✅ **Autopoiético** (P2): Se auto-mejora
- ✅ **Trazable** (P3, P6): Todo issue tiene origen y destino
- ✅ **Modular** (P4, P7): Componible a diferentes escalas
- ✅ **Validado** (P5): Checkpoints garantizan calidad
- ✅ **Ordenado** (P8): Dependencias explícitas
- ✅ **Inmutable** (P9): Outputs versionados
- ✅ **Adaptativo** (P10): Feedback continuo

---

## 🧭 Navegación

- **← Anterior**: [03. Los 5 Rostros de DAATH](03-cinco-rostros.md)
- **→ Siguiente**: [02. Arquitectura Operativa](../02-arquitectura/README.md)
- **↑ Fundamentos**: [README](README.md)

---

**Última actualización**: 2026-01-08 | **Versión**: 4.0.0
