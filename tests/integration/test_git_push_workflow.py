import os
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path("tools/git/push_workflow.py")

@pytest.mark.skipif(not SCRIPT.exists(), reason="Script not present")
def test_help_exit_zero():
    r = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "Push workflow CLI" in r.stdout or "Usage" in r.stdout

# Basic dry-run test (non destructive)
@pytest.mark.skipif(not SCRIPT.exists(), reason="Script not present")
def test_dry_run_minimal():
    r = subprocess.run([sys.executable, str(SCRIPT), "--dry-run", "--minimal"], capture_output=True, text=True)
    # Script should exit 0 on dry run minimal
    assert r.returncode == 0
    assert '"push"' in r.stdout

@pytest.mark.skipif(not SCRIPT.exists(), reason="Script not present")
def test_requires_files_in_non_interactive_commit():
    # Non-interactive without files and commit enabled should error
    r = subprocess.run([sys.executable, str(SCRIPT), "--non-interactive", "--config", ".gitpush-temp.yml"], capture_output=True, text=True)
    # .gitpush-temp.yml enables commit but not files; expect non-zero exit
    assert r.returncode != 0
    assert "no commit message provided" in r.stdout or "no commit message provided" in r.stderr or "refusing" in r.stdout

@pytest.mark.skipif(not SCRIPT.exists(), reason="Script not present")
def test_files_and_branch_flags_dry_run():
    r = subprocess.run([sys.executable, str(SCRIPT), "--dry-run", "--files", "README.md", "--branch", "main", "--allow-branch-push", "--json-output", "-"], capture_output=True, text=True)
    # Dry-run should succeed and mention pushing to origin/main
    assert r.returncode == 0
    assert "dry-run" in r.stdout.lower()
    assert "origin/main" in r.stdout

