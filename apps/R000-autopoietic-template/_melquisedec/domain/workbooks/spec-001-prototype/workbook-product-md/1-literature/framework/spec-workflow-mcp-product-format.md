# spec-workflow-mcp: product.md Format Specification

**Source Type**: Framework Documentation
**Source**: spec-workflow-mcp v1.1.2+ Official Template
**File**: `.spec-workflow/_meta/templates/spec-workflow-mcp-template/product-template.md`
**Date Accessed**: 2026-01-11
**Repository**: https://github.com/pimzino/spec-workflow-mcp
**Workbook**: workbook-product-md/
**Analyst**: SALOMÓN

---

## 1. Overview

**spec-workflow-mcp** is an MCP (Model Context Protocol) server that enables LLMs to manage specification-driven development workflows. The `product.md` file is one of three **Steering Documents** that provide project-level context.

### Steering Documents Hierarchy

```
.spec-workflow/
└── steering/                # Project-level strategic documents (OPTIONAL)
    ├── product.md           # ⭐ Product vision, users, goals, metrics
    ├── tech.md              # Technical stack, architecture principles
    └── structure.md         # Code organization, naming conventions
```

**Key Characteristics**:
- **Optional**: Not required for specs to function, but highly recommended
- **Project-level**: One per project, NOT per spec
- **Approval Required**: Must be approved via `mcp_spec-workflow2_approvals()` tool
- **Living Document**: Can evolve as the product matures

---

## 2. Official Template Structure

The official `product-template.md` from spec-workflow-mcp v1.1.2+ contains **7 main sections**:

### 2.1. Product Purpose

**Question**: What problem does this product solve?

**Content**:
- Core purpose statement (1-2 sentences)
- Problem domain description
- Value proposition

**Example** (from DAATH-ZEN project):
```markdown
## Product Purpose
Enable developers to create high-quality specifications 10x faster through
knowledge-driven templates powered by epistemological research methodologies
and GraphRAG semantic search.
```

---

### 2.2. Target Users

**Question**: Who are the primary users?

**Content**:
- User personas or roles
- User needs (what they want to achieve)
- User pain points (current frustrations)

**Example**:
```markdown
## Target Users

### Primary Users
- **Software Architects**: Need to document architectural decisions with traceability
- **Product Managers**: Need to create product.md with clear vision and metrics
- **Research Engineers**: Need to convert academic research into actionable specs

### User Needs
- Fast spec creation without sacrificing quality
- Automated literature synthesis
- GraphRAG-powered semantic search across concepts

### Pain Points
- Manual copy-paste from research papers is time-consuming
- Specs lack traceability to source literature
- Hard to maintain consistency across multiple specs
```

---

### 2.3. Key Features

**Question**: What are the main features that deliver value?

**Content**:
- Numbered list of 3-5 core features
- Feature name + description per item
- Focus on user-facing value, not technical implementation

**Format**:
```markdown
## Key Features

1. **Feature Name**: [Description of value delivered]
2. **Feature Name**: [Description of value delivered]
3. **Feature Name**: [Description of value delivered]
```

**Example**:
```markdown
## Key Features

1. **5-Workbook Epistemology**: Each artifact (product.md, requirements.md, etc.)
   has a self-contained workbook with literature → analysis → atomics → validation
   → ingestion → compilation flow.

2. **Scoping Review Methodology**: Research questions answered via Arksey & O'Malley
   framework with full source citations (no invented content).

3. **Neo4j GraphRAG**: All concepts ingested into graph database with CITED_IN,
   RELATES_TO, USED_IN relationships for semantic queries.

4. **Automated Validators**: Python-based validators (textstat readability,
   regex patterns) for automated quality checks.

5. **Jinja2 Compilation**: Templates compile from atomics/ with validation
   against 4-artefact/ contracts before output.
```

---

### 2.4. Business Objectives

**Question**: What business goals does this product aim to achieve?

**Content**:
- Bullet list of strategic objectives
- Focus on organizational impact, not just user features
- Measurable outcomes when possible

