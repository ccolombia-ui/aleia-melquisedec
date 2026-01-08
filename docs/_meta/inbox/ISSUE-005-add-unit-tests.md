---
id: ISSUE-005
title: Add unit tests for capture and storage modules
type: testing
area: packages
priority: high
status: open
created: 2026-01-08
assignee: null
tags: [testing, quality, daath-toolkit]
related_issues: [ISSUE-004]
---

# ISSUE-005: Add unit tests for capture and storage modules

## 📌 Objetivo

Crear suite completa de unit tests para los módulos `capture/` y `storage/` en `packages/daath-toolkit/`, asegurando cobertura >80% y validando funcionalidad crítica.

## 📖 Contexto

Después de la reorganización, los módulos críticos `chatlog_capture.py` (588 líneas) y `vector_store.py` (510 líneas) no tienen tests automatizados.

**Riesgos sin tests**:
- Refactorings pueden introducir bugs silenciosos
- Difícil validar que imports/paths funcionan después de cambios
- No hay garantía de que API pública se mantiene estable
- Dificulta contribuciones (no hay safety net)

**Solución**: Implementar pytest tests con mocks para dependencias externas (Pinecone, OpenAI, filesystem).

## 💡 Solución Propuesta

### Estructura de tests:
```
packages/daath-toolkit/
└── tests/
    ├── __init__.py
    ├── conftest.py                # Fixtures compartidas
    ├── test_capture/
    │   ├── __init__.py
    │   ├── test_chatlog_capture.py
    │   └── test_integration.py
    ├── test_storage/
    │   ├── __init__.py
    │   ├── test_vector_store.py
    │   └── test_integration.py
    └── fixtures/
        ├── sample_chatlog.yaml
        └── sample_vectors.json
```

### Prioridades de testing:

#### 1. ChatlogCapture (capture/chatlog_capture.py)
**Funciones críticas a testear**:
- `__init__()`: Validación de domain/instance
- `save_conversation()`: Guardar conversación en estructura correcta
- `_parse_by_rostro()`: Separar mensajes por rostro
- `_generate_metadata()`: Generar metadata YAML correcta
- `_create_directory_structure()`: Crear estructura _daath/

**Casos de test**:
- ✅ Happy path: Crear chatlog completo con todos los rostros
- ✅ Edge case: Conversación sin algunos rostros (ej. sin Morpheus)
- ✅ Error handling: Domain/instance inválidos
- ✅ File operations: Verificar estructura de directorios creada
- ✅ YAML generation: Validar formato metadata.yaml

#### 2. DomainAwareVectorStore (storage/vector_store.py)
**Funciones críticas a testear**:
- `__init__()`: Conexión a Pinecone (mocked)
- `upsert_vectors()`: Insertar vectores con metadata correcta
- `query_similar()`: Query por similaridad
- `list_instances()`: Listar instances de un domain
- `_build_namespace()`: Construcción de namespace domain/instance
- `delete_instance()`: Eliminar instance completa

**Casos de test**:
- ✅ Happy path: CRUD completo de vectores
- ✅ Namespace handling: Verificar namespacing correcto
- ✅ Metadata filtering: Queries con filtros
- ✅ Error handling: Pinecone connection errors (mocked)
- ✅ Batch operations: Upsert de múltiples vectores

## 🛠️ Implementación

### Paso 1: Setup pytest structure

```powershell
cd packages/daath-toolkit
New-Item -ItemType Directory -Force -Path "tests/test_capture"
New-Item -ItemType Directory -Force -Path "tests/test_storage"
New-Item -ItemType Directory -Force -Path "tests/fixtures"
```

### Paso 2: Crear conftest.py con fixtures

