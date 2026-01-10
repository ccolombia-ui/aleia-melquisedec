# Lección 001: Diseño de Arquitectura de Templates para Specs

## Metadatos

| Campo | Valor |
|-------|-------|
| **Lesson ID** | LESSON-001 |
| **Fecha** | 2026-01-10 |
| **Contexto** | Definición estrategia SPEC-001 |
| **Specs Relacionados** | SPEC-001 (built-template-spec-workflow) |
| **Confianza** | 0.85 (Alta - basado en análisis teórico) |
| **Estado** | Por validar en implementación |
| **Categoría** | Arquitectura / Meta-diseño |

---

## 📚 Lo que Aprendimos

### 1. Las Meta-Especificaciones son Fundamentales
**Aprendizaje**: Antes de implementar features, debemos especificar **cómo especificar**.

**Evidencia**: El usuario pivoteó de S001 (estructura básica de carpetas) a SPEC-001 (infraestructura de templates) porque sin templates apropiados, todas las specs futuras tendrían:
- Contenido duplicado
- Estructura inconsistente
- Pobre trazabilidad
- Gestión de versiones difícil

**Implicación**: En sistemas autopoiéticos, **la meta-infraestructura precede a la infraestructura**.

**Principio Aplicado**: **P2 (Autopoiesis)** - El sistema debe diseñarse para evolucionar antes de poder evolucionar.

---

### 2. Workbooks como Fuente Única de Verdad
**Aprendizaje**: Separar **contenido (workbooks)** de **presentación (artefactos spec)** habilita evolución sin romper specs.

**Arquitectura**:
```
Workbook (evoluciona) → Template (adapta) → Spec (vista compilada)
```

**Evidencia**:
- Los workbooks pueden actualizarse conforme el sistema aprende
- Múltiples specs pueden referenciar los mismos productos del workbook
- La compilación asegura que los specs siempre reflejen el conocimiento más reciente
- Obsidian provee ambiente natural de edición

**Implicación**: **Nunca escribir requirements.md directamente**—escribir workbooks, compilar a specs.

**Principio Aplicado**: **P9 (Inmutabilidad)** - Los specs compilados son snapshots, los workbooks son documentos vivos.

---

### 3. Integración RBM Requiere Soporte Estructural
**Aprendizaje**: La jerarquía Results-Based Management (RBM) debe estar **codificada en la estructura de carpetas**, no solo en la documentación.

**Estructura**:
```
wb-rbm-spec/
├── resultado_final.md           # Resultado Final
├── ri-001-feature/              # Resultado Intermedio
│   ├── ri-feature.md
│   └── rinm-producto/           # Resultados Inmediatos
│       ├── REQ-001-story.md     # Producto
│       ├── REQ-002-rule.md      # Producto
│       └── REQ-003-contract.md  # Producto
```

**Beneficios**:
1. **Trazabilidad**: El path del archivo codifica la jerarquía de resultados
2. **Métricas**: Cada nivel tiene outputs medibles
3. **Navegación**: El grafo de Obsidian muestra cadenas causales
4. **Validación**: Los scripts pueden verificar la matriz de coherencia

**Implicación**: RBM no es solo un "framework a aplicar"—es un **patrón arquitectónico**.

**Principio Aplicado**: **P7 (Recursión Fractal)** - La estructura se repite en cada escala.

---

### 4. Herencia de Templates Reduce Duplicación
**Aprendizaje**: Los elementos comunes (headers, metadata, protocolos) deben ser **heredados**, no duplicados.

**Patrón**:
```yaml
template_hierarchy:
  base: daath-zen-base.md        # HKM + Dublin Core
  variants:
    requirements:
      extends: base
      sections: [overview, stories, functional]
    design:
      extends: base
      sections: [architecture, decisions, adr]
```

