# Orquestador: Research Methodology - {{research.full_name}}

```yaml
---
id: "research-methodology-{{research.name}}-orchestrator"
title: "Orquestador: Research {{research.full_name}}"
version: "{{research.version}}"
created: "{{research.created}}"
owners: ["MELQUISEDEC"]
rostros: ["MELQUISEDEC", "HYPATIA", "SALOMON", "MORPHEUS", "ALMA"]
required_mcps:
  base: ["neo4j", "memory", "filesystem"]
  specialized: ["brave-search", "arxiv", "context7", "perplexity"]
checkpoints:
  - id: "ck-01-literature"
    rostro: "HYPATIA"
    require_approval: true
  - id: "ck-02-analysis"
    rostro: "SALOMON"
    require_approval: true
  - id: "ck-03-artifacts"
    rostro: "MORPHEUS"
    require_approval: false
  - id: "ck-04-execution"
    rostro: "ALMA"
    require_approval: true
config_file: "./config.yaml"
output_path: "../../apps/research-{{research.name}}/"
---
```

---

## 🎯 Propósito

Este orchestrator automatiza la ejecución del workflow de investigación metodológica siguiendo la cascada de rostros DAATH-ZEN. Lee configuración desde `config.yaml` y ejecuta tasks.md secuencialmente.

---

## 📋 Pre-requisitos

### 1. Configuración Inicial

```powershell
# 1. Verificar estructura spec-workflow
Test-Path ".spec-workflow/specs/research-methodology-{{research.name}}"

# 2. Validar config.yaml
$config = Get-Content ".spec-workflow/specs/research-methodology-{{research.name}}/config.yaml" | ConvertFrom-Yaml

# 3. Verificar MCPs disponibles
# - neo4j: Para graph database
# - memory: Para context management
# - filesystem: Para file operations
# - brave-search, arxiv, context7, perplexity: Para research

# 4. Verificar Neo4j running (si aplica)
docker ps | Select-String "neo4j"
```

### 2. Steering Documents

**Cargar contexto inicial**:
- Product: `.spec-workflow/steering/product.md`
- Tech: `.spec-workflow/steering/tech.md`
- Principios MELQUISEDEC: `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md`

---

## 🔄 Workflow de Ejecución

### FASE 0: MELQUISEDEC - Inicialización

#### Task 0.1: Crear estructura

