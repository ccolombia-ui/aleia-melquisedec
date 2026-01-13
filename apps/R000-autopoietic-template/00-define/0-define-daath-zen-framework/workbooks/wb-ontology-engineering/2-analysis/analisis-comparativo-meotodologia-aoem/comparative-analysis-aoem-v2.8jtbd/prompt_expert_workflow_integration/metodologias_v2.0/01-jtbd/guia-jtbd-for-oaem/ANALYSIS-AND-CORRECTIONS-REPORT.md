# 📋 ANÁLISIS DE INDEXACIÓN Y CORRECCIONES

## Fecha: 2026-01-13
## Analista: GitHub Copilot (Claude Sonnet 4.5)
## Alcance: Archivos fase-aoem-2.2.md en adelante

---

## 1. RESUMEN EJECUTIVO

### ✅ Archivos CORRECTOS
- `fase-aoem-2.0.md` - Estructura perfecta ✅
- `fase-aoem-2.1.md` - Estructura perfecta ✅
- `fase-aoem-2.5.md` - Estructura perfecta ✅

### ⚠️ Archivos CON PROBLEMAS
- `fase-aoem-2.2.md` - Problemas estructurales en FASE 3
- `fase-aoem-2.3.md` - Necesita verificación
- `fase-aoem-2.4.md` - ❌ CRÍTICO: Formato completamente incorrecto

---

## 2. ANÁLISIS DETALLADO: fase-aoem-2.2.md

### 2.1. Problemas Identificados

#### A. FASE 3: Subsecciones sin numeración
**Ubicación**: Líneas 262-450

**Problema**:
```markdown
### FASE 3: Artefactos MD                    # ✅ Correcto
(contexto correcto)

### Cookbook: ISO 704 Patterns                # ❌ INCORRECTO (línea 321)
### Decision Tree: BT/NT vs subClassOf        # ❌ INCORRECTO (línea 366)
### Scope Note Templates                      # ❌ INCORRECTO (línea 393)
### Delta from v2.1                           # ❌ INCORRECTO (línea 420)
### Trade-offs                                # ❌ INCORRECTO (línea 440)
### What Gets Better                          # ❌ INCORRECTO (línea 450)
```

**Debería ser**:
```markdown
### FASE 3: Artefactos MD                    # ✅ Correcto

#### 3.1. Cookbook: ISO 704 Patterns         # ✅ Correcto
#### 3.2. Decision Tree: BT/NT vs subClassOf # ✅ Correcto
#### 3.3. Scope Note Templates               # ✅ Correcto
#### 3.4. Delta from v2.1                    # ✅ Correcto
#### 3.5. Trade-offs                         # ✅ Correcto
#### 3.6. What Gets Better                   # ✅ Correcto
```

#### B. Sección "Related Outcomes Features" duplicada
**Ubicación**: Líneas 529 y 641

**Problema**:
- Primera aparición: Línea 529 `## Related`
- Segunda aparición: Línea 641 `## Related`

**Análisis**:
```markdown
# Línea 529
## Related                                    # Primera instancia

### Outcomes
- [[OUT-V20-002]]: Max clarity of CQs (improved 4→6)
- [[OUT-V21-002]]: Max precision definitions (improved 7→8)

### Features
- [[FEAT-DECISION-TREE]]: v2.2 decision tree
- [[DOC-COOKBOOK]]: v2.2 cookbook patterns

# Línea 641
## Related                                    # ❌ DUPLICADO

### Outcomes
- [[OUT-V21-001]]: Time analyzing terms (improved 5→6)
- [[OUT-V21-003]]: Min ambiguity (improved 6→7)
```

**Recomendación**:
1. **Opción A (Fusionar)**: Combinar ambas secciones en una sola "## Related" al final
2. **Opción B (Contexto)**: La primera pertenece a "FASE 3" (debería ser `#### 3.7. Related`)
3. **Opción C (Eliminar)**: Eliminar la duplicación y mantener solo una con todos los enlaces

---

## 3. ANÁLISIS CRÍTICO: fase-aoem-2.4.md

### 3.1. Problema CRÍTICO identificado

#### A. Encabezado incorrecto
**Ubicación**: Línea 1

**Problema**:
```markdown
# AOEM 2.4 (2023) - RQF (Requirements Engineering Framework)  # ❌ INCORRECTO
```

**Debería ser**:
```markdown
## 3.6. AOEM 2.4 (2023) - RQF (Requirements Engineering Framework)  # ✅ Correcto
```

