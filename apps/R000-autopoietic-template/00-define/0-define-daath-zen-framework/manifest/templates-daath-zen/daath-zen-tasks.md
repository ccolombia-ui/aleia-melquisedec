# DAATH-ZEN Template: Tasks Document

## Template Structure

This template defines the structure for implementation task documents in the DAATH-ZEN methodology. It extends `daath-zen-base.md` with detailed task breakdowns and project planning.

---

## Sections

### 1. Overview
- Total estimated effort (days/hours)
- Phase breakdown with durations
- Agent assignments
- References to requirements and design

### 2. Tasks
Each task follows this structure:

```markdown
### Task-{SPEC}-{NUMBER}: {Task Title}

- **Owner**: {Agent name - HYPATIA/SALOMON/MORPHEUS/ALMA}
- **File**: {Primary file or directory created/modified}
- **Requirements**: {Related requirement IDs}
- **Estimación**: {Hours or days}
- **Prioridad**: 🔴 ALTA / 🟡 MEDIA / 🟢 BAJA
- **Dependencies**: {Task IDs that must complete first}
- **Subtasks**:
  - {Subtask 1 description}
  - {Subtask 2 description}
  - ...
- **Validation**:
  \`\`\`bash
  # Commands to verify task completion
  pytest tests/
  mypy src/
  \`\`\`
- **Success Criteria**:
  - ✅ {Criterion 1}
  - ✅ {Criterion 2}
```

**Example**:
```markdown
### Task-000-001: Create Manifest Structure with Legacy Inputs

- **Owner**: MORPHEUS
- **File**: `00-define/0-define-daath-zen-framework/manifest/`
- **Requirements**: REQ-000-01
- **Estimación**: 4 hours
- **Prioridad**: 🔴 ALTA
- **Dependencies**: None
- **Subtasks**:
  - Create `manifest/README.md` with index
  - Create `manifest/legacy-inputs/` and copy 3 analysis files
  - Create `manifest/templates-daath-zen/` with 6 templates
  - Create `manifest/code-analysis/` with 3 documentation files
- **Validation**:
  \`\`\`bash
  tree 00-define/0-define-daath-zen-framework/manifest/
  find manifest/ -type f -name "*.md" | wc -l  # Should be 13+
  \`\`\`
- **Success Criteria**:
  - ✅ `manifest/` structure created with 3 subfolders
  - ✅ All legacy inputs copied (4 files)
  - ✅ All 6 DAATH-ZEN templates present
  - ✅ spec-workflow-mcp analysis documented (3 files)
```

### 3. Milestones & Checkpoints
Define major project milestones:

```markdown
### Milestone {NUMBER}: {Milestone Name}
- **Date**: {Target date}
- **Criteria**:
  - ✅ {Completion criterion 1}
  - ✅ {Completion criterion 2}
- **Checkpoint**: {Review process or validation}
```

### 4. Risk Management
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {Risk description} | Low/Medium/High | Low/Medium/High | {Mitigation strategy} |

### 5. Success Metrics
Quantitative and qualitative metrics to measure project success:

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| {Metric name} | {Target value} | TBD | 🟡 Pending |

### 6. Traceability Matrix
| Task | Requirement | Design Component | Validation |
|------|-------------|------------------|------------|
| Task-{SPEC}-XXX | REQ-{SPEC}-YY | ADR-ZZ | Test suite |

---

## Usage in Workbooks

### Academic Research Workbook
When researching project planning, atomics should capture:
- Agile methodologies (Scrum, Kanban)
- Estimation techniques (Story Points, Planning Poker)
- Risk management frameworks

### IMRAD Workbook
When synthesizing task planning knowledge:
- **Introduction**: Project planning importance
- **Literature Review**: Agile vs Waterfall, estimation techniques
- **Methodology**: How tasks were identified and estimated
- **Results**: Complete task breakdown with dependencies
- **Discussion**: Estimation accuracy, risk mitigation strategies
- **Conclusion**: Lessons learned for future planning
- **References**: Project management literature, Agile frameworks

---

## Metadata Requirements

All tasks documents MUST include:
- `spec:issue`: Spec ID
- `spec:owner`: Agent responsible
- Dublin Core fields
- Links to requirements and design documents

---

## References

- [Agile Manifesto](https://agilemanifesto.org/)
- [PMBOK Guide](https://www.pmi.org/pmbok-guide-standards) - Project Management Body of Knowledge
- [SPEC-000 Tasks](../../../.spec-workflow/specs/spec-000-investigation-daath-zen/tasks.md)

---

**Template Version**: 1.0.0
**Last Updated**: 2026-01-11
**Owner**: MORPHEUS
