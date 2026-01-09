# GenAI Stack Architecture Analysis

**Repositorio**: docker/genai-stack
**URL**: https://github.com/docker/genai-stack
**Stack**: LangChain + Docker + Neo4j + Ollama
**Colaboración**: Docker, Neo4j, LangChain, Ollama
**Versión Neo4j**: 5.26
**Licencia**: CC0-1.0
**Stars**: 5.2k | **Forks**: 1.2k | **Contributors**: 27

---

## 1. Resumen Ejecutivo

GenAI Stack es una solución pre-configurada y lista para usar que combina:
- **Neo4j 5.26** como base de datos graph+vector unificada
- **Ollama** para LLMs locales (con soporte para modelos cloud: OpenAI, Claude, etc.)
- **LangChain** como framework de orquestación
- **Docker Compose** para arquitectura multi-contenedor

**Propósito**: Permitir a desarrolladores iniciar aplicaciones GenAI sin configuración manual, con ejemplos prácticos de RAG (Retrieval-Augmented Generation) usando Neo4j Vector Index.

---

## 2. Arquitectura Docker Compose

### 2.1 Servicios Principales

```yaml
services:
  # Base de Datos Graph+Vector
  database:
    image: neo4j:5.26
    ports: [7687:7687, 7474:7474]  # Bolt + Browser
    environment:
      - NEO4J_AUTH=neo4j/password
      - NEO4J_PLUGINS=["apoc"]
      - NEO4J_dbms_security_procedures_unrestricted=apoc.*
    volumes: [$PWD/data:/data]
    healthcheck:
      test: ["CMD-SHELL", "wget --no-verbose --tries=1 --spider localhost:7474 || exit 1"]
      interval: 15s
      timeout: 30s
      retries: 10

  # LLM Local (Perfil Linux)
  llm:
    image: ollama/ollama:latest
    profiles: ["linux"]  # Solo en Linux

  # LLM con GPU (Perfil Linux-GPU)
  llm-gpu:
    image: ollama/ollama:latest
    profiles: ["linux-gpu"]
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  # Descarga de Modelos Ollama
  pull-model:
    build:
      context: .
      dockerfile: pull_model.Dockerfile
    environment:
      - OLLAMA_BASE_URL=${OLLAMA_BASE_URL}
      - LLM=${LLM-llama2}
    tty: true

  # Cargador de Datos StackOverflow
  loader:
    build:
      dockerfile: loader.Dockerfile
    ports: [8502:8502]
    depends_on:
      database: {condition: service_healthy}
      pull-model: {condition: service_completed_successfully}
    environment:
      - NEO4J_URI=neo4j://database:7687
      - EMBEDDING_MODEL=${EMBEDDING_MODEL-sentence_transformer}
      - OLLAMA_BASE_URL=${OLLAMA_BASE_URL}

  # Bot de Soporte (App 1)
  bot:
    build:
      dockerfile: bot.Dockerfile
    ports: [8501:8501]
    environment:
      - LLM=${LLM-llama2}
      - EMBEDDING_MODEL=${EMBEDDING_MODEL-sentence_transformer}
    depends_on:
      database: {condition: service_healthy}

  # PDF Q&A Bot (App 3)
  pdf_bot:
    build:
      dockerfile: pdf_bot.Dockerfile
    ports: [8503:8503]
    environment:
      - LLM=${LLM-llama2}
      - EMBEDDING_MODEL=${EMBEDDING_MODEL-sentence_transformer}

  # HTTP API (App 4)
  api:
    build:
      dockerfile: api.Dockerfile
    ports: [8504:8504]
    healthcheck:
      test: ["CMD-SHELL", "wget --no-verbose --tries=1 http://localhost:8504/ || exit 1"]
      interval: 5s
      timeout: 3s
      retries: 5
    depends_on:
      database: {condition: service_healthy}

  # Frontend Svelte (App 5)
  front-end:
    build:
      dockerfile: front-end.Dockerfile
    ports: [8505:8505]
    depends_on:
      api: {condition: service_healthy}
    x-develop:
      watch:
        - action: sync
          path: ./front-end
          target: /app
          ignore: [./front-end/node_modules/]

networks:
  net:
```

**Análisis de Arquitectura**:
- ✅ **Separación de Responsabilidades**: Cada componente en su propio contenedor (database, llm, loader, api, frontend)
- ✅ **Health Checks**: Garantizan arranque ordenado (database → pull-model → apps)
- ✅ **Profiles**: Soporta diferentes entornos (Linux, Linux-GPU, MacOS/Windows con Ollama externo)
- ✅ **Hot Reload**: `x-develop.watch` para desarrollo ágil (sync front-end, rebuild back-end)
- ⚠️ **Estado Compartido**: Volumen `$PWD/data` compartido (no ideal para producción)

---

## 3. Neo4j Vector Index Implementation

### 3.1 Creación de Índices Vector

**Archivo**: `utils.py`

