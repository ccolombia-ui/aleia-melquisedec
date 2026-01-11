"""
Unit tests for validate_metadata.py

Tests:
- Parse valid YAML frontmatter
- Detect missing/invalid frontmatter
- Validate Dublin Core fields
- Validate spec fields
- Validate date formats
- Validate @context field
- Validate keter-doc fields
"""

import sys
import tempfile
from pathlib import Path

import pytest

# Add tools/validation to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools" / "validation"))

from validate_metadata import MetadataValidator, ValidationError


@pytest.fixture
def temp_dir():
    """Create temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def valid_metadata():
    """Valid metadata YAML."""
    return """---
'@context': '../../../context.jsonld'
'@type': 'Workbook'
'@id': 'urn:melquisedec:workbook:test'
dc:
  title: "Test Workbook"
  creator: "HYPATIA"
  date: "2026-01-11"
  subject: ["testing", "validation"]
  description: "Test workbook for validation"
  type: "AcademicResearch"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  owner: "HYPATIA"
  status: "in-progress"
keter-doc:
  version: "1.0.0"
  schema: "https://schema.org/CreativeWork"
---

# Test Workbook
"""


def test_valid_metadata(temp_dir, valid_metadata):
    """Test validation of valid metadata."""
    readme = temp_dir / "README.md"
    readme.write_text(valid_metadata)

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert report.is_valid
    assert len(report.errors) == 0
    assert report.exit_code == 0


def test_missing_file():
    """Test validation of non-existent file."""
    validator = MetadataValidator(Path("nonexistent.md"))
    report = validator.validate()

    assert not report.is_valid
    assert len(report.errors) == 1
    assert "File not found" in report.errors[0].message


def test_missing_frontmatter(temp_dir):
    """Test detection of missing YAML frontmatter."""
    readme = temp_dir / "README.md"
    readme.write_text("# No frontmatter here")

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("Missing YAML frontmatter" in e.message for e in report.errors)


def test_invalid_yaml_syntax(temp_dir):
    """Test detection of invalid YAML syntax."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
dc:
  title: [unclosed bracket
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("Invalid YAML syntax" in e.message for e in report.errors)


def test_missing_context(temp_dir):
    """Test detection of missing @context field."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
dc:
  title: "Test"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("@context" in e.field for e in report.errors)


def test_missing_dc_section(temp_dir):
    """Test detection of missing 'dc' section."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
spec:
  issue: "SPEC-000"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("Missing 'dc' section" in e.message for e in report.errors)


def test_missing_dc_field(temp_dir):
    """Test detection of missing mandatory Dublin Core field."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  # Missing other required fields
spec:
  issue: "SPEC-000"
  owner: "TEST"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    # Should have errors for missing DC fields
    dc_errors = [e for e in report.errors if e.field.startswith("dc:")]
    assert len(dc_errors) > 0


def test_empty_dc_field(temp_dir):
    """Test detection of empty Dublin Core field."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: ""
  creator: "TEST"
  date: "2026-01-11"
  subject: []
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  owner: "TEST"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("title" in e.field and "cannot be empty" in e.message for e in report.errors)


def test_missing_spec_section(temp_dir):
    """Test detection of missing 'spec' section."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "2026-01-11"
  subject: ["test"]
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("Missing 'spec' section" in e.message for e in report.errors)


def test_missing_spec_field(temp_dir):
    """Test detection of missing mandatory spec field."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "2026-01-11"
  subject: ["test"]
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  # Missing owner field
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("spec:owner" in e.field for e in report.errors)


def test_invalid_date_format(temp_dir):
    """Test warning for invalid date format."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "11/01/2026"
  subject: ["test"]
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  owner: "TEST"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    # Should pass but have warning
    assert report.is_valid
    assert len(report.warnings) > 0
    assert any("ISO 8601" in w.message for w in report.warnings)


def test_valid_iso_date_formats(temp_dir):
    """Test acceptance of valid ISO 8601 date formats."""
    dates = ["2026-01-11", "2026-01-11T13:00:00", "2026-01-11T13:00:00-06:00"]

    for date in dates:
        readme = temp_dir / f'README_{date.replace(":", "_")}.md'
        readme.write_text(
            f"""---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "{date}"
  subject: ["test"]
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  owner: "TEST"
---"""
        )

        validator = MetadataValidator(readme)
        report = validator.validate()

        # Should not have date format warnings
        date_warnings = [w for w in report.warnings if "ISO 8601" in w.message]
        assert len(date_warnings) == 0, f"Date format {date} should be valid"


def test_keter_doc_warning(temp_dir):
    """Test warning for missing keter-doc section."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "2026-01-11"
  subject: ["test"]
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  owner: "TEST"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert report.is_valid
    assert any("keter-doc" in w.field for w in report.warnings)


def test_subject_must_be_list(temp_dir):
    """Test that dc:subject must be a list."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "2026-01-11"
  subject: "single-string"
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "SPEC-000"
  owner: "TEST"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert not report.is_valid
    assert any("subject must be a list" in e.message for e in report.errors)


def test_spec_issue_format_warning(temp_dir):
    """Test warning for non-standard spec:issue format."""
    readme = temp_dir / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
dc:
  title: "Test"
  creator: "TEST"
  date: "2026-01-11"
  subject: ["test"]
  description: "Test"
  type: "Test"
  format: "Markdown"
  language: "en"
  identifier: "test-001"
spec:
  issue: "my-issue-123"
  owner: "TEST"
---"""
    )

    validator = MetadataValidator(readme)
    report = validator.validate()

    assert report.is_valid
    assert any("should start with" in w.message for w in report.warnings)
