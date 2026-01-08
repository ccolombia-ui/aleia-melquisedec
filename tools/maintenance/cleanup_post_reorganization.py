"""
Script de Limpieza Post-Reorganización

Elimina archivos temporales y apps de prueba después de validar
la reorganización del monorepo.
"""

import sys
import shutil
from pathlib import Path
import argparse


def clean_test_app(base_path: Path = None, dry_run: bool = True):
    """
    Elimina la app de prueba 01-test-reorganizacion
    
    Args:
        base_path: Ruta base del proyecto
        dry_run: Si True, solo muestra qué se eliminaría
    """
    if base_path is None:
        base_path = Path(__file__).resolve().parent.parent.parent
    
    test_app = base_path / 'apps' / '01-test-reorganizacion'
    
    print(f"\n{'='*60}")
    print("Limpieza Post-Reorganización")
    print(f"{'='*60}\n")
    
    if not test_app.exists():
        print("✅ No hay apps de prueba para eliminar")
        return
    
    # Listar contenido
    files = list(test_app.rglob('*'))
    file_count = len([f for f in files if f.is_file()])
    
    print(f"📁 App encontrada: {test_app.name}")
    print(f"📊 Archivos: {file_count}")
    print(f"📦 Tamaño: {sum(f.stat().st_size for f in files if f.is_file()) / 1024:.2f} KB")
    
    if dry_run:
        print(f"\n⚠️ MODO DRY-RUN: No se eliminará nada")
        print(f"Ejecuta con --execute para eliminar realmente")
    else:
        print(f"\n🗑️ Eliminando...")
        shutil.rmtree(test_app)
        print(f"✅ Eliminado: {test_app}")
    
    print(f"\n{'='*60}\n")


def clean_pycache(base_path: Path = None, dry_run: bool = True):
    """Elimina directorios __pycache__"""
    if base_path is None:
        base_path = Path(__file__).resolve().parent.parent.parent
    
    pycache_dirs = list(base_path.rglob('__pycache__'))
    
    if not pycache_dirs:
        print("✅ No hay directorios __pycache__ para eliminar")
        return
    
    print(f"📁 Encontrados {len(pycache_dirs)} directorios __pycache__")
    
    if dry_run:
        print(f"⚠️ MODO DRY-RUN")
        for d in pycache_dirs:
            print(f"  - {d}")
    else:
        for d in pycache_dirs:
            shutil.rmtree(d)
            print(f"✅ Eliminado: {d}")


def generate_summary(base_path: Path = None):
    """Genera resumen del estado final"""
    if base_path is None:
        base_path = Path(__file__).resolve().parent.parent.parent
    
    print(f"\n{'='*60}")
    print("Resumen del Monorepo")
    print(f"{'='*60}\n")
    
    # Contar investigaciones
    apps_path = base_path / 'apps'
    apps = [d for d in apps_path.iterdir() if d.is_dir() and d.name[0].isdigit()]
    
    print(f"📊 Estadísticas:")
    print(f"  - Investigaciones activas: {len(apps)}")
    
    if apps:
        print(f"\n📁 Investigaciones:")
        for app in sorted(apps):
            proposito = app / 'PROPOSITO.md'
            if proposito.exists():
                # Leer status del PROPOSITO
                content = proposito.read_text(encoding='utf-8')
                if 'status:' in content:
                    status_line = [l for l in content.split('\n') if 'status:' in l][0]
                    status = status_line.split(':')[1].strip().split()[0]
                    print(f"  - {app.name}: {status}")
                else:
                    print(f"  - {app.name}: unknown")
    
    # Contar archivos en packages
    packages_path = base_path / 'packages'
    packages = [d for d in packages_path.iterdir() if d.is_dir()]
    
    print(f"\n📦 Packages:")
    for pkg in sorted(packages):
        py_files = list(pkg.rglob('*.py'))
        print(f"  - {pkg.name}: {len(py_files)} archivos Python")
    
    # Documentación
    docs_path = base_path / 'docs'
    md_files = list(docs_path.rglob('*.md'))
    
    print(f"\n📚 Documentación:")
    print(f"  - {len(md_files)} archivos markdown en docs/")
    
    # Root docs
    root_docs = ['README.md', 'ARQUITECTURA_MONOREPO.md', 'REORGANIZACION_COMPLETA.md', 
                 'ESTRUCTURA_VISUAL.md', 'QUICK_REFERENCE.md', 'CONTRIBUTING.md']
    existing_docs = [d for d in root_docs if (base_path / d).exists()]
    print(f"  - {len(existing_docs)} documentos principales en raíz")
    
    print(f"\n{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Limpieza post-reorganización del monorepo DAATH-ZEN"
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Ejecutar limpieza (sin esto, solo muestra qué se haría)'
    )
    parser.add_argument(
        '--clean-test-app',
        action='store_true',
        help='Limpiar app de prueba 01-test-reorganizacion'
    )
    parser.add_argument(
        '--clean-pycache',
        action='store_true',
        help='Limpiar directorios __pycache__'
    )
    parser.add_argument(
        '--summary',
        action='store_true',
        help='Mostrar resumen del estado final'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Ejecutar todas las limpiezas'
    )
    
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    # Si no se especifica nada, mostrar help
    if not (args.clean_test_app or args.clean_pycache or args.summary or args.all):
        parser.print_help()
        return
    
    # Ejecutar limpiezas
    if args.all or args.clean_test_app:
        clean_test_app(dry_run=dry_run)
    
    if args.all or args.clean_pycache:
        clean_pycache(dry_run=dry_run)
    
    if args.all or args.summary:
        generate_summary()
    
    if dry_run and (args.clean_test_app or args.clean_pycache or args.all):
        print("\n💡 Tip: Ejecuta con --execute para eliminar realmente los archivos\n")


if __name__ == '__main__':
    main()
