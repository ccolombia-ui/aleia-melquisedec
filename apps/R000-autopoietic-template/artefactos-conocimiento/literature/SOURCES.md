# Fuentes de Literatura - HYPATIA Knowledge Base

## 📚 Domain-Driven Design (DDD)

### Evans, Eric (2003)
- **Título**: Domain-Driven Design: Tackling Complexity in the Heart of Software
- **Editorial**: Addison-Wesley Professional
- **ISBN**: 978-0321125217
- **Páginas**: 560
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/ddd/evans-2003-domain-driven-design.pdf`
- **Conceptos clave**:
  - Bounded Context (p.335-345)
  - Ubiquitous Language (p.23-35)
  - Aggregate (p.125-135)
  - Repository (p.147-156)
  - Entity vs Value Object (p.89-105)

**Método de adquisición**:
- Buscar en Semantic Scholar API
- Alternativamente: Library Genesis, Anna's Archive
- Como último recurso: Extractos de Google Books

### Vernon, Vaughn (2013)
- **Título**: Implementing Domain-Driven Design
- **Editorial**: Addison-Wesley Professional
- **ISBN**: 978-0321834577
- **Páginas**: 656
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/ddd/vernon-2013-implementing-ddd.pdf`
- **Conceptos clave**:
  - Context Mapping (p.45-78)
  - Event Sourcing (p.210-245)
  - CQRS Pattern (p.246-280)
  - Strategic Design (p.79-120)

**Método de adquisición**: Mismo que Evans (2003)

---

## 📐 ISO/IEC 21838 - Basic Formal Ontology (BFO)

### ISO/IEC 21838-1:2019
- **Título**: Information technology — Top-level ontologies (TLO) — Part 1: Requirements
- **Organización**: ISO/IEC JTC 1/SC 32
- **Páginas**: ~40
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/iso/iso-21838-1-2019-requirements.pdf`
- **Conceptos clave**:
  - Top-Level Ontology definition
  - Requirements for TLO adoption
  - Interoperability criteria

**Método de adquisición**:
- ISO Official Store (requiere compra)
- Alternativamente: Draft versions disponibles en repositorios académicos
- BFO GitHub repository (versiones preliminares)

### ISO/IEC 21838-2:2019
- **Título**: Information technology — Top-level ontologies (TLO) — Part 2: Basic Formal Ontology (BFO)
- **Organización**: ISO/IEC JTC 1/SC 32
- **Páginas**: ~60
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/iso/iso-21838-2-2019-bfo.pdf`
- **Conceptos clave**:
  - Continuant vs Occurrent
  - Temporal regions
  - Spatial regions
  - Object vs Process
  - Quality vs Role

**Método de adquisición**: Mismo que Part 1

**Recursos alternativos**:
- BFO 2.0 Specification: https://github.com/BFO-ontology/BFO
- NCBIthesaurus BFO mappings
- Papers de Barry Smith (fundador de BFO)

---

## 📄 IMRAD Methodology

### Sollaci, Luciana B.; Pereira, Mauricio G. (2004)
- **Título**: The introduction, methods, results, and discussion (IMRAD) structure: a fifty-year survey
- **Journal**: Journal of the Medical Library Association
- **Volumen**: 92(3), pp. 364-367
- **DOI**: No DOI disponible (pre-DOI era)
- **PMID**: 15243643
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/imrad/sollaci-pereira-2004-imrad-structure.pdf`
- **Conceptos clave**:
  - IMRAD historical evolution
  - Section structure guidelines
  - Scientific writing standards

**Método de adquisición**:
- PubMed Central (open access)
- URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC442179/

### Wu, Jianguo (2011)
- **Título**: Improving the writing of research papers: IMRAD and beyond
- **Journal**: Landscape Ecology
- **Volumen**: 26, pp. 1345-1349
- **DOI**: 10.1007/s10980-011-9674-3
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/imrad/wu-2011-imrad-and-beyond.pdf`
- **Conceptos clave**:
  - IMRAD extensions
  - Discussion vs Conclusion
  - Literature Review integration

