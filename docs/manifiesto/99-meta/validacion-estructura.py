#!/usr/bin/env python3
"""
validacion-estructura.py

Valida la estructura mínima del manifiesto y los headers HKM de los archivos .md listados en metadata.yaml.

Usage:
    python docs/manifiesto/99-meta/validacion-estructura.py [--report-only]

Exit codes:
    0 - OK (todo valido)
    1 - Fallos detectados
"""

import sys
import yaml
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent  # repo root is two levels up from file
META_PATH = Path(__file__).resolve().parent / "metadata.yaml"

REQUIRED_DC = ["title", "creator", "date", "subject"]
REQUIRED_SECI = ["derives_from"]


def load_metadata():
    with open(META_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def check_directories(directories):
    missing = []
    for d in directories:
        p = ROOT / Path(d).relative_to('docs') if Path(d).is_absolute() else ROOT / d
        if not p.exists():
            missing.append(d)
    return missing


def extract_frontmatter(md_text):
    if not md_text.startswith('---'):
        return None
    end = md_text.find('---', 3)
    if end == -1:
        return None
    yaml_content = md_text[3:end]
    try:
        return yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return None


def validate_hkm_header(file_path: Path):
    text = file_path.read_text(encoding='utf-8')
    meta = extract_frontmatter(text)
    errors = []
    if meta is None:
        errors.append('Missing or invalid YAML frontmatter')
        return errors

    for field in ['id', 'is_a', 'version', 'dc', 'seci']:
        if field not in meta:
            errors.append(f"Missing required field '{field}' in header")
    if 'dc' in meta:
        for field in REQUIRED_DC:
            if field not in meta['dc']:
                errors.append(f"Missing dc.{field}")
    if 'seci' in meta:
        for field in REQUIRED_SECI:
            if field not in meta['seci']:
                errors.append(f"Missing seci.{field}")
    return errors


def main(report_only=False):
    meta = load_metadata()

    overall_ok = True

    print("Checking required directories...")
    missing_dirs = [d for d in meta.get('directories', []) if not (Path(ROOT) / d).exists()]
    if missing_dirs:
        overall_ok = False
        print('\n❌ Missing directories:')
        for d in missing_dirs:
            print(f"  - {d}")
    else:
        print('✅ All required directories exist')

    print('\nChecking required files...')
    missing_files = []
    for f in meta.get('required_files', []):
        if not (Path(ROOT) / f).exists():
            missing_files.append(f)
    if missing_files:
        overall_ok = False
        print('\n❌ Missing required files:')
        for f in missing_files:
            print(f"  - {f}")
    else:
        print('✅ All required files present')

    print('\nValidating HKM headers for markdown files in manifest...')
    problems = {}
    for f in meta.get('required_files', []):
        p = Path(ROOT) / f
        if p.exists() and p.suffix == '.md':
            errs = validate_hkm_header(p)
            if errs:
                problems[str(f)] = errs

    if problems:
        overall_ok = False
        print('\n❌ HKM header issues:')
        for fp, errs in problems.items():
            print(f"\nFile: {fp}")
            for e in errs:
                print(f"  - {e}")
    else:
        print('✅ HKM headers look valid for required files')

    # Simple check for cycles in derives_from isn't implemented here; recommend running graph checks.

    if overall_ok:
        print('\n\n✅ Manifest OK: No issues found')
        if not report_only:
            try:
                # Update metadata.yaml validation status
                meta['validation']['last_run'] = "2026-01-08T00:00:00Z"
                meta['validation']['status'] = 'ok'
                with open(META_PATH, 'w', encoding='utf-8') as f:
                    yaml.dump(meta, f, sort_keys=False, allow_unicode=True)
                print('✅ Updated metadata.yaml validation status')
            except Exception as e:
                print(f'⚠️ Could not update metadata.yaml: {e}')
        return 0
    else:
        print('\n\n❌ Manifest validation failed')
        if not report_only:
            try:
                meta['validation']['last_run'] = "2026-01-08T00:00:00Z"
                meta['validation']['status'] = 'failed'
                with open(META_PATH, 'w', encoding='utf-8') as f:
                    yaml.dump(meta, f, sort_keys=False, allow_unicode=True)
                print('✅ Updated metadata.yaml validation status')
            except Exception as e:
                print(f'⚠️ Could not update metadata.yaml: {e}')
        return 1


if __name__ == '__main__':
    report_only = '--report-only' in sys.argv
    rc = main(report_only=report_only)
    sys.exit(rc)
