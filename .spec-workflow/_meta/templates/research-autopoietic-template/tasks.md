# Tasks

<!-- HKM Metadata -->
---
hkm_type: workbook
epistemic_level: workbook
title: "Tasks - [TÍTULO_ÉPICA]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tasks, research, daath-zen, autopoietic]
synthesis_from:
  - requirements.md
  - design.md
---

> **Template**: DAATH-ZEN Advanced (archive/_templates/tasks.md - 95% coherence)
> **Workflow**: Divergente según `type` en ISSUE.yaml (research/app/social-project)
> **Autopoiesis**: Activar smart-thinking, sequential-thinking según fase

---

## PHASE 1: MELQUISEDEC (Problema)

> **Rostro**: MELQUISEDEC (Definición del Problema)
> **Checkpoint**: CK-01
> **MCPs Preferidos**: sequential-thinking (análisis estructurado), filesystem, grep-search
> **Output**: requirements.md completo, problem-statement.md validado

---

### [x] M1.1. Definir problem statement y success criteria

- **File**: `00-problem/problem-statement.md`
- **Requirements**: requirements.md § 1.1
- **Rostro**: MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[sequential-thinking]`
- **Lesson**: `06-lessons/m1.1-problem-definition.md`
- **Prompt**:
  ```
  Role: MELQUISEDEC Problem Definer
  Task: Analizar contexto del usuario, identificar problema central, formular pregunta de investigación específica, definir 3-5 success criteria medibles
  Restrictions: Problema debe ser específico (no vago), medible (con métricas), alineado con objetivos del monorepo
  Success: problem-statement.md con problema claro, pregunta de investigación SMART, success criteria validables
  ```
- **Context**: [Descripción del contexto específico de este problema]
- **Status**: Completed

---

### [ ] M1.2. Identificar stakeholders y roles

- **File**: `00-problem/stakeholders.md`
- **Requirements**: requirements.md § 6
- **Rostro**: MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[grep-search]`
- **Lesson**: `06-lessons/m1.2-stakeholders.md`
- **Prompt**:
  ```
  Role: MELQUISEDEC Problem Definer
  Task: Identificar stakeholders (Investigador Principal, Colaboradores, Revisores), asignar rostros DAATH-ZEN (MELQUISEDEC, HYPATIA, SALOMON, MORPHEUS, ALMA, DAATH), definir responsabilidades por checkpoint
  Restrictions: Cada checkpoint debe tener owner responsable de validación
  Success: stakeholders.md con matriz [Rol → Persona → Checkpoint → Responsabilidad]
  ```
- **Context**: [Quiénes participan en esta épica]
- **Status**: Not Started

---

### [ ] M1.3. Definir alcance y constraints

- **File**: `00-problem/scope-and-constraints.md`
- **Requirements**: requirements.md § 1.3, § 5
- **Rostro**: MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[sequential-thinking]`
- **Lesson**: `06-lessons/m1.3-scope-constraints.md`
- **Prompt**:
  ```
  Role: MELQUISEDEC Problem Definer
  Task: Definir qué está dentro/fuera del alcance, identificar constraints técnicos (stack, plataformas, recursos), identificar dependencies externas con riesgos
  Restrictions: Alcance debe ser realista para timeline, constraints deben estar documentados
  Success: scope-and-constraints.md con alcance claro, constraints justificados, riesgos mitigados
  ```
- **Context**: [Límites de esta investigación]
- **Status**: Not Started

---

### [ ] M1.4. Checkpoint CK-01 validation

- **File**: `.spec-workflow/checkpoints/CK-01-validation.yaml`
- **Requirements**: ISSUE.yaml § checkpoints.CK-01
- **Rostro**: MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[grep-search]`
- **Lesson**: `06-lessons/m1.4-ck01-validation.md`
- **Prompt**:
  ```
  Role: MELQUISEDEC Validator
  Task: Validar que problem-statement.md está completo, success criteria son medibles, stakeholders identificados, alcance definido, requirements.md draft completo
  Restrictions: Bloquear avance a PHASE 2 si algún criterio falla
  Success: CK-01-validation.yaml con checklist ✅, ISSUE.yaml actualizado (CK-01.completed = true)
  ```
