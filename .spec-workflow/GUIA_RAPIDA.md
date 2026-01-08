# 🚀 Guía Rápida: spec-workflow-mcp + DAATH-ZEN

## ¿Qué es este sistema?

Un workflow **integrado** de 3 niveles:

1. **spec-workflow-mcp** (Herramienta): Gestionar specs en VS Code
2. **DAATH-ZEN** (Método): Ejecutar con los 5 Rostros + MCPs + Output Triple
3. **Autopoiesis** (Ciclo): Lessons → Patterns → Mejores specs

**📖 Documento principal**: [RESUMEN_SISTEMA_COMPLETO.md](./RESUMEN_SISTEMA_COMPLETO.md) (léelo primero)

---

## ⚡ Quick Start (3 pasos)

### 1. Iniciar Dashboard
```powershell
npx -y spec-workflow-mcp@latest --dashboard --port 5000
```
Abre: http://localhost:5000

### 2. Ver Tareas en VS Code
- Panel lateral → Spec Workflow extension
- Árbol de specs y tareas

### 3. Ejecutar Primera Tarea
Marca `- [-]` en tasks.md para indicar "en progreso"

---

## 📁 Estructura

```
.spec-workflow/
├── RESUMEN_SISTEMA_COMPLETO.md    # ⭐ LEE ESTO PRIMERO
├── GUIA_RAPIDA.md                 # Esta guía
├── steering/
│   ├── product.md                 # Visión DAATH-ZEN
│   ├── tech.md                    # Stack técnico
│   ├── structure.md               # Organización
│   └── best-practices.md          # ⭐ GUÍA COMPLETA
├── specs/
│   └── {spec-name}-vX.Y.Z/
│       ├── requirements.md        # US + REQs
│       ├── design.md              # Architecture
│       ├── tasks.md               # ⭐ Tasks (ver formato abajo)
│       └── lessons-learned/       # Post-execution
└── approvals/                     # Opcional
```

---

## ✍️ Formato tasks.md (CRÍTICO)

**El parser SOLO detecta este formato exacto**:

```markdown
- [ ] 1.1. Fix all nucleo-investigacion references
  - File: *.md, *.py
  - _Requirements: REQ-1_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, grep-search]_
  - _Lesson: lessons-learned/task-1.1-fix-refs.md_
  - _Prompt: Role: MELQUISEDEC | Task: Scan files | Restrictions: None | Success: Fixed_
```

### Elementos OBLIGATORIOS:

| Elemento | Formato | Ejemplo |
|----------|---------|---------|
| Checkbox | `- [ ]` | `- [ ] 1.1. Title` |
| Task ID | `X.Y.` con **PUNTO** | `1.1.` (no `1.1`) |
| File | `- File: paths` | `- File: *.py, *.md` |
| Requirements | `- _Requirements: X_` | `- _Requirements: REQ-1, REQ-2_` |
| Rostro | `- _Rostro: NAME_` | `- _Rostro: MORPHEUS_` |
| MCPs | `- _MCPs: base=[...] \| specialized=[...]_` | Ver arriba |
| Lesson | `- _Lesson: path_` | `- _Lesson: lessons-learned/task-1.1.md_` |
| Prompt | `- _Prompt: Role: X \| Task: Y \| ..._` | Ver arriba |

**❌ Formato incorrecto = 0 tareas detectadas**

---

## 🎭 Los 5 Rostros

| Rostro | Rol | Tareas | MCPs Clave |
|--------|-----|--------|------------|
| **MELQUISEDEC** | Clasificador | Análisis, priorización | filesystem, grep-search |
| **HYPATIA** | Investigadora | Research, papers | brave-search, arxiv |
| **SALOMON** | Analista | Decisiones, análisis | sequential-thinking |
| **MORPHEUS** | Constructor | Diseño, código, tests | python-refactoring |
| **ALMA** | Publicador | Commit, push, docs | git, github |

**TODOS requieren**: `neo4j` + `memory` (MCPs base)

---

## 🎯 Output Triple

Cada tarea produce:

1. **Cypher** (Neo4j): Registro en grafo
2. **Markdown**: Código/docs generados
3. **Lesson**: Aprendizaje extraído (si aplica)

Sin Neo4j + Memory → **NO hay Output Triple válido**

---

## 📦 Specs Disponibles

