# Git Push Workflow

## Purpose

Este documento explica cómo usar el `git-push-workflow` como herramienta configurable y minimalista para orquestar la secuencia: pre-commit → tests → branch validation → commit → push → post-push. Está pensado para uso local y como paso final en pipelines CI.

## Key Features

- Archivo de configuración `.gitpush.yml` (opcional) para controlar etapas y comportamiento
- CLI `tools/git/push_workflow.py` con flags `--dry-run`, `--non-interactive`, `--minimal`, `--config`
- Minimal mode (sólo `pre_commit` + `push`) para rapidez
- `--json-output` para integrarlo en CI y recoger un resumen estructurado
- Exit codes adecuados para usar como condición de éxito/fallo en pipelines

## Example `.gitpush.yml`
```yaml
stages:
  pre_commit: true
  tests: true
  branch_validate: true
  commit: true
  push: true
  post_push: false
minimal: false
non_interactive: true
failure_mode: fail_fast
```

## Usage

### Local (interactive)
```bash
python tools/git/push_workflow.py --config .gitpush.yml
```

### Non-interactive (CI / final job in another workflow)
```bash
python tools/git/push_workflow.py --config .gitpush.yml --non-interactive --json-output /tmp/push-summary.json
```

### Dry-run
```bash
python tools/git/push_workflow.py --dry-run --config .gitpush.yml
```

### Minimal (fast)
```bash
python tools/git/push_workflow.py --minimal --config .gitpush.yml
```

## Example GitHub Actions snippet
```yaml
jobs:
  push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run push workflow
        run: python tools/git/push_workflow.py --config .gitpush.yml --non-interactive --json-output push-summary.json
```

## Integration Notes
- Ensure `pre-commit` is installed in CI if you enable `pre_commit` stage, or set `pre_commit: false` in `.gitpush.yml`
- Use `non_interactive: true` in `.gitpush.yml` for CI usage to avoid prompts
- The script returns non-zero when any enabled stage fails (unless `failure_mode: warn`)

## Minimal & Efficiency Considerations
- Default minimal mode helps fast pushes for doc-only changes or quick iterations
- Keep heavy stages (full test suite, long linters) disabled by default in CI and only enable in branches where required

## Troubleshooting
- If `pre-commit` not found: install via `pip install pre-commit`
- If `git` commands fail: check credentials and run `gh auth login` for GitHub tokens

## Extensibility
- Add custom stage runners in `.gitpush.yml` under `runners:` (point to local scripts)
- The script writes a JSON summary that can be parsed to generate release notes or trigger downstream jobs
