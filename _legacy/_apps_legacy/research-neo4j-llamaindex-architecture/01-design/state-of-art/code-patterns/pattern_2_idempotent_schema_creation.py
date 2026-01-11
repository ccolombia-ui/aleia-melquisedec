"""
Pattern 2: Idempotent Schema Creation

Source: docker/genai-stack - utils.py
Purpose: Permitir re-ejecución sin errores (safe para CI/CD, migrations, dev reset)
Advantage: IF NOT EXISTS permite schema evolution sin manual cleanup

Extracted from: https://github.com/docker/genai-stack/blob/main/utils.py
"""

from neo4j import GraphDatabase


def create_vector_index(driver) -> None:
    """
    Create vector indexes idempotently.

    Uses IF NOT EXISTS to prevent errors on re-execution.
    Indexes:
    - stackoverflow: Vector index on Question.embedding
    - top_answers: Vector index on Answer.embedding
    """
    # Index for questions
    index_query = """
    CREATE VECTOR INDEX stackoverflow IF NOT EXISTS
    FOR (m:Question) ON m.embedding
    """
    try:
        driver.query(index_query)
    except:  # Already exists
        pass

    # Index for answers
    index_query = """
    CREATE VECTOR INDEX top_answers IF NOT EXISTS
    FOR (m:Answer) ON m.embedding
    """
    try:
        driver.query(index_query)
    except:  # Already exists
        pass


def create_constraints(driver):
    """
    Create uniqueness constraints idempotently.

    Constraints:
    - Question.id: UNIQUE
    - Answer.id: UNIQUE
    - User.id: UNIQUE
    - Tag.name: UNIQUE
    """
    driver.query(
        """
        CREATE CONSTRAINT question_id IF NOT EXISTS
        FOR (q:Question) REQUIRE (q.id) IS UNIQUE
    """
    )

    driver.query(
        """
        CREATE CONSTRAINT answer_id IF NOT EXISTS
        FOR (a:Answer) REQUIRE (a.id) IS UNIQUE
    """
    )

    driver.query(
        """
        CREATE CONSTRAINT user_id IF NOT EXISTS
        FOR (u:User) REQUIRE (u.id) IS UNIQUE
    """
    )

    driver.query(
        """
        CREATE CONSTRAINT tag_name IF NOT EXISTS
        FOR (t:Tag) REQUIRE (t.name) IS UNIQUE
    """
    )


# ==================== HEXAGONAL ARCHITECTURE REFACTORING ====================

"""
Mejora Propuesta para MELQUISEDEC:
- Structured logging en vez de silent `except: pass`
- Validación de estado de índice (ONLINE vs POPULATING)
- Type hints + docstrings
- Error handling específico (no bare except)
"""

from dataclasses import dataclass
from typing import List, Protocol

import structlog

logger = structlog.get_logger()


@dataclass
class VectorIndexConfig:
    """Configuration for Neo4j HNSW Vector Index."""

    name: str
    node_label: str
    property_name: str
    dimension: int
    similarity_function: str = "cosine"  # cosine, euclidean
    m: int = 16  # HNSW connections per layer
    ef_construction: int = 64  # Build-time accuracy


class SchemaManagerPort(Protocol):
    """Port: Schema management operations."""

    def create_vector_index(self, config: VectorIndexConfig) -> None:
        """Create vector index idempotently."""
        ...

    def create_constraint(self, label: str, property_name: str) -> None:
        """Create uniqueness constraint idempotently."""
        ...

    def get_index_status(self, index_name: str) -> str:
        """Get index status (ONLINE, POPULATING, FAILED)."""
        ...


