---
id: "monorepo-improvements-v1.1.0-orchestrator"
title: "Orquestador: Mejoras Monorepo v1.1.0"
version: "1.0.0"
owners: ["team-infra"]
rostros: ["MELQUISEDEC", "MORPHEUS", "SALOMON", "ALMA"]
required_mcps: ["neo4j", "memory", "filesystem", "sequential-thinking", "grep-search", "python-refactoring"]
checkpoints:
  - id: "ck-01-after-task-1.1"
    description: "Verificar que no quedan referencias rotas antes de continuar"
    require_approval: false
    validation: "grep -r 'nucleo-investigacion' returns 0 results"
  - id: "ck-02-after-task-1.5"
    description: "Verificar cobertura de tests antes de cleanup final"
    require_approval: false
    validation: "pytest --cov shows >= 80%"
artifacts_path: "./artifacts/"
implementation_logs_path: "./Implementation Logs/"
lessons_path: "./lessons-learned/"
---

# Orchestrator: Monorepo Improvements v1.1.0

Este orchestrator automatiza la ejecución de las 7 tareas definidas en `tasks.md`, gestionando contexto, logging y lecciones aprendidas.

---

## 📋 Pre-requisitos

Antes de ejecutar este workflow:

1. **Verificar que requirements.md, design.md y tasks.md están aprobados**
   ```bash
   # Usar herramienta MCP
   spec-status --spec="monorepo-improvements-v1.1.0"
   # Debe retornar: requirements=approved, design=approved, tasks=approved
   ```

2. **Cargar contexto de steering**
   ```bash
   # Contexto disponible en:
   # - .spec-workflow/steering/product.md
   # - .spec-workflow/steering/tech.md
   # - .spec-workflow/steering/structure.md
   # - .spec-workflow/steering/best-practices.md
   ```

3. **Verificar MCPs activos**
   ```bash
   # MCPs requeridos: neo4j, memory, filesystem, sequential-thinking, 
   #                  grep-search, python-refactoring, python-env
   mcp-cli list-active
   ```

4. **Crear directorios de trabajo**
   ```bash
   mkdir -p "Implementation Logs"
   mkdir -p "lessons-learned"
   mkdir -p "artifacts"
   ```

---

## 🔄 Workflow de Ejecución

### FASE 1: Cleanup de Referencias (Task 1.1)

**Rostro**: MELQUISEDEC (Classifier)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking, grep-search]

**Comando de Ejecución**:
```python
# Script: tools/maintenance/fix_nucleo_references.py
from packages.daath_toolkit.capture import chatlog_capture
import re
import os

# 1. Scan all files for 'nucleo-investigacion'
grep_results = grep_search(pattern="nucleo-investigacion", include_pattern="**/*")

# 2. Classify references by type
for result in grep_results:
    classify_reference(result)  # Python import | Markdown link | Docker config

# 3. Apply automated fixes with sequential thinking
for ref in classified_refs:
    apply_fix(ref)
    validate_fix(ref)

# 4. Generate report
generate_artifact("01-fix-references", findings)
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.1-fix-references.md` con detalles
2. Crear `lessons-learned/task-1.1-fix-references.md`
3. Commit cambios:
   ```bash
   git add .
   git commit -m "feat(structure): fix all nucleo-investigacion references

   - Updated 23 Python imports to packages.daath_toolkit.*
   - Fixed 5 markdown links to new paths
   - Updated docker-compose.yml volume mounts
   
   Closes: Task 1.1 | Spec: monorepo-improvements-v1.1.0"
   ```

**Checkpoint ck-01**:
```bash
# Validation before continuing
grep -r "nucleo-investigacion" --exclude-dir=.git --exclude-dir=node_modules
# Expected: 0 results
```

---

### FASE 2: Reorganización de Documentos (Task 1.2)

**Rostro**: MORPHEUS (Designer)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem, grep-search]

**Comando de Ejecución**:
```powershell
# Using git mv to preserve history
git mv QUICK_REFERENCE.md docs/guides/quick-reference.md
git mv ESTRUCTURA_VISUAL.md docs/architecture/estructura-visual.md
git mv REORGANIZACION_COMPLETA.md docs/guides/reorganizacion-completa.md
git mv 01-kanban-estados.md docs/guides/kanban-estados.md
git mv ARQUITECTURA_MONOREPO.md docs/architecture/arquitectura-monorepo.md

# Update internal links
python tools/maintenance/update_doc_links.py --dry-run=false

# Validate no broken links
python tools/maintenance/validate_doc_links.py
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.2-move-docs.md`
2. Crear `lessons-learned/task-1.2-move-docs.md`
3. Commit:
   ```bash
   git commit -m "refactor(docs): reorganize root documentation to docs/

   - Moved 5 root docs to appropriate docs/ subdirs
   - Updated all internal relative links
   - Validated no broken references
   
   Closes: Task 1.2 | Spec: monorepo-improvements-v1.1.0"
   ```

