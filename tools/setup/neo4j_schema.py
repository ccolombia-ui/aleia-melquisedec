"""
Schema Neo4j para Sistema de Autopoiesis

Este archivo contiene el schema completo de Neo4j para:
- Dominios temáticos
- Research instances
- Lessons learned
- Prompt evolution
- Trazabilidad completa

Uso:
    python scripts/neo4j_schema.py --action=create
    python scripts/neo4j_schema.py --action=query --query=domains
"""

from neo4j import GraphDatabase
from typing import List, Dict, Optional
from datetime import datetime
import os


class AutopoiesisSchema:
    """Schema manager para el sistema de autopoiesis en Neo4j."""

    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # =========================================================================
    # CONSTRAINTS Y ÍNDICES
    # =========================================================================

    def create_constraints(self):
        """Crea constraints de uniqueness para garantizar integridad."""

        constraints = [
            # Dominios
            "CREATE CONSTRAINT domain_id_unique IF NOT EXISTS FOR (d:Domain) REQUIRE d.id IS UNIQUE",

            # Research Instances
            "CREATE CONSTRAINT instance_id_unique IF NOT EXISTS FOR (i:ResearchInstance) REQUIRE i.id IS UNIQUE",

            # Lessons
            "CREATE CONSTRAINT lesson_id_unique IF NOT EXISTS FOR (l:Lesson) REQUIRE l.id IS UNIQUE",

            # Prompt Types
            "CREATE CONSTRAINT prompt_type_id_unique IF NOT EXISTS FOR (p:PromptType) REQUIRE p.id IS UNIQUE",

            # Outputs
            "CREATE CONSTRAINT output_id_unique IF NOT EXISTS FOR (o:Output) REQUIRE o.id IS UNIQUE",
        ]

        with self.driver.session() as session:
            for constraint in constraints:
                session.run(constraint)
                print(f"✅ Constraint creado: {constraint.split('FOR')[1].split('REQUIRE')[0].strip()}")

    def create_indexes(self):
        """Crea índices para queries frecuentes."""

        indexes = [
            # Índices por domain_id (queries frecuentes)
            "CREATE INDEX domain_id_index IF NOT EXISTS FOR (n) ON (n.domain_id)",

            # Índices por status
            "CREATE INDEX instance_status_index IF NOT EXISTS FOR (i:ResearchInstance) ON (i.status)",
            "CREATE INDEX lesson_status_index IF NOT EXISTS FOR (l:Lesson) ON (l.status)",

            # Índices por rostro
            "CREATE INDEX lesson_rostro_index IF NOT EXISTS FOR (l:Lesson) ON (l.rostro)",

            # Índices por fecha
            "CREATE INDEX instance_created_index IF NOT EXISTS FOR (i:ResearchInstance) ON (i.started_at)",
            "CREATE INDEX lesson_extracted_index IF NOT EXISTS FOR (l:Lesson) ON (i.extracted_at)",
        ]

        with self.driver.session() as session:
            for index in indexes:
                session.run(index)
                print(f"✅ Índice creado: {index.split('FOR')[1].split('ON')[0].strip()}")

    # =========================================================================
    # CREACIÓN DE NODOS
    # =========================================================================

    def create_domain(
        self,
        domain_id: str,
        name: str,
        description: str,
        prompt_type_id: str,
        prompt_version: str = "1.0.0"
    ) -> Dict:
        """Crea un Domain node."""

        query = """
        CREATE (d:Domain {
            id: $domain_id,
            name: $name,
            description: $description,
            created_at: datetime(),
            prompt_type_id: $prompt_type_id,
            prompt_version: $prompt_version,
            instances_count: 0,
            lessons_count: 0
        })
        RETURN d
        """

        with self.driver.session() as session:
            result = session.run(query, {
                "domain_id": domain_id,
                "name": name,
                "description": description,
                "prompt_type_id": prompt_type_id,
                "prompt_version": prompt_version
            })
            return result.single()[0]

    def create_research_instance(
        self,
        instance_id: str,
        name: str,
        domain_id: str,
        prompt_instance_id: str,
        prompt_type_version: str
    ) -> Dict:
        """Crea un ResearchInstance node y lo conecta a su Domain."""

        query = """
        MATCH (d:Domain {id: $domain_id})
        CREATE (i:ResearchInstance {
            id: $instance_id,
            name: $name,
            domain_id: $domain_id,
            status: 'in-progress',
            started_at: datetime(),
            completed_at: null,
            prompt_instance_id: $prompt_instance_id,
            prompt_type_version: $prompt_type_version,
            outputs_produced: 0,
            lessons_extracted: 0
        })
        CREATE (i)-[:BELONGS_TO]->(d)

        // Incrementar contador de instances en domain
        SET d.instances_count = d.instances_count + 1

        RETURN i, d
        """

        with self.driver.session() as session:
            result = session.run(query, {
                "instance_id": instance_id,
                "name": name,
                "domain_id": domain_id,
                "prompt_instance_id": prompt_instance_id,
                "prompt_type_version": prompt_type_version
            })
            return result.single()

    def create_lesson(
        self,
        lesson_id: str,
        instance_id: str,
        domain_id: str,
        rostro: str,
        text: str,
        confidence: float,
        applies_to_prompt: str,
        scope: str = "domain"
    ) -> Dict:
        """Crea un Lesson node y lo conecta a su ResearchInstance."""

        query = """
        MATCH (i:ResearchInstance {id: $instance_id})
        MATCH (d:Domain {id: $domain_id})

        CREATE (l:Lesson {
            id: $lesson_id,
            instance_id: $instance_id,
            domain_id: $domain_id,
            rostro: $rostro,
            confidence: $confidence,
            status: 'proposed',
            text: $text,
            extracted_at: datetime(),
            applies_to_prompt: $applies_to_prompt,
            scope: $scope
        })

        CREATE (i)-[:LEARNED]->(l)

        // Incrementar contadores
        SET i.lessons_extracted = i.lessons_extracted + 1
        SET d.lessons_count = d.lessons_count + 1

        RETURN l, i, d
        """

        with self.driver.session() as session:
            result = session.run(query, {
                "lesson_id": lesson_id,
                "instance_id": instance_id,
                "domain_id": domain_id,
                "rostro": rostro,
                "text": text,
                "confidence": confidence,
                "applies_to_prompt": applies_to_prompt,
                "scope": scope
            })
            return result.single()

    def create_prompt_type(
        self,
        prompt_id: str,
        domain_id: str,
        version: str,
        lessons_incorporated: int = 0,
        changelog: str = ""
    ) -> Dict:
        """Crea un PromptType node."""

        query = """
        MATCH (d:Domain {id: $domain_id})

        CREATE (p:PromptType {
            id: $prompt_id,
            domain_id: $domain_id,
            version: $version,
            created_at: datetime(),
            lessons_incorporated: $lessons_incorporated,
            changelog: $changelog
        })

        CREATE (p)-[:BELONGS_TO_DOMAIN]->(d)

        RETURN p, d
        """

        with self.driver.session() as session:
            result = session.run(query, {
                "prompt_id": prompt_id,
                "domain_id": domain_id,
                "version": version,
                "lessons_incorporated": lessons_incorporated,
                "changelog": changelog
            })
            return result.single()

    def create_output(
        self,
        output_id: str,
        instance_id: str,
        version: str,
        path: str,
        vector_namespace: str
    ) -> Dict:
        """Crea un Output node."""

        query = """
        MATCH (i:ResearchInstance {id: $instance_id})

        CREATE (o:Output {
            id: $output_id,
            instance_id: $instance_id,
            version: $version,
            path: $path,
            vector_namespace: $vector_namespace,
            created_at: datetime()
        })

        CREATE (i)-[:PRODUCED]->(o)

        SET i.outputs_produced = i.outputs_produced + 1

        RETURN o, i
        """

        with self.driver.session() as session:
            result = session.run(query, {
                "output_id": output_id,
                "instance_id": instance_id,
                "version": version,
                "path": path,
                "vector_namespace": vector_namespace
            })
            return result.single()

    # =========================================================================
    # RELACIONES (EVOLUTION)
    # =========================================================================

    def link_lesson_improves_prompt(
        self,
        lesson_id: str,
        prompt_id: str,
        from_version: str,
        to_version: str
    ):
        """Crea relación IMPROVES entre Lesson y PromptType."""

        query = """
        MATCH (l:Lesson {id: $lesson_id})
        MATCH (p:PromptType {id: $prompt_id})

        CREATE (l)-[:IMPROVES {
            from_version: $from_version,
            to_version: $to_version,
            incorporated_at: datetime()
        }]->(p)

        // Actualizar status de lesson
        SET l.status = 'validated'
        SET l.version_applied = $to_version

        RETURN l, p
        """

        with self.driver.session() as session:
            return session.run(query, {
                "lesson_id": lesson_id,
                "prompt_id": prompt_id,
                "from_version": from_version,
                "to_version": to_version
            }).single()

    def link_prompt_evolution(
        self,
        old_prompt_id: str,
        new_prompt_id: str
    ):
        """Crea relación EVOLVED_TO entre versiones de PromptType."""

        query = """
        MATCH (p1:PromptType {id: $old_prompt_id})
        MATCH (p2:PromptType {id: $new_prompt_id})

        CREATE (p1)-[:EVOLVED_TO {
            evolved_at: datetime()
        }]->(p2)

        RETURN p1, p2
        """

        with self.driver.session() as session:
            return session.run(query, {
                "old_prompt_id": old_prompt_id,
                "new_prompt_id": new_prompt_id
            }).single()

    def link_lesson_validated_in(
        self,
        lesson_id: str,
        instance_id: str,
        result: str = "success"
    ):
        """Crea relación VALIDATED_IN entre Lesson y ResearchInstance."""

        query = """
        MATCH (l:Lesson {id: $lesson_id})
        MATCH (i:ResearchInstance {id: $instance_id})

        CREATE (l)-[:VALIDATED_IN {
            validated_at: datetime(),
            result: $result
        }]->(i)

        // Recalcular confidence basado en validaciones
        WITH l
        MATCH (l)-[v:VALIDATED_IN]->()
        WITH l, COUNT(v) as validations,
             SUM(CASE WHEN v.result = 'success' THEN 1 ELSE 0 END) as successes
        SET l.confidence = l.confidence * (1.0 + (successes * 0.1))

        RETURN l, i
        """

        with self.driver.session() as session:
            return session.run(query, {
                "lesson_id": lesson_id,
                "instance_id": instance_id,
                "result": result
            }).single()

    def link_instance_used_prompt(
        self,
        instance_id: str,
        prompt_id: str
    ):
        """Crea relación USED_PROMPT entre ResearchInstance y PromptType."""

        query = """
        MATCH (i:ResearchInstance {id: $instance_id})
        MATCH (p:PromptType {id: $prompt_id})

        CREATE (i)-[:USED_PROMPT {
            used_at: datetime()
        }]->(p)

        RETURN i, p
        """

        with self.driver.session() as session:
            return session.run(query, {
                "instance_id": instance_id,
                "prompt_id": prompt_id
            }).single()

    # =========================================================================
    # QUERIES ÚTILES
    # =========================================================================

    def get_domain_evolution(self, domain_id: str) -> List[Dict]:
        """Ver evolución completa de un dominio."""

        query = """
        MATCH (d:Domain {id: $domain_id})<-[:BELONGS_TO]-(i:ResearchInstance)
        OPTIONAL MATCH (i)-[:LEARNED]->(l:Lesson)
        OPTIONAL MATCH (l)-[:IMPROVES]->(p:PromptType)

        RETURN d.name AS domain,
               COUNT(DISTINCT i) AS total_instances,
               COUNT(DISTINCT l) AS total_lessons,
               COUNT(DISTINCT CASE WHEN l.status = 'validated' THEN l END) AS validated_lessons,
               MAX(p.version) AS latest_prompt_version
        """

        with self.driver.session() as session:
            result = session.run(query, {"domain_id": domain_id})
            return [dict(record) for record in result]

    def get_lessons_by_rostro(self, rostro: str, status: str = "validated") -> List[Dict]:
        """Ver lessons de un rostro específico."""

        query = """
        MATCH (l:Lesson {rostro: $rostro, status: $status})
        OPTIONAL MATCH (l)-[:IMPROVES]->(p:PromptType)

        RETURN l.id AS lesson_id,
               l.text AS lesson,
               l.confidence AS confidence,
               p.version AS applied_in_version,
               l.extracted_at AS extracted_at
        ORDER BY l.confidence DESC
        """

        with self.driver.session() as session:
            result = session.run(query, {"rostro": rostro, "status": status})
            return [dict(record) for record in result]

    def get_lesson_traceability(self, lesson_id: str) -> Dict:
        """Trazabilidad completa de una lesson."""

        query = """
        MATCH (i:ResearchInstance)-[:LEARNED]->(l:Lesson {id: $lesson_id})
        OPTIONAL MATCH (l)-[:IMPROVES]->(p:PromptType)
        OPTIONAL MATCH (l)-[:VALIDATED_IN]->(i2:ResearchInstance)

        RETURN l.id AS lesson_id,
               l.text AS lesson,
               l.confidence AS confidence,
               i.id AS origin_instance,
               p.version AS applied_version,
               COLLECT(DISTINCT i2.id) AS validated_in_instances
        """

        with self.driver.session() as session:
            result = session.run(query, {"lesson_id": lesson_id})
            return dict(result.single())

    def get_universal_lessons(self) -> List[Dict]:
        """Lessons universales (scope=universal)."""

        query = """
        MATCH (l:Lesson {scope: 'universal', status: 'validated'})
        OPTIONAL MATCH (l)-[:APPLIES_TO_DOMAIN]->(d:Domain)

        RETURN l.id AS lesson_id,
               l.text AS lesson,
               l.confidence AS confidence,
               COLLECT(DISTINCT d.name) AS applicable_domains
        ORDER BY l.confidence DESC
        """

        with self.driver.session() as session:
            result = session.run(query)
            return [dict(record) for record in result]

    def get_instances_with_improved_prompt(self, min_version: str = "1.1.0") -> List[Dict]:
        """Instances que usaron versión mejorada del prompt."""

        query = """
        MATCH (i:ResearchInstance)-[:USED_PROMPT]->(p:PromptType)
        WHERE p.version >= $min_version

        RETURN i.id AS instance_id,
               i.name AS instance_name,
               p.id AS prompt_used,
               p.version AS prompt_version,
               p.lessons_incorporated AS lessons_count
        ORDER BY p.version DESC
        """

        with self.driver.session() as session:
            result = session.run(query, {"min_version": min_version})
            return [dict(record) for record in result]

    def get_confidence_by_rostro(self) -> List[Dict]:
        """Confidence promedio de lessons por rostro."""

        query = """
        MATCH (l:Lesson)
        WHERE l.status = 'validated'

        RETURN l.rostro AS rostro,
               AVG(l.confidence) AS avg_confidence,
               COUNT(l) AS validated_lessons
        ORDER BY avg_confidence DESC
        """

        with self.driver.session() as session:
            result = session.run(query)
            return [dict(record) for record in result]

    # =========================================================================
    # UPDATES
    # =========================================================================

    def complete_instance(
        self,
        instance_id: str,
        status: str = "completed"
    ):
        """Marcar instance como completada."""

        query = """
        MATCH (i:ResearchInstance {id: $instance_id})
        SET i.status = $status,
            i.completed_at = datetime()

        // Calcular duración
        WITH i, duration.inSeconds(i.started_at, i.completed_at).hours AS duration_hours
        SET i.duration_hours = duration_hours

        RETURN i
        """

        with self.driver.session() as session:
            return session.run(query, {
                "instance_id": instance_id,
                "status": status
            }).single()

    def reject_lesson(
        self,
        lesson_id: str,
        reason: str
    ):
        """Rechazar una lesson."""

        query = """
        MATCH (l:Lesson {id: $lesson_id})
        SET l.status = 'rejected',
            l.rejection_reason = $reason

        RETURN l
        """

        with self.driver.session() as session:
            return session.run(query, {
                "lesson_id": lesson_id,
                "reason": reason
            }).single()


