# Arquitectura del Monorepo

Documentación de decisiones arquitectónicas y estructura del proyecto.

## 📄 Documentos

### Decisiones de Arquitectura (ADRs)
- [[ADR-001-monorepo-structure]] - Estructura del monorepo y principios de organización

### Documentación de Estructura
- [[arquitectura-monorepo]] - **Arquitectura completa del proyecto** (movido desde raíz en 2026-01-08)
  - Descripción de cada carpeta top-level
  - Convenciones de naming
  - Flujos de trabajo

- [[estructura-visual]] - **Diagrama visual ASCII** (movido desde raíz en 2026-01-08)
  - Tree structure del monorepo
  - Colores y jerarquía visual

## 🎯 Principios Arquitectónicos

1. **Modularidad**: Separación clara entre `docs/`, `packages/`, `apps/`, `infrastructure/`, `tools/`
2. **Reusabilidad**: Packages compartidos entre apps
3. **Escalabilidad**: Estructura preparada para múltiples investigaciones
4. **Documentación Como Código**: ADRs versionados con el proyecto

## 🔗 Enlaces Relacionados

- **Guías**: [../guides/](../guides/)
- **Manifiesto**: [../manifiesto/](../manifiesto/)
- **Setup**: [[configuracion-completa]]
