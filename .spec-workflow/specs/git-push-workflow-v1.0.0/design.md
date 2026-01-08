# Design: Git Push Workflow

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                 GIT PUSH WORKFLOW                    │
└─────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────┐
│  STAGE 1: PRE-COMMIT VALIDATION (MORPHEUS)          │
│  - Syntax check (pylint, mypy)                      │
│  - Formatter (black, isort)                         │
│  - Linter (flake8)                                  │
│  MCPs: filesystem, python-env, python-refactoring   │
└─────────────────────────────────────────────────────┘
           │ PASS
           ▼
┌─────────────────────────────────────────────────────┐
│  STAGE 2: TEST EXECUTION (MORPHEUS)                 │
│  - Detect changed modules                           │
│  - Run pytest on affected tests                     │
│  - Report coverage                                  │
│  MCPs: python-env, filesystem                       │
└─────────────────────────────────────────────────────┘
           │ PASS
           ▼
┌─────────────────────────────────────────────────────┐
│  STAGE 3: BRANCH VALIDATION (MELQUISEDEC)           │
│  - Check git status                                 │
│  - Validate branch name                             │
│  - Check upstream tracking                          │
│  MCPs: git, sequential-thinking                     │
└─────────────────────────────────────────────────────┘
           │ OK
           ▼
┌─────────────────────────────────────────────────────┐
│  STAGE 4: COMMIT (ALMA)                             │
│  - Generate/validate commit message                 │
│  - Include metadata (spec, task, rostro)            │
│  - Execute git commit                               │
│  MCPs: git, filesystem, memory                      │
└─────────────────────────────────────────────────────┘
           │ COMMITTED
           ▼
┌─────────────────────────────────────────────────────┐
│  STAGE 5: PUSH (ALMA)                               │
│  - Push to upstream                                 │
│  - Handle conflicts                                 │
│  - Report success/failure                           │
│  MCPs: git, github                                  │
└─────────────────────────────────────────────────────┘
           │ PUSHED
           ▼
┌─────────────────────────────────────────────────────┐
│  STAGE 6: POST-PUSH (ALMA)                          │
│  - Update Neo4j graph                               │
│  - Create tags if release                           │
│  - Log to memory                                    │
│  MCPs: neo4j, memory, git                           │
└─────────────────────────────────────────────────────┘
```

---

## Component Design

### 1. Pre-Commit Hook Script

**Location**: `.git/hooks/pre-commit`

**Responsibilities**:
- Run linters and formatters
- Fast-fail on errors
- Display clear error messages

**Pseudo-code**:
```python
def pre_commit_hook():
    changed_files = get_staged_files()
    
    # Filter by file type
    python_files = [f for f in changed_files if f.endswith('.py')]
    md_files = [f for f in changed_files if f.endswith('.md')]
    
    # Run checks in parallel
    results = []
    if python_files:
        results.append(run_black(python_files))
        results.append(run_flake8(python_files))
        results.append(run_isort(python_files))
        results.append(run_mypy(python_files))
    
    if md_files:
        results.append(run_markdownlint(md_files))
    
    if any(r.failed for r in results):
        print_errors(results)
        return EXIT_FAILURE
    
    return EXIT_SUCCESS
```

### 2. Test Runner

**Location**: `tools/testing/run_affected_tests.py`

**Responsibilities**:
- Detect changed Python modules
- Map to test files
- Run pytest with coverage

**Pseudo-code**:
```python
def run_affected_tests(changed_files):
    # Map source files to test files
    test_files = []
    for src in changed_files:
        if src.startswith('packages/'):
            pkg = extract_package_name(src)
            test_files.extend(find_tests_for_package(pkg))
    
    if not test_files:
        print("No tests affected, skipping")
        return EXIT_SUCCESS
    
    # Run pytest
    result = subprocess.run([
        'pytest',
        '--cov',
        '--cov-report=term-missing',
        *test_files
    ])
    
    return result.returncode