- **Acceptance Criteria**:
  - [ ] problem-statement.md completo y revisado
  - [ ] Success criteria son SMART
  - [ ] Stakeholders y roles asignados
  - [ ] Alcance y constraints documentados
  - [ ] requirements.md draft con objetivos claros
- **Status**: Not Started

---

## PHASE 2: HYPATIA (Investigación)

> **Rostro**: HYPATIA (Recopilación y Síntesis)
> **Checkpoint**: CK-02
> **MCPs Preferidos**: smart-thinking (síntesis), brave-search, fetch-webpage, firecrawl, context7
> **Output**: 01-literature/ con [N] fuentes, 02-atomics/ con [N] conceptos

---

### [ ] H2.1. Recopilar literatura primaria

- **File**: `01-literature/sources/`
- **Requirements**: requirements.md § 3.1 RF-01
- **Rostro**: HYPATIA
- **MCPs**: `base=[filesystem, memory] | specialized=[brave-search, fetch-webpage, firecrawl, markitdown]`
- **Lesson**: `06-lessons/h2.1-literature-collection.md`
- **Prompt**:
  ```
  Role: HYPATIA Researcher
  Task: Buscar [N] fuentes primarias sobre [tema específico], usar Brave Search para papers, fetch-webpage para artículos, firecrawl para blogs técnicos, convertir PDFs con markitdown, guardar en 01-literature/sources/ con HKM headers (hkm_type: source)
  Restrictions: Mínimo [N] fuentes de alta calidad (papers académicos, documentación oficial, blogs técnicos reconocidos)
  Success: [N] archivos .md en 01-literature/sources/, cada uno con HKM header válido, BibTeX en references.bib
  ```
- **Context**: [Tema específico de búsqueda]
- **Status**: Not Started

---

### [ ] H2.2. Crear notas atómicas (SECI Model)

- **File**: `02-atomics/`
- **Requirements**: requirements.md § 3.1 RF-02
- **Rostro**: HYPATIA
- **MCPs**: `base=[filesystem, memory] | specialized=[smart-thinking]`
- **Lesson**: `06-lessons/h2.2-atomic-notes.md`
- **Prompt**:
  ```
  Role: HYPATIA Researcher
  Task: Extraer conceptos atómicos de literatura usando SECI Model:
    - socialization/: Observaciones directas, experiencias (tácito → tácito)
    - externalization/: Conceptos articulados desde intuición (tácito → explícito)
    - combination/: Síntesis de conceptos explícitos (explícito → explícito)
    - internalization/: Aprendizajes incorporados (explícito → tácito)
  Crear [N] notas atómicas, cada una con UN concepto, HKM header (hkm_type: concept), synthesis_from apuntando a fuentes
  Restrictions: Atomicidad (1 concepto por nota), conexiones explícitas con smart-thinking, citas a fuentes
  Success: [N] notas en 02-atomics/, smart-thinking session con connections, validate-metadata.py pasa
  ```
- **Context**: [Conceptos clave a extraer]
- **Status**: Not Started

---

### [ ] H2.3. Sintetizar conceptos con Zettelkasten

- **File**: `02-atomics/combination/`
- **Requirements**: requirements.md § 3.1 RF-03
- **Rostro**: HYPATIA
- **MCPs**: `base=[filesystem, memory] | specialized=[smart-thinking]`
- **Lesson**: `06-lessons/h2.3-zettelkasten-synthesis.md`
- **Prompt**:
  ```
  Role: HYPATIA Researcher
  Task: Usar smart-thinking MCP para sintetizar conceptos atómicos, identificar conexiones emergentes (supports, refines, contradicts, extends), crear notas de síntesis en 02-atomics/combination/, documentar thought graph en .spec-workflow/context/
  Restrictions: Cada síntesis debe conectar ≥2 atomics, connections con strength ≥0.7
  Success: [N] notas de síntesis, smart-thinking graph con ≥[N] connections, pensamiento reflexivo documentado
  ```
