# Citation Validation Report Template

**Protocol Version**: v0.3.0
**Validation Date**: YYYY-MM-DD
**Validator**: [Human/AI/Tool identifier]
**Document Validated**: [Document name]

---

## Validation Metadata

```json
{
  "protocol_version": "0.3.0",
  "validation_id": "unique-id",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "validator": "[validator identifier]",
  "tools_used": ["verify_citation.py", "Crossref API"],
  "documents": ["document1.md", "document2.md"]
}
```

---

## Executive Summary

| Document | Total | Tier 1 (DOI) | Tier 2 (Secondary) | Books | Result |
|----------|-------|--------------|-------------------|-------|--------|
| Doc 1 | 0 | 0 | 0 | 0 | 0/0 VERIFIED |
| **Total** | **0** | **0** | **0** | **0** | **0/0 (100%)** |

---

## Journal Articles - Tier 1 (Crossref DOI)

| # | Citation | DOI | Verification | Status |
|---|----------|-----|--------------|--------|
| 1 | Author (Year) | 10.xxxx/xxxxx | Journal Vol:Pages | VERIFIED |

---

## Pre-DOI Papers - Tier 2 (Step 2b)

| # | Citation | Source | Verification | Status |
|---|----------|--------|--------------|--------|
| 1 | Author (Year) | JSTOR/Google Scholar | Journal Vol:Pages | VERIFIED_VIA_SECONDARY |

---

## Books - Step B1 (DOI)

| # | Citation | DOI | Publisher | Status |
|---|----------|-----|-----------|--------|
| 1 | Author (Year) | 10.xxxx/xxxxx | Publisher | VERIFIED |

---

## Books - Step B2 (ISBN)

| # | Citation | ISBN | Publisher | Status |
|---|----------|------|-----------|--------|
| 1 | Author (Year) | X-XX-XXXXXX-X | Publisher | VERIFIED |

---

## Book Chapters - Step B3

| # | Citation | Volume | Pages | Status |
|---|----------|--------|-------|--------|
| 1 | Author (Year) | Volume Title (Editor) | XX-XX | VERIFIED |

---

## Issues Found

### ISSUE N: [Error Type] - [Status]

**Citation**: [Original citation]
**Location**: [Document, line number]
**Error Type**: [WRONG_JOURNAL/WRONG_YEAR/WRONG_AUTHORS/etc.]
**Status**: [CORRECTED/UNRESOLVED]

| Field | Provided | Correct |
|-------|----------|---------|
| [field] | [provided value] | [correct value] |

**Source**: [URL to authoritative source]

**Corrected citation**:
> [Corrected citation text]

---

## Verification Notes

- [Any notes about the verification process]
- [Sources that were particularly helpful or problematic]
- [Recommendations for future validations]

---

*Report generated using reference_validation_protocol v0.3.0*
