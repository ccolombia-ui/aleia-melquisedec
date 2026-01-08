# Estrategia de Branching para Investigaciones

## 🌳 Filosofía

Cada investigación en DAATH-ZEN MELQUISEDEC es un **branch independiente** que crece orgánicamente desde `main`. Esta estrategia permite:

- ✅ Desarrollo paralelo de múltiples investigaciones sin conflictos
- ✅ Historial limpio y trazable por investigación
- ✅ Integración controlada de descubrimientos al conocimiento base
- ✅ Experimentación sin riesgo de romper `main`

---

## 📐 Estructura de Branches

### Branch Principal: `main`

- **Propósito**: Estado estable del monorepo
- **Contiene**:
  - Infraestructura base (packages/, infrastructure/, tools/)
  - Documentación general (docs/)
  - Template de investigación (apps/00-template/)
- **Protección**: Branch protegido, solo acepta PRs revisados
- **Nunca contiene**: Investigaciones activas en `apps/XX-nombre/`

### Branches de Investigación: `research/XX-nombre-investigacion`

- **Formato**: `research/[numero]-[nombre-kebab-case]`
- **Ejemplos**:
  - `research/01-grafos-conocimiento-cientifico`
  - `research/02-embeddings-semanticos`
  - `research/03-agentes-autonomos`
- **Propósito**: Desarrollo completo de una investigación
- **Contiene**:
  - Todo de `main`
  - Una carpeta `apps/XX-nombre/` con la investigación
- **Ciclo de vida**:
  1. Creación desde `main`
  2. Desarrollo activo (commits frecuentes)
  3. PR a `main` cuando esté madura (opcional)
  4. Archivado como referencia histórica

### Branches de Features: `feature/descripcion-corta`

- **Formato**: `feature/[descripcion-kebab-case]`
- **Ejemplos**:
  - `feature/nuevo-generador`
  - `feature/mejora-validator`
- **Propósito**: Mejoras a la infraestructura base
- **Contiene**: Cambios en packages/, tools/, infrastructure/
- **Ciclo de vida**: PR rápido a `main`, luego eliminar

### Branches de Hotfix: `hotfix/descripcion`

- **Formato**: `hotfix/[descripcion-kebab-case]`
- **Ejemplos**:
  - `hotfix/docker-compose-memory`
  - `hotfix/neo4j-connection`
- **Propósito**: Correcciones urgentes
- **Ciclo de vida**: PR inmediato a `main`, luego eliminar

---

## 🚀 Workflow Típico

### Iniciar Nueva Investigación

```powershell
# 1. Asegúrate de estar en main actualizado
git checkout main
git pull origin main

# 2. Crea branch de investigación
git checkout -b research/01-mi-investigacion

# 3. Genera la estructura con el toolkit
python packages/daath-toolkit/generators/new_research.py "Mi Investigación"

# 4. Primer commit
git add apps/01-mi-investigacion/
git commit -m "feat(research): initialize 01-mi-investigacion

- Created research structure using DAATH toolkit
- Configured PROPOSITO.md with MELQUISEDEC frontmatter
- Established 0-inbox for rapid capture"

# 5. Push al branch remoto
git push -u origin research/01-mi-investigacion
```

### Desarrollo Continuo

```powershell
# Commits frecuentes en tu branch
git add apps/01-mi-investigacion/
git commit -m "docs(research): add initial literature review"

git add apps/01-mi-investigacion/3-cuadernos/
git commit -m "feat(research): create data exploration notebook"

# Push regular
git push origin research/01-mi-investigacion
```

### Sincronizar con Main (Opcional)

```powershell
# Si main se actualiza y quieres los cambios
git checkout main
git pull origin main

git checkout research/01-mi-investigacion
git merge main -m "chore: sync with main updates"
git push origin research/01-mi-investigacion
```

### Integrar Investigación Madura a Main (Opcional)

