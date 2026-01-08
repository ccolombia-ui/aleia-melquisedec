# Conversaciones con ALMA

**Instance**: instance-XXX-{topic}  
**Rostro**: ALMA (Malkuth - La Publicadora)  
**Prompt usado**: daath-zen-{domain}-v{x.y.z}

---

## YYYY-MM-DD HH:MM - Publicación del Output

**ALMA**: [Respuesta completa de ALMA]

**Acciones de publicación**:
- ✅ Output guardado en `5-outputs/{OUTPUT_NAME}_v1.0.0/`
- ✅ Git commit creado: [SHA]
- ✅ Git tag creado: `output-{topic}-v1.0.0`
- ✅ Neo4j: Nodos y relaciones creadas
- ✅ Pinecone: Vectores insertados en namespace `DD-XXX.IXXX`

**Output producido**:
- **ID**: output-{topic}
- **Versión**: 1.0.0
- **Path**: `5-outputs/{OUTPUT_NAME}_v1.0.0/`
- **Neo4j Node ID**: [ID]
- **Vector Namespace**: DD-XXX.IXXX

---

## YYYY-MM-DD HH:MM - Extracción de Lessons

**ALMA**: Analizando chatlog para extraer lessons...

**Lessons propuestas** (revisión de usuario requerida):

1. **lesson-001-{rostro}-{topic}** (confidence: 0.XX)
   - **Contexto**: [Descripción del problema/situación]
   - **Solución**: [Qué se aprendió]
   - **Aplicable a**: daath-zen-{domain}
   
2. **lesson-002-{rostro}-{topic}** (confidence: 0.XX)
   - [...]

---

## Usuario Aprueba Lessons

**Usuario**: Aprobar lessons: [1, 2, ...] | Rechazar: [...]

**ALMA**: ✅ Lessons guardadas en `_daath/lessons/`

---

## Checkpoint ALMA

🔍 **Status**: ✅ Pasado

**Validaciones**:
- ✅ Output publicado correctamente
- ✅ Git commit + tag creados
- ✅ Neo4j sincronizado
- ✅ Vectores insertados
- ✅ Lessons extraídas y guardadas
- ✅ Output Triple completamente consistente

---

## Próximos Pasos

- 🔄 MORPHEUS: Incorporar lessons a `daath-zen-{domain}-v{x.y+1.z}`
- 📊 Validar lessons en próximas instances
- 📈 Actualizar métricas de dominio

---

**Generado automáticamente** | **Última actualización**: YYYY-MM-DD HH:MM
