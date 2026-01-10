# Triple Persistence System

Sistema de persistencia triple (Markdown + Graph + Vector) para knowledge management en proyectos de investigación MELQUISEDEC.

## Stack

- **Framework**: LlamaIndex 0.14.6
- **Database**: Neo4j 5.26 (Graph + Vector unified)
- **Embeddings**: Ollama nomic-embed-text (768 dim)
- **API**: FastAPI 0.109+

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```bash
# 1. Start infrastructure
docker-compose up -d

# 2. Run ingestion
python -m triple_persistence.cli ingest \
  --project research-autopoietic-template \
  --path ../apps/research-autopoietic-template/010-define

# 3. Query
python -m triple_persistence.cli query \
  --text "templates autopoiéticos"
```

## Architecture

```
triple_persistence/
├── __init__.py
├── ingestion.py      # Pipeline MD → Graph + Vector
├── retriever.py      # Hybrid queries (Vector + Graph)
├── models.py         # Pydantic schemas
├── neo4j_client.py   # Neo4j driver wrapper
└── api.py            # FastAPI endpoints
```

## API Endpoints

- `POST /ingest` - Ingest directory into triple-persistence
- `POST /query` - Hybrid semantic + graph query
- `GET /stats` - System statistics

## Development

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Format code
black triple_persistence/
```
