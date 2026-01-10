#!/usr/bin/env python3
"""
Batch generator for REQ-011 through REQ-052
Generates atomic requirement files from the requirements.md source
"""

import os
from pathlib import Path

# Define the requirements mapping
REQUIREMENTS = [
    # Phase 2: Lens Integration (Weeks 3-4)
    {
        "id": "011",
        "title": "Create DDD Lens Variants (6 templates)",
        "priority": "High",
        "type": "Template",
        "effort": "24 hours",
        "description": "Create Domain-Driven Design lens variants for software-focused research.",
        "acceptance_criteria": [
            "Folder: `artifact-templates/by-lens/ddd/`",
            "6 files: concept-ddd-tpl.md, analysis-ddd-tpl.md, etc.",
            "Each template adapted for DDD: Concept includes 'Ubiquitous Language' and 'Bounded Context', Analysis includes 'Domain Model' section, Decision includes 'Strategic Design Impact'",
            "README.md explains DDD lens philosophy",
        ],
        "dependencies": "REQ-002 through REQ-007",
        "validation_method": "Verify DDD strategic/tactical patterns included",
        "result_type": "intermediate",
        "associated_causes": "cause-keterdoc-lens-system",
        "associated_features": "feat-ddd-templates",
    },
    {
        "id": "012",
        "title": "Create Social Lens Variants (6 templates)",
        "priority": "Medium",
        "type": "Template",
        "effort": "24 hours",
        "description": "Create Social Science lens variants for qualitative research.",
        "acceptance_criteria": [
            "Folder: `artifact-templates/by-lens/social/`",
            "6 files: concept-social-tpl.md, analysis-social-tpl.md, etc.",
            "Each template adapted for Social Science: Concept includes 'Social Context' and 'Stakeholder Perspectives', Analysis includes 'Qualitative Coding' section, Experiment includes 'Participant Demographics'",
            "README.md explains Social lens philosophy",
        ],
        "dependencies": "REQ-002 through REQ-007",
        "validation_method": "Verify social science methods included",
        "result_type": "intermediate",
        "associated_causes": "cause-keterdoc-lens-system",
        "associated_features": "feat-social-templates",
    },
    {
        "id": "013",
        "title": "Document Lens Selection Guide",
        "priority": "High",
        "type": "Documentation",
        "effort": "8 hours",
        "description": "Create docs/guides/LENS-SELECTION-GUIDE.md to help choose appropriate lens.",
        "acceptance_criteria": [
            "File: `docs/guides/LENS-SELECTION-GUIDE.md`",
            "Decision matrix: Project Type → Recommended Lens",
            "Examples: 'Building a tool? Use DSR', 'Quantitative study? Use IMRAD'",
            "Comparison table showing differences between lenses",
            "Can combine lenses (e.g., DSR+DDD for software artifacts)",
            "Links to manifesto's lens documentation",
        ],
        "dependencies": "REQ-009 through REQ-012",
        "validation_method": "Developers can select correct lens for their project type",
        "result_type": "final",
        "associated_causes": "cause-keterdoc-usability",
        "associated_features": "feat-lens-guide",
    },
    # Phase 3: Workflow-Pattern System (Week 5)
    {
        "id": "014",
        "title": "Define Artifact-Workflow Mapping",
        "priority": "Critical",
        "type": "Configuration",
        "effort": "8 hours",
        "description": "Create config/artifact-workflows.yaml mapping artifact types to workflow patterns.",
        "acceptance_criteria": [
            "File: `config/artifact-workflows.yaml`",
            "Maps 28+ artifact types to patterns (e.g., concept → PATTERN-003-Conceptualize)",
            "Includes lens overrides (e.g., concept + DSR → PATTERN-003-DSR variant)",
            "Documents confidence score initialization (0.50 for new patterns)",
            "Version tracking (patterns can evolve v1.0.0 → v1.1.0)",
        ],
        "dependencies": "REQ-002 through REQ-007",
        "validation_method": "All artifact types have assigned pattern",
        "result_type": "immediate",
        "associated_causes": "cause-workflow-automation",
        "associated_features": "feat-pattern-mapping",
    },
    {
        "id": "015",
        "title": "Create Pattern - Output Triple (PATTERN-000)",
        "priority": "Critical",
        "type": "Configuration",
        "effort": "4 hours",
        "description": "Create patterns/PATTERN-000-output-triple.yaml for foundational Output Triple workflow.",
        "acceptance_criteria": [
            "File: `patterns/PATTERN-000-output-triple.yaml`",
            "Structure includes: id, version, confidence (0.90), description, steps, validation_criteria",
            "Steps: Write Markdown, Generate RDF triples, Import to Neo4j, Generate embeddings, Store in vector DB",
            "Validation criteria: All 3 outputs present, Neo4j relationships match SECI model",
            "lens_applicability: ['DSR', 'IMRAD', 'DDD', 'Social']",
        ],
        "dependencies": "None",
        "validation_method": "Pattern file validates against JSON Schema",
        "result_type": "immediate",
        "associated_causes": "cause-triple-persistence",
        "associated_features": "feat-output-triple",
    },
    {
        "id": "016",
        "title": "Create Patterns 001-009 (9 patterns)",
        "priority": "High",
        "type": "Configuration",
        "effort": "36 hours",
        "description": "Create 9 workflow patterns for different artifact types (Literature Review, Atomization, Conceptualize, Analyze, Decide, Experiment, Problem-RBM-GAC, Output-Production, Lesson-Extraction).",
        "acceptance_criteria": [
            "Files: patterns/PATTERN-001 through PATTERN-009",
            "Each contains: id, version, confidence, description, steps, validation_criteria, lens_applicability",
            "Confidence initialized (0.50 for new, 0.80-0.90 for documented patterns)",
            "At least 3 steps defined per pattern",
            "At least 2 validation criteria per pattern",
        ],
        "dependencies": "REQ-015",
        "validation_method": "All 10 patterns validate, cover 28+ artifact types",
        "result_type": "intermediate",
        "associated_causes": "cause-workflow-automation",
        "associated_features": "feat-workflow-patterns",
    },
    {
        "id": "017",
        "title": "Document Pattern System",
        "priority": "High",
        "type": "Documentation",
        "effort": "8 hours",
        "description": "Create docs/guides/PATTERN-SYSTEM.md explaining workflow pattern usage and evolution.",
        "acceptance_criteria": [
            "File: `docs/guides/PATTERN-SYSTEM.md`",
            "Sections: What are Patterns, How Confidence Scores Work, Pattern Evolution, Creating Custom Patterns",
            "Explains autopoiesis: lessons → pattern updates → confidence increases",
            "Shows example: PATTERN-003 v1.0.0 (confidence 0.50) → v1.1.0 (confidence 0.85)",
            "Links to manifesto/02-arquitectura/05-autopoiesis-system.md",
        ],
        "dependencies": "REQ-014 through REQ-016",
        "validation_method": "Developers understand how to use and evolve patterns",
        "result_type": "final",
        "associated_causes": "cause-autopoiesis",
        "associated_features": "feat-pattern-docs",
    },
    # Phase 4: Migration Tools (Week 6)
    {
        "id": "018",
        "title": "Script - Convert ISSUE.yaml to ISSUE.md",
        "priority": "Critical",
        "type": "Tool",
        "effort": "12 hours",
        "description": "Create tools/keterdoc/convert-issue-yaml-to-md.py for automated migration.",
        "acceptance_criteria": [
            "File: `tools/keterdoc/convert-issue-yaml-to-md.py`",
            "Reads ISSUE.yaml, outputs ISSUE.md with YAML-LD frontmatter",
            "Preserves all data (problem, gap, goal → Markdown sections)",
            "Adds KeterDoc metadata (id, is_a, dc, seci)",
            "CLI: `convert-issue-yaml-to-md.py --input ISSUE.yaml --output ISSUE.md --dry-run`",
            "Includes validation: warns if required fields missing",
            "Unit tests: 5 test cases (complete YAML, partial, invalid, etc.)",
        ],
        "dependencies": "REQ-001",
        "validation_method": "Converts 5 test ISSUE.yaml files successfully",
        "result_type": "immediate",
        "associated_causes": "cause-migration-automation",
        "associated_features": "feat-yaml-converter",
    },
    {
        "id": "019",
        "title": "Script - Generate Artifact from Template",
        "priority": "Critical",
        "type": "Tool",
        "effort": "12 hours",
        "description": "Create tools/keterdoc/generate-artifact-from-template.py for quick artifact creation.",
        "acceptance_criteria": [
            "File: `tools/keterdoc/generate-artifact-from-template.py`",
            "CLI: `generate-artifact-from-template.py concept 'Graph Databases' --lens dsr --output 020-conceive/02-atomics/concept-graph-databases.md`",
            "Automatically: Selects template, Generates unique id, Populates dc.date, Creates file",
            "Interactive mode: prompts for missing values",
            "Validation: checks KeterDoc compliance before writing",
            "Unit tests: 8 test cases (all combinations: type × lens)",
        ],
        "dependencies": "REQ-002 through REQ-012",
        "validation_method": "Generates 10 test artifacts successfully",
        "result_type": "immediate",
        "associated_causes": "cause-artifact-generation",
        "associated_features": "feat-template-generator",
    },
    {
        "id": "020",
        "title": "Script - Validate KeterDoc Compliance",
        "priority": "Critical",
        "type": "Tool",
        "effort": "12 hours",
        "description": "Create tools/keterdoc/validate-keterdoc-compliance.py for CI/CD validation.",
        "acceptance_criteria": [
            "File: `tools/keterdoc/validate-keterdoc-compliance.py`",
            "CLI: `validate-keterdoc-compliance.py --path apps/research-autopoietic-template/ --recursive`",
            "Validates: YAML-LD frontmatter present, KeterDoc fields present, dc.date format (ISO 8601), seci.derives_from paths exist, artifact_template reference valid",
            "Output: JSON report with pass/fail + detailed errors",
            "Exit code 0 (pass) or 1 (fail) for CI/CD",
            "Unit tests: 10 test cases (valid, missing fields, invalid dates, etc.)",
        ],
        "dependencies": "REQ-001, REQ-002",
        "validation_method": "Validates 20 test artifacts, catches all intentional errors",
        "result_type": "immediate",
        "associated_causes": "cause-quality-assurance",
        "associated_features": "feat-validation-tool",
    },
    {
        "id": "021",
        "title": "Script - Extract SECI Relationships",
        "priority": "High",
        "type": "Tool",
        "effort": "8 hours",
        "description": "Create tools/keterdoc/extract-seci-relationships.py to build dependency graph.",
        "acceptance_criteria": [
            "File: `tools/keterdoc/extract-seci-relationships.py`",
            "CLI: `extract-seci-relationships.py --path apps/ --output seci-graph.json`",
            "Parses all artifacts, extracts seci.derives_from and seci.informs",
            "Outputs graph JSON: nodes (artifacts) + edges (relationships)",
            "Detects cycles: warns if circular dependencies found",
            "Generates Mermaid diagram: `--format mermaid` option",
            "Unit tests: 5 test cases (simple graph, cycles, orphaned nodes)",
        ],
        "dependencies": "REQ-001, REQ-002",
        "validation_method": "Generates graph from 50 test artifacts",
        "result_type": "intermediate",
        "associated_causes": "cause-knowledge-graph",
        "associated_features": "feat-seci-extractor",
    },
    {
        "id": "022",
        "title": "Test Suite for All Tools",
        "priority": "High",
        "type": "Testing",
        "effort": "8 hours",
        "description": "Create tests/keterdoc/ with comprehensive unit tests for all 4 scripts.",
        "acceptance_criteria": [
            "Folder: `tests/keterdoc/`",
            "Files: test_convert.py, test_generate.py, test_validate.py, test_extract.py",
            "Coverage: >80% line coverage for all scripts",
            "Uses pytest framework",
            "Fixtures: test data in tests/keterdoc/fixtures/",
            "CI/CD integration: runs on every commit",
            "Test report: HTML coverage report generated",
        ],
        "dependencies": "REQ-018 through REQ-021",
        "validation_method": "All tests pass, coverage >80%",
        "result_type": "immediate",
        "associated_causes": "cause-quality-assurance",
        "associated_features": "feat-test-suite",
    },
    # Phase 5: Neo4j Integration (Week 7)
    {
        "id": "023",
        "title": "Script - YAML-LD to RDF Triples",
        "priority": "Critical",
        "type": "Tool",
        "effort": "16 hours",
        "description": "Create tools/neo4j/yaml-ld-to-rdf-triples.py to convert YAML-LD to RDF.",
        "acceptance_criteria": [
            "File: `tools/neo4j/yaml-ld-to-rdf-triples.py`",
            "Uses rdflib library for RDF generation",
            "CLI: `yaml-ld-to-rdf-triples.py --input concept.md --output concept.ttl --format turtle`",
            "Supports formats: turtle, n-triples, json-ld, xml",
            "Batch mode: processes entire directory",
            "Validates @context against context.jsonld",
            "Generates triples for: dc fields, seci relationships, artifact typing",
            "Unit tests: 10 test cases (simple, complex, invalid)",
        ],
        "dependencies": "REQ-001, REQ-002",
        "validation_method": "Generates valid RDF triples for 20 test artifacts",
        "result_type": "immediate",
        "associated_causes": "cause-rdf-generation",
        "associated_features": "feat-rdf-converter",
    },
    {
        "id": "024",
        "title": "Script - Import RDF Triples to Neo4j",
        "priority": "Critical",
        "type": "Tool",
        "effort": "16 hours",
        "description": "Create tools/neo4j/import-rdf-to-neo4j.py for RDF → Neo4j import.",
        "acceptance_criteria": [
            "File: `tools/neo4j/import-rdf-to-neo4j.py`",
            "CLI: `import-rdf-to-neo4j.py --input concept.ttl --neo4j-uri bolt://localhost:7687`",
            "Uses neosemantics (n10s) plugin for RDF import",
            "Creates nodes: (:Concept {id, title, version})",
            "Creates relationships: (:Concept)-[:DERIVES_FROM]->(:Paper)",
            "Batch import: processes directory of .ttl files",
            "Performance: imports 1000 artifacts in <5 minutes",
            "Dry-run mode: shows Cypher queries without executing",
            "Unit tests: 8 test cases (simple, batch, error handling)",
        ],
        "dependencies": "REQ-023",
        "validation_method": "Imports 100 test artifacts to Neo4j successfully",
        "result_type": "intermediate",
        "associated_causes": "cause-neo4j-integration",
        "associated_features": "feat-neo4j-importer",
    },
    {
        "id": "025",
        "title": "Create Semantic Query Examples",
        "priority": "High",
        "type": "Documentation",
        "effort": "8 hours",
        "description": "Create tools/neo4j/semantic-queries/ with 10 example Cypher queries.",
        "acceptance_criteria": [
            "Folder: `tools/neo4j/semantic-queries/`",
            "10 files: query-01 through query-10 (.cypher extension)",
            "Queries cover: concept lineage, knowledge flow, orphaned concepts, artifact counts, collaboration, patterns, temporal evolution, circular dependencies, trazabilidad reports",
            "Each query includes: description, example usage, expected output",
            "README.md with query explanations",
        ],
        "dependencies": "REQ-024",
        "validation_method": "All 10 queries run successfully on test data",
        "result_type": "final",
        "associated_causes": "cause-knowledge-queries",
        "associated_features": "feat-semantic-queries",
    },
    {
        "id": "026",
        "title": "Document Neo4j Integration Guide",
        "priority": "High",
        "type": "Documentation",
        "effort": "8 hours",
        "description": "Create docs/guides/NEO4J-INTEGRATION.md explaining complete Neo4j workflow.",
        "acceptance_criteria": [
            "File: `docs/guides/NEO4J-INTEGRATION.md`",
            "Sections: Setup Neo4j, Install neosemantics, Generate RDF, Import Triples, Query Examples",
            "Includes docker-compose.yml for Neo4j setup",
            "Screenshots: Neo4j Browser showing knowledge graph",
            "Troubleshooting section: common errors and fixes",
            "Links to manifesto/02-arquitectura/04-sincronizacion-knowledge.md",
        ],
        "dependencies": "REQ-023 through REQ-025",
        "validation_method": "Developer follows guide and imports data successfully",
        "result_type": "final",
        "associated_causes": "cause-documentation",
        "associated_features": "feat-neo4j-guide",
    },
    # Phase 6: Pilot Migration (Week 8)
    {
        "id": "027",
        "title": "Backup Current Template",
        "priority": "Critical",
        "type": "Safety",
        "effort": "2 hours",
        "description": "Create complete backup of research-autopoietic-template before migration.",
        "acceptance_criteria": [
            "Backup: `apps/research-autopoietic-template.backup-YYYYMMDD/`",
            "Includes all files (ISSUE.yaml, artifacts, configs)",
            "Documented rollback procedure",
            "Git tag: `pre-keterdoc-migration`",
        ],
        "dependencies": "None",
        "validation_method": "Backup directory complete, can restore if needed",
        "result_type": "immediate",
        "associated_causes": "cause-safety",
        "associated_features": "feat-backup",
    },
    {
        "id": "028",
        "title": "Migrate ISSUE.yaml to ISSUE.md",
        "priority": "Critical",
        "type": "Migration",
        "effort": "4 hours",
        "description": "Convert research-autopoietic-template/ISSUE.yaml → ISSUE.md.",
        "acceptance_criteria": [
            "File: `research-autopoietic-template/ISSUE.md` (NEW)",
            "Contains YAML-LD frontmatter with KeterDoc metadata",
            "All ISSUE.yaml data preserved in Markdown body",
            "Validation: passes validate-keterdoc-compliance.py",
            "ISSUE.yaml renamed to ISSUE.yaml.deprecated (not deleted)",
        ],
        "dependencies": "REQ-018, REQ-020, REQ-027",
        "validation_method": "ISSUE.md validates, spec-workflow-mcp reads it successfully",
        "result_type": "intermediate",
        "associated_causes": "cause-migration",
        "associated_features": "feat-issue-migration",
    },
    {
        "id": "029",
        "title": "Migrate Existing Artifacts",
        "priority": "High",
        "type": "Migration",
        "effort": "16 hours",
        "description": "Convert 20+ existing artifacts to new templates.",
        "acceptance_criteria": [
            "Migrate: 020-conceive/02-atomics/ (10+ concept files)",
            "Migrate: 030-design/03-analyses/ (5+ analysis files)",
            "Migrate: 030-design/04-decisions/ (5+ decision files)",
            "All artifacts have YAML-LD frontmatter",
            "All artifacts pass validation",
            "seci.derives_from populated (e.g., concept → paper in 010-define)",
            "Generate migration report (successes, manual interventions needed)",
        ],
        "dependencies": "REQ-019, REQ-020, REQ-028",
        "validation_method": "All migrated artifacts validate, seci relationships correct",
        "result_type": "intermediate",
        "associated_causes": "cause-migration",
        "associated_features": "feat-artifact-migration",
    },
    {
        "id": "030",
        "title": "Test Obsidian Integration",
        "priority": "High",
        "type": "Testing",
        "effort": "4 hours",
        "description": "Verify ISSUE.md and artifacts work natively in Obsidian.",
        "acceptance_criteria": [
            "Open research-autopoietic-template in Obsidian",
            "ISSUE.md displays correctly (frontmatter + body)",
            "Artifacts display correctly",
            "Graph view shows links between artifacts",
            "YAML-LD frontmatter parseable by Obsidian plugins",
            "Can edit and save without corruption",
            "Wikilinks work: [[concept-graph-databases]]",
        ],
        "dependencies": "REQ-028, REQ-029",
        "validation_method": "Obsidian user verifies all features work",
        "result_type": "final",
        "associated_causes": "cause-obsidian-integration",
        "associated_features": "feat-obsidian-compat",
    },
    {
        "id": "031",
        "title": "Test spec-workflow-mcp Integration",
        "priority": "High",
        "type": "Testing",
        "effort": "4 hours",
        "description": "Verify spec-workflow-mcp processes ISSUE.md correctly.",
        "acceptance_criteria": [
            "spec-workflow-mcp reads ISSUE.md",
            "Generates requirements.md from ISSUE.md",
            "Generates tasks.md from requirements.md",
            "Respects workflow_pattern field",
            "No errors or warnings during processing",
        ],
        "dependencies": "REQ-028",
        "validation_method": "spec-workflow-mcp generates all expected files",
        "result_type": "final",
        "associated_causes": "cause-spec-workflow-integration",
        "associated_features": "feat-mcp-compat",
    },
    {
        "id": "032",
        "title": "Generate Neo4j Knowledge Graph",
        "priority": "High",
        "type": "Testing",
        "effort": "4 hours",
        "description": "Import all migrated artifacts to Neo4j and verify relationships.",
        "acceptance_criteria": [
            "All artifacts converted to RDF (yaml-ld-to-rdf-triples.py)",
            "All RDF imported to Neo4j (import-rdf-to-neo4j.py)",
            "Neo4j Browser shows: 20+ nodes, DERIVES_FROM relationships, INFORMS relationships",
            "Sample query works: 'Show all concepts derived from paper X'",
            "Performance: query response time <1 second",
        ],
        "dependencies": "REQ-023, REQ-024, REQ-029",
        "validation_method": "Neo4j graph visualizer shows complete knowledge tree",
        "result_type": "final",
        "associated_causes": "cause-knowledge-graph",
        "associated_features": "feat-neo4j-graph",
    },
    {
        "id": "033",
        "title": "Run Full Validation Suite",
        "priority": "Critical",
        "type": "Testing",
        "effort": "4 hours",
        "description": "Execute all validation scripts on migrated project.",
        "acceptance_criteria": [
            "validate-keterdoc-compliance.py: 100% pass rate",
            "extract-seci-relationships.py: no cycles detected",
            "All unit tests pass (tests/keterdoc/)",
            "All semantic queries return expected results",
            "Validation report generated (JSON + HTML)",
        ],
        "dependencies": "REQ-020, REQ-021, REQ-022, REQ-029",
        "validation_method": "All checkpoints pass, zero errors",
        "result_type": "immediate",
        "associated_causes": "cause-quality-assurance",
        "associated_features": "feat-validation-suite",
    },
    {
        "id": "034",
        "title": "Extract lesson-002-migration-validation",
        "priority": "High",
        "type": "Autopoiesis",
        "effort": "8 hours",
        "description": "Document lessons learned from pilot migration.",
        "acceptance_criteria": [
            "File: `060-reflect/lessons/lesson-002-migration-validation.md`",
            "YAML-LD + KeterDoc frontmatter (using lesson-tpl.md)",
            "seci.derives_from: chatlog of migration session",
            "Sections: What worked well, What didn't work, Adjustments made, Confidence score, Recommendations",
            "Updates pattern confidence scores (e.g., PATTERN-007 confidence 0.50 → 0.75)",
        ],
        "dependencies": "REQ-028 through REQ-033",
        "validation_method": "Lesson validates, confidence score justified",
        "result_type": "final",
        "associated_causes": "cause-autopoiesis",
        "associated_features": "feat-lessons-learned",
    },
    # Phase 7: Manifesto-Wide Specs + Index Coherence (Weeks 9-10)
    {
        "id": "035",
        "title": "Create Module 01-fundamentos Specs (4 specs)",
        "priority": "High",
        "type": "Specification",
        "effort": "32 hours",
        "description": "Create implementation specs for manifesto module 01-fundamentos: spec-002 (Visual identity), spec-003 (Árbol de la Vida), spec-004 (5 Rostros automation), spec-005 (P1-P10 compliance checker).",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-002/` through `spec-005/`",
            "Each has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md uses YAML-LD + KeterDoc format (like spec-001)",
            "Links to manifesto/01-fundamentos/ sections",
        ],
        "dependencies": "REQ-001 through REQ-034",
        "validation_method": "All 4 specs created, follow template structure",
        "result_type": "intermediate",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-fundamentos-specs",
    },
    {
        "id": "036",
        "title": "Create Module 02-arquitectura Specs (5 specs)",
        "priority": "High",
        "type": "Specification",
        "effort": "40 hours",
        "description": "Create implementation specs for manifesto module 02-arquitectura: spec-006 through spec-010 (Research Instance validator, Checkpoints automation, KnowledgeWriter API, Autopoiesis system, KeterDoc validation suite).",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-006/` through `spec-010/`",
            "Each has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md uses YAML-LD + KeterDoc format",
            "Links to manifesto/02-arquitectura/ sections",
        ],
        "dependencies": "REQ-035",
        "validation_method": "All 5 specs created",
        "result_type": "intermediate",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-arquitectura-specs",
    },
    {
        "id": "037",
        "title": "Create Module 03-workflow Specs (4 specs)",
        "priority": "High",
        "type": "Specification",
        "effort": "32 hours",
        "description": "Create implementation specs for manifesto module 03-workflow: spec-011 through spec-014 (Kanban integration, Trazabilidad visualizer, Versionamiento automation, MCPs guide).",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-011/` through `spec-014/`",
            "Each has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md uses YAML-LD + KeterDoc format",
            "Links to manifesto/03-workflow/ sections",
        ],
        "dependencies": "REQ-036",
        "validation_method": "All 4 specs created",
        "result_type": "intermediate",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-workflow-specs",
    },
    {
        "id": "038",
        "title": "Create Module 04-implementacion Specs (3 specs)",
        "priority": "Medium",
        "type": "Specification",
        "effort": "24 hours",
        "description": "Create implementation specs for manifesto module 04-implementacion: spec-015 through spec-017 (Flujo-completo wizard, Lessons extraction automation, Interactive checklist validator).",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-015/` through `spec-017/`",
            "Each has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md uses YAML-LD + KeterDoc format",
            "Links to manifesto/04-implementacion/ sections",
        ],
        "dependencies": "REQ-037",
        "validation_method": "All 3 specs created",
        "result_type": "intermediate",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-implementacion-specs",
    },
    {
        "id": "039",
        "title": "Create Module 05-casos-estudio Specs (2 specs)",
        "priority": "Low",
        "type": "Documentation",
        "effort": "16 hours",
        "description": "Create documentation specs for manifesto module 05-casos-estudio: spec-018 (CASO-01-DDD), spec-019 (CASO-02-PROMPTS-DINAMICOS).",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-018/` and `spec-019/`",
            "Each has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md uses YAML-LD + KeterDoc format",
            "Links to manifesto/05-casos-estudio/ sections",
        ],
        "dependencies": "REQ-038",
        "validation_method": "All 2 specs created",
        "result_type": "intermediate",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-casos-specs",
    },
    {
        "id": "040",
        "title": "Create Module 06-referencias Specs (1 spec)",
        "priority": "Low",
        "type": "Tool",
        "effort": "8 hours",
        "description": "Create tool spec for manifesto module 06-referencias: spec-020 (Glosario kabalístico with search).",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-020/`",
            "Has: ISSUE.md, spec-config.yaml, requirements.md, design.md, tasks.md",
            "ISSUE.md uses YAML-LD + KeterDoc format",
            "Links to manifesto/06-referencias/ sections",
        ],
        "dependencies": "REQ-039",
        "validation_method": "spec-020 created",
        "result_type": "intermediate",
        "associated_causes": "cause-manifesto-implementation",
        "associated_features": "feat-referencias-spec",
    },
    {
        "id": "041",
        "title": "Create Master Index (spec-021)",
        "priority": "Critical",
        "type": "Documentation + Architecture",
        "effort": "16 hours",
        "description": "Rebuild docs/manifiesto/00-master-index.md with results chain and conceptualization map.",
        "acceptance_criteria": [
            "Folder: `.spec-workflow/specs/spec-021-master-index-coherence/`",
            "Files: ISSUE.md (YAML-LD + KeterDoc), requirements.md, design.md",
            "Deliverable: `docs/manifiesto/00-master-index.md` (NEW)",
            "Sections: Results Chain (Mermaid), Conceptualization Map, Implementation Status, Product Vision",
            "Deliverable: `docs/manifiesto/00-conceptualization-map.mermaid`",
            "Validation: All 20 previous specs referenced, no orphaned specs",
        ],
        "dependencies": "REQ-035 through REQ-040",
        "validation_method": "Master index shows complete system coherence, conceptualization map visualizes interconnections",
        "result_type": "final",
        "associated_causes": "cause-system-coherence",
        "associated_features": "feat-master-index",
    },
    {
        "id": "042",
        "title": "Generate Implementation Status Tracker",
        "priority": "High",
        "type": "Documentation",
        "effort": "8 hours",
        "description": "Create docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md for tracking.",
        "acceptance_criteria": [
            "File: `docs/guides/MANIFESTO-IMPLEMENTATION-STATUS.md`",
            "Table: Module | Specs | Status | Completion % | Next Actions",
            "Progress bars (visual)",
            "Links to each spec's ISSUE.md",
            "Auto-generated from spec folders (script: generate-status.py)",
            "CI/CD: updates automatically on spec changes",
        ],
        "dependencies": "REQ-035 through REQ-041",
        "validation_method": "Status document accurate, updates automatically",
        "result_type": "final",
        "associated_causes": "cause-tracking",
        "associated_features": "feat-status-tracker",
    },
    {
        "id": "043",
        "title": "Validate Complete System Coherence",
        "priority": "Critical",
        "type": "Testing",
        "effort": "8 hours",
        "description": "Run comprehensive validation across all 21 specs and 6 modules.",
        "acceptance_criteria": [
            "All 21 specs created (spec-001 through spec-021)",
            "All specs use YAML-LD + KeterDoc format",
            "All specs link to manifesto sections (seci.source)",
            "No orphaned documentation (every manifesto section → spec)",
            "Master index shows complete results chain",
            "Conceptualization map visualizes system",
            "Implementation status tracker accurate",
        ],
        "dependencies": "REQ-041, REQ-042",
        "validation_method": "Coherence validation script passes 100%",
        "result_type": "immediate",
        "associated_causes": "cause-quality-assurance",
        "associated_features": "feat-system-validation",
    },
    {
        "id": "044",
        "title": "Extract lesson-003-manifesto-coherence",
        "priority": "High",
        "type": "Autopoiesis",
        "effort": "8 hours",
        "description": "Document lessons learned from Phase 7 (manifesto-wide implementation).",
        "acceptance_criteria": [
            "File: `060-reflect/lessons/lesson-003-manifesto-coherence.md`",
            "YAML-LD + KeterDoc frontmatter",
            "seci.derives_from: chatlog of Phase 7 sessions",
            "Sections: How master index improves understanding, Challenges creating 21 specs, Value of conceptualization map, Recommendations, Confidence score evolution",
            "Updates MELQUISEDEC system confidence (overall 0.00 → 0.90)",
        ],
        "dependencies": "REQ-043",
        "validation_method": "Lesson validates, system confidence justified",
        "result_type": "final",
        "associated_causes": "cause-autopoiesis",
        "associated_features": "feat-manifesto-lesson",
    },
]

