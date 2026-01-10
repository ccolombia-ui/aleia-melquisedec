# 📚 ÍNDICE Y ANÁLISIS DE COHERENCIA: .spec-workflow

**Fecha**: 2026-01-09
**Versión MCP**: spec-workflow-mcp (pimzino/spec-workflow-mcp)
**Trust Score Context7**: 7.7/10
**Code Snippets**: 321

---

## 🔍 RESUMEN EJECUTIVO

| Aspecto | Estado | Puntuación |
|---------|--------|------------|
| Estructura de directorios | ⚠️ Parcial | 70% |
| Conformidad con MCP oficial | ⚠️ Divergencias significativas | 55% |
| Documentación interna | ✅ Excesiva pero útil | 85% |
| Formato de tasks.md | ⚠️ Extendido más allá del estándar | 65% |
| Steering docs | ✅ Completos | 90% |
| Specs activos | ⚠️ Mixtos en coherencia | 60% |

---

## 📁 ÍNDICE COMPLETO DE CARPETAS Y DOCUMENTOS

### 1. **Raíz: `.spec-workflow/`**

| Archivo | Propósito Declarado | Propósito MCP Oficial | Coherencia |
|---------|--------------------|-----------------------|------------|
| `README.md` | Guía del sistema DAATH-ZEN + spec-workflow | Entry point básico | ⚠️ **SOBRECARGADO** - Mezcla metodología propia con MCP |

**Diagnóstico**: El README mezcla 3 conceptos que deberían estar separados:
1. spec-workflow-mcp (herramienta)
2. DAATH-ZEN (metodología personalizada)
3. Autopoiesis (ciclo de aprendizaje)

---

### 2. **`steering/`** - Documentos de Dirección del Proyecto

| Archivo | Propósito | Coherencia MCP | Estado |
|---------|-----------|----------------|--------|
| `product.md` | Visión del producto DAATH-ZEN | ✅ Correcto | Específico para monorepo-improvements |
| `tech.md` | Stack técnico | ✅ Correcto | Bien estructurado |
| `structure.md` | Principios de organización | ✅ Correcto | Buen contenido |
| `best-practices.md` | ❌ **NO EXISTE EN MCP OFICIAL** | ⚠️ Añadido personalizado | Útil pero no estándar |

**Coherencia**: 80% - Los 3 archivos base (`product.md`, `tech.md`, `structure.md`) siguen el estándar MCP. `best-practices.md` es una extensión personalizada válida.

**Referencia MCP Oficial**:
```typescript
// create-steering-doc soporta:
docType: "product" | "tech" | "structure"
```

---

### 3. **`specs/`** - Especificaciones Activas

| Spec | Documentos | Estado | Coherencia |
|------|------------|--------|------------|
| `git-push-workflow-v1.0.0/` | ✅ requirements, design, tasks, lessons-learned | 1/9 tasks completado | ⚠️ 55% |
| `monorepo-improvements/` | ✅ + README, analysis/, _meta/ | 6/7 tasks completados | ⚠️ 60% |
| `research-keter-integration-v1.0.0/` | ✅ + artifacts/, Implementation Logs/, _meta/ | En progreso | ⚠️ 50% |
| `triple-persistence-architecture-best-practices/` | ✅ + tasks-ORIGINAL-RECOVERED.md | Formato recuperado | ⚠️ 45% |

#### 3.1 Estructura MCP Oficial vs. Actual

**MCP Oficial espera**:
```
specs/{spec-name}/
├── requirements.md
├── design.md
└── tasks.md
```

**Estructura Actual (extendida)**:
```
specs/{spec-name}/
├── requirements.md      ✅ Correcto
├── design.md            ✅ Correcto
├── tasks.md             ⚠️ Formato extendido
├── README.md            ❓ No estándar MCP
├── _meta/               ❌ No estándar MCP
├── analysis/            ❌ No estándar MCP
├── artifacts/           ❌ No estándar MCP
├── Implementation Logs/ ❌ No estándar MCP
└── lessons-learned/     ⚠️ Mencionado pero no oficial
```

---

### 4. **`_meta/`** - Meta-información

| Archivo | Propósito | Coherencia MCP | Valor |
|---------|-----------|----------------|-------|
| `RESUMEN_SISTEMA_COMPLETO.md` | Documentación exhaustiva del sistema | ❌ No existe en MCP | Alto valor interno |
| `GUIA_RAPIDA.md` | Quick start | ❌ No existe en MCP | Alto valor interno |
| `best-practices.md` | Guía completa (redundante con steering/) | ❌ Duplicación | Confuso |
| `templates/` | Templates personalizados | ⚠️ MCP tiene `get-template-context` | Parcial |

**Problema Crítico**: `best-practices.md` existe tanto en `_meta/` como mencionado para `steering/`. Esto viola el principio DRY.

---

### 5. **`analysis/`** - Análisis y Estudios

