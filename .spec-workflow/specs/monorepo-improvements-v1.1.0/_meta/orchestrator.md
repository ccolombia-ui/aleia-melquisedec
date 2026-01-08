---
id: "monorepo-improvements-v1.1.0-orchestrator"
version: "2.0.0"
principles:
  DRY: "No duplicar contenido - solo referenciar tasks.md"
  SSoT: "Single Source of Truth - steering apunta a manifiesto"
  SeparationOfConcerns: "Orchestrator gestiona flujo, no implementación"
  Idempotencia: "Ejecutar múltiples veces = mismo resultado"
  OutputTriple: "Cypher + Markdown + Lessons (DAATH-ZEN core)"
owners: ["team-infra"]
rostros: ["MELQUISEDEC", "MORPHEUS", "SALOMON", "ALMA"]
required_mcps: ["neo4j", "memory", "filesystem", "sequential-thinking", "grep-search", "python-refactoring"]
---

# DAATH-ZEN Issue Orchestrator: monorepo-improvements-v1.1.0

Orchestrator minimalista que **gestiona el flujo** de ejecución de tasks.md sin duplicar contenido.

---

## FASE 1: PREPARACIÓN

**Cargar Contexto (por referencia, no duplicar)**:
- 📖 Steering Product: [../../steering/product.md](../../steering/product.md) → refs a [docs/manifiesto/](../../../docs/manifiesto/)
- 🛠️ Steering Tech: [../../steering/tech.md](../../steering/tech.md) → refs a docs técnicos
- 📋 Requirements: [requirements.md](requirements.md)
- 🎨 Design: [design.md](design.md)
- ✅ **Tasks (fuente única)**: [tasks.md](tasks.md)

**Validaciones Pre-ejecución**:
```typescript
const status = await mcpClient.callTool('spec-status', {
  projectPath: "/absolute/path/to/project",
  specName: "monorepo-improvements-v1.1.0"
});
// Debe retornar: requirements=approved, design=approved, tasks=approved
```

**MCPs Activos**: Verificar neo4j, memory, filesystem, sequential-thinking, grep-search, python-refactoring

**Directorios**: Crear `Implementation Logs/`, `lessons-learned/`, `artifacts/`

---

## FASE 2: WORKFLOW

**Patrón de Ejecución (referenciando tasks.md)**:
```typescript
// Loop sobre todas las tasks en tasks.md
while (true) {
  // 1. Obtener siguiente tarea pendiente
  const nextTask = await mcpClient.callTool('manage-tasks', {
    projectPath: "/absolute/path/to/project",
    specName: "monorepo-improvements-v1.1.0",
    action: "next-pending"
  });

  if (!nextTask.data?.task) break; // No hay más tasks

  const task = nextTask.data.task;
  console.log(`Iniciando: ${task.id} - ${task.title}`);

  // 2. Marcar como en progreso
  await mcpClient.callTool('manage-tasks', {
    projectPath: "/absolute/path/to/project",
    specName: "monorepo-improvements-v1.1.0",
    action: "set-status",
    taskId: task.id,
    status: "in-progress"
  });

  // 3. EJECUTAR según task.prompt, task.rostro, task.mcps definidos en tasks.md
  //    (NO duplicar lógica aquí - tasks.md es la fuente única)
  await executeTaskFromDefinition(task);

  // 4. Marcar como completada
  await mcpClient.callTool('manage-tasks', {
    projectPath: "/absolute/path/to/project",
    specName: "monorepo-improvements-v1.1.0",
    action: "set-status",
    taskId: task.id,
    status: "completed"
  });

  // 5. Checkpoints (si aplica)
  if (task.id === "1.1") validateCheckpoint("ck-01-no-nucleo-refs");
  if (task.id === "1.5") validateCheckpoint("ck-02-coverage-80");
}
```

---

## FASE 3: IMPLEMENTATION-LOGS

**Registrar cada ejecución**:
```typescript
await mcpClient.callTool('log-implementation', {
  projectPath: "/absolute/path/to/project",
  specName: "monorepo-improvements-v1.1.0",
  taskId: task.id,
  summary: task.summary,
  filesModified: task.filesModified,
  linesAdded: task.stats.linesAdded,
  linesDeleted: task.stats.linesDeleted,
  testsCoverage: task.stats.coverage,
  notes: task.notes
});
```

Archivo generado: `Implementation Logs/task-${taskId}-${name}.md`

---

## FASE 4: LECCIONES-APRENDIDAS

**Crear lesson file** (no meta-tasks como 1.7):
```markdown
# Lesson: Task ${taskId} - ${title}

**Confidence**: ${0.0-1.0}
**Tags**: [${tool}, ${pattern}, ${domain}]

## ✅ What Worked
- [insights específicos]

## ❌ What Didn't Work
- [problemas encontrados]

## 💡 Key Insights
- [aprendizajes transferibles]

## 🔄 Recommendations
- [mejoras para futuras iteraciones]

## 📊 Cypher (Neo4j)
```cypher
CREATE (l:Lesson {
  task_id: "${taskId}",
  spec: "monorepo-improvements-v1.1.0",
  confidence: ${confidence},
  timestamp: datetime()
})
MERGE (s:Spec {name: "monorepo-improvements-v1.1.0"})
MERGE (s)-[:HAS_LESSON]->(l)
```
```

