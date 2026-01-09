"""
Pattern 1: Adapter Pattern - Multi-Provider Embeddings

Source: docker/genai-stack - chains.py
Purpose: Normalizar interfaz de diferentes providers de embeddings
Advantage: Cambiar provider con 1 variable de entorno

Extracted from: https://github.com/docker/genai-stack/blob/main/chains.py
"""

from typing import Any, Tuple

from langchain_aws import BedrockEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings


def load_embedding_model(embedding_model_name: str, config: dict = {}) -> Tuple[Any, int]:
    """
    Load embedding model based on provider name.

    Args:
        embedding_model_name: Provider name (ollama, openai, aws, google-genai-embedding-001)
        config: Configuration dict with provider-specific settings

    Returns:
        Tuple[embeddings_instance, dimension]

    Supported Providers:
        - ollama: Local LLM embeddings (4096 dimensions)
        - openai: OpenAI text-embedding-ada-002 (1536 dimensions)
        - aws: AWS Bedrock Titan Embeddings (1536 dimensions)
        - google-genai-embedding-001: Google Generative AI (768 dimensions)
        - (default): HuggingFace all-MiniLM-L6-v2 (384 dimensions)
    """
    if embedding_model_name == "ollama":
        embeddings = OllamaEmbeddings(
            base_url=config.get("ollama_base_url", "http://localhost:11434"), model="llama2"
        )
        dimension = 4096
        print("Embedding: Using Ollama")

    elif embedding_model_name == "openai":
        embeddings = OpenAIEmbeddings()
        dimension = 1536
        print("Embedding: Using OpenAI")

    elif embedding_model_name == "aws":
        embeddings = BedrockEmbeddings()
        dimension = 1536
        print("Embedding: Using AWS Bedrock")

    elif embedding_model_name == "google-genai-embedding-001":
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        dimension = 768
        print("Embedding: Using Google Generative AI Embeddings")

    else:  # Default: HuggingFace
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2", cache_folder="/embedding_model"
        )
        dimension = 384
        print("Embedding: Using SentenceTransformer (HuggingFace)")

    return embeddings, dimension


# ==================== HEXAGONAL ARCHITECTURE REFACTORING ====================

"""
Mejora Propuesta para MELQUISEDEC:
Usar protocolo EmbeddingPort en vez de if/elif gigante

Benefits:
- Type safety con mypy
- Dependency Injection (IoC)
- Testeable con mocks (no need for real Ollama/OpenAI)
- Open/Closed Principle (add new providers sin modificar código existente)
"""

from typing import List, Protocol


class EmbeddingPort(Protocol):
    """Port: Abstracción de embedding service."""

    @property
    def dimension(self) -> int:
        """Dimensión del vector embedding."""
        ...

    def embed_query(self, text: str) -> List[float]:
        """Genera embedding para una query única."""
        ...

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Genera embeddings para múltiples documentos (batch)."""
        ...


class OllamaEmbeddingAdapter:
    """Adapter: Implementa EmbeddingPort para Ollama."""

    def __init__(self, base_url: str, model: str = "llama2"):
        from langchain_ollama import OllamaEmbeddings

        self._embeddings = OllamaEmbeddings(base_url=base_url, model=model)
        self._dimension = 4096

    @property
    def dimension(self) -> int:
        return self._dimension

    def embed_query(self, text: str) -> List[float]:
        return self._embeddings.embed_query(text)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embeddings.embed_documents(texts)


class OpenAIEmbeddingAdapter:
    """Adapter: Implementa EmbeddingPort para OpenAI."""

    def __init__(self, api_key: str = None):
        from langchain_openai import OpenAIEmbeddings

        self._embeddings = OpenAIEmbeddings(api_key=api_key)
        self._dimension = 1536

    @property
    def dimension(self) -> int:
        return self._dimension

    def embed_query(self, text: str) -> List[float]:
        return self._embeddings.embed_query(text)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embeddings.embed_documents(texts)


class EmbeddingFactory:
    """Factory: Crea adapter basado en configuración."""

    @staticmethod
    def create(provider: str, config: dict) -> EmbeddingPort:
        """
        Create embedding adapter based on provider name.

        Args:
            provider: Provider name (ollama, openai, qwen3)
            config: Provider-specific configuration

        Returns:
            EmbeddingPort implementation

        Raises:
            ValueError: If provider not supported
        """
        if provider == "ollama":
            return OllamaEmbeddingAdapter(
                base_url=config.get("ollama_base_url", "http://localhost:11434"),
                model=config.get("model", "llama2"),
            )
        elif provider == "openai":
            return OpenAIEmbeddingAdapter(api_key=config.get("openai_api_key"))
        # Add more providers as needed: qwen3, aws, google, etc.
        else:
            raise ValueError(f"Unsupported embedding provider: {provider}")


# ==================== USAGE EXAMPLE ====================

if __name__ == "__main__":
    # ❌ Old Pattern (genai-stack)
    embeddings_old, dimension_old = load_embedding_model(
        embedding_model_name="ollama", config={"ollama_base_url": "http://localhost:11434"}
    )
    print(f"Old Pattern: dimension={dimension_old}")

    # ✅ New Pattern (MELQUISEDEC Hexagonal Architecture)
    embedding_service: EmbeddingPort = EmbeddingFactory.create(
        provider="ollama", config={"ollama_base_url": "http://localhost:11434", "model": "qwen3"}
    )
    print(f"New Pattern: dimension={embedding_service.dimension}")

    # Dependency Injection Example
    def process_documents(texts: List[str], embedding_service: EmbeddingPort):
        """Business logic no depende de Ollama/OpenAI específico."""
        embeddings = embedding_service.embed_documents(texts)
        print(f"Processed {len(embeddings)} embeddings")
        return embeddings

    # Testeable con mock
    class MockEmbeddingService:
        @property
        def dimension(self) -> int:
            return 128

        def embed_query(self, text: str) -> List[float]:
            return [0.1] * 128

        def embed_documents(self, texts: List[str]) -> List[List[float]]:
            return [[0.1] * 128 for _ in texts]

    # Test sin llamar a Ollama/OpenAI real
    process_documents(["test1", "test2"], MockEmbeddingService())