```python
# tests/conftest.py
import pytest
from pathlib import Path
from unittest.mock import Mock, MagicMock
import tempfile
import shutil

@pytest.fixture
def temp_workspace():
    """Create temporary workspace directory"""
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_messages():
    """Sample conversation messages"""
    return [
        {"role": "user", "content": "¿Qué es autopoiesis?"},
        {"role": "assistant", "content": "[MELQUISEDEC] La autopoiesis es..."},
        {"role": "user", "content": "Dame un ejemplo"},
        {"role": "assistant", "content": "[HYPATIA] Un ejemplo claro es..."},
    ]

@pytest.fixture
def mock_pinecone():
    """Mock Pinecone client"""
    mock_client = MagicMock()
    mock_index = MagicMock()
    mock_client.Index.return_value = mock_index
    return mock_client, mock_index

@pytest.fixture
def sample_vectors():
    """Sample vector embeddings"""
    return [
        {"id": "vec-1", "values": [0.1] * 1536, "metadata": {"text": "test"}},
        {"id": "vec-2", "values": [0.2] * 1536, "metadata": {"text": "test2"}},
    ]
```

### Paso 3: Tests para ChatlogCapture

```python
# tests/test_capture/test_chatlog_capture.py
import pytest
from pathlib import Path
from daath_toolkit.capture import ChatlogCapture

class TestChatlogCapture:
    
    def test_init_valid(self, temp_workspace):
        """Test initialization with valid parameters"""
        capture = ChatlogCapture(
            domain="physics",
            instance="quantum",
            workspace_root=temp_workspace
        )
        assert capture.domain == "physics"
        assert capture.instance == "quantum"
    
    def test_init_invalid_domain(self, temp_workspace):
        """Test initialization with invalid domain"""
        with pytest.raises(ValueError, match="domain"):
            ChatlogCapture(domain="", instance="test", workspace_root=temp_workspace)
    
    def test_save_conversation_creates_structure(self, temp_workspace, sample_messages):
        """Test that save_conversation creates proper directory structure"""
        capture = ChatlogCapture("physics", "quantum", temp_workspace)
        capture.save_conversation(sample_messages)
        
        # Verify structure
        assert (temp_workspace / "_daath" / "chatlog").exists()
        assert (temp_workspace / "_daath" / "chatlog" / "by-rostro").exists()
        assert (temp_workspace / "_daath" / "chatlog" / "metadata.yaml").exists()
    
    def test_parse_by_rostro_separates_correctly(self, temp_workspace, sample_messages):
        """Test that messages are correctly separated by rostro"""
        capture = ChatlogCapture("physics", "quantum", temp_workspace)
        capture.save_conversation(sample_messages)
        
        # Check individual rostro files
        melquisedec_file = temp_workspace / "_daath" / "chatlog" / "by-rostro" / "01-melquisedec.md"
        hypatia_file = temp_workspace / "_daath" / "chatlog" / "by-rostro" / "02-hypatia.md"
        
        assert melquisedec_file.exists()
        assert hypatia_file.exists()
        
        # Verify content
        melquisedec_content = melquisedec_file.read_text()
        assert "La autopoiesis es" in melquisedec_content
        
        hypatia_content = hypatia_file.read_text()
        assert "Un ejemplo claro" in hypatia_content
    
    def test_metadata_yaml_format(self, temp_workspace, sample_messages):
        """Test that metadata.yaml has correct format"""
        import yaml
        
        capture = ChatlogCapture("physics", "quantum", temp_workspace)
        capture.save_conversation(sample_messages, metadata={"topic": "autopoiesis"})
        
        metadata_file = temp_workspace / "_daath" / "chatlog" / "metadata.yaml"
        metadata = yaml.safe_load(metadata_file.read_text())
        
        assert metadata["domain"] == "physics"
        assert metadata["instance"] == "quantum"
        assert metadata["topic"] == "autopoiesis"
        assert "created_at" in metadata
    
    def test_empty_conversation(self, temp_workspace):
        """Test handling of empty conversation"""
        capture = ChatlogCapture("physics", "quantum", temp_workspace)
        
        with pytest.raises(ValueError, match="empty"):
            capture.save_conversation([])
```

### Paso 4: Tests para DomainAwareVectorStore

