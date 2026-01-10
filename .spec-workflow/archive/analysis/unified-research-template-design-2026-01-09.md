# Prompt de Análisis: Unified Research Template con Versionado y Triple Persistencia

> **Created**: 2026-01-09
> **Purpose**: Diseñar un template unificado de investigación con gestión de épicas, versionado automático y coherencia triple (MD + Grafo + Vector)
> **Thinking Mode**: Complex reasoning con múltiples MCPs
> **Status**: 🔄 Analysis in progress

---

## 🎯 Contexto del Problema

### Situación Actual

Existen dos templates separados:
- `research-methodology-template`: Para investigaciones académicas puras
- `app-spec-template`: Para especificaciones de aplicaciones

### Necesidad Identificada

Crear **UN SOLO TEMPLATE UNIFICADO** que:

1. **Fase común** (MELQUISEDEC → HYPATIA → SALOMON): Construir dominio de conocimiento confiable y trazable
2. **Fase divergente** (SALOMON → adelante): Workflow diferenciado según tipo de artefacto:
   - `research`: Continúa con análisis académico puro
   - `app`: Genera especificaciones de aplicación (HEX/HEX-WF/HEX-WF-MCP)
   - `social-project`: Genera diseños de proyectos sociales con stakeholders y teoría del cambio

### Requerimientos Críticos del Template

#### 1. Gestión de Épicas y Versionado
```yaml
workflow:
  epic: "fundacion"  # Primera épica de la investigación
  version_strategy: "semantic"  # v1.0.0, v1.1.0, v2.0.0

version_lifecycle:
  - phase: "active_development"
    epic: "fundacion"
    version: "v1.0.0-dev"
    documents:
      - 01-literature/*.md
      - 02-atomics/*.md
      - 03-workbook/*.md
      - 04-artifacts/*

  - phase: "epic_closure"
    trigger: "all tasks completed"
    action: "archive entire epic with semantic version"
    result: "archive/issue-research-dsr-v1.0.0/"

  - phase: "gap_resolution"
    trigger: "lessons-learned identifies gaps"
    action: "clean spec-issue for new tasks"
    result: "new epic with version v1.1.0 or v2.0.0"
```

#### 2. Triple Persistencia Coherente
```yaml
persistence:
  layers:
    markdown:
      path: "{spec-path}/{phase}/{documents}.md"
      version_control: "git"

    graph:
      database: "neo4j"
      labels: ["Concept", "Source", "Relationship", "Version"]
      properties:
        - version_tag: "v1.0.0"
        - epic_name: "fundacion"
        - created_at: timestamp
        - archived: boolean

    vector:
      store: "chroma/qdrant/weaviate"  # TBD
      collections:
        - name: "atomics_v1"
        - metadata: {version: "v1.0.0", epic: "fundacion"}
        - embeddings: "text-embedding-3-small"

  coherence_strategy:
    on_document_create:
      - write_markdown
      - create_graph_node(md_path)
      - generate_embedding(content)
      - link_all_three_with_uuid

    on_epic_closure:
      - archive_markdown_folder
      - tag_graph_nodes(archived=true, version="v1.0.0")
      - archive_vector_collection("atomics_v1.0.0")

    on_rollback:
      - git_revert(commit_sha)
      - neo4j_restore_snapshot(version)
      - vector_restore_snapshot(version)
```

#### 3. Gestión de Contexto y Git Workflow
```yaml
context_management:
  per_task:
    - save_context: "mcp_memory store"
    - checkpoint: "CK-{phase}-{task_id}"
    - git_operations:
        - commit: "feat({task_id}): {task_description}"
        - tag: "task-{task_id}-complete"

  per_epic:
    - aggregate_context: "all tasks in epic"
    - final_commit: "chore(epic-{name}): close v{version}"
    - git_tag: "v{version}"
    - push: "origin main"

  rollback_capability:
    levels:
      - task_level: "git revert {task_commit}"
      - epic_level: "git reset --hard v{previous_version}"
      - graph_level: "neo4j restore from snapshot"
      - vector_level: "restore vector collection backup"
```

---

## 🧠 Instrucciones para el Agente con Pensamiento Complejo

### Objetivo Principal

