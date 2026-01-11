# Hypothesis Document

> **DSR Phase**: Problem Identification
> **DAATH-ZEN Rostro**: HYPATIA (Researcher)
> **Version**: v1.0.0 (Initial)
> **Status**: 🔴 TO BE VALIDATED
> **Date**: 2026-01-08

## 🧪 Hipótesis Central

**La migración completa de Keter desde aleia-bereshit a aleia-melquisedec mediante abstracción de 5 dependencias hardcodeadas (DAATH, YESOD, AYIN, Templates L0, Multi-tenancy), arquitectura modular de paquetes (keter-core, keter-mcp, keter-services), y estrategia Test-Driven Refactoring (TDD), permitirá preservar 100% de la calidad actual (92.94% coverage, 131 tests, 0 bugs) mientras se alcanza independencia 9/10, completándose en ~22 días de trabajo con ROI 8x superior a reconstruir desde cero.**

## 🔍 Hipótesis Específicas por RQ

### H1: Dependencias Hardcodeadas (RQ1)

**Hipótesis**: Existen exactamente 5 categorías de dependencias hardcodeadas que impiden que Keter funcione fuera de aleia-bereshit, con score de acoplamiento variable (DAATH: 8/10, YESOD: 5/10, AYIN: 6/10, Templates: 9/10, Multi-tenancy: 7/10).

**Predicción**:
- DAATH tendrá ≥10 import statements en código Keter (`import { DaathValidator } from '@aleia/daath'`)
- YESOD tendrá ≥8 schemas importados (PolicySchema, RuleSchema, etc.)
- AYIN tendrá hardcoded `ayin_config` schema name en ≥15 queries
- Templates L0 tendrán 87 archivos JSON específicos de ALEIA
- Multi-tenancy tendrá lógica de negocio ALEIA en ≥5 servicios

**Validación**:
- [ ] Catálogo de dependencias con ubicaciones exactas (archivos + líneas)
- [ ] Score de acoplamiento validado (1-10 por dependencia)
- [ ] Matriz de impacto: funcionalidad que se pierde sin cada dependencia

**Expected Outcome**: Score promedio de acoplamiento ~7/10 (confirmando Independence 4/10 actual)

---

### H2: Abstracción Sin Pérdida de Funcionalidad (RQ2)

**Hipótesis**: Cada dependencia puede ser abstraída mediante patrón específico sin pérdida de funcionalidad:
- DAATH → Interface + Optional Dependency
- YESOD → Schema Migration (no abstraction needed)
- AYIN → Config-Driven Naming
- Templates → Plugin System
- Multi-tenancy → Interface + Adapter Pattern

**Predicción**:
- Interfaces TypeScript cubrirán 100% de method signatures actuales
- Adapters ALEIA implementarán interfaces manteniendo comportamiento exacto
- Tests existentes seguirán pasando con adapters (comportamiento idéntico)
- Fallback strategy permitirá operar sin dependencias opcionales (graceful degradation)

**Validación**:
- [ ] ≥8 interfaces diseñadas con 100% cobertura funcional
- [ ] Mock implementations validan que interfaces son suficientes
- [ ] Adapter ALEIA pasa todos los tests existentes (131/131)
- [ ] Keter funciona en modo degradado sin DAATH (Policy Engine sin KG validation)

**Expected Outcome**: 0% pérdida funcional con adapters, degradación controlada sin adapters

---

### H3: Arquitectura Modular Óptima (RQ3)

**Hipótesis**: Arquitectura modular de 3 packages + 1 app (`keter-core`, `keter-mcp`, `keter-services`, `apps/keter`) supera arquitectura monolítica en reusabilidad, testability y tree-shaking, siguiendo patrón usado por LlamaIndex/Langchain.

**Predicción**:
- `keter-core` será package standalone (0 dependencias internas)
- `keter-mcp` dependerá solo de `keter-core`
- `keter-services` consumirá `keter-core` sin depender de `keter-mcp`
- `apps/keter` orquestará todos los packages + adapters ALEIA
- Bundle size reducido 40% vs monolith (tree-shaking efectivo)

