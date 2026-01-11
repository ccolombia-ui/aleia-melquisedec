# Test: Product Vision Completeness

**Test ID**: TEST-PRODUCT-001
**Type**: Completeness Check
**Artifact**: product.md
**Component**: Vision Statement section

---

## Test Objective

Verify that the product vision statement in `product.md` meets the criteria defined in literature (Cagan, Pichler, Maurya) and contains all essential components for an effective vision.

---

## Test Criteria

### ✅ Pass Conditions

All of the following MUST be true:

#### 1. **Presence Check**
- [ ] Vision statement exists in product.md
- [ ] Vision statement is not empty or placeholder text

#### 2. **Length Check** (Cagan: "simple enough to remember")
- [ ] Vision is 1-2 sentences
- [ ] Vision is ≤ 200 words
- [ ] Vision is ≥ 10 words (not too short to be meaningful)

#### 3. **Component Check** (WHO, WHAT, HOW)
- [ ] **WHO**: Target customer/user is mentioned or clearly implied
  - Examples: "developers", "project managers", "students"
- [ ] **WHAT**: Transformation/change to be created is stated
  - Examples: "10x faster", "eliminate manual work", "enable remote collaboration"
- [ ] **HOW**: Key approach or differentiation is indicated
  - Examples: "knowledge-driven templates", "AI-powered", "blockchain-based"

#### 4. **Timeframe Check** (Cagan: "2-10 years out")
- [ ] Vision implies long-term scope (not quarterly/annual goal)
- [ ] NO mentions of short-term timeframes:
  - ❌ "Q1", "Q2", "next quarter"
  - ❌ "this year", "2026"
  - ❌ "in 6 months"

#### 5. **Clarity Check** (Cagan: "context for daily work")
- [ ] Vision is understandable without domain expertise
- [ ] Vision uses concrete language (not vague buzzwords)
- [ ] Flesch-Kincaid readability score ≥ 60 (8th-9th grade level)

#### 6. **Inspiration Check** (Cagan: "inspire the team")
- [ ] Vision uses aspirational language:
  - ✅ "empower", "enable", "transform", "revolutionize"
  - ✅ "unlock", "democratize", "simplify", "accelerate"
- [ ] Vision focuses on customer benefit (not company profit)
- [ ] Vision is believable (not science fiction)

---

## Test Execution

### Manual Checklist

```markdown
## Vision Statement: {{project_name}}

**Vision**: [PASTE VISION HERE]

### Checklist
- [ ] 1. Presence: Vision exists and is not empty
- [ ] 2. Length: 1-2 sentences, 10-200 words (current: ___ words)
- [ ] 3a. WHO: Target customer mentioned
- [ ] 3b. WHAT: Transformation stated
- [ ] 3c. HOW: Key approach indicated
- [ ] 4. Timeframe: Long-term (no Q1/Q2/this year)
- [ ] 5. Clarity: Readability score ≥ 60 (current: ___)
- [ ] 6. Inspiration: Aspirational language present

**RESULT**: [ ] PASS / [ ] FAIL
```

### Automated Validation (Python)

```python
# File: 4-artefact/validate_vision.py

import re
from textstat import flesch_kincaid_grade

def validate_vision(vision_text: str) -> dict:
    """
    Validate vision statement against criteria.

    Returns:
        dict with keys: pass (bool), errors (list), warnings (list)
    """
    errors = []
    warnings = []

    # 1. Presence check
    if not vision_text or vision_text.strip() == "":
        errors.append("Vision statement is empty")
        return {"pass": False, "errors": errors, "warnings": warnings}

    # 2. Length check
    word_count = len(vision_text.split())
    sentence_count = vision_text.count('.') + vision_text.count('!') + vision_text.count('?')

    if word_count < 10:
        errors.append(f"Vision too short ({word_count} words, minimum 10)")
    if word_count > 200:
        errors.append(f"Vision too long ({word_count} words, maximum 200)")
    if sentence_count > 2:
        warnings.append(f"Vision has {sentence_count} sentences, recommend 1-2")

    # 3. Component check (heuristic)
    aspirational_words = ['empower', 'enable', 'transform', 'revolutionize',
                          'unlock', 'democratize', 'simplify', 'accelerate']
    has_aspirational = any(word in vision_text.lower() for word in aspirational_words)
    if not has_aspirational:
        warnings.append("Vision lacks aspirational language (empower, enable, etc.)")

    # 4. Timeframe check
    short_term_patterns = [
        r'\bQ[1-4]\b', r'\bquarter\b', r'\bthis year\b', r'\b202[0-9]\b',
        r'\b[0-9]+ months?\b', r'\bnext year\b'
    ]
    for pattern in short_term_patterns:
        if re.search(pattern, vision_text, re.IGNORECASE):
            errors.append(f"Vision mentions short-term timeframe (found: {pattern})")

    # 5. Clarity check
    try:
        readability = flesch_kincaid_grade(vision_text)
        if readability > 12:  # College level
            warnings.append(f"Vision may be too complex (grade level: {readability}, target: 8-9)")
    except:
        warnings.append("Could not calculate readability score")

    # 6. Vague buzzwords check
    vague_buzzwords = ['best', 'innovative', 'cutting-edge', 'world-class',
                       'synergy', 'leverage', 'optimize']
    found_buzzwords = [word for word in vague_buzzwords if word in vision_text.lower()]
    if found_buzzwords:
        warnings.append(f"Vision contains vague buzzwords: {', '.join(found_buzzwords)}")

    # Determine pass/fail
    passed = len(errors) == 0

    return {
        "pass": passed,
        "errors": errors,
        "warnings": warnings,
        "word_count": word_count,
        "sentence_count": sentence_count
    }

# Example usage
if __name__ == "__main__":
    test_vision = "Empower developers to create specs 10x faster with knowledge-driven templates"
    result = validate_vision(test_vision)

    print(f"PASS: {result['pass']}")
    print(f"Word Count: {result['word_count']}")
    print(f"Errors: {result['errors']}")
    print(f"Warnings: {result['warnings']}")
```