Diseñar la arquitectura completa del **Unified Research Template** que resuelva:
1. Unificación de templates con workflows divergentes
2. Gestión de épicas y versionado semántico
3. Triple persistencia coherente (MD + Graph + Vector)
4. Workflow git integrado con checkpoints
5. Capacidad de rollback multi-capa
6. Mejores prácticas para mantener coherencia

### Metodología de Pensamiento Requerida

Utiliza **Sequential Thinking** para explorar el problema paso a paso:

```yaml
thinking_process:
  tool: "mcp_sequential-th_sequentialthinking"
  total_thoughts_estimate: 20-30

  phases:
    1_understanding:
      thoughts: 1-5
      focus: "Analizar templates actuales, identificar puntos de unificación"

    2_architecture:
      thoughts: 6-12
      focus: "Diseñar estructura unificada con workflows divergentes"

    3_versioning:
      thoughts: 13-18
      focus: "Diseñar sistema de épicas + versionado + archivado"

    4_persistence:
      thoughts: 19-25
      focus: "Diseñar triple persistencia con coherencia"

    5_verification:
      thoughts: 26-30
      focus: "Validar diseño, identificar risks, proponer mitigaciones"
```

### MCPs a Activar

#### MCPs de Pensamiento Complejo
```yaml
thinking_mcps:
  - name: "sequential-thinking"
    id: "mcp_sequential-th_sequentialthinking"
    use: "Análisis paso a paso del diseño"

  - name: "smart-thinking"
    id: "mcp_ai_smithery_l_smartthinking"
    use: "Exploración de alternativas de arquitectura"

  - name: "maxential-thinking"
    id: "mcp_maxential-thi_branch"
    use: "Branches para comparar estrategias de persistencia"
```

#### MCPs de Memoria y Contexto
```yaml
memory_mcps:
  - name: "memory-search"
    id: "mcp_ai_smithery_l_search"
    use: "Buscar decisiones previas en smart-thinking memory"

  - name: "memory-fetch"
    id: "mcp_ai_smithery_l_fetch"
    use: "Recuperar análisis completos de memoria"
```

#### MCPs de Investigación
```yaml
research_mcps:
  - name: "perplexity-research"
    id: "mcp_docker_mcp_ga_perplexity_research"
    use: "Investigar mejores prácticas de versionado multi-layer"

  - name: "brave-search"
    id: "activate_brave_search_tools"
    use: "Buscar papers sobre coherence in multi-modal knowledge bases"

  - name: "context7"
    id: "activate_library_documentation_tools"
    use: "Documentación de Neo4j, Chroma, Git workflows"
```

#### MCPs de Gestión de Documentos
```yaml
document_mcps:
  - name: "filesystem"
    id: "activate_directory_and_file_creation_tools"
    use: "Crear estructura del nuevo template"

  - name: "git"
    id: "activate_git_branch_management_tools"
    use: "Diseñar git workflow con épicas"
```

---

## 📋 Tareas del Agente (Desglose Estructurado)

### Task 1: Analizar Templates Actuales
**Thinking**: Sequential thoughts 1-5

```
🎭 Role: Arquitecto de Templates

📋 Context:
- Existen dos templates: research-methodology-template y app-spec-template
- Ambos comparten fases iniciales (MELQUISEDEC, HYPATIA, SALOMON)
- Divergen después de SALOMON según tipo de artefacto

🎯 Task:
Analizar ambos templates y extraer:
1. Elementos comunes a unificar
2. Puntos de divergencia
3. Estructura de carpetas común
4. Tareas compartidas vs específicas

🔍 Tools:
- activate_directory_and_file_creation_tools
- mcp_filesystem_read_multiple_files
- mcp_sequential-th_sequentialthinking

📤 Output:
Documento markdown con análisis comparativo
```

---

### Task 2: Diseñar Arquitectura Unificada
**Thinking**: Sequential thoughts 6-12 + Smart-thinking branches

