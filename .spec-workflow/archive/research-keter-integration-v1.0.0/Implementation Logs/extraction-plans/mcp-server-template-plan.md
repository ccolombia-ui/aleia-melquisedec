# MCP Server Template Extraction Plan
**Parent**: research-keter-integration-v1.0.0
**Target**: `_templates/mcp-server-template/`
**Source**: [REPO:aleia-bereshit] `apps/keter/packages/keter/mcp/`
**Status**: Planning
**Priority**: P1

---

## 1. Executive Summary

Extraer el patrón de MCP Server de Keter como template reutilizable en MELQUISEDEC. El objetivo es crear un skeleton completo que permita crear nuevos MCP servers rápidamente, incluyendo tool registration, handlers, cache management y test patterns.

**Timeline**: 1-2 días (Sprint 3)
**Confidence**: 90%
**Risk Level**: Low (template extraction sin dependencies complejas)

---

## 2. Scope Definition

### 2.1 In Scope ✅

**Server Skeleton** (de `keter/mcp/server/`):
```typescript
// Template MCP server with:
- Server initialization
- Tool registration pattern
- Handler architecture
- Error handling
- Logging
```

**Tool Patterns** (de `keter/mcp/tools/`):
```typescript
// Generic tool patterns:
- CRUD operations (create, read, update, delete)
- List/query operations
- Validation operations
- Bulk operations
```

**Performance Patterns** (de `keter/mcp/performance/`):
```typescript
// Cache management:
- cache-manager.ts
- Invalidation strategies
- TTL configuration
```

**Test Patterns** (de `keter/tests/mcp/`):
```typescript
// Test structure:
- Tool testing patterns
- Mock server setup
- E2E workflow tests
```

**Documentation**:
- README with setup guide
- Tool customization guide
- Deployment guide
- Best practices

### 2.2 Out of Scope ❌

**Domain-Specific Logic**:
- ❌ decree-* tools (specific to keter domain)
- ❌ policy-* tools (will be in policy-engine package)
- ❌ Supabase integration details
- ❌ CMIS repository tools
- ❌ Validity handlers (specific to keter use case)

**Infrastructure**:
- ❌ Production deployment configs (user provides)
- ❌ Database schemas
- ❌ Authentication/authorization (template only)

---

## 3. Template Structure

### 3.1 Directory Layout

```
_templates/mcp-server-template/
├── README.md                     # Comprehensive setup guide
├── CUSTOMIZATION.md              # How to customize for your domain
├── package.json                  # With dependencies
├── tsconfig.json                 # TypeScript config
├── .gitignore                    # Standard Node.js gitignore
├── server/
│   ├── index.ts                  # Server entry point
│   ├── config.ts                 # Configuration management
│   ├── registry.ts               # Tool registration
│   └── types.ts                  # Shared types
├── tools/
│   ├── example-create.ts         # Example CREATE tool
│   ├── example-read.ts           # Example READ tool
│   ├── example-update.ts         # Example UPDATE tool
│   ├── example-delete.ts         # Example DELETE tool
│   ├── example-list.ts           # Example LIST tool
│   └── example-validate.ts       # Example VALIDATE tool
├── handlers/
│   ├── base-handler.ts           # Base handler class
│   ├── error-handler.ts          # Error handling utilities
│   └── response-builder.ts       # Response formatting
├── performance/
│   ├── cache-manager.ts          # Cache management
│   └── rate-limiter.ts           # Rate limiting (optional)
├── utils/
│   ├── logger.ts                 # Logging utilities
│   └── validators.ts             # Common validators
├── tests/
│   ├── setup.ts                  # Test setup
│   ├── mocks/
│   │   └── mock-storage.ts       # Mock storage for testing
│   ├── tools/
│   │   ├── example-create.test.ts
│   │   └── example-read.test.ts
│   └── integration/
│       └── e2e-workflow.test.ts
└── examples/
    ├── simple-server.ts          # Minimal example
    └── advanced-server.ts        # With cache + handlers
```

### 3.2 Placeholder System

**Naming Convention**:
```typescript
// Throughout template, use PLACEHOLDERS for customization:
{{PROJECT_NAME}}       // e.g., "my-research-mcp"
{{DOMAIN_ENTITY}}      // e.g., "Document", "Policy", "User"
{{STORAGE_BACKEND}}    // e.g., "Supabase", "MongoDB", "FileSystem"
{{PORT}}               // e.g., 3000, 3001

// Example in code:
export const config = {
  projectName: '{{PROJECT_NAME}}',
  port: parseInt(process.env.PORT || '{{PORT}}'),
};
```

**Setup Script** (bonus):
```bash
# scripts/setup.sh
#!/bin/bash
read -p "Project name: " PROJECT_NAME
read -p "Domain entity: " DOMAIN_ENTITY
# Replace placeholders in all files
find . -type f -exec sed -i "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" {} +
```

