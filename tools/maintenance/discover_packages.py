#!/usr/bin/env python3
"""
Package Discovery Mechanism for ALEIA-MELQUISEDEC Monorepo

Automatically discovers packages by scanning pyproject.toml files,
supports both pip and poetry formats, and generates dependency graph.

Usage:
    python tools/maintenance/discover_packages.py
    python tools/maintenance/discover_packages.py --format json
    python tools/maintenance/discover_packages.py --graph

Author: SALOMON (architect)
Rostro: SALOMON Analyzer
Task: 1.4 - Package discovery mechanism
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

try:
    import tomli as tomllib
except ImportError:
    try:
        import tomllib  # Python 3.11+
    except ImportError:
        print("ERROR: Please install tomli: pip install tomli")
        sys.exit(1)


class PackageDiscovery:
    """Discovers and analyzes packages in the monorepo."""

    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.packages: Dict[str, Dict] = {}

    def discover(self) -> Dict[str, Dict]:
        """Discover all packages with pyproject.toml files."""
        pyproject_files = self.root_path.rglob("**/pyproject.toml")

        for pyproject_path in pyproject_files:
            # Skip virtual environments and cache directories
            if any(
                part in pyproject_path.parts
                for part in [".venv", "venv", "__pycache__", ".cache", "node_modules"]
            ):
                continue

            package_info = self._parse_pyproject(pyproject_path)
            if package_info:
                package_name = package_info["name"]
                self.packages[package_name] = package_info

        return self.packages

    def _parse_pyproject(self, pyproject_path: Path) -> Optional[Dict]:
        """Parse a pyproject.toml file and extract package information."""
        try:
            with open(pyproject_path, "rb") as f:
                data = tomllib.load(f)

            # Support both poetry and PEP 621 format
            if "project" in data:
                # PEP 621 format (pip)
                project = data["project"]
                package_info = {
                    "name": project.get("name", "unknown"),
                    "version": project.get("version", "0.0.0"),
                    "description": project.get("description", ""),
                    "path": str(pyproject_path.parent.relative_to(self.root_path)),
                    "format": "pip",
                    "dependencies": project.get("dependencies", []),
                    "optional_dependencies": project.get("optional-dependencies", {}),
                    "authors": [author.get("name", "") for author in project.get("authors", [])],
                    "requires_python": project.get("requires-python", ""),
                }
            elif "tool" in data and "poetry" in data["tool"]:
                # Poetry format
                poetry = data["tool"]["poetry"]
                package_info = {
                    "name": poetry.get("name", "unknown"),
                    "version": poetry.get("version", "0.0.0"),
                    "description": poetry.get("description", ""),
                    "path": str(pyproject_path.parent.relative_to(self.root_path)),
                    "format": "poetry",
                    "dependencies": list(poetry.get("dependencies", {}).keys()),
                    "dev_dependencies": list(poetry.get("dev-dependencies", {}).keys()),
                    "authors": poetry.get("authors", []),
                }
            else:
                # No recognized format
                return None

            return package_info

        except Exception as e:
            print(f"Warning: Failed to parse {pyproject_path}: {e}", file=sys.stderr)
            return None

    def generate_graph(self) -> Dict[str, List[str]]:
        """Generate a dependency graph of packages."""
        graph = {}

        for package_name, package_info in self.packages.items():
            deps = []

            # Extract dependency names from dependencies list
            if package_info["format"] == "pip":
                for dep in package_info["dependencies"]:
                    # Handle version specifiers (e.g., "package>=1.0.0" -> "package")
                    dep_name = dep.split("[")[0].split(">")[0].split("=")[0].split("<")[0].strip()
                    if dep_name in self.packages:
                        deps.append(dep_name)
            elif package_info["format"] == "poetry":
                for dep in package_info["dependencies"]:
                    if dep != "python" and dep in self.packages:
                        deps.append(dep)

            graph[package_name] = deps

        return graph

    def print_summary(self):
        """Print a human-readable summary of discovered packages."""
        print(f"\n🔍 Package Discovery Results")
        print("=" * 60)
        print(f"Root: {self.root_path}")
        print(f"Packages found: {len(self.packages)}\n")

        for package_name, info in sorted(self.packages.items()):
            print(f"📦 {package_name} v{info['version']}")
            print(f"   Path: {info['path']}")
            print(f"   Format: {info['format']}")
            print(f"   Description: {info['description']}")

            if info["format"] == "pip":
                print(f"   Dependencies: {len(info['dependencies'])}")
                if info["optional_dependencies"]:
                    print(f"   Optional groups: {', '.join(info['optional_dependencies'].keys())}")
            else:  # poetry
                print(f"   Dependencies: {len(info['dependencies'])}")
                print(f"   Dev dependencies: {len(info.get('dev_dependencies', []))}")

            print()

    def print_graph(self):
        """Print dependency graph in human-readable format."""
        graph = self.generate_graph()

        print("\n🕸️  Dependency Graph")
        print("=" * 60)

        for package, deps in sorted(graph.items()):
            if deps:
                print(f"{package}")
                for dep in deps:
                    print(f"  └─ {dep}")
            else:
                print(f"{package} (no internal dependencies)")

        print()


def main():
    parser = argparse.ArgumentParser(description="Discover packages in ALEIA-MELQUISEDEC monorepo")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--graph",
        action="store_true",
        help="Show dependency graph",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Root path of monorepo (default: current directory)",
    )

    args = parser.parse_args()

    # Discover packages
    discovery = PackageDiscovery(args.root)
    packages = discovery.discover()

    if args.format == "json":
        # JSON output
        output = {
            "packages": packages,
            "graph": discovery.generate_graph() if args.graph else None,
        }
        print(json.dumps(output, indent=2))
    else:
        # Human-readable output
        discovery.print_summary()
        if args.graph:
            discovery.print_graph()


if __name__ == "__main__":
    main()
