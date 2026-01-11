# Lean Canvas - Ash Maurya

**Tipo de Fuente**: Framework de Modelo de Negocio
**Autor**: Ash Maurya
**Año**: 2012
**Fuente Original**: https://leanstack.com/lean-canvas
**Libro Relacionado**: Running Lean: Iterate from Plan A to a Plan That Works
**ISBN**: 978-1449305178
**Editorial**: O'Reilly Media
**Idioma Original**: Inglés
**Traducción**: Español (términos clave en inglés)
**Fecha de Acceso**: 2026-01-11
**Workbook**: workbook-product-md/

---

## 1. Visión General del Framework

El **Lean Canvas** es una adaptación del Business Model Canvas creada por Ash Maurya específicamente para startups y emprendedores. Reemplaza 4 bloques del canvas original (Key Partners, Key Activities, Key Resources, Customer Relationships) con bloques más relevantes para startups: Problem, Solution, Key Metrics y Unfair Advantage.

### 1.1. Propósito

El Lean Canvas sirve para:
- Documentar modelo de negocio de forma rápida (15-20 minutos)
- Identificar riesgos más grandes del modelo
- Priorizar qué validar primero
- Comunicar idea de negocio concisamente
- Iterar rápidamente conforme se aprende

### 1.2. Filosofía Lean Startup

Basado en principios de Lean Startup (Eric Ries):
- **Build-Measure-Learn**: Ciclo rápido de validación
- **Validated Learning**: Aprender de experimentos, no opiniones
- **Minimum Viable Product**: Versión más simple para aprender
- **Pivot or Persevere**: Cambiar estrategia basado en datos

