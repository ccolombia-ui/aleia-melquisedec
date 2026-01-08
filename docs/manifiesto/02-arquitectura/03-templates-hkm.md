# Templates HKM: Headers de Metadata

```yaml
---
id: "arquitectura-03-templates-hkm"
is_a: "architecture/metadata-standard"
version: "4.0.0"
dc:
  title: "Templates HKM: Headers Knowledge Management"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["HKM", "Metadata", "Dublin Core", "SECI", "Trazabilidad"]
seci:
  derives_from: ["../01-fundamentos/04-principios-fundacionales.md"]
  informs: ["../03-workflow/02-trazabilidad.md"]
---
```

---

## ¿Qué es HKM?

**HKM (Header Knowledge Management)** es el estándar de metadata obligatorio para todos los artifacts en MELQUISEDEC.

### Propósito

1. **Trazabilidad**: Conocer origen y derivaciones de cada artifact
2. **Versionamiento**: Tracking de cambios a lo largo del tiempo
3. **Descubribilidad**: Búsqueda eficiente en el grafo de conocimiento
4. **Interoperabilidad**: Metadata estándar reconocida (Dublin Core)

---

## Estructura del Header

Todo archivo `.md` en MELQUISEDEC DEBE comenzar con este header:

```yaml
---
id: "unique-identifier"
is_a: "artifact-type"
version: "X.Y.Z"
dc:
  title: "Human-readable title"
  creator: ["Author 1", "Author 2"]
  date: "YYYY-MM-DD"
  subject: ["Tag1", "Tag2"]
  source: ["Source reference"]
seci:
  derives_from: ["../path/to/source1.md", "../path/to/source2.md"]
  informs: ["../path/to/derivative1.md"]
---
```

---

## Campos Obligatorios

### 1. `id` (string, obligatorio)

Identificador único del artifact en formato kebab-case.

**Convención**:
```
{artifact-type}-{descriptor}

Ejemplos:
- concept-crisp-dm
- analysis-methodologies-comparison
- output-guia-crisp-dm
- lesson-001-hypatia-citations
```

**Reglas**:
- Único dentro del domain
- Minúsculas con guiones
- Sin espacios ni caracteres especiales
- Debe coincidir con el nombre del archivo (sin `.md`)

---

### 2. `is_a` (string, obligatorio)

Tipo de artifact según taxonomía MELQUISEDEC.

**Tipos válidos**:

| Carpeta | Tipos |
|---------|-------|
| `0-inbox/` | `issue`, `task`, `dependency` |
| `1-literature/` | `paper`, `book`, `article`, `code-source` |
| `2-atomic/` | `concept`, `definition`, `question`, `argument` |
| `3-workbook/` | `analysis`, `decision`, `experiment`, `draft` |
| `4-dataset/` | `template`, `schema`, `dataset`, `diagram` |
| `5-outputs/` | `output`, `deliverable` |
| `_melquisedec/` | `metadata`, `checkpoint`, `prompt` |

**Ejemplos**:
```yaml
is_a: "concept"              # Concepto atómico
is_a: "analysis"             # Análisis comparativo
is_a: "template"             # Template reutilizable
is_a: "output"               # Output final
```

---

### 3. `version` (string, obligatorio)

Versión semántica del artifact.

**Formato**: `MAJOR.MINOR.PATCH`

```yaml
version: "1.0.0"    # Primera versión estable
version: "1.1.0"    # Nueva feature (compatible)
version: "2.0.0"    # Breaking change
version: "1.0.1"    # Bug fix
```

**Reglas**:
- Artifacts empiezan en `1.0.0`
- Outputs son inmutables → nueva versión = nuevo archivo
- Incremento según semver

---

### 4. `dc` (object, obligatorio)

Metadata Dublin Core para interoperabilidad.

#### 4.1. `dc.title` (string, obligatorio)

Título human-readable del artifact.

```yaml
dc:
  title: "CRISP-DM Methodology"
  title: "Comparación de Metodologías de Data Science"
  title: "Guía Completa de CRISP-DM"
```

#### 4.2. `dc.creator` (array, obligatorio)

Autores del artifact.

```yaml
dc:
  creator: ["HYPATIA"]              # Un rostro
  creator: ["SALOMON", "MORPHEUS"]  # Múltiples rostros
  creator: ["Usuario", "ALMA"]      # Usuario + rostro
```

#### 4.3. `dc.date` (string, obligatorio)

Fecha de creación en formato ISO 8601.

```yaml
dc:
  date: "2026-01-08"
  date: "2026-01-08T14:30:00Z"  # Con timestamp (opcional)
```

#### 4.4. `dc.subject` (array, obligatorio)

Tags/categorías del artifact.

```yaml
dc:
  subject: ["CRISP-DM", "Data Science", "Methodology"]
  subject: ["Authentication", "Security", "OAuth2"]
  subject: ["Trazabilidad", "Metadata", "Autopoiesis"]
```

#### 4.5. `dc.source` (array, opcional)

Referencias externas (URLs, DOIs, ISBNs).