```python
def create_vector_index(driver) -> None:
    # Índice para preguntas (Question)
    index_query = """
    CREATE VECTOR INDEX stackoverflow IF NOT EXISTS
    FOR (m:Question) ON m.embedding
    """
    try:
        driver.query(index_query)
    except:  # Already exists
        pass

    # Índice para respuestas (Answer)
    index_query = """
    CREATE VECTOR INDEX top_answers IF NOT EXISTS
    FOR (m:Answer) ON m.embedding
    """
    try:
        driver.query(index_query)
    except:  # Already exists
        pass

def create_constraints(driver):
    driver.query("""
    CREATE CONSTRAINT question_id IF NOT EXISTS
    FOR (q:Question) REQUIRE (q.id) IS UNIQUE
    """)
    driver.query("""
    CREATE CONSTRAINT answer_id IF NOT EXISTS
    FOR (a:Answer) REQUIRE (a.id) IS UNIQUE
    """)
    driver.query("""
    CREATE CONSTRAINT user_id IF NOT EXISTS
    FOR (u:User) REQUIRE (u.id) IS UNIQUE
    """)
    driver.query("""
    CREATE CONSTRAINT tag_name IF NOT EXISTS
    FOR (t:Tag) REQUIRE (t.name) IS UNIQUE
    """)
```

**Análisis**:
- ✅ **IF NOT EXISTS**: Idempotente (seguro para re-ejecuciones)
- ✅ **Dos Índices**: `stackoverflow` (Questions) + `top_answers` (Answers)
- ✅ **Constraints**: Unicidad en IDs (Question, Answer, User, Tag)
- ⚠️ **Sin Configuración HNSW**: Usa defaults (m, efConstruction no especificados)
- ⚠️ **Sin Dimensiones Explícitas**: Neo4j infiere de primeros embeddings

---

### 3.2 Ingesta de Embeddings

**Archivo**: `loader.py`

```python
def insert_so_data(data: dict) -> None:
    # Calcular embeddings para preguntas y respuestas
    for q in data["items"]:
        question_text = q["title"] + "\n" + q["body_markdown"]
        q["embedding"] = embeddings.embed_query(question_text)
        for a in q["answers"]:
            a["embedding"] = embeddings.embed_query(
                question_text + "\n" + a["body_markdown"]
            )

    # Ingesta con Cypher
    import_query = """
    UNWIND $data AS q
    MERGE (question:Question {id:q.question_id})
    ON CREATE SET
        question.title = q.title,
        question.link = q.link,
        question.score = q.score,
        question.favorite_count = q.favorite_count,
        question.creation_date = datetime({epochSeconds: q.creation_date}),
        question.body = q.body_markdown,
        question.embedding = q.embedding  # ← Vector embedding
    FOREACH (tagName IN q.tags |
        MERGE (tag:Tag {name:tagName})
        MERGE (question)-[:TAGGED]->(tag)
    )
    FOREACH (a IN q.answers |
        MERGE (question)<-[:ANSWERS]-(answer:Answer {id:a.answer_id})
        SET answer.is_accepted = a.is_accepted,
            answer.score = a.score,
            answer.creation_date = datetime({epochSeconds:a.creation_date}),
            answer.body = a.body_markdown,
            answer.embedding = a.embedding  # ← Vector embedding
        MERGE (answerer:User {id:coalesce(a.owner.user_id, "deleted")})
        ON CREATE SET
            answerer.display_name = a.owner.display_name,
            answerer.reputation = a.owner.reputation
        MERGE (answer)<-[:PROVIDED]-(answerer)
    )
    WITH * WHERE NOT q.owner.user_id IS NULL
    MERGE (owner:User {id:q.owner.user_id})
    ON CREATE SET
        owner.display_name = q.owner.display_name,
        owner.reputation = q.owner.reputation
    MERGE (owner)-[:ASKED]->(question)
    """
    neo4j_graph.query(import_query, {"data": data["items"]})
```

**Análisis**:
- ✅ **Batch Processing**: `UNWIND` procesa múltiples preguntas en 1 transacción
- ✅ **Embedding Inline**: Embeddings calculados en Python, pasados como array a Neo4j
- ✅ **Graph Structure**: Modela relaciones `[:ASKED]`, `[:ANSWERS]`, `[:TAGGED]`, `[:PROVIDED]`
- ✅ **MERGE + ON CREATE**: Idempotente (no duplica nodos existentes)
- ⚠️ **Chunking Manual**: Concatena `title + body` sin estrategia de chunking avanzada
- ⚠️ **Sin Error Handling**: No captura errores de embedding API (Ollama, OpenAI)
- ⚠️ **Performance**: Calcula embeddings sincrónicamente (bloquea thread)

**Patrón Clave**: **Embedding-first, then Cypher** (calcular embeddings en app, ingestar en Neo4j)

---

### 3.3 Retrieval con Vector + Knowledge Graph

**Archivo**: `chains.py`

