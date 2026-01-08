"""
Validador de Estructura de Investigación

Valida que una investigación en apps/ siga los principios DAATH-ZEN:
- PROPOSITO.md existe y tiene metadata válida
- Solo existen carpetas con contenido
- Estructura sigue convenciones
"""

import sys
from pathlib import Path
import yaml
import argparse


class ResearchValidator:
    """Valida estructura de investigaciones DAATH-ZEN"""

    VALID_FOLDERS = {
        '0-inbox', '1-literature', '2-atomic', '3-workbook',
        '4-dataset', '5-outputs', '_daath'
    }

    def __init__(self, research_path: Path):
        self.path = research_path
        self.errors = []
        self.warnings = []
        self.info = []

    def validate(self) -> bool:
        """Ejecuta todas las validaciones"""
        self._check_proposito()
        self._check_folders()
        self._check_content()

        return len(self.errors) == 0

    def _check_proposito(self):
        """Valida PROPOSITO.md"""
        proposito_path = self.path / 'PROPOSITO.md'

        if not proposito_path.exists():
            self.errors.append("❌ PROPOSITO.md no existe")
            return

        content = proposito_path.read_text(encoding='utf-8')

        # Buscar bloque YAML (puede estar entre ```yaml o directamente con ---)
        yaml_content = None

        if '```yaml' in content:
            # Formato con ```yaml
            yaml_start = content.find('```yaml') + 7
            yaml_end = content.find('```', yaml_start)
            if yaml_end > yaml_start:
                yaml_str = content[yaml_start:yaml_end].strip()
                # Limpiar --- si están presentes
                yaml_str = yaml_str.replace('---', '').strip()
                yaml_content = yaml_str
        elif content.strip().startswith('---'):
            # Formato directo con ---
            yaml_end = content.find('---', 3)
            if yaml_end > 0:
                yaml_content = content[3:yaml_end].strip()

        if yaml_content:
            try:
                metadata = yaml.safe_load(yaml_content)

                # Validar campos requeridos
                required = ['id', 'version', 'created', 'status', 'purpose', 'initiated_by']
                for field in required:
                    if field not in metadata:
                        self.errors.append(f"❌ PROPOSITO.md falta campo: {field}")
                    else:
                        value = str(metadata[field])[:50]  # Truncar para display
                        self.info.append(f"✓ {field}: {value}")

                # Validar status
                valid_statuses = ['inception', 'active', 'synthesis', 'completed', 'archived']
                if metadata.get('status') not in valid_statuses:
                    self.warnings.append(f"⚠️ Status '{metadata.get('status')}' no es estándar")

            except Exception as e:
                self.errors.append(f"❌ Error parseando YAML: {e}")
        else:
            self.warnings.append("⚠️ PROPOSITO.md no tiene YAML frontmatter válido")

    def _check_folders(self):
        """Valida estructura de carpetas"""
        folders = [d for d in self.path.iterdir() if d.is_dir()]

        for folder in folders:
            folder_name = folder.name

            # Ignorar carpetas del sistema
            if folder_name.startswith('.'):
                continue

            # Validar nombre
            if folder_name not in self.VALID_FOLDERS:
                self.warnings.append(f"⚠️ Carpeta no estándar: {folder_name}")
            else:
                self.info.append(f"✓ Carpeta válida: {folder_name}")

    def _check_content(self):
        """Verifica principio: solo carpetas con contenido"""
        for folder_name in self.VALID_FOLDERS:
            folder = self.path / folder_name

            if folder.exists():
                files = list(folder.rglob('*'))
                actual_files = [f for f in files if f.is_file() and not f.name.startswith('.')]

                if len(actual_files) == 0:
                    self.warnings.append(f"⚠️ Carpeta vacía: {folder_name}/")
                else:
                    self.info.append(f"✓ {folder_name}/ tiene {len(actual_files)} archivos")

    def print_report(self):
        """Imprime reporte de validación"""
        print(f"\n{'='*60}")
        print(f"Validación: {self.path.name}")
        print(f"{'='*60}\n")

        if self.errors:
            print("🔴 ERRORES:")
            for error in self.errors:
                print(f"  {error}")
            print()

        if self.warnings:
            print("🟡 ADVERTENCIAS:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()

        if self.info:
            print("ℹ️ INFORMACIÓN:")
            for info in self.info:
                print(f"  {info}")
            print()

        # Resumen
        status = "✅ VÁLIDO" if len(self.errors) == 0 else "❌ INVÁLIDO"
        print(f"{'='*60}")
        print(f"Estado: {status}")
        print(f"Errores: {len(self.errors)} | Advertencias: {len(self.warnings)}")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Valida estructura de investigaciones DAATH-ZEN"
    )
    parser.add_argument(
        'research_path',
        type=str,
        help='Ruta a la investigación (ej: apps/01-mi-investigacion)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Modo estricto: warnings también fallan'
    )

    args = parser.parse_args()

    research_path = Path(args.research_path)

    if not research_path.exists():
        print(f"❌ Error: Ruta no existe: {research_path}")
        sys.exit(1)

    if not research_path.is_dir():
        print(f"❌ Error: No es un directorio: {research_path}")
        sys.exit(1)

    # Validar
    validator = ResearchValidator(research_path)
    is_valid = validator.validate()
    validator.print_report()

    # Exit code
    if args.strict and len(validator.warnings) > 0:
        sys.exit(1)

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