**Example**:
```markdown
## Business Objectives

- Reduce spec creation time by 90% (from 8 hours to 45 minutes per spec)
- Enable knowledge reuse across projects via atomic concepts
- Improve spec quality with automated validation (0 undocumented claims)
- Scale team productivity without hiring more documentation specialists
```

---

### 2.5. Success Metrics

**Question**: How will we measure product success?

**Content**:
- Metric name + target value per item
- Mix of quantitative (numbers) and qualitative (user satisfaction) metrics
- Time-bound when possible (e.g., "within Q1 2026")

**Format**:
```markdown
## Success Metrics

- [Metric Name]: [Target Value]
- [Metric Name]: [Target Value]
- [Metric Name]: [Target Value]
```

**Example**:
```markdown
## Success Metrics

- **Spec Creation Time**: < 1 hour per spec (90% reduction from 8-hour baseline)
- **Citation Coverage**: 100% of claims traceable to 1-literature/ sources
- **Validator Pass Rate**: ≥ 95% of specs pass automated validation on first try
- **User Adoption**: 3+ teams using DAATH-ZEN templates within Q1 2026
- **NPS (Net Promoter Score)**: ≥ 70 from pilot users
```

---

### 2.6. Product Principles

**Question**: What core principles guide product decisions?

**Content**:
- Numbered list of 3-5 principles
- Principle name + explanation per item
- Principles should be actionable (guide decision-making)

**Format**:
```markdown
## Product Principles

1. **[Principle Name]**: [Explanation of how this guides decisions]
2. **[Principle Name]**: [Explanation]
3. **[Principle Name]**: [Explanation]
```

**Example**:
```markdown
## Product Principles

1. **Autocontenido (Self-Contained)**: Every workbook contains ALL necessary
   elements (literature → validation → compilation) to generate its artifact.
   No external dependencies beyond 1-literature/ sources.

2. **Trazabilidad Total (Total Traceability)**: Every claim must cite a source.
   Use [source-name, page numbers] format. No invented content. If a statement
   cannot be cited, it should not exist.

3. **Epistemología Explícita (Explicit Epistemology)**: Make knowledge
   transformation visible: ENTRADA (1-literature/) → PROCESO (2-analysis/) →
   EXTRACCIÓN (3-atomics/) → VALIDACIÓN (4-artefact/) → COMPILACIÓN (5-compiler/)
   → INGESTA (6-outputs/).

4. **Metodología Documentada (Documented Methodology)**: Each workbook follows
   Scoping Review (Arksey & O'Malley 2005) for domain discovery, NOT IMRAD
   (which is for experiments). Methodology must be explicit in README.md.

5. **Automatización con Validación (Automation with Validation)**: Compilation
   is automated (Jinja2 templates), but MUST validate against 4-artefact/
   contracts before output. No "trust but verify" – validate then compile.
```

---

### 2.7. Monitoring & Visibility (Optional)

**Question**: How do users track progress and monitor the system?

**Content** (if applicable):
- Dashboard type (web, CLI, desktop)
- Real-time updates mechanism
- Key metrics displayed
- Sharing capabilities

**Example**:
```markdown
## Monitoring & Visibility

- **Dashboard Type**: VS Code Webview (spec-workflow-mcp approval dashboard)
- **Real-time Updates**: Polling every 2 seconds for approval status changes
- **Key Metrics Displayed**:
  - Approval status (pending/approved/rejected/needs-revision)
  - Document type (requirements/design/tasks/steering)
  - Timestamp of last update
  - Reviewer feedback (if rejected/needs-revision)
- **Sharing Capabilities**: Approval requests visible in MCP server dashboard,
  exportable to JSON for audit trails
```

---

### 2.8. Future Vision (Optional)

**Question**: Where do we see this product evolving?

**Content**:
- High-level future direction (not detailed roadmap)
- Potential enhancements (not commitments)
- Categories: Remote Access, Analytics, Collaboration