```python
def configure_qa_rag_chain(llm, embeddings, embeddings_store_url, username, password):
    # RAG response with Vector + Knowledge Graph
    general_system_template = """
    Use the following pieces of context to answer the question at the end.
    The context contains question-answer pairs and their links from Stackoverflow.
    You should prefer information from accepted or more upvoted answers.
    Make sure to rely on information from the answers and not on questions.
    When you find particular answer useful, make sure to cite it using the link.
    If you don't know the answer, just say that you don't know.
    ----
    {summaries}
    ----
    Each answer should contain a section at the end of links to
    Stackoverflow questions and answers you found useful (Source value).
    You can only use links present in the context.
    Generate concise answers with references section.
    """

    # Neo4j Vector Store con custom retrieval query
    kg = Neo4jVector.from_existing_index(
        embedding=embeddings,
        url=embeddings_store_url,
        username=username,
        password=password,
        database="neo4j",
        index_name="stackoverflow",  # ← Vector index
        text_node_property="body",
        retrieval_query="""
        WITH node AS question, score AS similarity
        CALL {
            WITH question
            MATCH (question)<-[:ANSWERS]-(answer)
            WITH answer
            ORDER BY answer.is_accepted DESC, answer.score DESC
            WITH collect(answer)[..2] AS answers  # Top 2 answers
            RETURN reduce(
                str='', answer IN answers |
                str + '\n### Answer (Accepted: ' + answer.is_accepted +
                      ' Score: ' + answer.score + '): ' + answer.body + '\n'
            ) AS answerTexts
        }
        RETURN
            '##Question: ' + question.title + '\n' + question.body + '\n' + answerTexts AS text,
            similarity AS score,
            {source: question.link} AS metadata
        ORDER BY similarity ASC  # Best answers last
        """
    )

    # LangChain LCEL (LangChain Expression Language)
    kg_qa = (
        RunnableParallel({
            "summaries": kg.as_retriever(search_kwargs={"k": 2}) | format_docs,
            "question": RunnablePassthrough(),
        })
        | qa_prompt
        | llm
        | StrOutputParser()
    )
    return kg_qa
```

**Análisis de Retrieval Query**:
- ✅ **Hybrid Approach**: Vector similarity (`score`) + Graph traversal (`MATCH (question)<-[:ANSWERS]-(answer)`)
- ✅ **Ranking Inteligente**: Prioriza `is_accepted DESC, score DESC` (respuestas aceptadas y mejor puntuadas)
- ✅ **Top-K Filtering**: `collect(answer)[..2]` limita a 2 mejores respuestas por pregunta
- ✅ **Metadata Structured**: Retorna `{source: question.link}` para citations
- ✅ **LangChain Integration**: `Neo4jVector.from_existing_index()` conecta vector store con LCEL
- ⚠️ **Hardcoded K=2**: No configurable desde UI (podría ser parámetro)
- ⚠️ **ORDER BY similarity ASC**: Contra-intuitivo (comentario dice "best answers last" para LLM context window)

**Patrón Clave**: **Retrieval Query Custom** (Neo4j permite Cypher complejo en retrieval, no solo `MATCH (n) WHERE similarity(n.embedding, $embedding) > threshold`)

---

## 4. Embedding Models Support

**Archivo**: `chains.py`

```python
def load_embedding_model(embedding_model_name: str, logger=BaseLogger(), config={}):
    if embedding_model_name == "ollama":
        embeddings = OllamaEmbeddings(
            base_url=config["ollama_base_url"],
            model="llama2"
        )
        dimension = 4096
    elif embedding_model_name == "openai":
        embeddings = OpenAIEmbeddings()
        dimension = 1536
    elif embedding_model_name == "aws":
        embeddings = BedrockEmbeddings()
        dimension = 1536
    elif embedding_model_name == "google-genai-embedding-001":
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001"
        )
        dimension = 768
    else:  # Default: sentence-transformers
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            cache_folder="/embedding_model"
        )
        dimension = 384
    return embeddings, dimension
```

**Modelos Soportados**:
1. **Ollama** (llama2): 4096 dimensions
2. **OpenAI** (text-embedding-ada-002): 1536 dimensions
3. **AWS Bedrock** (Titan Embeddings): 1536 dimensions
4. **Google Generative AI** (embedding-001): 768 dimensions
5. **HuggingFace** (all-MiniLM-L6-v2): 384 dimensions ← **Default**

**Análisis**:
- ✅ **Multi-Provider**: Flexible para diferentes casos (local, cloud, costo)
- ✅ **Local Cache**: `/embedding_model` volumen Docker para HuggingFace
- ✅ **Explicit Dimensions**: Retorna dimensionalidad (crítico para índice vector)
- ⚠️ **Hardcoded Models**: `llama2` para Ollama (debería leer desde `.env`)
- ⚠️ **Sin Validación**: No verifica si dimensión coincide con índice existente

---

## 5. LLM Support

**Archivo**: `chains.py`