- **Context**: [Relaciones entre conceptos]
- **Status**: Not Started

---

### [ ] H2.4. Checkpoint CK-02 validation

- **File**: `.spec-workflow/checkpoints/CK-02-validation.yaml`
- **Requirements**: ISSUE.yaml § checkpoints.CK-02
- **Rostro**: HYPATIA + MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[grep-search, python-validation]`
- **Lesson**: `06-lessons/h2.4-ck02-validation.md`
- **Prompt**:
  ```
  Role: HYPATIA Researcher + MELQUISEDEC Validator
  Task: Validar que se recopilaron ≥[N] fuentes, se crearon ≥[N] atomics, validate-metadata.py pasa sin errores, smart-thinking graph tiene ≥[N] connections, literatura cubre todos los objetivos de requirements.md
  Restrictions: Bloquear avance a PHASE 3 si cobertura < 80%
  Success: CK-02-validation.yaml ✅, ISSUE.yaml actualizado (CK-02.completed = true)
  ```
- **Acceptance Criteria**:
  - [ ] Mínimo [N] fuentes en 01-literature/
  - [ ] Mínimo [N] atomics en 02-atomics/
  - [ ] validate-metadata.py pasa sin errores
  - [ ] Smart-thinking graph con ≥[N] connections
  - [ ] Cobertura de objetivos ≥80%
- **Status**: Not Started

---

## PHASE 3: SALOMON (Análisis)

> **Rostro**: SALOMON (Análisis y Diseño)
> **Checkpoint**: CK-03
> **MCPs Preferidos**: sequential-thinking (análisis paso a paso), python-refactoring, reasoning-branches (alternativas)
> **Output**: 03-workbook/ con diseño completo, ADRs, diagramas

---

### [ ] S3.1. Análisis comparativo de alternativas

- **File**: `03-workbook/analysis/comparative-analysis.md`
- **Requirements**: requirements.md § 3.2 RF-04
- **Rostro**: SALOMON
- **MCPs**: `base=[filesystem, memory] | specialized=[sequential-thinking]`
- **Lesson**: `06-lessons/s3.1-comparative-analysis.md`
- **Prompt**:
  ```
  Role: SALOMON Architect
  Task: Realizar análisis comparativo de [N] enfoques/alternativas basados en literatura de 02-atomics/, crear matriz de comparación con criterios objetivos (performance, complejidad, mantenibilidad, costos), usar sequential-thinking para análisis estructurado
  Restrictions: Criterios deben estar justificados con evidencia de literatura, scoring debe ser objetivo
  Success: comparative-analysis.md con matriz de decisión, recommendation justificada, referencias a atomics
  ```
- **Context**: [Alternativas a comparar]
- **Status**: Not Started

---

### [ ] S3.2. Diseñar arquitectura/modelo

- **File**: `03-workbook/design/architecture.md`
- **Requirements**: requirements.md § 3.2 RF-05
- **Rostro**: SALOMON
- **MCPs**: `base=[filesystem, memory] | specialized=[sequential-thinking]`
- **Lesson**: `06-lessons/s3.2-architecture-design.md`
- **Prompt**:
  ```
  Role: SALOMON Architect
  Task: Diseñar arquitectura/modelo basado en análisis comparativo, crear diagramas Mermaid (C4 Context/Container/Component, secuencia, clases), documentar decisiones arquitectónicas, definir componentes y sus interfaces
  Restrictions: Arquitectura debe seguir principios del análisis (ej. Hexagonal si aplicable), diagramas deben ser completos
  Success: architecture.md con ≥3 diagramas, diseño completo listo para implementación
  ```
- **Context**: [Tipo de arquitectura requerida]
- **Status**: Not Started

---

### [ ] S3.3. Documentar decisiones (ADRs)

- **File**: `03-workbook/decisions/`
- **Requirements**: requirements.md § 3.2 RF-05
- **Rostro**: SALOMON
- **MCPs**: `base=[filesystem, memory] | specialized=[filesystem]`
- **Lesson**: `06-lessons/s3.3-adrs.md`
- **Prompt**:
  ```
  Role: SALOMON Architect
  Task: Documentar [N] decisiones arquitectónicas clave como ADRs (Architecture Decision Records), seguir formato: Context → Decision → Consequences → Alternatives Considered → Status
  Restrictions: Solo decisiones de alto impacto, cada ADR debe referenciar análisis que la justifica
  Success: [N] ADRs en 03-workbook/decisions/, cada uno con justificación completa
  ```
- **Context**: [Decisiones clave a documentar]
- **Status**: Not Started

---

### [ ] S3.4. Validar diseño con criterios

- **File**: `03-workbook/validation/design-validation.md`
- **Requirements**: requirements.md § 3.2 RF-06
- **Rostro**: SALOMON
- **MCPs**: `base=[filesystem, memory] | specialized=[sequential-thinking]`
- **Lesson**: `06-lessons/s3.4-design-validation.md`
- **Prompt**:
  ```
  Role: SALOMON Architect
  Task: Validar diseño contra success criteria de requirements.md, verificar que arquitectura resuelve problema, que decisiones están justificadas, que diseño es implementable con recursos disponibles
  Restrictions: Validación debe ser objetiva (checklist), identificar riesgos si los hay
  Success: design-validation.md con checklist ✅, riesgos identificados y mitigados
  ```
- **Context**: [Criterios específicos de validación]
- **Status**: Not Started

---

### [ ] S3.5. Checkpoint CK-03 validation

- **File**: `.spec-workflow/checkpoints/CK-03-validation.yaml`
- **Requirements**: ISSUE.yaml § checkpoints.CK-03
- **Rostro**: SALOMON + MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[grep-search]`
- **Lesson**: `06-lessons/s3.5-ck03-validation.md`
- **Prompt**:
  ```
  Role: SALOMON Architect + MELQUISEDEC Validator
  Task: Validar que análisis comparativo está completo, arquitectura documentada con diagramas, [N] ADRs documentados, design validation pasa, diseño alineado con requirements.md
  Restrictions: Bloquear avance a PHASE 4 si diseño no validado
  Success: CK-03-validation.yaml ✅, ISSUE.yaml actualizado (CK-03.completed = true)
  ```
