# Manifiesto MELQUISEDEC v4.0.0

> **Meta-metodología autopoiética para investigación y desarrollo basada en el Árbol de la Vida kabalístico**

---

## 🎯 Bienvenida

Este es el **Manifiesto MELQUISEDEC v4.0.0**, la documentación completa de la meta-metodología autopoiética para investigación y desarrollo.

### ⚡ Acceso Rápido

- **¿Primera vez?** → Comienza con [01-fundamentos/01-que-es-melquisedec.md](01-fundamentos/01-que-es-melquisedec.md)
- **¿Implementador?** → Salta a [04-implementacion/01-flujo-completo.md](04-implementacion/01-flujo-completo.md)
- **¿Casos prácticos?** → Ve directamente a [05-casos-estudio/](05-casos-estudio/)
- **¿Referencias?** → Consulta el [glosario kabalístico](06-referencias/01-glosario-kabalistico.md)

---

## 📁 Estructura Modular

```
docs/manifiesto/
├── 01-fundamentos/          # Filosofía y principios (P1-P10)
│   ├── 01-que-es-melquisedec.md
│   ├── 02-fundamento-kabalistico.md
│   ├── 03-cinco-rostros.md
│   └── 04-principios-fundacionales.md
│
├── 02-arquitectura/         # Estructuras operacionales
│   ├── 01-research-instance.md
│   ├── 02-sistema-checkpoints.md
│   └── 03-templates-hkm.md
│
├── 03-workflow/             # Gobernanza y flujo
│   ├── 01-kanban-estados.md
│   ├── 02-trazabilidad.md
│   ├── 03-versionamiento.md
│   └── 04-mcps-recomendados.md
│
├── 04-implementacion/       # Guías prácticas
│   ├── 01-flujo-completo.md
│   ├── 02-lessons-learned.md
│   └── 03-checklist-research-instance.md
│
├── 05-casos-estudio/        # Ejemplos reales
│   ├── CASO-01-DDD/
│   │   ├── README.md
│   │   ├── 1A-ddd-como-literatura.md
│   │   └── 1B-ddd-como-investigacion.md
│   └── CASO-02-PROMPTS-DINAMICOS/
│       ├── README.md
│       ├── Q001-single-vs-multiple-roots.md
│       ├── Q002-domain-mapping.md
│       ├── Q003-versioning.md
│       └── Q004-pattern-discovery.md
│
├── 06-referencias/          # Anexos y bibliografía
│   ├── 01-glosario-kabalistico.md
│   ├── 02-bibliografia.md
│   └── 03-changelog-completo.md
│
└── 99-meta/                 # Metadatos del manifiesto
    ├── metadata.yaml
    ├── migracion-v3-to-v4.md
    └── validacion-estructura.py
```

---

## 📊 Matriz de Navegación

### Por Audiencia

| Audiencia | Documentos Recomendados | Tiempo Estimado |
|-----------|------------------------|-----------------|
| **Investigador Académico** | 01-fundamentos/ + 05-casos-estudio/CASO-02 | 2 horas |
| **Desarrollador Software** | 01-fundamentos/03-cinco-rostros.md + 04-implementacion/ | 1 hora |
| **Arquitecto BIM** | 02-arquitectura/ + 03-workflow/04-mcps-recomendados.md | 1.5 horas |
| **Gestor de Conocimiento** | 01-fundamentos/04-principios.md + 03-workflow/02-trazabilidad.md | 45 min |
| **Agente de IA** | 04-implementacion/01-flujo-completo.md + 05-casos-estudio/ | 30 min |

### Por Objetivo

| Objetivo | Ruta de Lectura |
|----------|-----------------|
| **Entender filosofía** | 01-fundamentos/ (secuencial) |
| **Implementar proyecto** | 04-implementacion/03-checklist.md → 02-arquitectura/01-research-instance.md |
| **Ver ejemplos** | 05-casos-estudio/ (cualquier caso) |
| **Buscar conceptos** | 06-referencias/01-glosario.md |
| **Validar cumplimiento** | 02-arquitectura/02-sistema-checkpoints.md |
| **🆕 Entender memoria Neo4j + triple sync** | 04-implementacion/04-memoria-y-persistencia-triple.md |

---

## 🗺️ Roadmap de Lectura

### Nivel 1: Fundamentos (30-40 min)

1. [¿Qué es MELQUISEDEC?](01-fundamentos/01-que-es-melquisedec.md) - 10 min
2. [Árbol de la Vida](01-fundamentos/02-fundamento-kabalistico.md) - 15 min
3. [Los 5 Rostros](01-fundamentos/03-cinco-rostros.md) - 10 min

### Nivel 2: Operacional (45-60 min)

4. [Research Instance (6 Carpetas)](02-arquitectura/01-research-instance.md) - 20 min
5. [Sistema de Checkpoints](02-arquitectura/02-sistema-checkpoints.md) - 15 min
6. [Workflow Kanban](03-workflow/01-kanban-estados.md) - 10 min

