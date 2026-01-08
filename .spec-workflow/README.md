# .spec-workflow - Spec-Driven Development + DAATH-ZEN

## 🎯 Sistema Integrado de 3 Niveles

Esta carpeta implementa un **workflow completo** que combina:

1. **spec-workflow-mcp**: Herramienta de gestión (VS Code extension + dashboard)
2. **DAATH-ZEN**: Metodología de ejecución (5 Rostros + MCPs + Output Triple)
3. **Autopoiesis**: Ciclo de aprendizaje (Lessons → Patterns → Mejora continua)

---

## 📖 Documentación Principal (EMPIEZA AQUÍ)

| Documento | Propósito | Cuándo Leer |
|-----------|-----------|-------------|
| ⭐ [RESUMEN_SISTEMA_COMPLETO.md](_meta/RESUMEN_SISTEMA_COMPLETO.md) | Visión general del sistema | **LEE PRIMERO** |
| 🚀 [GUIA_RAPIDA.md](_meta/GUIA_RAPIDA.md) | Quick start, troubleshooting | Segundo paso |
| 📋 [steering/best-practices.md](_meta/best-practices.md) | Guía completa (10 secciones) | Referencia continua |
| 🎨 [_templates/daath-zen-patterns/](../templates/daath-zen-patterns/) | Catálogo de patterns | Al crear nuevos specs |

---

## 📁 Estructura Completa

```
.spec-workflow/
├── RESUMEN_SISTEMA_COMPLETO.md    # ⭐ Documento maestro
├── GUIA_RAPIDA.md                 # Quick start
├── README.md                      # Este archivo
├── steering/                      # Contexto global del proyecto
│   ├── product.md                 # Visión DAATH-ZEN
│   ├── tech.md                    # Stack técnico
│   ├── structure.md               # Organización
│   └── best-practices.md          # ⭐ Guía completa
├── specs/                         # Especificaciones activas
│   ├── monorepo-improvements-v1.1.0/
│   │   ├── requirements.md        # 6 User Stories
│   │   ├── design.md              # Architecture
│   │   ├── tasks.md               # 7 tasks con rostros + MCPs
│   │   └── lessons-learned/       # (Futuro)
│   ├── demo-fix-references/
│   │   ├── requirements.md        # 4 User Stories
│   │   ├── design.md              # Reference fixing
│   │   ├── tasks.md               # 5 tasks con rostros + MCPs
│   │   └── lessons-learned/       # (Futuro)
│   └── git-push-workflow-v1.0.0/  # ⭐ EJEMPLO COMPLETO
│       ├── requirements.md        # 4 US, 6 REQs, 3 NFRs
│       ├── design.md              # Full architecture + diagrams
│       ├── tasks.md               # 9 tasks completas
│       └── lessons-learned/       # Ready for lessons
├── approvals/                     # Approval flow (opcional)
└── archive/                       # Specs completados (histórico)
```

---

## 🧠 DAATH-ZEN: Los 5 Rostros

| Rostro | Rol | MCPs Típicos | Tareas Típicas |
|--------|-----|--------------|----------------|
| **MELQUISEDEC** | Clasificador | grep-search, file-search, semantic-search | Análisis, búsqueda, triage |
| **HYPATIA** | Investigador | fetch-webpage, github-repo, context7 | Research, documentación externa |
| **SALOMON** | Analista | python-refactoring, get-errors, list-code-usages | Análisis estático, refactoring |
| **MORPHEUS** | Diseñador | python-env, pytest, run-terminal | Implementación, testing |
| **ALMA** | Publicador | create-file, replace-string, git-add-commit | Escritura, commits, cierre |

**MCPs Base (OBLIGATORIOS)**: `neo4j`, `memory` (para Output Triple)