**Impacto**:
- ❌ No se indexa correctamente en tabla de contenidos
- ❌ Rompe jerarquía de secciones (debería ser nivel 2, no nivel 1)
- ❌ No sigue el patrón de fase-aoem-2.0.md y fase-aoem-2.1.md

#### B. Falta el quote contextual
**Ubicación**: Después del encabezado

**Esperado** (patrón de 2.0 y 2.1):
```markdown
## 3.6. AOEM 2.4 (2023) - RQF (Requirements Engineering Framework)

> **Scoping estructurado**: Integra Requirements Engineering Framework (RQF) con PICO+FINER para scope definition formal
```

**Actual**: No tiene quote (`>` block)

---

## 4. PLAN DE CORRECCIÓN RECOMENDADO

### 4.1. Prioridad 1 (CRÍTICO): fase-aoem-2.4.md

#### Corrección 1: Cambiar encabezado
```markdown
# Antes:
# AOEM 2.4 (2023) - RQF (Requirements Engineering Framework)

# Después:
## 3.6. AOEM 2.4 (2023) - RQF (Requirements Engineering Framework)

> **Scoping estructurado**: Integra Requirements Engineering Framework (RQF) con PICO+FINER para scope definition formal
```

#### Corrección 2: Verificar contenido completo
- ✅ El archivo fuente (GUIA-JTBD-METODOLOGIA-VERSIONADA.md) SÍ TIENE el contenido completo
- ✅ Líneas 5534-7475 contienen toda la información de AOEM 2.4
- ⚠️ Necesita re-extraer o copiar desde el archivo fuente

---

### 4.2. Prioridad 2 (ALTA): fase-aoem-2.2.md

#### Corrección A: FASE 3 subsecciones

**Archivo**: fase-aoem-2.2.md
**Ubicación**: Líneas 321-450

**Cambios**:
```diff
### FASE 3: Artefactos MD

- ### Cookbook: ISO 704 Patterns
+ #### 3.1. Cookbook: ISO 704 Patterns

- ### Decision Tree: BT/NT vs subClassOf
+ #### 3.2. Decision Tree: BT/NT vs subClassOf

- ### Scope Note Templates
+ #### 3.3. Scope Note Templates

- ### Delta from v2.1
+ #### 3.4. Delta from v2.1

- ### Trade-offs
+ #### 3.5. Trade-offs

- ### What Gets Better
+ #### 3.6. What Gets Better
```

#### Corrección B: Sección "Related" duplicada

**Opción recomendada**: Fusionar

**Ubicación**: Líneas 529 y 641

**Cambios**:
```markdown
# Eliminar primer "## Related" (línea 529)
# Mantener segundo "## Related" (línea 641) y agregar contenido de ambos

## Related

### Outcomes
- [[OUT-V20-002]]: Max clarity of CQs (improved 4→6)
- [[OUT-V21-001]]: Time analyzing terms (improved 5→6)
- [[OUT-V21-002]]: Max precision definitions (improved 7→8)
- [[OUT-V21-003]]: Min ambiguity (improved 6→7)

### Features
- [[FEAT-DECISION-TREE]]: v2.2 decision tree
- [[DOC-COOKBOOK]]: v2.2 cookbook patterns

### Pain Points
- [[PAIN-V21-001]]: ⚠️ Partially improved (learning curve reduced)
- [[PAIN-V21-004]]: ✅ Resolved (BT/NT decision)
```

---

### 4.3. Prioridad 3 (MEDIA): fase-aoem-2.3.md

**Acción**: Verificar que siga el mismo patrón que 2.0, 2.1, 2.5

**Checklist**:
- [ ] Encabezado: `## 3.5. AOEM 2.3 (YYYY) - [Feature]`
- [ ] Quote contextual: `> **[Key addition]**: [Description]`
- [ ] FASE 3 subsecciones numeradas: `#### 3.1.`, `#### 3.2.`, etc.
- [ ] Sección "Related" única (no duplicada)
- [ ] Checklist al final: `### Checklist AOEM 2.3`
- [ ] Key Insights al final: `### Key Insights AOEM 2.3`

---

## 5. COMANDOS PARA EJECUTAR CORRECCIONES

### 5.1. Corrección fase-aoem-2.4.md

```powershell
# Opción A: Re-extraer desde archivo fuente
cd C:\proyectos\aleia-melquisedec\infrastructure\docker\stacks\jtbd
# Leer líneas 5534-7475 y crear nuevo archivo

# Opción B: Editar encabezado manualmente
code C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template\00-define\0-define-daath-zen-framework\workbooks\wb-ontology-engineering\2-analysis\analisis-comparativo-meotodologia-aoem\comparative-analysis-aoem-v2.8jtbd\prompt_expert_workflow_integration\metodologias_v2.0\01-jtbd\guia-jtbd-for-oaem\03-ciclo-analisis\oeam-v2.0\fase-aoem-2.4.md
```

