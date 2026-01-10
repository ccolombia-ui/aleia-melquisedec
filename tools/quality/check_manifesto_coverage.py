#!/usr/bin/env python3
"""
Validate manifesto coverage: ensure each heading has canonical doc or TODO entry.

Ensures that:
1. Every major manifesto heading (H1-H3) is covered by a canonical document
2. Uncovered headings are explicitly tracked in a TODO list
3. No manifesto sections are silently ignored

Exit codes:
- 0: All checks passed (100% coverage or TODOs tracked)
- 1: Validation errors found (gaps without TODOs)
"""
import json
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

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    yaml_content = match.group(1)

    for line in yaml_content.split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip().strip("\"'")

    return frontmatter


def extract_manifesto_headings(manifesto_path: Path, max_level: int = 3) -> List[Tuple[int, str]]:
    """
    Extract headings from manifesto up to specified level.

    Returns:
        List of (level, heading_text) tuples
    """
    try:
        content = manifesto_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"ERROR: Could not read manifesto: {e}")
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
    """Convert heading text to canonical slug."""
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def find_canonical_docs(root_dir: Path) -> Set[str]:
    """Find all canonical document slugs."""
    canonical_dir = root_dir / "canonical"
    if not canonical_dir.exists():
        return set()

    canonical_slugs = set()
    for md_file in canonical_dir.glob("*.md"):
        canonical_slugs.add(md_file.stem)

    return canonical_slugs


def find_canonical_for_values(root_dir: Path) -> Set[str]:
    """Find all canonical_for values in documents."""
    canonical_for_values = set()

    for md_file in root_dir.rglob("*.md"):
        # Skip certain directories
        if any(skip in str(md_file) for skip in ["node_modules", ".venv", ".git", "htmlcov"]):
            continue

        frontmatter = extract_frontmatter(md_file)
        if "canonical_for" in frontmatter:
            canonical_for = frontmatter["canonical_for"]
            if canonical_for:
                canonical_for_values.add(canonical_for)

    return canonical_for_values


def load_todo_list(root_dir: Path) -> Set[str]:
    """Load TODO list of intentionally uncovered manifesto headings."""
    todo_file = root_dir / "canonical" / "TODO.md"
    if not todo_file.exists():
        return set()

    try:
        content = todo_file.read_text(encoding="utf-8")
    except Exception:
        return set()

    # Extract slugs from TODO items (lines starting with - [ ])
    todo_slugs = set()
    for match in re.finditer(r"^\s*-\s*\[\s*\]\s*`([^`]+)`", content, re.MULTILINE):
        todo_slugs.add(match.group(1))

    return todo_slugs


def validate_manifesto_coverage(root_dir: Path) -> Tuple[bool, Dict, List[str]]:
    """
    Validate that all manifesto headings are covered.

    Returns:
        (success, stats, errors)
    """
    # Find manifesto file
    manifesto_candidates = [
        root_dir / "docs" / "manifiesto" / "bereshit-v3.0.0.md",
        root_dir / "apps" / "research-autopoietic-template" / "raw-manifiesto.md",
        root_dir / "raw-manifiesto.md",
    ]

    manifesto_path = None
    for candidate in manifesto_candidates:
        if candidate.exists():
            manifesto_path = candidate
            break

    if not manifesto_path:
        return False, {}, ["ERROR: Could not find manifesto file"]

    print(f"Using manifesto: {manifesto_path.relative_to(root_dir)}")

    # Extract manifesto headings
    headings = extract_manifesto_headings(manifesto_path, max_level=3)

    # Generate expected slugs
    heading_slugs = {slugify(text): (level, text) for level, text in headings}

    # Find canonical docs and references
    canonical_docs = find_canonical_docs(root_dir)
    canonical_for_values = find_canonical_for_values(root_dir)
    todo_slugs = load_todo_list(root_dir)

    # Coverage analysis
    covered_slugs = canonical_docs | canonical_for_values
    uncovered_slugs = set(heading_slugs.keys()) - covered_slugs - todo_slugs

    # Statistics
    total_headings = len(heading_slugs)
    covered_count = len(covered_slugs & set(heading_slugs.keys()))
    todo_count = len(todo_slugs & set(heading_slugs.keys()))
    uncovered_count = len(uncovered_slugs)

    coverage_rate = (covered_count + todo_count) / total_headings if total_headings > 0 else 0

    stats = {
        "total_headings": total_headings,
        "covered": covered_count,
        "todo": todo_count,
        "uncovered": uncovered_count,
        "coverage_rate": coverage_rate,
    }

    errors = []

    # Report uncovered headings (not documented and not in TODO)
    if uncovered_slugs:
        errors.append(
            f"ERROR: {uncovered_count} manifesto heading(s) have no canonical doc or TODO entry:\n"
        )
        for slug in sorted(uncovered_slugs):
            level, text = heading_slugs[slug]
            errors.append(f"   {'  ' * (level - 1)}- {text} (slug: {slug})")
        errors.append(f"\nTIP: Either create canonical/{slug}.md or add to canonical/TODO.md")

    return len(errors) == 0, stats, errors


def main() -> int:
    """Main entry point."""
    repo_root = Path(__file__).resolve().parent.parent.parent

    print("=" * 60)
    print("Manifesto Coverage Validation")
    print("=" * 60)
    print(f"Repository: {repo_root}")
    print()

    success, stats, errors = validate_manifesto_coverage(repo_root)

    # Print statistics
    print()
    print("Coverage Statistics:")
    print(f"  Total manifesto headings: {stats['total_headings']}")
    print(f"  Covered (canonical docs): {stats['covered']}")
    print(f"  Tracked in TODO:          {stats['todo']}")
    print(f"  Uncovered (gaps):         {stats['uncovered']}")
    print(f"  Coverage rate:            {stats['coverage_rate']:.1%}")
    print()

    # Save report as JSON
    report_path = (
        repo_root / f"manifesto-coverage-{stats['total_headings']}-{stats['covered']}.json"
    )
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        print(f"Report saved: {report_path.name}")
    except Exception as e:
        print(f"WARNING: Could not save report: {e}")

    print()

    if success:
        print("SUCCESS: All manifesto headings are covered or tracked!")
        print()
        return 0
    else:
        print("ERROR: Validation failed:")
        print()
        for error in errors:
            print(error)
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