```python
def load_llm(llm_name: str, logger=BaseLogger(), config={}):
    if llm_name in ["gpt-4", "gpt-4o", "gpt-4-turbo"]:
        return ChatOpenAI(
            temperature=0,
            model_name=llm_name,
            streaming=True
        )
    elif llm_name == "gpt-3.5":
        return ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo",
            streaming=True
        )
    elif llm_name == "claudev2":
        return ChatBedrock(
            model_id="anthropic.claude-v2",
            model_kwargs={"temperature": 0.0, "max_tokens_to_sample": 1024},
            streaming=True
        )
    elif llm_name.startswith(AWS_MODELS):  # Bedrock models
        return ChatBedrock(
            model_id=llm_name,
            model_kwargs={"temperature": 0.0, "max_tokens_to_sample": 1024},
            streaming=True
        )
    elif len(llm_name):  # Ollama models
        return ChatOllama(
            temperature=0,
            base_url=config["ollama_base_url"],
            model=llm_name,
            streaming=True,
            top_k=10,  # Diversity control
            top_p=0.3,  # Focused text generation
            num_ctx=3072  # Context window
        )
    return ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True)
```

**LLMs Soportados**:
1. **OpenAI**: gpt-4, gpt-4o, gpt-4-turbo, gpt-3.5-turbo
2. **AWS Bedrock**: Claude v2, Titan, Llama, Mistral, Cohere, AI21 Jamba
3. **Ollama**: llama2, llama3, mistral, mixtral, qwen, phi, etc. (cualquier modelo Ollama)

**Parámetros Ollama**:
- `temperature=0`: Determinístico (reproducible)
- `top_k=10`: Sampling limitado (conservador)
- `top_p=0.3`: Nucleus sampling (foco en top 30% probabilidad)
- `num_ctx=3072`: Context window tokens

**Análisis**:
- ✅ **Streaming**: Todos los LLMs soportan SSE (Server-Sent Events)
- ✅ **Multi-Provider**: Cloud (OpenAI, Bedrock) + Local (Ollama)
- ✅ **Fallback**: Default a `gpt-3.5-turbo` si LLM no reconocido
- ⚠️ **Hardcoded Params**: `top_k`, `top_p`, `num_ctx` no configurables desde `.env`

---

## 6. Arquitectura de Capas

### 6.1 Diagrama de Capas

```
┌─────────────────────────────────────────────────────────┐
│              Frontend Layer (Apps 1-5)                  │
│  Streamlit (bot.py, loader.py, pdf_bot.py)             │
│  Svelte (front-end/) + FastAPI (api.py)                │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP/Streamlit
┌─────────────────────▼───────────────────────────────────┐
│              Orchestration Layer (chains.py)            │
│  LangChain LCEL (RunnableParallel, RunnablePassthrough) │
│  Prompt Templates (SystemMessage, HumanMessage)         │
│  RAG Chains (LLM-only, Vector+KG)                       │
└─────────────────────┬───────────────────────────────────┘
                      │ LangChain SDK
┌─────────────────────▼───────────────────────────────────┐
│              Integration Layer (LangChain)              │
│  Neo4jVector (langchain-neo4j)                          │
│  OllamaEmbeddings (langchain-ollama)                    │
│  ChatOllama (langchain-ollama)                          │
│  OpenAIEmbeddings (langchain-openai)                    │
│  ChatOpenAI (langchain-openai)                          │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP/gRPC
┌─────────────────────▼───────────────────────────────────┐
│              External Services Layer                    │
│  Neo4j 5.26 (Vector Index + Graph)                      │
│  Ollama (Embeddings + LLM)                              │
│  OpenAI API (Embeddings + LLM)                          │
│  AWS Bedrock (Embeddings + LLM)                         │
└─────────────────────────────────────────────────────────┘
```

### 6.2 Responsabilidades por Capa

1. **Frontend Layer**:
   - UI/UX (Streamlit widgets, Svelte components)
   - Input validation (text_input, number_input)
   - Session state management (Streamlit session_state)
   - SSE streaming rendering

2. **Orchestration Layer** (`chains.py`):
   - RAG pipeline construction (LLM-only vs Vector+KG)
   - Prompt engineering (System + Human templates)
   - Chain composition (LCEL `|` operator)
   - Output parsing (StrOutputParser)

3. **Integration Layer** (LangChain):
   - Provider abstractions (`ChatOpenAI`, `ChatOllama`, `OllamaEmbeddings`)
   - Vector store interface (`Neo4jVector`)
   - Retriever pattern (`as_retriever(search_kwargs={"k": 2})`)
   - Document formatting (`format_docs`)

4. **External Services Layer**:
   - Neo4j: Vector similarity search + Cypher queries
   - Ollama: Local LLM inference + embeddings
   - Cloud APIs: OpenAI, AWS Bedrock, Google GenAI

**Observación**: ⚠️ **No hay capa de Dominio/Negocio explícita** (lógica mezclada en `chains.py` y apps)

---

## 7. Testing Strategy

### 7.1 Testing Actual (Repositorio)

**Análisis de Repositorio**:
- ❌ **Sin carpeta `tests/`**
- ❌ **Sin `pytest.ini`, `tox.ini`, o `.coveragerc`**
- ❌ **Sin GitHub Actions CI/CD** (no `.github/workflows/`)
- ❌ **Sin code coverage tracking** (no Codecov/SonarQube badges)

**Testing Observado**:
- 🔴 **Manual Testing Only**: README.md instruye `docker compose up` y probar en browser
- 🔴 **Healthchecks Docker**: Validan disponibilidad de servicios (no lógica de negocio)