**Método de adquisición**:
- Semantic Scholar API
- SpringerLink (puede requerir acceso institucional)
- Sci-Hub como alternativa

### Nair, Prashanth K. & Nair, Santhosh J. (2014)
- **Título**: Organization of a Research Paper: The IMRAD Format
- **Libro**: Scientific Writing and Communication in Agriculture and Natural Resources
- **Editorial**: Springer
- **Páginas**: pp. 13-25
- **DOI**: 10.1007/978-3-319-03101-9_2
- **Status**: ⏳ Pendiente de descarga
- **Ubicación**: `literature/imrad/nair-nair-2014-imrad-format.pdf`

**Método de adquisición**:
- Semantic Scholar API
- SpringerLink

---

## 💻 spec-workflow-mcp Repository

### Repository Metadata
- **URL**: https://github.com/ccolombia-ui/spec-workflow-mcp
- **Descripción**: Model Context Protocol server for specification workflow management
- **Tecnología**: Python, MCP SDK, SQLite
- **Status**: ⏳ Pendiente de clonado
- **Ubicación**: `literature/spec-workflow-mcp/`
- **Archivos clave**:
  - `src/server.py`: MCP server implementation
  - `src/tools/`: Tool implementations
  - `src/models/`: Data models
  - `docs/`: Documentation

**Método de adquisición**:
```bash
git clone https://github.com/ccolombia-ui/spec-workflow-mcp.git literature/spec-workflow-mcp/
```

**Análisis a realizar**:
- Extractar arquitectura MCP
- Documentar tool patterns
- Identificar design decisions
- Mapear data models

---

## 📊 Estadísticas de Descarga

| Categoría | Fuentes | Páginas Est. | Status |
|-----------|---------|--------------|--------|
| DDD       | 2       | ~1,200       | ⏳     |
| ISO       | 2       | ~100         | ⏳     |
| IMRAD     | 3       | ~50          | ⏳     |
| Código    | 1 repo  | ~5,000 LOC   | ⏳     |
| **TOTAL** | **8**   | **~1,350 p.**| **0%** |

## 🚀 Plan de Descarga

### Prioridad 1: Acceso Libre
1. Sollaci & Pereira (2004) - PubMed Central ✅ Open Access
2. spec-workflow-mcp - GitHub ✅ Público
3. BFO 2.0 Spec - GitHub ✅ Público

### Prioridad 2: Semantic Scholar API
1. Evans (2003) - Buscar excerpts
2. Vernon (2013) - Buscar excerpts
3. Wu (2011) - Paper completo
4. Nair & Nair (2014) - Chapter completo

### Prioridad 3: Alternativas
1. Google Books - Previews de DDD books
2. Library Genesis - PDFs completos
3. Anna's Archive - Backup

### Prioridad 4: Compra (si necesario)
1. ISO 21838-1:2019 (~$100 USD)
2. ISO 21838-2:2019 (~$150 USD)

## 🔍 Validación Post-Descarga

Cada fuente descargada debe pasar:

1. **Verificación de Integridad**
   - [ ] PDF no corrupto
   - [ ] Texto extraíble (no scan de imagen)
   - [ ] Metadatos correctos (autor, año, título)

2. **Verificación de Contenido**
   - [ ] Páginas completas (no faltantes)
   - [ ] Índice accesible
   - [ ] Bibliografía incluida

3. **Registro en Knowledge Base**
   - [ ] Archivo en `literature/<categoria>/`
   - [ ] Metadatos en este archivo
   - [ ] Hash SHA-256 calculado
   - [ ] Entrada en catálogo SQLite

## 📝 Notas de Uso

Este archivo es **dinámico** y se actualiza durante el proceso de descarga. Cada fuente descargada debe:

1. Cambiar status de ⏳ a ✅
2. Registrar ubicación exacta del archivo
3. Calcular hash SHA-256 para integridad
4. Documentar páginas clave para análisis atómico

---

**Última actualización**: 2026-01-10  
**Responsable**: Melquisedec AI Assistant  
**Spec**: SPEC-001 Task 2.1 (HYPATIA Knowledge Acquisition)