**Comando PowerShell**:
```powershell
# Leer configuración
$config = Get-Content ".\.spec-workflow\specs\research-methodology-{{research.name}}\config.yaml" | ConvertFrom-Yaml

# Variables
$researchPath = ".\apps\research-$($config.research.name)"
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

# Crear carpetas según config.yaml
Write-Host "🔧 Creando estructura de investigación..." -ForegroundColor Cyan
foreach ($folder in $config.outputs.structure) {
    $folderPath = Join-Path $researchPath $folder
    New-Item -ItemType Directory -Force -Path $folderPath | Out-Null
    Write-Host "✅ Created: $folder" -ForegroundColor Green
}

# Crear ISSUE.yaml
$issueYaml = @"
---
id: 'research-$($config.research.name)'
is_a: 'research/methodology'
version: '$($config.research.version)'

# DUBLIN CORE
dc:
  title: 'Research: $($config.research.full_name)'
  creator: ['$($config.research.owner)']
  date: '$(Get-Date -Format "yyyy-MM-dd")'
  subject: $($config.scope.domains | ConvertTo-Json -Compress)
  description: 'Investigación formal de $($config.research.full_name)'
  type: '$($config.research.type)'

# MELQUISEDEC WORKFLOW
melquisedec:
  estado: 'in-progress'
  cascada_actual: 'MELQUISEDEC'
  rostros: $($config.rostros.name | ConvertTo-Json -Compress)
  checkpoints: $($config.checkpoints.id | ConvertTo-Json -Compress)

# HKM
hkm:
  permalink: '$researchPath'
  version: '$($config.research.version)'
---
"@

$issueYaml | Out-File "$researchPath\ISSUE.yaml" -Encoding UTF8

# Crear README.md inicial
$readmeContent = @"
# Research: $($config.research.full_name)

> **Research Instance**: RI-$($config.research.name.ToUpper())
> **Type**: $($config.research.type)
> **Status**: 🟡 In Progress
> **Owner**: $($config.research.owner)
> **Started**: $(Get-Date -Format "yyyy-MM-dd")

## 🎯 Objetivo

Investigación formal de **$($config.research.full_name)** para:
1. Comprender fundamentos y artefactos
2. Extraer conocimiento atómico trazable
3. Identificar frameworks canónicos
4. Generar artefactos ejecutables
5. Adoptar mejores prácticas en MELQUISEDEC

## 🔬 Research Questions

$($config.scope.research_questions | ForEach-Object { "- $_" } | Out-String)

## 📂 Estructura

\`\`\`
$($config.outputs.structure | ForEach-Object { "- $_" } | Out-String)
\`\`\`

## 🔄 Workflow (DAATH-ZEN)

- [ ] MELQUISEDEC: Inicialización
- [ ] HYPATIA: Literature Review + Atomization
- [ ] SALOMON: Analysis + Synthesis
- [ ] MORPHEUS: Artifacts + Scripts
- [ ] ALMA: Execution + Validation

## 📊 Progress

- **Phase**: Initialization
- **Rostro activo**: MELQUISEDEC
- **Tasks completed**: 0/27

---

**Última actualización**: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
"@

$readmeContent | Out-File "$researchPath\README.md" -Encoding UTF8

Write-Host "`n✅ Estructura inicializada exitosamente" -ForegroundColor Green
Write-Host "📁 Location: $researchPath" -ForegroundColor Cyan
```

**Post-ejecución**:
```powershell
# Log de implementación
$logContent = @"
# Implementation Log: Task 0.1 - Initialize Structure

**Timestamp**: $timestamp
**Task**: 0.1 - Crear estructura de investigación
**Rostro**: MELQUISEDEC
**Status**: ✅ Completed

## Actions Performed
- Created folder structure: $($config.outputs.structure -join ', ')
- Created ISSUE.yaml with HKM + Dublin Core metadata
- Created initial README.md

## Artifacts Generated
- \`apps/research-$($config.research.name)/\`
- \`apps/research-$($config.research.name)/ISSUE.yaml\`
- \`apps/research-$($config.research.name)/README.md\`

## Next Steps
- Task 1.1: HYPATIA - Identificar fuentes canónicas

---
**Log created**: $timestamp
"@

New-Item -ItemType Directory -Force -Path ".\.spec-workflow\specs\research-methodology-{{research.name}}\Implementation Logs" | Out-Null
$logContent | Out-File ".\.spec-workflow\specs\research-methodology-{{research.name}}\Implementation Logs\task-0.1-init-structure.md" -Encoding UTF8

# Commit cambios
git add "apps/research-$($config.research.name)"
git add ".spec-workflow/specs/research-methodology-{{research.name}}/Implementation Logs/task-0.1-init-structure.md"
git commit -m "chore(research-$($config.research.name)): Initialize research structure

- Created folder structure following config.yaml
- Added ISSUE.yaml with metadata
- Added initial README.md

Task: 0.1
Rostro: MELQUISEDEC"
```

---

### FASE 1: HYPATIA - Literature Review

#### Task 1.1: Identificar fuentes