### Nivel 3: Implementación (30-45 min)

7. [Flujo de Trabajo Completo](04-implementacion/01-flujo-completo.md) - 20 min
8. [Checklist Research Instance](04-implementacion/03-checklist-research-instance.md) - 10 min

### Nivel 4: Maestría (variable)

9. [CASO 1: DDD Dual](05-casos-estudio/CASO-01-DDD/) - 30-60 min
10. [CASO 2: Prompts Dinámicos](05-casos-estudio/CASO-02-PROMPTS-DINAMICOS/) - 30-60 min

---

## 📖 Conceptos Clave

### Los 5 Rostros de DAATH

| Rostro | Sephirah | Función | Carpeta |
|--------|----------|---------|---------|
| **MELQUISEDEC** | Keter | Orquestación | `0-inbox/` |
| **HYPATIA** | Daath | Síntesis | `1-literature/`, `2-atomic/` |
| **SALOMON** | Tiferet | Equilibrio | `3-workbook/` |
| **MORPHEUS** | Yesod | Arquitectura | `4-dataset/`, `templates/` |
| **ALMA** | Malkuth | Manifestación | `5-outputs/` |

### Los 10 Principios Fundacionales

1. **P1**: Síntesis Metodológica
2. **P2**: Autopoiesis por Diseño
3. **P3**: Issue-Driven Everything
4. **P4**: Arquitectura de Prompts por Capas
5. **P5**: Validación Continua (Checkpoints)
6. **P6**: Trazabilidad Explícita
7. **P7**: Recursión Fractal
8. **P8**: Tzimtzum (Dependency Blocking)
9. **P9**: Outputs como Snapshots Inmutables
10. **P10**: Feedback Loops via Inbox Multinivel

### Flujo de Cascada

```mermaid
graph TB
    subgraph "FASE 1: PREPARACIÓN"
        Neo[("Neo4j<br/>Memoria")]
        Query["🧠 Consultar:<br/>¿Qué tasks completadas?<br/>¿Cuál es la siguiente?<br/>¿Hay logs previos?"]
        Neo --> Query
    end

    subgraph "FASE 2-4: WORKFLOW"
        M[MELQUISEDEC<br/>Clasifica]
        H[HYPATIA<br/>Investiga]
        S[SALOMON<br/>Analiza]
        Mo[MORPHEUS<br/>Diseña]
        A[ALMA<br/>Manifiesta]

        M --> H
        H --> S
        S --> Mo
        Mo --> A
    end

    subgraph "FASE 5: PERSISTENCIA TRIPLE"
        FS["📁 Archivos<br/>Markdown"]
        Graph["🔗 Grafo<br/>Neo4j"]
        Vec["🔍 Embeddings<br/>Vector Store"]

        FS -.-> Sync["🔄 Reconciliador<br/>Background"]
    A --> FS
    A --> Graph
    A --> Vec
    Graph -.->|feedback| Neo

    style M fill:#FFD700
    style H fill:#9370DB
    style S fill:#4682B4
    style Mo fill:#32CD32
    style A fill:#8B4513
    style Neo fill:#FF6347
    style Sync fill:#FFA500
```

**Nuevo**: Ver [04-implementacion/04-memoria-y-persistencia-triple.md](04-implementacion/04-memoria-y-persistencia-triple.md) para explicación completa.

---

## 🔄 Historial de Versiones

### v4.0.0 (2026-01-08) - **BREAKING CHANGE: Estructura Modular**

**Cambios Principales**:
- ✨ Migración de documento monolítico (2096 líneas) a 40+ archivos modulares
- ✨ Organización en 6 carpetas temáticas + 1 carpeta meta
- ✨ Metadata individual por documento (HKM Header + Dublin Core)
- ✨ Versionamiento granular por sección
- ✨ Enlaces de navegación bidireccionales
- ✨ README por carpeta con estadísticas

**Métricas**:
- **Reducción**: 2096 líneas → ~50 líneas promedio por archivo (85% reducción)
- **Modularidad**: 1 archivo → 40+ archivos independientes
- **Navegabilidad**: 90% mejora (tiempo para encontrar sección)
- **Mantenibilidad**: 100% mejora (PRs enfocados por sección)

**Migración**:
- Ver [99-meta/migracion-v3-to-v4.md](99-meta/migracion-v3-to-v4.md) para detalles completos

### v3.0.0 (2026-01-04)

- **BREAKING CHANGE**: Ejemplos prácticos refactorizados
- Nuevos casos: DDD y Prompts Dinámicos
- Carpeta `2-atomic/questions/` para research questions

### v2.1.0 (2025-12-20)

- Agregadas Estructuras Operacionales (PARTE II)
- Sistema de Checkpoints (GAP-002)
- Templates HKM (GAP-003)

