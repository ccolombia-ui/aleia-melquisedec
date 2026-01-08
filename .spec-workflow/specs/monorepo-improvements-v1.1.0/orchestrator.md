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

**Git Workflow**:
```bash
# Commits incrementales por task (ver tasks.md para mensajes)
git add .
git commit -m "${task.commitMessage}"

# Tag al completar todas las tasks
git tag -a monorepo-improvements-v1.1.0 -m "Release v1.1.0"

# Push
git push origin main
git push origin monorepo-improvements-v1.1.0
```

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
