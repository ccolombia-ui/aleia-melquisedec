# Chatlog: Canonical Stubs Merge & Spec-001 Kickoff
**Date**: 2026-01-10
**Participants**: User, GitHub Copilot (Gemini 3 Pro)

## Summary
The session focused on two main streams:
1.  **Completing Option 1 (Canonical Stubs)**:
    - Verified generation of 20 stubs from `raw-manifiesto.md` (v4.3.1) instead of legacy `bereshit`.
    - Merged `feature/canonical-stubs-batch-1` into `main` after resolving a workspace conflict.
    - Added `check_coherence` and `check_canonical_uniqueness` to CI/Main.

2.  **Starting Spec-001 (KeterDoc Implementation)**:
    - Identified "race condition" where Spec implementation started before Stubs were merged.
    - Moved Spec work (REQ-002...REQ-010) to `feature/spec-001-implementation`.
    - Defined roadmap: REQ-001 (Vocabulary), REQ-002 (Template Generator), REQ-003 (Metadata).

## Decisions
- **Source of Truth**: `raw-manifiesto.md` is the definitive source for canonical headings.
- **Branching Strategy**: Use `feature/spec-001-implementation` for KeterDoc work to avoid poluting `main` during the heavy refactor.
- **Workflow**: Proceed with `design.md` elaboration and `tasks.md` creation for Spec-001.

## Next Steps
- Implement `REQ-001`: Create `context.jsonld`.
- Detail `design.md` in `.spec-workflow` folder.
- Create `tasks.md` in `.spec-workflow` folder.
