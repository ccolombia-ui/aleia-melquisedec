#!/usr/bin/env python3
"""
Pre-commit hook to validate document coherence.

Ensures that:
1. New or modified documents meet minimum coherence threshold (0.2)
2. Documents have reasonable structure and content
3. Documents are not just random text dumps

Exit codes:
- 0: All checks passed
- 1: Validation errors found
"""
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


def tokenize(text: str) -> List[str]:
    """Extract meaningful words (3+ letters) from text."""
    text = text.lower()
    # Remove code blocks and frontmatter
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    words = re.findall(r"\b\w{3,}\b", text)
    return [w for w in words if w.isalpha()]


def cosine_sim(tokens_a: List[str], tokens_b: List[str]) -> float:
    """Calculate cosine similarity between two token lists."""
    if not tokens_a or not tokens_b:
        return 0.0

    vocab = set(tokens_a) | set(tokens_b)
    vec_a = [tokens_a.count(w) for w in vocab]
    vec_b = [tokens_b.count(w) for w in vocab]

    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = sum(a * a for a in vec_a) ** 0.5
    mag_b = sum(b * b for b in vec_b) ** 0.5

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot / (mag_a * mag_b)


def calculate_coherence(text: str) -> float:
    """
    Calculate document coherence score (0-1).

    Measures semantic consistency by comparing adjacent paragraphs.
    Higher scores indicate more coherent, focused documents.
    """
    # Split into paragraphs (2+ newlines or heading separators)
    paragraphs = re.split(r"\n\s*\n+", text)
    paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 50]

    if len(paragraphs) < 2:
        # Single paragraph or very short doc: assume coherent
        return 1.0

    # Calculate pairwise similarities between adjacent paragraphs
    similarities = []
    for i in range(len(paragraphs) - 1):
        tokens_a = tokenize(paragraphs[i])
        tokens_b = tokenize(paragraphs[i + 1])
        sim = cosine_sim(tokens_a, tokens_b)
        similarities.append(sim)

    # Average similarity = coherence score
    if not similarities:
        return 0.0

    return sum(similarities) / len(similarities)


def get_changed_markdown_files() -> List[Path]:
    """Get list of markdown files that are staged or modified."""
    try:
        # Get staged files
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True,
            text=True,
            check=True,
        )
        staged_files = result.stdout.strip().split("\n") if result.stdout.strip() else []

        # Get modified files
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACM"],
            capture_output=True,
            text=True,
            check=True,
        )
        modified_files = result.stdout.strip().split("\n") if result.stdout.strip() else []

        # Combine and filter for markdown
        all_files = set(staged_files + modified_files)
        md_files = [Path(f) for f in all_files if f.endswith(".md") and Path(f).exists()]

        return md_files
    except subprocess.CalledProcessError:
        # Fallback: no git changes detected
        return []


def validate_coherence(
    files: List[Path], threshold: float = 0.2, exclude_patterns: List[str] = None
) -> Tuple[bool, List[str]]:
    """
    Validate coherence of specified files.

    Args:
        files: List of markdown files to check
        threshold: Minimum coherence score (default 0.2)
        exclude_patterns: Patterns to skip

    Returns:
        (success, errors): Tuple of boolean success and list of error messages
    """
    if exclude_patterns is None:
        exclude_patterns = [
            "node_modules",
            ".venv",
            "venv",
            "__pycache__",
            ".git",
            "htmlcov",
            "_templates",
            "CHANGELOG",
            "LICENSE",
            "README",
        ]

    errors = []
    checked_count = 0

    for md_file in files:
        # Skip excluded patterns
        if any(pattern in str(md_file) for pattern in exclude_patterns):
            continue

        # Skip ADR, template, and draft/stub files
        if (
            "ADR-" in md_file.name
            or "template" in md_file.name.lower()
            or "canonical" in str(md_file)
            or "reports" in str(md_file)
            or "chatlogs" in str(md_file)
            or "lessons-learned" in str(md_file)
        ):
            continue

        # Skip very short files (likely templates or stubs)
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"WARNING: Could not read {md_file}: {e}")
            continue

        # Skip files under 500 chars (too small to measure coherence)
        if len(content) < 500:
            continue

        checked_count += 1
        coherence = calculate_coherence(content)

        if coherence < threshold:
            errors.append(
                f"ERROR: {md_file}: Coherence too low ({coherence:.2f} < {threshold})\n"
                f"   This document may lack focus or contain disjointed sections.\n"
                f"   Consider:\n"
                f"   - Splitting into multiple focused documents\n"
                f"   - Adding transitions between sections\n"
                f"   - Removing unrelated content"
            )
        else:
            print(f"   OK: {md_file.name}: {coherence:.2f}")

    return len(errors) == 0, errors, checked_count


def main() -> int:
    """Main entry point for pre-commit hook."""
    print("=" * 60)
    print("Document Coherence Validation")
    print("=" * 60)
    print()

    # Get changed files (if running in git context)
    changed_files = get_changed_markdown_files()

    if not changed_files:
        print("INFO: No markdown files to check (no staged/modified .md files)")
        print()
        return 0

    print(f"Checking coherence for {len(changed_files)} file(s)...")
    print()

    # Validate with threshold 0.2 (20% coherence minimum)
    success, errors, checked_count = validate_coherence(changed_files, threshold=0.2)

    print()
    if success:
        print(f"SUCCESS: All {checked_count} document(s) passed coherence check!")
        print()
        return 0
    else:
        print("ERROR: Coherence validation failed:")
        print()
        for error in errors:
            print(error)
            print()
        print(f"Total errors: {len(errors)}")
        print()
        print("TIP: Focus documents on single topics, add transitions,")
        print("   or split into separate files for better coherence.")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