Archivo: `lessons-learned/task-${taskId}-${name}.md`

**Agregación final**: Ejecutar task 1.7 para generar `lessons-learned/summary.yaml`

---

## FASE 5: PERSISTENCIA

**Resumen**: La persistencia final debe usar el `git-push-workflow` compartido (`tools/git/push_workflow.py`) como la *última tarea* del orchestrator. El agente **siempre** debe preguntar (si está en modo interactivo) 2 parámetros antes de ejecutar la persistencia: **(1) lista de archivos a incluir en el push** y **(2) branch destino**. Por política: **NO USAREMOS RAMAS A MENOS QUE SE INDIQUE EXPLÍCITAMENTE** en la configuración (`allow_branch_push: true`) o se pase `--allow-branch-push` vía CLI.

### Uso recomendado (interactivo)
```bash
# Ejemplo interactivo: el agente preguntará por files y branch si no están provistos
python tools/git/push_workflow.py --commit-message "spec: complete monorepo-improvements-v1.1.0"
# El agente preguntará: Files to include in commit (comma-separated) → ej: .spec-workflow/specs/monorepo-improvements-v1.1.0/*,Implementation\ Logs/*,lessons-learned/*
# Luego preguntará: Target branch to push to (empty = current branch)
```

### Uso recomendado (non-interactive / CI)
```bash
# Incluir un archivo .gitpush.yml en el spec o pasar --files/--branch
python tools/git/push_workflow.py --config .spec-workflow/specs/monorepo-improvements-v1.0.0/.gitpush.yml --non-interactive --json-output artifacts/push-summary.json
```

### Ejemplo de `.gitpush.yml` (por spec)
```yaml
stages:
  pre_commit: false
  tests: false
  branch_validate: false
  commit: true
  push: true
  post_push: false
files:
  - ".spec-workflow/specs/monorepo-improvements-v1.1.0/**"
  - "Implementation Logs/**"
  - "lessons-learned/**"
branch: main
allow_branch_push: false
non_interactive: true
commit_message: "spec: complete monorepo-improvements-v1.1.0"
dry_run: false
failure_mode: fail_fast
```

> Nota: Si `non_interactive: true` y no hay `files` o `branch` definidos, el script fallará (esto evita pushes accidentalmente incompletos). El agente está obligado a solicitar ambos parámetros cuando se ejecute interactivamente.

### Integración en el Orchestrator
Añade la llamada al final del bucle de tasks (fase 2) después de: 1) marcar todas las tasks completadas, 2) crear lessons, 3) generar artifacts y logs. Ejemplo (pseudocódigo):
```typescript
// After all tasks are completed and logs/lessons generated
await runCommand(`python tools/git/push_workflow.py --config .spec-workflow/specs/monorepo-improvements-v1.1.0/.gitpush.yml --non-interactive --json-output artifacts/push-summary.json`)
if (pushSummary.results.some(r => !r.ok)) {
  // Log failure and mark spec as needing attention
  await createIssueOrNote("Push failed", pushSummary)
}
```

### Tagging y archivado
- Después de un push exitoso, considerar crear tag de release y mover el spec a `archive/`:
```bash
git tag -a monorepo-improvements-v1.1.0 -m "Release v1.1.0"
python tools/git/push_workflow.py --config .spec-workflow/specs/monorepo-improvements-v1.1.0/.gitpush.yml --non-interactive --post-push
# Archive locally
mv .spec-workflow/specs/monorepo-improvements-v1.1.0 .spec-workflow/archive/specs/
```

### Buenas prácticas recomendadas
- **No duplicar**: usar el script central (`tools/git/push_workflow.py`) y per-spec `.gitpush.yml` para parámetros.
- **Preguntar siempre**: agente debe preguntar `files` y `branch` si no provistos; nunca asumir.
- **No usar ramas salvo explícito**: policy enforced by script; use `allow_branch_push: true` only when intended.
- **Guardar resumen JSON**: usar `--json-output` para registrar el resultado y anexarlo a `Implementation Logs/`.
- **Plantilla por spec**: añadir `.gitpush.example.yml` en la carpeta del spec para guiar al mantenedor.

---

**Neo4j Nodes** (desde lessons):
```bash
# Ejecutar cypher queries desde cada lesson file
cat lessons-learned/task-*.md | grep -A 20 "## 📊 Cypher" | neo4j-import
```

**Archive Spec**:
```bash
mv .spec-workflow/specs/monorepo-improvements-v1.1.0 \
   .spec-workflow/archive/specs/monorepo-improvements-v1.1.0
```

---

## 📚 Referencias

- **Tasks (fuente única)**: [tasks.md](tasks.md)
- **Requirements**: [requirements.md](requirements.md)
- **Design**: [design.md](design.md)
- **Steering**: [../../steering/](../../steering/) (apuntan a manifiesto)
- **Spec Workflow MCP**: [GitHub](https://github.com/pimzino/spec-workflow-mcp)

---

_Orchestrator minimalista: 80 líneas vs 763 originales. DRY, SSoT, Idempotente._
