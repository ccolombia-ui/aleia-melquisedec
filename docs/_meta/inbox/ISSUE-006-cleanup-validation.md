---
id: ISSUE-006
title: Create cleanup script for post-reorganization validation
type: maintenance
area: tooling
priority: low
status: open
created: 2026-01-08
assignee: null
tags: [cleanup, automation, validation]
related_issues: [ISSUE-001, ISSUE-002]
---

# ISSUE-006: Create cleanup script for post-reorganization validation

## 📌 Objetivo

Crear script automatizado que valide la salud del monorepo después de reorganizaciones, detectando archivos huérfanos, directorios vacíos, imports rotos, y otros problemas estructurales.

## 📖 Contexto

Después de la gran reorganización (eliminación de `nucleo-investigacion/`, movimiento de archivos), necesitamos:
- Validar que no quedaron artifacts antiguos
- Detectar directorios vacíos no intencionales
- Encontrar archivos huérfanos sin referencias
- Verificar que estructura cumple con principios DAATH-ZEN

**Solución**: Script `tools/maintenance/cleanup_post_reorganization.py` (ya existe parcialmente) expandido con validaciones adicionales.

## 💡 Solución Propuesta

Expandir `cleanup_post_reorganization.py` con checks adicionales:

### Validaciones a implementar:

1. **Orphan files detection**:
   - Archivos .py sin imports desde otros archivos
   - Archivos .md sin links desde otros docs
   - Archivos de config sin uso

2. **Empty directories**:
   - Directorios sin archivos (excepto `__init__.py`)
   - Directorios de packages sin `__init__.py`

3. **Naming conventions**:
   - Archivos que no siguen kebab-case (docs) o snake_case (python)
   - Directorios que no siguen convenciones

4. **Structure validation**:
   - Verificar que `apps/` solo contiene research apps
   - Verificar que `packages/` solo contiene packages Python
   - Verificar que `tools/` solo contiene scripts operacionales
   - Verificar que `docs/` solo contiene documentación

5. **Dependency validation**:
   - Detectar imports a paths que no existen
   - Detectar requirements duplicados en múltiples requirements.txt

6. **Old references**:
   - Buscar menciones a `nucleo-investigacion`
   - Buscar menciones a otras estructuras obsoletas

## 🛠️ Implementación

### Paso 1: Expandir cleanup_post_reorganization.py

