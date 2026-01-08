#!/usr/bin/env python3
"""Push workflow CLI

Usage:
  python tools/git/push_workflow.py [--config .gitpush.yml] [--dry-run]
  [--non-interactive] [--minimal]

Features:
- Reads .gitpush.yml (optional) to control stages
- Supports flags: --dry-run, --non-interactive, --minimal
- Stages: pre_commit, tests, branch_validate, commit, push, post_push
- Minimal default executes: pre_commit + push
- Returns non-zero exit codes on failure (unless failure_mode=warn)
- Emits JSON summary on completion when --json-output is provided
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict

try:
    import yaml
except Exception:
    yaml = None


DEFAULT_CONFIG = {
    "stages": {
        "pre_commit": True,
        "tests": False,
        "branch_validate": False,
        "commit": False,
        "push": True,
        "post_push": False,
    },
    # minimal mode will only run pre_commit + push
    "minimal": True,
    "dry_run": False,
    "non_interactive": True,
    "commit_message": None,
    "failure_mode": "fail_fast",
    "runners": {
        "tests": "tools/testing/run_affected_tests.py",
        "branch_validate": "tools/git/validate_branch.py",
        "commit_msg_generator": "tools/git/generate_commit_msg.py",
    },
}


@dataclass
class StageResult:
    name: str
    ok: bool
    code: int
    message: str = ""


def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return DEFAULT_CONFIG.copy()
    if yaml is None:
        print("⚠️  PyYAML not installed, ignoring config file", file=sys.stderr)
        return DEFAULT_CONFIG.copy()
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    cfg = DEFAULT_CONFIG.copy()
    cfg.update(data)
    # merge stages if present
    if "stages" in data:
        cfg["stages"].update(data["stages"])
    if "runners" in data:
        cfg["runners"].update(data["runners"])
    return cfg


def run_subprocess(cmd, check=True, capture_output=False, text=True):
    print(f"$ {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=capture_output, text=text)


def stage_pre_commit() -> StageResult:
    # Prefer pre-commit if available
    try:
        r = run_subprocess(["pre-commit", "run", "--all-files"], check=False)
        ok = r.returncode == 0
        return StageResult("pre_commit", ok, r.returncode, r.stdout or r.stderr or "")
    except FileNotFoundError:
        return StageResult("pre_commit", False, 127, "pre-commit not installed")


def stage_tests(runner: str) -> StageResult:
    if not Path(runner).exists():
        return StageResult("tests", False, 127, f"tests runner not found: {runner}")
    try:
        r = run_subprocess([sys.executable, runner], check=False)
        ok = r.returncode == 0
        return StageResult("tests", ok, r.returncode, r.stdout or r.stderr or "")
    except Exception as e:
        return StageResult("tests", False, 1, str(e))


def stage_branch_validate(runner: str, non_interactive: bool) -> StageResult:
    if not Path(runner).exists():
        return StageResult(
            "branch_validate", False, 127, f"branch_validate runner not found: {runner}"
        )
    try:
        cmd = [sys.executable, runner]
        if non_interactive:
            cmd.append("--non-interactive")
        r = run_subprocess(cmd, check=False)
        ok = r.returncode == 0
        return StageResult("branch_validate", ok, r.returncode, r.stdout or r.stderr or "")
    except Exception as e:
        return StageResult("branch_validate", False, 1, str(e))


def get_current_branch() -> str:
    try:
        out = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        return out
    except Exception:
        return "unknown"


def stage_commit(
    commit_message: str | None, non_interactive: bool, files: list | None = None
) -> StageResult:
    # If commit_message is None and non_interactive, skip commit stage
    if commit_message is None and non_interactive:
        return StageResult("commit", True, 0, "skipped (non-interactive + no message)")
    # If message is None: try to generate via generator
    if commit_message is None:
        # best-effort: call generator if exists
        gen = Path("tools/git/generate_commit_msg.py")
        if gen.exists():
            try:
                r = run_subprocess([sys.executable, str(gen)], check=False, capture_output=True)
                if r.returncode == 0:
                    commit_message = r.stdout.strip()
                else:
                    commit_message = None
            except Exception:
                commit_message = None
    if commit_message is None:
        return StageResult("commit", False, 2, "no commit message provided and generator failed")
    # Perform commit
    try:
        if files:
            # add explicit file list
            # allow globs; use shell expansion via git add --
            cmd = ["git", "add", "--"] + files
            run_subprocess(cmd, check=True)
        else:
            run_subprocess(["git", "add", "-A"], check=True)
        run_subprocess(["git", "commit", "-m", commit_message], check=False)
        return StageResult("commit", True, 0, "committed")
    except subprocess.CalledProcessError as e:
        return StageResult("commit", False, e.returncode, str(e))


def stage_push(
    dry_run: bool, target_branch: str | None = None, allow_branch_push: bool = False
) -> StageResult:
    current = get_current_branch()
    branch = target_branch or current
    # If user requested a different branch but branch pushes are not allowed, error
    if branch != current and not allow_branch_push:
        return StageResult(
            "push",
            False,
            3,
            (
                f"refusing to push to branch '{branch}' "
                f"(different from current '{current}'). "
                "Enable allow_branch_push in config or pass --allow-branch-push to override)"
            ),
        )
    if dry_run:
        return StageResult("push", True, 0, f"dry-run: would push to origin/{branch}")
    try:
        r = run_subprocess(["git", "push", "origin", branch], check=False)
        ok = r.returncode == 0
        return StageResult("push", ok, r.returncode, r.stdout or r.stderr or "")
    except Exception as e:
        return StageResult("push", False, 1, str(e))


def stage_post_push(runner: str) -> StageResult:
    if not Path(runner).exists():
        return StageResult("post_push", False, 127, f"post_push runner not found: {runner}")
    try:
        r = run_subprocess([sys.executable, runner], check=False)
        ok = r.returncode == 0
        return StageResult("post_push", ok, r.returncode, r.stdout or r.stderr or "")
    except Exception as e:
        return StageResult("post_push", False, 1, str(e))


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=".gitpush.yml")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--non-interactive", action="store_true")
    p.add_argument("--minimal", action="store_true")
    p.add_argument("--commit-message", help="Commit message to use (overrides generator)")
    p.add_argument(
        "--files",
        help="Comma-separated list of files or globs to include in commit (default: all staged)",
    )
    p.add_argument(
        "--branch",
        help=(
            "Target branch to push to (default: current branch). "
            "NOTE: branches are only used if allowed in config"
        ),
    )
    p.add_argument(
        "--allow-branch-push",
        action="store_true",
        help=(
            "Allow pushing to a branch different than the current local branch "
            "(default false unless enabled in config)"
        ),
    )
    p.add_argument("--json-output", help="Path to write JSON summary")
    args = p.parse_args(argv)

    cfg = load_config(Path(args.config))
    # apply CLI overrides
    if args.dry_run:
        cfg["dry_run"] = True
    if args.non_interactive:
        cfg["non_interactive"] = True
    if args.minimal:
        cfg["minimal"] = True
        # minimal mode: only pre_commit + push
        cfg["stages"] = {k: False for k in cfg["stages"]}
        cfg["stages"]["pre_commit"] = True
        cfg["stages"]["push"] = True

    # CLI-level file/branch overrides
    if args.files:
        cfg["files"] = [f.strip() for f in args.files.split(",") if f.strip()]
    if args.branch:
        cfg["branch"] = args.branch
    if args.allow_branch_push:
        cfg["allow_branch_push"] = True

    if cfg.get("minimal"):
        cfg["stages"] = {k: False for k in cfg["stages"]}
        cfg["stages"]["pre_commit"] = True
        cfg["stages"]["push"] = True

    results = []

    def handle_result(res: StageResult):
        print(f"[{res.name}] {'OK' if res.ok else 'FAIL'} (code={res.code}) {res.message}")
        results.append(asdict(res))
        return res.ok

    # Execute stages in order if enabled
    stages_cfg = cfg["stages"]

    # 1. pre-commit
    if stages_cfg.get("pre_commit"):
        res = stage_pre_commit()
        ok = handle_result(res)
        if not ok and cfg.get("failure_mode") == "fail_fast":
            print("Fail-fast on pre_commit")
            sys.exit(res.code or 1)

    # 2. tests
    if stages_cfg.get("tests"):
        res = stage_tests(cfg["runners"].get("tests"))
        ok = handle_result(res)
        if not ok and cfg.get("failure_mode") == "fail_fast":
            print("Fail-fast on tests")
            sys.exit(res.code or 1)

    # 3. branch validation
    if stages_cfg.get("branch_validate"):
        res = stage_branch_validate(
            cfg["runners"].get("branch_validate"), cfg.get("non_interactive")
        )
        ok = handle_result(res)
        if not ok and cfg.get("failure_mode") == "fail_fast":
            print("Fail-fast on branch validation")
            sys.exit(res.code or 1)

    # Prompt for parameters if needed (agent must ask files and branch when interactive)
    files_param = cfg.get("files")
    branch_param = cfg.get("branch")
    allow_branch_push = cfg.get("allow_branch_push", False)

    if stages_cfg.get("commit"):
        # If interactive and missing files, ask
        if not files_param and not cfg.get("non_interactive"):
            resp = input("Files to include in commit (comma-separated, empty = all): ").strip()
            files_param = [f.strip() for f in resp.split(",") if f.strip()] if resp else None
        # Commit stage
        res = stage_commit(
            args.commit_message or cfg.get("commit_message"),
            cfg.get("non_interactive"),
            files=files_param,
        )
        ok = handle_result(res)
        if not ok and cfg.get("failure_mode") == "fail_fast":
            print("Fail-fast on commit")
            sys.exit(res.code or 1)

    # 5. push
    if stages_cfg.get("push"):
        # If interactive and missing branch, ask
        if not branch_param and not cfg.get("non_interactive"):
            resp = input("Target branch to push to (empty = current branch): ").strip()
            branch_param = resp if resp else None
        res = stage_push(
            cfg.get("dry_run") or args.dry_run,
            target_branch=branch_param,
            allow_branch_push=allow_branch_push,
        )
        ok = handle_result(res)
        if not ok and cfg.get("failure_mode") == "fail_fast":
            print("Fail-fast on push")
            sys.exit(res.code or 1)

    # 6. post_push
    if stages_cfg.get("post_push"):
        res = stage_post_push(
            cfg["runners"].get("post_push")
            or cfg["runners"].get("log_to_neo4j", "tools/git/log_to_neo4j.py")
        )
        handle_result(res)

    summary = {"config_used": cfg, "results": results}
    if args.json_output:
        with open(args.json_output, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, indent=2)
    print(json.dumps(summary, indent=2))
    # Exit code: 0 if all OK, otherwise 1
    if all(r["ok"] for r in results):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
