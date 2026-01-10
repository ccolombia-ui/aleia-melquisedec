#!/usr/bin/env python3
"""
Traducir todos los REQ-XXX a español manteniendo frontmatter YAML-LD intacto
"""

import re
from pathlib import Path

# Diccionario de traducciones técnicas (mantener consistencia terminológica)
TRANSLATIONS = {
    # Títulos y encabezados
    "Generated From": "Generado Desde",
    "Metadata": "Metadatos",
    "Summary": "Resumen",
    "Problem Statement": "Planteamiento del Problema",
    "Requirement Specification": "Especificación del Requerimiento",
    "Description": "Descripción",
    "Acceptance Criteria": "Criterios de Aceptación",
    "Dependencies and Constraints": "Dependencias y Restricciones",
    "Dependencies": "Dependencias",
    "Validation Method": "Método de Validación",
    "Implementation Guidance": "Guía de Implementación",
    "Generated": "Generado",
    "Template": "Plantilla",
    "Status": "Estado",
    
    # result_type
    "intermediate": "intermedio",
    "immediate": "inmediato",
    "final": "final",
    
    # Prioridades
    "Critical": "Crítico",
    "High": "Alto",
    "Medium": "Medio",
    "Low": "Bajo",
    
    # Tipos
    "Template": "Plantilla",
    "Documentation": "Documentación",
    "Configuration": "Configuración",
    "Tool": "Herramienta",
    "Testing": "Pruebas",
    "Safety": "Seguridad",
    "Migration": "Migración",
    "Autopoiesis": "Autopoiesis",
    "Specification": "Especificación",
    
    # Frases comunes
    "This requirement addresses the need for": "Este requerimiento aborda la necesidad de",
    "as part of the KeterDoc architecture implementation": "como parte de la implementación de la arquitectura KeterDoc",
    "This requirement should be implemented following the DAATH-ZEN configurable template pattern and validated against the acceptance criteria listed above.": "Este requerimiento debe implementarse siguiendo el patrón de plantilla configurable DAATH-ZEN y validarse contra los criterios de aceptación listados arriba.",
    
    # Términos específicos de requerimientos
    "Create": "Crear",
    "Document": "Documentar",
    "Script": "Script",
    "Test": "Probar",
    "Migrate": "Migrar",
    "Generate": "Generar",
    "Validate": "Validar",
    "Extract": "Extraer",
    "Backup": "Respaldar",
    "Run": "Ejecutar",
    
    # Frases descriptivas específicas
    "for CI/CD validation": "para validación CI/CD",
    "for automated migration": "para migración automatizada",
    "for quick artifact creation": "para creación rápida de artefactos",
    "to build dependency graph": "para construir grafo de dependencias",
    "with comprehensive unit tests": "con pruebas unitarias comprehensivas",
    "to convert YAML-LD to RDF": "para convertir YAML-LD a RDF",
    "for RDF → Neo4j import": "para importación RDF → Neo4j",
    "with 10 example Cypher queries": "con 10 queries Cypher de ejemplo",
    "explaining complete Neo4j workflow": "explicando el flujo completo de Neo4j",
    "before migration": "antes de la migración",
    "Convert": "Convertir",
    "to new templates": "a las nuevas plantillas",
    "and verify relationships": "y verificar relaciones",
    "on migrated project": "en el proyecto migrado",
    "from pilot migration": "de la migración piloto",
    "for manifesto module": "para módulo del manifiesto",
    "with results chain and conceptualization map": "con cadena de resultados y mapa de conceptualización",
    "for tracking": "para seguimiento",
    "across all 21 specs and 6 modules": "a través de las 21 specs y 6 módulos",
    "from Phase 7": "de la Fase 7",
    
    # Sustantivos adicionales
    "implementation specs": "especificaciones de implementación",
    "Visual identity": "Identidad visual",
    "automation": "automatización",
    "checker": "verificador",
    "documentation specs": "especificaciones de documentación",
    "tool spec": "especificación de herramienta",
    "searchable glossary": "glosario buscable",
    "master index": "índice maestro",
    "status tracker": "rastreador de estado",
    "system coherence": "coherencia del sistema",
    "manifesto-wide implementation": "implementación del manifiesto completo",
    
    # Términos de aceptación
    "Each has": "Cada uno tiene",
    "All": "Todos",
    "specs created": "specs creadas",
    "follow": "siguen",
    "structure": "estructura",
    
    # Varios
    "Unit tests": "Pruebas unitarias",
    "test cases": "casos de prueba",
    "File": "Archivo",
    "Folder": "Carpeta",
    "through": "hasta",
    "uses": "usa",
    "format": "formato",
    "like": "como",
    "Links to": "Enlaces a",
    "sections": "secciones",
    "Deliverable": "Entregable",
    "Table": "Tabla",
    "Progress bars": "Barras de progreso",
    "visual": "visual",
    "Auto-generated": "Auto-generado",
    "from spec folders": "de las carpetas spec",
    "updates automatically": "actualiza automáticamente",
    "on spec changes": "ante cambios en specs",
    
    # Sustantivos técnicos (mantener algunos en inglés si son nombres propios)
    "lens variants": "variantes de lens",
    "workflow patterns": "patrones de workflow",
    "knowledge graph": "grafo de conocimiento",
    "validation suite": "suite de validación",
    "compliance": "cumplimiento",
    "migration": "migración",
    
    # Effort
    "hours": "horas",
    "hour": "hora",
}

