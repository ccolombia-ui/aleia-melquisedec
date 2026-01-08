# Research App Integration v1.0.0 - Design

## Architecture Philosophy

Este spec aplica pensamiento sistémico multinivel para resolver la pregunta: **"¿Dónde vive el código en un ecosistema DAATH-ZEN?"**

### Principios Guía

1. **Separación Framework/Implementación**:
   - Framework (melquisedec) = metodología + tooling
   - Apps (bereshit, otros) = uso concreto del framework

2. **Modularidad por Propósito**:
   - `packages/` = componentes reutilizables
   - `apps/` = aplicaciones/investigaciones
   - `tools/` = scripts de desarrollo

3. **Autonomía con Coherencia**:
   - Repos independientes para investigaciones
   - Dependencia compartida en daath-toolkit
   - Guidelines comunes en documentación

---

## System Context

```mermaid
graph TD
    A[aleia-melquisedec<br/>FRAMEWORK] -->|proporciona| B[daath-toolkit]
    A -->|define| C[Metodología DAATH-ZEN]
    A -->|ofrece| D[spec-workflow]

    B -->|usado por| E[aleia-bereshit]
    B -->|usado por| F[aleia-{futuro}]

    E -->|contiene| G[apps/keter]
    E -->|contiene| H[apps/...]

    C -->|guía| E
    C -->|guía| F

    D -->|gestiona| E
    D -->|gestiona| F

    G -.posible.-> I[Package: keter-tool]
    I -.si madura.-> B

    style A fill:#e1f5ff,stroke:#0066cc,stroke-width:3px
    style B fill:#fff4e1,stroke:#ff9900,stroke-width:2px
    style G fill:#ffe1e1,stroke:#cc0000,stroke-width:2px
    style I fill:#e1ffe1,stroke:#00cc00,stroke-width:2px,stroke-dasharray: 5 5
```

**Leyenda**:
- 🔵 Framework (melquisedec): núcleo estable
- 🟠 Toolkit (daath-toolkit): herramientas compartidas
- 🔴 App bajo estudio (keter): caso concreto
- 🟢 Posible evolución: si keter madura → package

---

## Component Design

### 1. Decision Tree System

**Propósito**: Algoritmo de decisión para clasificar componentes

```python
class ComponentClassifier:
    """
    Clasifica componentes en: package, app, tool, example
    """

    def classify(self, component: Component) -> Placement:
        # Nivel 1: Propósito
        if component.is_methodology_or_tooling():
            if component.is_framework_core():
                return Placement.PACKAGES_MELQUISEDEC
            else:
                return Placement.TOOLS

        # Nivel 2: Reusabilidad
        if component.is_reusable_library():
            if component.maturity >= MaturityLevel.BETA:
                return Placement.PACKAGES_IN_ORIGIN_REPO
            else:
                return Placement.APPS_IN_ORIGIN_REPO

        # Nivel 3: Independencia
        if component.has_independent_lifecycle():
            return Placement.SEPARATE_REPO

        # Nivel 4: Naturaleza
        if component.is_research_or_application():
            if component.is_demo_or_example():
                return Placement.EXAMPLES_MELQUISEDEC
            else:
                return Placement.APPS_IN_SEPARATE_REPO

        # Default: conservador
        return Placement.APPS_IN_SEPARATE_REPO
```

**Implementación Real**: Flowchart visual en Mermaid + tabla de decisión

---

### 2. Keter Analysis Framework

**Metodología de Análisis**:

```yaml
Análisis Estructural:
  - Escanear directorio tree
  - Identificar módulos principales
  - Mapear dependencias internas

Análisis de Dependencias:
  - requirements.txt / pyproject.toml
  - Imports de terceros
  - Imports locales vs externos

Análisis de Madurez:
  - Existencia de tests
  - Coverage (si medible)
  - Documentación (docstrings, README)
  - Versionado (tags git?)

Análisis Funcional:
  - ¿Qué hace keter?
  - ¿Es standalone o depende de contexto?
  - ¿Tiene CLI, API, o es librería?

Análisis de Valor:
  - ¿Útil solo para bereshit?
  - ¿Reutilizable en otros proyectos?
  - ¿Es herramienta core o investigación específica?
```

**Output**: Scorecard multidimensional

