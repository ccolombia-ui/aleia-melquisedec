"""
Script de Limpieza Post-Reorganización

Valida salud del monorepo post-reorganización, detectando:
- Archivos huérfanos sin referencias
- Symlinks rotos
- Imports Python no utilizados
- Archivos temporales obsoletos

Clasificación por severidad:
- CRITICAL: Rompe funcionalidad (symlinks rotos, imports fallidos)
- MODERATE: Desorden estructural (archivos huérfanos, temp files)
- MINOR: Optimizaciones (__pycache__, logs antiguos)

Usage:
    # Dry-run (default) - muestra qué se encontró
    python cleanup_post_reorganization.py --all

    # Execute cleanup - SOLO para MINOR severity
    python cleanup_post_reorganization.py --all --execute

    # Specific checks
    python cleanup_post_reorganization.py --orphans --temp-files
    python cleanup_post_reorganization.py --broken-symlinks
"""

import sys
import shutil
import re
from pathlib import Path
import argparse
from typing import List, Dict, Set
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Issue:
    """Representa un problema estructural detectado"""
    category: str  # 'orphan', 'symlink', 'temp', 'pycache'
    severity: str  # 'CRITICAL', 'MODERATE', 'MINOR'
    path: Path
    description: str
    suggested_fix: str = None


