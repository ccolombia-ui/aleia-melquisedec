# ADR 001: Estructura de Monorepo

**Estado**: Aceptado  
**Fecha**: 2026-01-07  
**Autores**: Equipo MELQUISEDEC  

---

## Contexto

El proyecto ALEIA-MELQUISEDEC comenzó con una estructura simple:
- `bereshit/` - Manifiesto
- `nucleo-investigacion/` - Docker + MCP + Scripts
- `apps/` - Vacío con `.gitkeep`
- `_templates/` - Templates de apps

A medida que el proyecto crece, esta estructura se vuelve limitante:
- No hay separación clara entre código reutilizable y apps específicas
- Scripts mezclados en `nucleo-investigacion/scripts`
- Documentación dispersa
- Difícil escalar a múltiples investigaciones

---

## Decisión

Reorganizar como **monorepo modular** con:

```
aleia-melquisedec/
├── docs/              # Documentación centralizada
├── packages/          # Código reutilizable
├── apps/              # Investigaciones específicas
├── infrastructure/    # Docker, K8s, IaC
└── tools/             # Scripts de desarrollo
```

### Principios:

1. **Separación de Concerns**: Cada directorio tiene un propósito claro
2. **Reusabilidad**: `packages/` contiene componentes compartidos
3. **Escalabilidad**: Fácil agregar nuevas apps sin modificar infraestructura
4. **Documentación como Código**: Todo en `docs/` versionado con el código

---

## Consecuencias

### Positivas ✅

- ✅ **Modularidad**: Componentes independientes y reutilizables
- ✅ **Escalabilidad**: Múltiples investigaciones sin conflictos
- ✅ **Mantenibilidad**: Estructura clara facilita navegación
- ✅ **Testing**: Framework centralizado en `packages/daath-toolkit/testing`
- ✅ **CI/CD**: Preparado para automatización en `.github/workflows`
- ✅ **Onboarding**: README y docs centralizados facilitan incorporación

### Negativas ⚠️

- ⚠️ **Complejidad Inicial**: Más directorios que estructura simple
- ⚠️ **Migración**: Requiere actualizar referencias existentes
- ⚠️ **Learning Curve**: Nuevos contribuidores deben entender estructura

### Mitigaciones

- Crear `ARQUITECTURA_MONOREPO.md` con diagrama completo
- Mantener `README.md` como punto de entrada simple
- Proporcionar scripts de migración y validación
- Documentar flujos de trabajo comunes

---

## Alternativas Consideradas

### 1. Mantener Estructura Simple
**Rechazado**: No escala para múltiples investigaciones

### 2. Multi-repo (repo por investigación)
**Rechazado**: 
- Dificulta compartir código común
- Complica sincronización de infraestructura
- Overhead de gestión de repos

### 3. Monorepo con Turborepo/Nx
**Pospuesto**: 
- Overhead innecesario para fase actual
- Se puede migrar en el futuro si es necesario
- Decisión reversible

---

## Implementación

### Fase 1: Reorganización (actual)
- [x] Diseñar estructura
- [x] Mover archivos existentes
- [ ] Actualizar referencias en código
- [ ] Validar funcionamiento

### Fase 2: Documentación
- [x] Crear `ARQUITECTURA_MONOREPO.md`
- [ ] Crear ADRs para decisiones clave
- [ ] Actualizar guías de contribución

### Fase 3: Automatización
- [ ] Scripts de generación de apps
- [ ] Validadores de estructura
- [ ] CI/CD básico

---

## Referencias

- [Manifiesto MELQUISEDEC v3.0.0](../manifiesto/bereshit-v3.0.0.md)
- [Arquitectura del Monorepo](../../ARQUITECTURA_MONOREPO.md)
- [Monorepo Tools Comparison](https://monorepo.tools/)

---

## Notas

- Esta decisión alinea con el principio MELQUISEDEC de "crecimiento orgánico"
- La estructura permite que cada investigación evolucione independientemente
- Mantiene minimalismo: solo se crean carpetas cuando hay contenido
