"""
Domain-Aware Vector Store para Autopoiesis

Gestión de vectores organizados por:
- Domain ID (DD-001, DD-002, etc.)
- Instance ID dentro del domain
- Artifact type (concept, analysis, output, lesson)

Uso:
    store = DomainAwareVectorStore("melquisedec-knowledge")
    
    # Insertar artifact
    store.upsert_artifact(
        domain_id="DD-001",
        instance_id="I001",
        artifact_id="concept-crisp-dm",
        artifact_type="concept",
        text="CRISP-DM is a data mining methodology...",
        metadata={"version": "1.0.0"}
    )
    
    # Buscar en domain
    results = store.search_in_domain(
        query="data mining methodology",
        domain_id="DD-001",
        top_k=5
    )
"""

from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from typing import List, Dict, Optional, Literal
import os
from datetime import datetime


class DomainAwareVectorStore:
    """
    Vector store con organización por dominios y instances.
    
    Estructura de namespaces:
        {domain_id}.{instance_id}
        
    Ejemplos:
        DD-001.global          # Conocimiento general del domain
        DD-001.I001            # Instance 001 de domain DD-001
        DD-001.I001.lessons    # Lessons de instance 001
    """
    
    def __init__(
        self,
        index_name: str = "melquisedec-knowledge",
        dimension: int = 1536,  # text-embedding-ada-002
        metric: str = "cosine"
    ):
        # Inicializar Pinecone
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = index_name
        
        # Crear índice si no existe
        if index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=index_name,
                dimension=dimension,
                metric=metric,
                spec=ServerlessSpec(
                    cloud='aws',
                    region=os.getenv("PINECONE_REGION", "us-east-1")
                )
            )
        
        self.index = self.pc.Index(index_name)
        
        # Inicializar OpenAI
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # =========================================================================
    # UPSERT (INSERCIÓN/ACTUALIZACIÓN)
    # =========================================================================
    
    def upsert_artifact(
        self,
        domain_id: str,
        instance_id: str,
        artifact_id: str,
        artifact_type: Literal["concept", "analysis", "output", "lesson"],
        text: str,
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Inserta artifact con namespace correcto.
        
        Args:
            domain_id: ID del domain (DD-001, DD-002, etc.)
            instance_id: ID de la instance (I001, I002, etc.)
            artifact_id: ID único del artifact
            artifact_type: Tipo de artifact
            text: Texto para generar embedding
            metadata: Metadata adicional
        
        Returns:
            Vector ID generado
        """
        # Generar embedding
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        embedding = response.data[0].embedding
        
        # Namespace pattern: {domain_id}.{instance_id}
        namespace = f"{domain_id}.{instance_id}"
        
        # Vector ID: {domain_id}-{instance_id}-{artifact_type}-{artifact_id}
        vector_id = f"{domain_id}-{instance_id}-{artifact_type}-{artifact_id}"
        
        # Metadata enriquecida
        enriched_metadata = {
            "domain_id": domain_id,
            "instance_id": instance_id,
            "artifact_id": artifact_id,
            "artifact_type": artifact_type,
            "created_at": datetime.utcnow().isoformat(),
            "text": text[:1000],  # Primeros 1000 chars para referencia
            **(metadata or {})
        }
        
        # Upsert
        self.index.upsert(
            vectors=[{
                "id": vector_id,
                "values": embedding,
                "metadata": enriched_metadata
            }],
            namespace=namespace
        )
        
        return vector_id
    
    def upsert_lesson(
        self,
        domain_id: str,
        instance_id: str,
        lesson_id: str,
        lesson_text: str,
        rostro: str,
        confidence: float,
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Inserta lesson como vector.
        
        Args:
            domain_id: ID del domain
            instance_id: ID de la instance que generó la lesson
            lesson_id: ID de la lesson
            lesson_text: Texto completo de la lesson
            rostro: Rostro que generó la lesson
            confidence: Confidence score de la lesson
            metadata: Metadata adicional
        
        Returns:
            Vector ID generado
        """
        return self.upsert_artifact(
            domain_id=domain_id,
            instance_id=instance_id,
            artifact_id=lesson_id,
            artifact_type="lesson",
            text=lesson_text,
            metadata={
                "rostro": rostro,
                "confidence": confidence,
                **(metadata or {})
            }
        )
    
    def upsert_domain_knowledge(
        self,
        domain_id: str,
        artifact_id: str,
        text: str,
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Inserta conocimiento general del domain (no específico de instance).
        
        Usa namespace especial: {domain_id}.global
        """
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        embedding = response.data[0].embedding
        
        namespace = f"{domain_id}.global"
        vector_id = f"{domain_id}-global-{artifact_id}"
        
        enriched_metadata = {
            "domain_id": domain_id,
            "instance_id": "global",
            "artifact_id": artifact_id,
            "artifact_type": "domain-knowledge",
            "created_at": datetime.utcnow().isoformat(),
            "text": text[:1000],
            **(metadata or {})
        }
        
        self.index.upsert(
            vectors=[{
                "id": vector_id,
                "values": embedding,
                "metadata": enriched_metadata
            }],
            namespace=namespace
        )
        
        return vector_id
    
    # =========================================================================
    # SEARCH (BÚSQUEDA)
    # =========================================================================
    
    def search_in_domain(
        self,
        query: str,
        domain_id: str,
        instance_id: Optional[str] = None,
        artifact_type: Optional[str] = None,
        top_k: int = 5,
        include_global: bool = True
    ) -> List[Dict]:
        """
        Busca en un domain específico (opcionalmente en instance).
        
        Args:
            query: Query en lenguaje natural
            domain_id: Domain donde buscar
            instance_id: Instance específica (opcional)
            artifact_type: Filtrar por tipo (opcional)
            top_k: Número de resultados
            include_global: Incluir conocimiento global del domain
        
        Returns:
            Lista de matches con score y metadata
        """
        # Generar embedding del query
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=query
        )
        query_embedding = response.data[0].embedding
        
        # Determinar namespaces a buscar
        namespaces = []
        
        if instance_id:
            namespaces.append(f"{domain_id}.{instance_id}")
        else:
            # Buscar en todas las instances del domain (requiere listar)
            # Por ahora, asumimos que se especifica instance o se usa global
            pass
        
        if include_global:
            namespaces.append(f"{domain_id}.global")
        
        # Filter por tipo (opcional)
        filter_dict = {}
        if artifact_type:
            filter_dict["artifact_type"] = artifact_type
        
        # Query en cada namespace y combinar resultados
        all_matches = []
        
        for namespace in namespaces:
            try:
                results = self.index.query(
                    vector=query_embedding,
                    namespace=namespace,
                    filter=filter_dict if filter_dict else None,
                    top_k=top_k,
                    include_metadata=True
                )
                
                for match in results.matches:
                    all_matches.append({
                        "id": match.id,
                        "score": match.score,
                        "namespace": namespace,
                        **match.metadata
                    })
            
            except Exception as e:
                # Namespace no existe (OK, puede ser que no haya data aún)
                continue
        
        # Ordenar por score y limitar a top_k
        all_matches.sort(key=lambda x: x["score"], reverse=True)
        return all_matches[:top_k]
    
    def search_lessons(
        self,
        query: str,
        domain_id: Optional[str] = None,
        rostro: Optional[str] = None,
        min_confidence: float = 0.0,
        top_k: int = 5
    ) -> List[Dict]:
        """
        Busca lessons específicamente.
        
        Args:
            query: Query en lenguaje natural
            domain_id: Filtrar por domain (opcional)
            rostro: Filtrar por rostro (opcional)
            min_confidence: Confidence mínima (opcional)
            top_k: Número de resultados
        
        Returns:
            Lista de lessons relevantes
        """
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=query
        )
        query_embedding = response.data[0].embedding
        
        # Construir filter
        filter_dict = {"artifact_type": "lesson"}
        if rostro:
            filter_dict["rostro"] = rostro
        if min_confidence > 0.0:
            filter_dict["confidence"] = {"$gte": min_confidence}
        if domain_id:
            filter_dict["domain_id"] = domain_id
        
        # Query (sin namespace para buscar en todos)
        results = self.index.query(
            vector=query_embedding,
            filter=filter_dict,
            top_k=top_k,
            include_metadata=True
        )
        
        return [{
            "id": match.id,
            "score": match.score,
            **match.metadata
        } for match in results.matches]
    
    def search_cross_domain(
        self,
        query: str,
        artifact_type: Optional[str] = None,
        top_k: int = 5
    ) -> List[Dict]:
        """
        Busca en TODOS los domains.
        
        Útil para encontrar patterns universales.
        """
        response = self.openai.embeddings.create(
            model="text-embedding-ada-002",
            input=query
        )
        query_embedding = response.data[0].embedding
        
        filter_dict = {}
        if artifact_type:
            filter_dict["artifact_type"] = artifact_type
        
        results = self.index.query(
            vector=query_embedding,
            filter=filter_dict if filter_dict else None,
            top_k=top_k,
            include_metadata=True
        )
        
        return [{
            "id": match.id,
            "score": match.score,
            **match.metadata
        } for match in results.matches]
    
    # =========================================================================
    # DELETE
    # =========================================================================
    
    def delete_instance(
        self,
        domain_id: str,
        instance_id: str
    ):
        """
        Elimina todos los vectores de una instance.
        
        Útil para rollback si instance falla.
        """
        namespace = f"{domain_id}.{instance_id}"
        
        # Eliminar namespace completo
        self.index.delete(delete_all=True, namespace=namespace)
    
    # =========================================================================
    # STATS
    # =========================================================================
    
    def get_namespace_stats(self, namespace: str) -> Dict:
        """Obtiene estadísticas de un namespace."""
        
        stats = self.index.describe_index_stats()
        
        if namespace in stats.namespaces:
            return {
                "namespace": namespace,
                "vector_count": stats.namespaces[namespace].vector_count
            }
        else:
            return {
                "namespace": namespace,
                "vector_count": 0
            }
    
    def get_domain_stats(self, domain_id: str) -> Dict:
        """Obtiene estadísticas de un domain completo."""
        
        stats = self.index.describe_index_stats()
        
        # Contar vectores en todos los namespaces del domain
        total_vectors = 0
        namespaces_count = 0
        
        for ns, ns_stats in stats.namespaces.items():
            if ns.startswith(f"{domain_id}."):
                total_vectors += ns_stats.vector_count
                namespaces_count += 1
        
        return {
            "domain_id": domain_id,
            "total_vectors": total_vectors,
            "namespaces_count": namespaces_count
        }


# =============================================================================
# EJEMPLO DE USO
# =============================================================================

if __name__ == "__main__":
    # Inicializar store
    store = DomainAwareVectorStore("melquisedec-knowledge")
    
    # Ejemplo 1: Insertar concepto en instance
    vector_id = store.upsert_artifact(
        domain_id="DD-001",
        instance_id="I001",
        artifact_id="concept-crisp-dm",
        artifact_type="concept",
        text="CRISP-DM is a data mining methodology with 6 phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.",
        metadata={
            "version": "1.0.0",
            "source": "wikipedia"
        }
    )
    print(f"✅ Concepto insertado: {vector_id}")
    
    # Ejemplo 2: Insertar lesson
    lesson_id = store.upsert_lesson(
        domain_id="DD-001",
        instance_id="I001",
        lesson_id="lesson-001-hypatia-citations",
        lesson_text="Filter papers by citation count (>100 for mature topics) to ensure quality and relevance. This reduces noise from low-quality or unreviewed papers.",
        rostro="HYPATIA",
        confidence=0.95,
        metadata={
            "status": "validated",
            "validated_in": ["DD-001-I002", "DD-001-I003"]
        }
    )
    print(f"✅ Lesson insertada: {lesson_id}")
    
    # Ejemplo 3: Buscar en domain
    results = store.search_in_domain(
        query="data mining methodology",
        domain_id="DD-001",
        instance_id="I001",
        top_k=3
    )
    print(f"\n🔍 Resultados de búsqueda:")
    for r in results:
        print(f"  - {r['id']} (score: {r['score']:.3f})")
        print(f"    {r['text'][:100]}...")
    
    # Ejemplo 4: Buscar lessons de HYPATIA
    hypatia_lessons = store.search_lessons(
        query="how to filter academic papers",
        rostro="HYPATIA",
        min_confidence=0.8,
        top_k=5
    )
    print(f"\n📚 Lessons de HYPATIA:")
    for lesson in hypatia_lessons:
        print(f"  - {lesson['id']} (confidence: {lesson['confidence']})")
    
    # Ejemplo 5: Stats del domain
    stats = store.get_domain_stats("DD-001")
    print(f"\n📊 Stats de domain DD-001:")
    print(f"  Total vectores: {stats['total_vectors']}")
    print(f"  Namespaces: {stats['namespaces_count']}")