```yaml
dc:
  source:
    - "https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining"
    - "DOI:10.1109/TKDE.2000.123456"
    - "ISBN:978-0321125217"
```

---

### 5. `seci` (object, obligatorio)

Metadata del modelo SECI (Nonaka) para trazabilidad.

#### 5.1. `seci.derives_from` (array, obligatorio)

Lista de artifacts de los cuales deriva este artifact.

```yaml
seci:
  derives_from:
    - "../1-literature/papers/chapman-2000-crisp-dm.pdf"
    - "../2-atomic/concepts/concept-data-mining.md"
```

**Reglas**:
- Rutas relativas desde el archivo actual
- Debe existir el archivo referenciado
- Puede estar vacío `[]` solo para artifacts raíz (fuentes primarias)

#### 5.2. `seci.informs` (array, opcional)

Lista de artifacts que derivan de este artifact.

```yaml
seci:
  informs:
    - "../3-workbook/analysis-methodologies.md"
    - "../5-outputs/GUIA_CRISP_DM_v1.0.0/README.md"
```

**Reglas**:
- Rutas relativas
- Puede estar vacío si aún no hay derivatives
- Se actualiza cuando se crean derivatives

---

## Campos Opcionales

### 6. `status` (string, opcional)

Estado del artifact (útil para workflows).

```yaml
status: "draft"          # Borrador en progreso
status: "review"         # En revisión
status: "published"      # Publicado
status: "deprecated"     # Obsoleto
status: "archived"       # Archivado
```

---

### 7. `confidence` (float, opcional)

Nivel de confianza del artifact (usado en lessons).

```yaml
confidence: 0.95    # Alta confianza
confidence: 0.70    # Confianza media
confidence: 0.50    # Baja confianza
```

---

### 8. `rostro` (string, opcional)

Rostro que creó el artifact (alternativa a `dc.creator`).

```yaml
rostro: "HYPATIA"
rostro: "SALOMON"
rostro: "MORPHEUS"
```

---

### 9. `git_tag` (string, opcional)

Git tag asociado al output (solo para outputs).

```yaml
git_tag: "output-guia-crisp-dm-v1.0.0"
```

---

## Ejemplos Completos

### Ejemplo 1: Concepto Atómico

```yaml
---
id: "concept-crisp-dm"
is_a: "concept"
version: "1.0.0"
dc:
  title: "CRISP-DM Methodology"
  creator: ["HYPATIA"]
  date: "2026-01-08"
  subject: ["CRISP-DM", "Data Mining", "Methodology"]
  source: ["https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining"]
seci:
  derives_from: ["../1-literature/papers/chapman-2000-crisp-dm.pdf"]
  informs: ["../3-workbook/analysis-methodologies.md"]
---

# CRISP-DM

[Contenido del concepto...]
```

---

### Ejemplo 2: Análisis

```yaml
---
id: "analysis-methodologies-comparison"
is_a: "analysis"
version: "1.0.0"
dc:
  title: "Comparación de Metodologías de Data Science"
  creator: ["SALOMON"]
  date: "2026-01-08"
  subject: ["Comparison", "Decision", "Methodologies"]
seci:
  derives_from:
    - "../2-atomic/concepts/concept-crisp-dm.md"
    - "../2-atomic/concepts/concept-tdsp.md"
    - "../2-atomic/concepts/concept-kdd.md"
  informs: ["../5-outputs/GUIA_METODOLOGIAS_v1.0.0/README.md"]
status: "published"
---

# Comparación: CRISP-DM vs TDSP vs KDD

[Contenido del análisis...]
```

---

### Ejemplo 3: Output Final

```yaml
---
id: "output-guia-crisp-dm"
is_a: "output"
version: "1.0.0"
dc:
  title: "Guía Completa de CRISP-DM"
  creator: ["ALMA"]
  date: "2026-01-08"
  subject: ["CRISP-DM", "Guide", "Tutorial"]
seci:
  derives_from:
    - "../3-workbook/analysis-methodologies.md"
    - "../4-dataset/templates/crisp-dm-phase1-template.md"
  informs: []
status: "published"
git_tag: "output-guia-crisp-dm-v1.0.0"
---

# Guía Completa de CRISP-DM v1.0.0

[Contenido del output...]
```

---

### Ejemplo 4: Lesson

```yaml
---
id: "lesson-001-hypatia-citations"
is_a: "lesson"
version: "1.0.0"
dc:
  title: "Filter Papers by Citation Count"
  creator: ["ALMA"]
  date: "2026-01-08"
  subject: ["Research", "Quality", "Best Practice"]
seci:
  derives_from: ["../_melquisedec/logs/instance-001-chatlog.md"]
  informs: ["../_melquisedec/prompts/hypatia-v1.1.0.md"]
rostro: "HYPATIA"
confidence: 0.95
status: "validated"
---

# Lesson: Filter Papers by Citation Count

[Contenido de la lesson...]
```

---

## Validación de Headers

### Herramienta: `validate-metadata.py`

