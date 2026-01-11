// ============================================================
// Neo4j Ingestion Script: Product Vision Concepts
// ============================================================
// Purpose: Ingest product-related concepts from workbook-product-md
//          into Neo4j for GraphRAG queries and semantic traversal
// Created: 2026-01-11
// Workbook: workbook-product-md
// ============================================================

// Clean up existing product concepts (optional, for re-ingestion)
// MATCH (c:Concept:Product) DETACH DELETE c;

// ============================================================
// 1. CREATE CONCEPT NODES
// ============================================================

// Create Product Vision concept
CREATE (pv:Concept:Product {
  id: 'concept-product-vision',
  name: 'Product Vision',
  category: 'product-management',
  subcategory: 'strategy',
  definition: 'A clear, inspiring, long-term goal that describes the future state the product aims to create, typically spanning 2-10 years',
  timeframe: '2-10 years',
  length: '1-2 sentences',
  tone: 'aspirational yet believable',
  created: datetime('2026-01-11T00:00:00Z'),
  workbook: 'workbook-product-md'
});

// Create Target Group concept
CREATE (tg:Concept:Product {
  id: 'concept-target-group',
  name: 'Target Group',
  category: 'product-management',
  subcategory: 'customer',
  definition: 'The primary users, customers, or market segments that the product serves',
  examples: ['developers', 'project managers', 'enterprise teams'],
  created: datetime('2026-01-11T00:00:00Z'),
  workbook: 'workbook-product-md'
});

// Create Customer Needs concept
CREATE (cn:Concept:Product {
  id: 'concept-customer-needs',
  name: 'Customer Needs',
  category: 'product-management',
  subcategory: 'problem',
  definition: 'The top 3 problems or jobs-to-be-done that customers are trying to solve',
  format: 'top 3 problems',
  pain_levels: ['must-have', 'nice-to-have'],
  created: datetime('2026-01-11T00:00:00Z'),
  workbook: 'workbook-product-md'
});

// Create Differentiation concept
CREATE (diff:Concept:Product {
  id: 'concept-differentiation',
  name: 'Differentiation',
  category: 'product-management',
  subcategory: 'strategy',
  definition: 'The unique value proposition and unfair advantage that sets the product apart from alternatives',
  components: ['UVP', 'unfair advantage', 'key attributes'],
  created: datetime('2026-01-11T00:00:00Z'),
  workbook: 'workbook-product-md'
});

// Create Success Criteria concept
CREATE (sc:Concept:Product {
  id: 'concept-success-criteria',
  name: 'Success Criteria',
  category: 'product-management',
  subcategory: 'metrics',
  definition: 'Business goals and key metrics that define product success',
  metric_types: ['revenue', 'market share', 'user growth', 'engagement'],
  frameworks: ['OKR', 'SMART', 'KPI'],
  created: datetime('2026-01-11T00:00:00Z'),
  workbook: 'workbook-product-md'
});

// Create Positioning Statement concept
CREATE (ps:Concept:Product {
  id: 'concept-positioning-statement',
  name: 'Positioning Statement',
  category: 'product-management',
  subcategory: 'positioning',
  definition: 'A structured statement defining target customer, need, product category, benefit, and differentiation',
  template: 'For [target] who [need], [product] is a [category] that [benefit]. Unlike [competitor], our product [differentiation].',
  author: 'Geoffrey Moore',
  source: 'Crossing the Chasm',
  created: datetime('2026-01-11T00:00:00Z'),
  workbook: 'workbook-product-md'
});

// ============================================================
// 2. CREATE SOURCE NODES
// ============================================================

// Create book source: Inspired (Cagan)
CREATE (inspired:Source:Book {
  id: 'inspired-book',
  title: 'Inspired: How to Create Tech Products Customers Love',
  author: 'Marty Cagan',
  publisher: 'Wiley',
  year: 2017,
  isbn: '978-1119387503',
  category: 'product-management',
  created: datetime('2026-01-11T00:00:00Z')
});

// Create book source: Strategize (Pichler)
CREATE (strategize:Source:Book {
  id: 'strategize-book',
  title: 'Strategize: Product Strategy and Product Roadmap Practices',
  author: 'Roman Pichler',
  publisher: 'Pichler Consulting',
  year: 2016,
  isbn: '978-0993499203',
  category: 'product-management',
  created: datetime('2026-01-11T00:00:00Z')
});

// Create book source: Running Lean (Maurya)
CREATE (lean:Source:Book {
  id: 'running-lean-book',
  title: 'Running Lean: Iterate from Plan A to a Plan That Works',
  author: 'Ash Maurya',
  publisher: "O'Reilly Media",
  year: 2012,
  isbn: '978-1449305178',
  category: 'lean-startup',
  created: datetime('2026-01-11T00:00:00Z')
});

