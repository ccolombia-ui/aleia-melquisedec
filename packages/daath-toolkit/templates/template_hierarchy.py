"""
Template Hierarchy Implementation.

Loads config.yaml-ld and resolves template inheritance (base + variant merge)
with LRU caching for improved performance.

Usage:
    >>> from daath_toolkit.templates import TemplateHierarchy
    >>> hierarchy = TemplateHierarchy('path/to/config.yaml-ld')
    >>> template = hierarchy.load_template('requirements')
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


@dataclass
class TemplateSection:
    """Represents a section in a template."""

    name: str
    position: Optional[str] = None  # e.g., "after:overview"
    mandatory: bool = True
    format: str = "markdown"
    description: str = ""
    source: Optional[str] = None  # "workbook" | "generated"
    path_pattern: Optional[str] = None
    exclude_pattern: Optional[str] = None
    components: Dict[str, str] = field(default_factory=dict)
    structure: Dict[str, Any] = field(default_factory=dict)
    fields: List[str] = field(default_factory=list)
    subsections: List[str] = field(default_factory=list)
    columns: List[str] = field(default_factory=list)
    criteria: List[str] = field(default_factory=list)
    auto_generated: bool = False


@dataclass
class TemplateVariant:
    """Represents a template variant that extends the base template."""

    name: str
    extends: str  # Base template name
    version: str
    file: str
    document_type: str
    phase: str
    description: str
    additional_sections: List[TemplateSection] = field(default_factory=list)


@dataclass
class TemplateConfig:
    """Complete template configuration loaded from config.yaml-ld."""

    version: str
    created: str
    maintainer: str
    schema_version: str
    base_name: str
    base_file: str
    base_sections: List[TemplateSection]
    variants: Dict[str, TemplateVariant]
    transclusion_settings: Dict[str, Any]
    validation_settings: Dict[str, Any]
    compilation_settings: Dict[str, Any]


class TemplateHierarchy:
    """
    Manages template hierarchy with inheritance resolution and caching.

    This class loads the config.yaml-ld file and provides methods to:
    - Load and merge base + variant templates
    - Cache resolved templates for performance
    - Resolve template inheritance chains

    Attributes:
        config_path: Path to config.yaml-ld
        template_dir: Directory containing template files
        config: Loaded TemplateConfig object
    """

    def __init__(self, config_path: str | Path):
        """
        Initialize TemplateHierarchy with configuration file.

        Args:
            config_path: Path to config.yaml-ld file

        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config format is invalid
        """
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        self.template_dir = self.config_path.parent
        self.config = self._load_config()
        self._cache_info = {"hits": 0, "misses": 0}

    def _load_config(self) -> TemplateConfig:
        """
        Load and parse config.yaml-ld file.

        Returns:
            TemplateConfig object with parsed configuration

        Raises:
            ValueError: If YAML is invalid or required fields missing
        """
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                config_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in config file: {e}")

        # Extract base template info
        base = config_data["template_hierarchy"]["base"]
        base_sections = [
            TemplateSection(
                name=section["name"],
                mandatory=section.get("mandatory", True),
                format=section.get("format", "markdown"),
                description=section.get("description", ""),
                fields=section.get("fields", []),
                auto_generated=section.get("auto_generated", False),
            )
            for section in base["sections"]
        ]

        # Extract variants
        variants = {}
        for variant_name, variant_data in config_data["template_hierarchy"]["variants"].items():
            additional_sections = []
            for section_data in variant_data.get("additional_sections", []):
                section = TemplateSection(
                    name=section_data["name"],
                    position=section_data.get("position"),
                    mandatory=section_data.get("mandatory", True),
                    format=section_data.get("format", "markdown"),
                    description=section_data.get("description", ""),
                    source=section_data.get("source"),
                    path_pattern=section_data.get("path_pattern"),
                    exclude_pattern=section_data.get("exclude_pattern"),
                    components=section_data.get("components", {}),
                    structure=section_data.get("structure", {}),
                    fields=section_data.get("fields", []),
                    subsections=section_data.get("subsections", []),
                    columns=section_data.get("columns", []),
                    criteria=section_data.get("criteria", []),
                )
                additional_sections.append(section)

            variants[variant_name] = TemplateVariant(
                name=variant_name,
                extends=variant_data["extends"],
                version=variant_data["version"],
                file=variant_data["file"],
                document_type=variant_data["document_type"],
                phase=variant_data["phase"],
                description=variant_data["description"],
                additional_sections=additional_sections,
            )

        return TemplateConfig(
            version=config_data["version"],
            created=config_data["created"],
            maintainer=config_data["maintainer"],
            schema_version=config_data["schema_version"],
            base_name=base["name"],
            base_file=base["file"],
            base_sections=base_sections,
            variants=variants,
            transclusion_settings=config_data.get("transclusion", {}),
            validation_settings=config_data.get("validation", {}),
            compilation_settings=config_data.get("compilation", {}),
        )

    @lru_cache(maxsize=32)
    def load_template(self, variant: str) -> str:
        """
        Load and merge base template with variant template.

        Uses LRU cache to avoid reloading templates repeatedly.

        Args:
            variant: Name of template variant (requirements, design, tasks, etc.)

        Returns:
            Merged template content as string

        Raises:
            ValueError: If variant doesn't exist
            FileNotFoundError: If template file not found
        """
        if variant not in self.config.variants:
            raise ValueError(
                f"Variant '{variant}' not found. "
                f"Available: {', '.join(self.config.variants.keys())}"
            )

        self._cache_info["misses"] += 1

        # Load base template
        base_path = self.template_dir / self.config.base_file
        if not base_path.exists():
            raise FileNotFoundError(f"Base template not found: {base_path}")

        with open(base_path, "r", encoding="utf-8") as f:
            base_content = f.read()

        # Load variant template
        variant_config = self.config.variants[variant]
        variant_path = self.template_dir / variant_config.file

        # If variant file exists, merge it; otherwise use base with config
        if variant_path.exists():
            with open(variant_path, "r", encoding="utf-8") as f:
                variant_content = f.read()
            merged = self._merge_templates(base_content, variant_content, variant_config)
        else:
            # Generate variant from base + config
            merged = self._generate_variant_from_config(base_content, variant_config)

        return merged

    def _merge_templates(self, base: str, variant: str, config: TemplateVariant) -> str:
        """
        Merge base template with variant template.

        Merges templates by:
        1. Preserving base HKM header and JSON-LD metadata
        2. Inserting variant-specific sections at configured positions
        3. Replacing {{BODY_SECTIONS}} placeholder with variant content

        Args:
            base: Base template content
            variant: Variant template content
            config: Variant configuration

        Returns:
            Merged template content
        """
        # Strategy: Replace {{BODY_SECTIONS}} in base with variant body
        # Variant body is everything after the "---" separator following metadata

        # Extract variant body (after metadata)
        variant_lines = variant.split("\n")
        body_start = 0
        separator_count = 0

        for i, line in enumerate(variant_lines):
            if line.strip() == "---":
                separator_count += 1
                if separator_count >= 3:  # After HKM, JSON-LD, and title separator
                    body_start = i + 1
                    break

        variant_body = "\n".join(variant_lines[body_start:])

        # Replace {{BODY_SECTIONS}} in base
        merged = base.replace("{{BODY_SECTIONS}}", variant_body)

        return merged

    def _generate_variant_from_config(self, base: str, variant_config: TemplateVariant) -> str:
        """
        Generate variant template from base + configuration.

        Creates variant content by inserting configured sections
        into the base template at specified positions.

        Args:
            base: Base template content
            variant_config: Variant configuration

        Returns:
            Generated variant template
        """
        body_sections = []

        for section in variant_config.additional_sections:
            # Generate section markdown based on configuration
            section_md = self._generate_section_markdown(section)
            body_sections.append(section_md)

        # Join all body sections
        body_content = "\n\n---\n\n".join(body_sections)

        # Replace {{BODY_SECTIONS}} in base
        variant = base.replace("{{BODY_SECTIONS}}", body_content)

        return variant

    def _generate_section_markdown(self, section: TemplateSection) -> str:
        """
        Generate markdown for a section based on its configuration.

        Args:
            section: TemplateSection configuration

        Returns:
            Generated markdown content
        """
        lines = []

        # Section title
        lines.append(f"## {section.name.replace('_', ' ').title()}")
        lines.append("")

        if section.description:
            lines.append(f"_{section.description}_")
            lines.append("")

        # Generate content based on source type
        if section.source == "workbook":
            if section.path_pattern:
                lines.append(f"{{{{{{TRANSCLUDE:{section.path_pattern}}}}}}}}}")
            else:
                lines.append(f"{{{{{{CONTENT_FROM_WORKBOOK:{section.name}}}}}}}}}")
        elif section.source == "generated":
            lines.append(f"{{{{{{GENERATED:{section.name}}}}}}}}}")
        else:
            # Placeholder for manual content
            lines.append(f"{{{{{{CONTENT:{section.name}}}}}}}}}")

        lines.append("")

        return "\n".join(lines)

    def get_variant_config(self, variant: str) -> TemplateVariant:
        """
        Get configuration for a specific variant.

        Args:
            variant: Variant name

        Returns:
            TemplateVariant configuration

        Raises:
            ValueError: If variant doesn't exist
        """
        if variant not in self.config.variants:
            raise ValueError(f"Variant '{variant}' not found")
        return self.config.variants[variant]

    def list_variants(self) -> List[str]:
        """
        Get list of available template variants.

        Returns:
            List of variant names
        """
        return list(self.config.variants.keys())

    def cache_info(self) -> Dict[str, int]:
        """
        Get cache statistics.

        Returns:
            Dictionary with 'hits' and 'misses' counts
        """
        # Get LRU cache info from load_template
        lru_info = self.load_template.cache_info()
        return {
            "hits": lru_info.hits,
            "misses": lru_info.misses,
            "maxsize": lru_info.maxsize,
            "currsize": lru_info.currsize,
        }

    def clear_cache(self) -> None:
        """Clear template cache."""
        self.load_template.cache_clear()
        self._cache_info = {"hits": 0, "misses": 0}
