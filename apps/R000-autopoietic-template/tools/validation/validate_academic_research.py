#!/usr/bin/env python3
"""
Validator for Academic Research template structure.

Checks:
- 5 required folders exist (1-6, excluding 5-reserved)
- README.md exists with valid metadata
- Atomics follow naming convention (atomic-XXX-{title}.md)
- No empty folders (except 5-reserved)
- sources.yaml exists in 1-literature/
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List

from validate_metadata import MetadataValidator, ValidationError


@dataclass
class ValidationReport:
    """Validation report with errors and warnings."""

    directory: Path
    errors: List[ValidationError]
    warnings: List[ValidationError]

    @property
    def is_valid(self) -> bool:
        """Returns True if no errors (warnings are OK)."""
        return len(self.errors) == 0

    @property
    def exit_code(self) -> int:
        """Returns exit code: 0 (success), 1 (errors), 2 (warnings only)."""
        if len(self.errors) > 0:
            return 1
        elif len(self.warnings) > 0:
            return 2
        return 0


class AcademicResearchValidator:
    """Validates Academic Research template structure."""

    # Required folders (1-literature, 2-analysis, 3-atomics, 4-artifacts, 6-outputs)
    REQUIRED_FOLDERS = ["1-literature", "2-analysis", "3-atomics", "4-artifacts", "6-outputs"]

    # Atomic naming pattern: atomic-XXX-{title}.md or concept-XXX-{title}.md or pattern-XXX-{title}.md
    ATOMIC_PATTERN = re.compile(r"^(atomic|concept|pattern|principle|method)-\d{3}-.+\.md$")

    def __init__(self, directory: Path):
        self.directory = directory
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []

    def validate(self) -> ValidationReport:
        """Run all validation checks."""
        if not self.directory.exists():
            self.errors.append(
                ValidationError(field="directory", message=f"Directory not found: {self.directory}")
            )
            return self._create_report()

        if not self.directory.is_dir():
            self.errors.append(
                ValidationError(
                    field="directory", message=f"Path is not a directory: {self.directory}"
                )
            )
            return self._create_report()

        # Run validation checks
        self._validate_required_folders()
        self._validate_readme()
        self._validate_literature_folder()
        self._validate_atomics_naming()
        self._check_empty_folders()

        return self._create_report()

    def _validate_required_folders(self) -> None:
        """Check that all 5 required folders exist."""
        for folder in self.REQUIRED_FOLDERS:
            folder_path = self.directory / folder
            if not folder_path.exists():
                self.errors.append(
                    ValidationError(field="folder", message=f"Missing required folder: {folder}/")
                )
            elif not folder_path.is_dir():
                self.errors.append(
                    ValidationError(field="folder", message=f"Path is not a directory: {folder}/")
                )

    def _validate_readme(self) -> None:
        """Validate README.md exists and has valid metadata."""
        readme_path = self.directory / "README.md"

        if not readme_path.exists():
            self.errors.append(ValidationError(field="readme", message="Missing README.md file"))
            return

        # Validate metadata using MetadataValidator
        metadata_validator = MetadataValidator(readme_path)
        metadata_report = metadata_validator.validate()

        # Add metadata errors/warnings to our report
        for error in metadata_report.errors:
            self.errors.append(error)
        for warning in metadata_report.warnings:
            self.warnings.append(warning)

    def _validate_literature_folder(self) -> None:
        """Check that 1-literature/ has sources.yaml."""
        lit_folder = self.directory / "1-literature"

        if not lit_folder.exists():
            return  # Already reported as error

        # Check for sources.yaml
        sources_file = lit_folder / "sources.yaml"
        if not sources_file.exists():
            self.warnings.append(
                ValidationError(
                    field="1-literature",
                    message="Missing sources.yaml (recommended for PRISMA flow)",
                    severity="warning",
                )
            )

        # Check for subfolder structure (papers/, books/, frameworks/)
        expected_subfolders = ["paper", "book", "framework"]
        has_any_subfolder = any((lit_folder / sf).exists() for sf in expected_subfolders)

        if not has_any_subfolder:
            self.warnings.append(
                ValidationError(
                    field="1-literature",
                    message="No subfolders found (recommended: paper/, book/, framework/)",
                    severity="warning",
                )
            )

    def _validate_atomics_naming(self) -> None:
        """Check that atomics in 3-atomics/ follow naming convention."""
        atomics_folder = self.directory / "3-atomics"

        if not atomics_folder.exists():
            return  # Already reported as error

        # Get all .md files in atomics folder
        md_files = list(atomics_folder.glob("*.md"))

        if len(md_files) == 0:
            self.warnings.append(
                ValidationError(
                    field="3-atomics",
                    message="No atomic files found (folder is empty)",
                    severity="warning",
                )
            )
            return

        # Check naming convention for each file
        invalid_names = []
        for md_file in md_files:
            if not self.ATOMIC_PATTERN.match(md_file.name):
                invalid_names.append(md_file.name)

        if invalid_names:
            self.errors.append(
                ValidationError(
                    field="3-atomics",
                    message=f"Files don't follow naming convention (atomic-XXX-title.md): {', '.join(invalid_names)}",
                )
            )

    def _check_empty_folders(self) -> None:
        """Check for empty folders (warnings only)."""
        for folder in self.REQUIRED_FOLDERS:
            folder_path = self.directory / folder

            if not folder_path.exists():
                continue  # Already reported as error

            # Check if folder has any files or subdirectories
            contents = list(folder_path.iterdir())

            if len(contents) == 0:
                # Empty folder is a warning (not an error)
                self.warnings.append(
                    ValidationError(
                        field=folder, message=f"Folder is empty: {folder}/", severity="warning"
                    )
                )

    def _create_report(self) -> ValidationReport:
        """Create validation report."""
        return ValidationReport(
            directory=self.directory, errors=self.errors, warnings=self.warnings
        )


def print_report(report: ValidationReport, verbose: bool = False) -> None:
    """Print validation report to console."""
    print(f"\n{'=' * 60}")
    print(f"Academic Research Structure Validation Report")
    print(f"Directory: {report.directory}")
    print(f"{'=' * 60}\n")

    if report.is_valid and len(report.warnings) == 0:
        print("✅ All Academic Research structure checks passed!")
        print(f"   • 5 required folders present")
        print(f"   • README.md with valid metadata")
        print(f"   • Atomics follow naming convention")
        print(f"   • No empty folders")
        return

    # Print errors
    if report.errors:
        print(f"❌ Errors ({len(report.errors)}):")
        for error in report.errors:
            print(f"  • [{error.field}] {error.message}")
        print()

    # Print warnings
    if report.warnings:
        print(f"⚠️  Warnings ({len(report.warnings)}):")
        for warning in report.warnings:
            print(f"  • [{warning.field}] {warning.message}")
        print()

    # Summary
    if report.is_valid:
        print("✅ Validation passed with warnings")
    else:
        print("❌ Validation failed")

    print(f"\nExit code: {report.exit_code}")


def main():
    parser = argparse.ArgumentParser(description="Validate Academic Research template structure")
    parser.add_argument("directory", type=Path, help="Path to Academic Research workbook directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # Validate structure
    validator = AcademicResearchValidator(args.directory)
    report = validator.validate()

    # Print report
    print_report(report, verbose=args.verbose)

    # Exit with appropriate code
    sys.exit(report.exit_code)


if __name__ == "__main__":
    main()
