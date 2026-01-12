# HITO 3 - Implementation & POC Integration (PARA DUMMIES)

**Version**: 0.1.0  
**Status**: In Progress  
**Last Updated**: 2026-01-12

---

## 🎯 ¿Qué estamos haciendo?

**Analogía**: Si HITO 2 fue preparar las recetas y moldes, HITO 3 es **instalar el robot de calidad** que verifica automáticamente que cada pizza salga perfecta.

### Los 4 Productos Principales

1. **CI/CD Pipeline** (El Robot Inspector) 🤖
   - Verifica automáticamente cada cambio
   - Ejecuta 3 tipos de tests: ROBOT, SHACL, SPARQL
   - Genera reportes con badges (✅ PASS / ❌ FAIL)

2. **Validation Scripts** (Las 3 Estaciones de Control) 🔍
   - ROBOT: Verifica axiomas OWL (consistencia lógica)
   - pySHACL: Valida instancias (reglas de negocio)
   - SPARQL: Ejecuta CQs (responde preguntas)

3. **PyKEEN Experiment** (Experimento de Similitud) 🧪
   - Genera embeddings (vectores numéricos)
   - Predice relaciones (link prediction)
   - Evalúa calidad (Hits@10, Mean Rank)

4. **Documentation** (Manual del Robot) 📚
   - README-HITO3.md (esta guía)
   - Setup instructions
   - Troubleshooting guide

---

## 🍕 Analogía: La Línea de Control de Calidad

Imagina que tu pizzería ahora tiene 3 inspectores automáticos:

### Inspector 1: ROBOT (El Lógico) 🧠
- **Pregunta**: "¿La receta tiene sentido matemáticamente?"
- **Verifica**: 
  - ¿Un libro puede ser Y NO SER una revista al mismo tiempo? (disjointness)
  - ¿Si algo es Ficción, automáticamente es Categoría? (subclass inference)
  - ¿Las propiedades tienen dominio y rango correctos?
- **Resultado**: Report HTML con errores/warnings

### Inspector 2: pySHACL (El Estricto) 📋
- **Pregunta**: "¿Las pizzas cumplen las reglas del negocio?"
- **Verifica**:
  - ¿Cada Libro tiene exactamente 1 ISBN?
  - ¿Cada Préstamo tiene fecha de inicio y fin?
  - ¿Los valores son del tipo correcto (string, date, etc.)?
- **Resultado**: Lista de violaciones con ubicación exacta

### Inspector 3: SPARQL (El Funcional) ✅
- **Pregunta**: "¿El sistema responde correctamente a las preguntas?"
- **Verifica**:
  - CQ1: "¿Qué libros escribió García Márquez?" → [CienAñosDeSoledad, AmorEnTiemposDelColera]
  - CQ2: "¿Quién prestó '1984'?" → [Usuario123]
  - CQ3: "¿Cuántos préstamos activos hay?" → [2]
- **Resultado**: Pass rate (% de CQs que pasaron)

---

## 🔄 Flujo Completo (7 Pasos)

```
1. Developer hace cambio → 2. Git push → 3. GitHub Actions trigger
                                              ↓
4. CI/CD corre 3 validaciones (ROBOT + pySHACL + SPARQL)
                                              ↓
5. Genera reportes → 6. Badges actualizados → 7. Email si falla
```

**Tiempo**: ~5 minutos por ejecución (automatizado)

---

## 📦 Lo que vamos a construir

### Estructura de carpetas

```
hito-3-implementacion/
├── README-HITO3.md (esta guía)
├── ci-cd/
│   ├── .github/workflows/ontology-validation.yml (pipeline GitHub Actions)
│   └── badges/ (generated badges: validation-pass.svg)
├── validation-scripts/
│   ├── run_robot.sh (ROBOT validation)
│   ├── run_shacl.py (pySHACL validation)
│   ├── run_sparql_tests.py (CQ execution)
│   └── requirements.txt (Python deps)
├── shacl-shapes/
│   ├── concept-shapes.ttl (reglas para conceptos)
│   ├── relation-shapes.ttl (reglas para relaciones)
│   └── instance-shapes.ttl (reglas para instancias)
├── embedding-experiment/
│   ├── pykeen_config.yaml (configuración TransE)
│   ├── train_embeddings.py (script entrenamiento)
│   ├── evaluate_embeddings.py (métricas)
│   └── results/ (output: vectores, gráficos t-SNE)
└── reports/ (generated)
    ├── robot-report.html
    ├── shacl-report.txt
    ├── sparql-results.json
    └── pykeen-metrics.json
```

---

## 🚀 Cómo funciona el CI/CD

### Workflow GitHub Actions (simplificado)

