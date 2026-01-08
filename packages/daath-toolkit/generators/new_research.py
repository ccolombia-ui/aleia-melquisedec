"""
Generador de Nuevas Investigaciones

Crea una nueva investigación a partir del template 00-template
con personalización interactiva.
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime
import argparse


def generate_research(
    name: str,
    purpose: str = None,
    initiated_by: str = "MELQUISEDEC",
    base_path: Path = None
):
    """
    Genera una nueva investigación

    Args:
        name: Nombre de la investigación (ej: "knowledge-graph-analysis")
        purpose: Propósito breve de la investigación
        initiated_by: Rostro que inicia (MELQUISEDEC, HYPATIA, etc.)
        base_path: Path base del proyecto
    """
    if base_path is None:
        # Detectar root del proyecto (donde está apps/)
        current = Path(__file__).resolve()
        while current.parent != current:
            if (current / 'apps').exists():
                base_path = current
                break
            current = current.parent

        if base_path is None:
            print("❌ Error: No se pudo detectar la raíz del proyecto")
            sys.exit(1)

    # Paths
    apps_path = base_path / 'apps'
    template_path = apps_path / '00-template'

    # Encontrar siguiente número
    existing_apps = [d for d in apps_path.iterdir() if d.is_dir() and d.name.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))]
    next_number = len(existing_apps)  # 00-template no cuenta

    # Nombre con número
    app_id = f"{next_number:02d}-{name}"
    target_path = apps_path / app_id

    if target_path.exists():
        print(f"❌ Error: Ya existe: {target_path}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"Creando nueva investigación: {app_id}")
    print(f"{'='*60}\n")

    # Copiar template
    print(f"📂 Copiando template...")
    shutil.copytree(template_path, target_path)

    # Personalizar PROPOSITO.md
    print(f"✏️ Personalizando PROPOSITO.md...")
    proposito_path = target_path / 'PROPOSITO.md'
    content = proposito_path.read_text(encoding='utf-8')

    # Reemplazos
    replacements = {
        '[NOMBRE-INVESTIGACIÓN]': name.replace('-', ' ').title(),
        'app-[nombre-corto]': f"app-{name}",
        'YYYY-MM-DD': datetime.now().strftime('%Y-%m-%d'),
        'MELQUISEDEC"  # MELQUISEDEC': f'{initiated_by}"  # {initiated_by}'
    }

    if purpose:
        # Reemplazar el placeholder de purpose
        content = content.replace(
            '[Describir en 2-3 líneas qué problema resuelve esta investigación\n   y qué conocimiento busca generar]',
            purpose
        )

    for old, new in replacements.items():
        content = content.replace(old, new)

    proposito_path.write_text(content, encoding='utf-8')

    # Personalizar README.md
    readme_path = target_path / 'README.md'
    readme_content = readme_path.read_text(encoding='utf-8')
    readme_content = readme_content.replace('[NOMBRE-INVESTIGACIÓN]', name.replace('-', ' ').title())
    readme_path.write_text(readme_content, encoding='utf-8')

    # Crear 0-inbox por defecto
    inbox_path = target_path / '0-inbox'
    inbox_path.mkdir(exist_ok=True)

    inbox_readme = inbox_path / 'README.md'
    inbox_readme.write_text(f"""# Inbox - {name}

Ideas, issues y requests iniciales.

## Agregar Contenido

Crear archivos markdown aquí:
- `YYYY-MM-DD-idea-descriptiva.md` para ideas
- `issue-001-titulo.md` para issues
- `request-funcionalidad.md` para requests

""", encoding='utf-8')

    print(f"\n{'='*60}")
    print(f"✅ Investigación creada exitosamente!")
    print(f"{'='*60}\n")
    print(f"📍 Ubicación: {target_path}")
    print(f"\n📝 Próximos pasos:")
    print(f"  1. cd {target_path}")
    print(f"  2. code PROPOSITO.md  # Personalizar completamente")
    print(f"  3. Crear contenido en 0-inbox/")
    print(f"  4. Activar rostros según necesidad")
    print(f"\n")


def main():
    parser = argparse.ArgumentParser(
        description="Genera nueva investigación DAATH-ZEN desde template"
    )
    parser.add_argument(
        'name',
        type=str,
        help='Nombre de la investigación (ej: knowledge-graph-analysis)'
    )
    parser.add_argument(
        '--purpose',
        type=str,
        help='Propósito breve de la investigación'
    )
    parser.add_argument(
        '--initiated-by',
        type=str,
        default='MELQUISEDEC',
        choices=['MELQUISEDEC', 'HYPATIA', 'SALOMON', 'MORPHEUS', 'ALMA'],
        help='Rostro que inicia la investigación'
    )

    args = parser.parse_args()

    # Validar nombre
    if not args.name.replace('-', '').replace('_', '').isalnum():
        print("❌ Error: El nombre debe ser alfanumérico con guiones")
        sys.exit(1)

    generate_research(
        name=args.name,
        purpose=args.purpose,
        initiated_by=args.initiated_by
    )


if __name__ == '__main__':
    main()