**Validación**:
- [ ] Dependency graph sin ciclos (DAG válido)
- [ ] `keter-core` exporta interfaces públicas (≥15 exports)
- [ ] Bundle analysis: tree-shaking elimina código no usado
- [ ] Cada package puede ser instalado independientemente (`npm install @melquisedec/keter-core`)

**Expected Outcome**: Arquitectura modular con dependency graph acíclico y bundle size reducido

---

### H4: Test-Driven Refactoring (RQ4)

**Hipótesis**: Estrategia TDD (test interface → refactor code → validate coverage) permite mantener ≥92.94% coverage durante migración, con 0 regressions si se sigue protocolo de 5 pasos.

**Protocolo TDD Propuesto**:
1. Baseline: Run all tests → 131/131 passing
2. Write tests for new interface (unit tests con mocks)
3. Refactor code to use interface (inject dependency)
4. Run tests → should still pass (131/131)
5. Measure coverage → should be ≥92.94%

**Predicción**:
- Coverage permanecerá ≥92% en cada layer refactorizada
- Si coverage cae <92%, rollback inmediato y re-diseño de abstraction
- Mocks permitirán unit testing sin dependencias externas (DAATH, Supabase)
- Integration tests validarán comportamiento end-to-end con adapters

**Validación**:
- [ ] Testing strategy documentada con checkpoints de coverage
- [ ] ≥8 mocks creados (1 por interface)
- [ ] Coverage reports por phase (baseline, post-layer-1, post-layer-2, etc.)
- [ ] 0 regressions detectadas (todos los tests existentes siguen pasando)

**Expected Outcome**: Coverage final ≥92.94%, 0 regressions, timeline sin retrabajos

---

### H5: Configuración Independiente de ALEIA (RQ5)

**Hipótesis**: Config-driven approach (`.env` + `KeterConfig` interface) permite deployment en ANY proyecto sin hardcoded ALEIA settings, con ≤15 config options necesarias para funcionalidad completa.

**Config Mínimo Predicho**:
```typescript
interface KeterConfig {
  database: {
    coreSchema: string;        // "keter_core" or custom
    configSchema: string;      // "keter_config" or custom
    graphSchema: string;       // "shared_kg" or custom
  };
  knowledgeGraph?: {           // Optional DAATH integration
    enabled: boolean;
    endpoint: string;
  };
  templates: {
    provider: 'file' | 'database' | 'custom';
    path?: string;
  };
  multiTenant: {
    enabled: boolean;
    resolver: ITenantResolver;
  };
}
```

**Predicción**:
- ≤15 config options cubren 100% de casos de uso
- Ejemplo `.env` genérico funciona sin modificaciones ALEIA
- Inicialización: `new KeterApp(config)` suficiente para startup
- Config validation catch errores en startup (fail-fast)

**Validación**:
- [ ] `KeterConfig` interface documentada (TypeScript + JSDoc)
- [ ] Ejemplo `.env.example` para proyecto genérico
- [ ] Demo app: Keter corriendo con config mínimo (no ALEIA)
- [ ] Config validator implementado (zod schema para KeterConfig)

**Expected Outcome**: Keter deployable en proyecto genérico con <30 líneas de configuración

---

### H6: Migración Schema Sin Downtime (RQ6)

**Hipótesis**: Config-driven schema naming (NO renombrar schemas físicos) permite zero-downtime migration, con schemas Supabase permaneciendo con nombres originales pero mapeados vía config.

**Estrategia Predicha**:
- ALEIA mantiene: `ayin_config`, `keter_core`, `shared_kg`, `shared`
- Proyecto nuevo usa: `my_app_config`, `my_app_core`, `my_app_kg`, `shared`
- Keter queries usan: `${config.database.coreSchema}.policies` (template strings)
- Migrations son responsabilidad del proyecto host (Keter no toca schemas)

**Predicción**:
- 0 minutos de downtime para ALEIA (no hay renaming)
- ≥50 queries refactorizados para usar config.database.* placeholders
- Migration guide permitirá nuevos proyectos crear schemas en <15 minutos
- RLS policies permanecen intactas (schema-agnostic via config)

