# Guía de Contribución

Bienvenido a **DAATH-ZEN MELQUISEDEC**. Este proyecto sigue principios específicos de organización y filosofía.

## 🎯 Filosofía

Antes de contribuir, lee el [Manifiesto MELQUISEDEC v3.0.0](docs/manifiesto/bereshit-v3.0.0.md).

**Principios clave**:
1. **Autopoiesis**: El sistema se mejora a sí mismo
2. **No inventar**: Orquestar metodologías existentes
3. **Crecimiento orgánico**: Crear solo cuando hay contenido
4. **5 Rostros**: MELQUISEDEC → HYPATIA → SALOMON → MORPHEUS → ALMA

---

## 🚀 Setup del Entorno

```powershell
# 1. Fork y clone
git clone https://github.com/tu-usuario/aleia-melquisedec.git
cd aleia-melquisedec

# 2. Configurar ambiente
cp .env.example .env
# Editar .env con tus credenciales

# 3. Levantar infraestructura
cd infrastructure/docker
docker-compose up -d

# 4. Instalar dependencias (si aplica)
cd ../../packages/core-mcp
pip install -r requirements.txt
```

---

## 📝 Crear Nueva Investigación

```powershell
# 1. Copiar template
cp -r apps/00-template apps/01-mi-investigacion

# 2. Personalizar PROPOSITO.md
cd apps/01-mi-investigacion
code PROPOSITO.md

# 3. Crear solo carpetas necesarias
# NO crear todas las carpetas anticipadamente
# Crear solo cuando tengas contenido
```

---

## 🔧 Modificar Código Reutilizable

### Para `packages/core-mcp`

```powershell
# 1. Crear rama
git checkout -b feature/mejora-mcp

# 2. Hacer cambios
code packages/core-mcp/...

# 3. Testing
python tools/testing/test_mcp_toolkit.py

# 4. Commit siguiendo convención
git commit -m "feat(core-mcp): agregar validación de configuración"
```

### Para `packages/daath-toolkit`

```powershell
# Similar a core-mcp
# Asegurar que no rompe apps existentes
```

---

## 🧪 Testing

Antes de hacer PR, ejecutar:

```powershell
# Test de MCPs
python tools/testing/test_mcp_toolkit.py --verbose

# Test de estructura (cuando esté disponible)
python tools/testing/validate_research_structure.py apps/01-mi-app

# Test de código Python (cuando esté disponible)
pytest packages/
```

---

## 📖 Documentación

### ADRs (Architecture Decision Records)

Para cambios arquitectónicos importantes:

```powershell
# Crear nuevo ADR
code docs/architecture/ADR-{número}-{título}.md
```

Usar template:
```markdown
# ADR {número}: {Título}

**Estado**: Propuesto | Aceptado | Rechazado | Deprecado
**Fecha**: YYYY-MM-DD
**Autores**: [Nombres]

## Contexto
[Problema que se resuelve]

## Decisión
[Qué se decidió y por qué]

## Consecuencias
### Positivas
### Negativas
### Mitigaciones

## Alternativas Consideradas
## Referencias
```

### Guías

Para tutoriales y how-tos:

```powershell
code docs/guides/{nombre-guia}.md
```

---

## 🌳 Estructura de Commits

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>(<scope>): <descripción>

[cuerpo opcional]

[footer opcional]
```

**Tipos**:
- `feat`: Nueva funcionalidad
- `fix`: Bug fix
- `docs`: Cambios en documentación
- `style`: Formateo (no afecta código)
- `refactor`: Refactoring
- `test`: Agregar/modificar tests
- `chore`: Mantenimiento

**Scopes**:
- `core-mcp`: Paquete core-mcp
- `daath-toolkit`: Paquete daath-toolkit
- `apps`: Aplicaciones
- `infrastructure`: Docker, K8s
- `tools`: Scripts
- `docs`: Documentación

**Ejemplos**:
```bash
feat(core-mcp): agregar soporte para Redis MCP
fix(tools): corregir encoding en setup_neo4j.ps1
docs(guides): actualizar guía de MCP Toolkit
refactor(daath-toolkit): simplificar validadores
```

---

## 🔀 Pull Requests

### Checklist

- [ ] Código sigue principios del Manifiesto
- [ ] Tests pasan (`python tools/testing/test_mcp_toolkit.py`)
- [ ] Documentación actualizada
- [ ] Commits siguen convención
- [ ] ADR creado si es cambio arquitectónico
- [ ] Sin archivos de configuración local (`.env`, secretos)

### Template de PR

```markdown
## Descripción
[Qué hace este PR]

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Breaking change
- [ ] Documentación

## Rostro MELQUISEDEC
¿Qué rostro activa este cambio?
- [ ] MELQUISEDEC (Orquestador)
- [ ] HYPATIA (Investigadora)
- [ ] SALOMON (Sintetizador)
- [ ] MORPHEUS (Transformador)
- [ ] ALMA (Narrador)