**Evidencia**:
- Si el formato del header HKM cambia, actualizar solo el template base
- La versión se propaga automáticamente
- Consistencia garantizada
- Principio DRY (Don't Repeat Yourself)

**Implicación**: Usar **config.yaml-ld** para definir jerarquía de herencia.

**Principio Aplicado**: **P1 (Síntesis)** - Orquestar, no duplicar.

---

### 5. Protocolo Keter-Doc Habilita Interoperabilidad Semántica
**Aprendizaje**: Usar **JSON-LD** para metadata de documentos habilita:
1. Semántica explícita
2. Ingestión en graph database
3. Linking entre proyectos
4. Razonamiento de IA sobre relaciones

**Ejemplo**:
```yaml
# issue.yaml-ld
"@context":
  "@vocab": "http://melquisedec.org/ontology#"
  dc: "http://purl.org/dc/terms/"

"@type": "ResearchIssue"
"@id": "urn:melquisedec:issue:spec-001"
dc:title: "Build daath-zen templates"
dc:created: "2026-01-10"
implementsPrinciple:
  - "@id": "urn:melquisedec:principle:P1"
  - "@id": "urn:melquisedec:principle:P2"
```

**Implicación**: Cada documento debe tener **@context**, **@type**, **@id**.

**Principio Aplicado**: **P6 (Persistencia Triple)** - Capa de graph semántico.

---

### 6. Decisión de Granularidad: Producto = REQ-XXX
**Aprendizaje**: REQ-XXX debe mapear a **Resultados Inmediatos (Productos)**, no Resultados Intermedios (Features).

**Razonamiento**:
- **Muy grueso** (REQ-001 = autenticación completa): Pierde trazabilidad
- **Muy fino** (REQ-001-01-a-1 = una línea de código): Inmanejable
- **Justo** (REQ-001-01 = historia de usuario "login con email"): Testeable, trazable, medible

**Esquema de Numeración**:
```
REQ-RI-Rinm
REQ-001-01  = Resultado Intermedio 001, Resultado Inmediato 01
REQ-001-02  = Resultado Intermedio 001, Resultado Inmediato 02
REQ-002-01  = Resultado Intermedio 002, Resultado Inmediato 01
```

**Implicación**: Cada REQ mapea a un **producto medible** con criterios de éxito claros.

**Principio Aplicado**: **P5 (Checkpoints)** - Validar a nivel de producto.

---

### 7. Enfoque Híbrido: Contenido Modular, Artefactos Monolíticos
**Aprendizaje**: spec-workflow-mcp espera **archivos únicos** (requirements.md), pero necesitamos **contenido modular** (workbooks).

**Solución**: **Paso de compilación**
```
Workbook (modular) → compile_spec_from_workbook.py → Spec (monolítico)
```

**Proceso**:
1. Usuario edita workbook en Obsidian
2. IA ejecuta script de compilación
3. Script procesa transclusions `![[]]`
4. Genera requirements.md con matriz de coherencia
5. Valida contra protocolo keter-doc
6. Escribe a spec-workflow-mcp

**Beneficios**:
- Lo mejor de ambos mundos
- Compatibilidad con spec-workflow-mcp
- Flexibilidad de workbook
- Consistencia automatizada

**Implicación**: Necesitamos **compile_spec_from_workbook.py** en SPEC-001.

**Principio Aplicado**: **P1 (Síntesis)** - Orquestar herramientas existentes.

---

### 8. Investigación Antes de Implementación
**Aprendizaje**: SPEC-001 requiere **fase de investigación** antes de escribir requirements.

**Tasks a Investigar**:
1. Formato actual de spec-workflow-mcp (¿qué es obligatorio?)
2. Diseño de protocolo keter-doc (schema JSON-LD)
3. Soporte de transclusions (¿nativo o compilado?)
4. Numeración REQ-XXX (¿qué tan profundo anidar?)
5. Compatibilidad Obsidian (estrategia de sincronización Neo4j)

**Razonamiento**:
- No se pueden diseñar templates sin entender restricciones
- No se puede diseñar protocolo sin estudiar ontologías
- No se puede decidir monolítico vs modular sin probar herramientas

**Implicación**: SPEC-001 tiene **Fase 0: Investigación** antes de Requirements.

**Principio Aplicado**: **P3 (Issue-Driven)** - Cada investigación es un issue.

---

### 9. Matriz de Coherencia Debe Ser Computable
**Aprendizaje**: La matriz de coherencia RBM debe ser **datos**, no solo narrativa.

**Formato**:
```yaml
# coherence-matrix.yaml
result_chain:
  - id: RF-001
    title: "Sistema de autenticación seguro"
    intermediate_results:
      - id: RI-001
        title: "Feature de login"
        immediate_results:
          - id: REQ-001-01
            title: "Historia de usuario: login con email"
            metrics:
              - success_rate: ">95%"
              - response_time: "<500ms"
```

**Beneficios**:
- Machine-readable
- Scripts de validación
- Generación automática de diagramas
- Ingestión a Neo4j

**Implicación**: Los templates incluyen sección **coherence-matrix.yaml**.

**Principio Aplicado**: **P6 (Persistencia Triple)** - Datos estructurados para graph.

---

### 10. Autopoiesis Requiere Loops de Feedback
**Aprendizaje**: El sistema aprende **comparando intención de diseño (workbook) con realidad de implementación (logs)**.

**Loop**:
```
1. Diseñar en workbook (predicción)
2. Implementar desde tasks
3. Loguear resultados reales
4. Comparar predicción vs realidad
5. Actualizar workbook con lecciones
6. Incrementar score de confianza
7. Propagar a otros workbooks
```

**Ejemplo**:
- Workbook predijo: "API de login < 500ms"
- Log de implementación: "Real: 350ms promedio"
- Lección: "Predicción precisa, incrementar confianza 0.75 → 0.85"
- Propagar: Actualizar workbooks relacionados de autenticación

**Implicación**: Necesitamos script **compare_prediction_vs_reality.py**.

**Principio Aplicado**: **P2 (Autopoiesis)** - El sistema se mejora a sí mismo.

---

## 🎯 Patrones Descubiertos

### Patrón 1: Triángulo Template-Workbook-Spec
```
   Template (estructura)
      /  \
     /    \
Workbook  Spec
(contenido) (vista)
```

- **Template**: Define estructura y herencia
- **Workbook**: Contiene contenido evolutivo
- **Spec**: Snapshot compilado para spec-workflow-mcp

### Patrón 2: Meta-Spec Antes de Feature-Spec
```
SPEC-001 (meta)  →  SPEC-002+ (features)
```

Construir infraestructura para especificar antes de especificar features.

### Patrón 3: Compilar-Validar-Someter
```
1. Editar workbook (manual)
2. Compilar a spec (automático)
3. Validar coherencia (automático)
4. Someter a dashboard (automático)
5. Aprobar (manual)
```

Automatización entre pasos manuales.

### Patrón 4: RBM como File System
```
Estructura de carpetas = Jerarquía de resultados
Nombre de archivo = ID de producto
Contenido = Especificación de producto
```

### Patrón 5: JSON-LD en Todas Partes
```
Cada YAML → Agregar @context, @type, @id
```

Habilita compatibilidad con semantic web.

---

## 🚀 Acciones Recomendadas

### Inmediato (SPEC-001 Fase 0)
1. ✅ Crear workbook `wb-rbm-spec-001/`
2. ⏳ Investigar formato actual de spec-workflow-mcp
3. ⏳ Diseñar protocolo keter-doc (schema JSON-LD)
4. ⏳ Probar transclusions Obsidian → Neo4j

### Corto Plazo (SPEC-001 Implementación)
1. ⏳ Crear template base `daath-zen-base.md`
2. ⏳ Crear templates variantes (requirements, design, tasks, steering)
3. ⏳ Implementar `compile_spec_from_workbook.py`
4. ⏳ Implementar validadores de coherencia

### Largo Plazo (Post-SPEC-001)
1. ⏳ Crear SPEC-002 usando templates SPEC-001 (validación)
2. ⏳ Implementar loop de feedback autopoiético
3. ⏳ Construir sistema de scoring de confianza
4. ⏳ Crear motor de recomendación de templates

---

## 🔄 Estrategia de Evolución

### Versión 1.0 (SPEC-001)
- Herencia básica de templates
- Compilación manual
- Validación simple de coherencia

### Versión 1.1 (Después de 3 specs)
- Compilación automatizada al guardar
- Matriz de coherencia mejorada
- Extracción de patrones desde lecciones

### Versión 2.0 (Después de 10 specs)
- Templates sugeridos por IA
- Recomendaciones basadas en confianza
- Workbooks auto-actualizables

---

## ⚠️ Riesgos y Mitigaciones

### Riesgo 1: Sobre-Ingeniería
**Riesgo**: Templates demasiado complejos, usuarios los evitan.
**Mitigación**: Empezar minimal, agregar features basado en pain points reales.

### Riesgo 2: Incompatibilidad con spec-workflow-mcp
**Riesgo**: Specs compilados no funcionan con dashboard.
**Mitigación**: Probar compilación temprano, validar contra parser de la herramienta.

### Riesgo 3: Lock-in a Obsidian
**Riesgo**: Sistema solo funciona con Obsidian.
**Mitigación**: Usar Markdown estándar, links como `[text](path)` como fallback.

### Riesgo 4: Complejidad Creciente
**Riesgo**: Cada spec agrega nuevas features de template, sistema se vuelve inmanejable.
**Mitigación**: Gobernanza estricta vía versionado de config.yaml-ld.

---

## 📊 Métricas de Éxito

### Calidad de Templates
- [ ] Todos los 6 templates heredan de base
- [ ] No hay contenido duplicado entre templates
- [ ] Cambios de versión se propagan en < 5 minutos

### Usabilidad de Workbook
- [ ] Nuevo workbook de spec creado en < 30 minutos
- [ ] Compilación exitosa al primer intento > 80%
- [ ] Validación de coherencia detecta errores > 90%

### Efectividad de Autopoiesis
- [ ] Lecciones capturadas después de cada spec
- [ ] Scores de confianza incrementan con el tiempo
- [ ] Templates evolucionan basados en lecciones

---

## 🔗 Documentos Relacionados

- [CHATLOG-2026-01-10_125024-spec-001-estrategia-es.md](../logs/CHATLOG-2026-01-10_125024-spec-001-estrategia-es.md)
- [raw-manifiesto-melquisedec.md](../manifest/1-inputs/raw-manifiesto-melquisedec.md)
- SPEC-001 (por crear)

---

## 💡 Conclusión Clave

> **"No especificar features antes de especificar cómo especificar."**

SPEC-001 no trata sobre construir un sistema—trata sobre construir el **lenguaje y gramática** para describir sistemas. Una vez que esa meta-capa existe, todas las specs futuras se vuelven:
- Más consistentes
- Menos duplicadas
- Más trazables
- Más evolutivas

Esto es **arquitectura lingüística**: definir el vocabulario antes de escribir la historia.

---

**Lección Extraída Por**: GitHub Copilot (Claude Sonnet 4.5)
**Confianza**: 0.85 (Alta - basado en análisis teórico, por validar)
**Próxima Validación**: Después de implementación SPEC-001
**Estado**: Aprendizaje Activo
