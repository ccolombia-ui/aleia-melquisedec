"""
Unit tests for TemplateHierarchy class.

Tests template loading, inheritance resolution, caching, and error handling.
"""

from pathlib import Path

import pytest
from daath_toolkit.templates import TemplateConfig, TemplateHierarchy, TemplateVariant


# Fixtures
@pytest.fixture
def config_path():
    """Path to test config.yaml-ld file."""
    base_path = Path(__file__).parent.parent
    return (
        base_path
        / "apps"
        / "R000-autopoietic-template"
        / "_melquisedec"
        / "templates"
        / "config.yaml-ld"
    )


@pytest.fixture
def hierarchy(config_path):
    """TemplateHierarchy instance for testing."""
    return TemplateHierarchy(config_path)


# Test: Configuration Loading
def test_load_config_success(hierarchy):
    """Test that config loads without errors."""
    assert hierarchy.config is not None
    assert isinstance(hierarchy.config, TemplateConfig)
    assert hierarchy.config.version == "1.0.0"


def test_config_has_base_template(hierarchy):
    """Test that base template is defined in config."""
    assert hierarchy.config.base_name == "daath-zen-base"
    assert hierarchy.config.base_file == "daath-zen-base.md"
    assert len(hierarchy.config.base_sections) > 0


def test_config_has_six_variants(hierarchy):
    """Test that all 6 variants are defined."""
    expected_variants = ["requirements", "design", "tasks", "product", "tech", "structure"]
    actual_variants = hierarchy.list_variants()

    assert len(actual_variants) == 6
    for variant in expected_variants:
        assert variant in actual_variants


# Test: Template Loading
def test_load_base_template_exists(hierarchy):
    """Test that base template file exists."""
    base_path = hierarchy.template_dir / hierarchy.config.base_file
    assert base_path.exists(), f"Base template not found: {base_path}"


def test_load_variant_template_returns_string(hierarchy):
    """Test that loading a variant returns a string."""
    template = hierarchy.load_template("requirements")
    assert isinstance(template, str)
    assert len(template) > 0


def test_load_invalid_variant_raises_error(hierarchy):
    """Test that loading non-existent variant raises ValueError."""
    with pytest.raises(ValueError, match="Variant 'invalid' not found"):
        hierarchy.load_template("invalid")


# Test: Template Inheritance
def test_variant_extends_base(hierarchy):
    """Test that variant templates include base sections."""
    template = hierarchy.load_template("requirements")

    # Check for base template markers
    assert "# HKM Header" in template
    assert "@context" in template
    assert "keter-doc-protocol-v1.0.0" in template
    assert "## Metadatos" in template
    assert "## Overview" in template
    assert "## Principios MELQUISEDEC Aplicados" in template


def test_all_variants_extend_base(hierarchy):
    """Test that all variants correctly extend base template."""
    for variant_name in hierarchy.list_variants():
        variant_config = hierarchy.get_variant_config(variant_name)
        assert variant_config.extends == "base", f"Variant {variant_name} doesn't extend base"


# Test: Variant-Specific Content
def test_requirements_has_coherence_matrix_section(hierarchy):
    """Test that requirements variant includes RBM coherence matrix section."""
    variant_config = hierarchy.get_variant_config("requirements")
    section_names = [s.name for s in variant_config.additional_sections]

    assert "coherence_matrix" in section_names
    assert "user_stories" in section_names
    assert "functional_requirements" in section_names


def test_design_has_adr_section(hierarchy):
    """Test that design variant includes ADR section."""
    variant_config = hierarchy.get_variant_config("design")
    section_names = [s.name for s in variant_config.additional_sections]

    assert "adr_decisions" in section_names
    assert "architectural_overview" in section_names


def test_tasks_has_task_list_section(hierarchy):
    """Test that tasks variant includes task list section."""
    variant_config = hierarchy.get_variant_config("tasks")
    section_names = [s.name for s in variant_config.additional_sections]

    assert "task_list" in section_names


# Test: Caching
def test_cache_improves_performance(hierarchy):
    """Test that LRU cache reduces load time on repeated calls."""
    # Clear cache first
    hierarchy.clear_cache()

    # First load (cache miss)
    template1 = hierarchy.load_template("requirements")
    cache_info1 = hierarchy.cache_info()

    # Second load (cache hit)
    template2 = hierarchy.load_template("requirements")
    cache_info2 = hierarchy.cache_info()

    # Templates should be identical
    assert template1 == template2

    # Cache hits should increase
    assert cache_info2["hits"] > cache_info1["hits"]


def test_cache_clear_works(hierarchy):
    """Test that clearing cache resets statistics."""
    # Load template
    hierarchy.load_template("requirements")

    # Clear cache
    hierarchy.clear_cache()
    cache_info = hierarchy.cache_info()

    # Cache should be empty
    assert cache_info["hits"] == 0
    assert cache_info["currsize"] == 0


# Test: Configuration Validation
def test_invalid_config_path_raises_error():
    """Test that invalid config path raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        TemplateHierarchy("/nonexistent/config.yaml-ld")


def test_all_variants_have_required_fields(hierarchy):
    """Test that all variants have required configuration fields."""
    required_fields = [
        "name",
        "extends",
        "version",
        "file",
        "document_type",
        "phase",
        "description",
    ]

    for variant_name in hierarchy.list_variants():
        variant = hierarchy.get_variant_config(variant_name)
        for field in required_fields:
            assert hasattr(variant, field), f"Variant {variant_name} missing field {field}"


# Test: Transclusion Settings
def test_transclusion_settings_loaded(hierarchy):
    """Test that transclusion settings are loaded from config."""
    settings = hierarchy.config.transclusion_settings
    assert settings.get("enabled") is True
    assert settings.get("syntax") == "obsidian"


# Test: Validation Settings
def test_validation_settings_loaded(hierarchy):
    """Test that validation settings are loaded from config."""
    settings = hierarchy.config.validation_settings
    assert "keter_doc" in settings
    assert "rbm_coherence" in settings


# Performance Test
def test_load_template_completes_within_time_limit(hierarchy):
    """Test that template loading completes within 100ms."""
    import time

    start = time.time()
    hierarchy.load_template("requirements")
    duration = time.time() - start

    # Should complete in less than 100ms (0.1 seconds)
    assert duration < 0.1, f"Template loading took {duration:.3f}s, expected < 0.1s"


# Integration Test
def test_full_workflow_all_variants(hierarchy):
    """Test loading all variants successfully."""
    variants = hierarchy.list_variants()

    for variant in variants:
        template = hierarchy.load_template(variant)

        # Basic validation
        assert isinstance(template, str)
        assert len(template) > 100
        assert "# HKM Header" in template
        assert "{{DOCUMENT_TITLE}}" in template


# Test: Error Handling
def test_get_variant_config_invalid_raises_error(hierarchy):
    """Test that getting invalid variant config raises ValueError."""
    with pytest.raises(ValueError, match="Variant 'invalid' not found"):
        hierarchy.get_variant_config("invalid")


def test_list_variants_returns_correct_count(hierarchy):
    """Test that list_variants returns exactly 6 variants."""
    variants = hierarchy.list_variants()
    assert len(variants) == 6