- **Acceptance Criteria**:
  - [ ] Análisis comparativo completo
  - [ ] Arquitectura con ≥3 diagramas
  - [ ] [N] ADRs documentados
  - [ ] Design validation pasa
  - [ ] Diseño alineado con requirements
- **Status**: Not Started

---

## PHASE 4: MORPHEUS+ALMA (Implementación+Publicación) [DIVERGENTE]

> **Rostros**: MORPHEUS (Implementación) + ALMA (Publicación)
> **Checkpoint**: CK-04
> **MCPs Preferidos**: python-refactoring, python-env (research/app), filesystem (todos)
> **Output**: 04-artifacts/ + 05-outputs/ (estructura diverge según `type`)

---

### 4A. Research Type Workflow

#### [ ] R4.1. Implementar notebooks de análisis

- **File**: `04-artifacts/notebooks/`
- **Requirements**: requirements.md § 3.3 RF-07
- **Rostro**: MORPHEUS
- **MCPs**: `base=[filesystem, memory] | specialized=[python-env, activate-python-environment-tools]`
- **Lesson**: `06-lessons/r4.1-research-notebooks.md`
- **Prompt**:
  ```
  Role: MORPHEUS Implementer (Research)
  Task: Implementar [N] Jupyter notebooks siguiendo diseño de 03-workbook/, ejecutar análisis estadístico/ML según arquitectura, documentar resultados inline, asegurar reproducibilidad (requirements.txt, seeds)
  Restrictions: Notebooks deben ser auto-contenidos, ejecutables en <10min, resultados validables
  Success: [N] notebooks en 04-artifacts/notebooks/, todos ejecutables sin errores, resultados documentados
  ```