**Example**:
```markdown
## Future Vision

### Potential Enhancements

- **Remote Access**: Tunnel features for sharing spec-workflow dashboards with
  remote stakeholders (similar to ngrok for VS Code Webview)

- **Analytics**: Historical trends dashboard showing spec creation velocity,
  validator pass rates over time, most-cited literature sources

- **Collaboration**: Multi-user support with concurrent editing, commenting on
  specs, approval workflows with multiple reviewers

- **AI-Assisted Analysis**: LLM-powered literature synthesis suggestions,
  automated concept extraction from papers, smart recommendations for related
  concepts based on current workbook
```

---

## 3. Validation Rules

### 3.1. Mandatory Sections

**All product.md files MUST include**:
1. ✅ Product Purpose
2. ✅ Target Users
3. ✅ Key Features
4. ✅ Business Objectives
5. ✅ Success Metrics
6. ✅ Product Principles

**Optional sections**:
7. ⏸️ Monitoring & Visibility (only if product includes dashboard/UI)
8. ⏸️ Future Vision (recommended for strategic context)

### 3.2. Content Quality Checks

**Length Constraints**:
- Product Purpose: 1-3 paragraphs (100-300 words)
- Target Users: 3-5 user types with needs/pain points
- Key Features: 3-7 features with descriptions
- Business Objectives: 3-5 objectives
- Success Metrics: 4-8 metrics with targets
- Product Principles: 3-5 principles with explanations

**Clarity Constraints**:
- Use active voice, not passive ("Enable developers" not "Developers are enabled")
- Avoid vague buzzwords ("innovative", "cutting-edge", "revolutionary") without concrete examples
- Metrics must be measurable (include target values and time bounds)
- Principles must be actionable (guide decisions, not just platitudes)

### 3.3. Format Constraints

**Markdown Compliance**:
- Use `##` for main sections (level 2 headings)
- Use `###` for subsections (level 3 headings)
- Use `-` for unordered lists (not `*` or `+`)
- Use numbered lists for sequential items (Key Features, Product Principles)
- Include code blocks with language tags: ````markdown` not just ````

**File Naming**:
- MUST be named exactly `product.md` (lowercase, no prefix/suffix)
- MUST be placed in `.spec-workflow/steering/product.md`
- One product.md per project (not per spec)

---

## 4. Workflow Integration

### 4.1. Approval Process

**Steering documents require approval** via spec-workflow-mcp dashboard:

```python
# Step 1: Load steering guide
mcp_spec-workflow2_steering-guide()

# Step 2: Create product.md following template
create_file("../.spec-workflow/steering/product.md", content)

# Step 3: Request approval
mcp_spec-workflow2_approvals(
    action="request",
    type="document",
    category="steering",
    categoryName="steering",
    title="Request approval for product.md steering document",
    filePath=".spec-workflow/steering/product.md"
)

# Step 4: Poll status until approved
status = mcp_spec-workflow2_approvals(action="status", approvalId=approval_id)
while status == "pending":
    # Wait 5-10 seconds
    status = mcp_spec-workflow2_approvals(action="status", approvalId=approval_id)

# Step 5: Clean up approval request (after approved)
mcp_spec-workflow2_approvals(action="delete", approvalId=approval_id)