```yaml
name: Ontology Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Install ROBOT (Java)
      - Install pySHACL (Python)
      - Install SPARQL engine (Apache Jena ARQ)
      
      - Run ROBOT validation
      - Run pySHACL validation
      - Run SPARQL tests
      
      - Upload reports
      - Update badges
      - Notify on failure
```

### ¿Cuándo se ejecuta?

- ✅ Cada push a feature/spec-001-implementation
- ✅ Cada pull request a main
- ✅ Manualmente desde GitHub UI
- ❌ NO se ejecuta en commits locales (solo en GitHub)

---

## 🧪 PyKEEN Embedding Experiment

### ¿Qué son embeddings?

**Analogía**: Convierte conceptos en coordenadas GPS.

- Libro → [0.8, 0.3, -0.1, 0.5, ...] (vector de 100 dimensiones)
- Autor → [0.7, 0.4, 0.0, 0.6, ...]

**Ventaja**: Puedes medir "distancia semántica":
- `distance(Libro, Autor)` = 0.2 (muy relacionados)
- `distance(Libro, Usuario)` = 0.7 (menos relacionados)

### Casos de uso

1. **Link Prediction**: "Si CienAñosDeSoledad → hasAutor → ¿?, predice GGMarquez"
2. **Semantic Search**: "Encuentra conceptos similares a 'Préstamo'"
3. **Clustering**: "Agrupa libros por temática automáticamente"

### Métricas de Evaluación

- **Hits@10**: ¿El concepto correcto está en el top 10? (target: >80%)
- **Mean Rank**: Posición promedio del correcto (target: <50)
- **MRR** (Mean Reciprocal Rank): 1/posición (target: >0.5)

---

## 📊 Checklist de Progreso

### Fase 1: Setup (2h)
- [ ] Crear estructura de carpetas
- [ ] Instalar herramientas localmente (ROBOT, pySHACL, ARQ)
- [ ] Configurar GitHub Actions secrets (si aplica)

### Fase 2: Validation Scripts (6h)
- [ ] Script ROBOT con reporte HTML
- [ ] SHACL shapes para 5 conceptos clave (Libro, Autor, Préstamo, Usuario, Categoría)
- [ ] Script pySHACL con output JSON
- [ ] Automatización SPARQL tests (5 CQs)

### Fase 3: CI/CD Pipeline (4h)
- [ ] Workflow YAML completo
- [ ] Badge generation (shields.io)
- [ ] Email notifications (GitHub Actions)
- [ ] Test ejecución en PR de prueba

### Fase 4: PyKEEN Experiment (8h)
- [ ] Config TransE model (100 dims, 500 epochs)
- [ ] Script entrenamiento con logging
- [ ] Evaluación métricas (Hits@10, MR, MRR)
- [ ] t-SNE visualization (2D plot)
- [ ] Report experiment results

### Fase 5: Documentation (2h)
- [ ] README-HITO3.md (esta guía) ✅
- [ ] Setup instructions por OS (Windows, Linux, Mac)
- [ ] Troubleshooting common errors
- [ ] Update main README status

**Total estimado**: 22 horas (~3 días)

---

## 🛠️ Herramientas y Dependencias

### ROBOT (OWL Validation)
```bash
# Install (requiere Java 11+)
wget https://github.com/ontodev/robot/releases/download/v1.9.5/robot.jar
java -jar robot.jar --version
```

### pySHACL (Constraint Validation)
```bash
pip install pyshacl rdflib
pyshacl --version
```

### Apache Jena ARQ (SPARQL Engine)
```bash
wget https://dlcdn.apache.org/jena/binaries/apache-jena-4.10.0.tar.gz
tar -xzf apache-jena-4.10.0.tar.gz
export PATH=$PATH:$(pwd)/apache-jena-4.10.0/bin
arq --version
```

### PyKEEN (Knowledge Graph Embeddings)
```bash
pip install pykeen torch
pykeen --version
```

---

## 🎓 Glosario Técnico

| Término | Definición | Analogía |
|---------|-----------|----------|
| **CI/CD** | Continuous Integration/Deployment | Robot que revisa cada cambio automáticamente |
| **ROBOT** | OWL validation tool | Inspector de lógica matemática |
| **pySHACL** | SHACL validator | Inspector de reglas de negocio |
| **SPARQL** | RDF query language | Lenguaje para preguntas a la base de datos |
| **Hits@10** | Top-10 accuracy | ¿La respuesta correcta está en las primeras 10? |
| **Mean Rank** | Average position | Posición promedio de la respuesta correcta |
| **TransE** | Translation embedding model | Modelo que aprende: Libro + hasAutor = Autor |
| **t-SNE** | Dimensionality reduction | Proyección de 100D a 2D para visualización |

---

## 🧑‍💼 Roles y Responsabilidades