```powershell
# Solo cuando la investigación tenga valor para el repositorio base
# Por ejemplo: nuevos patrones, herramientas, documentación

# Crear PR desde GitHub UI o CLI
gh pr create \
  --title "feat(research): integrate 01-mi-investigacion findings" \
  --body "## Summary

Esta investigación exploró [descripción].

## Key Findings
- Finding 1
- Finding 2

## Integration
- Adds apps/01-mi-investigacion/
- Updates docs/ with new patterns
- Enriches shared knowledge base

## MELQUISEDEC Principles
- ✅ Autopoiesis: Sistema se mejora con descubrimientos
- ✅ Organic Growth: Estructura emerge naturalmente
- ✅ Knowledge Synthesis: Conecta con investigaciones previas" \
  --base main \
  --head research/01-mi-investigacion
```

---

## 🔒 Protección de Branches

### `main` Branch Protection (configurar en GitHub)

```yaml
Required Reviews: 1
Require status checks: ✓ Tests workflow
Include administrators: ✓
Require linear history: ✓
Require conversation resolution: ✓
```

### `research/*` Branches (sin protección estricta)

- Permite experimentación libre
- El investigador es dueño de su branch
- Recomendado: pushes frecuentes como backup

---

## 📊 Convenciones de Commits

Usar [Conventional Commits](https://www.conventionalcommits.org/) con scopes específicos:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

- `feat`: Nueva funcionalidad o descubrimiento
- `fix`: Corrección de bug
- `docs`: Solo documentación
- `chore`: Tareas de mantenimiento
- `refactor`: Reestructuración sin cambio funcional
- `test`: Añadir o corregir tests
- `perf`: Mejora de performance

### Scopes para Investigaciones

- `research`: Cambios en `apps/XX-nombre/`
- `core`: Cambios en `packages/core-mcp/`
- `toolkit`: Cambios en `packages/daath-toolkit/`
- `infra`: Cambios en `infrastructure/`
- `tools`: Cambios en `tools/`
- `docs`: Cambios en documentación general

### Ejemplos

```bash
# Investigación
feat(research): add sentiment analysis in 3-cuadernos/exploracion.ipynb
docs(research): document methodology in PROPOSITO.md

# Infraestructura
feat(toolkit): add export functionality to validator
fix(core): resolve Neo4j connection timeout
chore(infra): upgrade Neo4j to 5.16

# Documentación
docs(guides): add Neo4j indexing best practices
docs(manifiesto): clarify HYPATIA rostro principles
```

---

## 🗂️ Naming Conventions

### Research Branches

```
research/[numero]-[tema-principal]

✅ research/01-grafos-conocimiento
✅ research/02-embeddings-multimodales
✅ research/03-agentes-conversacionales

❌ research/investigacion-1
❌ research/mi-research
❌ research/test
```

### Feature Branches

```
feature/[componente]-[descripcion]

✅ feature/toolkit-batch-generator
✅ feature/core-async-queries
✅ feature/infra-kubernetes-setup

❌ feature/mejora
❌ feature/fix
```

### Hotfix Branches

```
hotfix/[problema-especifico]

✅ hotfix/neo4j-memory-leak
✅ hotfix/docker-compose-ports
✅ hotfix/validator-yaml-parsing

❌ hotfix/arreglo
❌ hotfix/urgente
```

---

## 📅 Ciclo de Vida de Investigaciones

### Fase 1: Iniciación (Semana 1)

```
research/01-nombre
├── Branch creado desde main
├── apps/01-nombre/ generado con toolkit
├── PROPOSITO.md completado con objetivos
└── Primera exploración en 0-inbox/
```

**Commits**: 5-10 commits iniciales de setup

### Fase 2: Exploración (Semanas 2-4)

```
research/01-nombre
├── Commits diarios en 3-cuadernos/
├── Referencias en 1-referencias/
├── Experimentos en 4-dataset/
└── Documentación iterativa en PROPOSITO.md
```

**Commits**: 20-50 commits de desarrollo activo

### Fase 3: Consolidación (Semanas 5-6)

```
research/01-nombre
├── Notebooks limpios y documentados
├── Outputs finales en 5-outputs/
├── README.md completo
└── PROPOSITO.md actualizado con hallazgos
```

**Commits**: 10-15 commits de documentación

### Fase 4: Integración (Opcional)

```
PR: research/01-nombre → main
├── Review de 1-2 peers
├── CI/CD pasa todos los checks
├── Documentación actualizada en docs/
└── Merge con squash o merge commit
```

**Resultado**: Conocimiento integrado al repositorio base

### Fase 5: Archivo

```
Branch: research/01-nombre
├── No eliminado (mantener historial)
├── Marcado como "archived" en GitHub
├── Referenciado en docs/research-index.md
└── Disponible para consultas futuras
```

---

## 🔄 Sincronización Multi-Investigador

### Escenario: 2+ investigadores trabajando en paralelo

```
main
├── research/01-investigador-a
│   └── apps/01-tema-a/
└── research/02-investigador-b
    └── apps/02-tema-b/
```

**Estrategia**:
1. Cada investigador trabaja en su branch independiente
2. **No hay conflictos** porque cada uno tiene su `apps/XX-nombre/`
3. Pushes frecuentes a sus branches remotos
4. Sincronización con `main` solo cuando sea necesario

### Escenario: Colaboración en misma investigación

```
research/01-tema-compartido
├── Investigador A: 3-cuadernos/analisis-parte1.ipynb
└── Investigador B: 3-cuadernos/analisis-parte2.ipynb
```

**Estrategia**:
1. Comunicación frecuente (daily standups)
2. Dividir trabajo en archivos/carpetas distintas
3. Pull antes de cada sesión: `git pull origin research/01-tema-compartido`
4. Commits pequeños y frecuentes
5. Si hay conflictos, resolverlos colaborativamente

---

## 🎯 Casos de Uso Avanzados

### Investigación que Deriva en Feature

```bash
# Descubres un patrón útil en tu investigación
# que debería ser parte del toolkit

# 1. Crea feature branch desde main
git checkout main
git checkout -b feature/pattern-from-research-01

# 2. Extrae y generaliza el código
cp apps/01-mi-investigacion/utils/pattern.py packages/daath-toolkit/patterns/

# 3. Commit y PR a main
git add packages/daath-toolkit/patterns/pattern.py
git commit -m "feat(toolkit): add pattern discovered in research-01"
git push -u origin feature/pattern-from-research-01

# 4. Crear PR a main
gh pr create --base main --head feature/pattern-from-research-01

# 5. Una vez merged, actualiza tu research branch
git checkout research/01-mi-investigacion
git merge main
```

### Investigación Pausada y Retomada

```bash
# Pausar (ya pushed a remote)
git checkout main

# ... tiempo pasa ...

# Retomar
git checkout research/01-mi-investigacion
git pull origin research/01-mi-investigacion  # Por si hubo cambios
git merge main  # Sincronizar con actualizaciones de main

# Continuar trabajando
```

### Investigación Publicable (Paper)

```bash
# Tu investigación resulta en un paper
# Crea un tag en el branch de investigación

git checkout research/01-mi-investigacion
git tag -a publication/paper-2026 -m "Version published in Journal XYZ 2026"
git push origin publication/paper-2026

# Ahora puedes referenciar este tag específico
# para reproducibilidad del paper
```

---

## ✅ Checklist de Inicio de Investigación

- [ ] Branch creado con nombre correcto: `research/XX-nombre`
- [ ] Estructura generada con `new_research.py`
- [ ] PROPOSITO.md completado con:
  - [ ] Frontmatter YAML
  - [ ] Objetivos claros
  - [ ] Metodologías seleccionadas
  - [ ] Tags relevantes
- [ ] Primer commit con mensaje semántico
- [ ] Push a remote: `git push -u origin research/XX-nombre`
- [ ] README.md local con quick start
- [ ] .gitignore configurado para datos grandes

---

## ✅ Checklist de Integración a Main

- [ ] Investigación tiene hallazgos valiosos para el repositorio
- [ ] Documentación completa y clara
- [ ] Notebooks ejecutables sin errores
- [ ] Sin datos sensibles o credenciales
- [ ] PR creado con descripción detallada
- [ ] Tests pasan (si aplica)
- [ ] Revisión de al menos 1 peer
- [ ] CHANGELOG.md actualizado
- [ ] Merge realizado

---

## 📚 Referencias

- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Manifiesto MELQUISEDEC v3.0.0](../manifiesto/bereshit-v3.0.0.md)
- [ADR-001: Monorepo Structure](../architecture/ADR-001-monorepo-structure.md)