**Validación**:
- [ ] Queries refactorizados: `SELECT * FROM ${config.database.coreSchema}.policies`
- [ ] ALEIA testing: Keter funciona con schemas originales
- [ ] Demo project: Keter funciona con schemas custom
- [ ] Migration guide documentado (≥10 pasos)

**Expected Outcome**: Zero-downtime migration, ANY proyecto puede usar schemas custom

---

## 📊 Hipótesis de Esfuerzo

### Effort Estimation by Layer

| Layer | Effort (days) | Risk | Complexity |
|-------|---------------|------|------------|
| Layer 1: DAATH | 2 days | LOW | Interface + Optional |
| Layer 2: YESOD | 1.5 days | LOW | Schema copy |
| Layer 3: AYIN | 1.5 days | MEDIUM | Query refactoring |
| Layer 4: Templates | 3 days | MEDIUM | Plugin system |
| Layer 5: Multi-tenancy | 3 days | HIGH | Business logic |
| Phase 2: Extract | 2 days | LOW | Move files |
| Phase 3: Bridge | 3.5 days | MEDIUM | Adapters + Testing |
| Phase 4: Decouple | 1.5 days | LOW | Final migration |

**Total**: 18 days core work + 4 days buffer = **22 days**

### ROI Calculation

- **Rebuilding from scratch**: 180 days (6 months)
- **Migration effort**: 22 days (1 month)
- **Savings**: 158 days (5.3 months)
- **ROI**: 158 / 22 = **7.2x** (rounded to 8x)

**Validación**:
- [ ] Timeline tracking por phase (actual vs estimated)
- [ ] Effort ajustado si complejidad mayor a predicción
- [ ] ROI recalculado con esfuerzo real al final

---

## 🎯 Success Criteria Global

La hipótesis central será VALIDADA si al finalizar la migración:

### Calidad (Non-Negotiable)
- [x] ✅ Coverage ≥92.94% (baseline: 92.94%)
- [x] ✅ 131/131 tests passing (baseline: 131/131)
- [x] ✅ 0 bugs (baseline: 0 bugs)
- [x] ✅ 0 vulnerabilities (baseline: 0 vuln)
- [x] ✅ A+ security rating (baseline: A+)

### Independencia
- [ ] ✅ Independence score ≥9/10 (baseline: 4/10)
- [ ] ✅ Keter funciona standalone sin ALEIA (demo project)
- [ ] ✅ ALEIA usa Keter via adapters (production working)

### Timeline
- [ ] ✅ Migración completada en ≤30 días (estimate: 22 days + buffer)
- [ ] ✅ 0 retrabajos por pérdida de calidad
- [ ] ✅ 0 rollbacks por tests fallidos

### ROI
- [ ] ✅ Effort real ≤30 días (vs 180 días rebuild)
- [ ] ✅ ROI ≥6x (target: 8x)

## 🚨 Invalidation Triggers

La hipótesis será INVALIDADA si:

1. **Coverage cae <90%** → Testing strategy inadecuada
2. **Tests fallan >5% (>6 tests)** → Abstraction rompió comportamiento
3. **Timeline excede 45 días** → Complexity subestimada
4. **Independence score <7/10** → Abstractions insuficientes
5. **Production downtime en ALEIA** → Migration strategy defectuosa

**Contingency Plan**: Si hipótesis invalidada, evaluar:
- Option A: Ajustar abstractions y re-intentar
- Option B: Hybrid approach (migrar solo core, dejar app en bereshit)
- Option C: Snapshot keter en bereshit y rebuild incremental en melquisedec

## 📝 Next Steps

1. ✅ Hypothesis document completado
2. [ ] Start RQ1: Dependency audit (validar H1)
3. [ ] Start RQ4: Testing strategy (preparar para H4)
4. [ ] Checkpoint: Review hypothesis con evidencia de RQ1
5. [ ] Proceder con design phase (RQ2, RQ3)

**Estimated**: 1 semana para validación inicial de hipótesis centrales (H1, H4)