| Archivo | Propósito | Coherencia MCP | Estado |
|---------|-----------|----------------|--------|
| `gap-analysis-2026-01-08.md` | Análisis de gaps post-implementación | ❌ No estándar | Útil |
| `mcp-thinking-servers-comparative-analysis.md` | Comparativa de MCPs | ❌ No estándar | Útil |
| `pre-commit-vs-push-workflow-DUMMIES.md` | Guía explicativa | ❌ No estándar | Útil |

**Veredicto**: Carpeta útil pero **no reconocida por spec-workflow-mcp**. El MCP no tiene herramientas para gestionar estos archivos.

---

### 6. **`approvals/`** - Flujo de Aprobaciones

| Contenido | Estado | Coherencia MCP |
|-----------|--------|----------------|
| `.gitkeep` | Vacío | ⚠️ Sin uso |

**MCP Oficial**:
```typescript
// request-approval crea archivos en:
.spec-workflow/approvals/{spec-name}/
```

**Estado Actual**: La carpeta existe pero no se está usando el flujo de aprobaciones del MCP.

---

### 7. **`archive/`** - Specs Archivados

| Subcarpeta | Contenido | Coherencia MCP |
|------------|-----------|----------------|
| `specs/demo-fix-references/` | Spec completo archivado | ⚠️ Parcial |
| `image/` | ❓ Imágenes | ❌ No estándar |
| `tasks.md` | ❓ Tasks sueltos | ❌ No estándar |
| `templates/` | Templates antiguos | ❌ No estándar |

**MCP Oficial espera**:
```
archive/
└── specs/
    └── {spec-name}/
```

**Problema**: `archive/` tiene archivos sueltos y carpetas no estándar.

---

## ⚠️ GAPS DE COHERENCIA IDENTIFICADOS

### GAP-1: Formato de `tasks.md` Extendido (CRÍTICO)

**MCP Oficial** (según documentación Context7):
```markdown
- [ ] 1.1 Task title
  - Description of task
  - Files: ["src/file.ts"]
  - Requirements: ["REQ-1"]
```

**Formato Actual en Melquisedec**:
```markdown
- [ ] 1.1. Task title
  - File: *.md, *.py
  - _Requirements: REQ-1_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[...]_
  - _Lesson: lessons-learned/task-1.1.md_
  - _Prompt: Role: X | Task: Y | Restrictions: Z | Success: W_
```

**Diferencias**:
| Campo | MCP Oficial | Melquisedec | Impacto |
|-------|-------------|-------------|---------|
| Task ID | `1.1` | `1.1.` (con punto) | ⚠️ Parser puede fallar |
| Requirements | `Requirements:` | `_Requirements:_` (itálica) | ⚠️ Parser puede no detectar |
| Rostro | ❌ No existe | ✅ Añadido | ❓ Ignorado por MCP |
| MCPs | ❌ No existe | ✅ Añadido | ❓ Ignorado por MCP |
| Lesson | ❌ No existe | ✅ Añadido | ❓ Ignorado por MCP |
| Prompt | ❌ No existe | ✅ Añadido | ❓ Ignorado por MCP |

**Riesgo**: Los campos añadidos son útiles para DAATH-ZEN pero **el MCP oficial los ignora** y podrían romper el parser de tasks.

---

### GAP-2: Carpetas No Reconocidas

El MCP oficial reconoce SOLO:
```
.spec-workflow/
├── specs/
├── steering/
├── approvals/
└── archive/
```

**Carpetas añadidas no reconocidas**:
- `_meta/` - El MCP no sabe que existe
- `analysis/` - El MCP no sabe que existe
- Dentro de specs: `_meta/`, `analysis/`, `artifacts/`, `Implementation Logs/`

---

### GAP-3: Duplicación de Documentación

| Documento | Ubicación 1 | Ubicación 2 | Problema |
|-----------|-------------|-------------|----------|
| best-practices | `steering/best-practices.md` (referenciado) | `_meta/best-practices.md` (existe) | ¿Cuál es el SSoT? |
| Templates | `_meta/templates/` | Patrones en `_templates/daath-zen-patterns/` (fuera de .spec-workflow) | Fragmentación |

---

### GAP-4: Flujo de Aprobaciones No Usado

El MCP tiene herramientas de aprobación:
```typescript
// request-approval, get-approval-status, delete-approval
```

**Estado actual**: `approvals/` vacío con `.gitkeep`. No se está usando el flujo de aprobaciones oficial.

---

### GAP-5: Versionado Inconsistente de Specs

| Spec | Versionado | Problema |
|------|------------|----------|
| `git-push-workflow-v1.0.0` | ✅ Semver en nombre | Correcto |
| `monorepo-improvements` | ❌ Sin versión en carpeta | Solo en steering/product.md |
| `research-keter-integration-v1.0.0` | ✅ Semver en nombre | Correcto |
| `triple-persistence-architecture-best-practices` | ❌ Nombre muy largo, sin versión | Problema |

---

## 🎯 ESTRATEGIA RECOMENDADA

