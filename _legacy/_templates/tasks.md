# Tasks

## PHASE 1: Research & Formal Specification

- [x] R1.1. Analyze docker/genai-stack architecture
  - File: apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/genai-stack.md
  - _Requirements: REQ-1_
  - _Rostro: HYPATIA_
  - _MCPs: base=[neo4j, memory] | specialized=[brave-search, fetch-webpage, filesystem]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r1.1-genai-stack.md_
  - _Prompt: Role: HYPATIA Researcher | Task: Analyze docker/genai-stack repository, extract Neo4j Vector Index implementation, multi-provider embeddings, hybrid query patterns, LangChain LCEL composition, testing strategy | Restrictions: Focus on production-ready patterns, document strengths AND weaknesses | Success: 897-line analysis with 7 patterns extracted, 3 refactored to Hexagonal Architecture_

- [ ] R1.2. Analyze LlamaIndex Neo4j integration
  - File: apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/frameworks/llamaindex.md
  - _Requirements: REQ-1_
  - _Rostro: HYPATIA_
  - _MCPs: base=[neo4j, memory] | specialized=[context7, fetch-webpage, filesystem]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r1.2-llamaindex.md_
  - _Prompt: Role: HYPATIA Researcher | Task: Analyze llama-index-vector-stores-neo4j, extract Neo4jVectorStore interface, query methods, configuration patterns, compare against LangChain Neo4jVector | Restrictions: Document API completeness, identify gaps vs genai-stack | Success: ≥400 line analysis with code examples, comparative matrix_

- [ ] R1.3. Extract hybrid query patterns from Tomasonjo blogs
  - File: apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/best-practices/hybrid-queries.md
  - _Requirements: REQ-1_
  - _Rostro: HYPATIA_
  - _MCPs: base=[neo4j, memory] | specialized=[brave-search, fetch-webpage, markdown-converter]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r1.3-hybrid-patterns.md_
  - _Prompt: Role: HYPATIA Researcher | Task: Search Tomaso Njo Neo4j blogs, extract Cypher patterns combining vector similarity + graph traversal, RAG architectures, knowledge graph construction best practices | Restrictions: Focus on production-ready patterns with benchmarks | Success: ≥300 line analysis with ≥5 hybrid query patterns_

- [ ] R1.4. Comparative analysis: Haystack vs LangChain vs LlamaIndex
  - File: apps/research-neo4j-llamaindex-architecture/01-design/state-of-art/comparative-analysis.md
  - _Requirements: REQ-1_
  - _Rostro: HYPATIA_
  - _MCPs: base=[neo4j, memory] | specialized=[github-mcp, sequential-thinking]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r1.4-comparative.md_
  - _Prompt: Role: HYPATIA Researcher | Task: Compare Haystack, LangChain, LlamaIndex for Neo4j integration, create matrix (ease of use, flexibility, performance, community support, Neo4j maturity), recommend framework for MELQUISEDEC | Restrictions: Use objective metrics, cite GitHub stats, documentation quality | Success: Comparative matrix + justified recommendation_

- [ ] R1.5. MELQUISEDEC validation checkpoint for research phase
  - File: apps/research-neo4j-llamaindex-architecture/.melquisedec/hypatia_validation.yaml
  - _Requirements: REQ-1_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, grep-search]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r1.5-validation.md_
  - _Prompt: Role: MELQUISEDEC Validator | Task: Verify ≥4 frameworks analyzed, ≥20 code patterns extracted, ≥5 RQs answered with evidence, comparative analysis complete, hypothesis updated based on findings | Restrictions: Flag incomplete analysis, require evidence citations | Success: validation.yaml with checklist, all items ✅ or documented resolution plan_

- [ ] R2.1. Design hexagonal architecture for MELQUISEDEC
  - File: apps/research-neo4j-llamaindex-architecture/01-design/architecture/hexagonal-architecture.md
  - _Requirements: REQ-2_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, sequential-thinking]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r2.1-hexagonal.md_
  - _Prompt: Role: SALOMON Architect | Task: Design Hexagonal Architecture based on R1 findings, define layers (domain/application/infrastructure/interfaces), specify 8 Ports (VectorStorePort, EmbeddingServicePort, etc.), create C4 diagrams (Context/Container/Component/Code), write ADR-003 | Restrictions: Follow DDD principles, justify with research findings | Success: ≥800 line architecture spec with diagrams, ADR, package structure_