```python
"""
Valida que todos los archivos .md tengan HKM header válido.

Usage:
    python _melquisedec/validate-metadata.py
"""

import yaml
from pathlib import Path

REQUIRED_FIELDS = ["id", "is_a", "version", "dc", "seci"]
REQUIRED_DC_FIELDS = ["title", "creator", "date", "subject"]
REQUIRED_SECI_FIELDS = ["derives_from"]

def validate_header(filepath: Path) -> bool:
    """Valida header HKM de un archivo."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer frontmatter YAML
    if not content.startswith("---"):
        print(f"❌ {filepath}: Missing YAML frontmatter")
        return False

    yaml_end = content.find("---", 3)
    if yaml_end == -1:
        print(f"❌ {filepath}: Unclosed YAML frontmatter")
        return False

    yaml_content = content[3:yaml_end]

    try:
        metadata = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        print(f"❌ {filepath}: Invalid YAML: {e}")
        return False

    # Validar campos requeridos
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            print(f"❌ {filepath}: Missing required field '{field}'")
            return False

    # Validar Dublin Core
    for field in REQUIRED_DC_FIELDS:
        if field not in metadata["dc"]:
            print(f"❌ {filepath}: Missing required dc.{field}")
            return False

    # Validar SECI
    for field in REQUIRED_SECI_FIELDS:
        if field not in metadata["seci"]:
            print(f"❌ {filepath}: Missing required seci.{field}")
            return False

    print(f"✅ {filepath}: Valid HKM header")
    return True


def validate_all():
    """Valida todos los archivos .md en carpetas principales."""

    folders = [
        "0-inbox", "1-literature", "2-atomic",
        "3-workbook", "4-dataset", "5-outputs"
    ]

    all_valid = True

    for folder in folders:
        folder_path = Path(folder)
        if not folder_path.exists():
            continue

        for md_file in folder_path.rglob("*.md"):
            if not validate_header(md_file):
                all_valid = False

    if all_valid:
        print("\n✅ All files have valid HKM headers")
    else:
        print("\n❌ Some files have invalid headers")

    return all_valid


if __name__ == "__main__":
    validate_all()
```

---

## Buenas Prácticas

### ✅ DO

- **Usar IDs descriptivos**: `concept-jwt-authentication` mejor que `concept-001`
- **Actualizar `informs`**: Cuando creas derivative, actualiza parent's `informs`
- **Versionar correctamente**: Cambio significativo = bump version
- **Documentar sources**: Siempre referenciar fuentes primarias
- **Mantener trazabilidad**: `derives_from` completo y correcto

### ❌ DON'T

- **IDs genéricos**: `concept-001`, `analysis-temp`
- **Versiones incorrectas**: `v1`, `1.0`, `version-1`
- **Derives_from vacío**: Solo para fuentes primarias externas
- **Creators vagos**: "Usuario" sin especificar rostro
- **Subjects genéricos**: "Research", "Analysis" (demasiado amplio)

---

## Integración con Neo4j

Los headers HKM se mapean directamente a nodos y relaciones en Neo4j:

```cypher
// Crear nodo desde HKM header
CREATE (c:Concept {
  id: "concept-crisp-dm",
  title: "CRISP-DM Methodology",
  version: "1.0.0",
  created_at: date("2026-01-08"),
  creator: "HYPATIA",
  subjects: ["CRISP-DM", "Data Mining", "Methodology"]
})

// Crear relaciones de trazabilidad
MATCH (source:Paper {id: "paper-chapman-2000"})
MATCH (concept:Concept {id: "concept-crisp-dm"})
CREATE (concept)-[:DERIVES_FROM]->(source)

MATCH (concept:Concept {id: "concept-crisp-dm"})
MATCH (analysis:Analysis {id: "analysis-methodologies"})
CREATE (concept)-[:INFORMS]->(analysis)
```

---

## Integración con Pinecone

La metadata HKM se incluye en los vectores:

```python
from pinecone import Pinecone

pc = Pinecone(api_key="...")
index = pc.Index("melquisedec-knowledge")

# Generar embedding + metadata
vector_data = {
    "id": "concept-crisp-dm",
    "values": embedding,  # Vector de OpenAI
    "metadata": {
        "id": "concept-crisp-dm",
        "type": "concept",
        "title": "CRISP-DM Methodology",
        "version": "1.0.0",
        "creator": "HYPATIA",
        "subjects": ["CRISP-DM", "Data Mining", "Methodology"],
        "derives_from": ["paper-chapman-2000"],
        "text": full_text[:1000]  # Primeros 1000 chars
    }
}

index.upsert(vectors=[vector_data], namespace="DD-001.I001")
```

---

## Referencias

- [Research Instance](01-research-instance.md) - Estructura de 6 carpetas
- [Trazabilidad](../03-workflow/02-trazabilidad.md) - Grafos de conocimiento
- [Dublin Core Metadata Initiative](https://www.dublincore.org/)
- [SECI Model (Nonaka & Takeuchi)](https://en.wikipedia.org/wiki/SECI_model_of_knowledge_dimensions)

---

**Versión**: 4.0.0
**Última actualización**: 2026-01-08
**Próxima revisión**: 2026-04-08