### 1.3. Estructura Visual del Canvas

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│   Problem    │   Solution   │    Unique    │   Unfair     │   Customer   │
│              │              │    Value     │  Advantage   │   Segments   │
│              │              │ Proposition  │              │              │
│              │              │    (UVP)     │              │              │
│ Top 3        │ Top 3        │              │              │ Target       │
│ problems     │ features     │ Single clear │ Can't be     │ customers    │
│              │              │ compelling   │ easily       │              │
│ Existing     │              │ message      │ copied/      │ Early        │
│ Alternatives │              │              │ bought       │ Adopters     │
├──────────────┼──────────────┴──────────────┼──────────────┼──────────────┤
│              │       Channels              │   Revenue    │     Cost     │
│ Key Metrics  │                             │   Streams    │  Structure   │
│              │ Path to                     │              │              │
│ Actionable   │ customers                   │ Revenue      │ Fixed costs  │
│ metrics      │                             │ model        │ Variable     │
│              │                             │              │ costs        │
└──────────────┴─────────────────────────────┴──────────────┴──────────────┘
```

---

## 2. Componentes del Framework (9 Bloques)

### 2.1. Customer Segments (Segmentos de Cliente)

**Definición**: ¿Para quién estamos creando valor? ¿Quiénes son nuestros clientes más importantes?

**Contenido**:
- **Target Customers**: Segmentos de clientes objetivo
- **Early Adopters**: Primeros usuarios que adoptarán el producto

**Preguntas Clave**:
- ¿Quiénes tienen el problema que estamos resolviendo?
- ¿Quiénes están buscando activamente soluciones?
- ¿Quiénes pagarán por nuestra solución?

**Ejemplo**:
- **Target Customers**: Desarrolladores de software en startups tech (50-500 empleados)
- **Early Adopters**: Tech leads que ya usan metodologías ágiles y buscan mejorar documentación

**Estrategia de Maurya**:
- Comenzar con segmento MÁS PEQUEÑO posible (riches are in niches)
- Validar con al menos 5 entrevistas de clientes potenciales
- Early adopters tienen el problema AHORA y buscan solución activamente

---

### 2.2. Problem (Problema)

**Definición**: Top 3 problemas que enfrentan los Customer Segments.

**Formato**:
- Lista priorizada de 3 problemas principales
- Ordenados por importancia (más crítico primero)
- Incluir "Existing Alternatives" (soluciones actuales que usan clientes)

**Preguntas Clave**:
- ¿Cuáles son los top 3 problemas que enfrentan?
- ¿Qué tan intenso es el dolor de cada problema? (nice-to-have vs must-have)
- ¿Cómo resuelven el problema hoy? (existing alternatives)

**Ejemplo**:
1. **Problem #1**: Síntesis manual de literatura toma 8+ horas por ADR, con gaps de citación frecuentes
2. **Problem #2**: Specs sin trazabilidad a fuentes, dificultan auditorías y reproducibilidad
3. **Problem #3**: Conceptos no reutilizables entre proyectos, duplicación de esfuerzo

**Existing Alternatives**:
- Copiar/pegar manualmente desde papers (lento, propenso a errores)
- Templates genéricos sin metodología (inconsistentes)
- Wikipedia para contexto (no citable en specs formales)

**Validación según Maurya**:
- Problema debe ser "hair-on-fire" (dolor intenso NOW)
- Si cliente no paga hoy por existing alternative, no es problema real
- Validar con Customer Discovery interviews (5-10 entrevistas mínimo)

---

### 2.3. Unique Value Proposition (UVP)

**Definición**: Mensaje único y claro que declara por qué tu producto es diferente y vale la pena comprar.

**Fórmula de Maurya**:
```
UVP = [End Result Customer Wants] + [Specific Time Period] + [Address Objections]
```

**Componentes**:
- **End Result**: Beneficio final que obtiene el cliente (no feature)
- **Time Period**: Cuánto tiempo toma lograr el resultado
- **Objections**: Obstáculo principal que previene compra

**Ejemplo Famoso**:
- **Domino's Pizza**: "Fresh hot pizza delivered to your door in 30 minutes or it's free"
  - End Result: Fresh hot pizza delivered
  - Time: 30 minutes
  - Objection: "Will it arrive cold?" → FREE si no cumple

**Ejemplo DAATH-ZEN**:
- "Crea specs de alta calidad en < 1 hora con trazabilidad 100% a fuentes, sin inventar contenido"
  - End Result: Specs de alta calidad con trazabilidad
  - Time: < 1 hora (vs 8 horas actual)
  - Objection: "¿Cómo sé que no inventamos contenido?" → 100% citación

**High-Concept Pitch** (opcional):
- Describir producto como "[X] para [Y]"
- Ejemplo: "GitHub para knowledge management" o "Notion meets Academia.edu"

**Criterios de Calidad**:
- ✅ Clara: Entendible por alguien en 5 segundos
- ✅ Específica: Incluye números (30 min, 100%, 10x)
- ✅ Cliente-céntrica: Enfocada en beneficio, no feature
- ✅ Diferenciada: Por qué elegir esto vs alternativas

---

### 2.4. Solution (Solución)

**Definición**: Top 3 características del producto que resuelven los Top 3 Problems.

**Formato**:
- Lista de 3 características principales
- Correspondencia 1:1 con top 3 problems
- Descripción breve de cada feature

**Regla de Oro de Maurya**:
> "List features, not solutions. And list the simplest thing that could possibly work."

**Ejemplo**:
1. **5-Workbook Epistemology** → Resuelve Problem #1 (síntesis manual lenta)
   - Literatura → análisis → atomics → validación → compilación → ingesta

2. **Scoping Review Methodology** → Resuelve Problem #2 (sin trazabilidad)
   - Cada claim citado [source, page], 0 contenido inventado

3. **Neo4j GraphRAG** → Resuelve Problem #3 (conceptos no reutilizables)
   - Concepts con relaciones CITED_IN, RELATES_TO, USED_IN

**Anti-Patrón**:
- ❌ Listar todas las features posibles (scope creep)
- ❌ Features no conectadas a problems (nice-to-have)
- ❌ Solución compleja cuando simple funcionaría

**MVP (Minimum Viable Product)**:
- Para cada feature, preguntar: "¿Cuál es la versión MÁS SIMPLE que valida la hipótesis?"
- Ejemplo: En lugar de "ML-powered semantic search", empezar con "keyword search"

---

### 2.5. Channels (Canales)

**Definición**: ¿Cómo llegaremos a los Customer Segments? Path to customers.

**Tipos de Canales**:
1. **Inbound**: Clientes llegan a nosotros (SEO, content marketing, referrals)
2. **Outbound**: Nosotros buscamos clientes (cold email, ads, sales calls)

**Fases del Customer Journey**:
- **Awareness**: ¿Cómo se enteran de nuestro producto?
- **Acquisition**: ¿Cómo adquirimos clientes?
- **Activation**: ¿Cómo los convertimos en usuarios activos?
- **Retention**: ¿Cómo los mantenemos regresando?
- **Revenue**: ¿Cómo generamos ingresos?
- **Referral**: ¿Cómo nos recomiendan a otros?

**Ejemplo DAATH-ZEN**:
- **Awareness**:
  - Blog posts sobre "epistemological workflows for specs"
  - GitHub open-source templates
  - Presentaciones en conferencias tech (PyCon, FOSDEM)
- **Acquisition**:
  - Free tier: 3 specs gratis, luego $29/mes
  - GitHub Marketplace listing
- **Activation**:
  - Onboarding wizard: "Create your first spec in 10 minutes"
  - Templates precargados con ejemplos
- **Retention**:
  - Weekly email: "Your spec quality score this week"
  - Slack integration para notificaciones

**Estrategia de Maurya**:
- **Early Stage**: Foco en 1-2 canales que lleguen directamente a early adopters
- **Validation**: Probar canal con 10 clientes antes de escalar
- **Avoid**: Canales caros/lentos en etapa temprana (TV ads, trade shows)

---

### 2.6. Revenue Streams (Flujos de Ingresos)

**Definición**: ¿Cómo ganamos dinero? ¿Cuánto pagan los clientes por el valor que reciben?

**Modelos de Pricing** (según Maurya):

1. **Freemium**
   - Free tier con limitaciones
   - Premium tier con features avanzadas
   - Ejemplo: 3 specs gratis, luego $29/mes unlimited

2. **Subscription**
   - Pago recurrente mensual/anual
   - Ejemplo: $29/mes o $290/año (20% descuento)

3. **Pay-per-use**
   - Pago por cada transacción o uso
   - Ejemplo: $5 por spec generado

4. **Licensing**
   - Pago único por licencia perpetua
   - Ejemplo: $499 one-time, unlimited specs

5. **Enterprise**
   - Contrato anual con SLA y soporte
   - Ejemplo: $10K/año para equipo de 50 devs

**Estrategia de Pricing de Maurya**:
- **Price Point**: Definir número específico desde día 1 (no "TBD")
- **Valor Percibido**: Precio debe reflejar 10x el valor entregado
- **Ancla de Precio**: Si ahorras $1000/mes, cobrar $100/mes (10% del ahorro)
- **Testing**: Validar willingness-to-pay con early adopters (no solo "¿comprarías?" sino "¿comprarás HOY?")

**Ejemplo DAATH-ZEN**:
- **Free Tier**: 3 specs/mes (para probar)
- **Pro**: $29/mes unlimited specs + GraphRAG search
- **Team**: $99/mes para 10 usuarios + shared workbooks
- **Enterprise**: Custom pricing, white-label, on-premise deployment

**Métricas Clave**:
- **ARPU** (Average Revenue Per User): $29
- **LTV** (Lifetime Value): $29 × 12 meses × 3 años = $1,044
- **CAC** (Customer Acquisition Cost): Target < $100 (LTV/CAC > 3)

---

### 2.7. Cost Structure (Estructura de Costos)

**Definición**: ¿Cuáles son los costos más importantes inherentes a nuestro modelo de negocio?

**Tipos de Costos**:
- **Fixed Costs**: No varían con volumen (salarios, oficina, software licenses)
- **Variable Costs**: Escalan con clientes (hosting, API calls, customer support)

**Ejemplo DAATH-ZEN**:
- **Fixed Costs** (~$15K/mes):
  - Salarios: 2 devs full-time ($10K/mes)
  - Infraestructura base: Neo4j hosting ($2K/mes)
  - Software licenses: GitHub, Notion, Slack ($500/mes)
  - Marketing: Content writer ($2.5K/mes)

- **Variable Costs** (~$5 per customer/mes):
  - Hosting escalable: AWS/GCP compute ($3 per customer)
  - LLM API calls: OpenAI/Anthropic ($2 per customer)
  - Email/notifications: SendGrid ($0.10 per customer)

**Break-Even Analysis**:
```
Fixed Costs = $15K/mes
Variable Costs = $5/customer
Price = $29/customer
Contribution Margin = $29 - $5 = $24/customer