```python
# tests/test_storage/test_vector_store.py
import pytest
from unittest.mock import patch, MagicMock
from daath_toolkit.storage import DomainAwareVectorStore

class TestDomainAwareVectorStore:
    
    @patch('daath_toolkit.storage.vector_store.pinecone')
    def test_init_connects_to_pinecone(self, mock_pinecone):
        """Test initialization connects to Pinecone"""
        store = DomainAwareVectorStore(domain="physics", api_key="test-key")
        
        mock_pinecone.init.assert_called_once()
        assert store.domain == "physics"
    
    @patch('daath_toolkit.storage.vector_store.pinecone')
    def test_build_namespace(self, mock_pinecone):
        """Test namespace building"""
        store = DomainAwareVectorStore(domain="physics", api_key="test-key")
        
        namespace = store._build_namespace("quantum")
        assert namespace == "physics/quantum"
    
    @patch('daath_toolkit.storage.vector_store.pinecone')
    def test_upsert_vectors(self, mock_pinecone, sample_vectors):
        """Test upserting vectors"""
        mock_index = MagicMock()
        mock_pinecone.Index.return_value = mock_index
        
        store = DomainAwareVectorStore(domain="physics", api_key="test-key")
        store.upsert_vectors("quantum", sample_vectors)
        
        # Verify upsert was called with correct namespace
        mock_index.upsert.assert_called_once()
        call_args = mock_index.upsert.call_args
        assert call_args[1]['namespace'] == "physics/quantum"
    
    @patch('daath_toolkit.storage.vector_store.pinecone')
    def test_query_similar(self, mock_pinecone):
        """Test querying similar vectors"""
        mock_index = MagicMock()
        mock_index.query.return_value = {
            'matches': [
                {'id': 'vec-1', 'score': 0.95},
                {'id': 'vec-2', 'score': 0.87}
            ]
        }
        mock_pinecone.Index.return_value = mock_index
        
        store = DomainAwareVectorStore(domain="physics", api_key="test-key")
        results = store.query_similar("quantum", [0.1] * 1536, top_k=2)
        
        assert len(results['matches']) == 2
        assert results['matches'][0]['score'] == 0.95
    
    @patch('daath_toolkit.storage.vector_store.pinecone')
    def test_list_instances(self, mock_pinecone):
        """Test listing instances in domain"""
        mock_index = MagicMock()
        mock_index.describe_index_stats.return_value = {
            'namespaces': {
                'physics/quantum': {'vector_count': 100},
                'physics/relativity': {'vector_count': 50},
                'chemistry/organic': {'vector_count': 75}
            }
        }
        mock_pinecone.Index.return_value = mock_index
        
        store = DomainAwareVectorStore(domain="physics", api_key="test-key")
        instances = store.list_instances()
        
        assert len(instances) == 2
        assert "quantum" in instances
        assert "relativity" in instances
        assert "organic" not in instances  # Different domain
```

### Paso 5: Integration tests

```python
# tests/test_capture/test_integration.py
import pytest
from pathlib import Path
from daath_toolkit.capture import ChatlogCapture

@pytest.mark.integration
class TestChatlogCaptureIntegration:
    """Integration tests with real filesystem"""
    
    def test_end_to_end_capture(self, temp_workspace):
        """Test complete end-to-end chatlog capture"""
        messages = [
            {"role": "user", "content": "Test question"},
            {"role": "assistant", "content": "[MELQUISEDEC] Test answer"},
            {"role": "user", "content": "Follow up"},
            {"role": "assistant", "content": "[HYPATIA] Detailed explanation"},
        ]
        
        capture = ChatlogCapture("test-domain", "test-instance", temp_workspace)
        result = capture.save_conversation(messages, metadata={"test": True})
        
        # Verify all artifacts created
        chatlog_dir = temp_workspace / "_daath" / "chatlog"
        assert (chatlog_dir / "full-transcript.md").exists()
        assert (chatlog_dir / "metadata.yaml").exists()
        assert (chatlog_dir / "by-rostro" / "01-melquisedec.md").exists()
        assert (chatlog_dir / "by-rostro" / "02-hypatia.md").exists()
        
        # Verify content integrity
        transcript = (chatlog_dir / "full-transcript.md").read_text()
        assert "Test question" in transcript
        assert "Test answer" in transcript
```

