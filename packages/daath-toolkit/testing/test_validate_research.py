"""
Tests for validators.validate_research module

Tests:
- Valid research structure validation
- Missing PROPOSITO.md detection
- Invalid YAML frontmatter handling
- Folder structure validation
- Empty folder detection
- Status field validation
"""

import pytest
from pathlib import Path
import sys
from pathlib import Path as PathLib

# Add parent directory to path for imports
sys.path.insert(0, str(PathLib(__file__).parent.parent))

from validators.validate_research import ResearchValidator


class TestResearchValidator:
    """Test suite for ResearchValidator"""

    def test_valid_research_passes_validation(self, valid_research_structure):
        """Valid research structure should pass all checks"""
        validator = ResearchValidator(valid_research_structure)
        result = validator.validate()

        assert result is True
        assert len(validator.errors) == 0

    def test_missing_proposito_fails(self, invalid_research_structure):
        """Research without PROPOSITO.md should fail"""
        validator = ResearchValidator(invalid_research_structure)
        result = validator.validate()

        assert result is False
        assert any("PROPOSITO.md no existe" in error for error in validator.errors)

    def test_proposito_with_missing_fields(self, temp_research_dir, invalid_proposito_content):
        """PROPOSITO.md with missing required fields should fail"""
        research_path = temp_research_dir / "DD-001-incomplete"
        research_path.mkdir()
        (research_path / "PROPOSITO.md").write_text(invalid_proposito_content, encoding='utf-8')

        validator = ResearchValidator(research_path)
        result = validator.validate()

        assert result is False
        # Should have errors for missing fields
        assert any("falta campo" in error for error in validator.errors)

    def test_proposito_without_yaml_generates_warning(self, temp_research_dir, proposito_without_yaml):
        """PROPOSITO.md without YAML frontmatter should generate warning"""
        research_path = temp_research_dir / "DD-001-no-yaml"
        research_path.mkdir()
        (research_path / "PROPOSITO.md").write_text(proposito_without_yaml, encoding='utf-8')

        validator = ResearchValidator(research_path)
        validator.validate()

        assert any("no tiene YAML frontmatter" in warning for warning in validator.warnings)

    def test_invalid_status_generates_warning(self, temp_research_dir):
        """Invalid status value should generate warning"""
        research_path = temp_research_dir / "DD-001-bad-status"
        research_path.mkdir()

        content = """---
id: DD-001-bad-status
version: 1.0.0
created: 2024-01-15T10:00:00Z
status: invalid-status
purpose: Test
initiated_by: HYPATIA
---

# Test
"""
        (research_path / "PROPOSITO.md").write_text(content, encoding='utf-8')

        validator = ResearchValidator(research_path)
        validator.validate()

        assert any("Status" in warning and "no es estándar" in warning for warning in validator.warnings)

    def test_valid_folders_accepted(self, valid_research_structure):
        """Valid folder names should be accepted"""
        validator = ResearchValidator(valid_research_structure)
        validator.validate()

        # No errors related to folder structure
        folder_errors = [e for e in validator.errors if "carpeta" in e.lower()]
        assert len(folder_errors) == 0

    def test_info_messages_generated_for_valid_fields(self, valid_research_structure):
        """Valid metadata fields should generate info messages"""
        validator = ResearchValidator(valid_research_structure)
        validator.validate()

        # Should have info messages for parsed fields
        assert len(validator.info) > 0
        assert any("id:" in info for info in validator.info)
        assert any("version:" in info for info in validator.info)

    def test_yaml_parsing_error_detected(self, temp_research_dir):
        """Malformed YAML should be caught"""
        research_path = temp_research_dir / "DD-001-bad-yaml"
        research_path.mkdir()

        content = """---
id: DD-001-bad-yaml
version: 1.0.0
created: 2024-01-15T10:00:00Z
status: active
purpose: Test
initiated_by: HYPATIA
invalid yaml structure [[[
---

# Test
"""
        (research_path / "PROPOSITO.md").write_text(content, encoding='utf-8')

        validator = ResearchValidator(research_path)
        validator.validate()

        assert any("Error parseando YAML" in error for error in validator.errors)

    def test_empty_research_directory(self, temp_research_dir):
        """Empty research directory should fail"""
        research_path = temp_research_dir / "DD-001-empty"
        research_path.mkdir()

        validator = ResearchValidator(research_path)
        result = validator.validate()

        assert result is False
        assert any("PROPOSITO.md no existe" in error for error in validator.errors)

    def test_required_fields_all_validated(self, temp_research_dir):
        """All required fields should be validated"""
        research_path = temp_research_dir / "DD-001-complete"
        research_path.mkdir()

        # Complete valid PROPOSITO.md
        content = """---
id: DD-001-complete
version: 1.0.0
created: 2024-01-15T10:00:00Z
status: active
purpose: Complete research
initiated_by: HYPATIA
---

# Complete Research
"""
        (research_path / "PROPOSITO.md").write_text(content, encoding='utf-8')

        validator = ResearchValidator(research_path)
        validator.validate()

        # Check that all required fields were validated
        required_fields = ['id', 'version', 'created', 'status', 'purpose', 'initiated_by']
        for field in required_fields:
            assert any(field in info for info in validator.info)
