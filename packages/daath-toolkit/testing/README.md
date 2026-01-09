# Test Suite - DAATH Toolkit

## Overview

Suite de tests para `daath-toolkit` con cobertura para validators y capture modules.

## Cobertura Actual

- **Cobertura Total**: 68%
- **capture.chatlog_capture**: 77% (141 statements, 32 miss)
- **validators.validate_research**: 56% (111 statements, 49 miss)

## Ejecutar Tests

```bash
# Activar entorno virtual
.venv\Scripts\activate

# Ejecutar todos los tests (excepto vector_store que requiere dependencias AI)
python -m pytest packages/daath-toolkit/testing/ --ignore=packages/daath-toolkit/testing/test_vector_store.py -v

# Con cobertura
python -m pytest packages/daath-toolkit/testing/ --ignore=packages/daath-toolkit/testing/test_vector_store.py --cov=capture --cov=validators --cov-report=html

# Ver reporte HTML
start htmlcov/index.html
```

## Estructura de Tests

```
testing/
├── conftest.py                    # Fixtures compartidas
├── test_validate_research.py      # 10 tests (100% passing)
├── test_chatlog_capture.py        # 11 tests (100% passing)
└── test_vector_store.py           # 14 tests (requiere pinecone/openai)
```

## Fixtures Disponibles

### Research Structure Fixtures
- `temp_research_dir`: Directorio temporal para testing
- `valid_research_structure`: Estructura completa válida
- `invalid_research_structure`: Estructura inválida (sin PROPOSITO.md)
- `valid_proposito_content`: PROPOSITO.md con YAML válido
- `invalid_proposito_content`: PROPOSITO.md con campos faltantes
- `proposito_without_yaml`: PROPOSITO.md sin frontmatter

### Chatlog Fixtures
- `temp_output_dir`: Directorio de output temporal
- `sample_chatlog_metadata`: Metadata de ejemplo

### Mock Fixtures (para vector_store)
- `mock_pinecone_client`: Mock de Pinecone API
- `mock_openai_client`: Mock de OpenAI API

## Tests por Módulo

### test_validate_research.py (10 tests)

✅ `test_valid_research_passes_validation` - Estructura válida debe pasar
✅ `test_missing_proposito_fails` - Sin PROPOSITO.md debe fallar
✅ `test_proposito_with_missing_fields` - Campos faltantes debe fallar
✅ `test_proposito_without_yaml_generates_warning` - Sin YAML genera warning
✅ `test_invalid_status_generates_warning` - Status inválido genera warning
✅ `test_valid_folders_accepted` - Carpetas válidas aceptadas
✅ `test_info_messages_generated_for_valid_fields` - Info generado para campos válidos
✅ `test_yaml_parsing_error_detected` - YAML malformado detectado
✅ `test_empty_research_directory` - Directorio vacío falla
✅ `test_required_fields_all_validated` - Todos los campos requeridos validados

### test_chatlog_capture.py (11 tests)

✅ `test_initialization_creates_directories` - Inicialización crea directorios
✅ `test_start_instance_creates_metadata` - Start crea metadata.yaml
✅ `test_record_message_writes_to_transcript` - Mensajes escritos a transcript
✅ `test_record_message_separates_by_rostro` - Mensajes separados por rostro
✅ `test_record_checkpoint_adds_to_metadata` - Checkpoints agregados a metadata
✅ `test_record_potential_lesson_adds_to_metadata` - Lessons agregados a metadata
✅ `test_finalize_instance_updates_metadata` - Finalize actualiza metadata
✅ `test_multiple_messages_maintain_order` - Orden cronológico mantenido
✅ `test_empty_prompts_dict_handled` - Dict vacío manejado
✅ `test_git_metadata_stored_when_provided` - Git metadata almacenado
✅ `test_invalid_rostro_handled_gracefully` - Rostro conocido funciona

### test_vector_store.py (14 tests - no ejecutados)

⚠️ Requiere instalación de dependencias opcionales:
```bash
pip install pinecone-client openai
```

Los tests están preparados con mocks completos para:
- Inicialización de índice Pinecone
- Generación de embeddings con OpenAI
- Upsert de artifacts
- Búsqueda en domains e instances
- Namespaces management
- Metadata filtering
- Deletion de artifacts
- Stats retrieval

## Mejoras Futuras

### Para alcanzar 80%+ de cobertura:

**validate_research.py (56% → 80%)**:
- Agregar tests para `_check_folders()` con carpetas inválidas
- Agregar tests para `_check_content()` con contenido vacío
- Agregar tests para warnings adicionales

**chatlog_capture.py (77% → 85%)**:
- Agregar tests para métodos de escritura (`_write_metadata`, `_init_full_transcript`, `_init_by_rostro_files`)
- Agregar tests para output tracking (`add_output_produced`)
- Agregar tests para git commit tracking al finalizar
- Agregar tests para rollback info

## Dependencias de Testing

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "isort>=5.12.0",
    "flake8>=6.0.0"
]
```

## CI/CD Integration

Para integrar en GitHub Actions:

```yaml
- name: Run tests
  run: |
    pip install -e ".[dev]"
    pytest packages/daath-toolkit/testing/ --ignore=packages/daath-toolkit/testing/test_vector_store.py --cov --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

## Notas

- Los tests de `vector_store` están completos pero requieren dependencias AI opcionales
- Se usan mocks para evitar llamadas reales a APIs externas (Pinecone, OpenAI)
- Todos los tests usan fixtures con datos temporales (auto-cleanup)
- La cobertura HTML se genera en `htmlcov/` para análisis detallado