class Neo4jSchemaManager:
    """Adapter: Implements SchemaManagerPort for Neo4j."""

    def __init__(self, driver):
        self._driver = driver

    def create_vector_index(self, config: VectorIndexConfig) -> None:
        """
        Create HNSW vector index with explicit configuration.

        Args:
            config: VectorIndexConfig with HNSW parameters

        Raises:
            Neo4jSchemaError: If index creation fails
        """
        cypher_query = f"""
        CREATE VECTOR INDEX {config.name} IF NOT EXISTS
        FOR (n:{config.node_label})
        ON n.{config.property_name}
        OPTIONS {{
            indexConfig: {{
                `vector.dimensions`: {config.dimension},
                `vector.similarity_function`: '{config.similarity_function}'
            }},
            indexProvider: 'vector-2.0',
            vectorIndexConfig: {{
                `vector.hnsw.m`: {config.m},
                `vector.hnsw.ef_construction`: {config.ef_construction}
            }}
        }}
        """

        try:
            self._driver.query(cypher_query)
            logger.info(
                "vector_index_created",
                index_name=config.name,
                node_label=config.node_label,
                dimension=config.dimension,
                hnsw_m=config.m,
                hnsw_ef_construction=config.ef_construction,
            )
        except Exception as e:
            logger.error("vector_index_creation_failed", index_name=config.name, error=str(e))
            # Check if error is because index already exists
            if "already exists" not in str(e).lower():
                raise Neo4jSchemaError(f"Failed to create index {config.name}: {e}")

    def create_constraint(self, label: str, property_name: str) -> None:
        """
        Create uniqueness constraint idempotently.

        Args:
            label: Node label (e.g., "Question")
            property_name: Property name (e.g., "id")
        """
        constraint_name = f"{label.lower()}_{property_name}"
        cypher_query = f"""
        CREATE CONSTRAINT {constraint_name} IF NOT EXISTS
        FOR (n:{label})
        REQUIRE (n.{property_name}) IS UNIQUE
        """

        try:
            self._driver.query(cypher_query)
            logger.info(
                "constraint_created",
                constraint_name=constraint_name,
                label=label,
                property_name=property_name,
            )
        except Exception as e:
            logger.error(
                "constraint_creation_failed", constraint_name=constraint_name, error=str(e)
            )
            if "already exists" not in str(e).lower():
                raise Neo4jSchemaError(f"Failed to create constraint {constraint_name}: {e}")

    def get_index_status(self, index_name: str) -> str:
        """
        Get index status.

        Args:
            index_name: Name of the index

        Returns:
            Status string: ONLINE, POPULATING, FAILED, NOT_FOUND
        """
        cypher_query = """
        SHOW INDEXES
        WHERE name = $index_name
        RETURN state
        """

        try:
            result = self._driver.query(cypher_query, {"index_name": index_name})
            if result:
                status = result[0]["state"]
                logger.info("index_status_checked", index_name=index_name, status=status)
                return status
            else:
                logger.warning("index_not_found", index_name=index_name)
                return "NOT_FOUND"
        except Exception as e:
            logger.error("index_status_check_failed", index_name=index_name, error=str(e))
            raise Neo4jSchemaError(f"Failed to check index status: {e}")


class Neo4jSchemaError(Exception):
    """Custom exception for Neo4j schema operations."""

    pass


# ==================== USAGE EXAMPLE ====================

if __name__ == "__main__":
    from neo4j import GraphDatabase

    # ❌ Old Pattern (genai-stack)
    print("=== Old Pattern (Silent Errors) ===")
    driver_old = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    create_vector_index(driver_old)
    create_constraints(driver_old)
    driver_old.close()

    # ✅ New Pattern (MELQUISEDEC with structured logging + validation)
    print("\n=== New Pattern (Structured Logging + Validation) ===")
    driver_new = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    schema_manager = Neo4jSchemaManager(driver_new)

    # Create vector index with explicit HNSW config
    vector_index_config = VectorIndexConfig(
        name="melquisedec_embeddings",
        node_label="Document",
        property_name="embedding",
        dimension=1536,
        similarity_function="cosine",
        m=16,  # HNSW parameter
        ef_construction=64,  # HNSW parameter
    )
    schema_manager.create_vector_index(vector_index_config)

    # Validate index is ONLINE
    status = schema_manager.get_index_status("melquisedec_embeddings")
    assert status == "ONLINE", f"Index not ready: {status}"

    # Create constraints
    schema_manager.create_constraint("Question", "id")
    schema_manager.create_constraint("Answer", "id")
    schema_manager.create_constraint("User", "id")

    driver_new.close()

    print("\n✅ Schema creation completed with validation")