**Prompt para Copilot**:
```
🎭 Role: HYPATIA (Investigadora)

📋 Context:
- Research: {{research.full_name}} ({{research.name}})
- Config: .spec-workflow/specs/research-methodology-{{research.name}}/config.yaml
- RQs: {{scope.research_questions}}
- Domains: {{scope.domains}}
- Quality requirements:
  * Min sources: {{quality.metrics.min_sources}}
  * Min peer-reviewed: {{quality.metrics.min_peer_reviewed}}

🎯 Task:
Buscar y documentar fuentes canónicas sobre {{research.full_name}} usando MCP tools.

🔍 Search Strategy:
1. Use `mcp_docker_mcp_ga_search_papers` (arXiv) para papers académicos:
   - Query: "{{research.full_name}}"
   - Categories: ["cs.AI", "cs.SE"] (adjust según domains)
   - Max results: 20
   - Sort by: relevance

2. Use `activate_brave_search_tools` + `brave_search` para resources web:
   - Query: "{{research.full_name}} best practices"
   - Query: "{{research.full_name}} frameworks"

3. Use `mcp_context7_resolve-library-id` + `get-library-docs` para docs técnicas:
   - Library name: [framework name if known]

4. Use `mcp_apify_search-actors` si se necesita scraping de sitios específicos

📝 Output:
File: apps/research-{{research.name}}/01-literature/sources.yaml

Format:
```yaml
sources:
  papers:
    - id: "paper-001"
      title: "..."
      authors: ["Author A", "Author B"]
      year: 2024
      doi: "10.1234/..."
      arxiv_id: "2401.12345"
      url: "https://arxiv.org/abs/2401.12345"
      quality: "peer-reviewed"
      relevance: "high"  # high | medium | low

  frameworks:
    - id: "framework-001"
      name: "Framework Name"
      url: "https://github.com/org/repo"
      stars: 5000
      maintained: true
      last_update: "2024-01-01"
      relevance: "high"

  web_resources:
    - id: "resource-001"
      title: "..."
      url: "https://..."
      type: "blog" | "documentation" | "tutorial"
      relevance: "medium"
```

🚫 Restrictions:
- NO usar fuentes no verificadas (blogs personales sin autoridad)
- Priorizar fuentes recientes (últimos 5 años para papers)
- Verificar disponibilidad de contenido completo
- NO duplicar fuentes (verificar IDs únicos)

✅ Success Criteria:
- ≥{{quality.metrics.min_sources}} fuentes documentadas
- ≥{{quality.metrics.min_peer_reviewed}} fuentes peer-reviewed
- Metadata completa por fuente
- URLs/DOIs verificados y accesibles
- sources.yaml válido (YAML lint pass)

💡 Tips:
- Si encuentras surveys o systematic reviews, priorízalos (alto valor)
- Busca frameworks con >1000 stars en GitHub
- Verifica que papers tengan DOI (indica peer-review)
```

**Validación post-ejecución**:
```powershell
# Verificar sources.yaml existe y es válido
$sourcesPath = ".\apps\research-$($config.research.name)\01-literature\sources.yaml"

if (Test-Path $sourcesPath) {
    $sources = Get-Content $sourcesPath | ConvertFrom-Yaml

    $paperCount = $sources.sources.papers.Count
    $frameworkCount = $sources.sources.frameworks.Count
    $totalSources = $paperCount + $frameworkCount

    $peerReviewedCount = ($sources.sources.papers | Where-Object { $_.quality -eq "peer-reviewed" }).Count

    Write-Host "`n📊 Sources Validation:" -ForegroundColor Cyan
    Write-Host "  Total sources: $totalSources (required: $($config.quality.metrics.min_sources))" -ForegroundColor $(if ($totalSources -ge $config.quality.metrics.min_sources) { "Green" } else { "Red" })
    Write-Host "  Peer-reviewed: $peerReviewedCount (required: $($config.quality.metrics.min_peer_reviewed))" -ForegroundColor $(if ($peerReviewedCount -ge $config.quality.metrics.min_peer_reviewed) { "Green" } else { "Red" })

    if ($totalSources -ge $config.quality.metrics.min_sources -and $peerReviewedCount -ge $config.quality.metrics.min_peer_reviewed) {
        Write-Host "`n✅ Task 1.1 PASS" -ForegroundColor Green
    } else {
        Write-Host "`n❌ Task 1.1 FAIL - Insuficientes fuentes" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "`n❌ Task 1.1 FAIL - sources.yaml no encontrado" -ForegroundColor Red
    exit 1
}
```

#### Tasks 1.2-1.6: Similar structure...

_[Por brevedad, los prompts de tasks 1.2-1.6 siguen el mismo patrón documentado en tasks.md]_

#### Checkpoint CK-01: HYPATIA Validation

```powershell
# Ejecutar validación automática
$checkpointScript = @"
# Checkpoint CK-01: HYPATIA Validation