TEMPLATE = """---
'@context':
  '@vocab': 'https://schema.org/'
  dc: 'http://purl.org/dc/terms/'
  mel: 'https://melquisedec.org/ns/'
'@type': 'Requirement'
'@id': 'https://melquisedec.org/req/REQ-{req_id}'
dc:title: 'REQ-{req_id}: {title}'
dc:created: '2026-01-10'
dc:creator:
  '@type': 'Person'
  foaf:name: 'GitHub Copilot'
version: '0.1.0'
status: 'draft'
template_root: 'template-configurable_daath-zen-root.md'
artifact_template: 'daath-zen-req-template.md'
manifesto_coherence:
  - file: 'docs/manifiesto/02-arquitectura/03-templates-hkm.md'
    lines: '120-220'
    rationale: 'Requirement follows KeterDoc standard with RBM-GAC mapping.'
---

# REQ-{req_id}: {title}

**Generated From:** `_templates/daath-zen-patterns/daath-zen-req-template.md`

**Metadata**:

- **result_type**: {result_type}
- **associated_causes**: {associated_causes}
- **associated_features**: {associated_features}
- **priority**: {priority}
- **type**: {req_type}
- **effort**: {effort}

---

## Summary

{description}

---

## 1. Problem Statement

This requirement addresses the need for {title} as part of the KeterDoc architecture implementation (spec-001).

## 2. Requirement Specification

### 2.1 Description

{description}

### 2.2 Acceptance Criteria

{acceptance_criteria}

## 3. Dependencies and Constraints

**Dependencies**: {dependencies}

**Validation Method**: {validation_method}

## 4. Implementation Guidance

This requirement should be implemented following the DAATH-ZEN configurable template pattern and validated against the acceptance criteria listed above.

---

*Generated: 2026-01-10 | Template: daath-zen-req-template.md | Status: draft*
"""


