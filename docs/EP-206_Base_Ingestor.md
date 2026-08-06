# EP-206 — Base Ingestor

---

# EP-206 — Base Ingestor

---

## Document Control

| Field | Value |
|-------|-------|
| **Project** | AI Legal Evidence Processing Platform |
| **Document ID** | EP-206 |
| **Document Title** | Base Ingestor |
| **Version** | 1.0 |
| **Status** | Approved for Implementation |
| **Sprint** | Sprint 5 — Evidence Ingestion Framework |
| **Author** | George Jordan |
| **Repository** | AI Legal Evidence Processing Platform |
| **Last Updated** | August 2026 |

---

# 1. Purpose

The Base Ingestor defines the standard interface for every evidence ingestion module.

Rather than allowing each evidence source to implement its own interface, every ingestor must inherit from a common base class.

This ensures consistency, extensibility, and interoperability across the platform.

---

# 2. Objectives

- Standardize evidence ingestion
- Support multiple evidence sources
- Enable modular expansion
- Populate the EvidenceContext
- Maintain a common ingestion contract

---

# 3. Supported Evidence Sources

Initial implementations include:

- Local Files
- Gmail Takeout (MBOX)
- ZIP Archives

Future implementations may include:

- Outlook PST
- Microsoft 365
- Google Drive
- Dropbox
- OneDrive
- Mobile Device Exports

---

# 4. Public Interface

class BaseIngestor

name

supports(path)

ingest(path, context)

---

# 5. Responsibilities

Every ingestor must:

- Determine whether it supports a given evidence source.
- Extract evidence.
- Populate the shared EvidenceContext.
- Return the updated context.

---

# 6. Processing Flow

Evidence Source

↓

BaseIngestor

↓

EvidenceContext

↓

Pipeline

↓

ProcessingStage

---

## Version 1.0 Status

- 🚧 Design Complete
- ⏳ Implementation Pending

---

---

# Version 1.0 Status

## Completed

- ✅ Abstract `BaseIngestor` contract
- ✅ Standard ingestion interface
- ✅ Unit test passing

---

## Unit Tests

| Test | Status |
|------|:------:|
| test_base_ingestor_can_be_subclassed | ✅ |

---

## Next Milestone

EP-206B — Ingestor Registry

---