// Create book source: Crossing the Chasm (Moore)
CREATE (chasm:Source:Book {
  id: 'crossing-chasm-book',
  title: 'Crossing the Chasm: Marketing and Selling Disruptive Products',
  author: 'Geoffrey A. Moore',
  publisher: 'HarperBusiness',
  year: 1991,
  isbn: '978-0062292988',
  category: 'marketing',
  created: datetime('2026-01-11T00:00:00Z')
});

// Create framework source: Product Vision Board
CREATE (pvb:Source:Framework {
  id: 'product-vision-board-framework',
  title: 'The Product Vision Board',
  author: 'Roman Pichler',
  organization: 'Roman Pichler Consulting',
  url: 'https://www.romanpichler.com/tools/product-vision-board/',
  year: 2016,
  category: 'product-management',
  created: datetime('2026-01-11T00:00:00Z')
});

// Create framework source: Lean Canvas
CREATE (lc:Source:Framework {
  id: 'lean-canvas-framework',
  title: 'Lean Canvas',
  author: 'Ash Maurya',
  organization: 'Leanstack',
  url: 'https://leanstack.com/lean-canvas',
  year: 2012,
  category: 'lean-startup',
  created: datetime('2026-01-11T00:00:00Z')
});

// ============================================================
// 3. CREATE RELATIONSHIPS: Concept → Source (CITED_IN)
// ============================================================

// Product Vision → Inspired book (pages 35-42)
MATCH (pv:Concept {id: 'concept-product-vision'}),
      (inspired:Source {id: 'inspired-book'})
CREATE (pv)-[:CITED_IN {
  pages: [35, 36, 37, 38, 39, 40, 41, 42],
  key_quote: 'The product vision describes the future we are trying to create, typically 2-10 years out',
  page_quote: 37
}]->(inspired);

// Product Vision → Product Vision Board framework
MATCH (pv:Concept {id: 'concept-product-vision'}),
      (pvb:Source {id: 'product-vision-board-framework'})
CREATE (pv)-[:CITED_IN {
  description: 'Visual framework for structuring product vision'
}]->(pvb);

// Target Group → Product Vision Board
MATCH (tg:Concept {id: 'concept-target-group'}),
      (pvb:Source {id: 'product-vision-board-framework'})
CREATE (tg)-[:CITED_IN]->(pvb);

// Customer Needs → Lean Canvas
MATCH (cn:Concept {id: 'concept-customer-needs'}),
      (lc:Source {id: 'lean-canvas-framework'})
CREATE (cn)-[:CITED_IN {
  description: 'Top 3 problems methodology from Lean Canvas'
}]->(lc);

// Differentiation → Lean Canvas (Unfair Advantage)
MATCH (diff:Concept {id: 'concept-differentiation'}),
      (lc:Source {id: 'lean-canvas-framework'})
CREATE (diff)-[:CITED_IN {
  description: 'Unfair Advantage component of Lean Canvas'
}]->(lc);

// Positioning Statement → Crossing the Chasm
MATCH (ps:Concept {id: 'concept-positioning-statement'}),
      (chasm:Source {id: 'crossing-chasm-book'})
CREATE (ps)-[:CITED_IN {
  pages: [154],
  description: 'Moore positioning statement template'
}]->(chasm);

// ============================================================
// 4. CREATE RELATIONSHIPS: Concept → Concept (RELATES_TO)
// ============================================================

// Product Vision relates to all other concepts
MATCH (pv:Concept {id: 'concept-product-vision'}),
      (tg:Concept {id: 'concept-target-group'})
CREATE (pv)-[:RELATES_TO {
  relationship: 'defines',
  description: 'Vision defines who the target group is'
}]->(tg);

MATCH (pv:Concept {id: 'concept-product-vision'}),
      (cn:Concept {id: 'concept-customer-needs'})
CREATE (pv)-[:RELATES_TO {
  relationship: 'addresses',
  description: 'Vision addresses customer needs'
}]->(cn);

MATCH (pv:Concept {id: 'concept-product-vision'}),
      (diff:Concept {id: 'concept-differentiation'})
CREATE (pv)-[:RELATES_TO {
  relationship: 'expresses',
  description: 'Vision expresses key differentiation'
}]->(diff);

MATCH (pv:Concept {id: 'concept-product-vision'}),
      (sc:Concept {id: 'concept-success-criteria'})
CREATE (pv)-[:RELATES_TO {
  relationship: 'measured_by',
  description: 'Vision success measured by criteria'
}]->(sc);

// Target Group relates to Customer Needs
MATCH (tg:Concept {id: 'concept-target-group'}),
      (cn:Concept {id: 'concept-customer-needs'})
CREATE (tg)-[:RELATES_TO {
  relationship: 'has',
  description: 'Target group has specific customer needs'
}]->(cn);

