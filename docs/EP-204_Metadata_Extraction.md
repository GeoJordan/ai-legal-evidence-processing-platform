# EP-204 — Evidence Context & Metadata Extraction

---

## Document Control

| Field | Value |
|--------|-------|
| Project | AI Legal Evidence Processing Platform |
| Document ID | EP-204 |
| Version | 1.0 |
| Status | Design |
| Sprint | Sprint 3 |
| Author | George Jordan |

---

# 1. Purpose

Introduce the shared EvidenceContext object and implement metadata extraction for every discovered evidence file.

---

# 2. Responsibilities

EvidenceContext

- Store workflow state
- Store FileRecords
- Store statistics
- Store warnings/errors

Metadata Extractor

- Determine MIME type
- Validate filesystem metadata
- Populate processing context

---

# 3. Processing Flow

Workflow
    │
    ▼
Configuration
    │
    ▼
Scanner
    │
    ▼
EvidenceContext
    │
    ▼
Metadata Extractor
    │
    ▼
Updated EvidenceContext