Más info: [steering/best-practices.md#mcps-por-tipo-de-tarea](_meta/best-practices.md)

---

## 📊 Estado Actual del Sistema

| Spec | Versión | Tasks | Estado | Patrón Usado |
|------|---------|-------|--------|--------------|
| monorepo-improvements | v1.1.0 | 7 | ⚙️ Ready | daath-zen-refactoring |
| demo-fix-references | - | 5 | ⚙️ Ready | daath-zen-refactoring |
| git-push-workflow | v1.0.0 | 9 | ⭐ Example | daath-zen-git-workflow |
| **TOTAL** | - | **21** | - | - |

**Dashboard**: http://localhost:5000 (F5 para refrescar)

---

## 🎨 DAATH-ZEN Patterns

Patterns reutilizables para acelerar creación de specs:

| Pattern | Versión | Confidence | Specs | Link |
|---------|---------|------------|-------|------|
| **daath-zen-refactoring** | v1.0.0 | 0.85 | 3 | [Ver pattern](../_templates/daath-zen-patterns/daath-zen-refactoring.md) |
| **daath-zen-git-workflow** | v1.0.0 | 0.88 | 1 | [Ver pattern](../_templates/daath-zen-patterns/daath-zen-git-workflow.md) |

**Catálogo Completo**: [_templates/daath-zen-patterns/README.md](../_templates/daath-zen-patterns/README.md)

**Criterios para Nuevo Pattern**:
- ✅ Validado en 3+ specs
- ✅ Generalizable (no específico a un proyecto)
- ✅ Reduce tiempo ≥30%
- ✅ Lessons con confidence ≥ 0.80

---

## 🔄 Workflow Completo (9 Pasos)

```
1. Lee task (ROSTRO detecta su tarea)
   ↓
2. Consulta neo4j + memory (contexto)
   ↓
3. Usa MCPs especializados (tools)
   ↓
4. Ejecuta tarea (código/docs/análisis)
   ↓
5. Genera Output Triple:
   - Cypher → Neo4j (trazabilidad)
   - Markdown → Code/Docs (deliverable)
   - Lesson → lessons-learned/ (aprendizaje)
   ↓
6. Commit (git-push si aplica)
   ↓
7. Marca tarea como ✅ (dashboard)
   ↓
8. Al finalizar spec: Agrega lessons (task X.9)
   ↓
9. Patrón validado (3+ specs) → daath-zen-<type>
```

---

## 🚀 Cómo Empezar

### 1️⃣ **Primera Vez**
```bash
# Dashboard activo
# http://localhost:5000

# Verifica que aparezcan 21 tasks
# Si no aparecen: Ver GUIA_RAPIDA.md → Troubleshooting
```

### 2️⃣ **Ejecuta Primera Task**
```markdown
# monorepo-improvements-v1.1.0/tasks.md
- [ ] 1.1. Fix nucleo-investigacion references
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[grep-search, file-search]_
  - _Lesson: lessons-learned/task-1.1-fix-references.md_
```

### 3️⃣ **Genera Output Triple**
- **Cypher**: Log a Neo4j con metadatos
- **Markdown**: Cambios en código (git diff o nuevos archivos)
- **Lesson**: Documenta en `lessons-learned/task-1.1-fix-references.md`

---

## 🛠️ Comandos Útiles

```bash
# Dashboard
# Ya está corriendo en localhost:5000

# Ver tasks en terminal
grep -r "\- \[ \]" .spec-workflow/specs/*/tasks.md

# Validar formato de tasks (crítico)
# CORRECTO: - [ ] X.Y. Title
# INCORRECTO: - [ ] X.Y Title (falta punto)

# Refrescar dashboard
# F5 en navegador
```

---

## 📚 Recursos Adicionales

| Recurso | Link |
|---------|------|
| Manifiesto DAATH-ZEN v4 | [docs/manifiesto/](../docs/manifiesto/) |
| Workflow Autopoiesis | [[05-autopoiesis]] |
| ADR Monorepo | [docs/architecture/ADR-001-monorepo-structure.md](../docs/architecture/ADR-001-monorepo-structure.md) |
| MCPs Docker Toolkit | [docs/guides/docker-mcp-toolkit.md](../docs/guides/docker-mcp-toolkit.md) |
| Estrategia Branching | [docs/guides/estrategia-branching.md](../docs/guides/estrategia-branching.md) |

---

## ✅ Checklist de Validación

### Para Nuevas Tasks
- [ ] Formato: `- [ ] X.Y. [Verbo] + [Objeto]`
- [ ] Campo `_Rostro: NOMBRE_` presente
- [ ] Campo `_MCPs:` con base + specialized
- [ ] Campo `_Lesson:` con path o N/A
- [ ] Campo `_Prompt:` estructurado (Role | Task | Restrictions | Success)

### Para Nuevos Specs
- [ ] 3 archivos mínimos: requirements.md, design.md, tasks.md
- [ ] User Stories numeradas (US-1, US-2...)
- [ ] Reqs funcionales numerados (REQ-1, REQ-2...)
- [ ] Tasks con rostros asignados
- [ ] Directorio `lessons-learned/` creado
- [ ] Task final (X.9) para agregar lessons

### Para Crear Pattern
- [ ] Validado en 3+ specs
- [ ] Lessons con confidence ≥ 0.80
- [ ] Variaciones documentadas
- [ ] Template en `_templates/daath-zen-patterns/`
- [ ] README actualizado

---

## 🐛 Troubleshooting

### Tasks no aparecen en dashboard
1. **Verifica formato**: `- [ ] X.Y.` (punto después del número)
2. **Refresca dashboard**: F5 en navegador
3. **Revisa logs**: `spec-workflow-mcp` output en VS Code
4. **Ver**: [GUIA_RAPIDA.md#troubleshooting](_meta/GUIA_RAPIDA.md#troubleshooting)

### MCPs no están disponibles
1. **Docker corriendo**: `docker ps` debe mostrar contenedores
2. **MCPs en config**: Verifica `packages/core-mcp/config/`
3. **Ver**: [docs/guides/docker-mcp-toolkit.md](../docs/guides/docker-mcp-toolkit.md)

### Lessons no se generan
1. **Campo presente**: `_Lesson: path_` en task
2. **Directorio existe**: `mkdir lessons-learned/`
3. **Output Triple**: Verifica que Cypher + Markdown + Lesson se generen juntos
4. **Ver**: [steering/best-practices.md#output-triple](_meta/best-practices.md)

---

## 📝 Próximos Pasos Sugeridos

1. ✅ **Sistema documentado** (este README)
2. ⏭️ **Ejecutar primera task** (monorepo-improvements 1.1)
3. ⏭️ **Validar Output Triple** (Cypher + Markdown + Lesson)
4. ⏭️ **Completar primer spec** (monorepo-improvements)
5. ⏭️ **Agregar lessons** (task 1.7)
6. ⏭️ **Evolucionar pattern** (actualizar daath-zen-refactoring si hay nuevos insights)

---

**Última actualización**: 2024 (Sistema v3.0)  
**Mantenido por**: ALMA (Rostro Publicador DAATH-ZEN)