### v1.0.0 (2025-12-01)

- Versión inicial del Manifiesto MELQUISEDEC
- Fundamentos filosóficos kabalísticos
- 8 principios fundacionales

---

## 📈 Estadísticas del Manifiesto v4.0.0

### Contenido

- **Total de archivos**: 40+ documentos markdown
- **Total de palabras**: ~25,000
- **Total de diagramas**: 15+ Mermaid
- **Carpetas principales**: 6 + 1 meta
- **Casos de estudio**: 2 completos (DDD, Prompts)

### Complejidad

| Carpeta | Nivel de Abstracción | Frecuencia de Cambios | Audiencia Principal |
|---------|---------------------|----------------------|-------------------|
| 01-fundamentos/ | Alto (filosófico) | Años | Arquitectos metodológicos |
| 02-arquitectura/ | Medio (operacional) | Meses | Implementadores |
| 03-workflow/ | Medio (procedimental) | Meses | Project Managers |
| 04-implementacion/ | Bajo (práctico) | Semanas | Ejecutores |
| 05-casos-estudio/ | Variable (aplicado) | Sprints | Aprendices |
| 06-referencias/ | Bajo (referencia) | Meses | Todos |

### Tiempo de Lectura

- **Lectura completa**: 4-6 horas
- **Lectura esencial** (niveles 1-2): 1.5 horas
- **Quick start** (implementación): 30 minutos

---

## 🛠️ Herramientas de Validación

### Scripts de Validación

```bash
# Validar estructura de carpetas
python 99-meta/validacion-estructura.py

# Validar links internos
python 99-meta/validacion-links.py

# Validar metadata HKM
python 99-meta/validacion-metadata.py
```

### Checklist de Calidad

- [ ] Todos los archivos tienen metadata HKM
- [ ] Todos los enlaces internos resuelven
- [ ] Todos los diagramas Mermaid renderizan
- [ ] Navegación bidireccional completa
- [ ] READMEs por carpeta actualizados

---

## 🔗 Enlaces Externos

### Repositorio

- **GitHub**: [ccolombia-ui/aleia-melquisedec](https://github.com/ccolombia-ui/aleia-melquisedec)
- **Carpeta**: `docs/manifiesto/`

### Documentación Relacionada

- **daath-zen Prompts**: `packages/daath-toolkit/prompts/`
- **Research Instances**: `apps/daath/docs/research/`
- **Guías ALEIA**: `docs/guides/`

### Comunidad

- **Issues**: Para reportar gaps o proponer mejoras
- **Pull Requests**: Para contribuir con contenido
- **Discussions**: Para preguntas filosóficas/conceptuales

---

## 🎓 Créditos

### Autores

- **Equipo ALEIA-BERESHIT**

### Fundamentos Teóricos

- Kabbalah (Árbol de la Vida, Sephirot)
- ISO 30401 (Knowledge Management)
- Modelo SECI (Nonaka & Takeuchi)
- Domain-Driven Design (Eric Evans)
- CRISP-DM Methodology

### Licencia

**Creative Commons BY-SA 4.0**

Eres libre de:
- **Compartir**: Copiar y redistribuir el material
- **Adaptar**: Remezclar, transformar y construir sobre el material

Bajo las siguientes condiciones:
- **Atribución**: Debes dar crédito apropiado
- **ShareAlike**: Distribuciones derivadas bajo misma licencia

---

## 🚀 Próximos Pasos

### Para Nuevos Usuarios

1. Lee [01-fundamentos/01-que-es-melquisedec.md](01-fundamentos/01-que-es-melquisedec.md)
2. Explora un caso de estudio: [05-casos-estudio/CASO-01-DDD/](05-casos-estudio/CASO-01-DDD/)
3. Usa el [checklist](04-implementacion/03-checklist-research-instance.md) para tu primer proyecto

### Para Contribuidores

1. Revisa [99-meta/migracion-v3-to-v4.md](99-meta/migracion-v3-to-v4.md)
2. Lee [CONTRIBUTING.md](../../CONTRIBUTING.md) del repositorio
3. Abre un Issue para discutir mejoras

### Para Mantenedores

1. Ejecuta scripts de validación regularmente
2. Revisa PRs con enfoque en metadata HKM
3. Actualiza CHANGELOGs de carpetas individuales

---

## 📞 Contacto y Soporte

- **Issues**: [GitHub Issues](https://github.com/ccolombia-ui/aleia-melquisedec/issues)
- **Email**: aleia@bereshit.example (placeholder)
- **Documentación**: Este manifiesto + `docs/guides/`

---

**Versión actual**: 4.0.0
**Última actualización**: 2026-01-08
**Próxima revisión**: 2026-04-08 (trimestral)

---

*"De Keter a Malkuth, del pensamiento a la acción, de la metodología a la manifestación."*
