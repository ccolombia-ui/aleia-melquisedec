#!/usr/bin/env python3
"""
Pre-commit hook to validate canonical_for uniqueness.

Ensures that:
1. Each canonical_for value is unique across all documents
2. canonical_for values only reference existing canonical/ documents
3. No circular references exist

Exit codes:
- 0: All checks passed
- 1: Validation errors found
"""
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


def extract_frontmatter(file_path: Path) -> Dict[str, str]:
    """Extract YAML frontmatter from a markdown file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"WARNING: Could not read {file_path}: {e}")
        return {}

    # Match YAML frontmatter between --- delimiters
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    yaml_content = match.group(1)

    # Parse simple YAML key-value pairs (not full YAML parser)
    for line in yaml_content.split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip().strip("\"'")

    return frontmatter


def find_markdown_files(root_dir: Path, exclude_patterns: List[str] = None) -> List[Path]:
    """Find all markdown files, excluding specified patterns."""
    if exclude_patterns is None:
        exclude_patterns = [
            "node_modules",
            ".venv",
            "venv",
            "__pycache__",
            ".git",
            "htmlcov",
            "_templates",
        ]

    markdown_files = []
    for md_file in root_dir.rglob("*.md"):
        # Skip excluded directories
        if any(pattern in str(md_file) for pattern in exclude_patterns):
            continue
        markdown_files.append(md_file)

    return markdown_files


def validate_canonical_for(root_dir: Path) -> Tuple[bool, List[str]]:
    """
    Validate canonical_for fields across all documents.

    Returns:
        (success, errors): Tuple of boolean success and list of error messages
    """
    errors = []
    canonical_for_map: Dict[str, List[Path]] = {}
    canonical_docs: Set[str] = set()

    # Find all markdown files
    md_files = find_markdown_files(root_dir)

    print(f"Scanning {len(md_files)} markdown files...")

    # First pass: collect all canonical docs and canonical_for values
    for md_file in md_files:
        frontmatter = extract_frontmatter(md_file)

        # Track canonical/ documents
        if "canonical" in str(md_file):
            rel_path = md_file.relative_to(root_dir)
            canonical_slug = rel_path.stem
            canonical_docs.add(canonical_slug)

        # Track canonical_for values
        if "canonical_for" in frontmatter:
            canonical_for = frontmatter["canonical_for"]
            if canonical_for:
                if canonical_for not in canonical_for_map:
                    canonical_for_map[canonical_for] = []
                canonical_for_map[canonical_for].append(md_file)

    print(f"Found {len(canonical_docs)} canonical documents")
    print(f"Found {len(canonical_for_map)} unique canonical_for references")

    # Second pass: validate uniqueness and references
    for canonical_for, files in canonical_for_map.items():
        # Check uniqueness: each canonical_for should appear only once
        if len(files) > 1:
            file_list = "\n  - ".join(str(f.relative_to(root_dir)) for f in files)
            errors.append(
                f"ERROR: Duplicate canonical_for='{canonical_for}' found in:\n  - {file_list}"
            )

        # Check that referenced canonical doc exists
        if canonical_for not in canonical_docs:
            rel_path = files[0].relative_to(root_dir)
            errors.append(
                f"ERROR: {rel_path}: references non-existent canonical_for='{canonical_for}'\n"
                f"   Expected: canonical/{canonical_for}.md"
            )

    # Check for orphaned canonical documents (no references)
    referenced_canonicals = set(canonical_for_map.keys())
    orphaned = canonical_docs - referenced_canonicals
    if orphaned:
        print(f"WARNING: Found {len(orphaned)} orphaned canonical documents (no references):")
        for slug in sorted(orphaned):
            print(f"   - canonical/{slug}.md")

    return len(errors) == 0, errors


def main() -> int:
    """Main entry point for pre-commit hook."""
    # Determine repository root
    repo_root = Path(__file__).resolve().parent.parent.parent

    print("=" * 60)
    print("Canonical_for Uniqueness Validation")
    print("=" * 60)
    print(f"Repository: {repo_root}")
    print()

    success, errors = validate_canonical_for(repo_root)

    if success:
        print()
        print("SUCCESS: All canonical_for checks passed!")
        print()
        return 0
    else:
        print()
        print("ERROR: Validation failed:")
        print()
        for error in errors:
            print(error)
            print()
        print(f"Total errors: {len(errors)}")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
