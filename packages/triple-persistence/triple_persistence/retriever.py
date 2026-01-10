"""
Triple Persistence Hybrid Retriever

Combines vector similarity search with graph traversal for enriched results.
"""

from time import time
from typing import Any, Dict, List, Optional

# Optional imports: tests use mocks and don't require heavy dependencies
try:
    from llama_index.core import VectorStoreIndex
    from llama_index.core.schema import NodeWithScore, TextNode
except Exception:
    VectorStoreIndex = None
    NodeWithScore = None
    TextNode = None

try:
    from neo4j import GraphDatabase
except Exception:
    GraphDatabase = None

from .models import QueryRequest, QueryResponse, QueryResult


class HybridRetriever:
    """
    Hybrid retriever combining:
    1. Vector similarity search (semantic)
    2. Graph traversal (structural relationships)
    3. BM25 keyword search (lexical)
    """

    def __init__(self, index: VectorStoreIndex, neo4j_driver: Any, project: str = "default"):
        """
        Initialize hybrid retriever.

        Args:
            index: LlamaIndex VectorStoreIndex
            neo4j_driver: Neo4j driver instance
            project: Project identifier
        """
        self.index = index
        self.driver = neo4j_driver
        self.project = project
        self.query_engine = index.as_query_engine(similarity_top_k=50)

    def query(self, request: QueryRequest) -> QueryResponse:
        """
        Execute hybrid query combining vector search and graph traversal.

        Args:
            request: QueryRequest with query text and parameters

        Returns:
            QueryResponse with ranked results
        """
        start_time = time()

        print(f"\n🔍 Query: {request.query}")
        print(f"   Top-K: {request.top_k}")
        print(f"   Include Graph: {request.include_graph}")

        # Step 1: Vector similarity search
        vector_results = self._vector_search(request.query, request.top_k * 2)
        print(f"   📊 Vector results: {len(vector_results)}")

        # Step 2: Group by document and calculate document-level scores
        doc_results = self._group_by_document(vector_results)
        print(f"   📄 Unique documents: {len(doc_results)}")

        # Step 3: Enrich with graph relationships (if enabled)
        if request.include_graph:
            doc_results = self._enrich_with_graph(doc_results, request.top_k)
            print(f"   🔗 Graph-enriched documents: {len(doc_results)}")

        # Step 4: Apply filters
        if request.filters:
            doc_results = self._apply_filters(doc_results, request.filters)
            print(f"   🔍 Filtered documents: {len(doc_results)}")

        # Step 5: Rank and limit
        final_results = sorted(doc_results, key=lambda x: x.similarity, reverse=True)[
            : request.top_k
        ]

        query_time_ms = (time() - start_time) * 1000

        print(f"   ⏱️  Query time: {query_time_ms:.2f}ms")

        return QueryResponse(
            results=final_results, query_time_ms=query_time_ms, total_results=len(final_results)
        )

    def _vector_search(self, query: str, top_k: int) -> List[NodeWithScore]:
        """
        Perform vector similarity search.

        Args:
            query: Query text
            top_k: Number of results to retrieve

        Returns:
            List of NodeWithScore from LlamaIndex
        """
        retriever = self.index.as_retriever(similarity_top_k=top_k)
        nodes = retriever.retrieve(query)
        return nodes

    def _group_by_document(self, nodes: List[NodeWithScore]) -> List[QueryResult]:
        """
        Group chunks by document and aggregate scores.

        Takes the best chunk per document and creates QueryResult objects.

        Args:
            nodes: List of NodeWithScore from vector search

        Returns:
            List of QueryResult grouped by document
        """
        doc_map: Dict[str, QueryResult] = {}

        for node in nodes:
            # Extract document info from node metadata
            doc_id = node.node.metadata.get("document_id", "unknown")
            doc_path = node.node.metadata.get("file_path", "unknown")

            # Get or create QueryResult for this document
            if doc_id not in doc_map:
                doc_map[doc_id] = QueryResult(
                    document_id=doc_id,
                    document_path=doc_path,
                    similarity=node.score or 0.0,
                    excerpt=node.node.get_content(),
                    related_documents=[],
                    metadata=node.node.metadata,
                )
            else:
                # Keep highest scoring chunk
                if node.score and node.score > doc_map[doc_id].similarity:
                    doc_map[doc_id].similarity = node.score
                    doc_map[doc_id].excerpt = node.node.get_content()

        return list(doc_map.values())

    def _enrich_with_graph(
        self, results: List[QueryResult], max_related: int = 5
    ) -> List[QueryResult]:
        """
        Enrich results with graph relationships.

        For each result, find related documents via:
        - :REFERENCES relationships
        - :TAGGED_WITH common tags
        - :BELONGS_TO same phase

        Args:
            results: List of QueryResult
            max_related: Maximum related documents per result

        Returns:
            Enriched QueryResult list
        """
        with self.driver.session() as session:
            for result in results:
                # Find related documents
                query = """
                MATCH (d:Document {id: $doc_id})

                // Direct references
                OPTIONAL MATCH (d)-[:REFERENCES]->(ref:Document)

                // Reverse references
                OPTIONAL MATCH (d)<-[:REFERENCES]-(rev:Document)

                // Same tags
                OPTIONAL MATCH (d)-[:TAGGED_WITH]->(t:Tag)<-[:TAGGED_WITH]-(tagged:Document)

                // Same phase
                OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Phase)<-[:BELONGS_TO]-(phase_doc:Document)

                WITH d,
                     collect(DISTINCT ref.id) as refs,
                     collect(DISTINCT rev.id) as revs,
                     collect(DISTINCT tagged.id) as tags,
                     collect(DISTINCT phase_doc.id) as phases

                WITH d,
                     refs + revs + tags + phases as all_related

                UNWIND all_related as related_id
                WITH d, related_id
                WHERE related_id IS NOT NULL AND related_id <> d.id

                MATCH (related:Document {id: related_id})

                RETURN DISTINCT related.id as id,
                       related.path as path,
                       related.title as title
                LIMIT $max_related
                """

                related = session.run(
                    query, doc_id=result.document_id, max_related=max_related
                ).data()

                # Add related document IDs to result
                result.related_documents = [r["id"] for r in related]

                # Boost similarity score if there are many related docs
                if len(result.related_documents) > 0:
                    boost = min(0.1, len(result.related_documents) * 0.02)
                    result.similarity += boost

        return results

    def _apply_filters(
        self, results: List[QueryResult], filters: Dict[str, Any]
    ) -> List[QueryResult]:
        """
        Apply filters to results.

        Supported filters:
        - type: Document type
        - rostro: Rostro name
        - phase: Phase name
        - tags: List of required tags

        Args:
            results: List of QueryResult
            filters: Dict of filter conditions

        Returns:
            Filtered QueryResult list
        """
        with self.driver.session() as session:
            filtered = []

            for result in results:
                # Check if document matches all filters
                match = True

                if "type" in filters:
                    doc_type = session.run(
                        "MATCH (d:Document {id: $doc_id}) RETURN d.type as type",
                        doc_id=result.document_id,
                    ).single()
                    if not doc_type or doc_type["type"] != filters["type"]:
                        match = False

                if "rostro" in filters and match:
                    has_rostro = session.run(
                        """
                        MATCH (d:Document {id: $doc_id})-[:CREATED_BY]->(r:Rostro {name: $rostro})
                        RETURN count(*) as count
                        """,
                        doc_id=result.document_id,
                        rostro=filters["rostro"],
                    ).single()
                    if not has_rostro or has_rostro["count"] == 0:
                        match = False

                if "phase" in filters and match:
                    has_phase = session.run(
                        """
                        MATCH (d:Document {id: $doc_id})-[:BELONGS_TO]->(p:Phase {name: $phase})
                        RETURN count(*) as count
                        """,
                        doc_id=result.document_id,
                        phase=filters["phase"],
                    ).single()
                    if not has_phase or has_phase["count"] == 0:
                        match = False

                if "tags" in filters and match:
                    required_tags = filters["tags"]
                    if isinstance(required_tags, str):
                        required_tags = [required_tags]

                    for tag in required_tags:
                        has_tag = session.run(
                            """
                            MATCH (d:Document {id: $doc_id})-[:TAGGED_WITH]->(t:Tag {name: $tag})
                            RETURN count(*) as count
                            """,
                            doc_id=result.document_id,
                            tag=tag,
                        ).single()
                        if not has_tag or has_tag["count"] == 0:
                            match = False
                            break

                if match:
                    filtered.append(result)

        return filtered

    def get_document_context(self, document_id: str) -> Dict[str, Any]:
        """
        Get full context for a document including all relationships.

        Args:
            document_id: Document ID

        Returns:
            Dict with document info and all relationships
        """
        with self.driver.session() as session:
            # Get document node
            doc = session.run(
                """
                MATCH (d:Document {id: $doc_id})
                RETURN d
                """,
                doc_id=document_id,
            ).single()

            if not doc:
                return {}

            doc_data = dict(doc["d"])

            # Get all relationships
            relationships = session.run(
                """
                MATCH (d:Document {id: $doc_id})

                OPTIONAL MATCH (d)-[:REFERENCES]->(ref:Document)
                OPTIONAL MATCH (d)<-[:REFERENCES]-(rev:Document)
                OPTIONAL MATCH (d)-[:TAGGED_WITH]->(t:Tag)
                OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Phase)
                OPTIONAL MATCH (d)-[:CREATED_BY]->(r:Rostro)

                RETURN collect(DISTINCT {id: ref.id, title: ref.title}) as references,
                       collect(DISTINCT {id: rev.id, title: rev.title}) as referenced_by,
                       collect(DISTINCT t.name) as tags,
                       p.name as phase,
                       r.name as rostro
                """,
                doc_id=document_id,
            ).single()

            return {
                "document": doc_data,
                "references": relationships["references"] if relationships else [],
                "referenced_by": relationships["referenced_by"] if relationships else [],
                "tags": relationships["tags"] if relationships else [],
                "phase": relationships["phase"] if relationships else None,
                "rostro": relationships["rostro"] if relationships else None,
            }

    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the knowledge base.

        Returns:
            Dict with counts and metrics
        """
        with self.driver.session() as session:
            stats = session.run(
                """
                MATCH (d:Document)
                OPTIONAL MATCH (c:Chunk)
                OPTIONAL MATCH (t:Tag)
                OPTIONAL MATCH (p:Phase)
                OPTIONAL MATCH (r:Rostro)
                OPTIONAL MATCH ()-[rel:REFERENCES]->()

                RETURN count(DISTINCT d) as documents,
                       count(DISTINCT c) as chunks,
                       count(DISTINCT t) as tags,
                       count(DISTINCT p) as phases,
                       count(DISTINCT r) as rostros,
                       count(rel) as references
            """
            ).single()

            return dict(stats) if stats else {}
