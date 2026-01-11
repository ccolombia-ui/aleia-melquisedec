# Análisis 002: Estructura de product.md según spec-workflow-mcp

**Tipo**: Análisis de Framework
**Pregunta de Investigación**: ¿Cuál es la estructura oficial de product.md según spec-workflow-mcp y cómo se integra con otros frameworks de gestión de producto?
**Metodología**: Scoping Review (Arksey & O'Malley, 2005)
**Fecha**: 2026-01-11
**Analista**: SALOMÓN
**Workbook**: workbook-product-md/
**Fuente Principal**: [1-literature/framework/spec-workflow-mcp-product-format.md](../1-literature/framework/spec-workflow-mcp-product-format.md)

---

## 1. Introducción

### 1.1. Contexto

**spec-workflow-mcp** es un servidor MCP (Model Context Protocol) que permite a los LLMs gestionar workflows de desarrollo guiado por especificaciones. Este análisis se enfoca en el artefacto `product.md`, uno de los tres **Steering Documents** que proveen contexto estratégico a nivel de proyecto.

### 1.2. Pregunta de Investigación

> **¿Cuál es la estructura oficial y reglas de validación para product.md según spec-workflow-mcp v1.1.2+, y cómo se relaciona con frameworks establecidos de gestión de producto?**

### 1.3. Objetivos del Análisis

1. Identificar la estructura oficial de product.md (secciones obligatorias y opcionales)
2. Documentar reglas de validación (formato, contenido, workflow)
3. Comparar con frameworks de gestión de producto (Product Vision Board, Lean Canvas, SVPG)
4. Extraer conceptos atómicos reutilizables para 3-atomics/
5. Proponer estructura de compilación para 5-compiler/

---

## 2. Hallazgos: Estructura Oficial de product.md

### 2.1. Jerarquía de Steering Documents

Según [spec-workflow-mcp-product-format.md, Sección 1](../1-literature/framework/spec-workflow-mcp-product-format.md#1-overview), los **Steering Documents** son documentos estratégicos **opcionales** a nivel de proyecto:

```
.spec-workflow/
└── steering/                # Documentos estratégicos de proyecto (OPCIONAL)
    ├── product.md           # ⭐ Visión, usuarios, objetivos, métricas
    ├── tech.md              # Stack técnico, principios arquitectónicos
    └── structure.md         # Organización de código, convenciones
```

**Características clave**:
- **Opcionales**: No requeridos para que los specs funcionen, pero altamente recomendados
- **Nivel de proyecto**: UNO por proyecto, NO por spec
- **Requieren aprobación**: Deben ser aprobados vía `mcp_spec-workflow2_approvals()` tool
- **Documento vivo**: Puede evolucionar conforme el producto madura

**Distinción crítica** [spec-workflow-mcp-product-format.md, Sección 5.2]:
- **Steering docs** (product.md, tech.md, structure.md): UNO por proyecto, estratégicos, alto nivel
- **Spec docs** (requirements.md, design.md, tasks.md): MÚLTIPLES por proyecto, tácticos, específicos de feature

---

### 2.2. Estructura Oficial: 7 Secciones

Según [spec-workflow-mcp-product-format.md, Sección 2](../1-literature/framework/spec-workflow-mcp-product-format.md#2-official-template-structure), el template oficial contiene:

#### **Secciones Obligatorias** (6):

1. **Product Purpose** (Propósito del Producto)
   - **Pregunta**: ¿Qué problema resuelve este producto?
   - **Contenido**: Declaración de propósito (1-2 enunciados), dominio del problema, propuesta de valor
   - **Longitud**: 1-3 párrafos (100-300 palabras)

2. **Target Users** (Usuarios Objetivo)
   - **Pregunta**: ¿Quiénes son los usuarios principales?
   - **Contenido**: Personas o roles de usuario, necesidades (qué quieren lograr), puntos de dolor (frustraciones actuales)
   - **Longitud**: 3-5 tipos de usuario con necesidades/dolores

3. **Key Features** (Características Clave)
   - **Pregunta**: ¿Cuáles son las características principales que entregan valor?
   - **Contenido**: Lista numerada de 3-5 características core, nombre + descripción por ítem
   - **Formato**: Enfocado en valor para el usuario, NO implementación técnica

4. **Business Objectives** (Objetivos de Negocio)
   - **Pregunta**: ¿Qué objetivos de negocio busca lograr este producto?
   - **Contenido**: Lista de 3-5 objetivos estratégicos, enfocados en impacto organizacional
   - **Medibilidad**: Resultados medibles cuando sea posible

5. **Success Metrics** (Métricas de Éxito)
   - **Pregunta**: ¿Cómo mediremos el éxito del producto?
   - **Contenido**: Nombre de métrica + valor objetivo por ítem
   - **Mix**: Cuantitativas (números) y cualitativas (satisfacción de usuario)
   - **Longitud**: 4-8 métricas con targets

6. **Product Principles** (Principios del Producto)
   - **Pregunta**: ¿Qué principios guían las decisiones del producto?
   - **Contenido**: Lista numerada de 3-5 principios, nombre + explicación por ítem
   - **Accionables**: Los principios deben guiar decisiones (no solo platitudes)

#### **Secciones Opcionales** (2):

7. **Monitoring & Visibility** (Monitoreo y Visibilidad) - OPCIONAL
   - **Condición**: Solo si el producto incluye dashboard/UI
   - **Contenido**: Tipo de dashboard, mecanismo de actualizaciones en tiempo real, métricas clave mostradas, capacidades de compartir

8. **Future Vision** (Visión Futura) - OPCIONAL
   - **Contenido**: Dirección futura de alto nivel (no roadmap detallado), mejoras potenciales (no compromisos)
   - **Categorías**: Acceso Remoto, Analítica, Colaboración

---

### 2.3. Reglas de Validación

#### 2.3.1. Restricciones de Longitud

Según [spec-workflow-mcp-product-format.md, Sección 3.2](../1-literature/framework/spec-workflow-mcp-product-format.md#32-content-quality-checks):

| Sección | Longitud Recomendada |
|---------|----------------------|
| Product Purpose | 1-3 párrafos (100-300 palabras) |
| Target Users | 3-5 tipos de usuario con necesidades/dolores |
| Key Features | 3-7 características con descripciones |
| Business Objectives | 3-5 objetivos |
| Success Metrics | 4-8 métricas con targets |
| Product Principles | 3-5 principios con explicaciones |

#### 2.3.2. Restricciones de Claridad

**Voz activa** [spec-workflow-mcp-product-format.md, Sección 3.2]:
- ✅ Correcto: "Permitir a los desarrolladores crear specs 10x más rápido"
- ❌ Incorrecto: "Los desarrolladores son habilitados para crear specs"

**Evitar buzzwords vagos** sin ejemplos concretos:
- ❌ Evitar: "innovador", "de vanguardia", "revolucionario"
- ✅ Usar: Ejemplos concretos y métricas específicas

**Métricas medibles**:
- Deben incluir valores objetivo y límites de tiempo
- Ejemplo: "Tiempo de Creación de Spec: < 1 hora (reducción 90% desde baseline de 8 horas) para Q1 2026"

**Principios accionables**:
- Deben guiar decisiones, no solo declaraciones genéricas
- Ejemplo: "Presupuesto de Latencia Sobre Riqueza de Características: Si una característica añade >500ms a latencia de query GraphRAG, diferirla a Fase 2"

#### 2.3.3. Restricciones de Formato

Según [spec-workflow-mcp-product-format.md, Sección 3.3](../1-literature/framework/spec-workflow-mcp-product-format.md#33-format-constraints):

**Cumplimiento de Markdown**:
- Usar `##` para secciones principales (headings nivel 2)
- Usar `###` para subsecciones (headings nivel 3)
- Usar `-` para listas no ordenadas (no `*` o `+`)
- Usar listas numeradas para ítems secuenciales (Key Features, Product Principles)
- Incluir bloques de código con tags de lenguaje: ````markdown` no solo ````

**Nomenclatura de archivo**:
- DEBE llamarse exactamente `product.md` (minúsculas, sin prefijo/sufijo)
- DEBE colocarse en `.spec-workflow/steering/product.md`
- Uno product.md por proyecto (no por spec)

---

### 2.4. Integración con Workflow de Aprobación

#### 2.4.1. Proceso de Aprobación

Según [spec-workflow-mcp-product-format.md, Sección 4.1](../1-literature/framework/spec-workflow-mcp-product-format.md#41-approval-process), los steering documents **requieren aprobación** vía dashboard de spec-workflow-mcp:

```python
# Paso 1: Cargar guía de steering
mcp_spec-workflow2_steering-guide()

# Paso 2: Crear product.md siguiendo template
create_file("../.spec-workflow/steering/product.md", content)

# Paso 3: Solicitar aprobación
mcp_spec-workflow2_approvals(
    action="request",
    type="document",
    category="steering",
    categoryName="steering",
    title="Solicitar aprobación para documento steering product.md",
    filePath=".spec-workflow/steering/product.md"
)

# Paso 4: Encuestar status hasta aprobado
status = mcp_spec-workflow2_approvals(action="status", approvalId=approval_id)
while status == "pending":
    # Esperar 5-10 segundos
    status = mcp_spec-workflow2_approvals(action="status", approvalId=approval_id)

# Paso 5: Limpiar solicitud de aprobación (después de aprobado)
mcp_spec-workflow2_approvals(action="delete", approvalId=approval_id)

# Paso 6: Repetir para tech.md y structure.md
```

**Estados de aprobación**:
- `pending`: Esperando revisión del usuario en dashboard
- `approved`: Usuario aprobó, proceder con workflow
- `rejected`: Usuario rechazó, atender feedback y recrear
- `needs-revision`: Usuario solicitó cambios, actualizar y re-solicitar

#### 2.4.2. Timing

**Workflow de steering documents** (los 3 documentos: product.md, tech.md, structure.md):
- **Tiempo estimado**: 1-2 horas (30-40 minutos por documento)
- **Cuándo crear**:
  - En inicialización del proyecto (antes del primer spec)
  - Cuando la visión del producto cambia significativamente
  - Al añadir nuevas áreas de producto (actualización opcional)

**Nota importante**: Los steering docs son OPCIONALES. Puedes comenzar con specs (requirements.md, design.md, tasks.md) sin steering docs. Sin embargo, los steering docs proveen contexto valioso para LLMs trabajando en specs.

---

## 3. Análisis Comparativo con Frameworks de Gestión de Producto

### 3.1. Product Vision Board (Roman Pichler, 2016)

#### Estructura del Framework

El **Product Vision Board** [Pichler, Strategize, 2016] organiza la estrategia de producto en una jerarquía visual:

```
                    Vision
                      |
        ┌─────────────┼─────────────┐
        |             |             |
    Target       Needs          Product
    Group                      Concept
        |             |             |
        └─────────────┴─────────────┘
                      |
              Business Goals
```

**Componentes**:
1. **Vision**: ¿Por qué construimos este producto? (propósito aspiracional)
2. **Target Group**: ¿Para quién? (segmentos de clientes, personas)
3. **Needs**: ¿Qué problema resuelve? (necesidades del usuario, dolores)
4. **Product**: ¿Qué es? (concepto del producto, características clave)
5. **Business Goals**: ¿Qué logramos? (objetivos de negocio, métricas)

#### Mapeo a product.md

Según [spec-workflow-mcp-product-format.md, Sección 9.1](../1-literature/framework/spec-workflow-mcp-product-format.md#91-product-management-frameworks), existe compatibilidad directa:

| Product Vision Board | product.md Sección | Contenido Mapeado |
|----------------------|-------------------|-------------------|
| Vision | Product Purpose | Propósito aspiracional, problema a resolver |
| Target Group | Target Users | Segmentos de usuarios, personas, roles |
| Needs | Target Users (subsección) | Puntos de dolor, frustraciones actuales |
| Product | Key Features | Concepto del producto, características core |
| Business Goals | Business Objectives | Objetivos estratégicos organizacionales |

**Convergencia observada**:
- Ambos frameworks priorizan visión aspiracional (no feature list)
- Ambos conectan necesidades del usuario → características del producto → objetivos de negocio
- Ambos recomiendan claridad y brevedad (Vision Board es visual, product.md es textual)

**Divergencias**:
- Product Vision Board NO incluye métricas de éxito detalladas (solo Business Goals de alto nivel)
- product.md añade **Product Principles** (no presente en Vision Board)
- product.md añade **Success Metrics** con targets específicos (Vision Board es más estratégico)

---

### 3.2. Lean Canvas (Ash Maurya, 2012)

#### Estructura del Framework

El **Lean Canvas** [Maurya, Running Lean, 2012, p.13-25] es una adaptación del Business Model Canvas enfocada en startups:

```
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│  Problem   │  Solution  │   UVP      │  Unfair    │  Customer  │
│            │            │            │ Advantage  │  Segments  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│  Existing  │  Key       │  Channels  │  Revenue   │  Cost      │
│Alternatives│  Metrics   │            │  Streams   │ Structure  │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

**Componentes clave para product.md**:
1. **Problem**: Top 3 problemas del usuario (con niveles de dolor)
2. **Solution**: Características principales (top 3)
3. **UVP** (Unique Value Proposition): Fórmula `[Resultado Final] + [Tiempo] + [Objeciones Resueltas]`
4. **Customer Segments**: Segmentos de clientes (early adopters primero)
5. **Key Metrics**: Métricas accionables (no vanity metrics)

#### Mapeo a product.md

| Lean Canvas | product.md Sección | Contenido Mapeado |
|-------------|-------------------|-------------------|
| Problem | Target Users (pain points) | Top 3 problemas, niveles de dolor |
| Solution | Key Features | Características principales (3-7) |
| UVP | Product Purpose | Propuesta de valor única |
| Customer Segments | Target Users | Segmentos de usuarios, early adopters |
| Key Metrics | Success Metrics | Métricas accionables con targets |

**Convergencia observada**:
- Ambos priorizan problemas del usuario antes de soluciones
- Ambos requieren métricas específicas (Key Metrics vs Success Metrics)
- Ambos evitan "vanity metrics" (Lean Canvas) / "vague buzzwords" (product.md)

**Divergencias**:
- Lean Canvas incluye modelo de negocio completo (Revenue Streams, Cost Structure) - product.md NO
- Lean Canvas es más táctico (canales, ventaja injusta) - product.md es más estratégico
- product.md añade **Product Principles** (no presente en Lean Canvas)

---

### 3.3. SVPG Product Strategy (Marty Cagan, 2017)

#### Estructura del Framework

El framework **SVPG** (Silicon Valley Product Group) [Cagan, Inspired, 2017, p.35-42] define product vision como:

> "La product vision describe el futuro que estamos tratando de crear, típicamente 2-10 años fuera" [Cagan, 2017, p.37]

**Componentes de product vision según SVPG**:
1. **WHO**: ¿Para quién estamos construyendo? (target customers)
2. **WHAT**: ¿Qué transformación buscamos lograr? (aspirational outcome)
3. **HOW**: ¿Cómo lo lograremos? (approach, differentiators)
4. **WHY**: ¿Por qué importa? (impact on users/business)

**Principios SVPG**:
- La visión debe **inspirar** al equipo (no solo describir)
- Debe ser **estratégica** (no táctica)
- Debe ser **clara** (memorable, fácil de repetir)
- Debe ser **long-term** (2-10 años, no próximo quarter)

#### Mapeo a product.md

| SVPG Component | product.md Sección | Contenido Mapeado |
|----------------|-------------------|-------------------|
| WHO | Target Users | Target customers, personas |
| WHAT | Product Purpose | Transformación aspiracional |
| HOW | Key Features + Product Principles | Approach, differentiators, guiding principles |
| WHY | Business Objectives | Impacto en usuarios/negocio |
| Product Principles (SVPG) | Product Principles | Principios que guían decisiones del producto |

**Convergencia observada**:
- Ambos requieren visión aspiracional (no feature list)
- Ambos enfatizan claridad y brevedad (1-2 enunciados para visión core)
- Ambos incluyen **Product Principles** como concepto central
- Ambos requieren timeframe largo (2-10 años según SVPG)

**Divergencias**:
- SVPG NO prescribe estructura específica de documento (es framework conceptual)
- product.md es más estructurado (7 secciones obligatorias/opcionales)
- product.md añade **Success Metrics** detalladas (SVPG es más filosófico)

---

### 3.4. Tabla Comparativa: Convergencia de Frameworks

| Componente | Product Vision Board | Lean Canvas | SVPG | product.md |
|------------|---------------------|-------------|------|------------|
| **Visión Aspiracional** | ✅ Vision | ✅ UVP | ✅ WHAT/WHY | ✅ Product Purpose |
| **Usuarios Objetivo** | ✅ Target Group | ✅ Customer Segments | ✅ WHO | ✅ Target Users |
| **Problemas/Necesidades** | ✅ Needs | ✅ Problem (top 3) | ✅ WHY (impact) | ✅ Target Users (pain points) |
| **Características** | ✅ Product | ✅ Solution (top 3) | ✅ HOW (approach) | ✅ Key Features |
| **Objetivos de Negocio** | ✅ Business Goals | ❌ (Revenue/Cost only) | ✅ WHY (business impact) | ✅ Business Objectives |
| **Métricas de Éxito** | ❌ (implícito en Goals) | ✅ Key Metrics | ❌ (no prescriptivo) | ✅ Success Metrics |
| **Principios del Producto** | ❌ | ❌ | ✅ Product Principles | ✅ Product Principles |
| **Modelo de Negocio** | ❌ | ✅ Revenue/Cost | ❌ | ❌ |

**Conclusión del análisis comparativo**:

product.md de spec-workflow-mcp **sintetiza lo mejor de 3 frameworks**:
1. De **Product Vision Board**: Jerarquía clara (Vision → Target/Needs/Product → Goals)
2. De **Lean Canvas**: Énfasis en métricas accionables, top problemas del usuario
3. De **SVPG**: Product principles como guía de decisiones, visión inspiracional long-term

**Diferenciadores únicos de product.md**:
- **Machine-readable**: Markdown + MCP tools (vs. visual boards o PDF)
- **Approval workflow**: Integración con dashboard async (vs. email threads)
- **LLM-optimized**: Estructura clara, contenido conciso, sin jerga
- **Project-level scope**: Steering document (no per-feature como PRD)

---

## 4. Anti-Patrones: Errores Comunes a Evitar

Según [spec-workflow-mcp-product-format.md, Sección 7](../1-literature/framework/spec-workflow-mcp-product-format.md#7-common-mistakes-to-avoid), se identifican **4 anti-patrones** principales:

### 4.1. Product Purpose Vago

❌ **MALO**:
```markdown
## Product Purpose
Construir una plataforma innovadora que aprovecha IA de vanguardia para
revolucionar la forma en que los desarrolladores crean especificaciones.
```

**Problemas**:
- Buzzwords sin sustancia ("innovadora", "de vanguardia", "revolucionar")
- No declara problema claro
- No hay resultado medible

✅ **BUENO**:
```markdown
## Product Purpose
Permitir a los desarrolladores crear especificaciones de alta calidad 10x más
rápido mediante templates guiados por conocimiento, metodologías de investigación
epistemológica y búsqueda semántica GraphRAG. DAATH-ZEN resuelve el "cuello de
botella de creación de specs" donde los equipos gastan 40-60% del tiempo de
proyecto en documentación en lugar de implementación.
```

**Por qué es bueno**:
- Propuesta de valor clara ("10x más rápido")
- Problema específico ("cuello de botella", "40-60% tiempo en docs")
- Mecanismo concreto ("investigación epistemológica", "GraphRAG")

---

### 4.2. Target Users Genéricos

❌ **MALO**:
```markdown
## Target Users
- Desarrolladores que quieren escribir mejor código
- Product managers que necesitan planear características
- Equipos que valoran calidad
```

**Problemas**:
- Demasiado genérico (todos los devs quieren mejor código)
- No menciona puntos de dolor
- No identifica necesidades específicas

✅ **BUENO**:
```markdown
## Target Users

### Primario: Software Architects (Nivel Senior/Lead)
- **Necesidad**: Documentar decisiones arquitectónicas con trazabilidad completa a literatura
- **Dolor**: Síntesis manual de investigación toma 8+ horas por ADR, frecuentemente con gaps de citación
- **Ganancia**: Reducir tiempo de creación de ADR a < 1 hora con síntesis automática de literatura

### Secundario: Product Managers (Technical PMs)
- **Necesidad**: Crear product.md con visión clara, métricas y criterios de éxito
- **Dolor**: Declaraciones de visión son vagas, carecen de conexión con datos de investigación de usuarios
- **Ganancia**: Generar product.md basado en datos desde Scoping Review de entrevistas de usuarios
```

---

### 4.3. Listas de Features en lugar de Principles

❌ **MALO**:
```markdown
## Product Principles

1. **Rápido**: El sistema debe ser rápido
2. **Confiable**: El sistema no debe fallar
3. **Amigable**: La UI debe ser fácil de usar
```

**Problemas**:
- No accionable (¿cómo decides si algo es "suficientemente rápido"?)
- Platitudes genéricas (todo producto quiere ser rápido/confiable/amigable)
- Sin guía de trade-offs (¿qué pasa si velocidad conflictúa con confiabilidad?)

✅ **BUENO**:
```markdown
## Product Principles

1. **Latency Budget Sobre Feature Richness**: Si una característica añade >500ms
   a latencia de query GraphRAG, diferirla a Fase 2. Experiencia de usuario se
   degrada exponencialmente más allá de 500ms. Trade-off: menos características,
   funcionalidad core más rápida.

2. **Fail-Fast Validation**: Validar temprano (contratos 4-artefact/) antes de
   compilación (5-compiler/). Si validación falla, detener inmediatamente con
   mensaje de error claro. Trade-off: workflow más estricto, menos sorpresas en runtime.

3. **Explicit Over Implicit**: Hacer transformaciones epistemológicas visibles
   (1-literature/ → 2-analysis/ → 3-atomics/ → etc.). Transparencia ayuda debugging.
   Trade-off: más archivos/carpetas, flujo de conocimiento más claro.
```

**Por qué es bueno**:
- Umbrales accionables ("presupuesto de latencia 500ms")
- Guía trade-offs ("menos características, core más rápido")
- Explica POR QUÉ ("transparencia ayuda debugging")

---

### 4.4. Success Metrics No Medibles

❌ **MALO**:
```markdown
## Success Metrics

- Aumentar satisfacción del usuario
- Mejorar calidad del código
- Reducir deuda técnica
```

**Problemas**:
- Sin baseline (¿mejorar desde qué?)
- Sin target (¿cuánta mejora?)
- No medible (¿cómo cuantificas "satisfacción"?)

✅ **BUENO**:
```markdown
## Success Metrics

- **User Satisfaction (NPS)**: ≥ 70 (baseline: N/A, target: Q1 2026, n ≥ 10 usuarios)
- **Code Coverage**: ≥ 80% (baseline: 0%, target: Q1 2026, medido vía pytest-cov)
- **Technical Debt Ratio**: < 10% (baseline: 35% desde SonarQube, target: Q2 2026)
```

**Por qué es bueno**:
- Medible (score NPS, % coverage, ratio de deuda)
- Tiene valores objetivo (≥ 70, ≥ 80%, < 10%)
- Time-bound (Q1 2026, Q2 2026)
- Incluye método de medición (pytest-cov, SonarQube)

---

## 5. Conceptos Atómicos Identificados

Del análisis de spec-workflow-mcp product.md, se extraen **7 conceptos atómicos** para `3-atomics/`:

### 5.1. concept-product-purpose.json

**Definición**: Declaración de propósito de producto (problema + solución + valor)

**Componentes**:
- Problem statement (declaración del problema)
- Solution approach (enfoque de solución)
- Value proposition (propuesta de valor)

**Longitud**: 1-3 párrafos (100-300 palabras)

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 2.1](../1-literature/framework/spec-workflow-mcp-product-format.md#21-product-purpose)
- [Cagan, Inspired, 2017, p.35-42]: Product vision como futuro aspiracional

---

### 5.2. concept-target-user-persona.json

**Definición**: Estructura de persona de usuario (rol + necesidades + dolores + ganancias)

**Componentes**:
- User role/title (rol/título de usuario)
- User needs (necesidades - qué quieren lograr)
- Pain points (puntos de dolor - frustraciones actuales)
- Gains (ganancias - beneficios esperados)

**Longitud**: 3-5 personas con sección de 2-4 bullets cada una

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 2.2](../1-literature/framework/spec-workflow-mcp-product-format.md#22-target-users)
- [Pichler, Product Vision Board, 2016]: Target Group component
- [Maurya, Lean Canvas, 2012, p.13-25]: Customer Segments + Early Adopters

---

### 5.3. concept-business-objective.json

**Definición**: Estructura de objetivo de negocio (objetivo estratégico + resultado medible)

**Componentes**:
- Strategic goal (objetivo estratégico)
- Organizational impact (impacto organizacional)
- Measurable outcome (resultado medible cuando sea posible)

**Longitud**: 3-5 objetivos

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 2.4](../1-literature/framework/spec-workflow-mcp-product-format.md#24-business-objectives)
- [Pichler, Product Vision Board, 2016]: Business Goals component

---

### 5.4. concept-success-metric.json

**Definición**: Estructura de métrica de éxito (nombre + target + baseline + método + timebound)

**Componentes**:
- Metric name (nombre de métrica)
- Target value (valor objetivo)
- Baseline value (valor baseline)
- Measurement method (método de medición)
- Time-bound (límite de tiempo)

**Longitud**: 4-8 métricas con targets

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 2.5](../1-literature/framework/spec-workflow-mcp-product-format.md#25-success-metrics)
- [Maurya, Lean Canvas, 2012, p.77-88]: Key Metrics (actionable metrics, not vanity)

---

### 5.5. concept-product-principle.json

**Definición**: Estructura de principio de producto (nombre + explicación + trade-offs + ejemplos)

**Componentes**:
- Principle name (nombre del principio)
- Explanation (explicación de cómo guía decisiones)
- Trade-offs (trade-offs explícitos)
- Examples (ejemplos de aplicación)

**Longitud**: 3-5 principios con explicaciones

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 2.6](../1-literature/framework/spec-workflow-mcp-product-format.md#26-product-principles)
- [Cagan, SVPG Product Principles]: Principles that guide product decisions

---

### 5.6. concept-key-feature.json

**Definición**: Estructura de característica clave (nombre + descripción + valor para usuario)

**Componentes**:
- Feature name (nombre de característica)
- Description (descripción de funcionalidad)
- User value (valor entregado al usuario)

**Longitud**: 3-7 características con descripciones

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 2.3](../1-literature/framework/spec-workflow-mcp-product-format.md#23-key-features)
- [Pichler, Product Vision Board, 2016]: Product component
- [Maurya, Lean Canvas, 2012]: Solution (top 3 features)

---

### 5.7. concept-steering-document.json

**Definición**: Tipos de steering documents (product/tech/structure) y workflow de aprobación

**Componentes**:
- Document types (tipos de documento: product, tech, structure)
- Approval workflow (workflow de aprobación: request → poll → delete)
- Approval states (estados: pending, approved, rejected, needs-revision)
- Timing (timing: 30-40 minutos por documento)

**Fuentes**:
- [spec-workflow-mcp-product-format.md, Sección 4](../1-literature/framework/spec-workflow-mcp-product-format.md#4-workflow-integration)

---

## 6. Implicaciones para Compilación (5-compiler/)

### 6.1. Estructura de Template Jinja2

Basado en el análisis, el template `5-compiler/templates/product.md.j2` debe seguir esta estructura:

```jinja2
# Product Vision: {{project_name}}

## Product Purpose
{{product_purpose}}

## Target Users
{% for user in target_users %}
### {{user.role}}
- **Necesidad**: {{user.needs}}
- **Dolor**: {{user.pain_points}}
- **Ganancia**: {{user.gains}}
{% endfor %}

## Key Features
{% for feature in key_features %}
{{loop.index}}. **{{feature.name}}**: {{feature.description}}
{% endfor %}

## Business Objectives
{% for objective in business_objectives %}
- {{objective.goal}}
{% endfor %}

## Success Metrics
{% for metric in success_metrics %}
- **{{metric.name}}**: {{metric.target}} (baseline: {{metric.baseline}}, target: {{metric.timebound}}, medido vía {{metric.method}})
{% endfor %}

## Product Principles
{% for principle in product_principles %}
{{loop.index}}. **{{principle.name}}**: {{principle.explanation}} Trade-off: {{principle.tradeoffs}}
{% endfor %}

{% if monitoring %}
## Monitoring & Visibility
- **Dashboard Type**: {{monitoring.dashboard_type}}
- **Real-time Updates**: {{monitoring.realtime_updates}}
- **Key Metrics Displayed**: {{monitoring.key_metrics}}
- **Sharing Capabilities**: {{monitoring.sharing}}
{% endif %}

{% if future_vision %}
## Future Vision
### Potential Enhancements
{% for enhancement in future_vision %}
- **{{enhancement.category}}**: {{enhancement.description}}
{% endfor %}
{% endif %}

---
**Compiled from**: workbook-product-md/
**Sources**: {{source_count}} referencias
**Last Updated**: {{compilation_date}}
```

### 6.2. Validación Pre-Compilación

El script `5-compiler/compile-product.py` debe validar contra `4-artefact/contract-product-md-schema.json`:

**Checks obligatorios**:
1. ✅ Las 6 secciones obligatorias están presentes
2. ✅ Product Purpose: 100-300 palabras
3. ✅ Target Users: 3-5 personas con needs/pains/gains
4. ✅ Key Features: 3-7 características
5. ✅ Business Objectives: 3-5 objetivos
6. ✅ Success Metrics: 4-8 métricas con targets + baselines + methods + timebound
7. ✅ Product Principles: 3-5 principios con trade-offs
8. ✅ No buzzwords vagos sin ejemplos concretos
9. ✅ Voz activa en lugar de pasiva
10. ✅ Formato Markdown correcto (##, ###, -, listas numeradas)

**Output en caso de error**: Mensaje detallado indicando qué sección falló validación y por qué.

---

## 7. Propuesta de Estructura para product.md de SPEC-001

Basado en el análisis de spec-workflow-mcp y frameworks de gestión de producto, se propone la siguiente estructura para product.md de SPEC-001 (Built Template spec-workflow):

### 7.1. Product Purpose

```markdown
## Product Purpose

Permitir a los desarrolladores crear especificaciones de alta calidad 10x más
rápido mediante templates guiados por conocimiento, metodologías de investigación
epistemológica (Scoping Review) y búsqueda semántica GraphRAG.

DAATH-ZEN resuelve el "cuello de botella de creación de specs" donde los equipos
gastan 40-60% del tiempo de proyecto en documentación en lugar de implementación,
resultando en specs sin trazabilidad a fuentes, conceptos no reutilizables y
compilación manual propensa a errores.
```

### 7.2. Target Users

```markdown
## Target Users

### Primario: Software Architects (Senior/Lead)
- **Necesidad**: Documentar decisiones arquitectónicas con trazabilidad completa a literatura académica
- **Dolor**: Síntesis manual de investigación toma 8+ horas por ADR, frecuentemente con gaps de citación
- **Ganancia**: Reducir tiempo de creación de ADR a < 1 hora con síntesis automática de literatura

### Secundario: Product Managers (Technical PMs)
- **Necesidad**: Crear product.md con visión clara, métricas de éxito y criterios validables
- **Dolor**: Declaraciones de visión son vagas, carecen de conexión con datos de investigación de usuarios
- **Ganancia**: Generar product.md basado en datos desde Scoping Review de entrevistas de usuarios

### Terciario: Research Engineers (ML/AI)
- **Necesidad**: Convertir papers académicos en specs de implementación accionables
- **Dolor**: Papers usan formato IMRAD (experimental), specs necesitan formato de descubrimiento de dominio
- **Ganancia**: Aplicar Scoping Review methodology para mapear dominio desde papers sin inventar contenido
```

### 7.3. Key Features

```markdown
## Key Features

1. **5-Workbook Epistemology**: Cada artefacto (product.md, requirements.md, etc.)
   tiene un workbook autocontenido con flujo literatura → análisis → atomics →
   validación → compilación → ingesta.

2. **Scoping Review Methodology**: Preguntas de investigación respondidas vía
   framework Arksey & O'Malley con citación completa de fuentes (0 contenido inventado).

3. **Neo4j GraphRAG**: Todos los conceptos ingestados en base de datos de grafos
   con relaciones CITED_IN, RELATES_TO, USED_IN para queries semánticas.

4. **Automated Validators**: Validadores basados en Python (textstat readability,
   regex patterns) para checks de calidad automatizados contra contratos JSON Schema.

5. **Jinja2 Compilation**: Templates compilan desde atomics/ con validación contra
   contratos 4-artefact/ antes de output final.
```

### 7.4. Business Objectives

```markdown
## Business Objectives

- Reducir tiempo de creación de specs 90% (de 8 horas a 45 minutos por spec)
- Habilitar reuso de conocimiento entre proyectos vía conceptos atómicos
- Mejorar calidad de specs con validación automatizada (0 claims no documentados)
- Escalar productividad del equipo sin contratar más especialistas de documentación
```

### 7.5. Success Metrics

```markdown
## Success Metrics

- **Spec Creation Time**: < 1 hora por spec (baseline: 8 horas, reducción 90%, target: Q1 2026)
- **Citation Coverage**: 100% de claims trazables a fuentes 1-literature/ (baseline: ~40%, target: Q1 2026)
- **Validator Pass Rate**: ≥ 95% de specs pasan validación automatizada en primer intento (baseline: N/A, target: Q1 2026)
- **GraphRAG Query Latency**: < 500ms para búsqueda semántica de conceptos en 1000+ nodos (baseline: N/A, target: Q1 2026)
- **User Adoption**: 3+ equipos usando templates DAATH-ZEN para Q1 2026
- **NPS Score**: ≥ 70 desde usuarios piloto (n ≥ 10 respondentes, target: Q1 2026)
```

### 7.6. Product Principles

```markdown
## Product Principles

1. **Autocontenido (Self-Contained)**: Cada workbook contiene TODOS los elementos
   necesarios (literatura → validación → compilación) para generar su artefacto.
   Sin dependencias externas más allá de fuentes 1-literature/. Trade-off: más
   archivos por workbook, claridad de trazabilidad completa.

2. **Trazabilidad Total (Total Traceability)**: Cada claim debe citar una fuente.
   Usar formato [source-name, page numbers]. 0 contenido inventado. Si un enunciado
   no puede citarse, no debe existir. Trade-off: proceso de investigación más lento,
   conocimiento 100% verificable.

3. **Epistemología Explícita (Explicit Epistemology)**: Hacer transformaciones de
   conocimiento visibles: ENTRADA (1-literature/) → PROCESO (2-analysis/) →
   EXTRACCIÓN (3-atomics/) → VALIDACIÓN (4-artefact/) → COMPILACIÓN (5-compiler/)
   → INGESTA (6-outputs/). Transparencia ayuda debugging. Trade-off: más carpetas/
   estructura, flujo de conocimiento claro.

4. **Metodología Documentada (Documented Methodology)**: Cada workbook sigue Scoping
   Review (Arksey & O'Malley 2005) para descubrimiento de dominio, NO IMRAD (que es
   para experimentos). Metodología debe ser explícita en README.md. Trade-off:
   adherencia estricta a metodología, reproducibilidad científica.

5. **Automatización con Validación (Automation with Validation)**: Compilación es
   automatizada (templates Jinja2), pero DEBE validar contra contratos 4-artefact/
   antes de output. No "trust but verify" – validar luego compilar. Trade-off:
   workflow más estricto, menos errores en runtime.
```

---

## 8. Referencias

### 8.1. Fuentes Primarias

1. **spec-workflow-mcp Official Repository**
   - URL: https://github.com/pimzino/spec-workflow-mcp
   - Versión: v1.1.2+
   - Archivo: `product-template.md`
   - Accedido: 2026-01-11
   - Documentado en: [1-literature/framework/spec-workflow-mcp-product-format.md](../1-literature/framework/spec-workflow-mcp-product-format.md)

### 8.2. Frameworks de Gestión de Producto

2. **Strategize: Product Strategy and Product Roadmap Practices for the Digital Age**
   - Autor: Roman Pichler
   - Año: 2016
   - ISBN: 978-0993499203
   - Relevante: Product Vision Board framework (Vision → Target/Needs/Product → Goals)

3. **Running Lean: Iterate from Plan A to a Plan That Works**
   - Autor: Ash Maurya
   - Año: 2012
   - ISBN: 978-1449305178
   - Relevante: Lean Canvas (Problem → Solution → UVP → Metrics), top 3 problems methodology

4. **Inspired: How to Create Tech Products Customers Love**
   - Autor: Marty Cagan
   - Año: 2017
   - ISBN: 978-1119387503
   - Relevante: Product vision (WHO/WHAT/HOW/WHY), product principles concepts

### 8.3. Metodología de Investigación

5. **Scoping studies: towards a methodological framework**
   - Autores: Arksey, H., & O'Malley, L.
   - Año: 2005
   - Journal: International Journal of Social Research Methodology
   - Volume: 8(1)
   - Páginas: 19-32
   - DOI: 10.1080/1364557032000119616
   - Relevante: Framework de 6 etapas para scoping reviews

---

## 9. Próximos Pasos

### 9.1. Para 3-atomics/

Extraer los 7 conceptos identificados:
1. ⏳ `concept-product-purpose.json`
2. ⏳ `concept-target-user-persona.json`
3. ⏳ `concept-business-objective.json`
4. ⏳ `concept-success-metric.json`
5. ⏳ `concept-product-principle.json`
6. ⏳ `concept-key-feature.json`
7. ⏳ `concept-steering-document.json`

### 9.2. Para 4-artefact/

Crear validación:
- ⏳ `contract-product-md-schema.json`: JSON Schema para product.md
- ⏳ `test-product-md-structure.md`: Test de estructura (6 secciones obligatorias)
- ⏳ `test-product-md-quality.md`: Test de calidad (longitud, claridad, buzzwords)

### 9.3. Para 5-compiler/

Implementar compilación:
- ⏳ `compile-product.py`: Script Python que lee 2-analysis/ + 3-atomics/, valida, renderiza template
- ⏳ `templates/product.md.j2`: Template Jinja2 según estructura propuesta en Sección 7

### 9.4. Para 6-outputs/

Generar índices:
- ⏳ `cypher/ingest-product-md-structure.cypher`: Actualizar con nuevos conceptos
- ⏳ `embeddings/product-concepts-embeddings.json`: Generar embeddings bilingües (inglés + español)

---

## 10. Conclusión

Este análisis documenta la estructura oficial de product.md según spec-workflow-mcp v1.1.2+, identificando:

1. **7 secciones** (6 obligatorias + 2 opcionales)
2. **Reglas de validación** (longitud, claridad, formato)
3. **Workflow de aprobación** (request → poll → approved → delete)
4. **Convergencia de frameworks** (Product Vision Board + Lean Canvas + SVPG)
5. **4 anti-patrones** a evitar (propósito vago, usuarios genéricos, principios no accionables, métricas no medibles)
6. **7 conceptos atómicos** para extraer a 3-atomics/
7. **Estructura propuesta** para product.md de SPEC-001

El análisis confirma que product.md es un **steering document estratégico** (no PRD táctico) que sintetiza mejores prácticas de 3 frameworks establecidos, optimizado para lectura LLM y workflow de aprobación async.

**Próximo paso**: Atomizar los 7 conceptos en `3-atomics/` con esquema bilingüe (inglés + español) para grafos y embeddings.

---

**Documento creado**: 2026-01-11
**Analista**: SALOMÓN
**Workbook**: workbook-product-md/
**Status**: ✅ COMPLETO
**Siguiente**: 3-atomics/ atomización de conceptos