// Differentiation relates to Positioning Statement
MATCH (diff:Concept {id: 'concept-differentiation'}),
      (ps:Concept {id: 'concept-positioning-statement'})
CREATE (diff)-[:RELATES_TO {
  relationship: 'expressed_in',
  description: 'Differentiation expressed in positioning statement'
}]->(ps);

// ============================================================
// 5. CREATE ARTIFACT NODE (product.md)
// ============================================================

CREATE (product_md:Artifact {
  id: 'artifact-product-md',
  name: 'product.md',
  type: 'steering-document',
  category: 'spec-workflow-mcp',
  description: 'Product vision and strategy document',
  workbook: 'workbook-product-md',
  created: datetime('2026-01-11T00:00:00Z')
});

// Link concepts to artifact
MATCH (pv:Concept {id: 'concept-product-vision'}),
      (artifact:Artifact {id: 'artifact-product-md'})
CREATE (pv)-[:USED_IN {
  section: 'Vision Statement',
  required: true
}]->(artifact);

MATCH (tg:Concept {id: 'concept-target-group'}),
      (artifact:Artifact {id: 'artifact-product-md'})
CREATE (tg)-[:USED_IN {
  section: 'Target Group',
  required: true
}]->(artifact);

MATCH (cn:Concept {id: 'concept-customer-needs'}),
      (artifact:Artifact {id: 'artifact-product-md'})
CREATE (cn)-[:USED_IN {
  section: 'Customer Needs',
  required: true
}]->(artifact);

MATCH (diff:Concept {id: 'concept-differentiation'}),
      (artifact:Artifact {id: 'artifact-product-md'})
CREATE (diff)-[:USED_IN {
  section: 'Product Concept',
  required: true
}]->(artifact);

MATCH (sc:Concept {id: 'concept-success-criteria'}),
      (artifact:Artifact {id: 'artifact-product-md'})
CREATE (sc)-[:USED_IN {
  section: 'Business Goals',
  required: true
}]->(artifact);

MATCH (ps:Concept {id: 'concept-positioning-statement'}),
      (artifact:Artifact {id: 'artifact-product-md'})
CREATE (ps)-[:USED_IN {
  section: 'Positioning',
  required: false
}]->(artifact);

// ============================================================
// 6. VERIFICATION QUERIES
// ============================================================

// Count concepts created
// MATCH (c:Concept:Product) RETURN count(c) as product_concepts;
// Expected: 6 concepts

// Count sources created
// MATCH (s:Source) RETURN count(s) as sources;
// Expected: 6 sources (4 books + 2 frameworks)

// Find all concepts cited in Inspired book
// MATCH (c:Concept)-[r:CITED_IN]->(s:Source {id: 'inspired-book'})
// RETURN c.name as concept, r.pages as pages, r.key_quote as quote;

// Find all concepts used in product.md artifact
// MATCH (c:Concept)-[r:USED_IN]->(a:Artifact {id: 'artifact-product-md'})
// RETURN c.name as concept, r.section as section, r.required as required
// ORDER BY r.required DESC;

// Find relationships between Product Vision and other concepts
// MATCH (pv:Concept {id: 'concept-product-vision'})-[r:RELATES_TO]->(other:Concept)
// RETURN pv.name as from, r.relationship as relationship, other.name as to, r.description;

// ============================================================
// SUCCESS CONFIRMATION
// ============================================================

// Return summary of ingestion
MATCH (c:Concept:Product)
WITH count(c) as concept_count
MATCH (s:Source)
WITH concept_count, count(s) as source_count
MATCH (a:Artifact {id: 'artifact-product-md'})
WITH concept_count, source_count, count(a) as artifact_count
RETURN
  concept_count as `Concepts Created`,
  source_count as `Sources Created`,
  artifact_count as `Artifacts Created`,
  'Ingestion Complete ✅' as Status;

// ============================================================
// USAGE EXAMPLES
// ============================================================

// Example 1: Find all sources for Product Vision concept
// MATCH (c:Concept {id: 'concept-product-vision'})-[:CITED_IN]->(s:Source)
// RETURN s.title, s.author, s.year;

// Example 2: Find all concepts needed for product.md
// MATCH (c:Concept)-[:USED_IN]->(a:Artifact {id: 'artifact-product-md'})
// RETURN c.name, c.definition
// ORDER BY c.name;

// Example 3: Traverse from Vision to related concepts
// MATCH path = (pv:Concept {id: 'concept-product-vision'})-[:RELATES_TO*1..2]-(related)
// RETURN path;

// Example 4: Find which concepts from workbook-product-md
// MATCH (c:Concept {workbook: 'workbook-product-md'})
// RETURN c.name, c.category, c.definition;