### DevOps Engineer (tú, con apoyo de Copilot)
- Configurar GitHub Actions workflow
- Instalar herramientas localmente
- Debuggear fallos de CI/CD
- Mantener badges actualizados

### Ontology Engineer (equipo)
- Crear SHACL shapes rigurosos
- Validar reportes ROBOT
- Ajustar axiomas si hay inconsistencias
- Revisar false positives

### Data Scientist (equipo, opcional)
- Configurar PyKEEN hyperparameters
- Interpretar métricas de embeddings
- Generar visualizaciones
- Proponer mejoras de modelo

### Domain Expert (equipo)
- Validar que CQs representen casos reales
- Revisar violaciones SHACL (¿son errores reales?)
- Aprobar resultados de experimento

---

## ❓ FAQs - HITO 3

### 1. ¿Por qué necesitamos 3 validadores diferentes?
Cada uno verifica un aspecto distinto:
- ROBOT: Lógica (matemáticas)
- pySHACL: Reglas (negocio)
- SPARQL: Funcionalidad (casos de uso)

### 2. ¿Qué pasa si una validación falla?
- El CI/CD marca el commit como ❌ FAILED
- Se genera un reporte con el error específico
- No se puede mergear a main hasta que se arregle

### 3. ¿Puedo correr las validaciones localmente?
Sí, con los scripts en `validation-scripts/`:
```bash
./run_robot.sh
python run_shacl.py
python run_sparql_tests.py
```

### 4. ¿Qué hacer si el embedding experiment da métricas bajas?
- Aumentar epochs (500 → 1000)
- Cambiar modelo (TransE → DistMult)
- Agregar más triples de entrenamiento
- Consultar con Data Scientist

### 5. ¿Cuánto tarda el CI/CD en ejecutarse?
- ROBOT: ~30 segundos
- pySHACL: ~20 segundos
- SPARQL: ~10 segundos
- **Total**: ~1-2 minutos

### 6. ¿Dónde se guardan los reportes?
- En GitHub Actions: Artifacts tab
- Localmente: carpeta `reports/`
- En commits: badges en README.md

### 7. ¿Qué es un "embedding vector"?
Es una lista de números que representa un concepto:
```python
lib:Libro → [0.8, 0.3, -0.1, 0.5, ..., 0.2]  # 100 números
```
El modelo aprende estos números para que conceptos relacionados estén cerca.

### 8. ¿Por qué TransE y no otro modelo?
TransE es simple y rápido para POCs. Otros modelos (DistMult, ComplEx) son más precisos pero requieren más datos y tiempo.

### 9. ¿Cómo interpreto Hits@10 = 0.87?
Significa que el 87% de las veces, la respuesta correcta está en el top 10 de predicciones. Es una métrica excelente (>80%).

### 10. ¿Qué hacemos después de HITO 3?
HITO 4: Deployment & Monitoring (producción real con Biblioteca)

---

## 🔗 Referencias Cruzadas

- **HITO 1**: [README-HITO1.md](../hito-1-analisis/README-HITO1.md) - Análisis de gaps
- **HITO 2**: [README-HITO2.md](../hito-2-conceptualizacion/README-HITO2.md) - Templates y OTTR
- **Main README**: [README.md](../README.md) - Overview del proyecto
- **Guía Dummies**: [00-GUIA-PARA-DUMMIES.md](../00-GUIA-PARA-DUMMIES.md) - Analogías generales

---

## 📝 Documentos de HITO 3

1. **README-HITO3.md** (esta guía) - Overview para dummies
2. **ontology-validation.yml** - GitHub Actions workflow
3. **run_robot.sh** - Script validación ROBOT
4. **run_shacl.py** - Script validación pySHACL
5. **run_sparql_tests.py** - Automatización CQs
6. **concept-shapes.ttl** - SHACL shapes para conceptos
7. **pykeen_config.yaml** - Configuración embeddings
8. **train_embeddings.py** - Script entrenamiento PyKEEN
9. **evaluate_embeddings.py** - Métricas y visualización

---

## 🎯 Objetivos de Aprendizaje

Al completar HITO 3, habrás aprendido:

✅ Cómo configurar un pipeline CI/CD para ontologías  
✅ Diferencia entre validación OWL, SHACL y SPARQL  
✅ Cómo automatizar tests de competency questions  
✅ Qué son embeddings y cómo generarlos  
✅ Cómo interpretar métricas de link prediction  
✅ Best practices de DevOps para proyectos de ontologías

---

**¿Listo para empezar?** → Continúa con [Setup Instructions](setup-instructions.md)

**¿Te perdiste?** → Vuelve a [00-GUIA-PARA-DUMMIES.md](../00-GUIA-PARA-DUMMIES.md)
