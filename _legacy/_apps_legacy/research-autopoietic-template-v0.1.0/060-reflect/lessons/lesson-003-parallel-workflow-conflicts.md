---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
'@type': 'LearningResource'
'@id': 'https://melquisedec.org/lessons/lesson-003-parallel-workflow-conflicts'
dc:title: 'Lesson 003: Managing Parallel Workflows (Canonical Stubs vs Implementation)'
dc:created: '2026-01-10'
version: '1.0.0'
status: 'stable'
learning_type: 'process-improvement'
context:
  trigger: 'Git checkout blocked by uncommitted spec-001 requirements while trying to merge canonical stubs.'
  impact: 'Blocked workflow, risk of losing context.'
observation: 'Working on two distinct streams (Canonical Documentation vs KeterDoc Implementation) in parallel caused a workspace collision. The spec-001 files were in a "draft" state but prevented switching back to main to merge the "stable" stubs.'
analysis: 'The conflict arose because the "implementation" phase started (creating REQ files) before the "infrastructure" phase (canonical stubs) was fully merged. This is a common "race condition" in conscious software development.'
synthesis: 'Always complete the "Integration/Merge" cycle of a foundational task (like Stubs) before opening the floodgates of the dependent task (Requirement details), OR strictly use separate clean clones/worktrees for distinct parallel roles (Architect vs Builder).'
recommendation: 'Use "git worktree" for context switching when roles overlap, or strictly enforce "Finish -> Merge -> Switch" protocol. For now, the "Stash/Commit -> Switch -> Merge -> Switch Back" dance worked but is error-prone.'
---

# Lesson 003: Managing Parallel Workflows

**Context**:
During the execution of **Option 1 (Canonical Stubs)**, we initiated **Option 3 (Manual/Spec Implementation)** tasks (REQ document creation) in the same working directory. When trying to finalize Option 1 (Merge to `main`), Git blocked the checkout.

**Resolution**:
1. Stashed/Committed the WIP `spec-001` changes (REQ files).
2. Switched to `main` to merge the completed `feature/canonical-stubs-batch-1` branch.
3. Created `feature/spec-001-implementation` to properly house the WIP changes.
4. Restored changes to continue work.

**Takeaway**:
Clean separation of concerns applies to Git branches and Working Directories. Do not mix "Infrastructure" work (stubs) with "Content" work (requirements) in the same dirty index.