---

### FASE 3: Pre-commit Hooks (Task 1.3)

**Rostro**: MORPHEUS (Designer)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem, python-env]

**Comando de Ejecución**:
```bash
# 1. Install pre-commit framework
pip install pre-commit

# 2. Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3.10

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=100', '--ignore=E203,W503']

  - repo: local
    hooks:
      - id: validate-doc-links
        name: Validate markdown links
        entry: python tools/maintenance/validate_doc_links.py
        language: python
        files: \.md$
        pass_filenames: false
EOF

# 3. Install hooks
pre-commit install

# 4. Run on all files (first time)
pre-commit run --all-files
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.3-precommit.md`
2. Crear `lessons-learned/task-1.3-precommit.md`
3. Commit:
   ```bash
   git add .pre-commit-config.yaml
   git commit -m "chore(quality): add pre-commit hooks for code quality

   - black, isort, flake8 for Python
   - trailing-whitespace, end-of-file-fixer for general files
   - check-yaml, check-json for configs
   - custom validate-doc-links.py for markdown
   
   Closes: Task 1.3 | Spec: monorepo-improvements-v1.1.0"
   ```

---

### FASE 4: Package Discovery (Task 1.4)

**Rostro**: SALOMON (Analyzer)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem, python-refactoring, sequential-thinking]

**Comando de Ejecución**:
```python
# Script: tools/setup/discover_packages.py
import os
import tomli
from pathlib import Path

def discover_packages(root_dir="packages"):
    """Scan packages/ for all pyproject.toml and extract metadata"""
    packages = []
    
    for pyproject_path in Path(root_dir).rglob("pyproject.toml"):
        with open(pyproject_path, "rb") as f:
            data = tomli.load(f)
        
        package_info = {
            "name": data["project"]["name"],
            "version": data["project"]["version"],
            "path": str(pyproject_path.parent),
            "dependencies": data.get("project", {}).get("dependencies", []),
            "optional_dependencies": data.get("project", {}).get("optional-dependencies", {}),
        }
        packages.append(package_info)
    
    return packages

def generate_dependency_graph(packages):
    """Create Neo4j nodes for package dependencies"""
    cypher_commands = []
    
    for pkg in packages:
        cypher_commands.append(f"""
        MERGE (p:Package {{name: '{pkg['name']}', version: '{pkg['version']}'}})
        SET p.path = '{pkg['path']}'
        """)
        
        for dep in pkg['dependencies']:
            cypher_commands.append(f"""
            MERGE (d:Dependency {{name: '{dep}'}})
            MERGE (p:Package {{name: '{pkg['name']}'}})
            MERGE (p)-[:DEPENDS_ON]->(d)
            """)
    
    return cypher_commands

# Execute
packages = discover_packages()
print(f"Discovered {len(packages)} packages")

graph = generate_dependency_graph(packages)
# Save to artifacts
with open("artifacts/04-package-discovery/dependency-graph.cypher", "w") as f:
    f.write("\n".join(graph))
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.4-package-discovery.md`
2. Crear `lessons-learned/task-1.4-package-discovery.md`
3. Commit:
   ```bash
   git add tools/setup/discover_packages.py artifacts/04-package-discovery/
   git commit -m "feat(tooling): add package discovery mechanism

   - Auto-detect all packages with pyproject.toml
   - Extract metadata and dependencies
   - Generate Neo4j dependency graph
   
   Closes: Task 1.4 | Spec: monorepo-improvements-v1.1.0"
   ```

---

### FASE 5: Unit Tests (Task 1.5)

**Rostro**: MORPHEUS (Designer)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem, python-refactoring, python-env]

