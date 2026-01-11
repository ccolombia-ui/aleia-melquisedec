"""
Unit tests for validate_imrad_structure.py

Tests:
- Validate complete IMRAD structure
- Detect missing required files
- Validate section headers
- Detect missing sections
- Validate README metadata integration
"""

import sys
import tempfile
from pathlib import Path

import pytest

# Add tools/validation to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools" / "validation"))

from validate_imrad_structure import IMRADValidator


@pytest.fixture
def temp_workbook():
    """Create temporary workbook directory with IMRAD structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        workbook_dir = Path(tmpdir) / "test-workbook"
        workbook_dir.mkdir()

        # Create README with valid metadata
        readme = workbook_dir / "README.md"
        readme.write_text(
            """---
'@context': '../../../context.jsonld'
'@type': 'Workbook'
'@id': 'urn:melquisedec:workbook:test'
dc:
  title: "Test IMRAD Workbook"
  creator: "HYPATIA"
  date: "2026-01-11"
  subject: ["testing", "imrad"]
  description: "Test workbook for IMRAD validation"
  type: "IMRADResearch"
  format: "Markdown"
  language: "en"
  identifier: "test-imrad-001"
spec:
  issue: "SPEC-000"
  owner: "HYPATIA"
  status: "in-progress"
keter-doc:
  version: "1.0.0"
  schema: "https://schema.org/CreativeWork"
---

# Test IMRAD Workbook

Overview of the IMRAD workbook.
"""
        )

        yield workbook_dir


@pytest.fixture
def complete_imrad_structure(temp_workbook):
    """Create complete IMRAD structure."""
    files = {
        "01-introduction.md": """# 1. Introduction

## 1.1 Background

Background content.

## 1.2 Research Question

What is the question?
""",
        "02-methodology.md": """# 2. Methodology

## 2.1 Research Design

Design description.

## 2.2 Data Collection

Collection methods.
""",
        "03-results.md": """# 3. Results

## 3.1 Findings

The findings.
""",
        "04-analysis.md": """# 4. Analysis

## 4.1 Interpretation

Interpretation of results.
""",
        "05-discussion.md": """# 5. Discussion

## 5.1 Key Insights

Key insights.

## 5.2 Limitations

Study limitations.
""",
        "06-conclusion.md": """# 6. Conclusion

## 6.1 Summary

Summary of findings.

## 6.2 Future Work

Next steps.
""",
        "07-references.md": """# 7. References

## 7.1 Bibliography

[1] Reference 1

## 7.2 Appendices

Appendix A.
""",
    }

    for filename, content in files.items():
        (temp_workbook / filename).write_text(content)

    return temp_workbook


def test_valid_imrad_structure(complete_imrad_structure):
    """Test validation of complete valid IMRAD structure."""
    validator = IMRADValidator(complete_imrad_structure)
    report = validator.validate()

    assert report.is_valid
    assert len(report.errors) == 0
    assert report.exit_code == 0


def test_nonexistent_workbook():
    """Test validation of non-existent workbook directory."""
    validator = IMRADValidator(Path("nonexistent"))
    report = validator.validate()

    assert not report.is_valid
    assert len(report.errors) == 1
    assert "does not exist" in report.errors[0].message


def test_missing_required_file(temp_workbook):
    """Test detection of missing required IMRAD file."""
    # Create all files except 03-results.md
    files = [
        "01-introduction.md",
        "02-methodology.md",
        "04-analysis.md",
        "05-discussion.md",
        "06-conclusion.md",
        "07-references.md",
    ]

    for filename in files:
        (temp_workbook / filename).write_text(f"# {filename}\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("03-results.md" in e.field for e in report.errors)


def test_missing_multiple_files(temp_workbook):
    """Test detection of multiple missing files."""
    # Only create 2 files
    (temp_workbook / "01-introduction.md").write_text("# Introduction")
    (temp_workbook / "07-references.md").write_text("# References")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    # Should have errors for 5 missing files
    missing_errors = [e for e in report.errors if "Missing required file" in e.message]
    assert len(missing_errors) == 5


def test_missing_main_header(temp_workbook):
    """Test detection of missing main section header."""
    (temp_workbook / "01-introduction.md").write_text(
        """## 1.1 Background

No main header here.
"""
    )

    # Create other required files minimally
    for i in range(2, 8):
        filename = f"0{i}-test.md"
        (temp_workbook / filename).write_text(f"# {i}. Test\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any(
        "Missing main header" in e.message and "01-introduction.md" in e.field
        for e in report.errors
    )


def test_incorrect_main_header_level(temp_workbook):
    """Test detection of incorrect header level (not h1)."""
    (temp_workbook / "01-introduction.md").write_text(
        """## 1. Introduction

Incorrect header level.
"""
    )

    # Create other required files
    for i in range(2, 8):
        (temp_workbook / f"0{i}-test.md").write_text(f"# {i}. Test\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("should be h1" in e.message for e in report.errors)


def test_missing_expected_subsection(temp_workbook):
    """Test detection of missing expected subsection."""
    (temp_workbook / "01-introduction.md").write_text(
        """# 1. Introduction

## 1.1 Background

Background content.

# Missing 1.2 Research Question
"""
    )

    # Create other required files
    for i in range(2, 8):
        (temp_workbook / f"0{i}-test.md").write_text(f"# {i}. Test\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any(
        "Missing expected section" in e.message and "1.2" in e.message for e in report.errors
    )


def test_readme_metadata_integration(temp_workbook):
    """Test that README metadata validation is integrated."""
    # Create invalid README (missing dc section)
    readme = temp_workbook / "README.md"
    readme.write_text(
        """---
'@context': 'context.jsonld'
spec:
  issue: "SPEC-000"
---

# Test
"""
    )

    # Create valid IMRAD files
    for i in range(1, 8):
        (temp_workbook / f"0{i}-test.md").write_text(f"# {i}. Test\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    # Should fail due to invalid README metadata
    assert not report.is_valid
    assert any("README.md" in e.field for e in report.errors)


def test_missing_readme(temp_workbook):
    """Test detection of missing README.md."""
    # Remove README
    (temp_workbook / "README.md").unlink()

    # Create valid IMRAD files
    for i in range(1, 8):
        (temp_workbook / f"0{i}-test.md").write_text(f"# {i}. Test\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("README.md not found" in e.message for e in report.errors)


def test_file_headers_validation(complete_imrad_structure):
    """Test that all file headers are validated correctly."""
    validator = IMRADValidator(complete_imrad_structure)
    report = validator.validate()

    # Should validate all 7 files
    assert report.is_valid
    assert len(report.errors) == 0


def test_empty_imrad_file(temp_workbook):
    """Test detection of empty IMRAD file."""
    (temp_workbook / "01-introduction.md").write_text("")

    # Create other files
    for i in range(2, 8):
        (temp_workbook / f"0{i}-test.md").write_text(f"# {i}. Test\n\nContent.")

    validator = IMRADValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("Missing main header" in e.message for e in report.errors)


def test_all_section_headers_present(complete_imrad_structure):
    """Test validation when all expected section headers are present."""
    validator = IMRADValidator(complete_imrad_structure)
    report = validator.validate()

    # Should have no errors about missing sections
    section_errors = [e for e in report.errors if "Missing expected section" in e.message]
    assert len(section_errors) == 0