---

## 4. Core Components

### 4.1 Server Entry Point

```typescript
// server/index.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { toolRegistry } from './registry.js';
import { CacheManager } from '../performance/cache-manager.js';
import { logger } from '../utils/logger.js';

export class {{PROJECT_NAME}}Server {
  private server: Server;
  private cacheManager: CacheManager;

  constructor() {
    this.server = new Server(
      {
        name: '{{PROJECT_NAME}}-mcp-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.cacheManager = new CacheManager();
    this.setupHandlers();
  }

  private setupHandlers() {
    // Tool list handler
    this.server.setRequestHandler(
      ListToolsRequestSchema,
      async () => ({
        tools: toolRegistry.getAllTools(),
      })
    );

    // Tool call handler
    this.server.setRequestHandler(
      CallToolRequestSchema,
      async (request) => {
        const { name, arguments: args } = request.params;
        return await toolRegistry.executeTool(name, args);
      }
    );
  }

  async start() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    logger.info('{{PROJECT_NAME}} MCP Server started');
  }
}

// Start server if run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  new {{PROJECT_NAME}}Server().start().catch(logger.error);
}
```

### 4.2 Tool Registry Pattern

```typescript
// server/registry.ts
import { Tool } from '@modelcontextprotocol/sdk/types.js';

export class ToolRegistry {
  private tools: Map<string, Tool> = new Map();
  private handlers: Map<string, Function> = new Map();

  register(tool: Tool, handler: Function) {
    this.tools.set(tool.name, tool);
    this.handlers.set(tool.name, handler);
  }

  getAllTools(): Tool[] {
    return Array.from(this.tools.values());
  }

  async executeTool(name: string, args: any): Promise<any> {
    const handler = this.handlers.get(name);
    if (!handler) {
      throw new Error(`Tool not found: ${name}`);
    }
    return await handler(args);
  }
}

export const toolRegistry = new ToolRegistry();

// Auto-register tools
import { registerExampleTools } from '../tools/index.js';
registerExampleTools(toolRegistry);
```

### 4.3 Example Tool (CRUD Pattern)

```typescript
// tools/example-create.ts
import { z } from 'zod';
import { ToolRegistry } from '../server/registry.js';
import { BaseHandler } from '../handlers/base-handler.js';

const CreateSchema = z.object({
  name: z.string().min(1),
  description: z.string().optional(),
  metadata: z.record(z.unknown()).optional(),
});

export class CreateTool extends BaseHandler {
  async execute(args: z.infer<typeof CreateSchema>) {
    // PLACEHOLDER: Replace with your storage logic
    const {{DOMAIN_ENTITY_LOWER}} = {
      id: generateId(),
      ...args,
      createdAt: new Date().toISOString(),
    };

    // await storage.save({{DOMAIN_ENTITY_LOWER}});

    return this.success({
      {{DOMAIN_ENTITY_LOWER}},
      message: '{{DOMAIN_ENTITY}} created successfully',
    });
  }
}

export function registerCreateTool(registry: ToolRegistry) {
  registry.register(
    {
      name: '{{DOMAIN_ENTITY_LOWER}}-create',
      description: 'Create a new {{DOMAIN_ENTITY}}',
      inputSchema: {
        type: 'object',
        properties: {
          name: { type: 'string', description: 'Name of the {{DOMAIN_ENTITY}}' },
          description: { type: 'string' },
          metadata: { type: 'object' },
        },
        required: ['name'],
      },
    },
    async (args: unknown) => {
      const validated = CreateSchema.parse(args);
      return await new CreateTool().execute(validated);
    }
  );
}
```

### 4.4 Base Handler

```typescript
// handlers/base-handler.ts
export abstract class BaseHandler {
  protected success<T>(data: T) {
    return {
      content: [
        {
          type: 'text' as const,
          text: JSON.stringify({ success: true, data }, null, 2),
        },
      ],
    };
  }

  protected error(message: string, code?: string) {
    return {
      content: [
        {
          type: 'text' as const,
          text: JSON.stringify({
            success: false,
            error: { message, code },
          }, null, 2),
        },
      ],
      isError: true,
    };
  }

  protected validate<T>(schema: z.ZodSchema<T>, data: unknown): T {
    try {
      return schema.parse(data);
    } catch (error) {
      throw new Error(`Validation failed: ${error.message}`);
    }
  }
}
```

### 4.5 Cache Manager