class CleanupValidator:
    """Valida y limpia monorepo post-reorganización"""

    IGNORED_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'venv',
                   '.obsidian', 'dist', 'build', '.pytest_cache', 'htmlcov',
                   '.smart-env'}

    TEMP_FILE_PATTERNS = [
        r'\.gitpush.*\.json$',
        r'\.gitpush-.*\.yml$',
        r'.*~$',  # backup files
        r'\.DS_Store$',  # macOS
        r'Thumbs\.db$',  # Windows
    ]

    # Legacy references que no deberían existir
    LEGACY_PATTERNS = [
        (r'nucleo-investigacion', 'Use daath-toolkit instead'),
        (r'nucleo_investigacion', 'Use daath_toolkit instead'),
        (r'from\s+nucleo_investigacion', 'Update import to daath_toolkit'),
    ]

    # Naming conventions
    VALID_FOLDER_PREFIXES = [
        r'^\d{2}-',  # numbered folders (01-foundation, etc)
        r'^_',  # private/meta folders (_daath, _templates)
        r'^[a-z][a-z0-9-]*$',  # kebab-case (packages, tools, docs)
    ]

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.issues: List[Issue] = []

    def _should_ignore(self, path: Path) -> bool:
        """Verifica si la ruta debe ser ignorada"""
        for parent in [path] + list(path.parents):
            if parent.name in self.IGNORED_DIRS:
                return True
        return False

    def check_broken_symlinks(self):
        """Detecta symlinks rotos"""
        print("🔍 Checking for broken symlinks...")
        count = 0

        for path in self.root.rglob('*'):
            if self._should_ignore(path):
                continue

            if path.is_symlink():
                try:
                    path.resolve(strict=True)
                except (FileNotFoundError, RuntimeError):
                    self.issues.append(Issue(
                        category='symlink',
                        severity='CRITICAL',
                        path=path,
                        description="Broken symlink - target does not exist",
                        suggested_fix="Remove symlink or fix target"
                    ))
                    count += 1

        print(f"  Found {count} broken symlinks")

    def check_temp_files(self):
        """Detecta archivos temporales obsoletos"""
        print("🔍 Checking for temporary files...")
        count = 0

        for path in self.root.rglob('*'):
            if self._should_ignore(path) or not path.is_file():
                continue

            for pattern in self.TEMP_FILE_PATTERNS:
                if re.search(pattern, path.name):
                    self.issues.append(Issue(
                        category='temp',
                        severity='MINOR',
                        path=path,
                        description=f"Temporary file (pattern: {pattern})",
                        suggested_fix="Remove if no longer needed"
                    ))
                    count += 1
                    break

        print(f"  Found {count} temporary files")

    def check_orphan_files(self):
        """Detecta archivos Python huérfanos (sin imports)"""
        print("🔍 Checking for orphaned Python files...")

        # Construir grafo de imports
        py_files = [f for f in self.root.rglob('*.py')
                   if f.is_file() and not self._should_ignore(f)]

        import_graph = defaultdict(set)

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding='utf-8')
                # Detectar imports relativos y absolutos
                import_matches = re.findall(
                    r'from\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s+import|'
                    r'import\s+([a-zA-Z_][a-zA-Z0-9_.]*)',
                    content
                )
                for match in import_matches:
                    module = match[0] or match[1]
                    # Buscar archivo correspondiente
                    for target in py_files:
                        if module.replace('.', '/') in str(target):
                            import_graph[target].add(py_file)
            except Exception:
                pass

        # Archivos sin referencias entrantes (excepto __init__.py y scripts de entry)
        orphans = []
        for py_file in py_files:
            if py_file.name in ['__init__.py', '__main__.py', 'setup.py']:
                continue
            # Scripts en tools/ son entry points
            if 'tools/' in str(py_file.relative_to(self.root)):
                continue
            # Server.py es entry point
            if py_file.name == 'server.py':
                continue

            if py_file not in import_graph or len(import_graph[py_file]) == 0:
                self.issues.append(Issue(
                    category='orphan',
                    severity='MODERATE',
                    path=py_file,
                    description="Orphaned Python file - no imports from other files",
                    suggested_fix="Add imports or archive if deprecated"
                ))
                orphans.append(py_file)

        print(f"  Found {len(orphans)} orphaned Python files")

    def check_pycache(self):
        """Detecta directorios __pycache__"""
        print("🔍 Checking for __pycache__ directories...")
        pycache_dirs = [d for d in self.root.rglob('__pycache__')
                       if d.is_dir()]

        for pycache in pycache_dirs:
            self.issues.append(Issue(
                category='pycache',
                severity='MINOR',
                path=pycache,
                description="Python cache directory",
                suggested_fix="Remove (will be regenerated)"
            ))

        print(f"  Found {len(pycache_dirs)} __pycache__ directories")

    def check_empty_directories(self):
        """Detecta directorios vacíos (excepto los deliberadamente vacíos)"""
        print("🔍 Checking for empty directories...")
        count = 0

        for path in self.root.rglob('*'):
            if not path.is_dir() or self._should_ignore(path):
                continue

            # Verificar si está vacío (sin archivos ni subdirectorios no-ignorados)
            try:
                contents = list(path.iterdir())
                if not contents:
                    # Completamente vacío
                    self.issues.append(Issue(
                        category='empty_dir',
                        severity='MODERATE',
                        path=path,
                        description="Empty directory - no files or subdirectories",
                        suggested_fix="Remove if not needed, or add README.md explaining purpose"
                    ))
                    count += 1
                elif all(self._should_ignore(item) for item in contents):
                    # Solo contiene archivos ignorados (.git, etc)
                    self.issues.append(Issue(
                        category='empty_dir',
                        severity='MODERATE',
                        path=path,
                        description="Directory with only ignored files",
                        suggested_fix="Add content or remove directory"
                    ))
                    count += 1
            except PermissionError:
                pass

        print(f"  Found {count} empty directories")

    def check_naming_violations(self):
        """Detecta violaciones de convenciones de nombrado"""
        print("🔍 Checking for naming violations...")
        count = 0

        # Verificar carpetas de primer nivel (excepto .git, etc)
        for path in self.root.iterdir():
            if not path.is_dir() or self._should_ignore(path):
                continue

            folder_name = path.name

            # Verificar contra patrones válidos
            valid = False
            for pattern in self.VALID_FOLDER_PREFIXES:
                if re.match(pattern, folder_name):
                    valid = True
                    break

            if not valid:
                self.issues.append(Issue(
                    category='naming',
                    severity='MODERATE',
                    path=path,
                    description=f"Naming violation: '{folder_name}' doesn't follow conventions",
                    suggested_fix="Rename to kebab-case (e.g., my-folder) or numbered (01-folder)"
                ))
                count += 1

        print(f"  Found {count} naming violations")

    def check_legacy_references(self):
        """Detecta referencias a código legacy que ya no existe"""
        print("🔍 Checking for legacy references...")
        count = 0

        # Buscar en archivos de texto
        text_files = []
        for ext in ['.py', '.md', '.yml', '.yaml', '.json', '.sh', '.ps1', '.txt']:
            text_files.extend(self.root.rglob(f'*{ext}'))

        for file_path in text_files:
            if self._should_ignore(file_path) or not file_path.is_file():
                continue

            try:
                content = file_path.read_text(encoding='utf-8')

                for pattern, fix in self.LEGACY_PATTERNS:
                    matches = list(re.finditer(pattern, content, re.IGNORECASE))
                    if matches:
                        self.issues.append(Issue(
                            category='legacy',
                            severity='MODERATE',
                            path=file_path,
                            description=f"Legacy reference found: '{pattern}' ({len(matches)} occurrences)",
                            suggested_fix=fix
                        ))
                        count += 1
                        break  # Solo reportar una vez por archivo
            except (UnicodeDecodeError, PermissionError):
                pass

        print(f"  Found {count} files with legacy references")

    def check_broken_imports(self):
        """Detecta imports Python que fallan"""
        print("🔍 Checking for broken imports...")
        count = 0

        py_files = [f for f in self.root.rglob('*.py')
                   if f.is_file() and not self._should_ignore(f)]

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding='utf-8')

                # Extraer imports
                import_lines = []
                for line in content.split('\n'):
                    line = line.strip()
                    if line.startswith('import ') or line.startswith('from '):
                        import_lines.append(line)

                # Verificar si los imports son válidos (heurística simple)
                for import_line in import_lines:
                    # Detectar imports relativos que podrían estar rotos
                    if 'from . import' in import_line or 'from .. import' in import_line:
                        # Verificar estructura de carpetas
                        parent_dir = py_file.parent
                        if not (parent_dir / '__init__.py').exists():
                            self.issues.append(Issue(
                                category='broken_import',
                                severity='CRITICAL',
                                path=py_file,
                                description=f"Relative import in non-package: '{import_line}'",
                                suggested_fix="Add __init__.py or use absolute import"
                            ))
                            count += 1
                            break

                    # Detectar imports de módulos que ya no existen
                    if 'nucleo_investigacion' in import_line:
                        self.issues.append(Issue(
                            category='broken_import',
                            severity='CRITICAL',
                            path=py_file,
                            description=f"Import from deprecated module: '{import_line}'",
                            suggested_fix="Update to import from daath_toolkit"
                        ))
                        count += 1
                        break

            except (UnicodeDecodeError, PermissionError):
                pass

        print(f"  Found {count} files with broken imports")

    def generate_report(self) -> str:
        """Genera reporte de issues encontrados"""
        if not self.issues:
            return "✅ No issues found. Monorepo is clean!\n"

        # Agrupar por severidad
        by_severity = defaultdict(list)
        for issue in self.issues:
            by_severity[issue.severity].append(issue)

        report = []
        report.append(f"\n{'='*70}")
        report.append("CLEANUP REPORT - Post-Reorganization Validation")
        report.append(f"{'='*70}\n")

        report.append(f"Total issues found: {len(self.issues)}\n")

        for severity in ['CRITICAL', 'MODERATE', 'MINOR']:
            issues_list = by_severity.get(severity, [])
            if not issues_list:
                continue

            report.append(f"\n{severity} ({len(issues_list)} issues):")
            report.append("-" * 70)

            for issue in issues_list:
                rel_path = issue.path.relative_to(self.root)
                report.append(f"\n  [{issue.category.upper()}] {rel_path}")
                report.append(f"  Description: {issue.description}")
                if issue.suggested_fix:
                    report.append(f"  Fix: {issue.suggested_fix}")

        report.append(f"\n{'='*70}\n")

        return "\n".join(report)

    def execute_cleanup(self, categories: Set[str] = None):
        """
        Ejecuta limpieza para las categorías especificadas.

        IMPORTANTE: Solo se ejecuta automáticamente para MINOR severity.
        CRITICAL/MODERATE requieren revisión manual.
        """
        if categories is None:
            categories = {'temp', 'pycache'}  # Default: solo minor severity

        removed_count = 0

        for issue in self.issues:
            # Prevenir eliminación de CRITICAL/MODERATE sin confirmación explícita
            if issue.severity in ['CRITICAL', 'MODERATE'] and issue.category not in ['empty_dir']:
                continue

            if issue.category not in categories:
                continue

            try:
                if issue.path.is_dir():
                    shutil.rmtree(issue.path)
                    print(f"✅ Removed: {issue.path.relative_to(self.root)}")
                elif issue.path.is_file() or issue.path.is_symlink():
                    issue.path.unlink()
                    print(f"✅ Removed: {issue.path.relative_to(self.root)}")
                removed_count += 1
            except Exception as e:
                print(f"❌ Failed to remove {issue.path}: {e}")

        print(f"\n✅ Cleaned {removed_count} items")


