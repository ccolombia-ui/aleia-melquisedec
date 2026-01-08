# Product Steering - monorepo-improvements-v1.1.0

## 📖 Referencias Primarias (SSoT)

**DAATH-ZEN Fundamentos** (no duplicar, referenciar):
- **¿Qué es Melquisedec?**: [docs/manifiesto/01-fundamentos/01-que-es-melquisedec.md](../../docs/manifiesto/01-fundamentos/01-que-es-melquisedec.md)
- **Fundamento Kabalístico**: [docs/manifiesto/01-fundamentos/02-fundamento-kabalistico.md](../../docs/manifiesto/01-fundamentos/02-fundamento-kabalistico.md)
- **5 Rostros**: [docs/manifiesto/01-fundamentos/03-cinco-rostros.md](../../docs/manifiesto/01-fundamentos/03-cinco-rostros.md)
- **Principios Fundacionales**: [docs/manifiesto/01-fundamentos/04-principios-fundacionales.md](../../docs/manifiesto/01-fundamentos/04-principios-fundacionales.md)

**DAATH-ZEN Arquitectura**:
- **Sistema Checkpoints**: [docs/manifiesto/02-arquitectura/02-sistema-checkpoints.md](../../docs/manifiesto/02-arquitectura/02-sistema-checkpoints.md)
- **Sincronización Knowledge**: [docs/manifiesto/02-arquitectura/04-sincronizacion-knowledge.md](../../docs/manifiesto/02-arquitectura/04-sincronizacion-knowledge.md)
- **Sistema Autopoiesis**: [docs/manifiesto/02-arquitectura/05-autopoiesis-system.md](../../docs/manifiesto/02-arquitectura/05-autopoiesis-system.md)

**DAATH-ZEN Workflow**:
- **MCPs Recomendados**: [docs/manifiesto/03-workflow/04-mcps-recomendados.md](../../docs/manifiesto/03-workflow/04-mcps-recomendados.md)
- **Sistema Autopoiesis (workflow)**: [docs/manifiesto/03-workflow/05-autopoiesis.md](../../docs/manifiesto/03-workflow/05-autopoiesis.md)

---

## 🎯 Contexto para este Spec

**Objetivo v1.1.0**: Consolidar monorepo con autopoiesis completa post-reorganización

**Rostros Involucrados**:
- **MELQUISEDEC** (classifier) - Tasks 1.1, 1.6
- **MORPHEUS** (implementer) - Tasks 1.2, 1.3, 1.5
- **SALOMON** (architect) - Task 1.4
- **ALMA** (publisher) - Task 1.7

**Principios Aplicados**:
- **P1: Autopoiesis First** - Lessons alimentan Neo4j → nuevos issues
- **P3: Issue-Driven** - Spec iniciado desde issue explícito
- **P5: Knowledge Capture** - 6 lessons + summary.yaml
- **P10: Feedback Loops** - Cleanup script detecta nuevos problemas

**Métricas de Éxito**:
- 0 referencias `nucleo-investigacion`
- Raíz <10 archivos
- Pre-commit hooks activos
- daath-toolkit instalable
- Tests >80% coverage
- Script validación sin errores críticos