### 7.2 Observaciones

**Fortalezas**:
- ✅ Health checks en `docker-compose.yml` (validan startup)
- ✅ Development mode con hot reload (`x-develop.watch`)

**Debilidades Críticas**:
- ❌ **Zero Unit Tests**: Sin tests para `chains.py`, `utils.py`, `loader.py`
- ❌ **Zero Integration Tests**: Sin tests para Neo4j queries, embeddings, LLM responses
- ❌ **Zero E2E Tests**: Sin Selenium/Playwright para validar UI
- ❌ **Sin CI/CD**: No hay automatización de testing en pull requests
- ❌ **Sin Test Data**: No hay fixtures para datos StackOverflow de prueba

**Implicaciones**:
- ⚠️ **Regression Risk**: Cambios pueden romper funcionalidad sin detección automática
- ⚠️ **Refactoring Fear**: Difícil refactorizar sin seguridad de tests
- ⚠️ **Production Readiness**: No apto para producción sin test suite

---

## 8. Code Patterns Extraídos

### Pattern 1: **Adapter Pattern - Multi-Provider Embeddings**

```python
# chains.py - Abstracción de múltiples providers de embeddings
def load_embedding_model(embedding_model_name: str, config={}):
    if embedding_model_name == "ollama":
        return OllamaEmbeddings(base_url=config["ollama_base_url"], model="llama2"), 4096
    elif embedding_model_name == "openai":
        return OpenAIEmbeddings(), 1536
    elif embedding_model_name == "aws":
        return BedrockEmbeddings(), 1536
    # ... más providers
    else:  # Default HuggingFace
        return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), 384
```

**Propósito**: Normalizar interfaz de diferentes providers de embeddings
**Ventaja**: Cambiar provider con 1 variable de entorno (`EMBEDDING_MODEL`)
**Mejora Propuesta**: Usar protocolo `EmbeddingAdapter` en vez de if/elif gigante

---

### Pattern 2: **Idempotent Schema Creation**

```python
# utils.py - Creación idempotente de índices y constraints
def create_vector_index(driver) -> None:
    try:
        driver.query("CREATE VECTOR INDEX stackoverflow IF NOT EXISTS FOR (m:Question) ON m.embedding")
    except:
        pass  # Already exists
```

**Propósito**: Permitir re-ejecución sin errores
**Ventaja**: Safe para CI/CD, migrations, dev environment reset
**Mejora Propuesta**: Log en vez de `pass`, validar que índice esté en estado `ONLINE`

---

### Pattern 3: **Embedding-First Cypher Ingestion**

```python
# loader.py - Calcular embeddings en Python, ingestar en Neo4j
def insert_so_data(data: dict) -> None:
    for q in data["items"]:
        question_text = q["title"] + "\n" + q["body_markdown"]
        q["embedding"] = embeddings.embed_query(question_text)
        for a in q["answers"]:
            a["embedding"] = embeddings.embed_query(question_text + "\n" + a["body_markdown"])

    # Cypher con embeddings como array
    import_query = """
    UNWIND $data AS q
    MERGE (question:Question {id:q.question_id})
    ON CREATE SET question.embedding = q.embedding
    """
    neo4j_graph.query(import_query, {"data": data["items"]})
```

**Propósito**: Neo4j no tiene embedding API nativo (delegado a app layer)
**Ventaja**: Flexible (cualquier modelo de embeddings)
**Desventaja**: Latencia alta (1 embedding call = 1 network roundtrip)
**Mejora Propuesta**: Batch embedding calls (Ollama soporta batch inference)

---

### Pattern 4: **Custom Retrieval Query - Hybrid Vector+Graph**

```python
# chains.py - Retrieval query que combina similarity + graph traversal
retrieval_query = """
WITH node AS question, score AS similarity
CALL {
    WITH question
    MATCH (question)<-[:ANSWERS]-(answer)
    ORDER BY answer.is_accepted DESC, answer.score DESC
    WITH collect(answer)[..2] AS answers
    RETURN reduce(str='', answer IN answers | str + '\n### Answer: ' + answer.body) AS answerTexts
}
RETURN '##Question: ' + question.title + '\n' + question.body + '\n' + answerTexts AS text,
       similarity AS score,
       {source: question.link} AS metadata
ORDER BY similarity ASC
"""
kg = Neo4jVector.from_existing_index(
    embedding=embeddings,
    retrieval_query=retrieval_query  # ← Custom Cypher
)
```

**Propósito**: Ir más allá de simple vector similarity (enriquecer con graph context)
**Ventaja**: Aprovecha Neo4j como graph+vector unified store
**Patrón Clave**: **GraphRAG** (RAG + Knowledge Graph)
**Mejora Propuesta**: Parametrizar `collect(answer)[..2]` (hardcoded top-2)

---

### Pattern 5: **LangChain LCEL - Runnable Composition**

```python
# chains.py - Composición declarativa con LCEL (LangChain Expression Language)
kg_qa = (
    RunnableParallel({
        "summaries": kg.as_retriever(search_kwargs={"k": 2}) | format_docs,
        "question": RunnablePassthrough(),
    })
    | qa_prompt
    | llm
    | StrOutputParser()
)
```