# Step 6: Repeat for tech.md and structure.md
```

**Approval States**:
- `pending`: Awaiting user review in dashboard
- `approved`: User approved, proceed with workflow
- `rejected`: User rejected, address feedback and recreate
- `needs-revision`: User requested changes, update and re-request

### 4.2. Timing

**Steering documents workflow** (all 3 documents: product.md, tech.md, structure.md):
- **Estimated time**: 1-2 hours (30-40 minutes per document)
- **When to create**:
  - At project initialization (before first spec)
  - When product vision changes significantly
  - When adding new product areas (optional update)

**Note**: Steering docs are OPTIONAL. You can start with specs (requirements.md, design.md, tasks.md) without steering docs. However, steering docs provide valuable context for LLMs working on specs.

---

## 5. Related Documents

### 5.1. Steering Documents Family

```
.spec-workflow/steering/
├── product.md           # ⭐ THIS DOCUMENT (product vision, users, goals)
├── tech.md              # Technical stack, architecture principles, ADRs
└── structure.md         # Code organization, naming conventions, module boundaries
```

**Relationship**:
- **product.md**: WHAT we're building and WHY (business/user perspective)
- **tech.md**: HOW we're building it (technical decisions)
- **structure.md**: WHERE things go (code organization)

### 5.2. Spec Documents (Per-Spec, Not Project-Level)

```
.spec-workflow/specs/{spec-name}/
├── requirements.md      # User stories, functional/non-functional requirements
├── design.md            # Architecture, ADRs, tech decisions
├── tasks.md             # Task breakdown with rostros + MCPs + prompts
└── implementation-log.md # Auto-generated logs (optional)
```

**Key Difference**:
- **Steering docs** (product.md, tech.md, structure.md): ONE per project, strategic, high-level
- **Spec docs** (requirements/design/tasks): MULTIPLE per project, tactical, feature-specific

---

## 6. Examples from Real Projects

### 6.1. DAATH-ZEN MELQUISEDEC (This Project)

**File**: `.spec-workflow/steering/product.md`

**Excerpt** (Product Purpose):
```markdown
## Product Purpose

Enable developers to create high-quality specifications 10x faster through
knowledge-driven templates powered by epistemological research methodologies
and GraphRAG semantic search. DAATH-ZEN solves the "spec creation bottleneck"
where teams spend 40-60% of project time on documentation instead of implementation.
```

**Excerpt** (Target Users):
```markdown
## Target Users

### Primary Users
1. **Software Architects** (Senior/Lead level)
   - Need: Document architectural decisions with full traceability to literature
   - Pain: Manual research synthesis takes 8+ hours per ADR

2. **Product Managers** (Technical PMs)
   - Need: Create product.md with clear vision, metrics, success criteria
   - Pain: Vision statements are vague, lack connection to user research

3. **Research Engineers** (ML/AI teams)
   - Need: Convert academic papers into actionable implementation specs
   - Pain: Papers use IMRAD format (experimental), specs need domain discovery format
```

**Excerpt** (Success Metrics):
```markdown
## Success Metrics

- **Spec Creation Time**: < 1 hour per spec (baseline: 8 hours, target: 90% reduction)
- **Citation Coverage**: 100% of claims traceable to 1-literature/ sources (0 invented content)
- **Validator Pass Rate**: ≥ 95% of specs pass automated validation on first compilation
- **GraphRAG Query Latency**: < 500ms for semantic concept search across 1000+ nodes
- **User Adoption**: 3+ teams using DAATH-ZEN templates by Q1 2026
- **NPS Score**: ≥ 70 from pilot users (n ≥ 10 respondents)
```

### 6.2. Research Autopoietic Templates (Sibling Project)

**File**: `apps/research-autopoietic-template/.spec-workflow/steering/product.md`

**Excerpt** (Product Principles):
```markdown
## Product Principles

1. **Issue-Driven Everything**: Every atomic unit (REQ-XXX, CONCEPT-XXX, LIT-XXX)
   is an ISSUE.yaml with Gap/Goal/Outcomes. Enables fine-grained GitHub issue tracking.

2. **Scoping Review for Discovery**: Use Arksey & O'Malley (2005) framework for
   domain discovery, NOT IMRAD (which is for experiments). Explicit research question →
   literature selection → charting → synthesis → reporting.

3. **Atomic Reusability**: Each concept is a standalone JSON file reusable across
   specs. Avoids duplication, enables knowledge graphs (Neo4j).

4. **No Manual Copy-Paste**: All compilation is automated via Jinja2 templates
   reading from 3-atomics/. Human writes atomics, compiler writes artifacts.