- **Context**: [Análisis específicos a implementar]
- **Status**: Not Started

---

#### [ ] R4.2. Generar visualizaciones y reportes

- **File**: `05-outputs/reports/`, `05-outputs/visualizations/`
- **Requirements**: requirements.md § 3.4 RF-10, RF-11
- **Rostro**: ALMA
- **MCPs**: `base=[filesystem, memory] | specialized=[python-env]`
- **Lesson**: `06-lessons/r4.2-research-outputs.md`
- **Prompt**:
  ```
  Role: ALMA Publisher (Research)
  Task: Generar reporte técnico consolidando resultados de notebooks, crear visualizaciones publication-ready (matplotlib/seaborn), exportar a PDF/HTML, preparar presentación con hallazgos clave
  Restrictions: Visualizaciones deben seguir guidelines (colores, fonts), reporte debe ser autocontenido
  Success: Reporte técnico ≥20 páginas, ≥5 visualizaciones, presentación lista
  ```
- **Context**: [Audiencia del reporte]
- **Status**: Not Started

---

### 4B. App Type Workflow

#### [ ] A4.1. Implementar código fuente

- **File**: `04-artifacts/src/`
- **Requirements**: requirements.md § 3.3 RF-07
- **Rostro**: MORPHEUS
- **MCPs**: `base=[filesystem, memory] | specialized=[python-refactoring, python-env]`
- **Lesson**: `06-lessons/a4.1-app-implementation.md`
- **Prompt**:
  ```
  Role: MORPHEUS Implementer (App)
  Task: Implementar arquitectura de 03-workbook/ en código Python, seguir estructura Hexagonal si aplicable, escribir tests (TDD: Red-Green-Refactor), configurar Docker, CI/CD
  Restrictions: Coverage ≥80%, SonarQube quality gates, tests pasan en CI
  Success: Código en 04-artifacts/src/, tests en tests/, Docker stack funcional, CI ✅
  ```
- **Context**: [Stack técnico específico]
- **Status**: Not Started

---

#### [ ] A4.2. Documentar API y usuarios

- **File**: `05-outputs/user-docs/`, `05-outputs/api-docs/`
- **Requirements**: requirements.md § 3.4 RF-10, RF-11
- **Rostro**: ALMA
- **MCPs**: `base=[filesystem, memory] | specialized=[filesystem]`
- **Lesson**: `06-lessons/a4.2-app-documentation.md`
- **Prompt**:
  ```
  Role: ALMA Publisher (App)
  Task: Crear documentación de usuario (setup, guías, troubleshooting), generar API docs con Sphinx/MkDocs, preparar release notes, crear demos (videos/screenshots)
  Restrictions: Documentación debe ser testeable (otro usuario puede seguir pasos), API docs auto-generadas
  Success: User docs completa, API docs publicada, release notes lista
  ```
- **Context**: [Audiencia de usuarios]
- **Status**: Not Started

---

### 4C. Social-Project Type Workflow

#### [ ] SP4.1. Crear metodologías e instrumentos

- **File**: `04-artifacts/methodologies/`, `04-artifacts/instruments/`
- **Requirements**: requirements.md § 3.3 RF-07, RF-08
- **Rostro**: MORPHEUS
- **MCPs**: `base=[filesystem, memory] | specialized=[filesystem]`
- **Lesson**: `06-lessons/sp4.1-social-methodologies.md`
- **Prompt**:
  ```
  Role: MORPHEUS Implementer (Social-Project)
  Task: Crear guías metodológicas basadas en diseño de 03-workbook/, desarrollar instrumentos (encuestas, formatos, plantillas), validar con stakeholders, preparar material educativo
  Restrictions: Metodologías deben ser prácticas (aplicables), instrumentos validados con piloto
  Success: Guías metodológicas completas, instrumentos validados, material educativo listo
  ```
- **Context**: [Tipo de proyecto social]
- **Status**: Not Started

---