- [ ] R2.2. Create C4 diagrams for all architecture levels
  - File: apps/research-neo4j-llamaindex-architecture/01-design/architecture/c4-diagrams/
  - _Requirements: REQ-2_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r2.2-c4-diagrams.md_
  - _Prompt: Role: SALOMON Architect | Task: Create C4 diagrams in Mermaid format: Level 1 (Context: MELQUISEDEC + external systems), Level 2 (Container: packages), Level 3 (Component: internal modules), Level 4 (Code: key class diagrams) | Restrictions: Use Mermaid syntax, follow C4 model conventions | Success: 4 diagram files, each level properly detailed_

- [ ] R2.3. Define 8 Ports as Python Protocols
  - File: apps/research-neo4j-llamaindex-architecture/01-design/contracts/ports/
  - _Requirements: REQ-2_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r2.3-ports.md_
  - _Prompt: Role: SALOMON Architect | Task: Define 8 Ports as typing.Protocol: VectorStorePort, EmbeddingServicePort, GraphRepositoryPort, LLMPort, ChunkingPort, CachePort, ConfigPort, LoggingPort, include type hints, docstrings, method signatures | Restrictions: Use Protocol (not ABC), follow PEP 544 | Success: 8 .py files with complete Protocol definitions_

- [ ] R3.1. Write testing strategy document
  - File: apps/research-neo4j-llamaindex-architecture/01-design/contracts/testing-strategy.md
  - _Requirements: REQ-3_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, sequential-thinking]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r3.1-testing-strategy.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Write TDD testing strategy: Red-Green-Refactor workflow, test pyramid (unit 70%, integration 20%, e2e 10%), pytest fixtures for Neo4j (testcontainers), mocking strategies for Ports, coverage requirements (≥80%), SonarQube integration | Restrictions: Follow pytest best practices, ensure testability of Hexagonal Architecture | Success: ≥600 line strategy with examples, fixtures templates, coverage config_

- [ ] R3.2. Configure SonarQube quality gates
  - File: apps/research-neo4j-llamaindex-architecture/02-build/sonarqube-config/
  - _Requirements: REQ-3_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r3.2-sonarqube.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Configure SonarQube quality gates: coverage ≥80%, 0 code smells, 0 security hotspots, maintainability rating A, cognitive complexity <15, create sonar-project.properties + quality-profiles.json | Restrictions: Strict Python rules, no exceptions for legacy code | Success: SonarQube configs pass on sample code_

- [ ] R4.1. Write formal solution specification document
  - File: apps/research-neo4j-llamaindex-architecture/02-build/formal-solution-spec.md
  - _Requirements: REQ-4_
  - _Rostro: SALOMON+HYPATIA_
  - _MCPs: base=[neo4j, memory] | specialized=[sequential-thinking, filesystem]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r4.1-formal-spec.md_
  - _Prompt: Role: SALOMON+HYPATIA | Task: Consolidate research (R1), architecture (R2), testing (R3) into formal blueprint: Executive Summary, Architecture (Hexagonal), Ports, Adapters, Testing Strategy, Implementation Plan, Quality Assurance, References | Restrictions: ≥2000 lines, cite all research sources, include code examples | Success: Complete spec ready for implementation, validated by MELQUISEDEC_

- [ ] R4.2. Create implementation checklist
  - File: apps/research-neo4j-llamaindex-architecture/02-build/implementation-checklist.md
  - _Requirements: REQ-4_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r4.2-checklist.md_
  - _Prompt: Role: SALOMON Architect | Task: Create implementation checklist (≥50 items) covering: infrastructure setup (Docker, Neo4j, Ollama), domain entities, ports, adapters (Neo4j, Ollama, Chroma), use cases, tests (unit/integration/e2e), documentation, CI/CD | Restrictions: Atomic tasks, clear acceptance criteria per item | Success: Checklist with grouped items, dependencies marked, estimated hours_

