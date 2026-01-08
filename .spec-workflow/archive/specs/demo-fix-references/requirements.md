# Demo: Fix Nucleo-Investigacion References

## Overview
This specification covers cleaning up all remaining references to the deleted `nucleo-investigacion/` directory.

## User Stories

- **US-1**: Como desarrollador, quiero que no existan referencias rotas para que el código sea mantenible

## Functional Requirements

- **REQ-1**: All imports pointing to `nucleo-investigacion/` must be updated
- **REQ-2**: All markdown links to `nucleo-investigacion/` must be fixed or removed
- **REQ-3**: Configuration files referencing the old path must be updated

## Non-Functional Requirements

- **NFR-1**: Zero broken references after completion
- **NFR-2**: All tests must pass

## Acceptance Criteria

1. `grep -r "nucleo-investigacion" .` returns 0 results
2. All Python imports work correctly
3. All documentation links are valid