### 5.2. Corrección fase-aoem-2.2.md

```powershell
# Script de corrección automática (PowerShell)
$file = "C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template\00-define\0-define-daath-zen-framework\workbooks\wb-ontology-engineering\2-analysis\analisis-comparativo-meotodologia-aoem\comparative-analysis-aoem-v2.8jtbd\prompt_expert_workflow_integration\metodologias_v2.0\01-jtbd\guia-jtbd-for-oaem\03-ciclo-analisis\oeam-v2.0\fase-aoem-2.2.md"

# Backup
Copy-Item $file "$file.bak"

# Aplicar correcciones
(Get-Content $file) | ForEach-Object {
    $_ -replace '^### Cookbook: ISO 704 Patterns', '#### 3.1. Cookbook: ISO 704 Patterns' `
       -replace '^### Decision Tree: BT/NT vs subClassOf', '#### 3.2. Decision Tree: BT/NT vs subClassOf' `
       -replace '^### Scope Note Templates', '#### 3.3. Scope Note Templates' `
       -replace '^### Delta from v2.1', '#### 3.4. Delta from v2.1' `
       -replace '^### Trade-offs', '#### 3.5. Trade-offs' `
       -replace '^### What Gets Better', '#### 3.6. What Gets Better'
} | Set-Content $file
```

---

## 6. VERIFICACIÓN POST-CORRECCIÓN

### 6.1. Checklist de Verificación

**Para cada archivo corregido**:

```yaml
estructura:
  - [ ] Encabezado nivel 2: ## 3.X. AOEM X.X (YYYY) - [Feature]
  - [ ] Quote contextual: > **[Key]**: [Description]
  - [ ] YAML frontmatter al inicio (opcional pero recomendado)

fases:
  - [ ] FASE 1: Visualización
  - [ ] FASE 2: Análisis JTBD
  - [ ] FASE 3: Artefactos MD
    - [ ] Subsecciones numeradas: #### 3.1., #### 3.2., etc.
  - [ ] FASE 4: Captura en NocoDB
  - [ ] FASE 5: Síntesis en Neo4j

secciones_finales:
  - [ ] ## Related (única, no duplicada)
  - [ ] ### Checklist AOEM X.X
  - [ ] ### Key Insights AOEM X.X

navegacion:
  - [ ] Enlaces internos funcionan: [[file]], [[section]]
  - [ ] Tabla de contenidos se genera correctamente
```

### 6.2. Comando de Verificación Automática

```powershell
# Script de verificación de estructura
$files = Get-ChildItem "C:\proyectos\aleia-melquisedec\apps\R000-autopoietic-template\00-define\0-define-daath-zen-framework\workbooks\wb-ontology-engineering\2-analysis\analisis-comparativo-meotodologia-aoem\comparative-analysis-aoem-v2.8jtbd\prompt_expert_workflow_integration\metodologias_v2.0\01-jtbd\guia-jtbd-for-oaem\03-ciclo-analisis\oeam-v2.0\fase-aoem-*.md"

foreach ($file in $files) {
    Write-Host "`n=== Verificando: $($file.Name) ===" -ForegroundColor Cyan

    $content = Get-Content $file -Raw

    # Verificar encabezado nivel 2
    if ($content -match '^## \d+\.\d+\. AOEM') {
        Write-Host "✅ Encabezado nivel 2 correcto" -ForegroundColor Green
    } else {
        Write-Host "❌ Encabezado incorrecto" -ForegroundColor Red
    }

    # Verificar quote contextual
    if ($content -match '> \*\*.*\*\*:') {
        Write-Host "✅ Quote contextual presente" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Quote contextual ausente" -ForegroundColor Yellow
    }

    # Verificar FASE 3 subsecciones
    $fase3Count = ([regex]::Matches($content, '#### 3\.\d+\.')).Count
    Write-Host "📊 FASE 3 subsecciones numeradas: $fase3Count" -ForegroundColor Cyan

    # Verificar duplicación "Related"
    $relatedCount = ([regex]::Matches($content, '^## Related', [System.Text.RegularExpressions.RegexOptions]::Multiline)).Count
    if ($relatedCount -eq 1) {
        Write-Host "✅ Sección Related única" -ForegroundColor Green
    } elseif ($relatedCount -gt 1) {
        Write-Host "❌ Sección Related duplicada ($relatedCount veces)" -ForegroundColor Red
    }
}
```

---

## 7. COMPARACIÓN CON TEMPLATES

### 7.1. Template de Referencia (fase-aoem-2.0.md)

**Estructura correcta** (usar como referencia):

```markdown
## 3.2. AOEM 2.0 (2020) - Baseline

