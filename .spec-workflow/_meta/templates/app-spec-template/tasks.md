# Tasks: {{research.name}}
<!-- Template para seguimiento de tareas por rostro -->

## Estado General

| Rostro | Fase | Estado | Progreso |
|--------|------|--------|----------|
| MELQUISEDEC | 0-inbox | `{{status.melquisedec}}` | {{progress.melquisedec}}% |
| HYPATIA | 01-literature, 02-atomics | `{{status.hypatia}}` | {{progress.hypatia}}% |
| SALOMON | 03-workbook | `{{status.salomon}}` | {{progress.salomon}}% |
| MORPHEUS | 04-artifacts | `{{status.morpheus}}` | {{progress.morpheus}}% |
| ALMA | 05-outputs | `{{status.alma}}` | {{progress.alma}}% |

---

## MELQUISEDEC (Fase 0: Orquestación)

> **Pregunta clave:** ¿Qué tipo de app y qué flujo de conocimiento?

### Tareas

- [ ] **0.1** Clasificar tipo de app
  - Determinar: `{{app_type}}` (HEX | HEX-WF | HEX-WF-MCP)
  - Justificar la elección según requisitos

- [ ] **0.2** Crear estructura de carpetas
  ```
  {{app_name}}/
  ├── 0-inbox/
  │   └── ISSUE.yaml
  ├── 01-literature/
  ├── 02-atomics/
  ├── 03-workbook/
  ├── 04-artifacts/
  ├── 05-outputs/
  └── .melquisedec/
  ```

- [ ] **0.3** Crear ISSUE.yaml
  - Usar template: `_meta/templates/ISSUE.yaml.template`
  - Definir: nombre, dominio, app_type, research_questions

### Output Esperado

```
0-inbox/
└── ISSUE.yaml
```

### Checkpoint

No hay checkpoint formal. MELQUISEDEC inicia y delega a HYPATIA.

---

## HYPATIA (Fase 1: Investigación)

> **Pregunta clave:** ¿Qué dice la literatura canónica sobre `{{domain}}`?

### Tareas de Literatura (01-literature)

- [ ] **1.1** Identificar fuentes formales
  - Estándares (ISO, RFC, etc.): mínimo {{quality.min_formal_sources}}
  - Frameworks (DDD, Hexagonal, etc.)
  - Papers académicos (si aplica)

- [ ] **1.2** Documentar contenido relevante
  - Crear archivo por fuente en `01-literature/`
  - Formato: `SOURCE-{standard}-{nombre}.md`
  - Incluir: citas textuales, definiciones, diagramas

### Tareas de Atomización (02-atomics)

- [ ] **1.3** Atomizar conceptos (Zettelkasten)
  - Extraer conceptos atómicos de la literatura
  - Un concepto = Un archivo
  - Formato: `ATOMIC-{id}-{nombre}.md`
  - Mínimo: {{quality.min_atomics}} atomics

- [ ] **1.4** Mapear relaciones
  - Cada atomic debe tener `source_ref:` apuntando a 01-literature
  - Relacionar atomics entre sí (depends, relates, contradicts)

- [ ] **1.5** Checkpoint CK-01
  - Ejecutar: `validators/hypatia_checkpoint.py`
  - Verificar: min_formal_sources, min_atomics, all_traced

### Output Esperado

```
01-literature/
├── SOURCE-ISO-16175.md
├── SOURCE-DDD-evans.md
└── SOURCE-HEXAGONAL-cockburn.md

02-atomics/
├── ATOMIC-001-entity-definition.md
├── ATOMIC-002-value-object.md
├── ATOMIC-003-aggregate.md
└── ...
```

### Checkpoint CK-01

| Criterio | Requerido | Estado |
|----------|-----------|--------|
| Fuentes formales | ≥ {{quality.min_formal_sources}} | [ ] |
| Atomics creados | ≥ {{quality.min_atomics}} | [ ] |
| Atomics trazados | 100% | [ ] |

---

## SALOMON (Fase 2: Especificación)

> **Pregunta clave:** ¿Cómo se especifica `{{app_name}}` según la investigación de HYPATIA?

### Specs Requeridas según app_type

| app_type | SPEC-DOMAIN | SPEC-PORTS | SPEC-ADAPTERS | SPEC-WORKFLOWS | SPEC-MCP |
|----------|-------------|------------|---------------|----------------|----------|
| HEX | ✅ | ✅ | ✅ | ❌ | ❌ |
| HEX-WF | ✅ | ✅ | ✅ | ✅ | ❌ |
| HEX-WF-MCP | ✅ | ✅ | ✅ | ✅ | ✅ |

### Tareas

- [ ] **2.1** SPEC-DOMAIN.md
  - Especificar entidades del dominio
  - Especificar value objects
  - Especificar agregados
  - **Cada elemento debe trazar a un ATOMIC**

- [ ] **2.2** SPEC-PORTS.md
  - Especificar puertos inbound (driving)
  - Especificar puertos outbound (driven)
  - Definir contratos/interfaces
  - **Cada puerto debe trazar a un ATOMIC**

- [ ] **2.3** SPEC-ADAPTERS.md
  - Especificar adaptadores primarios (controllers, CLI)
  - Especificar adaptadores secundarios (repositorios, APIs)
  - **Cada adaptador debe trazar a un ATOMIC**

#### Solo si app_type = HEX-WF o HEX-WF-MCP

- [ ] **2.4** SPEC-WORKFLOWS.md
  - Especificar workflows/orquestaciones
  - Definir patrones de flujo
  - Especificar eventos/comandos

#### Solo si app_type = HEX-WF-MCP

