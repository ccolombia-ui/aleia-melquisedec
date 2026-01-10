#!/usr/bin/env python3
"""Simple generator: fill placeholders in daath-zen templates and write artifact file.
Usage: python tools/generate_from_daath_template.py TEMPLATE_PATH OUTPUT_PATH KEY=VALUE ...
Example:
  python tools/generate_from_daath_template.py _templates/daath-zen-patterns/daath-zen-req-template.md apps/.../REQ-001.md REQ_ID=001 REQ_TITLE="Define @context" result_type=immediate
"""
import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: generate_from_daath_template.py TEMPLATE_PATH OUTPUT_PATH KEY=VALUE ...")
    sys.exit(2)

template_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
replacements = {}
for kv in sys.argv[3:]:
    if "=" in kv:
        k, v = kv.split("=", 1)
        replacements[k] = v

content = template_path.read_text(encoding="utf-8")
for k, v in replacements.items():
    content = content.replace("{{" + k + "}}", v)

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(content, encoding="utf-8")
print(f"Generated {output_path}")