```

---

## 7. Common Mistakes to Avoid

### 7.1. Vague Product Purpose

❌ **BAD**:
```markdown
## Product Purpose
Build an innovative platform that leverages cutting-edge AI to revolutionize
the way developers create specifications.
```

**Problems**:
- Buzzwords without substance ("innovative", "cutting-edge", "revolutionize")
- No clear problem stated
- No measurable outcome

✅ **GOOD**:
```markdown
## Product Purpose
Enable developers to create high-quality specifications 10x faster through
knowledge-driven templates powered by epistemological research methodologies
and GraphRAG semantic search. DAATH-ZEN solves the "spec creation bottleneck"
where teams spend 40-60% of project time on documentation instead of implementation.
```

**Why it's good**:
- Clear value proposition ("10x faster")
- Specific problem ("spec creation bottleneck", "40-60% time on docs")
- Concrete mechanism ("epistemological research", "GraphRAG")

### 7.2. Generic Target Users

❌ **BAD**:
```markdown
## Target Users
- Developers who want to write better code
- Product managers who need to plan features
- Teams that value quality
```

**Problems**:
- Too generic (all devs want better code)
- No pain points mentioned
- No specific needs identified

✅ **GOOD**:
```markdown
## Target Users

### Primary: Software Architects (Senior/Lead)
- **Need**: Document architectural decisions with full traceability to literature
- **Pain**: Manual research synthesis takes 8+ hours per ADR, often with citation gaps
- **Gain**: Reduce ADR creation time to < 1 hour with automated literature synthesis

### Secondary: Product Managers (Technical PMs)
- **Need**: Create product.md with clear vision, metrics, and success criteria
- **Pain**: Vision statements are vague, lack connection to user research data
- **Gain**: Generate data-driven product.md from Scoping Review of user interviews
```

### 7.3. Feature Lists Instead of Principles

❌ **BAD**:
```markdown
## Product Principles

1. **Fast**: The system should be fast
2. **Reliable**: The system should not crash
3. **User-friendly**: The UI should be easy to use
```

**Problems**:
- Not actionable (how do you decide if something is "fast enough"?)
- Generic platitudes (every product wants to be fast/reliable/friendly)
- No trade-off guidance (what if speed conflicts with reliability?)

✅ **GOOD**:
```markdown
## Product Principles

1. **Latency Budget Over Feature Richness**: If a feature adds >500ms to GraphRAG
   query latency, defer it to Phase 2. User experience degrades exponentially
   beyond 500ms. Trade-off: fewer features, faster core functionality.

2. **Fail-Fast Validation**: Validate early (4-artefact/ contracts) before compilation
   (5-compiler/). If validation fails, stop immediately with clear error message.
   Trade-off: stricter workflow, fewer runtime surprises.

3. **Explicit Over Implicit**: Make epistemological transformations visible
   (1-literature/ → 2-analysis/ → 3-atomics/ → etc.). Transparency helps debugging.
   Trade-off: more files/folders, clearer knowledge flow.
```

**Why it's good**:
- Actionable thresholds ("500ms latency budget")
- Guides trade-offs ("fewer features, faster core")
- Explains WHY ("transparency helps debugging")

### 7.4. Unmeasurable Success Metrics

❌ **BAD**:
```markdown
## Success Metrics

- Increase user satisfaction
- Improve code quality
- Reduce technical debt
```

**Problems**:
- No baseline (improve from what?)
- No target (how much improvement?)
- Not measurable (how do you quantify "satisfaction"?)

✅ **GOOD**:
```markdown
## Success Metrics