## Testing
[Cómo se probó]

## Checklist
- [ ] Tests pasan
- [ ] Documentación actualizada
- [ ] ADR creado (si aplica)
```

---

## � Sistema de Issues y Mejoras

### Para Issues del Monorepo (Infraestructura)

Para reportar problemas o proponer mejoras a la estructura del monorepo, herramientas, o infraestructura general:

**Location**: `docs/_meta/inbox/`

#### Crear un Issue

1. **Copiar template**:
   ```powershell
   cp docs/_meta/templates/issue-template.md docs/_meta/inbox/ISSUE-XXX-descripcion.md
   ```

2. **Completar metadata YAML**:
   ```yaml
   ---
   id: ISSUE-XXX
   title: Título descriptivo del issue
   type: bug | enhancement | maintenance | testing
   area: codebase | documentation | packages | tooling | automation | infrastructure
   priority: high | medium | low
   status: open | in-progress | blocked | done
   created: YYYY-MM-DD
   assignee: nombre | null
   tags: [tag1, tag2, tag3]
   related_issues: [ISSUE-001, ISSUE-002]
   ---
   ```

3. **Completar secciones**:
   - **Objetivo**: ¿Qué se busca resolver?
   - **Contexto**: ¿Por qué es necesario?
   - **Solución Propuesta**: ¿Cómo resolverlo?
   - **Implementación**: Pasos concretos
   - **Criterios de Aceptación**: ¿Cuándo está completo?
   - **Testing**: ¿Cómo validar?

#### Workflow de Issues

```
OPEN → IN-PROGRESS → (BLOCKED?) → DONE
  ↓         ↓                        ↓
inbox/   inbox/                   done/
```

**Estados**:
- `open`: Issue nuevo, no iniciado
- `in-progress`: Alguien está trabajando
- `blocked`: Esperando dependencia o decisión
- `done`: Completado y validado

**Mover a done/**:
```powershell
# Cuando se complete el issue
git mv docs/_meta/inbox/ISSUE-XXX-nombre.md docs/_meta/done/ISSUE-XXX-nombre.md

# Actualizar metadata en el archivo
status: done
completed: YYYY-MM-DD
```

#### Buscar Issues

```powershell
# Ver todos los issues abiertos
ls docs/_meta/inbox/

# Buscar por tag
grep -r "tag: cleanup" docs/_meta/inbox/

# Buscar por área
grep -r "area: packages" docs/_meta/inbox/

# Buscar por prioridad alta
grep -r "priority: high" docs/_meta/inbox/
```

#### De Issue a Implementation

Los issues son **SPECS** que se convierten en **PROMPTS** para LLMs:

1. **Issue = SPEC**: Documento con contexto completo
2. **Issue → PROMPT**: Copiar issue completo al LLM
3. **LLM → CODE**: El LLM genera código/cambios
4. **Validation**: Ejecutar criterios de aceptación
5. **Done**: Mover issue a `done/` y cerrar

**Ejemplo**:
```
ISSUE-003 (add pre-commit)
  → Dar todo el issue al LLM
    → LLM genera .pre-commit-config.yaml
      → Ejecutar pytest/tests
        → Marcar como done
```

### Para Issues de Investigación (Apps)

Para issues específicos de proyectos de investigación:

**Location**: `apps/XX-nombre/0-inbox/`

Seguir estructura similar pero dentro del app específico.

### Diferencia: Monorepo vs App Issues

| Aspecto | Monorepo Issues | App Issues |
|---------|-----------------|------------|
| **Location** | `docs/_meta/inbox/` | `apps/XX/0-inbox/` |
| **Scope** | Infraestructura, tools, packages | Investigación específica |
| **Ejemplos** | "Fix imports", "Add pre-commit" | "Analizar dataset", "Entrenar modelo" |
| **Tracking** | Git + local markdown | Local markdown |

---

## 🐛 Reportar Bugs (Quick Issues)

Para bugs simples que no requieren SPEC completo, usar GitHub Issues:

```markdown
## Descripción del problema
[Descripción clara]

## Pasos para reproducir
1. [Paso 1]
2. [Paso 2]
3. [Error]

## Comportamiento esperado
[Qué debería pasar]

## Comportamiento actual
[Qué pasa realmente]

## Entorno
- OS: [Windows/Linux/Mac]
- Docker version: [x.x.x]
- Python version: [x.x.x]

## Logs relevantes
```
[Logs]
```
```

---

## 🎯 Roadmap y Prioridades

Ver [Roadmap](ROADMAP.md) para prioridades actuales.

---

## ❓ Preguntas

- 💬 Discussions: [GitHub Discussions](../../discussions)
- 📧 Email: [email del proyecto]
- 📚 Docs: [docs/](docs/)

---

## 📜 Código de Conducta

Este proyecto adhiere al [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

---

**¡Gracias por contribuir a DAATH-ZEN MELQUISEDEC!** 🙏
