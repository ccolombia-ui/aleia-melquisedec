---
id: "workflow-03-versionamiento"
is_a: "workflow/spec"
version: "4.0.0"
dc:
  title: "Versionamiento Semántico de Artifacts"
  creator: ["Equipo ALEIA-BERESHIT"]
  date: "2026-01-08"
  subject: ["Versionamiento", "Semver", "Outputs"]
seci:
  derives_from: ["../02-arquitectura/03-templates-hkm.md"]
  informs: ["../04-implementacion/01-flujo-completo.md"]
---

# Versionamiento (Semver) para MELQUISEDEC

## Objetivo
Establecer reglas claras para versionar artifacts en `2-atomic/`, `3-workbook/`, `4-dataset/` y `5-outputs/`.

## Reglas Principales
- Usar SemVer: `MAJOR.MINOR.PATCH`
  - **MAJOR**: Cambios incompatibles / breaking changes.
  - **MINOR**: Nuevas features compatibles.
  - **PATCH**: Correcciones, typos, ajustes menores.
- **Outputs**: Considerados inmutables; publicar un cambio requiere crear nueva carpeta `name_vX.Y.Z/` y tag en Git.
- **Concepts / Analyses**: Pueden iterar en `version` mientras estén en `draft`; la publicación promueve a `1.0.0`.

## Naming y Tags
- Output tag example: `output-guia-crisp-dm-v1.0.0`
- Branch naming: `feature/{artifact-id}-vX.Y.Z` o `fix/{artifact-id}-patch`

## Process: Publicar un Output
1. Completar checklist (ver `03-checklist-research-instance.md`).
2. Generar carpeta final en `5-outputs/name_vMAJOR.MINOR.PATCH/`.
3. Añadir `git tag output-name-vMAJOR.MINOR.PATCH`.
4. Registrar tag en `_melquisedec/metadata.yaml` y en HKM del artifact.

## Version Bump Guidelines
- Bump of MAJOR requires approval de SALOMON y MELQUISEDEC.
- MINOR bump puede ser aprobada por el rostro que produce el artifact + reviewer.
- PATCH bumps pueden ser automáticas tras tests y revisión rápida.

## Ejemplos
- `1.0.0`: Primera versión estable de la guía.
- `1.1.0`: Añade un capítulo sobre MLOps (compatible).
- `2.0.0`: Rediseño completo de esquema y breaking changes en APIs.

## Integración en HKM header
Mantener `version` en el header HKM y registrar `git_tag` para outputs:
```yaml
version: "1.0.0"
git_tag: "output-guia-crisp-dm-v1.0.0"
```

---

**Referencias**: `03-templates-hkm.md`, `01-research-instance.md`

**Versión**: 4.0.0  
**Última actualización**: 2026-01-08