```typescript
// performance/cache-manager.ts (from keter)
export interface CacheConfig {
  ttl: number;
  maxSize: number;
  strategy: 'LRU' | 'LFU';
}

export class CacheManager {
  private cache: Map<string, CacheEntry> = new Map();
  private config: CacheConfig;

  constructor(config: Partial<CacheConfig> = {}) {
    this.config = {
      ttl: config.ttl || 300_000,  // 5 minutes default
      maxSize: config.maxSize || 100,
      strategy: config.strategy || 'LRU',
    };
  }

  get<T>(key: string): T | null {
    const entry = this.cache.get(key);
    if (!entry) return null;

    if (Date.now() - entry.timestamp > this.config.ttl) {
      this.cache.delete(key);
      return null;
    }

    entry.lastAccessed = Date.now();
    return entry.value as T;
  }

  set<T>(key: string, value: T): void {
    if (this.cache.size >= this.config.maxSize) {
      this.evict();
    }

    this.cache.set(key, {
      value,
      timestamp: Date.now(),
      lastAccessed: Date.now(),
    });
  }

  invalidate(key: string): void {
    this.cache.delete(key);
  }

  clear(): void {
    this.cache.clear();
  }

  private evict(): void {
    // LRU eviction
    let oldest: string | null = null;
    let oldestTime = Date.now();

    for (const [key, entry] of this.cache.entries()) {
      if (entry.lastAccessed < oldestTime) {
        oldestTime = entry.lastAccessed;
        oldest = key;
      }
    }

    if (oldest) {
      this.cache.delete(oldest);
    }
  }
}

interface CacheEntry {
  value: unknown;
  timestamp: number;
  lastAccessed: number;
}
```

---

## 5. Migration Steps

### Phase 1: Setup (1 hour)
1. Create `_templates/mcp-server-template/` structure
2. Copy skeleton files from keter MCP
3. Replace domain-specific names with placeholders
4. Initialize package.json with dependencies

### Phase 2: Tool Extraction (2 hours)
1. Extract 6 example tools (create, read, update, delete, list, validate)
2. Remove keter-specific logic (decree, policy references)
3. Add clear PLACEHOLDER comments
4. Ensure each tool demonstrates a pattern

### Phase 3: Handler & Performance (2 hours)
1. Copy base-handler.ts
2. Copy cache-manager.ts
3. Add error-handler.ts utilities
4. Add logger.ts utilities

### Phase 4: Testing (2 hours)
1. Extract test patterns from keter
2. Create mock storage adapter
3. Write example tests for each tool
4. Create E2E workflow test

### Phase 5: Documentation (3 hours)
1. Write comprehensive README.md:
   - What is this template?
   - Quick start (5-minute setup)
   - Customization guide
   - Tool creation guide
   - Deployment guide
2. Write CUSTOMIZATION.md with step-by-step
3. Add inline comments throughout code
4. Create example usage files

---

## 6. Dependencies

### 6.1 Runtime Dependencies
```json
{
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "vitest": "^1.0.0",
    "@types/node": "^20.0.0",
    "tsx": "^4.0.0"
  }
}
```

### 6.2 Optional Dependencies
```json
{
  "optionalDependencies": {
    "winston": "^3.0.0"  // For advanced logging
  }
}
```

---

## 7. Documentation Structure

### 7.1 README.md Outline

```markdown
# MCP Server Template

🚀 Quick-start template for creating MCP (Model Context Protocol) servers.

## What's Included

- ✅ Server skeleton with tool registration
- ✅ 6 example tools (CRUD + list + validate)
- ✅ Base handler with error handling
- ✅ Cache manager for performance
- ✅ Test patterns and mocks
- ✅ TypeScript configuration
- ✅ Logger utilities

## Quick Start (5 minutes)

1. Copy template:
\`\`\`bash
cp -r _templates/mcp-server-template my-mcp-server
cd my-mcp-server
\`\`\`

2. Customize:
\`\`\`bash
# Replace placeholders
sed -i 's/{{PROJECT_NAME}}/my-project/g' **/*.ts
sed -i 's/{{DOMAIN_ENTITY}}/Document/g' **/*.ts
\`\`\`

3. Install & Run:
\`\`\`bash
npm install
npm run dev
\`\`\`

## Customization Guide

See [CUSTOMIZATION.md](CUSTOMIZATION.md) for detailed guide.

## Project Structure

[Tree diagram]

## Creating Your First Tool

[Step-by-step guide]

## Testing

\`\`\`bash
npm test
\`\`\`

## Deployment

[Deployment options]

## Reference Implementation

This template is extracted from @aleia/keter MCP server.
See: [REPO:aleia-bereshit] apps/keter/packages/keter/mcp/

## License

MIT
```

### 7.2 CUSTOMIZATION.md Outline