- **User Satisfaction (NPS)**: ≥ 70 (baseline: N/A, target: Q1 2026, n ≥ 10 users)
- **Code Coverage**: ≥ 80% (baseline: 0%, target: Q1 2026, measured via pytest-cov)
- **Technical Debt Ratio**: < 10% (baseline: 35% from SonarQube, target: Q2 2026)
```

**Why it's good**:
- Measurable (NPS score, coverage %, debt ratio)
- Has target values (≥ 70, ≥ 80%, < 10%)
- Time-bound (Q1 2026, Q2 2026)
- Includes measurement method (pytest-cov, SonarQube)

---

## 8. Atomic Concepts Extracted

From this literature source, the following atomic concepts should be extracted to `3-atomics/`:

1. **concept-product-purpose.json**: Product purpose statement structure (problem + solution + value)
2. **concept-target-user-persona.json**: User persona structure (role + needs + pain points + gains)
3. **concept-business-objective.json**: Business objective structure (strategic goal + measurable outcome)
4. **concept-success-metric.json**: Success metric structure (name + target + baseline + measurement method + time-bound)
5. **concept-product-principle.json**: Product principle structure (name + explanation + trade-offs + examples)
6. **concept-key-feature.json**: Key feature structure (name + description + user value)
7. **concept-steering-document.json**: Steering document types (product/tech/structure) and approval workflow

---

## 9. Related Standards and Frameworks

### 9.1. Product Management Frameworks

This spec-workflow-mcp product.md format is **compatible** with these frameworks:

1. **Product Vision Board** (Roman Pichler, 2016)
   - Vision → Target/Needs/Product → Business Goals
   - Maps to: Product Purpose → Target Users → Key Features → Business Objectives

2. **Lean Canvas** (Ash Maurya, 2012)
   - Problem → Solution → UVP → Metrics
   - Maps to: Target Users (pain points) → Key Features → Product Purpose → Success Metrics

3. **SVPG Product Strategy** (Marty Cagan, 2017)
   - Product vision + product principles + product priorities
   - Maps to: Product Purpose → Product Principles → Business Objectives

### 9.2. Differences from Traditional PRD (Product Requirements Document)

| Aspect | Traditional PRD | spec-workflow-mcp product.md |
|--------|----------------|------------------------------|
| **Scope** | Per-feature, detailed | Per-project, strategic |
| **Audience** | Engineering team | Entire organization + LLMs |
| **Length** | 10-50 pages | 2-5 pages |
| **Update Frequency** | Per release | Per quarter (or when vision changes) |
| **Requirements Detail** | High (user stories, acceptance criteria) | Low (high-level features only) |
| **Approval Process** | PM → Eng → Design → Stakeholders | MCP dashboard (async) |
| **Machine-Readable** | No (PDF/Word) | Yes (Markdown + MCP tools) |

**Key Insight**: product.md is a **steering document**, not a requirements document. Detailed requirements go in `.spec-workflow/specs/{spec-name}/requirements.md` (per-spec, not per-project).

---

## 10. References

### 10.1. Primary Sources

1. **spec-workflow-mcp Official Repository**
   - URL: https://github.com/pimzino/spec-workflow-mcp
   - Version: v1.1.2+
   - File: `product-template.md`
   - Accessed: 2026-01-11

2. **spec-workflow-mcp Steering Guide**
   - Tool: `mcp_spec-workflow2_steering-guide()`
   - Loads: Complete workflow for creating product.md, tech.md, structure.md
   - Approval process documented

### 10.2. Related Documentation

3. **DAATH-ZEN Product Steering Document**
   - File: `.spec-workflow/steering/product.md`
   - Example of real-world implementation
   - Shows DAATH-ZEN-specific adaptations

4. **Research Autopoietic Templates Product Steering**
   - File: `apps/research-autopoietic-template/.spec-workflow/steering/product.md`
   - Example of Issue-Driven approach
   - Shows atomic concept integration

5. **Best Practices Guide**
   - File: `.spec-workflow/_meta/best-practices.md`
   - Task format integration with spec-workflow-mcp
   - Rostro + MCP conventions

### 10.3. Product Management Frameworks

6. **Strategize: Product Strategy and Product Roadmap Practices for the Digital Age**
   - Author: Roman Pichler
   - Year: 2016
   - ISBN: 978-0993499203
   - Relevant: Product Vision Board framework

7. **Running Lean: Iterate from Plan A to a Plan That Works**
   - Author: Ash Maurya
   - Year: 2012
   - ISBN: 978-1449305178
   - Relevant: Lean Canvas problem/solution/UVP structure

8. **Inspired: How to Create Tech Products Customers Love**
   - Author: Marty Cagan
   - Year: 2017
   - ISBN: 978-1119387503
   - Relevant: Product vision and product principles concepts

---

## 11. Validation Checklist

Before finalizing product.md, verify:

### 11.1. Structure Compliance
- [ ] File is named exactly `product.md` (lowercase)
- [ ] File is in `.spec-workflow/steering/product.md`
- [ ] All 6 mandatory sections present (Purpose, Users, Features, Objectives, Metrics, Principles)
- [ ] Uses `##` for sections, `###` for subsections
- [ ] Uses `-` for bullet lists (not `*`)

