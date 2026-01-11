"""
Unit tests for validate_academic_research.py

Tests:
- Validate complete Academic Research structure
- Detect missing required folders
- Validate atomics naming convention
- Validate literature folder structure
- Validate README metadata integration
"""

import sys
import tempfile
from pathlib import Path

import pytest

# Add tools/validation to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools" / "validation"))

from validate_academic_research import AcademicResearchValidator


@pytest.fixture
def temp_workbook():
    """Create temporary workbook directory for Academic Research structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        workbook_dir = Path(tmpdir) / "test-academic-workbook"
        workbook_dir.mkdir()

        # Create README with valid metadata
        readme = workbook_dir / "README.md"
        readme.write_text(
            """---
'@context': '../../../context.jsonld'
'@type': 'Workbook'
'@id': 'urn:melquisedec:workbook:academic-test'
dc:
  title: "Test Academic Research Workbook"
  creator: "HYPATIA"
  date: "2026-01-11"
  subject: ["testing", "academic-research"]
  description: "Test workbook for Academic Research validation"
  type: "AcademicResearch"
  format: "Markdown"
  language: "en"
  identifier: "test-academic-001"
spec:
  issue: "SPEC-000"
  owner: "HYPATIA"
  status: "in-progress"
keter-doc:
  version: "1.0.0"
  schema: "https://schema.org/CreativeWork"
---

# Test Academic Research Workbook

Overview of the academic research workbook.
"""
        )

        yield workbook_dir


@pytest.fixture
def complete_academic_structure(temp_workbook):
    """Create complete Academic Research structure."""
    # Create required folders
    folders = [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]

    for folder in folders:
        (temp_workbook / folder).mkdir()

        # Create valid atomics in folders 1-4
        if folder != "6-literature":
            atomic_file = temp_workbook / folder / f'atomic-001-{folder.split("-")[1]}.md'
            atomic_file.write_text(
                f"""# Atomic: {folder}

Content for {folder}.
"""
            )

    # Create sources.yaml in literature folder
    sources_yaml = temp_workbook / "6-literature" / "sources.yaml"
    sources_yaml.write_text(
        """---
sources:
  - id: "source-001"
    title: "Test Source"
    author: "Test Author"
    year: 2026
---
"""
    )

    return temp_workbook


def test_valid_academic_structure(complete_academic_structure):
    """Test validation of complete valid Academic Research structure."""
    validator = AcademicResearchValidator(complete_academic_structure)
    report = validator.validate()

    assert report.is_valid
    assert len(report.errors) == 0
    assert report.exit_code == 0


def test_nonexistent_workbook():
    """Test validation of non-existent workbook directory."""
    validator = AcademicResearchValidator(Path("nonexistent"))
    report = validator.validate()

    assert not report.is_valid
    assert len(report.errors) == 1
    assert "does not exist" in report.errors[0].message


def test_missing_required_folder(temp_workbook):
    """Test detection of missing required folder."""
    # Create all folders except 3-data-analysis
    folders = [
        "1-theoretical-foundation",
        "2-research-methodology",
        "4-results-synthesis",
        "6-literature",
    ]

    for folder in folders:
        (temp_workbook / folder).mkdir()

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("3-data-analysis" in e.field for e in report.errors)


def test_missing_multiple_folders(temp_workbook):
    """Test detection of multiple missing folders."""
    # Only create 2 folders
    (temp_workbook / "1-theoretical-foundation").mkdir()
    (temp_workbook / "6-literature").mkdir()

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    # Should have errors for 3 missing folders (2, 3, 4)
    missing_errors = [e for e in report.errors if "Missing required folder" in e.message]
    assert len(missing_errors) == 3


def test_atomics_naming_convention_valid(temp_workbook):
    """Test validation of correct atomics naming convention."""
    folder = temp_workbook / "1-theoretical-foundation"
    folder.mkdir()

    # Create valid atomic files
    (folder / "atomic-001-ontology.md").write_text("# Atomic: Ontology")
    (folder / "atomic-002-epistemology.md").write_text("# Atomic: Epistemology")

    # Create other required folders minimally
    for f in ["2-research-methodology", "3-data-analysis", "4-results-synthesis", "6-literature"]:
        (temp_workbook / f).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    # Should have no errors about atomics naming
    atomics_errors = [e for e in report.errors if "atomic-" in e.message.lower()]
    assert len(atomics_errors) == 0


def test_atomics_naming_convention_invalid(temp_workbook):
    """Test detection of invalid atomics naming convention."""
    folder = temp_workbook / "1-theoretical-foundation"
    folder.mkdir()

    # Create invalid atomic files
    (folder / "atomic-1-bad.md").write_text("# Bad naming")  # Wrong: missing leading zero
    (folder / "atomic-002-goodname.md").write_text("# Good")  # Valid
    (folder / "not-atomic.md").write_text("# Not atomic")  # Doesn't match pattern

    # Create other required folders
    for f in ["2-research-methodology", "3-data-analysis", "4-results-synthesis", "6-literature"]:
        (temp_workbook / f).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    # Should have error for atomic-1-bad.md
    naming_errors = [e for e in report.errors if "atomic-1-bad.md" in e.field]
    assert len(naming_errors) == 1


def test_literature_sources_yaml_present(temp_workbook):
    """Test validation when sources.yaml is present."""
    # Create all required folders
    for f in [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]:
        (temp_workbook / f).mkdir()

    # Create sources.yaml
    (temp_workbook / "6-literature" / "sources.yaml").write_text(
        """---
