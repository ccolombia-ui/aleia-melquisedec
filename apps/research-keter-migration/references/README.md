# Research: Keter Migration - References

> **Purpose**: External documentation, papers, prior analysis
> **Status**: Updated 2026-01-08

## 📚 Internal References (Prior Work)

### Sprint 1-2 Analysis (research-keter-integration-v1.0.0)

**Location**: `.spec-workflow/specs/research-keter-integration-v1.0.0/`

1. **Orchestrator**
   - File: `_meta/orchestrator.md`
   - Content: 350-line orchestrator, 6 phases, 4 sprints
   - Relevant: Methodology for structured research

2. **Keter Raw Data**
   - File: `Implementation Logs/analysis/keter-raw-data.md`
   - Content: 295 lines, 13 sections (services, MCP tools, coverage, schemas)
   - Relevant: Baseline data for dependency audit

3. **Keter Evaluation**
   - File: `Implementation Logs/analysis/keter-evaluation.md`
   - Content: ~300 lines, ComponentMetadata + Scorecard
   - Relevant: Independence score 4/10, reusability 6/10

4. **Keter Decision**
   - File: `Implementation Logs/analysis/keter-decision.md`
   - Content: ~400 lines, decision tree execution
   - Relevant: Original decision (keep in bereshit) - NOW INVALIDATED

5. **ADR-002 Keter Integration Decision**
   - File: `docs/architecture/ADR-002-keter-integration-decision.md`
   - Content: ~500 lines, hybrid approach (keep app, extract patterns)
   - Relevant: Original decision + extraction plans - NOW OBSOLETE

6. **Policy Engine Extraction Plan**
   - File: `Implementation Logs/extraction-plans/policy-engine-plan.md`
   - Content: ~400 lines, detailed extraction plan
   - Relevant: Abstraction patterns (IStorageAdapter, etc.)

7. **MCP Server Template Plan**
   - File: `Implementation Logs/extraction-plans/mcp-server-template-plan.md`
   - Content: ~500 lines, template with placeholder system
   - Relevant: MCP architecture patterns

8. **Keter Analysis Case Study**
   - File: `docs/manifiesto/05-casos-estudio/keter-analysis.md`
   - Content: ~600 lines, complete case study
   - Relevant: Replicable methodology, lessons learned

**Total Prior Work**: ~3000 lines of analysis + documentation

---

## 🔗 External References

### Neo4j Documentation

1. **Neo4j 5.15+ Vector Index**
   - URL: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
   - Relevant: Native vector index (no external vector DB needed)

2. **Neo4j ACID Transactions**
   - URL: https://neo4j.com/docs/cypher-manual/current/transactions/
   - Relevant: Guarantees for graph + vector consistency

### TypeScript Best Practices

3. **Dependency Injection in TypeScript**
   - URL: https://www.typescriptlang.org/docs/handbook/2/classes.html
   - Relevant: Constructor injection pattern

4. **TypeScript Interfaces for Abstraction**
   - URL: https://www.typescriptlang.org/docs/handbook/2/interfaces.html
   - Relevant: Interface design for abstraction layers

### Testing Strategies

5. **Test-Driven Refactoring**
   - URL: https://martinfowler.com/articles/refactoring-2nd-changes.html
   - Relevant: Maintain coverage during refactoring

6. **Testing Best Practices**
   - URL: https://testing-library.com/docs/guiding-principles/
   - Relevant: Unit vs integration test strategies

### Architecture Patterns

7. **Hexagonal Architecture**
   - URL: https://alistair.cockburn.us/hexagonal-architecture/
   - Relevant: Ports & adapters pattern for abstractions

8. **Clean Architecture**
   - URL: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
   - Relevant: Dependency inversion principle

### Monorepo Patterns

9. **Turborepo Documentation**
   - URL: https://turbo.build/repo/docs
   - Relevant: Modular package management

10. **Nx Monorepo Patterns**
    - URL: https://nx.dev/concepts/more-concepts/applications-and-libraries
    - Relevant: Apps vs libraries structure

### Similar Migrations

11. **LlamaIndex Package Structure**
    - URL: https://github.com/run-llama/llama_index/tree/main/llama-index-core
    - Relevant: Modular package architecture (core, integrations, etc.)

12. **Langchain Modular Architecture**
    - URL: https://github.com/langchain-ai/langchain/tree/master/libs
    - Relevant: Split into langchain-core, langchain-community

---

## 📖 Research Papers (Optional)

### Design Science Research

13. **Hevner et al. (2004) - Design Science in IS Research**
    - Citation: MIS Quarterly, Vol. 28, No. 1, pp. 75-105
    - Relevant: DSR methodology foundations

14. **Peffers et al. (2007) - DSR Process Model**
    - Citation: Decision Support Systems, Vol. 45, No. 2, pp. 252-260
    - Relevant: 6-step DSR process (problem → design → build → evaluate)

---

## 🔍 Tools & Resources

### Static Analysis Tools

15. **Madge** (Dependency Graph)
    - URL: https://github.com/pahen/madge
    - Command: `npx madge --image deps.svg src/`

16. **Dependency Cruiser**
    - URL: https://github.com/sverweij/dependency-cruiser
    - Command: `npx depcruise --output-type dot src/`

### Testing Tools

17. **Vitest** (Unit Testing)
    - URL: https://vitest.dev/
    - Relevant: Fast TypeScript testing

18. **Playwright** (E2E Testing)
    - URL: https://playwright.dev/
    - Relevant: Integration testing

### Code Quality

19. **SonarQube**
    - URL: https://www.sonarqube.org/
    - Relevant: Code coverage tracking

20. **ESLint**
    - URL: https://eslint.org/
    - Relevant: Code quality enforcement

---

## 📝 Notes

- **Prior Work**: Sprint 1-2 provides solid foundation (~3000 lines docs)
- **Key Insight**: Original decision (keep in bereshit) invalidated by bereshit discontinuation
- **Leverage**: Extraction plans + case study still relevant for abstraction patterns

**Last Updated**: 2026-01-08
