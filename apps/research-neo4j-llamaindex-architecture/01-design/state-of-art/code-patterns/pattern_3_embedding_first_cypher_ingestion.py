"""
Pattern 3: Embedding-First Cypher Ingestion

Source: docker/genai-stack - loader.py
Purpose: Calcular embeddings en Python app layer, luego ingestar en Neo4j con Cypher
Advantage: Flexible (cualquier modelo de embeddings), Neo4j no necesita embedding API

Extracted from: https://github.com/docker/genai-stack/blob/main/loader.py
"""

from typing import Any, Dict, List


def insert_so_data_old_pattern(data: dict, embeddings, neo4j_graph) -> None:
    """
    Old Pattern from genai-stack: Synchronous embeddings + batch Cypher.

    Issues:
    - Synchronous embeddings (bloquea thread)
    - No error handling
    - Sin cache (recalcula en cada ingesta)
    - Sin batch processing (1 embedding = 1 HTTP call)
    """
    # Calculate embeddings for questions and answers
    for q in data["items"]:
        question_text = q["title"] + "\n" + q["body_markdown"]
        q["embedding"] = embeddings.embed_query(question_text)
        for a in q["answers"]:
            a["embedding"] = embeddings.embed_query(question_text + "\n" + a["body_markdown"])

    # Cypher ingestion with embeddings as array
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
        question.embedding = q.embedding
    FOREACH (tagName IN q.tags |
        MERGE (tag:Tag {name:tagName})
        MERGE (question)-[:TAGGED]->(tag)
    )
    FOREACH (a IN q.answers |
        MERGE (question)<-[:ANSWERS]-(answer:Answer {id:a.answer_id})
        SET
            answer.is_accepted = a.is_accepted,
            answer.score = a.score,
            answer.creation_date = datetime({epochSeconds:a.creation_date}),
            answer.body = a.body_markdown,
            answer.embedding = a.embedding
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


# ==================== HEXAGONAL ARCHITECTURE REFACTORING ====================

"""
Mejora Propuesta para MELQUISEDEC:
- Async embeddings (no bloquea thread)
- Batch processing (reduce HTTP calls)
- Redis cache (no recalcula embeddings)
- Error handling con retry
- Structured logging
- Type hints + protocols
"""

import asyncio
from dataclasses import dataclass
from typing import Any, Dict, List, Protocol

import structlog
from tenacity import retry, stop_after_attempt, wait_exponential

logger = structlog.get_logger()


@dataclass
class QuestionData:
    """Domain Entity: Question."""

    id: str
    title: str
    body: str
    link: str
    score: int
    tags: List[str]
    answers: List["AnswerData"]
    embedding: List[float] = None


@dataclass
class AnswerData:
    """Domain Entity: Answer."""

    id: str
    body: str
    is_accepted: bool
    score: int
    user_id: str
    embedding: List[float] = None


class EmbeddingServicePort(Protocol):
    """Port: Embedding service abstraction."""

    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts (async batch)."""
        ...


class CachePort(Protocol):
    """Port: Cache abstraction."""

    async def get(self, key: str) -> List[float] | None:
        """Get embedding from cache."""
        ...

    async def set(self, key: str, value: List[float], ttl: int = 3600) -> None:
        """Set embedding in cache with TTL."""
        ...


class GraphRepositoryPort(Protocol):
    """Port: Graph repository abstraction."""

    async def ingest_questions(self, questions: List[QuestionData]) -> None:
        """Ingest questions with embeddings into Neo4j."""
        ...


class AsyncOllamaEmbeddingAdapter:
    """Adapter: Async Ollama embeddings with batch support."""

    def __init__(self, base_url: str, model: str = "qwen3-embedding"):
        import httpx

        self._client = httpx.AsyncClient(base_url=base_url, timeout=30.0)
        self._model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for batch of texts.

        Uses Ollama batch API to reduce HTTP calls.
        Implements retry with exponential backoff.
        """
        logger.info("embedding_batch_started", num_texts=len(texts), model=self._model)

        try:
            response = await self._client.post(
                "/api/embeddings", json={"model": self._model, "prompt": texts}  # Ollama batch API
            )
            response.raise_for_status()
            embeddings = response.json()["embeddings"]

            logger.info(
                "embedding_batch_completed", num_texts=len(texts), dimension=len(embeddings[0])
            )
            return embeddings

        except Exception as e:
            logger.error("embedding_batch_failed", num_texts=len(texts), error=str(e))
            raise


class RedisCacheAdapter:
    """Adapter: Redis cache for embeddings."""

    def __init__(self, redis_url: str):
        import redis.asyncio as redis

        self._redis = redis.from_url(redis_url)

    async def get(self, key: str) -> List[float] | None:
        """Get embedding from Redis cache."""
        import json

        value = await self._redis.get(f"embedding:{key}")
        if value:
            logger.debug("cache_hit", key=key)
            return json.loads(value)
        logger.debug("cache_miss", key=key)
        return None

    async def set(self, key: str, value: List[float], ttl: int = 3600) -> None:
        """Set embedding in Redis cache with 1h TTL."""
        import json

        await self._redis.setex(f"embedding:{key}", ttl, json.dumps(value))
        logger.debug("cache_set", key=key, ttl=ttl)


class Neo4jGraphRepository:
    """Adapter: Neo4j graph repository for questions."""

    def __init__(self, driver):
        self._driver = driver

    async def ingest_questions(self, questions: List[QuestionData]) -> None:
        """
        Ingest questions with embeddings using MERGE (idempotent).

        Uses UNWIND for batch processing.
        """
        data = [
            {
                "question_id": q.id,
                "title": q.title,
                "body": q.body,
                "link": q.link,
                "score": q.score,
                "tags": q.tags,
                "embedding": q.embedding,
                "answers": [
                    {
                        "answer_id": a.id,
                        "body": a.body,
                        "is_accepted": a.is_accepted,
                        "score": a.score,
                        "user_id": a.user_id,
                        "embedding": a.embedding,
                    }
                    for a in q.answers
                ],
            }
            for q in questions
        ]

        cypher_query = """
        UNWIND $data AS q
        MERGE (question:Question {id:q.question_id})
        ON CREATE SET
            question.title = q.title,
            question.body = q.body,
            question.link = q.link,
            question.score = q.score,
            question.embedding = q.embedding
        FOREACH (tagName IN q.tags |
            MERGE (tag:Tag {name:tagName})
            MERGE (question)-[:TAGGED]->(tag)
        )
        FOREACH (a IN q.answers |
            MERGE (question)<-[:ANSWERS]-(answer:Answer {id:a.answer_id})
            SET
                answer.body = a.body,
                answer.is_accepted = a.is_accepted,
                answer.score = a.score,
                answer.embedding = a.embedding
            MERGE (answerer:User {id:a.user_id})
            MERGE (answer)<-[:PROVIDED]-(answerer)
        )
        """

        try:
            self._driver.query(cypher_query, {"data": data})
            logger.info("questions_ingested", num_questions=len(questions))
        except Exception as e:
            logger.error("questions_ingestion_failed", error=str(e))
            raise


class QuestionIngestionService:
    """Application Service: Orchestrates embedding + ingestion with cache."""

    def __init__(
        self,
        embedding_service: EmbeddingServicePort,
        cache: CachePort,
        graph_repository: GraphRepositoryPort,
    ):
        self._embedding_service = embedding_service
        self._cache = cache
        self._graph_repository = graph_repository

    async def ingest_questions(self, raw_questions: List[Dict[str, Any]]) -> None:
        """
        Ingest questions with cached embeddings.

        Steps:
        1. Check cache for existing embeddings
        2. Generate missing embeddings in batch
        3. Store embeddings in cache
        4. Ingest into Neo4j
        """
        questions: List[QuestionData] = []

        for q_raw in raw_questions:
            # Parse question
            question_text = f"{q_raw['title']}\n{q_raw['body_markdown']}"

            # Check cache for question embedding
            question_embedding = await self._cache.get(question_text)
            if not question_embedding:
                # Will generate later in batch
                question_embedding = None

            # Parse answers
            answers: List[AnswerData] = []
            for a_raw in q_raw.get("answers", []):
                answer_text = f"{question_text}\n{a_raw['body_markdown']}"
                answer_embedding = await self._cache.get(answer_text)
                if not answer_embedding:
                    answer_embedding = None

                answers.append(
                    AnswerData(
                        id=a_raw["answer_id"],
                        body=a_raw["body_markdown"],
                        is_accepted=a_raw["is_accepted"],
                        score=a_raw["score"],
                        user_id=a_raw.get("owner", {}).get("user_id", "deleted"),
                        embedding=answer_embedding,
                    )
                )

            questions.append(
                QuestionData(
                    id=q_raw["question_id"],
                    title=q_raw["title"],
                    body=q_raw["body_markdown"],
                    link=q_raw["link"],
                    score=q_raw["score"],
                    tags=q_raw["tags"],
                    answers=answers,
                    embedding=question_embedding,
                )
            )

        # Batch generate missing embeddings
        texts_to_embed = []
        text_to_entity = {}

        for q in questions:
            question_text = f"{q.title}\n{q.body}"
            if q.embedding is None:
                texts_to_embed.append(question_text)
                text_to_entity[question_text] = ("question", q)

            for a in q.answers:
                answer_text = f"{question_text}\n{a.body}"
                if a.embedding is None:
                    texts_to_embed.append(answer_text)
                    text_to_entity[answer_text] = ("answer", a)

        if texts_to_embed:
            logger.info("generating_missing_embeddings", count=len(texts_to_embed))
            embeddings = await self._embedding_service.embed_batch(texts_to_embed)

            # Assign embeddings and cache
            for text, embedding in zip(texts_to_embed, embeddings):
                entity_type, entity = text_to_entity[text]
                entity.embedding = embedding
                await self._cache.set(text, embedding)

        # Ingest into Neo4j
        await self._graph_repository.ingest_questions(questions)


# ==================== USAGE EXAMPLE ====================


async def main():
    # Setup dependencies
    embedding_service = AsyncOllamaEmbeddingAdapter(
        base_url="http://localhost:11434", model="qwen3-embedding"
    )
    cache = RedisCacheAdapter(redis_url="redis://localhost:6379")
    graph_repository = Neo4jGraphRepository(
        driver=None  # GraphDatabase.driver("bolt://localhost:7687", ...)
    )

    # Application Service
    ingestion_service = QuestionIngestionService(
        embedding_service=embedding_service, cache=cache, graph_repository=graph_repository
    )

    # Simulate StackOverflow API response
    raw_questions = [
        {
            "question_id": "123",
            "title": "How to use Neo4j Vector Index?",
            "body_markdown": "I want to store embeddings in Neo4j 5.15+...",
            "link": "https://stackoverflow.com/q/123",
            "score": 42,
            "tags": ["neo4j", "vector-index"],
            "answers": [
                {
                    "answer_id": "456",
                    "body_markdown": "You can use CREATE VECTOR INDEX...",
                    "is_accepted": True,
                    "score": 50,
                    "owner": {"user_id": "789"},
                }
            ],
        }
    ]

    # Ingest with cache + batch embeddings
    await ingestion_service.ingest_questions(raw_questions)
    print("✅ Ingestion completed with cached embeddings + batch processing")


if __name__ == "__main__":
    asyncio.run(main())