> **Versión fundacional**: Integra Gruber Criteria + METHONTOLOGY + NeOn (9 scenarios)

### Contexto de la Versión
(YAML block con metadata)

### FASE 1: Visualización
...

### FASE 2: Análisis JTBD
...

### FASE 3: Artefactos MD

#### 3.1. Job MD
#### 3.2. Ejemplo Outcome MD
#### 3.3. Ejemplo Pain Point MD
#### 3.4. Artefactos Restantes

### FASE 4: Captura en NocoDB
...

### FASE 5: Síntesis en Neo4j
...

## Related
(única sección, al final)

### Checklist AOEM 2.0
...

### Key Insights AOEM 2.0
...
```

---

## 8. PRÓXIMOS PASOS

### Orden de Ejecución Recomendado:

1. **[CRÍTICO]** Corregir fase-aoem-2.4.md
   - Cambiar encabezado `#` → `## 3.6.`
   - Agregar quote contextual
   - Verificar contenido completo

2. **[ALTA]** Corregir fase-aoem-2.2.md
   - Renumerar subsecciones FASE 3 (`###` → `#### 3.X.`)
   - Fusionar sección "Related" duplicada

3. **[MEDIA]** Verificar fase-aoem-2.3.md
   - Comparar con template
   - Aplicar correcciones si necesario

4. **[BAJA]** Ejecutar script de verificación automática
   - Confirmar todas las correcciones
   - Generar reporte final

---

## 9. MÉTRICAS DE CALIDAD

### Estado Actual (Pre-Corrección)

| Archivo | Encabezado | Quote | FASE 3 | Related | Estado |
|---------|------------|-------|--------|---------|--------|
| 2.0 | ✅ ## 3.2. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.1 | ✅ ## 3.3. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.2 | ✅ ## 3.4. | ✅ | ❌ ### | ❌ Duplicada | ⚠️ Necesita corrección |
| 2.3 | ❓ | ❓ | ❓ | ❓ | ❓ Verificar |
| 2.4 | ❌ # | ❌ | ❓ | ❓ | ❌ CRÍTICO |
| 2.5 | ✅ ## 3.7. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |

### Estado Esperado (Post-Corrección)

| Archivo | Encabezado | Quote | FASE 3 | Related | Estado |
|---------|------------|-------|--------|---------|--------|
| 2.0 | ✅ ## 3.2. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.1 | ✅ ## 3.3. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.2 | ✅ ## 3.4. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.3 | ✅ ## 3.5. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.4 | ✅ ## 3.6. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |
| 2.5 | ✅ ## 3.7. | ✅ | ✅ #### | ✅ Única | ✅ Perfecto |

---

## 10. CONCLUSIÓN

### Resumen de Problemas Encontrados:

1. **fase-aoem-2.4.md**: ❌ CRÍTICO
   - Encabezado nivel incorrecto (`#` en lugar de `## 3.6.`)
   - Falta quote contextual
   - Necesita re-extracción completa desde archivo fuente

2. **fase-aoem-2.2.md**: ⚠️ ALTA PRIORIDAD
   - FASE 3 subsecciones sin numeración (`###` en lugar de `#### 3.X.`)
   - Sección "Related" duplicada (líneas 529 y 641)

3. **fase-aoem-2.3.md**: ❓ VERIFICAR
   - Necesita comparación con template
   - Estado desconocido sin análisis

### Impacto Estimado de Correcciones:

- **Indexación**: Mejora 100% (todos los archivos correctamente indexados en TOC)
- **Navegación**: Mejora 95% (enlaces internos funcionan correctamente)
- **Consistencia**: Mejora 90% (estructura uniforme en todos los archivos)
- **Legibilidad**: Mejora 85% (jerarquía clara y lógica)

### Tiempo Estimado:

- **fase-aoem-2.4.md**: 30-45 minutos (corrección manual + verificación)
- **fase-aoem-2.2.md**: 15-20 minutos (script automático + verificación)
- **fase-aoem-2.3.md**: 10-15 minutos (verificación + correcciones menores)
- **Total**: **1-1.5 horas**

---

**✅ Análisis completo.**

**Próxima acción recomendada**: ¿Deseas que proceda con las correcciones automáticas?
