# DAATH Toolkit

**DAATH-ZEN Toolkit** for research automation, knowledge capture, and autopoiesis workflows.

## Overview

DAATH Toolkit provides essential utilities for implementing the DAATH-ZEN methodology in your research and development workflows.

## Features

- **Chatlog Capture**: Automated extraction and structuring of conversation logs
- **Vector Storage**: Domain-aware vector storage for knowledge graphs
- **Research Generators**: Templates and automation for research instances
- **Validators**: Quality assurance for research artifacts

## Installation

```bash
# From source (development)
pip install -e packages/daath-toolkit

# With AI dependencies
pip install -e "packages/daath-toolkit[ai]"

# With development tools
pip install -e "packages/daath-toolkit[dev]"
```

## Package Structure

```
daath-toolkit/
├── capture/          # Chatlog capture utilities
│   └── chatlog_capture.py
├── generators/       # Research instance generators
│   └── new_research.py
├── storage/          # Vector storage and knowledge graphs
│   └── vector_store.py
├── validators/       # Quality assurance validators
│   └── validate_research.py
└── testing/          # Test suite
```

## Usage

### Chatlog Capture

```python
from daath_toolkit.capture import chatlog_capture

# Capture conversation data
capture = chatlog_capture.ChatlogCapture()
result = capture.process(conversation_data)
```

### Vector Storage

```python
from daath_toolkit.storage import vector_store

# Initialize domain-aware vector store
store = vector_store.DomainAwareVectorStore()
store.index_documents(documents)
```

## Development

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=daath_toolkit --cov-report=term-missing

# Format code
black daath_toolkit/
isort daath_toolkit/

# Lint
flake8 daath_toolkit/
```

## Dependencies

### Core
- pyyaml >= 6.0.0
- neo4j >= 5.14.0

### Optional (AI)
- pinecone-client >= 3.0.0
- openai >= 1.0.0

## License

MIT License - See LICENSE file for details

## Project

Part of the [ALEIA-MELQUISEDEC](https://github.com/ccolombia-ui/aleia-melquisedec) monorepo.

**Methodology**: DAATH-ZEN v4.0.0
**Rostros**: MELQUISEDEC, HYPATIA, SALOMON, MORPHEUS, ALMA
