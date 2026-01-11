# Product Steering - Research Keter Migration

> **Tipo de Producto**: Research (DSR - Design Science Research)
> **Metodología**: DAATH-ZEN v2.0.0 - 5 Rostros
> **Owner**: HYPATIA (Research Lead)

## 🎯 Visión del Producto

Migrar Keter (Policy Engine + Backend Multi-Tenant + MCP Server) desde aleia-bereshit
a aleia-melquisedec, preservando 100% de calidad mientras se alcanza independencia 9/10.

## 📊 Métricas de Éxito

| Métrica | Actual | Target | Prioridad |
|---------|--------|--------|-----------|
| Test Coverage | 92.94% | ≥92.94% | P0 |
| Tests Passing | 131/131 | 131/131 | P0 |
| Bugs | 0 | 0 | P0 |
| Independencia | 3/10 | 9/10 | P0 |
| Tiempo Migración | - | ≤22 días | P1 |

## 🔬 Research Questions

1. **RQ1**: ¿Qué dependencias hardcodeadas tiene Keter actualmente?
2. **RQ2**: ¿Cómo abstraer cada dependencia sin perder funcionalidad?
3. **RQ3**: ¿Qué arquitectura de paquetes garantiza máxima modularidad?
4. **RQ4**: ¿Cómo mantener 92.94% coverage durante refactoring TDD?
5. **RQ5**: ¿Qué configuración permite deployment independiente?
6. **RQ6**: ¿Cómo migrar 4 schemas Supabase sin romper producción?

## ⚠️ Restricciones Críticas

- **ZERO REGRESSION**: No perder funcionalidad existente
- **TDD OBLIGATORIO**: Cada cambio debe tener tests primero
- **REVERSIBLE**: Cada fase debe ser reversible

## 📦 Entregables DSR

| Fase | Entregable | Criterio de Aceptación |
|------|------------|------------------------|
| Problem | `dependency-audit.md` | 100% deps catalogadas |
| Design | `formal-migration-spec.md` | ≥2500 líneas, aprobado por SALOMON |
| Build | Código migrado | CI green, coverage ≥92.94% |
| Evaluate | `independence-scorecard.md` | Score ≥9/10 |

## 🔗 Referencias

- [ADR-002 Original Decision](../../docs/architecture/ADR-002-keter-integration-decision.md)
- [Sprint 1 Analysis](../references/sprint-1-analysis.md)
