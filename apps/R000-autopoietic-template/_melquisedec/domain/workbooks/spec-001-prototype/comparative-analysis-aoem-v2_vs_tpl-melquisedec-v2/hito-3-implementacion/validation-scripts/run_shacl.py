"""
pySHACL Validation Script
Purpose: Validate RDF instances against SHACL shapes (business rules)
Requirements: Python 3.11+, pyshacl, rdflib
"""

import sys
from pathlib import Path
from pyshacl import validate
from rdflib import Graph
import json

# Configuration
ONTOLOGY_FILE = Path("apps/R000-autopoietic-template/_melquisedec/domain/workbooks/spec-001-prototype/comparative-analysis-aoem-v2_vs_tpl-melquisedec-v2/hito-2-conceptualizacion/templates-ottr-automatizacion/output/library-ontology-example.ttl")
SHAPES_DIR = Path("apps/R000-autopoietic-template/_melquisedec/domain/workbooks/spec-001-prototype/comparative-analysis-aoem-v2_vs_tpl-melquisedec-v2/hito-3-implementacion/shacl-shapes")
REPORT_DIR = Path("reports")

# Colors
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

def main():
    print("=" * 50)
    print("pySHACL Validation")
    print("=" * 50)
    print()
    
    # Create reports directory
    REPORT_DIR.mkdir(exist_ok=True)
    
    # Check if ontology exists
    if not ONTOLOGY_FILE.exists():
        print(f"{RED}✗ Ontology file not found: {ONTOLOGY_FILE}{NC}")
        return 1
    
    # Load data graph
    print(f"Loading ontology: {ONTOLOGY_FILE.name}")
    data_graph = Graph()
    data_graph.parse(str(ONTOLOGY_FILE), format="turtle")
    print(f"  ✓ Loaded {len(data_graph)} triples")
    print()
    
    # Find all SHACL shapes
    shapes_files = list(SHAPES_DIR.glob("*.ttl")) if SHAPES_DIR.exists() else []
    
    if not shapes_files:
        print(f"{YELLOW}⚠ No SHACL shapes found in {SHAPES_DIR}{NC}")
        print("  Skipping SHACL validation")
        return 0
    
    print(f"Found {len(shapes_files)} SHACL shape file(s):")
    for sf in shapes_files:
        print(f"  - {sf.name}")
    print()
    
    # Validate against each shapes file
    all_conforms = True
    total_violations = 0
    results_summary = []
    
    for shapes_file in shapes_files:
        print(f"Validating against: {shapes_file.name}")
        
        # Load shapes graph
        shapes_graph = Graph()
        shapes_graph.parse(str(shapes_file), format="turtle")
        
        # Run validation
        conforms, results_graph, results_text = validate(
            data_graph=data_graph,
            shacl_graph=shapes_graph,
            inference='rdfs',
            abort_on_first=False,
            allow_warnings=True,
            meta_shacl=False,
            advanced=True
        )
        
        # Parse results
        violations = results_text.count("Validation Result") if not conforms else 0
        total_violations += violations
        
        if conforms:
            print(f"  {GREEN}✓ CONFORMS{NC}")
        else:
            print(f"  {RED}✗ VIOLATIONS: {violations}{NC}")
            all_conforms = False
        
        # Save detailed report
        report_file = REPORT_DIR / f"shacl-{shapes_file.stem}-report.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(results_text)
        
        print(f"  📄 Report: {report_file}")
        print()
        
        results_summary.append({
            "shapes_file": shapes_file.name,
            "conforms": conforms,
            "violations": violations,
            "report_file": str(report_file)
        })
    
    # Save JSON summary
    summary_file = REPORT_DIR / "shacl-summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump({
            "all_conforms": all_conforms,
            "total_violations": total_violations,
            "shapes_validated": len(shapes_files),
            "results": results_summary
        }, f, indent=2)
    
    # Print summary
    print("=" * 50)
    print("Summary:")
    print("=" * 50)
    print(f"Total violations: {RED}{total_violations}{NC}" if total_violations > 0 else f"Total violations: {GREEN}0{NC}")
    print(f"Shapes validated: {len(shapes_files)}")
    print(f"📊 Summary: {summary_file}")
    print()
    
    if all_conforms:
        print(f"{GREEN}✓ Validation PASSED{NC}")
        return 0
    else:
        print(f"{RED}✗ Validation FAILED (violations found){NC}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