def translate_line(line):
    """Traducir una línea manteniendo formato Markdown y términos técnicos"""
    
    # No traducir líneas de frontmatter YAML
    if line.strip().startswith(("'@", "dc:", "version:", "status:", "template_root:", "artifact_template:", "manifesto_coherence:")):
        return line
    
    # No traducir líneas que son puramente código o nombres de archivo
    if line.strip().startswith("`") or ".md" in line or ".py" in line or ".yaml" in line:
        return line
    
    # Traducir
    translated = line
    for en, es in TRANSLATIONS.items():
        # Usar regex para traducir solo palabras completas, preservando formato
        pattern = r'\b' + re.escape(en) + r'\b'
        translated = re.sub(pattern, es, translated, flags=re.IGNORECASE)
    
    return translated

def translate_requirement_file(filepath):
    """Traducir un archivo REQ-XXX completo"""
    print(f"Traduciendo {filepath.name}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_frontmatter = False
    frontmatter_count = 0
    translated_lines = []
    
    for line in lines:
        # Detectar frontmatter YAML-LD (entre --- líneas)
        if line.strip() == '---':
            frontmatter_count += 1
            in_frontmatter = (frontmatter_count == 1)
            translated_lines.append(line)
            continue
        
        # No traducir dentro del frontmatter
        if in_frontmatter or frontmatter_count < 2:
            translated_lines.append(line)
        else:
            # Traducir contenido
            translated_lines.append(translate_line(line))
    
    # Escribir archivo traducido
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)

def main():
    """Traducir todos los REQ-011 a REQ-044"""
    workbooks_dir = Path(r"c:\proyectos\aleia-melquisedec\apps\research-autopoietic-template\010-define\workbooks")
    
    # Buscar todos los archivos REQ-0XX.md
    req_files = sorted(workbooks_dir.glob("REQ-0*.md"))
    
    print(f"Encontrados {len(req_files)} archivos REQ para traducir...")
    
    for req_file in req_files:
        # Extraer número de REQ
        match = re.match(r'REQ-(\d+)', req_file.name)
        if match:
            req_num = int(match.group(1))
            # Traducir REQ-002 en adelante (REQ-001 ya está traducido)
            if req_num >= 2:
                translate_requirement_file(req_file)
    
    print("\n✅ Traducción completada!")

if __name__ == "__main__":
    main()