`$researchPath = ".\apps\research-$($config.research.name)"

# 1. Count sources
`$sources = Get-Content "`$researchPath\01-literature\sources.yaml" | ConvertFrom-Yaml
`$sourcesCount = (`$sources.sources.papers.Count + `$sources.sources.frameworks.Count)

# 2. Count atomics
`$atomicsCount = (Get-ChildItem "`$researchPath\02-atomics\concepts" -Filter "*.md").Count

# 3. Verify relationships.yaml
`$relationshipsExist = Test-Path "`$researchPath\02-atomics\relationships.yaml"

# 4. Verify graph-ready
`$graphReadyExist = (Test-Path "`$researchPath\02-atomics\graph-ready\nodes.yaml") -and (Test-Path "`$researchPath\02-atomics\graph-ready\relationships.yaml")

# Determine status
`$status = "pass"
if (`$sourcesCount -lt $($config.checkpoints[0].criteria.min_sources)) { `$status = "fail" }
if (`$atomicsCount -lt $($config.checkpoints[0].criteria.min_atomics)) { `$status = "fail" }
if (-not `$relationshipsExist) { `$status = "fail" }

# Create validation file
`$validationYaml = @"
---
checkpoint: 'ck-01-literature'
rostro: 'HYPATIA'
phase: '01-literature'
date: '`$(Get-Date -Format "yyyy-MM-dd")'
timestamp: '`$(Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")'
status: '`$status'

criteria:
  min_sources: $($config.checkpoints[0].criteria.min_sources)
  actual_sources: `$sourcesCount
  min_atomics: $($config.checkpoints[0].criteria.min_atomics)
  actual_atomics: `$atomicsCount
  relationships_documented: `$relationshipsExist
  graph_ready_generated: `$graphReadyExist

approval:
  required: $($config.checkpoints[0].require_approval.ToString().ToLower())
  approved_by: null
  approved_at: null

notes: |
  Validation executed automatically.
  Sources: `$sourcesCount (papers + frameworks)
  Atomics: `$atomicsCount concepts extracted
  Relationships: `$(if (`$relationshipsExist) { 'Documented' } else { 'Missing' })
  Graph-ready: `$(if (`$graphReadyExist) { 'Generated' } else { 'Missing' })

next_steps: |
  $(if (`$status -eq "pass") {
    if ($($config.checkpoints[0].require_approval)) {
      "✅ Validation PASS. Awaiting manual approval before proceeding to SALOMON phase."
    } else {
      "✅ Validation PASS. Proceeding to SALOMON phase (Analysis)."
    }
  } else {
    "❌ Validation FAIL. Fix issues before proceeding."
  })
---
"@

`$validationYaml | Out-File "`$researchPath\.melquisedec\hypatia_validation.yaml" -Encoding UTF8

Write-Host "`n📋 Checkpoint CK-01 Result: `$status" -ForegroundColor `$(if (`$status -eq "pass") { "Green" } else { "Red" })
"@

Invoke-Expression $checkpointScript

# Si require_approval=true, pausar
if ($config.checkpoints[0].require_approval -and $status -eq "pass") {
    Write-Host "`n⏸️  Checkpoint CK-01 requires manual approval" -ForegroundColor Yellow
    Write-Host "Review: apps/research-$($config.research.name)/.melquisedec/hypatia_validation.yaml" -ForegroundColor Cyan
    Write-Host "`nTo approve and continue, run:" -ForegroundColor Cyan
    Write-Host "  # Update approved_by and approved_at fields" -ForegroundColor Gray
    Write-Host "  # Then re-run orchestrator" -ForegroundColor Gray
    exit 0
}
```

---

### FASE 2-4: SALOMON, MORPHEUS, ALMA

_[Estructura similar, usando prompts de tasks.md y validaciones automáticas]_

---

### FASE 5: Lessons Learned

#### Task 5.1-5.3: Documentar y mejorar

```powershell
# Agregar lecciones
$lessonsPath = ".\apps\research-$($config.research.name)\06-lessons"