def main():
    parser = argparse.ArgumentParser(
        description="Cleanup and validation post-reorganization - DAATH-ZEN MELQUISEDEC",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all checks (dry-run)
  python cleanup_post_reorganization.py --all

  # Run all checks and execute cleanup (ONLY MINOR severity)
  python cleanup_post_reorganization.py --all --execute

  # Check specific issues
  python cleanup_post_reorganization.py --orphans --broken-symlinks

  # Check and clean temp files
  python cleanup_post_reorganization.py --temp-files --execute
        """
    )

    # Flags de checks
    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all checks'
    )
    parser.add_argument(
        '--broken-symlinks',
        action='store_true',
        help='Check for broken symlinks'
    )
    parser.add_argument(
        '--orphans',
        action='store_true',
        help='Check for orphaned Python files'
    )
    parser.add_argument(
        '--temp-files',
        action='store_true',
        help='Check for temporary files'
    )
    parser.add_argument(
        '--pycache',
        action='store_true',
        help='Check for __pycache__ directories'
    )
    parser.add_argument(
        '--empty-dirs',
        action='store_true',
        help='Check for empty directories'
    )
    parser.add_argument(
        '--naming',
        action='store_true',
        help='Check for naming convention violations'
    )
    parser.add_argument(
        '--legacy-refs',
        action='store_true',
        help='Check for legacy references (nucleo-investigacion, etc)'
    )
    parser.add_argument(
        '--broken-imports',
        action='store_true',
        help='Check for broken Python imports'
    )

    # Execution flag
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute cleanup (default: dry-run). Only removes MINOR severity items.'
    )

    args = parser.parse_args()

    # Si no se especifica nada, mostrar help
    if not any([args.all, args.broken_symlinks, args.orphans,
               args.temp_files, args.pycache, args.empty_dirs,
               args.naming, args.legacy_refs, args.broken_imports]):
        parser.print_help()
        return 1

    # Inicializar validator
    root = Path(__file__).resolve().parent.parent.parent
    validator = CleanupValidator(root)

    print(f"\n{'='*70}")
    print("CLEANUP POST-REORGANIZATION VALIDATOR")
    print(f"Root: {root}")
    print(f"Mode: {'EXECUTE' if args.execute else 'DRY-RUN'}")
    print(f"{'='*70}\n")

    # Ejecutar checks
    if args.all or args.broken_symlinks:
        validator.check_broken_symlinks()

    if args.all or args.orphans:
        validator.check_orphan_files()

    if args.all or args.temp_files:
        validator.check_temp_files()

    if args.all or args.pycache:
        validator.check_pycache()

    if args.all or args.empty_dirs:
        validator.check_empty_directories()

    if args.all or args.naming:
        validator.check_naming_violations()

    if args.all or args.legacy_refs:
        validator.check_legacy_references()

    if args.all or args.broken_imports:
        validator.check_broken_imports()

    # Generar reporte
    report = validator.generate_report()
    print(report)

    # Ejecutar cleanup si se solicitó
    if args.execute:
        # Solo limpiar MINOR severity (temp, pycache)
        print("\n⚠️ EXECUTING CLEANUP (MINOR severity only)...\n")
        validator.execute_cleanup(categories={'temp', 'pycache'})
    else:
        print("💡 This was a dry-run. Use --execute to actually remove files.\n")
        print("⚠️ NOTE: --execute only removes MINOR severity items (temp files, pycache)")
        print("   CRITICAL/MODERATE issues must be reviewed and fixed manually.\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
