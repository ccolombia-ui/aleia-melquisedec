"""
SPARQL Competency Questions Test Automation
Purpose: Execute SPARQL queries and validate expected results
Requirements: Python 3.11+, rdflib
"""

import sys
from pathlib import Path
from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
import json
from typing import List, Dict, Any

# Configuration
ONTOLOGY_FILE = Path("apps/R000-autopoietic-template/_melquisedec/domain/workbooks/spec-001-prototype/comparative-analysis-aoem-v2_vs_tpl-melquisedec-v2/hito-2-conceptualizacion/templates-ottr-automatizacion/output/library-ontology-example.ttl")
REPORT_DIR = Path("reports")

# Colors
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

# Competency Questions (from competency-questions.md)
COMPETENCY_QUESTIONS = [
    {
        "id": "CQ1",
        "question": "¿Qué libros ha escrito Gabriel García Márquez?",
        "sparql": """
            PREFIX lib: <http://example.org/library/>
            SELECT ?book ?title
            WHERE {
                lib:GabrielGarcíaMárquez lib:authorOf ?book .
                ?book rdfs:label ?title .
                FILTER(lang(?title) = "es")
            }
        """,
        "expected_min_results": 2,
        "expected_contains": ["CienAñosDeSoledad", "AmorEnTiemposDelColera"]
    },
    {
        "id": "CQ2",
        "question": "¿A qué categoría pertenece el libro '1984'?",
        "sparql": """
            PREFIX lib: <http://example.org/library/>
            SELECT ?categoria ?nombre
            WHERE {
                lib:NineteenEightyFour lib:hasCategoria ?categoria .
                ?categoria rdfs:label ?nombre .
                FILTER(lang(?nombre) = "es")
            }
        """,
        "expected_min_results": 1,
        "expected_contains": ["Ficcion"]
    },
    {
        "id": "CQ3",
        "question": "¿Quién tiene prestado actualmente el libro '1984'?",
        "sparql": """
            PREFIX lib: <http://example.org/library/>
            SELECT ?usuario ?nombre
            WHERE {
                ?prestamo lib:borrowedItem lib:NineteenEightyFour ;
                          lib:borrowedBy ?usuario .
                ?usuario rdfs:label ?nombre .
            }
        """,
        "expected_min_results": 1,
        "expected_contains": []
    },
    {
        "id": "CQ4",
        "question": "¿Qué libros están disponibles (no prestados)?",
        "sparql": """
            PREFIX lib: <http://example.org/library/>
            SELECT ?book ?title
            WHERE {
                ?book a lib:Libro ;
                      rdfs:label ?title .
                FILTER(lang(?title) = "es")
                FILTER NOT EXISTS {
                    ?prestamo lib:borrowedItem ?book .
                }
            }
        """,
        "expected_min_results": 1,
        "expected_contains": []
    },
    {
        "id": "CQ5",
        "question": "¿Cuántos préstamos activos hay en total?",
        "sparql": """
            PREFIX lib: <http://example.org/library/>
            SELECT (COUNT(?prestamo) AS ?count)
            WHERE {
                ?prestamo a lib:Prestamo .
            }
        """,
        "expected_min_results": 1,
        "expected_type": "count"
    }
]

def execute_query(graph: Graph, sparql: str, cq_id: str) -> List[Dict[str, Any]]:
    """Execute SPARQL query and return results"""
    try:
        query = prepareQuery(sparql)
        results = graph.query(query)
        
        result_list = []
        for row in results:
            result_dict = {}
            for var in results.vars:
                result_dict[str(var)] = str(row[var]) if row[var] else None
            result_list.append(result_dict)
        
        return result_list
    except Exception as e:
        print(f"  {RED}✗ Query execution failed: {e}{NC}")
        return []

def validate_results(results: List[Dict], expected_min: int, expected_contains: List[str], cq_id: str) -> bool:
    """Validate query results against expectations"""
    passed = True
    
    # Check minimum results
    if len(results) < expected_min:
        print(f"    {RED}✗ Expected at least {expected_min} results, got {len(results)}{NC}")
        passed = False
    else:
        print(f"    {GREEN}✓ Result count: {len(results)} >= {expected_min}{NC}")
    
    # Check expected values
    if expected_contains:
        results_str = str(results)
        for expected in expected_contains:
            if expected not in results_str:
                print(f"    {RED}✗ Expected value '{expected}' not found{NC}")
                passed = False
            else:
                print(f"    {GREEN}✓ Found expected value: {expected}{NC}")
    
    return passed

def main():
    print("=" * 50)
    print("SPARQL Competency Questions Validation")
    print("=" * 50)
    print()
    
    # Create reports directory
    REPORT_DIR.mkdir(exist_ok=True)
    
    # Check if ontology exists
    if not ONTOLOGY_FILE.exists():
        print(f"{RED}✗ Ontology file not found: {ONTOLOGY_FILE}{NC}")
        return 1
    
    # Load graph
    print(f"Loading ontology: {ONTOLOGY_FILE.name}")
    graph = Graph()
    graph.parse(str(ONTOLOGY_FILE), format="turtle")
    print(f"  ✓ Loaded {len(graph)} triples")
    print()
    
    # Execute each CQ
    results_summary = []
    passed_count = 0
    failed_count = 0
    
    for cq in COMPETENCY_QUESTIONS:
        print(f"{cq['id']}: {cq['question']}")
        
        # Execute query
        results = execute_query(graph, cq['sparql'], cq['id'])
        print(f"  Results: {len(results)}")
        
        # Validate
        passed = validate_results(
            results,
            cq['expected_min_results'],
            cq.get('expected_contains', []),
            cq['id']
        )
        
        if passed:
            print(f"  {GREEN}✓ PASSED{NC}")
            passed_count += 1
        else:
            print(f"  {RED}✗ FAILED{NC}")
            failed_count += 1
        
        print()
        
        # Save results
        results_summary.append({
            "id": cq['id'],
            "question": cq['question'],
            "passed": passed,
            "result_count": len(results),
            "results": results
        })
    
    # Save JSON report
    report_file = REPORT_DIR / "sparql-results.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump({
            "total_cqs": len(COMPETENCY_QUESTIONS),
            "passed": passed_count,
            "failed": failed_count,
            "pass_rate": (passed_count / len(COMPETENCY_QUESTIONS)) * 100,
            "results": results_summary
        }, f, indent=2)
    
    # Print summary
    print("=" * 50)
    print("Summary:")
    print("=" * 50)
    print(f"Total CQs: {len(COMPETENCY_QUESTIONS)}")
    print(f"Passed: {GREEN}{passed_count}{NC}")
    print(f"Failed: {RED}{failed_count}{NC}")
    print(f"Pass Rate: {(passed_count / len(COMPETENCY_QUESTIONS)) * 100:.1f}%")
    print(f"📊 Report: {report_file}")
    print()
    
    if failed_count == 0:
        print(f"{GREEN}✓ All CQs PASSED{NC}")
        return 0
    else:
        print(f"{RED}✗ Some CQs FAILED{NC}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
