# GitHub Actions Workflows - Guía de Uso

## 📋 Workflows Disponibles

El proyecto DAATH-ZEN MELQUISEDEC incluye 4 workflows automatizados de GitHub Actions que mantienen la calidad y coherencia del repositorio.

---

## 1. CI/CD Pipeline (`.github/workflows/test.yml`)

### ⚡ Trigger
- Push a: `main`, `develop`, `research/**`, `feature/**`
- Pull requests a: `main`
- Manual: `workflow_dispatch`

### 🎯 Jobs

#### `validate-structure`
Valida la estructura de las investigaciones:
- ✅ Template (apps/00-template/) tiene estructura correcta
- ✅ Todas las research apps siguen el patrón DAATH-ZEN
- ✅ No hay números de app duplicados

#### `check-documentation`
Verifica documentación requerida:
- ✅ Archivos principales existen (README, ARQUITECTURA, etc.)
- ✅ Cada research app tiene PROPOSITO.md
- ✅ No hay links rotos (basic check)

#### `lint-commits`
Valida mensajes de commit (solo PRs):
- ✅ Siguen [Conventional Commits](https://www.conventionalcommits.org/)
- ✅ Formato: `type(scope): description`
- ✅ Types válidos: feat, fix, docs, chore, refactor, test, perf, ci, build, revert

#### `check-branch-naming`
Valida nombres de branches (solo PRs):
- ✅ `research/XX-nombre-kebab-case`
- ✅ `feature/descripcion-kebab-case`
- ✅ `hotfix/descripcion-kebab-case`

#### `security-check`
Escanea por problemas de seguridad:
- ✅ No hay credenciales hardcodeadas
- ✅ Archivos .env no están commiteados

#### `test-generators`
Prueba herramientas del toolkit:
- ✅ `new_research.py` funciona en modo dry-run

### 📊 Ejemplo de Uso

```bash
# Este push dispara el workflow completo
git checkout research/01-mi-investigacion
git add apps/01-mi-investigacion/
git commit -m "feat(research): add initial data exploration"
git push origin research/01-mi-investigacion
```

**Resultado**: GitHub Actions ejecuta automáticamente todos los checks. Verás ✅ o ❌ en el commit.

---

## 2. Changelog Automation (`.github/workflows/changelog.yml`)

### ⚡ Trigger
- Pull request **merged** a `main`

### 🎯 Funcionalidad

Actualiza automáticamente `CHANGELOG.md` cuando se hace merge de un PR:

1. **Extrae versión** del título del PR (si existe `v1.2.3`)
2. **Determina sección** según tipo de commit:
   - `feat` → Added
   - `fix` → Fixed
   - `docs` → Documentation
   - `refactor` → Changed
   - `perf` → Performance
3. **Añade entrada** con: título, número de PR, autor
4. **Commit automático** a `main`

### 📊 Ejemplo de Uso

```bash
# 1. Crear PR desde research branch
gh pr create \
  --title "feat(research): integrate sentiment analysis findings v1.1.0" \
  --body "Adds sentiment analysis research..." \
  --base main \
  --head research/02-sentiment

# 2. Merge del PR (via GitHub UI o CLI)
gh pr merge 5 --squash

# 3. El workflow automáticamente:
#    - Detecta versión: 1.1.0
#    - Añade a CHANGELOG.md:
#      ### Added
#      - feat(research): integrate sentiment analysis findings (#5 by @username)
#    - Commit y push a main
```

### ⚠️ Notas
- Si no hay versión en título, usa fecha: `unreleased-2026-01-08`
- El bot hace commit como `github-actions[bot]`

---

## 3. Documentation Health Check (`.github/workflows/documentation.yml`)

### ⚡ Trigger
- Push a `main` o `research/**` que modifiquen docs o .md
- Pull requests a `main` que modifiquen docs
- **Schedule**: Lunes a las 9 AM (weekly)
- Manual: `workflow_dispatch`

### 🎯 Jobs

#### `check-documentation-health`
Analiza salud de documentación:
- ✅ No hay archivos "huérfanos" (sin referencias)
- ✅ README tiene secciones requeridas
- ✅ YAML frontmatter válido en PROPOSITO.md
- ✅ Lista TODOs/FIXMEs para crear issues
- ✅ Identifica docs no actualizados (>90 días)
- 📊 Genera reporte semanal (artifact)

#### `check-code-documentation`
Valida docstrings en Python:
- ✅ Funciones tienen docstrings
- ✅ Clases tienen docstrings
- ⚠️ Lista funciones sin documentar

### 📊 Ejemplo de Uso

```bash
# Este push dispara el check
git checkout research/01-mi-investigacion
git add apps/01-mi-investigacion/PROPOSITO.md
git commit -m "docs(research): update methodology section"
git push origin research/01-mi-investigacion

# El workflow verifica:
# - PROPOSITO.md tiene YAML válido
# - Campos requeridos: id, version, created, status, purpose
# - No hay TODOs pendientes
```

**Reporte Semanal**: Descarga artifact "documentation-health-report" desde GitHub Actions tab.

---

## 4. Release Management (`.github/workflows/release.yml`)

### ⚡ Trigger
- Push de tags: `v*.*.*` (ej: `v1.0.0`)
- Manual: `workflow_dispatch` con input de versión

### 🎯 Jobs

#### `create-release`
Crea release en GitHub:
1. **Extrae changelog** para la versión
2. **Genera estadísticas**: commits, contributors, files, apps
3. **Crea GitHub Release** con notas automáticas
4. **Enlaza documentación** relevante

#### `validate-release`
Valida que el release está completo:
- ✅ Template válido
- ✅ Documentación principal presente
- ✅ Changelog actualizado

### 📊 Ejemplo de Uso

#### Opción 1: Via Tag (automático)

```bash
# 1. Actualizar CHANGELOG.md manualmente
nano CHANGELOG.md
# Añadir sección:
# ## [1.2.0] - 2026-01-08
# ### Added
# - Nueva feature...

git add CHANGELOG.md
git commit -m "docs: prepare CHANGELOG for v1.2.0"

# 2. Crear y push tag
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0

# 3. El workflow automáticamente:
#    - Crea GitHub Release con notas del CHANGELOG
#    - Añade estadísticas del proyecto
#    - Valida que todo está correcto
```

#### Opción 2: Manual (via GitHub UI)

1. Ve a: `Actions` → `Release Management` → `Run workflow`
2. Ingresa versión: `1.2.0`
3. Click `Run workflow`
4. El workflow hace todo automáticamente

---

## 🤖 ¿Son los Workflows "Prompts"?

### Respuesta: **NO exactamente, pero SÍ son instrucciones automatizadas**

Los workflows de GitHub Actions **NO son prompts para LLMs**, son **scripts YAML** que ejecutan comandos shell, Python, y acciones predefinidas.

### Comparación

| Aspecto | GitHub Actions Workflows | Prompts para LLMs |
|---------|-------------------------|-------------------|
| **Naturaleza** | Scripts declarativos en YAML | Instrucciones en lenguaje natural |
| **Ejecución** | Runners de GitHub (VMs Linux/Windows) | Modelo de lenguaje (GPT, Claude, etc.) |
| **Lenguaje** | YAML + Shell + Python | Inglés, español, etc. |
| **Determinismo** | Altamente determinístico | Probabilístico, puede variar |
| **Trigger** | Eventos de Git (push, PR, tag) | Invocación humana o API |
| **Objetivo** | Automatizar CI/CD, checks, deploys | Generar texto, código, análisis |

### Pero... 🤔

Los workflows **SÍ pueden considerarse "prompts"** en un sentido más amplio:

1. **Instrucciones claras**: Le dicen a GitHub qué hacer
2. **Contexto estructurado**: Definen cuando y cómo ejecutar
3. **Outputs esperados**: Especifican resultados deseados

### Arquitectura de un Workflow

```yaml
name: Mi Workflow              # ← Nombre descriptivo
on: [push]                     # ← Trigger (cuándo ejecutar)

jobs:                          # ← Trabajos a realizar
  mi-job:
    runs-on: ubuntu-latest     # ← Entorno de ejecución
    steps:                     # ← Pasos secuenciales
      - uses: actions/checkout@v4              # ← Acción predefinida
      - run: python mi_script.py               # ← Comando shell
      - run: |                                 # ← Multi-línea
          echo "Paso 1"
          echo "Paso 2"
```

### Paralelismo con Prompts

Si un workflow fuera un "prompt para un sistema de CI/CD", sería así:

```
PROMPT (lenguaje natural):
"Cuando alguien haga push a main:
1. Descarga el código
2. Ejecuta tests de Python
3. Valida estructura de investigaciones
4. Si todo pasa, marca el commit con ✅
5. Si algo falla, notifica al autor"

WORKFLOW (YAML):
name: CI
on: push: branches: [main]
jobs:
  test:
    steps:
      - checkout
      - setup python
      - run tests
      - validate structure
```

---

## 🔧 Mantenimiento de Workflows

### Modificar un Workflow

```bash
# 1. Editar el archivo YAML
nano .github/workflows/test.yml

# 2. Commit con tipo 'ci'
git add .github/workflows/test.yml
git commit -m "ci: add code coverage check to test workflow"

# 3. Push para probar
git push origin main

# 4. Verificar en GitHub → Actions
```

### Debugging

Si un workflow falla:

1. **Ver logs**: GitHub → Actions → Click en workflow → Click en job
2. **Reproducir localmente**:
   ```bash
   # Instalar act (GitHub Actions local)
   # https://github.com/nektos/act

   act push -j validate-structure
   ```
3. **Revisar sintaxis**: [GitHub Actions Validator](https://rhysd.github.io/actionlint/)

### Mejores Prácticas

- ✅ Mantener workflows **modulares** (un job por responsabilidad)
- ✅ Usar **actions reutilizables** del marketplace
- ✅ **Documentar** cada job con comentarios
- ✅ **Versionear** actions (ej: `@v4` no `@latest`)
- ✅ **Cachear** dependencias para velocidad
- ✅ **Condicionales** para ejecutar solo cuando necesario

---

## 📊 Dashboard de Estado

Puedes añadir estos badges al README:

```markdown
[![CI/CD](https://github.com/ccolombia-ui/aleia-melquisedec/actions/workflows/test.yml/badge.svg)](https://github.com/ccolombia-ui/aleia-melquisedec/actions)
[![Docs Health](https://github.com/ccolombia-ui/aleia-melquisedec/actions/workflows/documentation.yml/badge.svg)](https://github.com/ccolombia-ui/aleia-melquisedec/actions)
```

---

## 🎯 Quick Reference

| Necesito... | Workflow | Archivo |
|------------|----------|---------|
| Validar estructura de research | CI/CD Pipeline | `test.yml` |
| Actualizar CHANGELOG automático | Changelog Automation | `changelog.yml` |
| Revisar salud de docs | Documentation Health | `documentation.yml` |
| Crear release en GitHub | Release Management | `release.yml` |
| Verificar commits convencionales | CI/CD Pipeline | `test.yml` (lint-commits) |
| Validar nombres de branches | CI/CD Pipeline | `test.yml` (check-branch-naming) |
| Escanear seguridad | CI/CD Pipeline | `test.yml` (security-check) |

---

## 📚 Referencias

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Estrategia de Branching](./estrategia-branching.md)
