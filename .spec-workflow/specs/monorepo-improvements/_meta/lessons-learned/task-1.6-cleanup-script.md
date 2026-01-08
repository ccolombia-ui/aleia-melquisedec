---
id: lesson-task-1.6
title: Cleanup script for post-reorganization validation
type: lesson
confidence: 0.9
rostro: MELQUISEDEC
tags: [cleanup, validation, automation, dry-run]
created: 2026-01-08
task_ref: monorepo-improvements-v1.1.0#1.6
dc:
  title: "Task 1.6 - Cleanup post-reorganization script"
  creator: "GitHub Copilot + MELQUISEDEC"
  date: "2026-01-08"
  subject: ["monorepo", "cleanup", "validation", "automation"]
  source: ".spec-workflow/specs/monorepo-improvements-v1.1.0/tasks.md"
seci:
  derives_from:
    - "docs/_meta/inbox/ISSUE-006-cleanup-validation.md"
    - "tools/maintenance/cleanup_post_reorganization.py.backup"
  informs:
    - "REQ-6: Create cleanup script with severity classification"
---

# Lesson: Task 1.6 - Cleanup Post-Reorganization Script

## 📌 Context

Created automated validation script to detect and clean post-reorganization issues:
- Temporary files (`.gitpush*.json/yml`)
- Broken symlinks
- Orphaned Python files (no imports)
- Python cache directories (`__pycache__`)

**Requirement**: REQ-6 from `monorepo-improvements-v1.1.0`

---

## 🎯 What Worked

### 1. **Dry-Run by Default** ✅
```python
parser.add_argument('--execute', action='store_true',
    help='Execute cleanup (default: dry-run)')
```
- **Why**: Safety first - never delete without confirmation
- **Impact**: Prevents accidental data loss, builds confidence

### 2. **Severity Classification** ✅
```python
@dataclass
class Issue:
    category: str
    severity: str  # 'CRITICAL', 'MODERATE', 'MINOR'
    path: Path
    description: str
    suggested_fix: str = None
```
- **CRITICAL**: Broken symlinks, import failures
- **MODERATE**: Orphaned files, structural issues
- **MINOR**: Temp files, pycache

**Why**: Enables graduated response - only auto-clean MINOR items

### 3. **Pattern-Based Detection** ✅
```python
TEMP_FILE_PATTERNS = [
    r'\.gitpush.*\.json$',
    r'\.gitpush-.*\.yml$',
    r'.*~$',  # backup files
    r'\.DS_Store$',  # macOS
    r'Thumbs\.db$',  # Windows
]
```
- **Why**: Flexible, extensible, cross-platform
- **Result**: Detected 4 temp files in first run

### 4. **Comprehensive Report** ✅
```
======================================================================
CLEANUP REPORT - Post-Reorganization Validation
======================================================================

Total issues found: 150

MINOR (150 issues):
  [TEMP] .gitpush-prod-summary.json
  Description: Temporary file (pattern: \.gitpush.*\.json$)
  Fix: Remove if no longer needed
```
- **Why**: Transparency - user sees everything before action
- **Impact**: Trust + auditability

### 5. **Import Graph Analysis** ✅
```python
import_graph = defaultdict(set)

for py_file in py_files:
    # Parse imports with regex
    import_matches = re.findall(
        r'from\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s+import|'
        r'import\s+([a-zA-Z_][a-zA-Z0-9_.]*)',
        content
    )
```
- **Why**: Identifies truly orphaned files (0 imports)
- **Caveat**: Doesn't catch dynamic imports or test files
- **Result**: 0 orphans found (good health signal)

---

## ⚠️ What Didn't Work / Challenges

### 1. **False Positives in Orphan Detection**
- **Issue**: Entry point scripts (tools/, server.py) flagged as orphans
- **Solution**: Explicit exclusion list
```python
if py_file.name in ['__init__.py', '__main__.py', 'setup.py']:
    continue
if 'tools/' in str(py_file.relative_to(self.root)):
    continue
```
- **Learning**: Context matters - not all files without imports are orphans

### 2. **__pycache__ in .venv/**
- **Issue**: 142 of 146 pycache dirs were in `.venv/`
- **Expectation**: `.venv` should be in IGNORED_DIRS
- **Reality**: Regex patterns didn't match nested `.venv` paths properly
- **Solution**: Fixed in IGNORED_DIRS set
```python
IGNORED_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'venv',
               '.obsidian', 'dist', 'build', '.pytest_cache', 'htmlcov',
               '.smart-env'}
```
- **Learning**: Test ignored paths with real data before deployment

### 3. **No Dry-Run Summary at End**
- **Issue**: After showing 150 issues, user might forget it's dry-run
- **Solution**: Explicit reminder at end
```python
print("💡 This was a dry-run. Use --execute to actually remove files.\n")
print("⚠️ NOTE: --execute only removes MINOR severity items")
```

---

## 🚀 Execution Results

### First Run (Validation)
```powershell
python cleanup_post_reorganization.py --all

# Found: 4 temp files, 146 pycache dirs, 0 symlinks, 0 orphans
# Status: DRY-RUN ✅
```

