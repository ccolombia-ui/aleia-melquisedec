# Product Steering - monorepo-improvements-v1.1.0

## 📖 Referencias Primarias (SSoT)

**DAATH-ZEN Fundamentos** (no duplicar, referenciar):
- **¿Qué es Melquisedec?**: [[01-que-es-melquisedec]]
- **Fundamento Kabalístico**: [[02-fundamento-kabalistico]]
- **5 Rostros**: [[03-cinco-rostros]]
- **Principios Fundacionales**: [[04-principios-fundacionales]]

**DAATH-ZEN Arquitectura**:
- **Sistema Checkpoints**: [[02-sistema-checkpoints]]
- **Sincronización Knowledge**: [[04-sincronizacion-knowledge]]
- **Sistema Autopoiesis**: [[05-autopoiesis-system]]

**DAATH-ZEN Workflow**:
- **MCPs Recomendados**: [[04-mcps-recomendados]]
- **Sistema Autopoiesis (workflow)**: [[05-autopoiesis]]

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