```

### 3. Branch Validator

**Location**: `tools/git/validate_branch.py`

**Responsibilities**:
- Check git status
- Validate branch name follows conventions
- Warn on protected branches

**Pseudo-code**:
```python
def validate_branch():
    # Get current branch
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
    
    # Check if on main
    if branch == 'main':
        response = input("⚠️  You're on main. Create a feature branch? (y/n): ")
        if response.lower() == 'y':
            return suggest_branch_creation()
        elif response.lower() != 'n':
            return EXIT_FAILURE
    
    # Validate branch name format
    if not re.match(r'^(spec|hotfix|docs)/[\w-]+', branch):
        print(f"⚠️  Branch name '{branch}' doesn't follow convention")
        print("Expected: spec/<name> or hotfix/<name> or docs/<name>")
    
    # Check upstream
    try:
        subprocess.check_output(['git', 'rev-parse', '@{u}'])
    except:
        print("⚠️  No upstream tracking. Run: git push -u origin", branch)
        return EXIT_FAILURE
    
    return EXIT_SUCCESS
```

### 4. Commit Message Generator

**Location**: `tools/git/generate_commit_msg.py`

**Responsibilities**:
- Extract context from branch/spec
- Generate conventional commit message
- Include metadata

**Pseudo-code**:
```python
def generate_commit_message():
    # Get branch name
    branch = get_current_branch()
    
    # Extract spec from branch (e.g., spec/git-push-workflow-v1.0.0)
    spec_match = re.match(r'spec/([\w-]+)-v(\d+\.\d+\.\d+)', branch)
    if spec_match:
        spec_name = spec_match.group(1)
        version = spec_match.group(2)
    else:
        spec_name = None
        version = None
    
    # Get staged files to infer type
    changed_files = get_staged_files()
    commit_type = infer_commit_type(changed_files)
    
    # Prompt for task ID and description
    task_id = input("Task ID (e.g., 1.1): ").strip()
    description = input("Brief description: ").strip()
    
    # Read spec context if available
    rostro = None
    mcps = None
    if spec_name:
        task_info = read_task_from_spec(spec_name, task_id)
        rostro = task_info.get('rostro')
        mcps = task_info.get('mcps')
    
    # Generate message
    message = f"{commit_type}({spec_name}): {task_id} {description}\n\n"
    message += f"Spec: {spec_name}-v{version}\n"
    message += f"Task: {task_id}\n"
    if rostro:
        message += f"Rostro: {rostro}\n"
    if mcps:
        message += f"MCPs: {mcps}\n"
    message += f"Lesson: lessons-learned/task-{task_id}-lesson.md\n"
    
    return message
```

### 5. Push Handler

**Location**: `tools/git/push_workflow.py`

**Responsibilities**:
- Execute git push
- Handle authentication
- Report results

**Pseudo-code**:
```python
def push_to_remote(dry_run=False):
    branch = get_current_branch()
    
    # Get unpushed commits
    unpushed = get_unpushed_commits()
    print(f"📦 Pushing {len(unpushed)} commit(s) to origin/{branch}")
    
    for commit in unpushed:
        print(f"  - {commit['hash'][:7]}: {commit['message']}")
    
    if dry_run:
        print("🧪 Dry-run mode, not pushing")
        return EXIT_SUCCESS
    
    # Push
    result = subprocess.run(['git', 'push', 'origin', branch])
    
    if result.returncode == 0:
        print("✅ Successfully pushed to origin/" + branch)
        return EXIT_SUCCESS
    else:
        print("❌ Push failed. Check errors above.")
        return EXIT_FAILURE
```

### 6. Post-Push Neo4j Logger

**Location**: `tools/git/log_to_neo4j.py`

**Responsibilities**:
- Log commit to Neo4j
- Create relationships to spec/task

**Pseudo-code**:
```cypher
// Log commit to Neo4j
CREATE (c:Commit {
  hash: $commit_hash,
  message: $commit_message,
  author: $author,
  timestamp: datetime(),
  branch: $branch
})

// Link to spec
MATCH (s:Spec {id: $spec_id})
CREATE (c)-[:IMPLEMENTS]->(s)

// Link to task
MATCH (t:Task {id: $task_id})
CREATE (c)-[:COMPLETES]->(t)

// Link to rostro
MATCH (r:Rostro {name: $rostro_name})
CREATE (c)-[:EXECUTED_BY]->(r)
```

---

## Data Flow

```
User → git add → Pre-commit hook → Linters/Formatters
                        ↓
                   [PASS/FAIL]
                        ↓ PASS
