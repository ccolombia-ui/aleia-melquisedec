"""
Template Hierarchy Module for daath-zen templates.

This module implements the template inheritance system that resolves
base + variant templates with LRU caching for performance.
"""

from .template_hierarchy import TemplateConfig, TemplateHierarchy, TemplateVariant

__all__ = [
    "TemplateHierarchy",
    "TemplateConfig",
    "TemplateVariant",
]

__version__ = "1.0.0"