#### [ ] SP4.2. Generar informes y material de difusión

- **File**: `05-outputs/reports/`, `05-outputs/outreach/`
- **Requirements**: requirements.md § 3.4 RF-10, RF-12
- **Rostro**: ALMA
- **MCPs**: `base=[filesystem, memory] | specialized=[filesystem]`
- **Lesson**: `06-lessons/sp4.2-social-outputs.md`
- **Prompt**:
  ```
  Role: ALMA Publisher (Social-Project)
  Task: Generar informe de proyecto con resultados, crear material de difusión (infografías, videos, posts), preparar capacitación para usuarios finales, documentar impacto social
  Restrictions: Material debe ser accesible (lenguaje claro), informe debe incluir métricas de impacto
  Success: Informe completo, material de difusión publicado, capacitación documentada
  ```
- **Context**: [Audiencia del proyecto social]
- **Status**: Not Started

---

### [ ] 4.X. Checkpoint CK-04 validation (Común a todos los types)

- **File**: `.spec-workflow/checkpoints/CK-04-validation.yaml`
- **Requirements**: ISSUE.yaml § checkpoints.CK-04
- **Rostro**: MORPHEUS + ALMA + MELQUISEDEC
- **MCPs**: `base=[filesystem, memory] | specialized=[grep-search, python-validation]`
- **Lesson**: `06-lessons/4x-ck04-validation.md`
- **Prompt**:
  ```
  Role: MORPHEUS + ALMA + MELQUISEDEC
  Task: Validar que artifacts están completos y funcionales, outputs listos para publicación, validate-triple-coherence.py pasa, mínimo 1 lesson por checkpoint documentado, epic cumple success criteria de requirements.md
  Restrictions: Bloquear archivo si algún criterio falla
  Success: CK-04-validation.yaml ✅, ISSUE.yaml actualizado (CK-04.completed = true)
  ```
- **Acceptance Criteria**:
  - [ ] Artifacts funcionales en 04-artifacts/
  - [ ] Outputs listos en 05-outputs/
  - [ ] validate-triple-coherence.py pasa
  - [ ] Mínimo 1 lesson por CK-01 a CK-04
  - [ ] Success criteria cumplidos
- **Status**: Not Started

---

## PHASE 5: DAATH (Reflexión y Autopoiesis)

> **Rostro**: DAATH (Reflexión)
> **Checkpoint**: Post-CK-04
> **MCPs Preferidos**: smart-thinking (reflexión), filesystem
> **Output**: 06-lessons/ completo, template-improvements.md, epic archivado

---

### [ ] D5.1. Documentar lessons learned por checkpoint

- **File**: `06-lessons/checkpoint-lessons/`
- **Requirements**: requirements.md § 4.3 RNF-07
- **Rostro**: DAATH
- **MCPs**: `base=[filesystem, memory] | specialized=[smart-thinking]`
- **Lesson**: `06-lessons/d5.1-lessons-documentation.md`
- **Prompt**:
  ```
  Role: DAATH Reflector
  Task: Revisar experiencia en cada checkpoint (CK-01 a CK-04), documentar aprendizajes (problemas encontrados, soluciones, mejoras identificadas), usar smart-thinking para conectar lessons con conceptos de 02-atomics/
  Restrictions: Cada lesson debe seguir estructura: Context → Problem → Analysis → Solution → Impact → Applicability
  Success: Mínimo 1 lesson por checkpoint, smart-thinking connections documentadas
  ```
- **Context**: [Experiencias específicas]
- **Status**: Not Started

---

### [ ] D5.2. Identificar mejoras al template

- **File**: `06-lessons/template-improvements.md`
- **Requirements**: requirements.md § 4.3 RNF-08
- **Rostro**: DAATH
- **MCPs**: `base=[filesystem, memory] | specialized=[smart-thinking]`
- **Lesson**: `06-lessons/d5.2-template-improvements.md`
- **Prompt**:
  ```
  Role: DAATH Reflector
  Task: Analizar experiencia con research-autopoietic-template, identificar gaps (qué faltó), proponer mejoras (nuevos archivos, cambios en estructura, mejores prompts), priorizar cambios (P0/P1/P2)
  Restrictions: Propuestas deben ser específicas (no "mejorar X"), justificadas con evidencia de lessons
  Success: template-improvements.md con ≥3 propuestas específicas, prioridades asignadas
  ```