### 11.2. Content Quality
- [ ] Product Purpose: 1-3 paragraphs, clear problem statement
- [ ] Target Users: 3-5 user types with needs/pains/gains
- [ ] Key Features: 3-7 features with user-facing value descriptions
- [ ] Business Objectives: 3-5 strategic goals
- [ ] Success Metrics: 4-8 metrics with targets + baselines + measurement methods
- [ ] Product Principles: 3-5 principles with trade-offs and examples
- [ ] No vague buzzwords without concrete examples
- [ ] Active voice used throughout

### 11.3. Workflow Compliance
- [ ] Approval requested via `mcp_spec-workflow2_approvals(action: request)`
- [ ] Status polled until `approved` status received
- [ ] Approval cleaned up via `mcp_spec-workflow2_approvals(action: delete)`
- [ ] Document committed to Git after approval

### 11.4. Integration with Workbook
- [ ] Literature documented in `1-literature/framework/spec-workflow-mcp-product-format.md` (this file)
- [ ] Analysis synthesized in `2-analysis/analysis-002-product-md-structure.md`
- [ ] Atomic concepts extracted to `3-atomics/concept-*.json` (7 concepts identified)
- [ ] Validation contract created in `4-artefact/contract-product-md-schema.json`
- [ ] Compiler template created in `5-compiler/templates/product.md.j2`
- [ ] Neo4j ingestion script in `6-outputs/cypher/ingest-product-md-schema.cypher`

---

## 12. Conclusion

**spec-workflow-mcp product.md** is a **strategic steering document** that provides project-level context for LLMs and teams. It follows a **7-section structure** (6 mandatory + 1-2 optional) and requires **approval via MCP dashboard** before use.

**Key Differentiators**:
1. **Project-level scope** (not per-spec, not per-feature)
2. **Strategic focus** (vision/users/goals, not detailed requirements)
3. **Machine-readable** (Markdown + MCP tools, not PDF/Word)
4. **Approval workflow** (async dashboard, not email threads)
5. **LLM-optimized** (clear structure, concise content, no jargon)

**Next Steps**:
1. Complete analysis in `2-analysis/analysis-002-product-md-structure.md` synthesizing this literature with Product Vision Board (Pichler), Lean Canvas (Maurya), and SVPG frameworks (Cagan)
2. Extract 7 atomic concepts to `3-atomics/` (product-purpose, target-user, business-objective, success-metric, product-principle, key-feature, steering-document)
3. Create JSON Schema validation contract in `4-artefact/contract-product-md-schema.json`
4. Implement Jinja2 template in `5-compiler/templates/product.md.j2`
5. Generate Neo4j ingestion script in `6-outputs/cypher/ingest-product-md-schema.cypher`

---

**End of Literature Documentation**

**Workbook Status**:
- ✅ 1-literature/: spec-workflow-mcp format documented (this file)
- ⏳ 2-analysis/: Synthesis pending
- ⏳ 3-atomics/: 7 concepts to extract
- ⏳ 4-artefact/: Schema validation pending
- ⏳ 5-compiler/: Template compilation pending
- ⏳ 6-outputs/: Neo4j ingestion pending