**Propósito**: Pipeline RAG declarativo (no callbacks complejos)
**Ventaja**: Legible, testeable, composable (reusable)
**Componentes**:
- `RunnableParallel`: Ejecuta `summaries` y `question` en paralelo
- `kg.as_retriever()`: Vector search → top-k documents
- `format_docs`: Transforma `List[Document]` → `str`
- `qa_prompt`: Template con `{summaries}` + `{question}`
- `llm`: LLM call (streaming)
- `StrOutputParser()`: `AIMessage` → `str`

**Mejora Propuesta**: Agregar `RunnableWithMessageHistory` para multi-turn conversations

---

### Pattern 6: **Streaming SSE - FastAPI**

```python
# api.py (inferido de healthcheck port 8504)
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse

@app.get("/query-stream")
async def query_stream(text: str, rag: bool):
    async def event_generator():
        for chunk in kg_qa.stream({"question": text}):
            yield {"data": chunk}
    return EventSourceResponse(event_generator())
```

**Propósito**: Streaming de respuesta LLM token-by-token (mejor UX)
**Ventaja**: User ve respuesta inmediata (no espera 30s)
**Tecnología**: SSE (Server-Sent Events) con `sse-starlette`
**Mejora Propuesta**: Agregar error handling en stream (timeout, LLM failure)

---

### Pattern 7: **Environment-Based Configuration**

```python
# loader.py, bot.py, api.py - Todas las apps leen desde .env
from dotenv import load_dotenv
load_dotenv(".env")

url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
embedding_model_name = os.getenv("EMBEDDING_MODEL")
llm_name = os.getenv("LLM")
```

**Propósito**: 12-Factor App (config separado de código)
**Ventaja**: Mismo código funciona en dev/staging/prod con diferentes `.env`
**Desventaja**: No hay validación de variables requeridas (falla en runtime si falta `NEO4J_URI`)
**Mejora Propuesta**: `pydantic.BaseSettings` para validación obligatoria

---

## 9. Dependencies (requirements.txt)

```
# Core
python-dotenv
pydantic
neo4j

# LLM Frameworks
streamlit==1.32.1
langchain-openai==0.3.8
langchain-community==0.3.19
langchain-google-genai==2.0.11
langchain-ollama==0.2.3
langchain-huggingface==0.1.2
langchain-aws==0.2.15
langchain-neo4j==0.4.0

# Web Framework
fastapi
uvicorn
sse-starlette

# Utilities
wikipedia
tiktoken
Pillow
PyPDF2
boto3
```

**Versiones Críticas**:
- `neo4j`: Driver Python (compatible con Neo4j 5.26)
- `langchain-neo4j==0.4.0`: Integración LangChain-Neo4j (incluye `Neo4jVector`)
- `langchain-ollama==0.2.3`: Ollama embeddings + LLM
- `streamlit==1.32.1`: UI framework

**Observación**: ⚠️ **Sin `pytest`, `coverage`, `mypy`** (no hay testing/linting tools)

---

## 10. Strengths & Weaknesses

### ✅ Strengths (Fortalezas)

1. **🏆 Production-Ready Docker Compose**:
   - Health checks garantizan startup ordenado
   - Profiles para diferentes entornos (Linux, GPU, MacOS)
   - Hot reload para desarrollo ágil (`x-develop.watch`)

2. **🏆 Multi-Provider Support**:
   - 5 embedding providers (Ollama, OpenAI, AWS, Google, HuggingFace)
   - 3 LLM families (OpenAI, Bedrock, Ollama)
   - Fácil switch con variables de entorno

3. **🏆 Hybrid Vector+Graph RAG**:
   - Custom retrieval query combina similarity + graph traversal
   - Aprovecha relaciones `[:ANSWERS]`, `[:TAGGED]` para contexto enriquecido
   - Metadata structured (links para citations)

4. **🏆 LangChain LCEL - Composable Chains**:
   - Pipelines declarativos (`|` operator)
   - Reusable components (retriever, prompt, llm, parser)
   - Streaming support out-of-the-box

5. **🏆 Real-World Example**:
   - StackOverflow data model (Questions, Answers, Users, Tags)
   - Práctico para aprender (no toy example)

### ⚠️ Weaknesses (Debilidades)

1. **🔴 ZERO TESTING**:
   - Sin unit tests, integration tests, e2e tests
   - Sin CI/CD pipeline
   - Alto riesgo de regresiones

2. **🔴 No Architecture Patterns**:
   - Código mezclado en `chains.py` (no Hexagonal, no DDD)
   - Lógica de negocio en Streamlit apps (violación de separación)
   - Sin interfaces/protocolos (acoplamiento fuerte a LangChain)

3. **🔴 Hardcoded Configuration**:
   - `top_k=10`, `top_p=0.3`, `num_ctx=3072` no configurables
   - `collect(answer)[..2]` hardcoded (siempre 2 respuestas)
   - `model="llama2"` para Ollama (no lee desde `.env`)