# =============================================================================
# CLI USAGE
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Neo4j Schema Manager para Autopoiesis")
    parser.add_argument("--action", choices=["create", "query"], required=True)
    parser.add_argument("--query", choices=["domains", "lessons", "rostros", "universal"])

    args = parser.parse_args()

    # Conectar a Neo4j (ajustar credenciales según tu setup)
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

    schema = AutopoiesisSchema(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

    try:
        if args.action == "create":
            print("🔧 Creando schema...")
            schema.create_constraints()
            schema.create_indexes()
            print("✅ Schema creado exitosamente")

        elif args.action == "query":
            if args.query == "domains":
                # Ejemplo: Ver evolución de domain DD-001
                results = schema.get_domain_evolution("DD-001")
                print("\n📊 Evolución del Dominio:")
                for r in results:
                    print(f"  {r}")

            elif args.query == "lessons":
                # Ejemplo: Lessons de HYPATIA
                results = schema.get_lessons_by_rostro("HYPATIA")
                print("\n📚 Lessons de HYPATIA:")
                for r in results:
                    print(f"  {r}")

            elif args.query == "rostros":
                results = schema.get_confidence_by_rostro()
                print("\n⭐ Confidence por Rostro:")
                for r in results:
                    print(f"  {r['rostro']}: {r['avg_confidence']:.2f} ({r['validated_lessons']} lessons)")

            elif args.query == "universal":
                results = schema.get_universal_lessons()
                print("\n🌍 Lessons Universales:")
                for r in results:
                    print(f"  {r}")

    finally:
        schema.close()