```markdown
| Dimensión        | Score | Rationale |
|------------------|-------|-----------|
| Reusabilidad     | 7/10  | Código modular pero específico |
| Madurez          | 4/10  | Sin tests, docs mínimas |
| Independencia    | 9/10  | Pocas deps externas |
| Valor Framework  | 3/10  | No es tooling core |
| → Clasificación  | APP (mantener en bereshit) | - |
```

---

### 3. ADR-002 Structure

**Template Completo**:

```markdown
# ADR-002: Multi-Repository Architecture Strategy

## Status
Accepted

## Context
[Descripción del problema: ecosistema creciente, falta criterios]

## Decision
### Framework Repository (aleia-melquisedec)
- Contiene: metodología, tooling core, spec-workflow
- NO contiene: investigaciones específicas

### Application Repositories (aleia-*, otros)
- Contienen: investigaciones, apps específicas
- Dependen de: daath-toolkit (vía pip)
- Siguen: metodología DAATH-ZEN

### Package Evolution Path
research app → mature tool → internal package → standalone package

## Consequences
### Positive
- Separación clara framework/uso
- Escalabilidad (n repos sin acoplar framework)
- Versionado independiente

### Negative
- Complejidad de gestión multi-repo
- Necesidad de guidelines claras
- Riesgo de fragmentación sin coordinación

### Mitigation
- spec-workflow gestiona multi-repo
- Guidelines documentadas
- daath-toolkit como punto de integración

## Compliance
- Aligned with: DAATH-ZEN principles (modularity, minimalism)
- Related: ARQUITECTURA_MONOREPO.md (actualizar)
```

---

### 4. apps/ Clarification Strategy

**Propuesta**: Renombrar `apps/` → `examples/` en melquisedec

**Rationale**:
- `apps/` sugiere "aplicaciones reales"
- `examples/` sugiere "demos/plantillas"
- Más claro para nuevos contributors

**Migration**:
```powershell
# 1. Rename directory
git mv apps/ examples/

# 2. Update references
# - ARQUITECTURA_MONOREPO.md
# - README.md
# - .gitignore (si tiene apps/ específico)

# 3. Update examples/README.md
# Clarificar: "Esta carpeta contiene templates y ejemplos de referencia"

# 4. Keep 00-template/ (ahora examples/00-template/)
```

**Alternative**: Mantener `apps/` pero README explícito:
```markdown
# apps/

⚠️ **Nota**: Esta carpeta NO es para investigaciones de producción.

Contenido:
- `00-template/`: Plantilla base para nuevos repos de investigación
- Futuros ejemplos de referencia

**Para investigaciones reales**: Crear repo separado usando el template.
```

---

### 5. New Research Repo Template

**Generación Automática**:

```python
# packages/daath-toolkit/generators/new_research_repo.py

def create_research_repo(name: str, purpose: str):
    """
    Crea nuevo repo de investigación con estructura DAATH-ZEN

    Args:
        name: Nombre del proyecto (ej: "cognitive-architectures")
        purpose: Descripción breve del propósito
    """
    repo_name = f"aleia-{name}"

    # 1. Clonar template structure
    copy_tree(TEMPLATE_PATH, repo_name)

    # 2. Personalizar archivos
    render_template("README.md", {
        "project_name": name,
        "purpose": purpose,
        "daath_version": get_daath_version()
    })

    # 3. Inicializar git
    subprocess.run(["git", "init"], cwd=repo_name)

    # 4. Instalar dependencies
    create_pyproject_toml(repo_name, name, purpose)

    # 5. Setup pre-commit
    copy_file("templates/.pre-commit-config.yaml",
              f"{repo_name}/.pre-commit-config.yaml")

    print(f"✅ Repo {repo_name} creado exitosamente")
    print(f"📍 Ubicación: ./{repo_name}")
    print(f"🚀 Next steps:")
    print(f"   cd {repo_name}")
    print(f"   pip install -e .")
    print(f"   pre-commit install")
```

**Contenido del Template**:
- Ver REQ-5 en requirements.md para estructura completa
- Pre-configurado con:
  - pyproject.toml con daath-toolkit dependency
  - GitHub Actions para tests
  - Pre-commit hooks
  - README con badge "DAATH-ZEN powered"

---

### 6. Multi-Repo Spec Workflow

**Convenciones de Tracking**:

```markdown
# En spec header (requirements.md)

## Repositories Affected
- 🏠 Primary: aleia-melquisedec (spec location)
- 🔗 Secondary: aleia-bereshit (implementation work)

## Cross-Repository Tracking
Use tags: `[REPO:bereshit]` en logs de implementación

Ejemplo:
```
[REPO:bereshit] Analyzed keter structure
[REPO:bereshit] Commit: abc123 - Added keter analysis
[REPO:melquisedec] Updated ADR-002 based on keter findings
```
```

**Directorio de Implementación Logs**:
```
.spec-workflow/specs/research-app-integration-v1.0.0/
├── requirements.md
├── design.md
├── tasks.md
└── Implementation Logs/
    ├── YYYY-MM-DD-session-01.md
    ├── YYYY-MM-DD-session-02.md
    └── analysis/
        ├── keter-evaluation.md      ← puede referenciar bereshit
        └── keter-decision.md
```

---

### 7. Keter Evaluation Process

**Sin acceso directo al código** (fuera del workspace), tenemos 2 opciones:

**Opción A: User-Provided Info**
```markdown
# Template para usuario
Por favor proporciona:
1. Estructura de directorios (tree output)
2. requirements.txt o pyproject.toml
3. README o descripción del propósito
4. Ejemplo de código principal
```

**Opción B: MCP Tool Access** (si disponible)
```python
# Usar mcp_filesystem_read_text_file si se puede activar
# para repo externo
```

**Opción C: Manual Inspection**
```markdown
# Documento estructurado de análisis manual
El usuario navega keter y responde cuestionario guiado
```

**Para este spec**: Documentamos el PROCESO, no requerimos acceso inmediato

---

## Data Structures

### ComponentMetadata
```python
@dataclass
class ComponentMetadata:
    name: str
    location: Path  # Current location
    purpose: str
    dependencies: List[str]
    has_tests: bool
    test_coverage: Optional[float]
    has_docs: bool
    maturity_level: MaturityLevel  # PROTOTYPE, BETA, STABLE
    reusability_score: int  # 1-10
    is_framework_core: bool

    def to_scorecard(self) -> str:
        """Generate markdown scorecard"""
        ...
```

### PlacementDecision
```python
@dataclass
class PlacementDecision:
    component: ComponentMetadata
    recommended_placement: Placement
    rationale: str
    action_items: List[str]
    confidence: float  # 0-1

    class Placement(Enum):
        PACKAGES_MELQUISEDEC = "packages/ in melquisedec"
        PACKAGES_ORIGIN_REPO = "packages/ in origin repo"
        APPS_SEPARATE_REPO = "apps/ in separate repo"
        EXAMPLES_MELQUISEDEC = "examples/ in melquisedec"
        TOOLS = "tools/ in appropriate repo"
        STANDALONE_REPO = "dedicated repo (large project)"
```

---

## API Design (Tooling)

### CLI Interface
```bash
# Analizar componente
daath-toolkit analyze <path> --output scorecard.md

# Aplicar decision tree
daath-toolkit classify <path> --format json

# Generar nuevo repo
daath-toolkit new-repo --name "cognitive-arch" \
                       --purpose "Estudios de BDI y SOAR"

# Validar estructura de repo
daath-toolkit validate-repo <path>
```

### Python API
```python
from daath_toolkit import ComponentAnalyzer, RepoGenerator

# Análisis
analyzer = ComponentAnalyzer()
metadata = analyzer.analyze("path/to/keter")
decision = analyzer.classify(metadata)

# Generación
generator = RepoGenerator()
generator.create("cognitive-arch",
                 purpose="Estudios de BDI y SOAR",
                 template="research")
```

---

## Integration Points

### 1. ARQUITECTURA_MONOREPO.md
- Agregar sección: "Multi-Repository Strategy"
- Referenciar ADR-002
- Actualizar diagrama con repos externos

### 2. CONTRIBUTING.md
- Nueva sección: "Where to Contribute"
- Link a decision tree
- Ejemplos de contribuciones por tipo

### 3. docs/manifiesto/
- Incorporar filosofía multi-repo en principios DAATH-ZEN
- Coherencia con autopoiesis (sistemas que crecen orgánicamente)