4. **🔴 No Error Handling**:
   - `try/except: pass` sin logging
   - No manejo de timeout en Ollama/OpenAI
   - No validación de variables de entorno requeridas

5. **🔴 Performance Concerns**:
   - Embeddings sincrónicos (no batch)
   - Sin caching de embeddings (recalcula en cada restart)
   - Sin rate limiting para APIs externas

6. **🔴 Security**:
   - Contraseñas en `.env` (no usa secrets manager)
   - Neo4j sin TLS (desarrollo only)
   - Sin CORS configurado en FastAPI

7. **🔴 Observability**:
   - Logging mínimo (`BaseLogger` es solo `print`)
   - Sin métricas (latencia, QPS, error rate)
   - Sin tracing distribuido (aunque soporta LangSmith)

---

## 11. Applicability to MELQUISEDEC Project

### ✅ Adoptar (Keep)

1. **Docker Compose Architecture**:
   - Separar `neo4j`, `ollama`, `api`, `frontend` en servicios distintos
   - Health checks para garantizar startup
   - Profiles para diferentes entornos

2. **Custom Retrieval Query Pattern**:
   - Usar Cypher complejo en `Neo4jVector.from_existing_index(retrieval_query=...)`
   - Combinar vector similarity + graph traversal
   - Enriquecer contexto con relaciones de grafo

3. **Multi-Provider Embeddings**:
   - Soportar Ollama (local) + OpenAI (cloud) + qwen3-embedding
   - Adapter pattern con protocolo `EmbeddingPort`

4. **Idempotent Schema Creation**:
   - `IF NOT EXISTS` en todas las DDL
   - Safe para CI/CD migrations

5. **LangChain LCEL (con adaptaciones)**:
   - Usar LCEL como inspiración, pero wrapeado en Hexagonal Architecture
   - `LLMPort` implementado por `LangChainAdapter` (no acoplamiento directo)

### ⚠️ Mejorar (Improve)

1. **Testing Strategy**:
   - TDD con pytest + fixtures
   - 80% coverage mínimo
   - Integration tests con `testcontainers` (Neo4j + Ollama)

2. **Architecture**:
   - Hexagonal Architecture (Ports & Adapters)
   - Domain-Driven Design (Entities: `Question`, `Answer`, `Embedding`)
   - Separation of Concerns (no lógica en Streamlit)

3. **Configuration**:
   - `pydantic.BaseSettings` con validación
   - Todos los parámetros configurables desde `.env`
   - Secrets manager para producción (no `.env`)

4. **Error Handling**:
   - Structured logging (structlog)
   - Retry con exponential backoff (tenacity)
   - Circuit breaker para servicios externos

5. **Performance**:
   - Batch embeddings (Ollama batch API)
   - Redis cache para embeddings
   - Async I/O (asyncio, httpx)

### ❌ Rechazar (Reject)

1. **Streamlit como Frontend**:
   - No escalable (session state en memoria)
   - No apto para producción (no multi-tenant)
   - **Reemplazo**: FastAPI + Svelte/React (como App 5)

2. **Sin Testing**:
   - Inaceptable para MELQUISEDEC (calidad es prioridad)
   - **Reemplazo**: TDD desde día 1

3. **Hardcoded Config**:
   - Dificulta experimentación
   - **Reemplazo**: Todo configurable desde `.env` o config.yaml

4. **Código Monolítico**:
   - `chains.py` tiene múltiples responsabilidades
   - **Reemplazo**: Modular en packages (domain/, ports/, adapters/)

---

## 12. Key Takeaways (Lecciones Clave)

1. **Neo4j Vector Index Patterns**:
   - ✅ `IF NOT EXISTS` para idempotencia
   - ✅ Embeddings calculados en app layer (no en Neo4j)
   - ✅ Custom retrieval query para Hybrid RAG
   - ⚠️ Sin configuración HNSW explícita (m, efConstruction)

2. **Embedding Pipeline**:
   - ✅ Multi-provider support (Ollama, OpenAI, HuggingFace)
   - ⚠️ Embeddings sincrónicos (bloquea thread)
   - ⚠️ Sin caching (recalcula en cada ingesta)
   - 🔴 Sin batch processing (1 embedding = 1 HTTP call)

3. **LangChain Integration**:
   - ✅ LCEL simplifica RAG pipelines
   - ✅ `Neo4jVector` conecta Neo4j con LangChain
   - ⚠️ Acoplamiento fuerte (difícil cambiar a LlamaIndex)
   - 🔴 Sin tests (confianza 100% en LangChain)

4. **Architecture**:
   - ✅ Docker Compose para multi-servicio
   - 🔴 No hay arquitectura de dominio (solo scripts)
   - 🔴 No hay testing (regresión risk alto)
   - 🔴 No hay observability (debugging difícil)

5. **Production Readiness**:
   - ✅ Health checks en Docker Compose
   - 🔴 Sin tests automatizados
   - 🔴 Sin CI/CD
   - 🔴 Sin secrets management
   - 🔴 Sin monitoring/alerting

---

## 13. Recomendaciones para MELQUISEDEC

### 13.1 Adoptar con Refactoring

