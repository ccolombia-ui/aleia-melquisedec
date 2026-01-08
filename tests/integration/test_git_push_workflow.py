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