```
🎭 Role: Arquitecto de Sistemas

📋 Context:
- Análisis de Task 1 completado
- Necesidad de workflow divergente post-SALOMON
- Tipos de artefactos: research | app | social-project

🎯 Task:
Diseñar la arquitectura del Unified Template:

1. Estructura de carpetas unificada
2. config.yaml parametrizable con:
   - artifact_type: [research, app, social]
   - versioning_strategy
   - persistence_layers
3. Tasks matrix: común vs específico por tipo
4. Checkpoints unificados

🔍 Tools:
- mcp_sequential-th_sequentialthinking (thoughts 6-12)
- mcp_ai_smithery_l_smartthinking (para branches de alternativas)
- mcp_maxential-thi_branch (comparar opciones de estructura)

📤 Output:
- unified-template-architecture.md
- config.yaml.template
- tasks-matrix.yaml
```

---

### Task 3: Diseñar Sistema de Épicas y Versionado
**Thinking**: Sequential thoughts 13-18 + Perplexity research

```
🎭 Role: Ingeniero de Configuración

📋 Context:
- Necesidad de versionar documentos, grafo y vectores coherentemente
- Épicas representan ciclos de investigación (ej: "fundacion")
- Al cerrar épica → archivar con versión semántica
- Lessons learned pueden abrir nueva épica con nueva versión

🎯 Task:
Diseñar el sistema de gestión de épicas:

1. Estructura de metadatos en ISSUE.yaml:
   ```yaml
   versioning:
     current_version: "v1.0.0"
     current_epic: "fundacion"
     epic_status: "active" | "closed" | "archived"
     version_history: []
   ```

2. Workflow de archivado:
   - Trigger: Epic closed
   - Actions:
     * git tag v{version}
     * Move all docs to archive/
     * Tag Neo4j nodes
     * Archive vector collection

3. Workflow de nueva épica:
   - Trigger: Lessons learned with gaps
   - Actions:
     * Clean spec-issue (keep structure)
     * Increment version (patch/minor/major)
     * Create new epic name
     * Reset task checkboxes

4. Rollback strategy:
   - git revert to version tag
   - neo4j restore snapshot
   - vector restore backup

🔍 Tools:
- mcp_sequential-th_sequentialthinking (thoughts 13-18)
- mcp_docker_mcp_ga_perplexity_research:
  query: "best practices versioning knowledge bases multi-layer persistence"

📤 Output:
- epic-versioning-design.md
- rollback-procedures.md
- ISSUE.yaml.v2-template (con campos de versioning)
```

---

### Task 4: Diseñar Triple Persistencia Coherente
**Thinking**: Sequential thoughts 19-25 + Branch exploration

```
🎭 Role: Arquitecto de Datos

📋 Context:
- Tres capas de persistencia: Markdown (filesystem), Graph (Neo4j), Vector (TBD)
- Deben estar sincronizadas y versionadas coherentemente
- Riesgo: Perder coherencia entre capas muy rápidamente

🎯 Task:
Investigar y diseñar estrategia de coherencia:

1. **Investigación de mejores prácticas**:
   - Use perplexity_research: "multi-modal knowledge base coherence strategies"
   - Use brave_search: papers sobre "knowledge graph vector store synchronization"
   - Use context7: Neo4j + Chroma/Qdrant documentation

2. **Diseñar sincronización**:

   a) Estrategia 1: UUID-based linking
   ```yaml
   atomic_concept:
     uuid: "550e8400-e29b-41d4-a716-446655440000"
     markdown_path: "02-atomics/ATOM-001-design-science.md"
     neo4j_node_id: 12345
     vector_id: "550e8400-..."
     version: "v1.0.0"
     epic: "fundacion"
   ```

   b) Estrategia 2: Event-driven sync
   ```python
   # Pseudo-workflow
   def create_atomic_concept(content):
       uuid = generate_uuid()

       # 1. Write markdown
       md_path = write_markdown(content, uuid)

       # 2. Create graph node
       node_id = neo4j.create_node({
           "label": "Concept",
           "uuid": uuid,
           "md_path": md_path,
           "version": current_version,
           "epic": current_epic
       })

       # 3. Generate embedding
       embedding = generate_embedding(content)
       vector_id = vector_store.add(
           embedding=embedding,
           metadata={
               "uuid": uuid,
               "version": current_version,
               "epic": current_epic
           }
       )

       # 4. Store mapping
       mapping_store.save({
           "uuid": uuid,
           "md": md_path,
           "graph": node_id,
           "vector": vector_id
       })
   ```

   c) Estrategia 3: Snapshot-based archival
   ```bash
   # Al cerrar épica
   git tag v1.0.0
   neo4j-admin backup --to=archive/graph-v1.0.0/
   vector-cli export atomics_v1.0.0 --format parquet
   ```

3. **Validar coherencia**:
   ```python
   def validate_coherence():
       # Check all UUIDs exist in all three layers
       for concept in get_all_concepts():
           assert filesystem.exists(concept.md_path)
           assert neo4j.node_exists(concept.uuid)
           assert vector_store.has_embedding(concept.uuid)
   ```

🔍 Tools:
- mcp_sequential-th_sequentialthinking (thoughts 19-25)
- mcp_maxential-thi_branch:
  - Branch 1: UUID linking strategy
  - Branch 2: Event-driven sync strategy
  - Branch 3: Snapshot-based archival
  - Merge: Best hybrid approach
- mcp_docker_mcp_ga_perplexity_research
- activate_brave_search_tools
- activate_library_documentation_tools (Neo4j, Chroma)

📤 Output:
- triple-persistence-architecture.md
- coherence-validation-script.py
- sync-workflows.md
```