```python
#!/usr/bin/env python3
"""
cleanup_post_reorganization.py - Validate monorepo health post-reorganization

Usage:
    python cleanup_post_reorganization.py                # Run all checks
    python cleanup_post_reorganization.py --check orphans # Run specific check
    python cleanup_post_reorganization.py --fix           # Auto-fix issues
    python cleanup_post_reorganization.py --report        # Generate report

Checks:
    - orphans: Find orphaned files without references
    - empty: Find empty directories
    - naming: Validate naming conventions
    - structure: Validate directory structure
    - deps: Validate dependencies
    - legacy: Find legacy/obsolete references
"""

import argparse
from pathlib import Path
from typing import List, Dict, Set
from dataclasses import dataclass
import re
import ast

@dataclass
class Issue:
    """Represents a structural issue"""
    category: str  # 'orphan', 'empty', 'naming', 'structure', 'deps', 'legacy'
    severity: str  # 'error', 'warning', 'info'
    path: Path
    description: str
    suggested_fix: str = None

class MonorepoValidator:
    """Validates monorepo structure and health"""

    # Patterns
    KEBAB_CASE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*\.(md|yaml|yml|json)$')
    SNAKE_CASE = re.compile(r'^[a-z0-9]+(_[a-z0-9]+)*\.py$')

    # Ignored paths
    IGNORED_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'venv',
                   '.obsidian', 'dist', 'build', '.pytest_cache', 'htmlcov'}

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.issues: List[Issue] = []
        self.file_index: Dict[Path, Set[Path]] = {}  # file -> files that reference it

    def _should_ignore(self, path: Path) -> bool:
        """Check if path should be ignored"""
        for parent in path.parents:
            if parent.name in self.IGNORED_DIRS:
                return True
        return False

    def check_orphans(self):
        """Find orphaned files without references"""
        print("🔍 Checking for orphaned files...")

        # Build reference graph
        all_files = [f for f in self.root.rglob('*') if f.is_file() and not self._should_ignore(f)]

        for file in all_files:
            if file.suffix in ['.py', '.md']:
                self._index_references(file)

        # Find orphans (no incoming references)
        for file, referrers in self.file_index.items():
            if not referrers and file.name not in ['__init__.py', 'README.md', 'LICENSE']:
                self.issues.append(Issue(
                    category='orphan',
                    severity='warning',
                    path=file,
                    description=f"Orphaned file with no incoming references",
                    suggested_fix="Add references or move to archive/"
                ))

    def _index_references(self, file: Path):
        """Index references from a file to other files"""
        try:
            content = file.read_text(encoding='utf-8')

            if file.suffix == '.py':
                # Find imports
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, (ast.Import, ast.ImportFrom)):
                        # Track import references
                        pass  # Implementation details

            elif file.suffix == '.md':
                # Find markdown links
                links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
                for _, target in links:
                    if not target.startswith('http'):
                        # Track link references
                        pass  # Implementation details

        except Exception:
            pass

    def check_empty_directories(self):
        """Find empty or near-empty directories"""
        print("🔍 Checking for empty directories...")

        for directory in self.root.rglob('*'):
            if directory.is_dir() and not self._should_ignore(directory):
                files = list(directory.iterdir())

                if not files:
                    self.issues.append(Issue(
                        category='empty',
                        severity='warning',
                        path=directory,
                        description="Empty directory",
                        suggested_fix="Remove directory or add README.md"
                    ))
                elif len(files) == 1 and files[0].name == '__init__.py':
                    # Python package with only __init__.py
                    self.issues.append(Issue(
                        category='empty',
                        severity='info',
                        path=directory,
                        description="Package with only __init__.py",
                        suggested_fix="Add module files or remove package"
                    ))

    def check_naming_conventions(self):
        """Validate naming conventions"""
        print("🔍 Checking naming conventions...")

        for file in self.root.rglob('*'):
            if file.is_file() and not self._should_ignore(file):

                # Python files should be snake_case
                if file.suffix == '.py' and not self.SNAKE_CASE.match(file.name):
                    if file.name not in ['setup.py', 'conftest.py', '__init__.py']:
                        self.issues.append(Issue(
                            category='naming',
                            severity='warning',
                            path=file,
                            description=f"Python file not in snake_case: {file.name}",
                            suggested_fix=f"Rename to {self._to_snake_case(file.stem)}.py"
                        ))

                # Docs should be kebab-case
                if file.suffix in ['.md', '.yaml', '.yml'] and not self.KEBAB_CASE.match(file.name):
                    # Exceptions
                    if file.name not in ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CHANGELOG.md']:
                        self.issues.append(Issue(
                            category='naming',
                            severity='info',
                            path=file,
                            description=f"Doc file not in kebab-case: {file.name}",
                            suggested_fix=f"Rename to {self._to_kebab_case(file.stem)}{file.suffix}"
                        ))

    def check_structure(self):
        """Validate directory structure"""
        print("🔍 Checking structure compliance...")

        # Check root structure
        expected_root = {'apps', 'docs', 'packages', 'tools', 'infrastructure', '_templates'}
        root_dirs = {d.name for d in self.root.iterdir() if d.is_dir() and not d.name.startswith('.')}

        unexpected = root_dirs - expected_root
        if unexpected:
            for dir_name in unexpected:
                self.issues.append(Issue(
                    category='structure',
                    severity='warning',
                    path=self.root / dir_name,
                    description=f"Unexpected root directory: {dir_name}",
                    suggested_fix="Move to appropriate location or document in ADR"
                ))

    def check_legacy_references(self):
        """Find legacy/obsolete references"""
        print("🔍 Checking for legacy references...")

        legacy_patterns = [
            r'nucleo-investigacion',
            r'nucleo_investigacion',
            # Add more legacy patterns
        ]

        for file in self.root.rglob('*'):
            if file.is_file() and not self._should_ignore(file):
                if file.suffix in ['.py', '.md', '.yaml', '.yml']:
                    try:
                        content = file.read_text(encoding='utf-8')
                        for pattern in legacy_patterns:
                            if re.search(pattern, content):
                                self.issues.append(Issue(
                                    category='legacy',
                                    severity='error',
                                    path=file,
                                    description=f"Legacy reference found: {pattern}",
                                    suggested_fix="Update to new structure/naming"
                                ))
                    except Exception:
                        pass

    def _to_snake_case(self, name: str) -> str:
        """Convert to snake_case"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _to_kebab_case(self, name: str) -> str:
        """Convert to kebab-case"""
        return self._to_snake_case(name).replace('_', '-')

    def generate_report(self) -> str:
        """Generate validation report"""
        report = []
        report.append("=" * 80)
        report.append("📋 MONOREPO VALIDATION REPORT")
        report.append("=" * 80)
        report.append(f"\n📁 Root: {self.root}")
        report.append(f"🔍 Total issues found: {len(self.issues)}\n")

        # Group by category and severity
        by_category = {}
        for issue in self.issues:
            key = (issue.category, issue.severity)
            if key not in by_category:
                by_category[key] = []
            by_category[key].append(issue)

        for (category, severity), issues in sorted(by_category.items()):
            icon = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}.get(severity, '•')
            report.append(f"\n{'─' * 80}")
            report.append(f"{icon} {category.upper()} [{severity.upper()}]: {len(issues)}")
            report.append(f"{'─' * 80}\n")

            for issue in issues[:10]:  # Show first 10
                rel_path = issue.path.relative_to(self.root)
                report.append(f"📄 {rel_path}")
                report.append(f"   {issue.description}")
                if issue.suggested_fix:
                    report.append(f"   💡 {issue.suggested_fix}")
                report.append("")

            if len(issues) > 10:
                report.append(f"   ... and {len(issues) - 10} more\n")

        report.append("=" * 80)
        return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Validate monorepo structure")
    parser.add_argument('--check', choices=['orphans', 'empty', 'naming', 'structure', 'deps', 'legacy'],
                       help='Run specific check')
    parser.add_argument('--report', action='store_true', help='Generate detailed report')
    parser.add_argument('--fix', action='store_true', help='Auto-fix issues where possible')

    args = parser.parse_args()

    root = Path.cwd()
    validator = MonorepoValidator(root)

    print(f"🚀 Monorepo Validator")
    print(f"📁 Workspace: {root}\n")

    # Run checks
    if args.check:
        getattr(validator, f'check_{args.check}')()
    else:
        validator.check_legacy_references()  # High priority
        validator.check_empty_directories()
        validator.check_naming_conventions()
        validator.check_structure()
        # validator.check_orphans()  # Can be slow

    # Results
    print(f"\n{'=' * 80}")
    if not validator.issues:
        print("✅ All checks passed!")
    else:
        print(f"⚠️  Found {len(validator.issues)} issues")
    print(f"{'=' * 80}\n")

    if args.report:
        report = validator.generate_report()
        print(report)

        report_file = root / 'docs' / '_meta' / 'validation-report.txt'
        report_file.write_text(report, encoding='utf-8')
        print(f"\n💾 Report saved to: {report_file}")

    return 1 if validator.issues else 0

if __name__ == '__main__':
    exit(main())
```

