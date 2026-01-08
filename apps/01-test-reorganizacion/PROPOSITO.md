# Propósito de Test Reorganizacion

```yaml
---
id: "app-test-reorganizacion"
version: "0.1.0"
created: "2026-01-07"
status: "inception"  # inception | active | synthesis | completed | archived

# Propósito inicial
purpose: |
  Validar la nueva estructura del monorepo DAATH-ZEN

# Rostro iniciador (según manifiesto MELQUISEDEC)
initiated_by: "MELQUISEDEC"  # MELQUISEDEC | HYPATIA | SALOMON | MORPHEUS | ALMA

# Metodologías orquestadas
methodologies:
  - "Zettelkasten"  # Para gestión de conocimiento atómico
  # Ejemplo adicional:
  # - "CRISP-DM"      # Para proyectos de data science
  # - "DDD"           # Para modelado de dominios complejos

# Tipo de aprendizaje
learning_mode: "active"  # active | passive | experimental

# Tags para búsqueda
tags:
  - "investigacion"
  - "conocimiento"
  # Agregar tags específicos del dominio
---
```

## 🎯 Objetivo

[Explicar detalladamente qué problema resuelve esta investigación y por qué es importante]

### Preguntas de Investigación

1. ¿[Pregunta principal]?
2. ¿[Pregunta secundaria]?
3. ¿[Pregunta adicional]?

### Hipótesis Inicial

[Si aplica, describir la hipótesis que se busca validar]

---

## 🌱 Evolución Esperada

Esta investigación crecerá orgánicamente según el [Principio DAATH-ZEN](../../ARQUITECTURA_MONOREPO.md):

### Fases y Carpetas

| Fase | Carpeta | ¿Cuándo se crea? | Propósito |
|------|---------|------------------|-----------|
| **Inception** | `0-inbox/` | Desde el inicio | Issues, ideas, requests iniciales |
| **Research** | `1-literature/` | Cuando hay fuentes | Papers, artículos, referencias |
| **Distillation** | `2-atomic/` | Al destilar conceptos | Notas atómicas (Zettelkasten) |
| **Synthesis** | `3-workbook/` | Durante análisis | Notebooks, experimentos, análisis |
| **Structuring** | `4-dataset/` | Al generar datos | Datasets, grafos, estructuras |
| **Output** | `5-outputs/` | Al crear entregables | Reportes, visualizaciones, APIs |
| **Meta** | `_daath/` | Continuamente | Metadata, aprendizajes, métricas |

**Regla de Oro**: ✨ **Solo crear carpetas cuando el contenido exista**

---

## 🎭 Rostros Activos

Según el [Manifiesto MELQUISEDEC](../../docs/manifiesto/bereshit-v3.0.0.md):

- [ ] **MELQUISEDEC**: Define arquitectura y flujos
- [ ] **HYPATIA**: Investiga fuentes y literatura
- [ ] **SALOMON**: Sintetiza conocimiento atómico
- [ ] **MORPHEUS**: Transforma en datasets
- [ ] **ALMA**: Narra y genera outputs

---

## 🔧 Herramientas y Tecnologías

### MCP Servers Utilizados
- [ ] `neo4j-cypher` - Grafos de conocimiento
- [ ] `neo4j-memory` - Sistema de memoria
- [ ] `arxiv` - Papers académicos
- [ ] `brave` - Búsqueda web
- [ ] `perplexity-ask` - Investigación profunda
- [ ] `filesystem` - Gestión de archivos
- [ ] `sequential-thinking` - Razonamiento complejo

### Stack Técnico
- Python 3.10+
- Neo4j 5.15
- Ollama (embeddings)
- [Agregar tecnologías específicas]

---

## 📊 Métricas de Éxito

- [ ] [Métrica 1: ej. "10 conceptos atómicos destilados"]
- [ ] [Métrica 2: ej. "Grafo con 50+ nodos relacionados"]
- [ ] [Métrica 3: ej. "Informe final de 10+ páginas"]

---

## 🗺️ Roadmap

### Fase 1: Inception (actual)
- [ ] Definir preguntas de investigación
- [ ] Crear estructura base
- [ ] Recopilar fuentes iniciales

### Fase 2: Research
- [ ] Buscar literatura relevante
- [ ] Extraer conceptos clave
- [ ] Documentar en `1-literature/`

### Fase 3: Synthesis
- [ ] Destilar notas atómicas
- [ ] Crear conexiones en grafo
- [ ] Analizar en `3-workbook/`

### Fase 4: Output
- [ ] Generar datasets finales
- [ ] Crear visualizaciones
- [ ] Publicar entregables

---

## 🔗 Enlaces Relacionados

- [Arquitectura del Monorepo](../../ARQUITECTURA_MONOREPO.md)
- [Manifiesto MELQUISEDEC](../../docs/manifiesto/bereshit-v3.0.0.md)
- [Guía MCP Toolkit](../../docs/guides/docker-mcp-toolkit.md)

---

## 📝 Log de Cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-01-07 | 0.1.0 | Creación inicial |

---

**"El conocimiento emerge del caos cuando se le da estructura"** - Principio DAATH-ZEN
