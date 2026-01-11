#!/usr/bin/env python3
"""
Validator for YAML-LD metadata in workbook README files.

Checks:
- 9 mandatory Dublin Core fields (dc:*)
- spec:issue and spec:owner fields
- Date format (ISO 8601)
- keter-doc:version and schema URL
"""

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import yaml


@dataclass
class ValidationError:
    """Represents a validation error."""

    field: str
    message: str
    severity: str = "error"  # "error" or "warning"


@dataclass
class ValidationReport:
    """Validation report with errors and warnings."""

    file_path: Path
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


class MetadataValidator:
    """Validates YAML-LD metadata in README.md files."""

    # Mandatory Dublin Core fields
    REQUIRED_DC_FIELDS = [
        "title",
        "creator",
        "date",
        "subject",
        "description",
        "type",
        "format",
        "language",
        "identifier",
    ]

    # Mandatory spec fields
    REQUIRED_SPEC_FIELDS = ["issue", "owner"]

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []

    def validate(self) -> ValidationReport:
        """Run all validation checks."""
        if not self.file_path.exists():
            self.errors.append(
                ValidationError(field="file", message=f"File not found: {self.file_path}")
            )
            return self._create_report()

        # Parse YAML frontmatter
        metadata = self._parse_frontmatter()
        if metadata is None:
            return self._create_report()

        # Run validation checks
        self._validate_context(metadata)
        self._validate_dublin_core(metadata)
        self._validate_spec_fields(metadata)
        self._validate_keter_doc(metadata)

        return self._create_report()

    def _parse_frontmatter(self) -> Optional[dict]:
        """Parse YAML frontmatter from README.md."""
        try:
            content = self.file_path.read_text(encoding="utf-8")
        except Exception as e:
            self.errors.append(ValidationError(field="file", message=f"Failed to read file: {e}"))
            return None

        # Check for YAML frontmatter markers (---)
        if not content.startswith("---"):
            self.errors.append(
                ValidationError(
                    field="frontmatter", message="Missing YAML frontmatter (should start with ---)"
                )
            )
            return None

        # Extract frontmatter between --- markers
        parts = content.split("---", 2)
        if len(parts) < 3:
            self.errors.append(
                ValidationError(
                    field="frontmatter", message="Invalid YAML frontmatter (missing closing ---)"
                )
            )
            return None

        frontmatter_text = parts[1]

        # Parse YAML
        try:
            metadata = yaml.safe_load(frontmatter_text)
        except yaml.YAMLError as e:
            self.errors.append(
                ValidationError(field="frontmatter", message=f"Invalid YAML syntax: {e}")
            )
            return None

        if not isinstance(metadata, dict):
            self.errors.append(
                ValidationError(
                    field="frontmatter", message="YAML frontmatter must be a dictionary"
                )
            )
            return None

        return metadata

    def _validate_context(self, metadata: dict) -> None:
        """Validate @context field."""
        if "@context" not in metadata:
            self.errors.append(ValidationError(field="@context", message="Missing @context field"))
            return

        context = metadata["@context"]

        # Check if it's a string (path to context.jsonld) or dict
        if isinstance(context, str):
            # Should reference context.jsonld
            if "context.jsonld" not in context:
                self.warnings.append(
                    ValidationError(
                        field="@context",
                        message="@context should reference context.jsonld",
                        severity="warning",
                    )
                )
        elif isinstance(context, dict):
            # Should have '@vocab' and namespace prefixes
            if "@vocab" not in context:
                self.warnings.append(
                    ValidationError(
                        field="@context",
                        message="@context dict should have @vocab",
                        severity="warning",
                    )
                )
        else:
            self.errors.append(
                ValidationError(field="@context", message="@context must be string or dict")
            )

    def _validate_dublin_core(self, metadata: dict) -> None:
        """Validate Dublin Core fields."""
        if "dc" not in metadata:
            self.errors.append(
                ValidationError(field="dc", message="Missing 'dc' section for Dublin Core metadata")
            )
            return

        dc = metadata["dc"]
        if not isinstance(dc, dict):
            self.errors.append(
                ValidationError(field="dc", message="'dc' section must be a dictionary")
            )
            return

        # Check mandatory fields
        for field in self.REQUIRED_DC_FIELDS:
            if field not in dc:
                self.errors.append(
                    ValidationError(
                        field=f"dc:{field}", message=f"Missing mandatory Dublin Core field: {field}"
                    )
                )
            elif dc[field] in [None, "", []]:
                self.errors.append(
                    ValidationError(
                        field=f"dc:{field}", message=f"Dublin Core field cannot be empty: {field}"
                    )
                )

        # Validate date format (ISO 8601)
        if "date" in dc and dc["date"]:
            self._validate_date_format(dc["date"])

        # Validate subject is list
        if "subject" in dc and dc["subject"]:
            if not isinstance(dc["subject"], list):
                self.errors.append(
                    ValidationError(
                        field="dc:subject",
                        message="dc:subject must be a list (e.g., ['topic1', 'topic2'])",
                    )
                )

    def _validate_date_format(self, date_str: str) -> None:
        """Validate date is in ISO 8601 format."""
        # Try parsing as ISO 8601
        valid_formats = [
            "%Y-%m-%d",  # 2026-01-11
            "%Y-%m-%dT%H:%M:%S",  # 2026-01-11T13:00:00
            "%Y-%m-%dT%H:%M:%S%z",  # 2026-01-11T13:00:00-06:00
        ]

        for fmt in valid_formats:
            try:
                datetime.strptime(date_str.replace("Z", "+00:00").split(".")[0], fmt)
                return  # Valid format
            except ValueError:
                continue

        self.warnings.append(
            ValidationError(
                field="dc:date",
                message=f"Date '{date_str}' not in ISO 8601 format (recommended: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)",
                severity="warning",
            )
        )

    def _validate_spec_fields(self, metadata: dict) -> None:
        """Validate spec:* fields."""
        if "spec" not in metadata:
            self.errors.append(ValidationError(field="spec", message="Missing 'spec' section"))
            return

        spec = metadata["spec"]
        if not isinstance(spec, dict):
            self.errors.append(
                ValidationError(field="spec", message="'spec' section must be a dictionary")
            )
            return

        # Check mandatory fields
        for field in self.REQUIRED_SPEC_FIELDS:
            if field not in spec:
                self.errors.append(
                    ValidationError(
                        field=f"spec:{field}", message=f"Missing mandatory spec field: {field}"
                    )
                )
            elif spec[field] in [None, ""]:
                self.errors.append(
                    ValidationError(
                        field=f"spec:{field}", message=f"Spec field cannot be empty: {field}"
                    )
                )

        # Validate spec:issue format (should be like SPEC-000 or similar)
        if "issue" in spec and spec["issue"]:
            issue = spec["issue"]
            if not isinstance(issue, str):
                self.errors.append(
                    ValidationError(field="spec:issue", message="spec:issue must be a string")
                )
            elif not issue.startswith("SPEC-") and not issue.startswith("spec-"):
                self.warnings.append(
                    ValidationError(
                        field="spec:issue",
                        message=f"spec:issue '{issue}' should start with 'SPEC-' or 'spec-'",
                        severity="warning",
                    )
                )

    def _validate_keter_doc(self, metadata: dict) -> None:
        """Validate keter-doc:* fields (optional but recommended)."""
        if "keter-doc" not in metadata:
            self.warnings.append(
                ValidationError(
                    field="keter-doc",
                    message="Missing 'keter-doc' section (recommended for KeterDoc metadata)",
                    severity="warning",
                )
            )
            return

        keter = metadata["keter-doc"]
        if not isinstance(keter, dict):
            self.errors.append(
                ValidationError(
                    field="keter-doc", message="'keter-doc' section must be a dictionary"
                )
            )
            return

        # Check version field
        if "version" not in keter:
            self.warnings.append(
                ValidationError(
                    field="keter-doc:version",
                    message="Missing keter-doc:version (recommended)",
                    severity="warning",
                )
            )

        # Check schema field
        if "schema" not in keter:
            self.warnings.append(
                ValidationError(
                    field="keter-doc:schema",
                    message="Missing keter-doc:schema URL (recommended)",
                    severity="warning",
                )
            )

    def _create_report(self) -> ValidationReport:
        """Create validation report."""
        return ValidationReport(
            file_path=self.file_path, errors=self.errors, warnings=self.warnings
        )


def print_report(report: ValidationReport, verbose: bool = False) -> None:
    """Print validation report to console."""
    print(f"\n{'=' * 60}")
    print(f"Metadata Validation Report: {report.file_path.name}")
    print(f"{'=' * 60}\n")

    if report.is_valid and len(report.warnings) == 0:
        print("✅ All metadata checks passed!")
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


def main():
    parser = argparse.ArgumentParser(
        description="Validate YAML-LD metadata in workbook README files"
    )
    parser.add_argument("readme_file", type=Path, help="Path to README.md file to validate")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # Validate metadata
    validator = MetadataValidator(args.readme_file)
    report = validator.validate()

    # Print report
    print_report(report, verbose=args.verbose)

    # Exit with appropriate code
    sys.exit(report.exit_code)


if __name__ == "__main__":
    main()
