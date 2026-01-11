# Orchestrator: MELQUISEDEC
<!-- Guía de orquestación para el template app-spec -->

## Propósito

Este documento define cómo MELQUISEDEC orquesta el flujo de trabajo
entre los 5 rostros para generar una aplicación completamente especificada
y trazable.

---

## Flujo de Orquestación

```
                              MELQUISEDEC
                                   │
                     ┌─────────────┴─────────────┐
                     │                           │
                     ▼                           │
              ┌─────────────┐                    │
              │   HYPATIA   │                    │
              │ (Research)  │                    │
              └──────┬──────┘                    │
                     │ CK-01                     │
                     ▼                           │
              ┌─────────────┐                    │
              │   SALOMON   │◄── app_type        │
              │   (Specs)   │    decision        │
              └──────┬──────┘                    │
                     │ CK-02                     │
                     ▼                           │
              ┌─────────────┐                    │
              │  MORPHEUS   │                    │
              │   (Code)    │                    │
              └──────┬──────┘                    │
                     │ CK-03                     │
                     ▼                           │
              ┌─────────────┐                    │
              │    ALMA     │────────────────────┘
              │ (Instance)  │     Report
              └─────────────┘
                     │ CK-04
                     ▼
                  RELEASE
```

---

## Comandos de Orquestación

### 1. Iniciar Nueva Investigación

```
MELQUISEDEC: Iniciar research para {app_name}
  - dominio: {domain}
  - app_type: {HEX | HEX-WF | HEX-WF-MCP}
```

**Acciones automáticas:**
1. Crear estructura de carpetas (0-inbox → 05-outputs)
2. Generar `0-inbox/ISSUE.yaml` desde template
3. Delegar a HYPATIA

### 2. Delegación a HYPATIA

```
MELQUISEDEC → HYPATIA: Investigar {domain}
  - research_questions: [...]
  - min_formal_sources: {N}
  - min_atomics: {M}
```

**HYPATIA retorna:**
- `01-literature/SOURCE-*.md`
- `02-atomics/ATOMIC-*.md`
- Status: CK-01 (pass/fail)

### 3. Delegación a SALOMON

```
MELQUISEDEC → SALOMON: Especificar {app_name}
  - app_type: {HEX | HEX-WF | HEX-WF-MCP}
  - atomics_dir: 02-atomics/
  - output_dir: 03-workbook/
```

**SALOMON genera según app_type:**

| app_type | SPECs a generar |
|----------|-----------------|
| HEX | DOMAIN, PORTS, ADAPTERS |
| HEX-WF | DOMAIN, PORTS, ADAPTERS, WORKFLOWS |
| HEX-WF-MCP | DOMAIN, PORTS, ADAPTERS, WORKFLOWS, MCP |

**SALOMON retorna:**
- `03-workbook/SPEC-*.md`
- Status: CK-02 (pass/fail)

### 4. Delegación a MORPHEUS

```
MELQUISEDEC → MORPHEUS: Implementar {app_name}
  - specs_dir: 03-workbook/
  - output_dir: 04-artifacts/
  - test_coverage: {min %}
```

**MORPHEUS genera:**
- `04-artifacts/src/` (código)
- `04-artifacts/tests/` (tests)
- `04-artifacts/config/` (schemas)

**MORPHEUS retorna:**
- Status: CK-03 (pass/fail)
- Coverage: {actual %}

### 5. Delegación a ALMA

```
MELQUISEDEC → ALMA: Validar y publicar {app_name}
  - artifacts_dir: 04-artifacts/
  - output_dir: 05-outputs/
```

**ALMA ejecuta:**
1. Correr todos los tests
2. Generar matriz de trazabilidad
3. Crear package instalable
4. Generar documentación
5. Crear release

**ALMA retorna:**
- `05-outputs/dist/`
- `05-outputs/TRACEABILITY-MATRIX.md`
- Status: CK-04 (pass/fail)

---

## Decisiones de Branching

### app_type Decision Tree

```
¿La app necesita exponer tools para LLM?
├── SÍ → HEX-WF-MCP
└── NO → ¿La app tiene workflows complejos?
         ├── SÍ → HEX-WF
         └── NO → HEX
```

### Checkpoint Failures

