# Policy Engine

> **REF**: Patterns extracted from [Keter](https://github.com/ccolombia-ui/aleia-bereshit/tree/main/apps/keter) implementation

Generic Policy Engine for declarative rule evaluation with conflict detection and lifecycle management.

## Features

- **Declarative Policies**: Define rules as data, not code
- **Conflict Detection**: Automatic detection of overlapping or contradictory policies
- **Lifecycle Management**: Version control and deprecation handling for policies
- **Storage Agnostic**: Abstract backend - works with any persistence layer
- **Type Safe**: Full typing support with Pydantic models

## Installation

```bash
# From monorepo root
pip install -e packages/policy-engine

# Or with dev dependencies
pip install -e "packages/policy-engine[dev]"
```

## Quick Start

```python
from policy_engine import PolicyEngine, Policy, PolicyContext
from policy_engine.validators import DefaultValidator

# Create engine with default validator
engine = PolicyEngine(validator=DefaultValidator())

# Define a policy
policy = Policy(
    id="POL-001",
    name="max-file-size",
    rules=[
        {"condition": "file.size > 10MB", "action": "reject"},
        {"condition": "file.size > 5MB", "action": "warn"},
    ],
    priority=100,
)

# Register policy
engine.register(policy)

# Evaluate context
context = PolicyContext(file={"size": "8MB", "type": "pdf"})
decision = engine.evaluate(context)

print(decision)
# Decision(action='warn', policy_id='POL-001', reason='file.size > 5MB')
```

## Architecture

```
packages/policy-engine/
├── src/policy_engine/
│   ├── __init__.py          # Public API exports
│   ├── interfaces.py        # Core interfaces (IPolicyEngine, IValidator, etc.)
│   ├── models.py            # Pydantic models (Policy, Decision, Conflict, etc.)
│   ├── engine.py            # PolicyEngine implementation
│   ├── validators/          # Built-in validators
│   │   ├── __init__.py
│   │   └── default.py
│   ├── detectors/           # Conflict detectors
│   │   ├── __init__.py
│   │   └── overlap.py
│   └── storage/             # Storage backends (abstract)
│       ├── __init__.py
│       ├── base.py
│       └── memory.py
├── tests/
│   ├── conftest.py
│   ├── test_engine.py
│   ├── test_validators.py
│   └── test_detectors.py
├── pyproject.toml
└── README.md
```

## Core Interfaces

### IPolicyEngine

```python
class IPolicyEngine(Protocol):
    def register(self, policy: Policy) -> None: ...
    def unregister(self, policy_id: str) -> None: ...
    def evaluate(self, context: PolicyContext) -> Decision: ...
    def get_applicable_policies(self, context: PolicyContext) -> list[Policy]: ...
```

### IValidator

```python
class IValidator(Protocol):
    def validate(self, policy: Policy) -> ValidationResult: ...
```

### IConflictDetector

```python
class IConflictDetector(Protocol):
    def detect(self, policies: list[Policy]) -> list[Conflict]: ...
```

## Design Decisions

1. **Storage Agnostic**: No assumptions about persistence layer (not tied to Supabase, Neo4j, etc.)
2. **Async-First**: Core operations support both sync and async patterns
3. **Extensible**: Easy to add custom validators, detectors, and storage backends
4. **Test-Driven**: >90% coverage target, patterns validated in Keter production

## Origin

This package extracts generic policy patterns from the Keter project:

- **Source**: `aleia-bereshit/apps/keter/core/`
- **Coverage**: 92.94% (original implementation)
- **Validation**: Production-tested with multi-tenant policies

See [ADR-002](../../docs/architecture/ADR-002-keter-integration-decision.md) for the full decision record.

## License

MIT - See [LICENSE](../../LICENSE) for details.