sources:
  - id: "test-source"
    title: "Test"
---
"""
    )

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    # Should have no errors about missing sources.yaml
    sources_errors = [e for e in report.errors if "sources.yaml" in e.field]
    assert len(sources_errors) == 0


def test_literature_sources_yaml_missing(temp_workbook):
    """Test detection of missing sources.yaml."""
    # Create all required folders
    for f in [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]:
        (temp_workbook / f).mkdir()

    # Don't create sources.yaml

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("sources.yaml not found" in e.message for e in report.errors)


def test_readme_metadata_integration(temp_workbook):
    """Test that README metadata validation is integrated."""
    # Create invalid README (missing spec section)
    readme = temp_workbook / "README.md"
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
---

# Test
"""
    )

    # Create valid folder structure
    for f in [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]:
        (temp_workbook / f).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    # Should fail due to invalid README metadata
    assert not report.is_valid
    assert any("README.md" in e.field for e in report.errors)


def test_missing_readme(temp_workbook):
    """Test detection of missing README.md."""
    # Remove README
    (temp_workbook / "README.md").unlink()

    # Create valid folder structure
    for f in [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]:
        (temp_workbook / f).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    assert any("README.md not found" in e.message for e in report.errors)


def test_no_folder_5(temp_workbook):
    """Test that folder 5 is correctly skipped (not required)."""
    # Create all required folders (note: no folder 5)
    folders = [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]

    for folder in folders:
        (temp_workbook / folder).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    # Should not have errors about missing folder 5
    folder_5_errors = [e for e in report.errors if "5-" in e.field]
    assert len(folder_5_errors) == 0


def test_empty_atomics_folder_allowed(temp_workbook):
    """Test that empty atomics folders are allowed (no atomics yet)."""
    # Create all required folders without atomics
    for f in [
        "1-theoretical-foundation",
        "2-research-methodology",
        "3-data-analysis",
        "4-results-synthesis",
        "6-literature",
    ]:
        (temp_workbook / f).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    # Empty folders are OK (no atomics requirement)
    assert report.is_valid or all("atomic" not in e.message.lower() for e in report.errors)


def test_multiple_atomics_naming_errors(temp_workbook):
    """Test detection of multiple atomics naming errors."""
    folder = temp_workbook / "1-theoretical-foundation"
    folder.mkdir()

    # Create multiple invalid atomic files
    (folder / "atomic-1-bad.md").write_text("# Bad 1")
    (folder / "atomic-02-bad.md").write_text("# Bad 2 - wrong prefix length")
    (folder / "atomic-999-good.md").write_text("# Good")

    # Create other folders
    for f in ["2-research-methodology", "3-data-analysis", "4-results-synthesis", "6-literature"]:
        (temp_workbook / f).mkdir()

    (temp_workbook / "6-literature" / "sources.yaml").write_text("sources: []")

    validator = AcademicResearchValidator(temp_workbook)
    report = validator.validate()

    assert not report.is_valid
    # Should have errors for atomic-1-bad.md and atomic-02-bad.md
    naming_errors = [e for e in report.errors if "Invalid atomics file naming" in e.message]
    assert len(naming_errors) >= 2