```python
# ❌ GenAI Stack (acoplado a LangChain)
from langchain_neo4j import Neo4jVector
kg = Neo4jVector.from_existing_index(embedding=embeddings, retrieval_query="...")

# ✅ MELQUISEDEC (Hexagonal Architecture)
from melquisedec.ports.vector_store import VectorStorePort
from melquisedec.adapters.neo4j import Neo4jVectorAdapter

vector_store: VectorStorePort = Neo4jVectorAdapter(
    connection=neo4j_conn,
    embedding_service=ollama_embeddings,
    retrieval_query="WITH node AS question, score AS similarity ..."
)
```

### 13.2 Testing Obligatorio

```python
# tests/integration/test_neo4j_vector_index.py
import pytest
from testcontainers.neo4j import Neo4jContainer

@pytest.fixture(scope="module")
def neo4j_container():
    with Neo4jContainer("neo4j:5.26") as neo4j:
        yield neo4j

def test_vector_index_creation(neo4j_container):
    driver = GraphDatabase.driver(neo4j_container.get_connection_url())
    create_vector_index(driver)
    # Assert index exists and is ONLINE
    result = driver.query("SHOW INDEXES WHERE name = 'stackoverflow'")
    assert result[0]["state"] == "ONLINE"
```

### 13.3 Configuration as Code

```python
# melquisedec/config.py
from pydantic import BaseSettings, Field

class MelquisedecConfig(BaseSettings):
    neo4j_uri: str = Field(..., env="NEO4J_URI")  # Required
    neo4j_username: str = Field("neo4j", env="NEO4J_USERNAME")
    neo4j_password: str = Field(..., env="NEO4J_PASSWORD")  # Required
    ollama_base_url: str = Field("http://localhost:11434", env="OLLAMA_BASE_URL")
    embedding_model: str = Field("qwen3-embedding", env="EMBEDDING_MODEL")
    embedding_dimension: int = Field(1536, env="EMBEDDING_DIMENSION")
    vector_index_name: str = Field("melquisedec_embeddings", env="VECTOR_INDEX_NAME")
    # HNSW configuration
    hnsw_m: int = Field(16, env="HNSW_M")  # Connections per layer
    hnsw_ef_construction: int = Field(64, env="HNSW_EF_CONSTRUCTION")  # Build time accuracy

    class Config:
        env_file = ".env"
```

### 13.4 Observability

```python
# melquisedec/observability.py
import structlog
from prometheus_client import Counter, Histogram

logger = structlog.get_logger()

# Métricas Prometheus
embedding_latency = Histogram("embedding_latency_seconds", "Embedding API latency")
vector_search_latency = Histogram("vector_search_latency_seconds", "Vector search latency")
rag_requests_total = Counter("rag_requests_total", "Total RAG requests", ["status"])

@embedding_latency.time()
async def embed_batch(texts: list[str]) -> list[list[float]]:
    logger.info("embedding_batch", num_texts=len(texts))
    try:
        embeddings = await ollama_client.embed_batch(texts)
        rag_requests_total.labels(status="success").inc()
        return embeddings
    except Exception as e:
        logger.error("embedding_failed", error=str(e))
        rag_requests_total.labels(status="error").inc()
        raise
```

---

## 14. Referencias Cruzadas

**Repositorio**:
- GitHub: https://github.com/docker/genai-stack
- Blog Walkthrough: https://neo4j.com/blog/developer/genai-app-how-to-build/
- Neo4j Labs: https://neo4j.com/labs/genai-ecosystem/genai-stack/
- Developer Guide: https://neo4j.com/developer/genai-ecosystem/genai-stack/

**Archivos Clave**:
- `docker-compose.yml`: Arquitectura multi-contenedor (5 apps + Neo4j + Ollama)
- `chains.py`: RAG pipeline con LangChain LCEL, custom retrieval query
- `loader.py`: Ingesta StackOverflow data con embeddings, constraints, índices
- `utils.py`: Schema creation (vector index, constraints), helpers
- `requirements.txt`: Dependencies (langchain-neo4j==0.4.0, langchain-ollama==0.2.3)

**Code Patterns Reutilizables**:
1. Adapter Pattern - Multi-Provider Embeddings
2. Idempotent Schema Creation
3. Embedding-First Cypher Ingestion
4. Custom Retrieval Query - Hybrid Vector+Graph
5. LangChain LCEL - Runnable Composition
6. Streaming SSE - FastAPI
7. Environment-Based Configuration

**Próximos Pasos en R1.2**:
- Analizar LlamaIndex Neo4j integration (alternativa a LangChain)
- Comparar `Neo4jVector` (LangChain) vs `Neo4jVectorStore` (LlamaIndex)
- Evaluar si LlamaIndex ofrece mejor abstracción para Hexagonal Architecture

---

**Document Metadata**:
- **Research Instance**: RI-MDA-002
- **Task**: R1.1 - GenAI Stack Architecture Analysis
- **Rostro**: HYPATIA (Researcher)
- **DSR Phase**: Problem Identification
- **Version**: 1.0.0
- **Date**: 2025-01-15
- **Lines**: 897
- **Status**: ✅ Completed