```
CK-01 FAIL (HYPATIA)
├── Faltan fuentes formales → HYPATIA: buscar más literatura
├── Faltan atomics → HYPATIA: atomizar más conceptos
└── Atomics sin trazabilidad → HYPATIA: agregar source_ref

CK-02 FAIL (SALOMON)
├── Specs incompletas → SALOMON: completar specs faltantes
├── Conceptos inventados → Volver a HYPATIA (falta atomic)
└── Sin trazabilidad → SALOMON: agregar atomic_ref

CK-03 FAIL (MORPHEUS)
├── Código sin spec → MORPHEUS: eliminar o crear spec
├── Tests failing → MORPHEUS: fix tests
└── Coverage bajo → MORPHEUS: agregar tests

CK-04 FAIL (ALMA)
├── Trazabilidad incompleta → Auditar cadena completa
├── Package no instalable → MORPHEUS: fix dependencies
└── Docs incompletas → ALMA: generar docs faltantes
```

---

## Estado del Workflow

### Status File: `.melquisedec/workflow_status.yaml`

```yaml
workflow:
  id: "{{workflow_id}}"
  app_name: "{{app_name}}"
  app_type: "{{app_type}}"
  started: "{{start_date}}"

  current:
    rostro: "{{current_rostro}}"
    phase: "{{current_phase}}"
    task: "{{current_task}}"

  checkpoints:
    CK-01:
      status: "{{status}}"  # pending | passed | failed
      date: "{{date}}"
      validation_file: ".melquisedec/hypatia_validation.yaml"
    CK-02:
      status: "{{status}}"
      date: "{{date}}"
      validation_file: ".melquisedec/salomon_validation.yaml"
    CK-03:
      status: "{{status}}"
      date: "{{date}}"
      validation_file: ".melquisedec/morpheus_validation.yaml"
    CK-04:
      status: "{{status}}"
      date: "{{date}}"
      validation_file: ".melquisedec/alma_validation.yaml"

  history:
    - timestamp: "{{timestamp}}"
      rostro: "{{rostro}}"
      action: "{{action}}"
      result: "{{result}}"
```

---

## Validación de Trazabilidad

### Cadena de Trazabilidad Completa

```
05-outputs/código.py
    │
    └── traza a → 03-workbook/SPEC-*.md
                      │
                      └── traza a → 02-atomics/ATOMIC-*.md
                                        │
                                        └── traza a → 01-literature/SOURCE-*.md
                                                          │
                                                          └── source formal (ISO, paper, etc.)
```

### Comando de Validación

```bash
python validators/traceability_check.py {{app_name}}
```

**Output esperado:**
```
Checking traceability for: {{app_name}}

[✓] 05-outputs → 04-artifacts: 100% traced
[✓] 04-artifacts → 03-workbook: 100% traced
[✓] 03-workbook → 02-atomics: 100% traced
[✓] 02-atomics → 01-literature: 100% traced
[✓] 01-literature → formal sources: 100% traced

RESULT: FULL TRACEABILITY ACHIEVED
```

---

## Métricas de Calidad

### Dashboard de Progreso

| Métrica | Umbral | Actual |
|---------|--------|--------|
| Fuentes formales | ≥ 3 | {{actual}} |
| Atomics creados | ≥ 10 | {{actual}} |
| Specs trazadas | 100% | {{actual}} |
| Código trazado | 100% | {{actual}} |
| Test coverage | ≥ 80% | {{actual}} |
| Checkpoints passed | 4/4 | {{actual}} |

---

## Integración con MCPs

### MCPs Usados por Fase

| Fase | Rostro | MCPs |
|------|--------|------|
| Research | HYPATIA | brave-search, context7, fetch |
| Spec | SALOMON | sequential-thinking |
| Code | MORPHEUS | filesystem |
| Instance | ALMA | filesystem |

### Configuración en VS Code

```json
// .vscode/mcp.json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@anthropic/sequential-thinking"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@anthropic/brave-search"]
    }
  }
}
```

---

## Comandos Útiles

```bash
# Iniciar nuevo research
python tools/orchestrator.py init {{app_name}} --type HEX-WF-MCP

# Ver estado actual
python tools/orchestrator.py status {{app_name}}

# Validar checkpoint específico
python tools/orchestrator.py validate {{app_name}} --checkpoint CK-02

# Generar reporte de trazabilidad
python tools/orchestrator.py trace {{app_name}}

# Rollback a fase anterior
python tools/orchestrator.py rollback {{app_name}} --to SALOMON
```
