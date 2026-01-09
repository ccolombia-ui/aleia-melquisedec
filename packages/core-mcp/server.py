"""
Servidor MCP ligero: Nucleo-Ligero
Uso: Ollama solo para embeddings (modelo configurable por EMBEDDING_MODEL)
"""

import logging
import math
import os
import time
from typing import Any, Dict, List, Optional

import ollama
import requests
from mcp.server.fastmcp import FastMCP
from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable

# Logging minimalista y útil
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("nucleo-ligero")

# Configuración por entorno
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password123")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")

# Instancia MCP
mcp = FastMCP("Nucleo-Ligero")

# Conectar a Neo4j con reintentos cortos (eficiente)


def conectar_neo4j(max_intentos: int = 20, espera: float = 1.5):
    for intento in range(1, max_intentos + 1):
        try:
            logger.info(f"Conectando a Neo4j ({intento}/{max_intentos})...")
            driver = GraphDatabase.driver(NEO4J_URI, auth=("neo4j", NEO4J_PASSWORD))
            with driver.session() as s:
                s.run("RETURN 1")
            logger.info("Conexión a Neo4j establecida")
            return driver
        except (ServiceUnavailable, AuthError) as e:
            logger.warning(f"Neo4j no listo: {e}")
            time.sleep(espera)
    raise RuntimeError("No se pudo conectar a Neo4j después de varios intentos")


neo4j_driver = conectar_neo4j()

# Función eficiente para solicitar embeddings a Ollama, con manejo de modelo faltante


def obtener_embedding(texto: str) -> List[float]:
    texto = texto or ""
    try:
        # Llamada directa a Ollama para embeddings
        resp = ollama.embeddings(model=EMBEDDING_MODEL, prompt=texto)
        # Normalmente resp puede ser dict con 'embedding'
        if isinstance(resp, dict) and "embedding" in resp:
            return resp["embedding"]
        # Si la librería devuelve lista directa
        if isinstance(resp, list):
            return resp
        raise RuntimeError("Respuesta inesperada de Ollama para embeddings")

    except Exception as e:
        # Intentar detectar error de modelo no encontrado y hacer pull
        err = str(e)
        logger.warning(f"Error embeddings ({EMBEDDING_MODEL}): {err}")
        try:
            logger.info(f"Intentando pull del modelo de embeddings: {EMBEDDING_MODEL}")
            # Algunos clientes Ollama soportan pull; si falla, capturamos
            ollama.pull(EMBEDDING_MODEL)
            # Reintentar una vez
            resp = ollama.embeddings(model=EMBEDDING_MODEL, prompt=texto)
            if isinstance(resp, dict) and "embedding" in resp:
                return resp["embedding"]
            if isinstance(resp, list):
                return resp
        except Exception as e2:
            logger.error(f"No se pudo obtener embeddings: {e2}")
            raise RuntimeError(f"Fallo al obtener embeddings desde Ollama: {e2}")


# Función ligera para extraer contenido (Firecrawl si disponible, else requests)


def extraer_contenido(url: str) -> str:
    if FIRECRAWL_API_KEY:
        try:
            from firecrawl import FirecrawlApp

            app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
            out = app.scrape_url(url)
            return out.get("content", "")
        except Exception as e:
            logger.warning(f"Firecrawl falló, simulando extracción: {e}")
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        return r.text[:2000]
    except Exception as e:
        logger.warning(f"No se pudo descargar {url}: {e}")
        return f"Contenido simulado de {url}"


# Guardar documento en Neo4j (propiedades ligeras)


def guardar_documento_neo4j(url: str, contenido: str, embedding: List[float]) -> str:
    with neo4j_driver.session() as s:
        result = s.run(
            "MERGE (d:Documento {url:$url}) SET d.contenido = $contenido, d.embedding = $embedding, d.creado = datetime() RETURN id(d) AS id",
            url=url,
            contenido=contenido[:1500],
            embedding=embedding,
        )
        rec = result.single()
        return str(rec["id"]) if rec else "-"


# Utilitario de similitud coseno


def cos_sim(a: List[float], b: List[float]) -> float:
    if not a or not b or len(a) != len(b):
        return -1.0
    num = sum(x * y for x, y in zip(a, b))
    sa = math.sqrt(sum(x * x for x in a))
    sb = math.sqrt(sum(y * y for y in b))
    if sa == 0 or sb == 0:
        return -1.0
    return num / (sa * sb)


# Herramientas MCP


@mcp.tool()
def ingestar_documento(url: str) -> str:
    """Ingesta documento: extrae contenido, vectoriza con Ollama (embeddings) y guarda en Neo4j."""
    try:
        logger.info(f"Ingestando: {url}")
        contenido = extraer_contenido(url)
        # Usar solo una porción para embeddings (eficiencia)
        texto_para_embed = contenido[:1024]
        embedding = obtener_embedding(texto_para_embed)
        doc_id = guardar_documento_neo4j(url, contenido, embedding)
        return f"Documento guardado: {doc_id}"
    except Exception as e:
        logger.error(f"Error ingestar_documento: {e}")
        return f"Error: {e}"


@mcp.tool()
def busqueda_semantica(query: str, top_k: int = 5) -> str:
    """Vectoriza la query y realiza búsqueda semántica sobre embeddings guardados (simulado)."""
    try:
        q_emb = obtener_embedding(query)
        with neo4j_driver.session() as s:
            # Recuperar candidatos con embeddings (simulación de índice vectorial)
            rows = s.run(
                "MATCH (d:Documento) WHERE exists(d.embedding) RETURN d.url AS url, d.contenido AS contenido, d.embedding AS embedding LIMIT 500"
            )
            candidatos = []
            for r in rows:
                emb = r["embedding"]
                if not isinstance(emb, list):
                    continue
                score = cos_sim(q_emb, emb)
                candidatos.append(
                    {"url": r["url"], "contenido": r["contenido"][:400], "score": score}
                )
            candidatos.sort(key=lambda x: x["score"], reverse=True)
            top = [c for c in candidatos if c["score"] > 0][:top_k]
            if not top:
                return "No se encontraron resultados similares."
            out = "Resultados semánticos:\n"
            for i, c in enumerate(top, 1):
                out += f"{i}. {c['url']} (score={c['score']:.4f})\n   {c['contenido']}\n\n"
            return out
    except Exception as e:
        logger.error(f"Error busqueda_semantica: {e}")
        return f"Error: {e}"


# Inicializar índices mínimos


def inicializar_indices():
    try:
        with neo4j_driver.session() as s:
            s.run("CREATE INDEX documento_url IF NOT EXISTS FOR (d:Documento) ON (d.url)")
            logger.info("Índices inicializados")
    except Exception as e:
        logger.warning(f"No se pudieron crear índices: {e}")


if __name__ == "__main__":
    logger.info("Iniciando Nucleo-Ligero (embeddings solo)")
    inicializar_indices()
    mcp.run()