User → git commit → Test runner → pytest
                        ↓
                   [PASS/FAIL]
                        ↓ PASS
               Branch validator → Status check
                        ↓
                   [OK/WARNING]
                        ↓ OK
            Commit msg generator → Prompt user
                        ↓
                User confirms
                        ↓
                  git commit -m
                        ↓
              User runs push_workflow.py
                        ↓
              Push handler → git push
                        ↓
                   [SUCCESS/FAIL]
                        ↓ SUCCESS
            Post-push logger → Neo4j + Memory
                        ↓
                      DONE
```

---

## Error Handling

### Pre-commit Failures
- Display specific linter errors
- Suggest auto-fix commands
- Allow bypass with `--no-verify` (not recommended)

### Test Failures
- Show pytest output
- Display coverage report
- Suggest running locally: `pytest -v`

### Push Conflicts
- Detect merge conflicts
- Suggest: `git pull --rebase origin <branch>`
- Retry after resolution

### Authentication Errors
- Check SSH keys or tokens
- Suggest: `gh auth login`
- Provide documentation link

---

## Configuration

### Configurable `.gitpush.yml` (recommended)
Create a repo-local `.gitpush.yml` to configure stages and behavior. This lets the push workflow be reused as the final task in other workflows (CI or scripts) and supports a minimal default.

Example `.gitpush.yml`:
```yaml
# .gitpush.yml - configuration for push_workflow.py
stages:
  pre_commit: true          # run pre-commit hooks (default true)
  tests: true               # run affected tests (default true)
  branch_validate: true     # validate branch (warn or fail)
  commit: true              # commit staged changes (if commit_message provided or auto)
  push: true                # push to upstream
  post_push: false          # run post-push tasks (neo4j logging)

# Minimal mode uses fewer stages for speed
minimal: false

# Behavior flags
dry_run: false              # if true, don't push
non_interactive: true       # use defaults, avoid prompts (useful for CI)
commit_message: null        # if set, use this message to commit
failure_mode: fail_fast     # 'fail_fast' or 'warn' (for branch validation, tests)

# Optional: path to test runner or custom scripts
runners:
  tests: tools/testing/run_affected_tests.py
  branch_validate: tools/git/validate_branch.py
  commit_msg_generator: tools/git/generate_commit_msg.py
```

**Notes**:
- `non_interactive: true` is recommended when this script runs as a final task in CI/CD workflows.
- `minimal: true` overrides stages to a minimal set: `pre_commit` + `push`.
- `failure_mode: warn` allows pushing even when validation shows warnings; `fail_fast` will stop the workflow.

### .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
        language_version: python3.10
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=88']
  
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ['--profile', 'black']
```

### pyproject.toml (pytest config)
```toml
[tool.pytest.ini_options]
minversion = "7.0"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov --cov-report=term-missing --cov-report=html"
```

---

## Integration as final task in CI/CD

To use this workflow as the final step in another workflow (for example a GitHub Actions job), invoke `tools/git/push_workflow.py` with `--non-interactive --dry-run=false` and a repo-local `.gitpush.yml` configured for CI (set `non_interactive: true`, `minimal: false`). Example GitHub Actions step:

```yaml
- name: Run git push workflow
  run: python tools/git/push_workflow.py --config .gitpush.yml --non-interactive
```

Key points:
- Use `--non-interactive` for CI so prompts are avoided
- Use `--dry-run` to test the workflow without pushing
- The script returns non-zero exit codes on failure (unless `failure_mode: warn`), which makes it suitable as a final step that gates the job

---

## Alternatives Considered

### 1. GitHub Actions for Pre-Push
**Pros**: Centralized, no local setup
**Cons**: Slow feedback loop, requires push to fail
**Decision**: Use local pre-commit hooks for fast feedback

### 2. Husky (npm) for Git Hooks
**Pros**: Popular, well-documented
**Cons**: Adds Node.js dependency to Python project
**Decision**: Use native git hooks + pre-commit framework

### 3. Manual Commit Messages
**Pros**: Flexibility
**Cons**: Inconsistent, error-prone
**Decision**: Generate template, allow editing

---

## Security Considerations

- Never commit secrets (use .gitignore)
- Validate remote URL before push
- Use SSH keys or tokens, not passwords
- Log all push attempts to audit trail

---

## Performance Optimizations

- Run linters in parallel (concurrent.futures)
- Cache test results (pytest-cache)
- Skip tests if no code changed
- Use incremental type checking (mypy)

---

## Future Enhancements

- Auto-create PR after push
- Integrate with Jira/Linear
- Slack notifications
- Auto-changelog generation