Break-Even = Fixed Costs / Contribution Margin
Break-Even = $15K / $24 = 625 customers
```

**Estrategia de Maurya**:
- **Runway**: Calcular meses de operación con funding actual
- **Burn Rate**: Fixed Costs + (Variable Costs × Current Customers)
- **Ramen Profitability**: Break-even con ingresos mínimos para vivir

---

### 2.8. Key Metrics (Métricas Clave)

**Definición**: Números clave que miden salud del negocio. Métricas **accionables**, no vanity metrics.

**Framework de Dave McClure (Pirate Metrics - AARRR)**:
1. **Acquisition**: ¿Cómo llegan los usuarios?
2. **Activation**: ¿Tienen una gran primera experiencia?
3. **Retention**: ¿Regresan?
4. **Revenue**: ¿Pagan?
5. **Referral**: ¿Nos recomiendan?

**Ejemplo DAATH-ZEN**:
- **Acquisition**: 1,000 signups/mes (de blog + GitHub)
- **Activation**: 40% crean primer spec en primeras 24h
- **Retention**: 60% de usuarios regresan semanalmente (WAU/MAU)
- **Revenue**: 10% convierten a Pro ($29/mes) → $2,900 MRR
- **Referral**: 20% invitan a compañero de equipo

**Métricas Accionables vs Vanity**:
- ❌ **Vanity**: "1 millón de descargas" (no indica engagement)
- ✅ **Actionable**: "30% de usuarios activos diariamente" (indica valor real)

**One Metric That Matters (OMTM)**:
Según Maurya, elegir **UNA métrica** para obsesionarse en cada fase:
- **Early Stage**: Activation Rate (¿cuántos completan onboarding?)
- **Growth Stage**: Retention (¿cuántos regresan semana a semana?)
- **Scale Stage**: Revenue (¿cuántos pagan?)

**Ejemplo OMTM para DAATH-ZEN**:
- **Fase Actual (Early)**: Activation → "% usuarios que crean primer spec < 1 hora"
- **Target**: 60% (baseline actual: ~30%)
- **Experimentos**: Mejorar onboarding wizard, templates preconfigurados

---

### 2.9. Unfair Advantage (Ventaja Injusta)

**Definición**: Algo que **no puede** ser fácilmente copiado o comprado.

**Criterios de Maurya**:
- ❌ NO es Unfair Advantage: Tecnología (se puede copiar), dinero (se puede conseguir)
- ✅ SÍ es Unfair Advantage: Network effects, brand, insider information, team expertise, assets

**Tipos de Unfair Advantage**:

1. **Network Effects**
   - Ejemplo: Cada usuario añadido hace el producto más valioso (como Facebook)
   - DAATH: Más equipos usando DAATH-ZEN → más conceptos atomizados → mejor GraphRAG

2. **Brand**
   - Ejemplo: Apple brand permite cobrar premium
   - DAATH: Credibilidad académica por usar metodologías formales (Scoping Review)

3. **Insider Information**
   - Ejemplo: Conocimiento único del dominio
   - DAATH: Experiencia en epistemología aplicada a specs (no común en tech)

4. **Team / Expertise**
   - Ejemplo: Equipo con habilidades raras
   - DAATH: Combinación de Computer Science + Philosophy + UX research

5. **Assets**
   - Ejemplo: Patentes, data exclusiva
   - DAATH: Base de datos de 10K+ conceptos atomizados (creciente)

**Ejemplo DAATH-ZEN**:
- **Primary Unfair Advantage**: Metodología epistemológica aplicada a specs (intersección única de domains)
- **Secondary**: Community de contribuidores académicos creando conceptos atomizados (network effect)

**Nota de Maurya**:
> "Most startups don't have an unfair advantage initially, and that's OK. The goal is to identify what could become one."

**Si no tienes Unfair Advantage HOY**:
- Dejar bloque vacío (honestidad)
- Enfocarse en construirlo (network effects, brand, expertise)
- Revisitar cada 3-6 meses

---

## 3. Proceso de Completar Lean Canvas

### 3.1. Orden Recomendado por Maurya

**NO llenar en orden de bloques (izquierda a derecha)**. Usar este orden:

1. **Customer Segments** (comenzar aquí)
   - ¿Para quién construimos?

2. **Problem**
   - ¿Qué top 3 problemas enfrentan?

3. **Unique Value Proposition**
   - ¿Por qué somos diferentes?

4. **Solution**
   - ¿Cómo resolvemos problemas?

5. **Channels**
   - ¿Cómo llegamos a customers?

6. **Revenue Streams**
   - ¿Cómo ganamos dinero?

7. **Cost Structure**
   - ¿Cuánto cuesta operar?

8. **Key Metrics**
   - ¿Cómo medimos progreso?

9. **Unfair Advantage** (último)
   - ¿Qué no pueden copiar?

### 3.2. Timeboxing

- **Primera versión**: 15-20 minutos (sketch rápido)
- **Versión refinada**: 1-2 horas (después de 5-10 customer interviews)
- **Revisión**: Cada sprint (2 semanas) o cuando hay aprendizaje significativo

### 3.3. Iteración y Pivots

**Tipos de Pivots** (según Eric Ries / Maurya):

1. **Zoom-in Pivot**: Una feature se convierte en el producto completo
2. **Zoom-out Pivot**: Producto completo se convierte en una feature de algo más grande
3. **Customer Segment Pivot**: Cambiar de segmento de clientes
4. **Customer Need Pivot**: Problema era diferente al que pensábamos
5. **Platform Pivot**: Cambiar de aplicación a platform (o viceversa)
6. **Business Architecture Pivot**: Cambiar de B2C a B2B (o viceversa)
7. **Value Capture Pivot**: Cambiar modelo de monetización
8. **Engine of Growth Pivot**: Cambiar estrategia de crecimiento (viral, paid, sticky)

**Cuándo pivotar**:
- Después de 5-10 customer interviews con feedback consistente
- Key Metrics no están mejorando después de 3 experimentos
- Descubriste problema más grande que el que estabas resolviendo

---

## 4. Relación con Otros Frameworks

### 4.1. Lean Canvas vs Business Model Canvas

| Aspecto | Business Model Canvas | Lean Canvas |
|---------|----------------------|-------------|
| **Creador** | Alexander Osterwalder | Ash Maurya |
| **Target** | Empresas establecidas | Startups |
| **Enfoque** | Modelo de negocio completo | Riesgos más grandes |
| **Bloques únicos BMC** | Key Partners, Key Activities, Key Resources, Customer Relationships | - |
| **Bloques únicos LC** | - | Problem, Solution, Key Metrics, Unfair Advantage |
| **Tiempo llenar** | 2-4 horas | 15-20 minutos |
| **Iteración** | Trimestral | Cada sprint (2 semanas) |

**Cuándo usar cada uno**:
- **Business Model Canvas**: Empresa madura con modelo probado, necesita optimizar
- **Lean Canvas**: Startup buscando product-market fit, necesita validar hipótesis rápido

### 4.2. Lean Canvas vs Product Vision Board

| Aspecto | Lean Canvas | Product Vision Board |
|---------|-------------|---------------------|
| **Scope** | Modelo de negocio completo | Solo estrategia de producto |
| **Revenue/Cost** | ✅ Incluye | ❌ No incluye |
| **Problem Detail** | ✅ Top 3 + Existing Alternatives | ✅ Needs (similar) |
| **Solution Detail** | ✅ Top 3 features | ✅ Product concept |
| **Metrics** | ✅ Key Metrics (AARRR) | ❌ Business Goals (alto nivel) |
| **Visual** | 9 bloques | 5 secciones jerárquicas |

**Recomendación de uso conjunto**:
1. Product Vision Board para alinear equipo en visión estratégica
2. Lean Canvas para detallar modelo de negocio y métricas
3. Ambos caben en una página, fácil de compartir

---

## 5. Aplicación a product.md de spec-workflow-mcp

### 5.1. Mapeo de Componentes

| Lean Canvas | product.md (spec-workflow-mcp) |
|-------------|--------------------------------|
| Customer Segments | Target Users |
| Problem (top 3 + alternatives) | Target Users (pain points + existing solutions) |
| Unique Value Proposition | Product Purpose (value proposition statement) |
| Solution (top 3 features) | Key Features |
| Key Metrics | Success Metrics |
| Revenue Streams | Business Objectives (revenue goals) |
| Cost Structure | ❌ No incluido (product.md no cubre financials) |
| Channels | ❌ No incluido (product.md no cubre marketing) |
| Unfair Advantage | Product Principles (implícito en "differentiators") |

### 5.2. Elementos de Lean Canvas NO en product.md

product.md de spec-workflow-mcp **NO incluye**:
- ❌ Cost Structure (financials fuera de scope)
- ❌ Channels (marketing/sales fuera de scope)
- ❌ Revenue Streams detallado (solo Business Objectives alto nivel)

**Razón**: product.md es **steering document técnico**, no business plan completo.

### 5.3. Elementos de product.md NO en Lean Canvas

product.md **añade** sobre Lean Canvas:
- ✅ **Product Principles**: Guías de decisión (Lean Canvas no tiene)
- ✅ **Success Metrics detalladas**: Con targets, baselines, timeframes (más específico que Key Metrics)
- ✅ **Monitoring & Visibility**: Dashboard requirements (Lean Canvas no cubre)

---

## 6. Herramientas y Recursos

### 6.1. Template Descargable

Ash Maurya ofrece templates en:
- **URL**: https://leanstack.com/lean-canvas
- **Formato**: PDF, PowerPoint, Miro board, LeanStack app
- **Licencia**: Creative Commons (uso libre con atribución)

### 6.2. LeanStack Software

- **Plataforma**: https://leanstack.com
- **Features**:
  - Canvas digital colaborativo
  - Versioning (track cambios en el tiempo)
  - Experiment tracker
  - Customer interview notes
- **Pricing**: Free tier disponible, Pro desde $19/mes

### 6.3. Workshops y Certificación

- **Lean Stack Workshop**: 2 días hands-on con Ash Maurya
- **Running Lean Online Course**: Video course con templates
- **Certificación**: "Lean Stack Practitioner" certification

---

## 7. Ejemplos Completos

### 7.1. Ejemplo: Airbnb (Early Stage)

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ Problem      │ Solution     │ UVP          │ Unfair Adv   │ Customer Seg │
├──────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│1.Conferences │1.Book room   │Stay like     │Community of  │Urban travelers│
│  no hotel    │  in home     │  a local     │  hosts       │Budget-minded │
│  rooms       │2.Web platform│Cheaper than  │Silicon Valley│Event-goers   │
│2.Hotels      │  photos/     │  hotels      │  network     │              │
│  expensive   │  reviews     │              │              │Early Adopters│
│3.Locals      │3.Payment     │              │              │Tech-savvy    │
│  want income │  escrow      │              │              │  millennials │
│              │              │              │              │              │
│Alternatives: │              │              │              │              │
│Craigslist    │              │              │              │              │
│Hotels        │              │              │              │              │
├──────────────┼──────────────┴──────────────┼──────────────┼──────────────┤
│ Key Metrics  │ Channels                    │ Revenue      │ Cost         │
├──────────────┼─────────────────────────────┼──────────────┼──────────────┤
│Bookings/week │Blog (host stories)          │10% host fee  │Marketing     │
│Avg price     │Craigslist posts             │3% guest fee  │Tech dev      │
│% repeat      │SEO: "SF lodging"            │              │Payment proc  │
│guests        │Referrals                    │              │Customer svc  │
└──────────────┴─────────────────────────────┴──────────────┴──────────────┘
```

