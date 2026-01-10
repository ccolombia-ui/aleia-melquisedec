# Quality Tools

CI/CD quality validation tools for the ALEIA-MELQUISEDEC monorepo.

## Overview

This directory contains pre-commit hooks and CI validation scripts to ensure:
1. **Canonical document uniqueness**: No duplicate `canonical_for` values
2. **Document coherence**: Minimum 0.2 coherence score for new/modified documents
3. **Manifesto coverage**: All major headings covered by canonical docs or tracked in TODO

## Tools

### 1. check_canonical_uniqueness.py

Validates that `canonical_for` frontmatter values are unique across all documents.

**Usage:**
```bash
python tools/quality/check_canonical_uniqueness.py
```

**Checks:**
- Each `canonical_for` value appears only once
- Referenced canonical documents exist in `canonical/` directory
- No circular references

**Exit codes:**
- `0`: All checks passed
- `1`: Validation errors found

### 2. check_coherence.py

Validates document coherence for staged/modified markdown files.

**Usage:**
```bash
python tools/quality/check_coherence.py
```

**Checks:**
- Coherence score ≥ 0.2 for all new/modified documents
- Documents have focused, related content
- Paragraphs flow logically

**What is coherence?**
Coherence measures semantic consistency by comparing adjacent paragraphs using cosine similarity. Higher scores (0.2-1.0) indicate focused, well-structured documents. Lower scores (<0.2) suggest disjointed content that should be split or restructured.

**Exit codes:**
- `0`: All documents meet threshold
- `1`: One or more documents below threshold

### 3. check_manifesto_coverage.py

Validates that all manifesto headings are either:
- Covered by a canonical document, OR
- Explicitly tracked in `canonical/TODO.md`

**Usage:**
```bash
python tools/quality/check_manifesto_coverage.py
```

**Checks:**
- All H1-H3 manifesto headings have canonical docs or TODO entries
- No sections are silently ignored
- Coverage rate statistics

**Output:**
- JSON report: `manifesto-coverage-{total}-{covered}.json`
- Coverage statistics printed to console

**Exit codes:**
- `0`: 100% coverage (docs + TODOs)
- `1`: Gaps found (no doc, no TODO)

## Integration

### Pre-commit Hooks

All tools are integrated as pre-commit hooks in [.pre-commit-config.yaml](../../.pre-commit-config.yaml):

```yaml
- repo: local
  hooks:
    - id: check-canonical-uniqueness
      name: Validate canonical_for uniqueness
      entry: python tools/quality/check_canonical_uniqueness.py
      language: python
      pass_filenames: false
      stages: [pre-commit]
      files: \.md$

    - id: check-coherence
      name: Validate document coherence
      entry: python tools/quality/check_coherence.py
      language: python
      pass_filenames: false
      stages: [pre-commit]
      files: \.md$
```

**Install:**
```bash
pip install pre-commit
pre-commit install
```

**Run manually:**
```bash
pre-commit run --all-files
```

### GitHub Actions

CI workflow defined in [.github/workflows/quality-gates.yml](../../.github/workflows/quality-gates.yml).

**Triggers:**
- Pull requests to `main` or `develop` (when `.md` or `.py` files change)
- Pushes to `main` (when `.md` or `.py` files change)

**Jobs:**
1. **canonical-uniqueness**: Validate canonical_for uniqueness
2. **coherence-check**: Validate document coherence
3. **manifesto-coverage**: Validate manifesto coverage (warning-only)
4. **quality-summary**: Aggregate results and fail if critical checks fail

**Artifacts:**
- Canonical uniqueness logs (30 days)
- Manifesto coverage JSON reports (30 days)

## Fixing Validation Errors

### Canonical Uniqueness Failures

**Error:**
```
❌ Duplicate canonical_for='feature-x' found in:
  - docs/guide-a.md
  - docs/guide-b.md
```

**Fix:**
1. Choose which document should reference `canonical/feature-x.md`
2. Update the other document to reference a different canonical or remove `canonical_for`
3. Commit and push

### Coherence Failures

**Error:**
```
❌ docs/my-doc.md: Coherence too low (0.15 < 0.2)
   This document may lack focus or contain disjointed sections.
```

**Fix options:**
1. **Split**: Break into multiple focused documents
2. **Restructure**: Add transitions between sections
3. **Remove**: Delete unrelated content
4. **Merge**: Consolidate related sections

### Manifesto Coverage Failures

**Error:**
```
❌ 5 manifesto heading(s) have no canonical doc or TODO entry:
   - Feature X (slug: feature-x)
   - Feature Y (slug: feature-y)
```

**Fix options:**

**Option A**: Create canonical documents
```bash
# Create canonical stubs
mkdir -p canonical
echo "---\ntitle: Feature X\ncanonical_for: feature-x\n---\n\nTODO: Document Feature X" > canonical/feature-x.md
```

**Option B**: Add to TODO list
```bash
# Create canonical/TODO.md if it doesn't exist
cat >> canonical/TODO.md <<EOF
## Pending Canonical Documents

- [ ] \`feature-x\` - Feature X documentation
- [ ] \`feature-y\` - Feature Y documentation
EOF
```

## Configuration

### Coherence Threshold

Adjust threshold in [check_coherence.py](./check_coherence.py):

```python
# Default: 0.2 (20% coherence minimum)
success, errors, checked_count = validate_coherence(
    changed_files,
    threshold=0.2  # Change this value
)
```

Lower values (0.1-0.15) are more permissive; higher values (0.3-0.5) are stricter.

### Excluded Patterns

Add patterns to skip certain directories:

```python
exclude_patterns = [
    'node_modules', '.venv', 'venv', '__pycache__',
    '.git', 'htmlcov', '_templates',
    'your-custom-pattern-here'
]
```

## Development

### Running Tests

```bash
# Test canonical uniqueness
python tools/quality/check_canonical_uniqueness.py

# Test coherence (requires staged/modified .md files)
git add docs/my-doc.md
python tools/quality/check_coherence.py

# Test manifesto coverage
python tools/quality/check_manifesto_coverage.py
```

### Adding New Checks

1. Create new script: `tools/quality/check_your_feature.py`
2. Add to `.pre-commit-config.yaml`:
   ```yaml
   - id: check-your-feature
     name: Validate your feature
     entry: python tools/quality/check_your_feature.py
     language: python
     pass_filenames: false
     stages: [pre-commit]
   ```
3. Add to GitHub Actions: `.github/workflows/quality-gates.yml`
4. Update this README

## References

- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [ALEIA-MELQUISEDEC Quality Standards](../../docs/guides/README.md)

## License

MIT License - See [LICENSE](../../LICENSE) for details.