---

### Task 5: Integrar Git Workflow y Context Management
**Thinking**: Sequential thoughts 26-30

```
🎭 Role: Ingeniero DevOps

📋 Context:
- Cada task debe hacer commit al finalizar
- Cada checkpoint debe ser un tag git
- Al cerrar épica → push con version tag
- Rollback debe ser seguro en todas las capas

🎯 Task:
Diseñar integración Git + Context Management:

1. **Per-task workflow**:
   ```bash
   # Al iniciar task
   git checkout -b task-{id}-{name}
   mcp_memory store context "Starting task {id}"

   # Durante task
   # ... work ...

   # Al completar task
   git add .
   git commit -m "feat(task-{id}): {description}"
   git tag task-{id}-complete
   mcp_memory store context "Completed task {id}"
   git checkout main
   git merge task-{id}-{name}
   ```

2. **Per-checkpoint workflow**:
   ```bash
   # Al llegar a checkpoint
   mcp_memory store context "Checkpoint {CK-ID} reached"
   git tag checkpoint-{CK-ID}

   # Si checkpoint fails
   git reset --hard checkpoint-{previous-CK-ID}
   neo4j restore snapshot-{previous-CK-ID}
   vector restore snapshot-{previous-CK-ID}
   ```

3. **Per-epic workflow**:
   ```bash
   # Al cerrar épica
   git add .
   git commit -m "chore(epic-{name}): close v{version}"
   git tag v{version}

   # Archive
   bash scripts/archive-epic.sh v{version}

   # Push
   git push origin main --tags
   ```

4. **Rollback procedures**:
   ```bash
   # Rollback to previous version
   bash scripts/rollback-to-version.sh v1.0.0

   # Inside script:
   # - git reset --hard v1.0.0
   # - neo4j-admin restore --from=archive/graph-v1.0.0/
   # - vector-cli import archive/vectors-v1.0.0.parquet
   ```

🔍 Tools:
- mcp_sequential-th_sequentialthinking (thoughts 26-30)
- activate_git_branch_management_tools
- mcp_memory (para context management)

📤 Output:
- git-workflow-integration.md
- scripts/archive-epic.sh
- scripts/rollback-to-version.sh
```

---

### Task 6: Validar Diseño y Mitigación de Riesgos
**Thinking**: Final thoughts + Branch merge