### 4. packages/daath-toolkit/
- Nuevos módulos:
  - `analyzers/component_analyzer.py`
  - `generators/new_research_repo.py`
  - `validators/repo_structure.py`

---

## Testing Strategy

### Tests para Decision Tree
```python
def test_classification_framework_core():
    component = mock_component(purpose="MCP integration")
    assert classify(component) == Placement.PACKAGES_MELQUISEDEC

def test_classification_research_app():
    component = mock_component(purpose="BDI study")
    assert classify(component) == Placement.APPS_SEPARATE_REPO

def test_classification_mature_tool():
    component = mock_component(
        purpose="Logging utility",
        maturity=MaturityLevel.STABLE,
        reusability=9
    )
    assert classify(component) == Placement.PACKAGES_ORIGIN_REPO
```

### Tests para Template Generator
```python
def test_new_repo_creates_structure():
    generator.create("test-repo", purpose="Test")
    assert os.path.exists("aleia-test-repo/pyproject.toml")
    assert os.path.exists("aleia-test-repo/apps/")
    assert "daath-toolkit" in read_file("aleia-test-repo/pyproject.toml")
```

---

## Migration Strategy (If Needed)

Si la decisión es mover keter:

### Scenario A: keter → package in bereshit
```bash
cd aleia-bereshit
git mv apps/keter packages/keter
# Restructure to src/ layout
# Add pyproject.toml
# Add tests/
```

### Scenario B: keter → standalone repo
```bash
# 1. Create new repo
daath-toolkit new-repo --name keter --purpose "..."

# 2. Copy code
cp -r aleia-bereshit/apps/keter/* aleia-keter/apps/keter/

# 3. Update dependencies
# aleia-keter/pyproject.toml includes daath-toolkit

# 4. Archive in bereshit
git mv aleia-bereshit/apps/keter aleia-bereshit/.archive/keter
```

### Scenario C: keter stays as-is
```markdown
# Document decision
## Rationale
Keter is still experimental and specific to bereshit investigations.

## Future Review
Re-evaluate when:
- Test coverage > 80%
- Requested by 2+ external projects
- Reaches v1.0.0
```

---

## Deliverables Summary

| Deliverable | Location | Format |
|-------------|----------|--------|
| ADR-002 | `docs/architecture/ADR-002-multi-repo-strategy.md` | Markdown |
| Decision Tree | `docs/guides/component-placement-guidelines.md` | Mermaid + Table |
| Repo Template | `docs/guides/new-research-repo-template.md` | Markdown + Code |
| Multi-Repo Workflow | `docs/guides/multi-repo-spec-workflow.md` | Markdown |
| Keter Analysis | `.spec-workflow/.../analysis/keter-evaluation.md` | Markdown |
| Keter Decision | `.spec-workflow/.../analysis/keter-decision.md` | Markdown |
| apps/ Clarification | Updated `ARQUITECTURA_MONOREPO.md` + `apps/README.md` | Markdown |

---

## Risk Analysis

### Risk 1: Fragmentación del Ecosistema
**Probabilidad**: Media
**Impacto**: Alto
**Mitigación**:
- Guidelines claras y fáciles de seguir
- daath-toolkit como punto de integración
- spec-workflow para coordinación

### Risk 2: Overhead de Gestión Multi-Repo
**Probabilidad**: Alta
**Impacto**: Medio
**Mitigación**:
- Automatización con CI/CD
- Templates pre-configurados
- Documentación exhaustiva

### Risk 3: Confusión sobre apps/ vs Investigaciones Reales
**Probabilidad**: Baja (después de este spec)
**Impacto**: Medio
**Mitigación**:
- Renombrado a examples/ o README explícito
- CONTRIBUTING.md actualizado

### Risk 4: Keter Analysis Incompleto (sin acceso)
**Probabilidad**: Media
**Impacto**: Bajo
**Mitigación**:
- Documentar proceso agnóstico del contenido
- Solicitar info al usuario
- Decisión provisional revisable

---

## Future Enhancements (v2.0.0+)

- **Monorepo tools**: Integración con Nx o Turborepo para multi-repo
- **Dependency graph**: Visualización de deps entre repos
- **Automated sync**: Scripts para propagar cambios toolkit → repos
- **Package registry**: Registry privado para packages internos
- **CI/CD templates**: GitHub Actions compartidos para todos los repos