def generate_requirement(req_data):
    """Generate a single requirement file from data."""
    req_id = req_data["id"]
    acceptance_criteria_text = "\n".join([f"- [ ] {ac}" for ac in req_data["acceptance_criteria"]])

    content = TEMPLATE.format(
        req_id=req_id,
        title=req_data["title"],
        result_type=req_data["result_type"],
        associated_causes=req_data["associated_causes"],
        associated_features=req_data["associated_features"],
        priority=req_data["priority"],
        req_type=req_data["type"],
        effort=req_data["effort"],
        description=req_data["description"],
        acceptance_criteria=acceptance_criteria_text,
        dependencies=req_data["dependencies"],
        validation_method=req_data["validation_method"],
    )

    return content


def main():
    """Generate all requirements REQ-011 through REQ-052."""
    output_dir = Path(
        r"c:\proyectos\aleia-melquisedec\apps\research-autopoietic-template\010-define\workbooks"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating {len(REQUIREMENTS)} requirements...")

    for req in REQUIREMENTS:
        req_id = req["id"]
        filename = f"REQ-{req_id}-{req['title'].lower().replace(' ', '-').replace('(', '').replace(')', '')[:50]}.md"
        filepath = output_dir / filename

        content = generate_requirement(req)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✓ Created {filename}")

    print(f"\n✅ Successfully generated {len(REQUIREMENTS)} requirements in {output_dir}")
    print(f"   REQ-011 through REQ-{REQUIREMENTS[-1]['id']}")


if __name__ == "__main__":
    main()