```
🎭 Role: Arquitecto Revisor

📋 Context:
- Diseño completo de Tasks 1-5
- Necesidad de validar coherencia del diseño completo
- Identificar riesgos y proponer mitigaciones

🎯 Task:
Revisar todo el diseño y crear:

1. **Matriz de validación**:
   | Componente | Requirement | Cumple | Riesgos | Mitigación |
   |------------|-------------|---------|---------|------------|
   | Unificación | Un solo template | ✅ | Complejidad | Docs claros |
   | Versionado | Épicas + semver | ✅ | Olvido de tag | Automation |
   | Triple persist | MD+Graph+Vector | ✅ | Desincronización | UUID + validation |
   | Git workflow | Commits + rollback | ✅ | Errores humanos | Scripts |

2. **Análisis de riesgos**:
   - Riesgo 1: Pérdida de coherencia entre capas
     * Probabilidad: Alta
     * Impacto: Crítico
     * Mitigación: Validation scripts automáticos

   - Riesgo 2: Confusión en versionado semántico
     * Probabilidad: Media
     * Impacto: Medio
     * Mitigación: Guidelines claros, automation

   - Riesgo 3: Rollback incompleto
     * Probabilidad: Media
     * Impacto: Alto
     * Mitigación: Snapshots automáticos, testing

3. **Recomendaciones finales**:
   - Implementar validation scripts ANTES de producción
   - Crear tutorial step-by-step para usar el template
   - Establecer CI/CD para validación continua

🔍 Tools:
- mcp_sequential-th_sequentialthinking (final thoughts)
- mcp_maxential-thi_merge_branch (consolidar análisis)
- mcp_ai_smithery_l_smartthinking (synthesize final recommendations)

📤 Output:
- design-validation-report.md
- risk-mitigation-plan.md
- implementation-roadmap.md
```

---

## 📤 Outputs Esperados del Agente

Al completar todas las tasks, el agente debe generar:

### Documentos de Diseño
1. `unified-template-architecture.md` - Arquitectura completa del template unificado
2. `epic-versioning-design.md` - Sistema de épicas y versionado
3. `triple-persistence-architecture.md` - Estrategia de coherencia MD+Graph+Vector
4. `git-workflow-integration.md` - Integración Git + Context Management
5. `design-validation-report.md` - Validación y riesgos

### Artefactos Ejecutables
1. `config.yaml.v2-template` - Template de configuración con versionado
2. `ISSUE.yaml.v2-template` - Template de issue con metadatos de épicas
3. `scripts/archive-epic.sh` - Script de archivado automático
4. `scripts/rollback-to-version.sh` - Script de rollback multi-capa
5. `scripts/validate-coherence.py` - Script de validación de coherencia

### Templates Estructurales
1. `unified-research-template/` - Carpeta del nuevo template con:
   - `README.md` - Documentación del template
   - `requirements.md` - Requirements del template
   - `design.md` - Diseño del template
   - `tasks.md` - Tasks matrix unificada
   - `_meta/orchestrator.md` - Orquestador con workflows divergentes

### Documentación de Implementación
1. `implementation-roadmap.md` - Roadmap de implementación
2. `migration-guide.md` - Guía de migración desde templates viejos
3. `user-tutorial.md` - Tutorial paso a paso para usar el template

---

## 🔄 Workflow de Ejecución para el Agente

### Fase 1: Setup
```bash
# Activar MCPs necesarios
activate_directory_and_file_creation_tools
activate_git_branch_management_tools
mcp_sequential-th_sequentialthinking (start session)
```

### Fase 2: Análisis (Tasks 1-2)
```
Sequential thinking: thoughts 1-12
- Analizar templates actuales
- Diseñar arquitectura unificada
Smart-thinking: branches para alternativas de estructura
```

### Fase 3: Versionado (Task 3)
```
Sequential thinking: thoughts 13-18
Perplexity research: "versioning strategies knowledge bases"
Brave search: papers on multi-layer versioning
```

### Fase 4: Persistencia (Task 4)
```
Sequential thinking: thoughts 19-25
Maxential branches:
  - Branch 1: UUID linking
  - Branch 2: Event-driven sync
  - Branch 3: Snapshot archival
  - Merge: Hybrid approach
Perplexity research: "knowledge graph vector coherence"
Context7: Neo4j + Chroma documentation
```

### Fase 5: Git Integration (Task 5)
```
Sequential thinking: thoughts 26-30
Create scripts for:
  - archive-epic.sh
  - rollback-to-version.sh
```

### Fase 6: Validation (Task 6)
```
Final thoughts + synthesis
Merge all branches
Generate final recommendations
```

### Fase 7: Documentation
```
Aggregate all outputs
Create unified documentation structure
Write implementation roadmap
```

---

