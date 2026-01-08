# Product Steering - DAATH-ZEN Melquisedec

## 🎯 Visión

DAATH-ZEN Melquisedec es un sistema de investigación autopoiético que permite capturar, procesar y evolucionar conocimiento colaborando con agentes de IA. El proyecto encarna el concepto de los **5 Rostros** de la inteligencia colectiva.

## 🌟 Principios de Producto

### P1: Autopoiesis First
El sistema debe ser capaz de auto-generarse y evolucionar a partir de sus propias interacciones.

### P3: Issue-Driven Everything
Todo trabajo inicia desde un ISSUE explícito con metadata estructurada.

### P5: Knowledge Capture
Cada interacción genera artifacts reutilizables (chatlogs, lessons, outputs).

### P10: Feedback Loops
Los outputs generan nuevos issues en un ciclo continuo de mejora.

## 🎭 Los 5 Rostros

1. **MELQUISEDEC** - El facilitador y contextualizador
2. **HYPATIA** - La investigadora y analista
3. **SALOMÓN** - El arquitecto y diseñador de soluciones
4. **MORPHEUS** - El implementador y ejecutor
5. **ALMA** - La evaluadora y sintetizadora de lessons learned

## 🎯 Objetivos del Release v1.1.0

Este spec agrupa mejoras de mantenimiento del monorepo identificadas post-reorganización:

1. Limpiar referencias a estructura obsoleta (`nucleo-investigacion`)
2. Organizar documentación en ubicaciones correctas
3. Implementar automatización de calidad (pre-commit hooks)
4. Formalizar el paquete daath-toolkit
5. Agregar cobertura de tests
6. Crear herramientas de validación continua

## 📊 Métricas de Éxito

- [ ] 0 referencias a `nucleo-investigacion` en el codebase
- [ ] Raíz del proyecto limpia (<10 archivos)
- [ ] Pre-commit hooks activos protegiendo main
- [ ] daath-toolkit instalable via `pip install -e .`
- [ ] Cobertura de tests >80% en capture/ y storage/
- [ ] Script de validación ejecutable sin errores
