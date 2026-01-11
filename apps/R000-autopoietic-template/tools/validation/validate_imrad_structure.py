#!/usr/bin/env python3
"""
Validator for IMRAD template structure.

Checks:
- 7 required files exist (01-07.md)
- README.md exists with valid metadata
- Section headers present in each file
- Proper file naming convention
"""

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

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


class IMRADValidator:
    """Validates IMRAD template structure."""

    # Required IMRAD files (01-07.md)
    REQUIRED_FILES = [
        "01-introduction.md",
        "02-literature-review.md",
        "03-methodology.md",
        "04-results.md",
        "05-discussion.md",
        "06-conclusion.md",
        "07-references.md",
    ]

    # Expected section headers in each file
    EXPECTED_HEADERS = {
        "01-introduction.md": ["# Introduction", "## Context", "## Problem Statement"],
        "02-literature-review.md": ["# Literature Review", "## Overview"],
        "03-methodology.md": ["# Methodology", "## Research Design"],
        "04-results.md": ["# Results", "## Overview"],
        "05-discussion.md": ["# Discussion", "## Interpretation"],
        "06-conclusion.md": ["# Conclusion", "## Summary"],
        "07-references.md": ["# References", "## Bibliography"],
    }

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
        self._validate_required_files()
        self._validate_readme()
        self._validate_file_headers()
        self._check_extra_files()

        return self._create_report()

    def _validate_required_files(self) -> None:
        """Check that all 7 required IMRAD files exist."""
        for filename in self.REQUIRED_FILES:
            file_path = self.directory / filename
            if not file_path.exists():
                self.errors.append(
                    ValidationError(
                        field="file", message=f"Missing required IMRAD file: {filename}"
                    )
                )
            elif file_path.stat().st_size == 0:
                self.warnings.append(
                    ValidationError(
                        field="file", message=f"File is empty: {filename}", severity="warning"
                    )
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

    def _validate_file_headers(self) -> None:
        """Check that each IMRAD file has expected section headers."""
        for filename in self.REQUIRED_FILES:
            file_path = self.directory / filename

            if not file_path.exists():
                continue  # Already reported as error

            # Read file content
            try:
                content = file_path.read_text(encoding="utf-8")
            except Exception as e:
                self.errors.append(
                    ValidationError(field=filename, message=f"Failed to read file: {e}")
                )
                continue

            # Check for expected headers
            expected_headers = self.EXPECTED_HEADERS.get(filename, [])
            for header in expected_headers:
                if header not in content:
                    self.warnings.append(
                        ValidationError(
                            field=filename,
                            message=f"Missing expected header: '{header}'",
                            severity="warning",
                        )
                    )

    def _check_extra_files(self) -> None:
        """Check for unexpected files (not errors, just warnings)."""
        # Get all .md files in directory
        md_files = [f.name for f in self.directory.glob("*.md")]

        expected_files = self.REQUIRED_FILES + ["README.md"]
        extra_files = [f for f in md_files if f not in expected_files]

        if extra_files:
            self.warnings.append(
                ValidationError(
                    field="structure",
                    message=f"Unexpected files found: {', '.join(extra_files)}",
                    severity="warning",
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
    print(f"IMRAD Structure Validation Report")
    print(f"Directory: {report.directory}")
    print(f"{'=' * 60}\n")

    if report.is_valid and len(report.warnings) == 0:
        print("✅ All IMRAD structure checks passed!")
        print(f"   • 7 required files present")
        print(f"   • README.md with valid metadata")
        print(f"   • Section headers correct")
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
    parser = argparse.ArgumentParser(description="Validate IMRAD template structure")
    parser.add_argument("directory", type=Path, help="Path to IMRAD workbook directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # Validate structure
    validator = IMRADValidator(args.directory)
    report = validator.validate()

    # Print report
    print_report(report, verbose=args.verbose)

    # Exit with appropriate code
    sys.exit(report.exit_code)


if __name__ == "__main__":
    main()