## ⚠️ Restricciones y Consideraciones

### Límites de Respuesta del Agente
Para evitar exceder límites de respuesta:

1. **Dividir en sub-prompts**: Si el agente llega a límite, dividir en prompts más pequeños:
   - Prompt 1: Tasks 1-2 (análisis + arquitectura)
   - Prompt 2: Task 3 (versionado)
   - Prompt 3: Task 4 (persistencia)
   - Prompt 4: Tasks 5-6 (git + validación)

2. **Usar archivos incrementales**: No generar todo en una respuesta, escribir archivos progresivamente

3. **Resúmenes intermedios**: Al completar cada task, generar resumen antes de continuar

### Priorización
Si recursos limitados, priorizar:
1. ✅ **Must have**: Arquitectura unificada + versionado básico
2. ⚠️ **Should have**: Triple persistencia con UUID linking
3. 💡 **Nice to have**: Rollback automático multi-capa

### Validación Continua
Después de cada task:
- Escribir output a filesystem
- Validar que el diseño es coherente con lo anterior
- Documentar decisiones arquitectónicas (ADRs)

---

## 📞 Soporte y Referencias

### Documentos de Referencia en el Workspace
- `.spec-workflow/_meta/templates/research-methodology-template/`
- `.spec-workflow/_meta/templates/app-spec-template/`
- `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md`
- `docs/architecture/ADR-001-monorepo-structure.md`

### MCPs Disponibles en el Sistema
- Sequential Thinking: `mcp_sequential-th_sequentialthinking`
- Smart Thinking: `mcp_ai_smithery_l_smartthinking`
- Maxential Thinking: `mcp_maxential-thi_branch`, `mcp_maxential-thi_merge_branch`
- Perplexity: `mcp_docker_mcp_ga_perplexity_research`
- Memory: `mcp_ai_smithery_l_search`, `mcp_ai_smithery_l_fetch`
- Brave Search: `activate_brave_search_tools`
- Context7: `activate_library_documentation_tools`
- Filesystem: `activate_directory_and_file_creation_tools`
- Git: `activate_git_branch_management_tools`

---

## 🎬 Prompt de Ejecución Final

```
🎭 Role: Senior Software Architect + Research Methodologist

📋 Context:
Has leído este documento completo: unified-research-template-design-2026-01-09.md
Entiendes el problema: unificar dos templates con workflows divergentes post-SALOMON
Conoces los requerimientos: épicas, versionado, triple persistencia, git workflow, rollback

🎯 Mission:
Ejecutar las 6 tasks descritas arriba usando pensamiento complejo (sequential-thinking)
para diseñar la arquitectura completa del Unified Research Template.

🔍 Methodology:
1. Activate sequential-thinking con estimación de 30 thoughts
2. Ejecutar Tasks 1-6 en orden
3. Usar branches (maxential/smart-thinking) cuando haya alternativas
4. Investigar con perplexity/brave cuando necesites best practices
5. Escribir outputs incrementalmente a filesystem
6. Validar coherencia del diseño continuamente

⚡ Start Command:
Ejecuta Task 1: Analizar Templates Actuales
Usa mcp_sequential-th_sequentialthinking con thought 1/30
```

---

**End of Prompt**

---

## 🗂️ Metadata del Prompt

```yaml
prompt:
  id: "unified-research-template-design"
  version: "1.0.0"
  created: "2026-01-09"
  purpose: "Diseño arquitectónico de template unificado con versionado"

  complexity:
    level: "high"
    estimated_thoughts: 30
    estimated_time: "2-3 hours"

  mcps_required:
    thinking:
      - sequential-thinking
      - smart-thinking
      - maxential-thinking
    research:
      - perplexity
      - brave-search
      - context7
    memory:
      - memory-search
      - memory-fetch
    management:
      - filesystem
      - git

  outputs:
    documents: 8
    scripts: 3
    templates: 5
    total_artifacts: 16

  success_criteria:
    - "Arquitectura unificada diseñada"
    - "Sistema de versionado con épicas definido"
    - "Estrategia de triple persistencia documentada"
    - "Scripts de archivado y rollback creados"
    - "Validación de coherencia implementada"
    - "Roadmap de implementación generado"
```