| Spec | Tasks | Patrón | Status |
|------|-------|--------|--------|
| monorepo-improvements-v1.1.0 | 7 | refactoring | 🟡 Ready |
| demo-fix-references | 5 | refactoring | 🟡 Ready |
| git-push-workflow-v1.0.0 | 9 | git-workflow | 🟢 Ejemplo completo |

**Total: 21 tareas**

---

## 🔄 Workflow Completo

```
Issue → MELQUISEDEC clasifica → Crear spec → Requirements → Design → Tasks
                                                                        ↓
                                    Dashboard detecta → Ejecutar tareas
                                                                        ↓
                    Tarea → Rostro + MCPs → Output Triple (3 outputs)
                                                                        ↓
                            Task final: ALMA agrega lessons
                                                                        ↓
                            3+ specs similares → DAATH-ZEN Pattern
                                                                        ↓
                                Pattern en futuros specs → ♻️ CICLO
```

---

## 🎨 Patrones DAATH-ZEN

Templates reutilizables extraídos de lessons validadas:

- **daath-zen-refactoring**: 7 tasks (confidence: 0.85)
- **daath-zen-git-workflow**: 9 tasks (confidence: 0.88)
- **daath-zen-research**: En desarrollo

**Ubicación**: `_templates/daath-zen-patterns/`

**Uso**:
```bash
cp _templates/daath-zen-patterns/daath-zen-refactoring.md \
   .spec-workflow/specs/my-spec-v1.0.0/requirements.md
```

---

## 🆘 Troubleshooting

### ❌ Tareas muestran 0 en dashboard

**Causa**: Formato incorrecto

**Checklist**:
- [ ] Checkbox: `- [ ] 1.1.` (con **PUNTO** después del número)
- [ ] Metadata indentada (2 espacios)
- [ ] Campos obligatorios: `_Rostro:_`, `_MCPs:_`, `_Lesson:_`
- [ ] Underscores en metadata: `_Field: value_`

### ❌ Dashboard dice "No Projects Available"

**Causa**: MCP server no corriendo

**Solución**:
```powershell
npx -y spec-workflow-mcp@latest --dashboard --port 5000
```

### ❌ Extension no muestra specs

**Causa**: Estructura incorrecta

**Solución**: Verificar que existe:
```
.spec-workflow/specs/{name}-vX.Y.Z/
  ├── requirements.md
  ├── design.md
  └── tasks.md
```

---

## 📚 Recursos Clave

### Documentación
- ⭐ [RESUMEN_SISTEMA_COMPLETO.md](./RESUMEN_SISTEMA_COMPLETO.md) - **LÉELO PRIMERO**
- ⭐ [steering/best-practices.md](./steering/best-practices.md) - Guía completa (10 secciones)
- [_templates/daath-zen-patterns/README.md](../_templates/daath-zen-patterns/README.md) - Catálogo de patrones

### Ejemplos
- ⭐ [specs/git-push-workflow-v1.0.0/](./specs/git-push-workflow-v1.0.0/) - Spec ejemplar completo
- [daath-zen-refactoring.md](../_templates/daath-zen-patterns/daath-zen-refactoring.md) - Pattern de refactoring
- [daath-zen-git-workflow.md](../_templates/daath-zen-patterns/daath-zen-git-workflow.md) - Pattern git ops

### Manifiesto DAATH-ZEN
- [MCPs Recomendados](../docs/manifiesto/03-workflow/04-mcps-recomendados.md)
- [Lesson Template](../_templates/_daath-template/lessons/lesson-template.md)

### External
- [spec-workflow-mcp GitHub](https://github.com/pimzino/spec-workflow-mcp)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## 🚀 Próximos Pasos

1. ✅ **Lee el resumen**: [RESUMEN_SISTEMA_COMPLETO.md](./RESUMEN_SISTEMA_COMPLETO.md)
2. ✅ **Estudia best practices**: [steering/best-practices.md](./steering/best-practices.md)
3. ✅ **Revisa ejemplo**: [specs/git-push-workflow-v1.0.0/](./specs/git-push-workflow-v1.0.0/)
4. ⏳ **Ejecuta task 1.1** de monorepo-improvements
5. ⏳ **Crea primera lesson** real
6. ⏳ **Valida Output Triple** funciona

---

**Sistema operacional y listo para ejecutar** 🎉

**Dashboard**: http://localhost:5000  
**Tareas totales**: 21 (7+5+9)  
**Patrones disponibles**: 2 (refactoring, git-workflow)
