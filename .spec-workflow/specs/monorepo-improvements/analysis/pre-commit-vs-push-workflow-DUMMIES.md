# 🎯 PRE-COMMIT vs PUSH WORKFLOW - Explicación Visual Para Dummies

## 📖 ANALOGÍA: Control de Calidad en una Fábrica

```
PRE-COMMIT = Inspector en la línea de producción
           Revisa CADA pieza antes de empaquetarla

PUSH WORKFLOW = Auditor final del lote
              Revisa TODO el lote antes de enviar al cliente
```

---

## 🔄 FLUJO COMPLETO (Diagrama)

```
┌─────────────────────────────────────────────────────────────────┐
│                    TU TRABAJO DIARIO                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ↓
         ┌─────────────────────────────────────┐
         │  1. Escribes código                │
         │     - archivo1.py                   │
         │     - archivo2.md                   │
         │  2. git add archivo1.py archivo2.md │
         │  3. git commit -m "mensaje"         │
         └─────────────────────────────────────┘
                              │
                              ↓
    ╔═════════════════════════════════════════════╗
    ║  🚨 PRE-COMMIT HOOKS (AUTOMÁTICO)          ║
    ║                                             ║
    ║  ✓ black: Formatea archivo1.py             ║
    ║  ✓ isort: Ordena imports                   ║
    ║  ✓ flake8: Valida estilo Python            ║
    ║  ✓ validate_doc_links: Chequea archivo2.md ║
    ║                                             ║
    ║  Tiempo: ~5-10 segundos                    ║
    ╚═════════════════════════════════════════════╝
                              │
                ┌─────────────┴─────────────┐
                │                           │
             ✅ PASA                      ❌ FALLA
                │                           │
         COMMIT EXITOSO              COMMIT BLOQUEADO
                │                           │
                │                    Debes arreglar errores
                │                           │
                │                    Vuelves a: git commit
                │                           │
                ↓                           ↓
      ┌─────────────────┐            [Volver arriba]
      │  Commit en Git  │
      │  (local)        │
      └─────────────────┘
                │
         (Puedes hacer más commits)
                │
                ↓
         ┌─────────────────┐
         │  Decides hacer  │
         │  git push       │
         └─────────────────┘
                │
                ↓
    ╔═════════════════════════════════════════════╗
    ║  🔧 PUSH WORKFLOW (MANUAL, OPCIONAL)       ║
    ║                                             ║
    ║  python tools/git/push_workflow.py         ║
    ║                                             ║
    ║  Stage 1: pre_commit                       ║
    ║    └─ Vuelve a ejecutar pre-commit hooks   ║
    ║       (por si hiciste commit --no-verify)  ║
    ║                                             ║
    ║  Stage 2: tests (❌ NO EXISTE)             ║
    ║    └─ run_affected_tests.py FALTANTE       ║
    ║                                             ║
    ║  Stage 3: branch_validate (❌ NO EXISTE)   ║
    ║    └─ validate_branch.py FALTANTE          ║
    ║                                             ║
    ║  Stage 4: commit (❌ NO EXISTE)            ║
    ║    └─ generate_commit_msg.py FALTANTE      ║
    ║                                             ║
    ║  Stage 5: push ✅                          ║
    ║    └─ git push origin main                 ║
    ║                                             ║
    ║  Stage 6: post_push (❌ NO EXISTE)         ║
    ║    └─ log_to_neo4j.py FALTANTE             ║
    ║                                             ║
    ║  Tiempo: ~30-60 segundos (minimal)         ║
    ╚═════════════════════════════════════════════╝
                              │
                              ↓
                   ┌────────────────────┐
                   │  Push a GitHub     │
                   │  (remoto)          │
                   └────────────────────┘
```

---

## 🤔 ¿POR QUÉ USAR AMBOS?

### Escenario 1: Todo funciona normal
```
git commit
  → Pre-commit ejecuta ✅
  → Commit exitoso

git push
  → Push directo, sin push_workflow
  → Listo ✅

RESULTADO: Pre-commit fue suficiente
```

### Escenario 2: Pre-commit falla por error de configuración
```
git commit
  → Pre-commit falla: "python3.10 not found" ❌
  → Usas: git commit --no-verify
  → Commit exitoso (sin validación)

python push_workflow.py
  → pre_commit stage ejecuta ✅
  → Valida código antes de push
  → push stage ejecuta
  → Listo ✅

RESULTADO: Push workflow actúa como safety net
```

### Escenario 3: Workflow completo en CI
```
GitHub Actions ejecuta:
  python push_workflow.py --non-interactive
  → pre_commit stage ✅
  → tests stage (si existiera) ✅
  → push stage ✅
  → post_push stage (log a Neo4j) ✅

RESULTADO: Validación completa automatizada
```

---

## 🎯 DIFERENCIAS CLAVE