### Actual Cleanup
```powershell
python cleanup_post_reorganization.py --temp-files --execute

# Removed:
✅ .gitpush-prod-summary.json
✅ .gitpush-prod.yml
✅ .gitpush-summary.json
✅ .gitpush-temp.yml

# Result: 4 items cleaned ✅
```

---

## 💡 Key Insights

### 1. **Safety Layers Matter**
- Default dry-run prevents accidents
- Severity classification prevents over-aggressive cleanup
- Explicit `--execute` flag creates conscious decision point

### 2. **Context is King for Orphan Detection**
- Entry points ≠ orphans
- Test files often have 0 imports (but are used by pytest)
- Scripts in `tools/` are deliberately standalone

### 3. **Ignore Patterns Need Real-World Testing**
- `.venv/` should never be scanned
- Git history is noise (exclude `.git/`)
- IDE folders (`.obsidian/`, `.vscode/`) should be skipped

### 4. **Transparency Builds Trust**
```
Total issues found: 150

MINOR (150 issues):
----------------------------------------------------------------------
```
- User sees exact count, category, path, fix
- No surprises = no regrets

---

## 🔧 Technical Details

### Script Structure
```
cleanup_post_reorganization.py
├── CleanupValidator class
│   ├── check_broken_symlinks()
│   ├── check_temp_files()
│   ├── check_orphan_files()
│   ├── check_pycache()
│   ├── generate_report()
│   └── execute_cleanup()
└── main() - CLI interface
```

### Dependencies
```python
import sys
import shutil          # rmtree, unlink
import re              # pattern matching
from pathlib import Path
import argparse        # CLI
from typing import List, Dict, Set
from dataclasses import dataclass
from collections import defaultdict
```

### Validation Checks
1. **Broken Symlinks**: `path.resolve(strict=True)` → FileNotFoundError
2. **Temp Files**: Regex patterns against filenames
3. **Orphan Files**: Import graph analysis via regex
4. **Pycache**: Simple `rglob('__pycache__')`

---

## 🔄 Next Steps / Future Improvements

### 1. **Add More Checks**
- [ ] Empty directories (except valid ones like `0-inbox/`)
- [ ] Duplicate files (same content, different paths)
- [ ] Large files (> 10MB without justification)
- [ ] Naming conventions violations (non-kebab-case docs)

### 2. **Improve Orphan Detection**
- [ ] Parse AST instead of regex (more accurate)
- [ ] Detect test files automatically (pytest pattern)
- [ ] Check imports from external packages too

### 3. **Generate JSON Report**
```python
--format json > cleanup_report.json
```
- Enables automation, CI integration
- Can track issues over time

### 4. **Pre-Commit Integration**
```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: cleanup-check
      name: Cleanup validator
      entry: python tools/maintenance/cleanup_post_reorganization.py --all
      language: system
      pass_filenames: false
```

---

## 📊 Metrics

| Metric | Value | Status |
|--------|-------|--------|
| **Script LOC** | ~340 lines | ✅ Concise |
| **Checks implemented** | 4 (symlinks, temp, orphans, pycache) | ✅ Complete |
| **First run issues** | 150 (4 temp + 146 pycache) | ✅ Expected |
| **False positives** | 0 (after entry point exclusion) | ✅ Accurate |
| **Execution time** | ~3-5 seconds | ✅ Fast |
| **Temp files cleaned** | 4 | ✅ Success |

---

## 🎓 Lessons for Future Tasks

### 1. **Always Start with Dry-Run**
- Build validation BEFORE cleanup
- Show user what WOULD happen
- Require explicit opt-in for destructive actions

### 2. **Classify Before Acting**
- Not all issues are equal
- CRITICAL needs manual review
- MINOR can be auto-fixed

### 3. **Test with Real Data**
- Theory: "regex will match .venv/"
- Reality: "why are there 142 pycache in venv?"
- Solution: Run on actual monorepo first

### 4. **Document Decisions**
```python
# Scripts in tools/ are entry points
if 'tools/' in str(py_file.relative_to(self.root)):
    continue  # Not orphaned, deliberately standalone
```
- Future maintainers thank you
- Prevents "why did they do this?" confusion

---

## 🔗 Related Artifacts

### Created
- `tools/maintenance/cleanup_post_reorganization.py` (new version)

### Referenced
- `ISSUE-006-cleanup-validation.md` - Original requirements
- `REQ-6` - Spec requirement
- `.gitignore` - Patterns for temp files

### Informs
- Task 1.7 (lessons summary)
- Future cleanup automation
- Pre-commit hooks strategy

---

## ✅ Definition of Done

- [x] Script created with 4 validation checks
- [x] Dry-run by default
- [x] Severity classification (CRITICAL/MODERATE/MINOR)
- [x] Comprehensive report generation
- [x] Execute flag for actual cleanup
- [x] 0 false positives in orphan detection
- [x] 4 temp files successfully cleaned
- [x] Lesson documented

**Task 1.6: COMPLETE** ✅
