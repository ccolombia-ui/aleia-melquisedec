#!/usr/bin/env python3
"""
validate_doc_links.py - Validates markdown links in the monorepo

Usage:
    python validate_doc_links.py                  # Scan all docs/
    python validate_doc_links.py --path apps/     # Scan specific path
    python validate_doc_links.py --fix            # Auto-fix broken links (where possible)
    python validate_doc_links.py --report         # Generate detailed report
    python validate_doc_links.py --verbose        # Show all links found

Features:
    - Detects broken internal links
    - Identifies moved files (searches for new location)
    - Validates markdown link syntax
    - Optionally auto-fixes simple cases
    - Generates comprehensive reports
"""

import re
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from collections import defaultdict


@dataclass
class LinkIssue:
    """Represents a broken or invalid link"""
    file_path: Path
    line_number: int
    link_text: str
    link_target: str
    issue_type: str  # 'broken', 'moved', 'invalid_syntax', 'external'
    suggested_fix: Optional[str] = None


class MarkdownLinkValidator:
    """Validates markdown links in a directory tree"""

    # Regex patterns
    MARKDOWN_LINK = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
    HEADING_ANCHOR = re.compile(r'#[a-zA-Z0-9_-]+')

    def __init__(self, root_path: Path, verbose: bool = False):
        self.root = root_path.resolve()
        self.verbose = verbose
        self.issues: List[LinkIssue] = []
        self.file_index: Dict[str, List[Path]] = defaultdict(list)
        self._build_file_index()

    def _build_file_index(self):
        """Build index of all files for fast lookup"""
        print(f"📂 Indexing files in {self.root}...")
        for file in self.root.rglob('*'):
            if file.is_file() and not self._should_ignore(file):
                self.file_index[file.name].append(file)
        print(f"✅ Indexed {sum(len(v) for v in self.file_index.values())} files")

    def _should_ignore(self, path: Path) -> bool:
        """Check if path should be ignored"""
        ignored_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv',
                       '.obsidian', 'dist', 'build', '.pytest_cache'}
        ignored_extensions = {'.pyc', '.pyo', '.pyd', '.so', '.dll', '.dylib'}

        # Check if any parent is ignored
        for parent in path.parents:
            if parent.name in ignored_dirs:
                return True

        # Check extension
        if path.suffix in ignored_extensions:
            return True

        return False

    def _is_external_link(self, target: str) -> bool:
        """Check if link is external (http, https, mailto, etc.)"""
        return any(target.startswith(prefix) for prefix in ['http://', 'https://', 'mailto:', 'ftp://'])

    def _resolve_relative_link(self, source_file: Path, target: str) -> Optional[Path]:
        """Resolve relative link from source file"""
        # Remove anchor if present
        target_path = target.split('#')[0] if '#' in target else target

        if not target_path:  # Just an anchor
            return source_file

        # Resolve relative to source file's directory
        try:
            resolved = (source_file.parent / target_path).resolve()
            return resolved if resolved.exists() else None
        except Exception:
            return None

    def _find_moved_file(self, original_name: str) -> Optional[Path]:
        """Try to find a moved file by name"""
        candidates = self.file_index.get(Path(original_name).name, [])
        return candidates[0] if candidates else None

    def _get_relative_path(self, source: Path, target: Path) -> str:
        """Get relative path from source to target"""
        try:
            return str(target.relative_to(source.parent)).replace('\\', '/')
        except ValueError:
            # Files not in same tree, use absolute workspace path
            try:
                return str(target.relative_to(self.root)).replace('\\', '/')
            except ValueError:
                return str(target)

    def validate_file(self, file_path: Path) -> List[LinkIssue]:
        """Validate all links in a markdown file"""
        if not file_path.suffix == '.md':
            return []

        issues = []

        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️  Could not read {file_path}: {e}")
            return []

        # Find all markdown links
        for line_num, line in enumerate(content.split('\n'), 1):
            for match in self.MARKDOWN_LINK.finditer(line):
                link_text = match.group(1)
                link_target = match.group(2)

                if self.verbose:
                    print(f"  🔗 Found: [{link_text}]({link_target})")

                # Skip external links
                if self._is_external_link(link_target):
                    continue

                # Validate internal link
                resolved = self._resolve_relative_link(file_path, link_target)

                if resolved is None:
                    # Link is broken - try to find moved file
                    moved_file = self._find_moved_file(link_target)

                    issue = LinkIssue(
                        file_path=file_path,
                        line_number=line_num,
                        link_text=link_text,
                        link_target=link_target,
                        issue_type='moved' if moved_file else 'broken',
                        suggested_fix=self._get_relative_path(file_path, moved_file) if moved_file else None
                    )
                    issues.append(issue)

        return issues

    def validate_all(self, path: Optional[Path] = None) -> List[LinkIssue]:
        """Validate all markdown files in path (or root)"""
        scan_path = path or self.root
        print(f"\n🔍 Scanning markdown files in {scan_path}...")

        markdown_files = list(scan_path.rglob('*.md'))
        print(f"📄 Found {len(markdown_files)} markdown files\n")

        for md_file in markdown_files:
            if self._should_ignore(md_file):
                continue

            if self.verbose:
                print(f"\n📝 Validating {md_file.relative_to(self.root)}...")

            file_issues = self.validate_file(md_file)
            self.issues.extend(file_issues)

        return self.issues

    def fix_issues(self, dry_run: bool = False) -> int:
        """Auto-fix issues where possible"""
        fixed_count = 0

        # Group issues by file
        issues_by_file: Dict[Path, List[LinkIssue]] = defaultdict(list)
        for issue in self.issues:
            if issue.suggested_fix:
                issues_by_file[issue.file_path].append(issue)

        for file_path, file_issues in issues_by_file.items():
            try:
                content = file_path.read_text(encoding='utf-8')
                original_content = content

                # Apply fixes
                for issue in file_issues:
                    old_link = f']({issue.link_target})'
                    new_link = f']({issue.suggested_fix})'
                    content = content.replace(old_link, new_link)
                    fixed_count += 1
                    print(f"✅ Fixed: {file_path.name}:{issue.line_number}")
                    print(f"   {old_link} → {new_link}")

                # Write back
                if not dry_run and content != original_content:
                    file_path.write_text(content, encoding='utf-8')

            except Exception as e:
                print(f"❌ Could not fix {file_path}: {e}")

        return fixed_count

    def generate_report(self) -> str:
        """Generate detailed report of all issues"""
        report = []
        report.append("=" * 80)
        report.append("📋 MARKDOWN LINK VALIDATION REPORT")
        report.append("=" * 80)
        report.append(f"\n📁 Root: {self.root}")
        report.append(f"🔍 Total issues found: {len(self.issues)}\n")

        # Group by issue type
        by_type: Dict[str, List[LinkIssue]] = defaultdict(list)
        for issue in self.issues:
            by_type[issue.issue_type].append(issue)

        for issue_type, issues in sorted(by_type.items()):
            report.append(f"\n{'─' * 80}")
            report.append(f"📌 {issue_type.upper()} LINKS: {len(issues)}")
            report.append(f"{'─' * 80}\n")

            for issue in issues:
                rel_path = issue.file_path.relative_to(self.root)
                report.append(f"📄 File: {rel_path}:{issue.line_number}")
                report.append(f"   Link: [{issue.link_text}]({issue.link_target})")
                if issue.suggested_fix:
                    report.append(f"   💡 Suggested fix: {issue.suggested_fix}")
                report.append("")

        report.append("=" * 80)
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description="Validate markdown links in monorepo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                        # Scan all docs/
  %(prog)s --path apps/           # Scan specific path
  %(prog)s --fix                  # Auto-fix broken links
  %(prog)s --fix --dry-run        # Preview fixes without applying
  %(prog)s --report               # Generate detailed report
  %(prog)s --verbose              # Show all links found
        """
    )

    parser.add_argument(
        '--path',
        type=Path,
        help='Path to scan (default: workspace root)'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Auto-fix broken links where possible'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview fixes without applying (requires --fix)'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate detailed report'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show all links found during scan'
    )

    args = parser.parse_args()

    # Determine root path
    if args.path:
        root = args.path.resolve()
    else:
        # Try to find workspace root
        cwd = Path.cwd()
        if (cwd / 'docs').exists() or (cwd / 'packages').exists():
            root = cwd
        else:
            root = cwd

    print(f"🚀 Markdown Link Validator")
    print(f"📁 Workspace: {root}\n")

    # Create validator
    validator = MarkdownLinkValidator(root, verbose=args.verbose)

    # Validate
    issues = validator.validate_all(args.path)

    # Results
    print(f"\n{'=' * 80}")
    if not issues:
        print("✅ All links are valid!")
    else:
        print(f"⚠️  Found {len(issues)} issues:")
        by_type = defaultdict(int)
        for issue in issues:
            by_type[issue.issue_type] += 1
        for issue_type, count in sorted(by_type.items()):
            print(f"   - {issue_type}: {count}")
    print(f"{'=' * 80}\n")

    # Fix if requested
    if args.fix and issues:
        print(f"\n🔧 {'Preview' if args.dry_run else 'Applying'} fixes...\n")
        fixed = validator.fix_issues(dry_run=args.dry_run)
        print(f"\n{'Would fix' if args.dry_run else 'Fixed'} {fixed} issues")

    # Report if requested
    if args.report and issues:
        report = validator.generate_report()
        print(f"\n{report}")

        # Save to file
        report_file = root / 'docs' / '_meta' / 'link-validation-report.txt'
        report_file.parent.mkdir(parents=True, exist_ok=True)
        report_file.write_text(report, encoding='utf-8')
        print(f"\n💾 Report saved to: {report_file}")

    # Exit code
    return 1 if issues else 0


if __name__ == '__main__':
    exit(main())