- [ ] R4.3. MELQUISEDEC final validation
  - File: apps/research-neo4j-llamaindex-architecture/.melquisedec/final_validation.yaml
  - _Requirements: REQ-4_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[sequential-thinking, grep-search]_
  - _Lesson: apps/research-neo4j-llamaindex-architecture/04-lessons/r4.3-final-validation.md_
  - _Prompt: Role: MELQUISEDEC Validator | Task: Validate Phase 1 completeness: formal spec ≥2000 lines, architecture diagrams complete, 8 Ports defined, testing strategy documented, implementation checklist ready, all lessons captured, hypothesis validated | Restrictions: Block Phase 2 if gaps detected | Success: final_validation.yaml ✅, approved to proceed to Phase 2_

## PHASE 2: Documentation Coherence

- [ ] 0.1. Update architecture documentation
  - File: docs/architecture/*.md
  - _Requirements: REQ-5_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem, grep-search]_
  - _Lesson: lessons-learned/task-0.1-update-docs.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Update docs/architecture/ to reflect Hexagonal Architecture design from R2, add references to formal spec, update ADR-003, sync structure with research findings | Restrictions: Preserve existing ADRs, maintain markdown link integrity | Success: All architecture docs reference research, no broken links_

- [ ] 0.2. Update DAATH templates with research findings
  - File: _templates/daath-zen-patterns/*.md
  - _Requirements: REQ-5_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: lessons-learned/task-0.2-update-templates.md_
  - _Prompt: Role: ALMA Publisher | Task: Update DAATH-ZEN templates to include patterns from R1 research (genai-stack patterns, hybrid queries, LlamaIndex integration), add rostro-specific guidance for Neo4j/Ollama work | Restrictions: Maintain DAATH-ZEN v2.0.0 structure | Success: Templates enriched with production-ready patterns_

- [ ] 0.3. Update test fixtures and mocks
  - File: tests/fixtures/*.py, packages/daath-toolkit/testing/mocks.py
  - _Requirements: REQ-5_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: lessons-learned/task-0.3-update-fixtures.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Create Neo4j fixtures using testcontainers, create mock implementations for 8 Ports, add sample embeddings data, configure pytest for async tests | Restrictions: Follow testing strategy from R3.1 | Success: Fixtures reusable across test suites, all Ports have mocks_

- [ ] 0.4. Update infrastructure configuration
  - File: infrastructure/docker/docker-compose.yml, tools/setup/*.sh
  - _Requirements: REQ-5_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: lessons-learned/task-0.4-update-infra.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Update docker-compose.yml based on genai-stack architecture (Neo4j 5.26, Ollama, health checks, profiles), create setup scripts for HNSW index, add environment variable templates | Restrictions: Follow research recommendations from R1.1 | Success: Docker stack starts Neo4j with vector index, Ollama with qwen3-embedding_

- [ ] 0.5. Validate documentation coherence
  - File: ALL_DOCUMENTATION
  - _Requirements: REQ-5_
  - _Rostro: MELQUISEDEC_
  - _MCPs: base=[neo4j, memory] | specialized=[grep-search, filesystem]_
  - _Lesson: lessons-learned/task-0.5-validate-coherence.md_
  - _Prompt: Role: MELQUISEDEC Validator | Task: Validate all documentation references research findings consistently, check cross-references (architecture ↔ research ↔ requirements), verify no orphan documents, ensure lessons captured | Restrictions: Block Phase 3 if inconsistencies found | Success: Documentation coherence report ✅, no broken references_

## PHASE 3: Implementation with TDD + QA

- [ ] 1.1. Implement domain entities
  - File: packages/daath-toolkit/domain/entities/*.py
  - _Requirements: REQ-6_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: lessons-learned/task-1.1-domain-entities.md_
  - _Prompt: Role: SALOMON Architect | Task: TDD implement domain entities (Document, Chunk, Embedding, Lesson), write tests first (Red), implement (Green), refactor (Refactor), ensure 80% coverage | Restrictions: Follow DDD principles, no infrastructure dependencies | Success: Tests pass, coverage ≥80%, SonarQube A rating_

- [ ] 1.2. Implement 8 Ports and adapters
  - File: packages/daath-toolkit/domain/ports/*.py, infrastructure/adapters/*.py
  - _Requirements: REQ-6_
  - _Rostro: SALOMON+MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: lessons-learned/task-1.2-ports-adapters.md_
  - _Prompt: Role: SALOMON+MORPHEUS | Task: TDD implement 8 Ports (Protocols) + 3 key adapters (Neo4jVectorStoreAdapter, OllamaEmbeddingAdapter, Neo4jGraphAdapter), use mocks for testing, follow patterns from R1 research | Restrictions: Adapters implement Ports exactly, no coupling | Success: All tests pass, adapters switchable via DI_

- [ ] 1.3. Implement document processing pipeline
  - File: packages/daath-toolkit/application/use_cases/ingest_document.py
  - _Requirements: REQ-6_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: lessons-learned/task-1.3-pipeline.md_
  - _Prompt: Role: SALOMON Architect | Task: TDD implement IngestDocumentUseCase: load markdown → statistical analysis → semantic chunking (LlamaIndex MarkdownNodeParser) → generate embeddings (Ollama) → store (Neo4j vector index + graph), follow pipeline from research | Restrictions: Use Ports only, async/await, handle errors | Success: End-to-end test from markdown to Neo4j_

- [ ] 1.4. Implement hybrid query use case
  - File: packages/daath-toolkit/application/use_cases/query_knowledge_base.py
  - _Requirements: REQ-6_
  - _Rostro: SALOMON_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: lessons-learned/task-1.4-hybrid-query.md_
  - _Prompt: Role: SALOMON Architect | Task: TDD implement QueryKnowledgeBaseUseCase: convert query to embedding → vector similarity search (Neo4j HNSW) → graph traversal (related lessons) → fusion (RRF), use patterns from R1.3 | Restrictions: Custom Cypher retrieval query, configurable top_k | Success: Integration test with testcontainers Neo4j_

- [ ] 1.5. Implement Neo4j schema manager
  - File: packages/daath-toolkit/infrastructure/adapters/neo4j/schema_manager.py
  - _Requirements: REQ-6_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[python-refactoring, python-env]_
  - _Lesson: lessons-learned/task-1.5-schema-manager.md_
  - _Prompt: Role: MORPHEUS Designer | Task: TDD implement SchemaManager: idempotent vector index creation (HNSW with explicit config), constraint creation (unique IDs), index status validation, follow pattern_2 from R1.1 | Restrictions: Structured logging (structlog), retry on transient failures | Success: Tests verify index creation, status check, idempotency_

- [ ] 1.6. Configure CI/CD with SonarQube quality gates
  - File: .github/workflows/ci.yml, sonar-project.properties
  - _Requirements: REQ-6_
  - _Rostro: MORPHEUS_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: lessons-learned/task-1.6-cicd.md_
  - _Prompt: Role: MORPHEUS Designer | Task: Configure GitHub Actions CI: run pytest with coverage, upload to SonarQube, enforce quality gates (coverage ≥80%, 0 smells), block merge if fails | Restrictions: Use testcontainers in CI, cache dependencies | Success: CI passes with all quality gates ✅_

- [ ] 1.7. Generate lessons-learned summary
  - File: .spec-workflow/specs/triple-persistence-architecture-best-practices/lessons-learned/summary.yaml
  - _Requirements: ALL_
  - _Rostro: ALMA_
  - _MCPs: base=[neo4j, memory] | specialized=[filesystem]_
  - _Lesson: lessons-learned/summary.yaml (self-documenting)_
  - _Prompt: Role: ALMA Publisher | Task: Aggregate all lessons from R1-R4 + Phase 2 + Phase 3, extract patterns (research methodology, architecture decisions, TDD workflow, obstacles overcome), calculate confidence scores, identify reusable patterns | Restrictions: Only include validated lessons with evidence | Success: summary.yaml with aggregated insights, ready for DAATH knowledge base_