### Paso 6: Configurar pytest coverage

```powershell
# Agregar a pyproject.toml (en ISSUE-004)
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --cov=daath_toolkit --cov-report=term-missing --cov-report=html"
markers = [
    "integration: marks tests as integration tests (deselect with '-m \"not integration\"')",
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
```

### Paso 7: Ejecutar tests

```powershell
cd packages/daath-toolkit

# Ejecutar todos los tests
pytest -v

# Solo unit tests (skip integration)
pytest -v -m "not integration"

# Con coverage
pytest -v --cov=daath_toolkit --cov-report=html

# Ver reporte HTML
start htmlcov/index.html
```

## ✅ Criterios de Aceptación

1. ✅ **Test structure creada**:
   - `tests/` directory con subdirectorios por módulo
   - `conftest.py` con fixtures reutilizables
   - Fixtures de ejemplo en `tests/fixtures/`

2. ✅ **Coverage >80%**:
   - ChatlogCapture: >80% line coverage
   - DomainAwareVectorStore: >80% line coverage
   - Report generado con `pytest --cov`

3. ✅ **Tests passing**:
   - Todos los tests pasan sin errores
   - No warnings críticos de pytest

4. ✅ **Mocking correcto**:
   - Dependencias externas (Pinecone, OpenAI) mocked
   - No llamadas reales a APIs durante tests

5. ✅ **Documentation**:
   - Docstrings en cada test explicando qué valida
   - README actualizado con instrucciones para ejecutar tests

## 🧪 Testing

### Manual Testing
```powershell
# 1. Instalar dependencies
pip install -e .[dev]

# 2. Ejecutar tests
pytest -v

# 3. Verificar coverage
pytest --cov=daath_toolkit --cov-report=term-missing
# Debe mostrar >80% coverage

# 4. Ejecutar specific test file
pytest tests/test_capture/test_chatlog_capture.py -v

# 5. Ejecutar specific test
pytest tests/test_capture/test_chatlog_capture.py::TestChatlogCapture::test_init_valid -v
```

### CI Integration (futuro)
```yaml
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -e .[dev]
      - run: pytest --cov=daath_toolkit --cov-report=xml
      - uses: codecov/codecov-action@v3  # Upload coverage
```

## 📚 Referencias

- **Pytest docs**: https://docs.pytest.org/
- **pytest-cov**: https://pytest-cov.readthedocs.io/
- **unittest.mock**: https://docs.python.org/3/library/unittest.mock.html
- **Testing best practices**: https://docs.python-guide.org/writing/tests/

## 📝 Notas Adicionales

### Estrategia de testing:
1. **Unit tests**: Testear funciones individuales con mocks
2. **Integration tests**: Testear flujos completos con real filesystem (temp)
3. **E2E tests** (futuro): Testear con Pinecone/OpenAI staging environments

### Fixtures reutilizables a crear:
- `temp_workspace`: Workspace temporal para tests
- `sample_messages`: Conversaciones de ejemplo
- `mock_pinecone`: Mock de cliente Pinecone
- `mock_openai`: Mock de cliente OpenAI (para futuros tests)
- `sample_vectors`: Vectores de ejemplo para storage tests

### Tests a agregar después:
- Tests de performance (large conversations, large vector batches)
- Tests de error recovery (network failures, disk full)
- Tests de backwards compatibility (API changes)
- Property-based testing con `hypothesis`

### Coverage targets por módulo:
- `chatlog_capture.py`: 85%+ (muchas edge cases)
- `vector_store.py`: 80%+ (depende de Pinecone, harder to mock)
- `generators/`: 70%+ (template rendering)
- `validators/`: 90%+ (validation logic, pure functions)

---

**Estado**: 🔴 OPEN  
**Estimación**: 3-4 horas  
**Bloqueadores**: ISSUE-004 (necesita pyproject.toml para pytest config)  
**Dependencias**: ISSUE-004 debe completarse primero