### Opción A: **Conformidad Estricta con MCP** (Recomendada si se usa dashboard/extension)

**Acciones**:
1. **Normalizar formato de tasks.md**:
   - Quitar punto final del task ID: `1.1.` → `1.1`
   - Mover campos DAATH-ZEN a comentarios HTML o sección separada

2. **Consolidar _meta/ en steering/**:
   - Mover `best-practices.md` a `steering/`
   - Mover guías a `steering/` o fuera de `.spec-workflow/`

3. **Limpiar archive/**:
   - Mover archivos sueltos a ubicaciones apropiadas
   - Mantener solo `archive/specs/`

4. **Activar flujo de aprobaciones**:
   - Usar `request-approval` del MCP
   - Integrar con VS Code extension

5. **Estandarizar versionado**:
   - Renombrar `monorepo-improvements` → `monorepo-improvements-v1.1.0`

**Pros**: Máxima compatibilidad con herramientas MCP
**Cons**: Pierde metadata DAATH-ZEN en tasks.md

---

### Opción B: **Extensión Documentada** (Recomendada si DAATH-ZEN es prioritario)

**Acciones**:
1. **Documentar extensiones en README.md**:
   ```markdown
   ## Extensiones DAATH-ZEN
   Este proyecto extiende spec-workflow-mcp con:
   - Campos adicionales en tasks.md (Rostro, MCPs, Lesson, Prompt)
   - Carpeta _meta/ para documentación interna
   - Carpeta analysis/ para estudios
   ```

2. **Crear wrapper/adapter**:
   - Script que normaliza tasks.md para MCP
   - Script que enriquece tasks.md con DAATH-ZEN

3. **Separar concerns**:
   ```
   .spec-workflow/        # MCP estándar
   .daath-zen/            # Extensiones DAATH-ZEN
   ```

4. **Mantener SSoT en steering/**:
   - Mover `_meta/best-practices.md` → `steering/best-practices.md`
   - Eliminar duplicados

**Pros**: Preserva metodología DAATH-ZEN, flexible
**Cons**: Requiere mantenimiento de 2 sistemas

---

### Opción C: **Híbrida Pragmática** (Balance)

**Acciones Inmediatas** (Quick Wins):
1. ✅ Unificar `best-practices.md` en `steering/`
2. ✅ Limpiar `archive/` de archivos sueltos
3. ✅ Añadir versión a `monorepo-improvements`

**Acciones de Mediano Plazo**:
4. Crear script de validación de coherencia
5. Documentar extensiones DAATH-ZEN
6. Probar flujo de aprobaciones MCP

**Mantener Como Está**:
- Formato extendido de tasks.md (si no rompe el parser)
- Carpetas `_meta/` y `analysis/` (documentarlas)

---

## 📋 TABLA DE ACCIONES PRIORIZADAS

| # | Acción | Impacto | Esfuerzo | Prioridad |
|---|--------|---------|----------|-----------|
| 1 | Unificar best-practices.md en steering/ | Alto (SSoT) | Bajo | 🔴 Alta |
| 2 | Renombrar monorepo-improvements con versión | Medio | Bajo | 🟡 Media |
| 3 | Limpiar archive/ de archivos sueltos | Medio | Bajo | 🟡 Media |
| 4 | Documentar extensiones DAATH-ZEN en README | Alto | Medio | 🔴 Alta |
| 5 | Probar formato tasks.md con MCP parser | Alto (validación) | Medio | 🔴 Alta |
| 6 | Evaluar flujo de aprobaciones | Bajo | Alto | 🟢 Baja |
| 7 | Crear script de validación | Medio | Alto | 🟢 Baja |

---

## 🔗 REFERENCIAS MCP OFICIALES

**Herramientas Core**:
- `spec-workflow-guide`: Carga guía completa
- `create-spec-doc`: Crea requirements/design/tasks
- `create-steering-doc`: Crea product/tech/structure
- `manage-tasks`: Lista, actualiza, completa tasks
- `request-approval`: Solicita aprobación
- `get-template-context`: Obtiene templates oficiales

**Estructura Oficial**:
```
.spec-workflow/           # 755 (rwxr-xr-x)
├── specs/               # 755 - Especificaciones activas
├── steering/            # 755 - Documentos de dirección
├── approvals/           # 755 - Flujo de aprobaciones (on-demand)
└── archive/             # 755 - Specs archivados
    └── specs/
```

---

## ✅ CONCLUSIÓN

El sistema actual de `.spec-workflow` en Melquisedec es **funcional pero divergente** del estándar MCP. Las extensiones DAATH-ZEN (Rostros, MCPs, Lessons, Prompts) añaden valor metodológico pero no son reconocidas por las herramientas oficiales.

**Recomendación Final**: Implementar **Opción C (Híbrida)** con foco en:
1. Consolidar documentación (eliminar duplicados)
2. Documentar extensiones explícitamente
3. Validar que el parser MCP funciona con el formato actual
4. Evaluar si el flujo de aprobaciones añade valor al workflow actual