# Generar summary.yaml
$summaryYaml = @"
---
summary:
  research: '$($config.research.name)'
  total_lessons: [count]
  categories:
    - what_worked
    - challenges
    - improvements

lessons:
  hypatia:
    what_worked: [extract from hypatia-lessons.md]
    challenges: [extract]
    recommendations: [extract]

  salomon:
    what_worked: [extract]
    challenges: [extract]
    recommendations: [extract]

  morpheus:
    what_worked: [extract]
    challenges: [extract]
    recommendations: [extract]

  alma:
    what_worked: [extract]
    challenges: [extract]
    recommendations: [extract]

improvements_for_v2:
  - "Improvement 1"
  - "Improvement 2"
---
"@

$summaryYaml | Out-File "$lessonsPath\summary.yaml" -Encoding UTF8
```

---

## 📊 Execution Monitoring

### Progress Dashboard

```powershell
function Show-ResearchProgress {
    param($ConfigPath)

    $config = Get-Content $ConfigPath | ConvertFrom-Yaml
    $researchPath = ".\apps\research-$($config.research.name)"

    Write-Host "`n" -NoNewline
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host " Research Progress: $($config.research.full_name)" -ForegroundColor White
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan

    # Check cada fase
    $phases = @(
        @{ Name = "Init (MELQUISEDEC)"; File = "$researchPath\ISSUE.yaml"; Icon = "🔧" }
        @{ Name = "Literature (HYPATIA)"; File = "$researchPath\.melquisedec\hypatia_validation.yaml"; Icon = "📚" }
        @{ Name = "Analysis (SALOMON)"; File = "$researchPath\.melquisedec\salomon_validation.yaml"; Icon = "🧠" }
        @{ Name = "Artifacts (MORPHEUS)"; File = "$researchPath\.melquisedec\morpheus_validation.yaml"; Icon = "⚙️" }
        @{ Name = "Execution (ALMA)"; File = "$researchPath\.melquisedec\alma_validation.yaml"; Icon = "🚀" }
    )

    foreach ($phase in $phases) {
        $status = if (Test-Path $phase.File) { "✅" } else { "⏳" }
        Write-Host "$($phase.Icon) $($phase.Name): $status" -ForegroundColor $(if ($status -eq "✅") { "Green" } else { "Yellow" })
    }

    Write-Host "═══════════════════════════════════════════════════════════`n" -ForegroundColor Cyan
}

# Usage
Show-ResearchProgress -ConfigPath ".\.spec-workflow\specs\research-methodology-{{research.name}}\config.yaml"
```

---

## 🚀 Quick Start

### Option 1: Ejecución Manual (Task by Task)

```powershell
# 1. Inicializar
# [Ejecutar comandos de Task 0.1]

# 2. HYPATIA - Literatura
# [Usar prompt de Task 1.1 con Copilot]
# [Validar resultados]
# [Continuar con Tasks 1.2-1.6]

# 3. Checkpoint CK-01
# [Ejecutar validación]
# [Si require_approval, esperar aprobación]

# 4. SALOMON - Análisis
# [Tasks 2.1-2.5]

# ... y así sucesivamente
```

### Option 2: Semi-automatizado (Con Copilot Agents)

```powershell
# TODO: Implementar agente que lea tasks.md y ejecute secuencialmente
# usando manage_todo_list tool para tracking
```

---

## 📚 Referencias

- **Config**: `./config.yaml`
- **Requirements**: `./requirements.md`
- **Design**: `./design.md`
- **Tasks**: `./tasks.md`
- **Principios MELQUISEDEC**: `docs/manifiesto/01-fundamentos/04-principios-fundacionales.md`

---

**Document Version**: {{research.version}}
**Last Updated**: {{research.created}}
**Maintainer**: MELQUISEDEC
