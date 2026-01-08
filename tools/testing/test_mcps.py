#!/usr/bin/env python3
"""Quick MCP tester

Reads `.vscode/mcp.json` and performs lightweight checks for each configured server:
- validates required env vars referenced as ${VAR}
- tries `--version` or `--help`
- if the process appears to be a long-running server, attempts to start and then terminate it

Usage:
    python scripts/test_mcps.py [--mcp-file .vscode/mcp.json] [--timeout 10] [--verbose]
"""

from __future__ import annotations
import json
import os
import re
import subprocess
import argparse
from pathlib import Path
from typing import Dict, Any
try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None

DEFAULT_TIMEOUT = 10


def read_mcp_file(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f).get("servers", {})


def resolve_env_value(value: str) -> (str, list):
    # Replace ${VAR} with environment value; return replaced string and missing vars
    missing = []
    def repl(m):
        var = m.group(1)
        val = os.environ.get(var)
        if val is None:
            missing.append(var)
            return ""
        return val
    out = re.sub(r"\$\{([^}]+)\}", repl, value)
    return out, missing


def run_check(name: str, spec: Dict[str, Any], timeout: int, verbose: bool) -> Dict[str, Any]:
    cmd = [spec.get("command")] + spec.get("args", [])
    env_spec = spec.get("env", {})
    env = os.environ.copy()
    missing_vars = []
    for k, v in env_spec.items():
        resolved, missing = resolve_env_value(v)
        if missing:
            missing_vars.extend(missing)
        env[k] = resolved

    if missing_vars:
        return {"name": name, "status": "missing_env", "missing": sorted(set(missing_vars)), "cmd": cmd}

    def try_run(test_args):
        try:
            full = list(cmd) + test_args
            if verbose:
                print(f"Running: {full}")
            proc = subprocess.run(full, capture_output=True, text=True, env=env, timeout=timeout)
            out = (proc.stdout or proc.stderr or "").strip()
            return {"rc": proc.returncode, "output": out.splitlines()[0] if out else ""}
        except subprocess.TimeoutExpired:
            return {"timeout": True}
        except FileNotFoundError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    # Try --version
    r = try_run(["--version"])
    if r.get("error"):
        return {"name": name, "status": "error", "error": r["error"], "cmd": cmd}
    if r.get("timeout"):
        # try --help
        r2 = try_run(["--help"])
        if r2.get("timeout"):
            # Try to start server briefly and then terminate (non-blocking)
            try:
                proc = subprocess.Popen(cmd, env=env)
                try:
                    proc.wait(timeout=2)
                    rc = proc.returncode
                    return {"name": name, "status": "exited_quickly", "rc": rc, "cmd": cmd}
                except subprocess.TimeoutExpired:
                    proc.kill()
                    return {"name": name, "status": "running", "note": "started and was running (killed)", "cmd": cmd}
            except FileNotFoundError as e:
                return {"name": name, "status": "error", "error": str(e), "cmd": cmd}
            except Exception as e:
                return {"name": name, "status": "error", "error": str(e), "cmd": cmd}
        else:
            return {"name": name, "status": "ok", "check": "help", "output": r2.get("output"), "cmd": cmd}
    else:
        return {"name": name, "status": "ok", "check": "version", "rc": r.get("rc"), "output": r.get("output"), "cmd": cmd}


def main():
    p = argparse.ArgumentParser(description="Quick MCP servers tester")
    p.add_argument("--mcp-file", default=Path(".vscode/mcp.json"), help="Path to MCP JSON file")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Seconds for command timeout")
    p.add_argument("--verbose", action="store_true")
    p.add_argument("--env-file", default=Path(".env"), help="Path to .env file to auto-load")
    p.add_argument("--no-env", action="store_true", help="Do not auto-load .env even if present")
    args = p.parse_args()

    mcp_path = Path(args.mcp_file)
    if not mcp_path.exists():
        print(f"MCP file not found: {mcp_path}")
        raise SystemExit(2)

    servers = read_mcp_file(mcp_path)
    results = []
    for name, spec in servers.items():
        print(f"Checking {name}...", end=" ")
        res = run_check(name, spec, timeout=args.timeout, verbose=args.verbose)
        results.append(res)
        status = res.get("status")
        if status == "ok":
            print("✅ ok", f"({res.get('check')}: {res.get('output')})" if res.get('output') else "")
        elif status == "missing_env":
            print("⚠️ missing env:", ",".join(res.get("missing")))
        elif status == "running":
            print("⚠️ running (assumed ok)")
        else:
            print("❌", status, res.get("error") or "")

    # If some servers are missing env vars, try loading .env and retrying them
    missing_servers = [(i, r) for i, r in enumerate(results) if r.get("status") == "missing_env"]
    if missing_servers and not args.no_env:
        env_path = Path(args.env_file)
        if load_dotenv is None:
            print("\npython-dotenv is not installed; cannot load .env automatically. Install python-dotenv or set env vars manually.")
        else:
            if env_path.exists():
                print(f"\nLoading environment variables from {env_path} and retrying missing checks...")
                load_dotenv(dotenv_path=str(env_path), override=False)
                for idx, old in missing_servers:
                    name = old["name"]
                    spec = servers[name]
                    print(f"Re-checking {name}...", end=" ")
                    new_res = run_check(name, spec, timeout=args.timeout, verbose=args.verbose)
                    results[idx] = new_res
                    status = new_res.get("status")
                    if status == "ok":
                        print("✅ ok (after .env)")
                    elif status == "missing_env":
                        print("⚠️ still missing env:", ",".join(new_res.get("missing")))
                    elif status == "running":
                        print("⚠️ running (assumed ok)")
                    else:
                        print("❌", status, new_res.get("error") or "")
            else:
                print(f"\n.env file not found at {env_path}; skipping auto-load.")

    # Summary
    print("\nSummary:")
    for r in results:
        print(f" - {r['name']}: {r['status']}")

    # Exit with non-zero if any non-ok result
    bad = [r for r in results if r['status'] not in ("ok", "running")]
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