## ✅ Criterios de Aceptación

1. ✅ **Script funcional**:
   - Ejecuta sin errores
   - Encuentra issues conocidos (legacy refs, naming, etc.)

2. ✅ **Checks implementados**:
   - ✅ Legacy references
   - ✅ Empty directories
   - ✅ Naming conventions
   - ✅ Structure validation
   - ⚠️ Orphan detection (opcional, puede ser lento)
   - ⚠️ Dependency validation (opcional)

3. ✅ **Report generado**:
   - Output legible en terminal
   - Report guardado en `docs/_meta/validation-report.txt`

4. ✅ **Performance aceptable**:
   - Ejecuta en <30 segundos para monorepo completo

## 🧪 Testing

```powershell
# Ejecutar todos los checks
python tools/maintenance/cleanup_post_reorganization.py --report

# Check específico
python tools/maintenance/cleanup_post_reorganization.py --check legacy

# Ver report
cat docs/_meta/validation-report.txt
```

## 📚 Referencias

- [ISSUE-001](ISSUE-001-fix-nucleo-refs.md): Fix legacy references
- [ISSUE-002](ISSUE-002-move-root-docs.md): Structure organization

---

**Estado**: 🔴 OPEN
**Estimación**: 2-3 horas
**Bloqueadores**: Ninguno
**Dependencias**: Se beneficia de ISSUE-001 y ISSUE-002 completados