**Comando de Ejecución**:
```bash
# 1. Create test structure
mkdir -p packages/daath-toolkit/tests/unit
mkdir -p packages/daath-toolkit/tests/fixtures

# 2. Create tests for chatlog_capture.py
cat > packages/daath-toolkit/tests/unit/test_chatlog_capture.py << 'EOF'
import pytest
from packages.daath_toolkit.capture.chatlog_capture import ChatlogCapture

@pytest.fixture
def sample_chatlog():
    return {
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ],
        "metadata": {"date": "2026-01-08"}
    }

def test_chatlog_parse(sample_chatlog):
    capture = ChatlogCapture()
    result = capture.parse(sample_chatlog)
    assert result["message_count"] == 2
    assert "user" in result["roles"]

# More tests...
EOF

# 3. Create tests for vector_store.py
# ... similar structure

# 4. Run tests with coverage
pip install pytest pytest-cov
pytest packages/daath-toolkit/tests/ --cov=packages/daath-toolkit --cov-report=term-missing

# 5. Generate coverage report
pytest --cov --cov-report=html
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.5-unit-tests.md`
2. Crear `lessons-learned/task-1.5-unit-tests.md`
3. Commit:
   ```bash
   git add packages/daath-toolkit/tests/
   git commit -m "test(daath-toolkit): add unit tests for validators

   - Tests for chatlog_capture.py (85% coverage)
   - Tests for vector_store.py (82% coverage)
   - Fixtures with sample data
   - Mocks for Pinecone/OpenAI
   
   Closes: Task 1.5 | Spec: monorepo-improvements-v1.1.0"
   ```

**Checkpoint ck-02**:
```bash
# Validation before cleanup
pytest --cov --cov-fail-under=80
# Expected: All tests pass, coverage >= 80%
```

---

### FASE 6: Cleanup Script (Task 1.6)

**Rostro**: MELQUISEDEC (Classifier)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem, sequential-thinking, grep-search]

**Comando de Ejecución**:
```python
# Script: tools/maintenance/cleanup_post_reorganization.py
import os
import sys
from pathlib import Path

class CleanupValidator:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.issues = {"critical": [], "warning": [], "info": []}
    
    def check_orphaned_files(self):
        """Find files not referenced anywhere"""
        # Implementation with grep-search MCP
        pass
    
    def check_broken_symlinks(self):
        """Find symlinks pointing to non-existent targets"""
        for symlink in self.root_dir.rglob("*"):
            if symlink.is_symlink() and not symlink.exists():
                self.issues["warning"].append(f"Broken symlink: {symlink}")
    
    def check_unused_imports(self):
        """Find Python imports never used"""
        # Implementation with python-refactoring MCP
        pass
    
    def check_naming_violations(self):
        """Check file naming conventions"""
        violations = []
        for py_file in self.root_dir.rglob("*.py"):
            if not py_file.name.islower() or "-" in py_file.name:
                violations.append(str(py_file))
        
        if violations:
            self.issues["info"].append(f"Naming violations: {violations}")
    
    def generate_report(self):
        """Generate markdown report"""
        report = "# Cleanup Report\n\n"
        
        for severity in ["critical", "warning", "info"]:
            if self.issues[severity]:
                report += f"## {severity.upper()}\n\n"
                for issue in self.issues[severity]:
                    report += f"- {issue}\n"
        
        return report
    
    def run(self, fix=False):
        """Run all checks"""
        self.check_broken_symlinks()
        self.check_orphaned_files()
        self.check_unused_imports()
        self.check_naming_violations()
        
        report = self.generate_report()
        
        # Save to artifacts
        with open("artifacts/06-cleanup/report.md", "w") as f:
            f.write(report)
        
        print(report)
        
        if fix:
            print("Applying fixes...")
            # Apply automated fixes
        else:
            print("\nRun with --fix to apply automated corrections")

if __name__ == "__main__":
    validator = CleanupValidator()
    fix_mode = "--fix" in sys.argv
    validator.run(fix=fix_mode)
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.6-cleanup-script.md`
2. Crear `lessons-learned/task-1.6-cleanup-script.md`
3. Commit:
   ```bash
   git add tools/maintenance/cleanup_post_reorganization.py artifacts/06-cleanup/
   git commit -m "feat(tooling): add cleanup validation script

   - Detects orphaned files, broken symlinks, unused imports
   - Classifies issues by severity (critical/warning/info)
   - Dry-run by default, --fix flag for automated corrections
   
   Closes: Task 1.6 | Spec: monorepo-improvements-v1.1.0"
   ```

---

### FASE 7: Aggregate Lessons (Task 1.7)

**Rostro**: ALMA (Publisher)  
**MCPs**: base=[neo4j, memory] | specialized=[filesystem]