- **Context**: [Experiencia con el template]
- **Status**: Not Started

---

### [ ] D5.3. Sync epic to Neo4j

- **File**: Graph database
- **Requirements**: ISSUE.yaml § hkm.graph_synced
- **Rostro**: DAATH
- **MCPs**: `base=[filesystem, memory] | specialized=[activate-python-environment-tools]`
- **Lesson**: `06-lessons/d5.3-neo4j-sync.md`
- **Prompt**:
  ```
  Role: DAATH Reflector
  Task: Ejecutar sync-hkm-to-neo4j.py para sincronizar todos los .md del epic a Neo4j, verificar que nodos y relaciones se crearon correctamente, actualizar ISSUE.yaml (hkm.graph_synced = true, last_sync = timestamp)
  Restrictions: Validar con validate-triple-coherence.py antes de marcar como synced
  Success: Epic sincronizado a Neo4j, validate-triple-coherence.py pasa, ISSUE.yaml actualizado
  ```
- **Context**: [Neo4j URI: bolt://localhost:7687]
- **Status**: Not Started

---

### [ ] D5.4. Archive epic con Git tag

- **File**: Git repository
- **Requirements**: requirements.md § 4.1 RNF-04
- **Rostro**: DAATH
- **MCPs**: `base=[filesystem, memory] | specialized=[activate-git-branch-management-tools]`
- **Lesson**: `06-lessons/d5.4-epic-archive.md`
- **Prompt**:
  ```
  Role: DAATH Reflector
  Task: Ejecutar archive-epic.sh para crear Git tag vX.Y.Z, realizar soft delete en Neo4j (marcar como archived, no eliminar), actualizar ISSUE.yaml (status = archived), generar README.md final con instrucciones de reproducción
  Restrictions: Tag debe seguir semver, Cypher debe preservar grafo (no DROP)
  Success: Git tag vX.Y.Z creado, epic archivado en Neo4j, README.md con reproducibilidad completa
  ```
- **Context**: [Versión a taggear]
- **Status**: Not Started

---

### [ ] D5.5. Final epic validation

- **File**: `.spec-workflow/checkpoints/FINAL-validation.yaml`
- **Requirements**: requirements.md § 9.1
- **Rostro**: MELQUISEDEC + DAATH
- **MCPs**: `base=[filesystem, memory] | specialized=[grep-search]`
- **Lesson**: `06-lessons/d5.5-final-validation.md`
- **Prompt**:
  ```
  Role: MELQUISEDEC Validator + DAATH Reflector
  Task: Validar Definition of Done completa: todos los checkpoints CK-01 a CK-04 completados, requirements funcionales P0 implementados, validate-triple-coherence.py pasa, validate-metadata.py pasa, lessons documentados, epic sincronizado y archivado
  Restrictions: Epic NO está done hasta que todo esté ✅
  Success: FINAL-validation.yaml ✅, epic marcado como DONE en ISSUE.yaml
  ```
- **Acceptance Criteria (DoD)**:
  - [ ] Todos los checkpoints CK-01 a CK-04 completados
  - [ ] Requirements funcionales P0 implementados
  - [ ] validate-triple-coherence.py pasa
  - [ ] validate-metadata.py pasa
  - [ ] Mínimo 1 lesson por checkpoint
  - [ ] Git tag vX.Y.Z creado
  - [ ] README.md con reproducibilidad
  - [ ] Epic sincronizado a Neo4j
- **Status**: Not Started

---

## Notas de Uso

### MCP Activation Strategy

Este template incluye gestión autopoiética de MCPs. Ver [references/mcp-orchestrator-strategy.md](references/mcp-orchestrator-strategy.md) para detalles.

**Tabla de MCPs por Fase**:

| Fase | MCPs Base | MCPs Especializados | Cuándo Activar |
|------|-----------|---------------------|----------------|
| MELQUISEDEC | filesystem, memory | sequential-thinking | Análisis estructurado del problema |
| HYPATIA | filesystem, memory | brave-search, fetch-webpage, firecrawl, smart-thinking | Búsqueda de literatura, síntesis conceptual |
| SALOMON | filesystem, memory | sequential-thinking, reasoning-branches | Análisis comparativo, diseño arquitectónico |
| MORPHEUS | filesystem, memory | python-refactoring, python-env, docker | Implementación de código/artifacts |
| ALMA | filesystem, memory | filesystem | Generación de outputs publicables |
| DAATH | filesystem, memory | smart-thinking, git | Reflexión, conexión de lessons, archivo |

### Context Management

**Smart Thinking**:
```yaml
# ISSUE.yaml → workflow.autopoiesis.context_management
session_id: "[GENERADO_POR_MCP]"
context_persistence: .spec-workflow/context/
```

**Archivos generados**:
- `.spec-workflow/context/session-[ID].json`: Sesión activa
- `.spec-workflow/context/thoughts-graph.json`: Grafo de pensamientos
- `.spec-workflow/context/connections.json`: Conexiones entre thoughts

### Reasoning Branches

Usar solo si se necesita explorar alternativas paralelas (ej. comparar 2+ diseños arquitectónicos):

```bash
# Crear branch
mcp_maxential-thi_create_branch --branchId alt-stack --description "Alternativa con stack diferente"

# Trabajar en branch
[Desarrollar pensamiento en branch]

# Merge de vuelta a main
mcp_maxential-thi_merge_branch --branchId alt-stack --strategy summary
```

### Validation Scripts

**Antes de CK-02**:
```bash
python packages/daath-toolkit/validators/validate-metadata.py --path apps/research-X/
```

**Antes de CK-04**:
```bash
# Sync MD → Neo4j
python scripts/sync-hkm-to-neo4j.py --epic-path apps/research-X/ --neo4j-uri bolt://localhost:7687

# Validate triple coherence
python scripts/validate-triple-coherence.py --epic apps/research-X/ --neo4j-uri bolt://localhost:7687
```

**Post-CK-04**:
```bash
# Archive epic
bash scripts/archive-epic.sh --epic apps/research-X/ --version 1.0.0
```

### Divergent Workflows

Este template soporta 3 tipos de proyectos. La estructura diverge post-SALOMON (CK-03):

**Research**:
- 04-artifacts/ → notebooks/, scripts/, models/
- 05-outputs/ → papers/, reports/, visualizations/

**App**:
- 04-artifacts/ → src/, tests/, infrastructure/
- 05-outputs/ → user-docs/, releases/, api-docs/

**Social-Project**:
- 04-artifacts/ → methodologies/, instruments/, tools/
- 05-outputs/ → reports/, training/, outreach/

Ajustar tasks en PHASE 4 según `type` en ISSUE.yaml.

---

## Referencias

- **HKM Standard**: [docs/manifiesto/02-arquitectura/03-templates-hkm.md](../../docs/manifiesto/02-arquitectura/03-templates-hkm.md)
- **DAATH-ZEN Format**: [_templates/tasks.md](_templates/tasks.md)
- **Principios P1-P7**: [docs/manifiesto/01-fundamentos/](../../docs/manifiesto/01-fundamentos/)
- **Hybrid Stack**: [apps/research-neo4j-llamaindex-architecture/01-design/](../../apps/research-neo4j-llamaindex-architecture/01-design/)
- **MCP Orchestrator**: [references/mcp-orchestrator-strategy.md](references/mcp-orchestrator-strategy.md)

---

**Última actualización**: YYYY-MM-DD
**Versión**: 1.0.0
**Checkpoint Actual**: CK-01 (MELQUISEDEC)
**Próximo Checkpoint**: CK-02 (HYPATIA)
