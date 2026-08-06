# EP-206B — Ingestor Registry

---

## Document Control

| Field | Value |
|-------|-------|
| **Project** | AI Legal Evidence Processing Platform |
| **Document ID** | EP-206B |
| **Document Title** | Ingestor Registry |
| **Version** | 1.0 |
| **Status** | Approved for Implementation |
| **Sprint** | Sprint 5 — Evidence Ingestion Framework |
| **Author** | George Jordan |
| **Repository** | AI Legal Evidence Processing Platform |
| **Last Updated** | August 2026 |

---

# 1. Purpose

The Ingestor Registry manages all available evidence ingestors and determines which ingestor should process a given evidence source.

---

# 2. Responsibilities

- Register ingestors
- Locate a compatible ingestor
- Decouple evidence routing from processing
- Support future ingestors without modifying the pipeline

---

# 3. Processing Flow

Evidence Source

↓

Registry

↓

Matching Ingestor

↓

EvidenceContext

---

# 4. Public Interface

class IngestorRegistry

register(ingestor)

find(path)

---

## Version 1.0 Status

- 🚧 Design Complete
- ⏳ Implementation Pending