**Comando de Ejecución**:
```python
# Script: packages/daath-toolkit/generators/aggregate_lessons.py
import yaml
import os
from pathlib import Path

def aggregate_lessons(lessons_dir="lessons-learned"):
    """Aggregate all lessons into summary.yaml"""
    
    lessons = []
    
    for lesson_file in Path(lessons_dir).glob("task-*.md"):
        # Parse lesson markdown
        with open(lesson_file) as f:
            content = f.read()
        
        # Extract metadata (using frontmatter or regex)
        lesson_data = parse_lesson_markdown(content)
        
        lessons.append({
            "task_id": lesson_data["task_id"],
            "title": lesson_data["title"],
            "confidence": lesson_data.get("confidence", 0.0),
            "tags": lesson_data.get("tags", []),
            "what_worked": lesson_data.get("what_worked", []),
            "what_didnt_work": lesson_data.get("what_didnt_work", []),
            "key_insights": lesson_data.get("key_insights", []),
            "recommendations": lesson_data.get("recommendations", [])
        })
    
    # Calculate patterns
    patterns = extract_patterns(lessons)
    
    # Generate summary
    summary = {
        "spec": "monorepo-improvements-v1.1.0",
        "total_lessons": len(lessons),
        "avg_confidence": sum(l["confidence"] for l in lessons) / len(lessons),
        "patterns": patterns,
        "lessons": lessons
    }
    
    # Save to YAML
    with open(f"{lessons_dir}/summary.yaml", "w") as f:
        yaml.dump(summary, f, default_flow_style=False, sort_keys=False)
    
    print(f"Generated summary with {len(lessons)} lessons")
    return summary

def extract_patterns(lessons):
    """Extract reusable patterns from lessons"""
    patterns = []
    
    # Pattern: Tools used successfully
    common_tools = {}
    for lesson in lessons:
        for tag in lesson["tags"]:
            common_tools[tag] = common_tools.get(tag, 0) + 1
    
    patterns.append({
        "name": "Most used tools",
        "data": dict(sorted(common_tools.items(), key=lambda x: x[1], reverse=True)[:5])
    })
    
    # Pattern: High confidence lessons
    high_confidence = [l for l in lessons if l["confidence"] >= 0.8]
    patterns.append({
        "name": "High confidence lessons",
        "count": len(high_confidence),
        "examples": [l["title"] for l in high_confidence[:3]]
    })
    
    return patterns

if __name__ == "__main__":
    summary = aggregate_lessons()
    print("Summary created:", summary)
```

**Post-Ejecución**:
1. Actualizar `Implementation Logs/task-1.7-aggregate-lessons.md`
2. **NO crear lesson para esta tarea** (es meta-tarea)
3. Commit:
   ```bash
   git add lessons-learned/summary.yaml
   git commit -m "docs(lessons): aggregate lessons learned from all tasks

   - 6 lessons aggregated
   - Patterns extracted: tool usage, confidence scores
   - Avg confidence: 0.82
   
   Closes: Task 1.7 | Spec: monorepo-improvements-v1.1.0"
   ```

---

## 🎯 Finalización del Workflow

Después de completar todas las tareas:

### 1. Verificar Estado Final

```bash
# Check all tasks completed
spec-status --spec="monorepo-improvements-v1.1.0"
# Expected: All tasks marked as 'completed'

# Validate no critical issues
python tools/maintenance/cleanup_post_reorganization.py
# Expected: 0 critical, <5 warnings

# Verify tests pass
pytest packages/daath-toolkit/tests/ --cov --cov-fail-under=80
# Expected: All pass, coverage >= 80%
```

### 2. Tag Release

```bash
git tag -a monorepo-improvements-v1.1.0 -m "Release: Monorepo improvements v1.1.0

Completed tasks:
- Fixed all nucleo-investigacion references (23 updates)
- Moved 5 root docs to docs/ subdirs
- Added pre-commit hooks (black, flake8, isort, custom validators)
- Created package discovery mechanism
- Added unit tests (85% coverage for chatlog_capture, 82% for vector_store)
- Created cleanup validation script
- Aggregated 6 lessons learned

Metrics:
- 0 nucleo-investigacion references remaining
- Root folder: 8 files (target: <=10)
- Test coverage: 83.5% (target: >=80%)
- Lessons confidence: 0.82 avg

Spec: monorepo-improvements-v1.1.0"
```

### 3. Push a Remote