| Aspecto | Pre-commit | Push Workflow |
|---------|------------|---------------|
| **Cuándo** | CADA commit | ANTES de push |
| **Trigger** | Automático (git hook) | Manual o CI |
| **Alcance** | Archivos en staging | Todo el repo |
| **Velocidad** | Rápido (5-10s) | Moderado (30-60s) |
| **Propósito** | Prevención básica | Validación completa |
| **Bypass** | --no-verify | (no aplicable) |
| **Estado** | ✅ Funciona (con bug) | ⚠️ Parcial (minimal) |

---

## 🐛 PROBLEMAS ACTUALES

### Problema 1: Pre-commit Python Version
```yaml
# .pre-commit-config.yaml
default_language_version:
  python: python3.10  # ❌ No existe en tu sistema

# Tu sistema:
Python 3.13.3  # ✅ Esto es lo que tienes

# Resultado:
RuntimeError: failed to find interpreter for python_spec='python3.10'

# Solución:
default_language_version:
  python: python3  # ✅ Usa la version del sistema
```

### Problema 2: Scripts Faltantes
```python
# push_workflow.py (línea 48-52)
"runners": {
    "tests": "tools/testing/run_affected_tests.py",      # ❌ NO EXISTE
    "branch_validate": "tools/git/validate_branch.py",   # ❌ NO EXISTE
    "commit_msg_generator": "tools/git/generate_commit_msg.py",  # ❌ NO EXISTE
}

# Resultado cuando ejecutas en modo full:
[tests] FAIL (code=127) tests runner not found
[branch_validate] FAIL (code=127) branch_validate runner not found
[commit] FAIL (code=2) no commit message provided and generator failed

# Por eso usamos --minimal:
python push_workflow.py --minimal
  → Solo ejecuta: pre_commit + push
  → Ignora: tests, branch_validate, commit, post_push
```

### Problema 3: htmlcov/ Versionado
```
htmlcov/  ← Esta carpeta NO debe estar en Git
├── index.html          (reportes de coverage)
├── coverage_html*.js
└── z_*_py.html

Por qué es malo:
- Son archivos temporales generados por pytest
- Cambian cada vez que corres tests
- Ocupan espacio innecesario en Git
- Causan conflictos de merge

Solución:
echo "htmlcov/" >> .gitignore
git rm -r --cached htmlcov/
```

---

## ✅ RECOMENDACIÓN MINIMALISTA

### 1. Fijar Pre-commit
```bash
# Editar .pre-commit-config.yaml
default_language_version:
  python: python3  # Sin version específica

# Resultado:
git commit
  → Pre-commit funciona sin errores ✅
  → No necesitas --no-verify
```

### 2. Usar Push Workflow en Minimal
```bash
# Opción A: Push directo (si pre-commit funcionó)
git push origin main

# Opción B: Push workflow como safety net
python tools/git/push_workflow.py --minimal
  → Vuelve a validar con pre-commit
  → Hace git push
  → Listo ✅
```

### 3. Limpiar .gitignore
```bash
# Agregar a .gitignore:
htmlcov/
.coverage
*.coverage

# Remover del repo:
git rm -r --cached htmlcov/ .coverage
git commit -m "chore: remove coverage artifacts"
```

### 4. NO implementar scripts faltantes (por ahora)
```
¿Por qué?
- Solo 2 de 9 tasks de git-push-workflow-v1.0.0 están completas
- Implementar todo = 8-12 horas de trabajo
- Beneficio actual: Bajo (pre-commit es suficiente)
- Filosofía DAATH-ZEN: "Build only what you need"

Decisión:
- Mantener push_workflow.py en modo minimal
- Documentar que solo minimal está implementado
- Si en el futuro necesitas tests automáticos, implementas entonces
```

---

## 🎓 PARA RECORDAR

### Pre-commit = Firewall del Commit
```
Tu código → Pre-commit → Commit
            ↑
            Bloquea código malo
            ANTES de que entre a Git
```

### Push Workflow = Validador del Push
```
Tus commits → Push Workflow → Push a GitHub
              ↑
              Valida TODO el trabajo
              ANTES de subirlo
```

### Complementariedad
```
Pre-commit: "Cada pieza debe ser perfecta"
Push Workflow: "El lote completo debe ser perfecto"

Ambos son necesarios en diferentes momentos
```

---

## 📊 RESUMEN VISUAL

```
┌─────────────────────────────────────────────────────────┐
│                    SITUACIÓN ACTUAL                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Pre-commit:   [████████░░] 80% funcional              │
│                Bug: python3.10 not found                │
│                                                         │
│  Push Workflow: [███░░░░░░░] 30% implementado          │
│                Solo: pre_commit + push                  │
│                Falta: tests, validate, commit, post     │
│                                                         │
│  .gitignore:   [██████░░░░] 60% completo               │
│                Falta: htmlcov/, .coverage               │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                   DESPUÉS DE FIXES                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Pre-commit:   [██████████] 100% funcional ✅          │
│                                                         │
│  Push Workflow: [██████████] 100% (minimal mode) ✅    │
│                Documentado como minimal by design       │
│                                                         │
│  .gitignore:   [██████████] 100% completo ✅           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

**¿Preguntas? Lee**: `.spec-workflow/analysis/gap-analysis-2026-01-08.md`