```markdown
# Customization Guide

## Step 1: Replace Placeholders

Replace these placeholders throughout the codebase:

| Placeholder | Example | Description |
|-------------|---------|-------------|
| {{PROJECT_NAME}} | my-research-mcp | Your MCP server name |
| {{DOMAIN_ENTITY}} | Document | Your domain entity (singular) |
| {{DOMAIN_ENTITY_LOWER}} | document | Lowercase version |
| {{PORT}} | 3000 | Server port |

## Step 2: Implement Storage

Choose your storage backend and implement:

\`\`\`typescript
// storage/index.ts
export interface IStorage {
  save(entity: any): Promise<void>;
  load(id: string): Promise<any>;
  delete(id: string): Promise<void>;
  query(criteria: any): Promise<any[]>;
}

// Example implementations:
// - SupabaseStorage (see examples/)
// - FileSystemStorage (see examples/)
// - InMemoryStorage (included for testing)
\`\`\`

## Step 3: Customize Tools

[Guide on adding/modifying tools]

## Step 4: Configure Cache

[Cache configuration options]

## Step 5: Add Authentication (Optional)

[Auth patterns]

## Step 6: Deploy

[Deployment guide]
```

---

## 8. Testing Strategy

### 8.1 Test Structure
```typescript
// tests/tools/example-create.test.ts
import { describe, it, expect, beforeEach } from 'vitest';
import { CreateTool } from '../../tools/example-create.js';
import { MockStorage } from '../mocks/mock-storage.js';

describe('CreateTool', () => {
  let tool: CreateTool;
  let storage: MockStorage;

  beforeEach(() => {
    storage = new MockStorage();
    tool = new CreateTool(storage);
  });

  it('should create entity successfully', async () => {
    const result = await tool.execute({
      name: 'Test Entity',
      description: 'Test description',
    });

    expect(result.content[0].text).toContain('created successfully');
  });

  it('should validate required fields', async () => {
    await expect(tool.execute({ name: '' })).rejects.toThrow('Validation');
  });
});
```

### 8.2 E2E Test
```typescript
// tests/integration/e2e-workflow.test.ts
describe('MCP Server E2E', () => {
  it('should handle complete CRUD workflow', async () => {
    const server = new {{PROJECT_NAME}}Server();

    // 1. Create
    const created = await server.executeTool('{{DOMAIN_ENTITY_LOWER}}-create', {
      name: 'Test',
    });
    expect(created.success).toBe(true);

    // 2. Read
    const read = await server.executeTool('{{DOMAIN_ENTITY_LOWER}}-read', {
      id: created.data.id,
    });
    expect(read.data.name).toBe('Test');

    // 3. Update
    await server.executeTool('{{DOMAIN_ENTITY_LOWER}}-update', {
      id: created.data.id,
      name: 'Updated',
    });

    // 4. Delete
    await server.executeTool('{{DOMAIN_ENTITY_LOWER}}-delete', {
      id: created.data.id,
    });
  });
});
```

---

## 9. Success Criteria

### 9.1 Functional
- [ ] Server starts without errors
- [ ] All 6 example tools work
- [ ] Cache manager functions correctly
- [ ] Test suite passes (>80% coverage)
- [ ] README examples are executable

### 9.2 Quality
- [ ] Zero hard-coded keter references
- [ ] All placeholders clearly marked
- [ ] Comprehensive inline comments
- [ ] TypeScript strict mode enabled
- [ ] Lint and format pass

### 9.3 Usability
- [ ] Can be customized in <30 minutes
- [ ] README quick start works
- [ ] CUSTOMIZATION.md is step-by-step clear
- [ ] Example projects run without modification

---

## 10. Rollback Plan

If extraction proves too complex:

**Plan B**: Minimal template
- Provide server skeleton only
- Document tool patterns in markdown
- Reference keter for examples

**Trigger**: If >2 days effort or testing fails

---

## 11. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Placeholders missed | 20% | Low | Grep for "keter", "decree", "policy" |
| Examples too complex | 30% | Medium | Keep simple, add "advanced" separate |
| MCP SDK breaking changes | 10% | High | Pin SDK version in package.json |

---

## 12. Post-Extraction

### 12.1 Maintenance
- **Owner**: Framework team
- **Updates**: When MCP SDK has breaking changes
- **Versioning**: Template version in README

### 12.2 Example Projects
Create example implementations:
- [ ] File-based MCP server
- [ ] Supabase-backed MCP server
- [ ] Neo4j-backed MCP server

---

## 13. References

- **Source Code**: [REPO:aleia-bereshit] `apps/keter/packages/keter/mcp/`
- **MCP SDK**: https://github.com/modelcontextprotocol/sdk
- **ADR-002**: [ADR-002-keter-integration-decision.md](../../docs/architecture/ADR-002-keter-integration-decision.md)
- **Keter Tests**: [REPO:aleia-bereshit] `apps/keter/tests/mcp/`

---

**End of Extraction Plan**
**Status**: ✅ Ready for Sprint 3 execution
**Estimated Duration**: 1-2 días
**Next**: Case study documentation