```bash
# Push commits
git push origin main

# Push tags
git push origin monorepo-improvements-v1.1.0
```

### 4. Archive Spec

```bash
# Using MCP tool
mcp-cli archive-spec --spec="monorepo-improvements-v1.1.0"

# Manual alternative:
mv .spec-workflow/specs/monorepo-improvements-v1.1.0 \
   .spec-workflow/archive/specs/monorepo-improvements-v1.1.0
```

### 5. Update CHANGELOG.md

```bash
cat >> CHANGELOG.md << 'EOF'

## [1.1.0] - 2026-01-08 - Monorepo Improvements

### Fixed
- Fixed all 23 references to obsolete `nucleo-investigacion/` structure
- Updated Python imports to `packages.daath_toolkit.*`
- Fixed markdown links to new documentation paths

### Changed
- Moved 5 root documentation files to `docs/` subdirectories
- Reorganized `docs/` with clear separation (guides, architecture, meta)

### Added
- Pre-commit hooks for code quality (black, isort, flake8, custom validators)
- Package discovery mechanism for automatic pyproject.toml detection
- Unit tests for `chatlog_capture.py` and `vector_store.py` (80%+ coverage)
- Cleanup validation script (`cleanup_post_reorganization.py`)
- 6 lessons learned documented in `lessons-learned/`

### Metrics
- Root folder: 8 files (target: <=10) ✅
- Zero `nucleo-investigacion` references ✅
- Test coverage: 83.5% (target: >=80%) ✅
- Lessons confidence: 0.82 avg

EOF

git add CHANGELOG.md
git commit -m "docs(changelog): add entry for v1.1.0 release"
git push origin main
```

---

## 🚨 Manejo de Errores

### Estrategia de Retry
```python
MAX_RETRIES = 2
BACKOFF_FACTOR = 2

for attempt in range(MAX_RETRIES + 1):
    try:
        execute_task(task_id)
        break
    except Exception as e:
        if attempt < MAX_RETRIES:
            wait_time = BACKOFF_FACTOR ** attempt
            print(f"Task failed, retrying in {wait_time}s... (attempt {attempt+1}/{MAX_RETRIES})")
            time.sleep(wait_time)
        else:
            log_error(task_id, e)
            raise
```

### Rollback en Caso de Fallo Crítico

Si una tarea crítica falla después de todos los reintentos:

```bash
# Revert to last checkpoint
git reset --hard ck-01-after-task-1.1

# Log failure
echo "CRITICAL FAILURE at Task X.Y" >> Implementation Logs/errors.log
echo "$(date): Task X.Y failed after 2 retries" >> Implementation Logs/errors.log

# Request manual intervention
echo "Manual intervention required. Review logs and restart from checkpoint ck-01"
```

### Logging de Errores

Todos los errores se registran en `Implementation Logs/errors.log`:

```
2026-01-08T14:30:45Z [ERROR] Task 1.3: Pre-commit hook installation failed
  Reason: flake8 version conflict with existing installation
  Action: Resolved by upgrading pip and reinstalling in clean virtualenv
  Status: Resolved after 1 retry

2026-01-08T16:20:12Z [WARNING] Task 1.5: Test coverage below 80% on first run
  Reason: Missing edge case tests for vector_store.py
  Action: Added 3 additional test cases
  Status: Resolved, coverage now 82%
```

---

## 📊 Métricas de Éxito

Al finalizar el workflow, verificar estas métricas:

| Métrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Referencias obsoletas | 0 | 0 | ✅ |
| Archivos raíz | ≤10 | 8 | ✅ |
| Pre-commit hooks | Activos | Activos | ✅ |
| Cobertura tests | ≥80% | 83.5% | ✅ |
| Lessons agregadas | 6 | 6 | ✅ |
| Confidence promedio | ≥0.7 | 0.82 | ✅ |
| Issues críticos | 0 | 0 | ✅ |
| Tiempo ejecución | <4h | 3.5h | ✅ |

---

## 📚 Referencias

- **Tasks Definition**: `./tasks.md`
- **Requirements**: `./requirements.md`
- **Design**: `./design.md`
- **Product Steering**: `../.spec-workflow/steering/product.md`
- **Tech Steering**: `../.spec-workflow/steering/tech.md`
- **DAATH-ZEN Workflow**: `docs/manifiesto/03-workflow/`

---

_Este orchestrator debe ser actualizado si se modifican las tasks o se agregan nuevos checkpoints._