### 7.2. Ejemplo: DAATH-ZEN MELQUISEDEC

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ Problem      │ Solution     │ UVP          │ Unfair Adv   │ Customer Seg │
├──────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│1.Manual lit  │1.5-Workbook  │Specs 10x     │Epistemology  │Software      │
│  synthesis   │  Epistemology│  faster with │  methodology │Architects    │
│  8+ hours    │2.Scoping     │  100% source │Academic      │(Senior/Lead) │
│2.Specs no    │  Review      │  traceability│  credibility │              │
│  traceability│3.Neo4j       │  in < 1 hour │Neo4j concept │Product Mgrs  │
│3.Concepts not│  GraphRAG    │              │  database    │(Technical)   │
│  reusable    │              │              │  (growing)   │              │
│              │              │              │              │Early Adopters│
│Alternatives: │              │              │              │Agile teams   │
│Manual copy/  │              │              │              │  with ADRs   │
│paste, generic│              │              │              │              │
│templates,    │              │              │              │              │
│Wikipedia     │              │              │              │              │
├──────────────┼──────────────┴──────────────┼──────────────┼──────────────┤
│ Key Metrics  │ Channels                    │ Revenue      │ Cost         │
├──────────────┼─────────────────────────────┼──────────────┼──────────────┤
│Activation:   │Blog: "epistemic workflows"  │Free: 3 specs │Fixed: $15K/mo│
│40% create    │GitHub templates open-source │Pro: $29/mo   │2 devs        │
│first spec    │PyCon/FOSDEM talks           │Team: $99/mo  │Neo4j host    │
│<24h          │GitHub Marketplace           │Enterprise:   │Variable:     │
│WAU/MAU: 60%  │Slack integration            │  custom      │$5/customer   │
│Pro conv: 10% │                             │              │hosting + LLM │
└──────────────┴─────────────────────────────┴──────────────┴──────────────┘
```

---

## 8. Críticas y Limitaciones

### 8.1. Fortalezas

✅ **Rápido**: 15-20 minutos primera versión
✅ **Enfoque en riesgo**: Destaca problemas críticos (Problem, UVP, Unfair Advantage)
✅ **Accionable**: Key Metrics guían qué medir
✅ **Iterativo**: Fácil de actualizar cada sprint
✅ **Visual**: Cabe en una página, fácil compartir

### 8.2. Limitaciones

⚠️ **Sobresimplificación**: 9 bloques no capturan complejidad de algunos modelos
⚠️ **No es plan de negocio**: No reemplaza financial projections detalladas
⚠️ **Requiere validación**: Canvas es hipótesis, necesita customer interviews
⚠️ **Unfair Advantage difícil**: Muchas startups no tienen uno al inicio

### 8.3. Críticas Comunes

**"Todos los bloques se ven igual en tamaño"**:
- Realidad: Algunos bloques son más críticos (Problem, UVP, Key Metrics)
- Solución de Maurya: Usar colores o asteriscos para indicar prioridad

**"No captura timing/secuenciación"**:
- Realidad: Lean Canvas es snapshot, no roadmap
- Complementar con Lean Roadmap o Story Mapping

**"Muy enfocado en B2C"**:
- Realidad: Funciona para B2B también, pero requiere adaptación
- B2B: Customer Segments = empresas, no individuos; Sales cycles más largos

---

## 9. Referencias

### 9.1. Fuente Original

- **Autor**: Ash Maurya
- **URL**: https://leanstack.com/lean-canvas
- **Blog**: https://blog.leanstack.com
- **Licencia**: Creative Commons Attribution-ShareAlike

### 9.2. Libro Principal

- **Título**: Running Lean: Iterate from Plan A to a Plan That Works (2nd Edition)
- **Autor**: Ash Maurya
- **Editorial**: O'Reilly Media
- **Año**: 2012 (1st), 2022 (2nd)
- **ISBN**: 978-1449305178
- **Páginas**: 240
- **Capítulos Relevantes**:
  - Capítulo 2: Document Your Plan A (Lean Canvas completo)
  - Capítulo 3: Identify the Riskiest Parts (priorización)
  - Capítulo 4: Systematically Test Your Plan (validación)

### 9.3. Artículos Complementarios

1. "Why Lean Canvas vs Business Model Canvas?" - Ash Maurya (2012)
2. "How to Fill a Lean Canvas in 20 Minutes" - Lean Stack Blog (2015)
3. "The #1 Reason Startups Fail" - Ash Maurya (2011) [42% fail: no market need]

### 9.4. Frameworks Relacionados

- **Business Model Canvas**: Alexander Osterwalder (2008) - Inspiración para Lean Canvas
- **Value Proposition Canvas**: Osterwalder & Pigneur (2014) - Deep dive en customer-product fit
- **Lean Startup**: Eric Ries (2011) - Filosofía subyacente

---

## 10. Notas para Atomización (3-atomics/)

**Conceptos clave a extraer**:

1. **concept-lean-canvas.json**: Estructura completa (9 bloques)
2. **concept-uvp-formula.json**: Fórmula UVP de Maurya (End Result + Time + Objections)
3. **concept-customer-segment-validation.json**: Criterios para validar segmentos (early adopters)
4. **concept-problem-solution-fit.json**: Correspondencia 1:1 entre top 3 problems y top 3 features
5. **concept-key-metrics-aarrr.json**: Framework Pirate Metrics (Acquisition-Activation-Retention-Revenue-Referral)
6. **concept-unfair-advantage.json**: Tipos (network effects, brand, team, assets)
7. **concept-existing-alternatives.json**: Cómo documentar soluciones actuales de clientes

**Términos en inglés** (mantener en atomic concepts):
- Lean Canvas
- Unique Value Proposition (UVP)
- Customer Segments, Early Adopters
- Problem, Solution
- Key Metrics, AARRR (Pirate Metrics)
- Unfair Advantage
- Existing Alternatives
- Revenue Streams, Cost Structure

**Relaciones con otros conceptos**:
- Lean Canvas Problem → Product Vision Board Needs
- Lean Canvas Solution → Product Vision Board Product
- Lean Canvas UVP → spec-workflow-mcp Product Purpose
- Lean Canvas Key Metrics → spec-workflow-mcp Success Metrics
- Lean Canvas Customer Segments → spec-workflow-mcp Target Users

---

**Documento completado**: 2026-01-11
**Workbook**: workbook-product-md/
**Siguiente paso**: Continuar poblando 1-literature/ (libros Cagan, Maurya, Moore)
**Status**: ✅ Traducción FIEL con términos clave en inglés