- [ ] **2.5** SPEC-MCP.md
  - Especificar herramientas MCP (tools)
  - Definir inputs/outputs por tool
  - Especificar prompts para el LLM

### Validación

- [ ] **2.6** Validar trazabilidad
  - Todo concepto en SPEC debe existir en 02-atomics/
  - NO inventar conceptos nuevos
  - Si falta un ATOMIC, volver a HYPATIA

- [ ] **2.7** Checkpoint CK-02

### Output Esperado

```
03-workbook/
├── SPEC-DOMAIN.md
├── SPEC-PORTS.md
├── SPEC-ADAPTERS.md
├── SPEC-WORKFLOWS.md      # Si HEX-WF+
└── SPEC-MCP.md            # Si HEX-WF-MCP
```

### Checkpoint CK-02

| Criterio | Requerido | Estado |
|----------|-----------|--------|
| Specs completas | según app_type | [ ] |
| Specs trazadas | 100% | [ ] |
| Sin conceptos inventados | 0 | [ ] |

---

## MORPHEUS (Fase 3: Implementación)

> **Pregunta clave:** ¿Cómo se implementa cada SPEC en código?

### Tareas

- [ ] **3.1** Implementar Domain
  - Crear código según `SPEC-DOMAIN.md`
  - Ubicación: `04-artifacts/src/domain/`
  - Incluir: entities, value_objects, aggregates

- [ ] **3.2** Implementar Ports
  - Crear código según `SPEC-PORTS.md`
  - Ubicación: `04-artifacts/src/ports/`
  - Incluir: interfaces inbound, interfaces outbound

- [ ] **3.3** Implementar Adapters
  - Crear código según `SPEC-ADAPTERS.md`
  - Ubicación: `04-artifacts/src/adapters/`
  - Incluir: primary adapters, secondary adapters

#### Solo si app_type = HEX-WF o HEX-WF-MCP

- [ ] **3.4** Implementar Workflows
  - Crear código según `SPEC-WORKFLOWS.md`
  - Ubicación: `04-artifacts/src/workflows/`

#### Solo si app_type = HEX-WF-MCP

- [ ] **3.5** Implementar MCP Tools
  - Crear código según `SPEC-MCP.md`
  - Ubicación: `04-artifacts/src/mcp/`
  - Incluir: server.py, tools/, schemas/

### Testing & Config

- [ ] **3.6** Crear Tests
  - Unit tests: `04-artifacts/tests/unit/`
  - Integration tests: `04-artifacts/tests/integration/`
  - Coverage mínimo: {{quality.min_test_coverage}}%

- [ ] **3.7** Crear Configuraciones
  - Schemas: `04-artifacts/config/schemas/`
  - Environments: `04-artifacts/config/envs/`

- [ ] **3.8** Checkpoint CK-03

### Output Esperado

```
04-artifacts/
├── src/
│   ├── domain/
│   ├── ports/
│   ├── adapters/
│   ├── workflows/       # Si HEX-WF+
│   └── mcp/             # Si HEX-WF-MCP
├── tests/
│   ├── unit/
│   └── integration/
└── config/
    ├── schemas/
    └── envs/
```

### Checkpoint CK-03

| Criterio | Requerido | Estado |
|----------|-----------|--------|
| Código traza a SPEC | 100% | [ ] |
| Tests coverage | ≥ {{quality.min_test_coverage}}% | [ ] |
| Tests passing | 100% | [ ] |

---

## ALMA (Fase 4: Instanciación)

> **Pregunta clave:** ¿El código es coherente, funciona y está listo para producción?

### Tareas

- [ ] **4.1** Ejecutar Tests
  - Correr todos los tests
  - Verificar coverage ≥ {{quality.min_test_coverage}}%
  - Fix any failing tests

- [ ] **4.2** Validar Trazabilidad Completa
  - código (04) → spec (03) → atomic (02) → source (01)
  - Generar matriz de trazabilidad

- [ ] **4.3** Crear Package
  - Crear `pyproject.toml` (o equivalente)
  - Verificar que es instalable: `pip install .`

- [ ] **4.4** Generar Documentación
  - API docs (mkdocs, sphinx, etc.)
  - README actualizado
  - CHANGELOG

- [ ] **4.5** Publicar
  - Crear tag de versión
  - Crear release en GitHub
  - Publicar en PyPI (si aplica)

- [ ] **4.6** Checkpoint CK-04

### Output Esperado

```
05-outputs/
├── dist/
│   └── {{app_name}}-1.0.0.tar.gz
├── docs/
│   └── api/
├── CHANGELOG.md
└── TRACEABILITY-MATRIX.md
```

### Checkpoint CK-04

| Criterio | Requerido | Estado |
|----------|-----------|--------|
| Trazabilidad completa | 100% | [ ] |
| Package instalable | ✅ | [ ] |
| Docs generados | ✅ | [ ] |
| Release creado | ✅ | [ ] |

---

## Registro de Progreso

### Historial

| Fecha | Rostro | Tarea | Estado | Notas |
|-------|--------|-------|--------|-------|
| {{date}} | MELQUISEDEC | 0.1 | | Clasificación inicial |

### Bloqueos Actuales

_Ninguno registrado_

### Decisiones Importantes

_Ninguna registrada_

---

## Comandos Útiles

```bash
# Validar checkpoint HYPATIA
python validators/hypatia_checkpoint.py {{app_name}}

# Validar checkpoint SALOMON
python validators/salomon_checkpoint.py {{app_name}}

# Validar checkpoint MORPHEUS
python validators/morpheus_checkpoint.py {{app_name}}

# Validar checkpoint ALMA
python validators/alma_checkpoint.py {{app_name}}

# Generar matriz de trazabilidad
python tools/traceability_matrix.py {{app_name}}
```