---

## Example Test Cases

### ✅ PASS: Good Vision

```
Vision: "Empower developers to create specs 10x faster with knowledge-driven
templates, eliminating manual duplication and enabling focus on problem-solving."

Checklist:
✅ 1. Presence: Yes
✅ 2. Length: 1 sentence, 20 words
✅ 3a. WHO: "developers"
✅ 3b. WHAT: "10x faster", "eliminating manual duplication"
✅ 3c. HOW: "knowledge-driven templates"
✅ 4. Timeframe: Long-term implied (no short-term mentions)
✅ 5. Clarity: Readability ~9th grade
✅ 6. Inspiration: "Empower", "enabling"

RESULT: PASS
```

---

### ❌ FAIL: Business Metric Vision

```
Vision: "Increase company revenue by 25% in Q1 2026 through improved product offerings."

Checklist:
✅ 1. Presence: Yes
✅ 2. Length: 1 sentence, 13 words
❌ 3a. WHO: Not mentioned (focus on company, not customer)
❌ 3b. WHAT: Revenue increase (not customer transformation)
❌ 3c. HOW: "improved offerings" (vague)
❌ 4. Timeframe: Short-term ("Q1 2026")
✅ 5. Clarity: Readable
❌ 6. Inspiration: Not aspirational (business metric)

RESULT: FAIL (4 criteria failed)
Errors:
- Vision mentions short-term timeframe (Q1 2026)
- Vision focuses on company benefit, not customer transformation
- Vision lacks aspirational language
- Key approach is vague ("improved offerings")
```

---

### ⚠️ PASS WITH WARNINGS: Vague Buzzwords

```
Vision: "Build the most innovative and cutting-edge platform to leverage synergies
in the market."

Checklist:
✅ 1. Presence: Yes
✅ 2. Length: 1 sentence, 15 words
⚠️ 3a. WHO: Not clearly stated
⚠️ 3b. WHAT: Vague ("leverage synergies")
⚠️ 3c. HOW: Buzzwords ("innovative", "cutting-edge")
✅ 4. Timeframe: Long-term implied
⚠️ 5. Clarity: Jargon-heavy
⚠️ 6. Inspiration: Vague buzzwords

RESULT: PASS (no hard errors, but 5 warnings)
Warnings:
- Vision contains vague buzzwords: innovative, cutting-edge, leverage, synergies
- Target customer not clearly stated
- Transformation is unclear
- Consider rewriting with concrete language
```

---

## Test Reporting

### Test Report Template

```markdown
# Product Vision Test Report

**Date**: {{test_date}}
**Artifact**: product.md
**Tester**: {{tester_name}}

## Vision Tested

{{vision_statement}}

## Test Results

- **Word Count**: {{word_count}}
- **Sentence Count**: {{sentence_count}}
- **Readability Score**: {{readability_score}}

### Passed Criteria
{{list_passed_criteria}}

### Failed Criteria
{{list_failed_criteria}}

### Warnings
{{list_warnings}}

## Overall Result

**STATUS**: [ ] PASS / [ ] FAIL

## Recommendations

{{recommendations_for_improvement}}

---

**Next Steps**:
- [ ] Address all failed criteria
- [ ] Consider warnings for improvement
- [ ] Re-run test after revisions
```

---

## References

- **[inspired-book]** Cagan, M. (2017). *Inspired*, p.35-42 (Product Vision characteristics)
- **[concept-product-vision]** `3-atomics/concept-product-vision.json` (Vision definition and validation rules)
- **[analysis-001]** `2-analysis/analysis-001-product-vision-components.md` (Literature synthesis)

---

## Test Maintenance

### When to Update This Test

- When new vision criteria are discovered in literature
- When validation rules change in `concept-product-vision.json`
- When spec-workflow-mcp updates product.md format requirements

### Version History

- **v1.0.0** (2026-01-11): Initial test based on Cagan, Pichler, Maurya frameworks

---

**Test Status**: ✅ READY FOR USE
**Related Tests**:
- TEST-PRODUCT-002: Target Group Completeness
- TEST-PRODUCT-003: Success Criteria Validation

**Usage**: Run this test after drafting vision statement, before compilation to product.md
