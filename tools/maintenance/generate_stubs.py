#!/usr/bin/env python3
"""
Generate canonical stubs for manifesto gaps.
"""
import re
import sys
from pathlib import Path
from typing import List, Set, Tuple

# Add tools/quality to path to reuse logic if needed,
# but for simplicity/independence copying key logic or imports is safer
# if we don't assume package structure.
# Let's just re-implement the extraction logic quickly to be self-contained.


def extract_manifesto_headings(manifesto_path: Path, max_level: int = 3) -> List[Tuple[int, str]]:
    try:
        content = manifesto_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading manifesto: {e}")
        return []

    # Remove frontmatter
    content = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)

    headings = []
    for match in re.finditer(r"^(#{1," + str(max_level) + r"})\s+(.+)$", content, re.MULTILINE):
        level = len(match.group(1))
        text = match.group(2).strip()
        headings.append((level, text))
    return headings


def slugify(text: str) -> str:
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def main():
    root_dir = Path(__file__).resolve().parent.parent.parent
    manifesto_path = root_dir / "docs" / "manifiesto" / "bereshit-v3.0.0.md"
    canonical_dir = root_dir / "canonical"
    canonical_dir.mkdir(exist_ok=True)

    print(f"Reading from: {manifesto_path}")
    headings = extract_manifesto_headings(manifesto_path)

    created_count = 0
    max_stubs = 10

    print(f"Found {len(headings)} headings. Generating top {max_stubs} missing stubs...")

    for level, text in headings:
        if created_count >= max_stubs:
            break

        slug = slugify(text)
        filename = f"{slug}.md"
        file_path = canonical_dir / filename

        if file_path.exists():
            continue

        # Check if matched by existing check (simple check here)
        # In a real scenario, we'd check canonical_for references too,
        # but for clean stubs we assume if the file exists its covered, if not valid candidate.

        content = f"""---
title: "{text}"
canonical_for: "{slug}"
status: draft
target_coverage: 0.8
type: canonical
---

# {text}

> **Canonical Document Stub**
> This document is the authoritative source for the concept: `{slug}`.
> It corresponds to Level {level} in the MELQUISEDEC Manifesto.

## Definition

*(Draft definition pending)*

## Relationships

- **Parent Concept**: (Link to parent)
- **Implementations**: (Links to implementations)

## Validation Criteria

- [ ] Defined clear scope
- [ ] Mapped to Manifesto section
"""
        try:
            file_path.write_text(content, encoding="utf-8")
            print(f"Created stub: canonical/{filename}")
            created_count += 1
        except Exception as e:
            print(f"Failed to create {filename}: {e}")

    print(f"\nSuccessfully generated {created_count} stubs.")


if __name__ == "__main__":
    main()
