---
id: "workflow-02-trazabilidad"
is_a: "workflow/spec"
version: "4.0.0"
dc:
  title: "Trazabilidad: Reglas y Validación"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["Trazabilidad", "SECI", "Grafo de Conocimiento"]
seci:
  derives_from: ["../02-arquitectura/03-templates-hkm.md"]
  informs: ["../04-implementacion/03-checklist-research-instance.md"]
---

# Trazabilidad: Políticas y Procesos

## Objetivo
Garantizar que cada artifact es trazable a sus fuentes (derivations), que se pueda navegar en el grafo y que la validación automatizada detecte rupturas.

## Principios
- **P6 Trazabilidad**: Todo concepto y análisis debe referenciar su(s) fuente(s).
- **Inmutabilidad de outputs**: Los outputs publicados son inmutables; las revisiones crean nuevas versiones con `seci.derives_from` apuntando al original.

## Reglas Específicas
1. `seci.derives_from` debe incluir rutas relativas a artifacts existentes.
2. `seci.informs` debe actualizarse cuando se crea un derivative.
3. No se permiten `derives_from` a archivos que están en `archived` sin referencia clara.
4. Validaciones periódicas (cron) deben ejecutar checks contra grafo Neo4j.

## Validaciones Automatizadas
- **validate-traceability.py**: Revisa que todos los `derives_from` apunten a archivos existentes.
- **graph-check**: Ensayar que no existan ciclos indebidos (salvo casos controlados documentados).
- **coverage-metric**: Porcentaje de artifacts con `derives_from` y `informs` correctos.

## Mapping a Neo4j
- Cada HKM header → nodo con propiedades `id`, `type`, `version`, `title`.
- `DERIVES_FROM` y `INFORMS` → relaciones dirigidas.
- Recomendación: Indizar nodo por `id` y `dc.title`.

### Ejemplo Cypher (creación simple)
```cypher
MERGE (a:Artifact {id: "concept-crisp-dm"})
MERGE (b:Paper {id: "paper-chapman-2000"})
MERGE (a)-[:DERIVES_FROM]->(b)
```

## Practicas para Autores
- Actualizar `seci.informs` del `derives_from` original al crear un derivative.
- Añadir `source` en `dc` con DOI o URL cuando sea posible.
- Emplear `confidence` y `rostro` donde aplique para ayudar en priorización.

## Reportes y Métricas
- Número de artifacts sin `derives_from` (objetivo < 5%).
- Porcentaje de artifacts con `informs` actualizado después de 7 días de creación del derivative.
- Lista de ciclos no-intencionados en grafo.

---

**Referencias**: `03-templates-hkm.md`, `01-research-instance.md`

**Versión**: 4.0.0
**Última actualización**: 2026-01-08
