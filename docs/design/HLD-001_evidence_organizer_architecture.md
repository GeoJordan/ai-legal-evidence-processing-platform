# HLD-001 — Evidence Organizer Version 2 Architecture

---

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HLD-001 |
| Title | Evidence Organizer Version 2 Architecture |
| Version | 1.0 |
| Status | Draft |
| Project | Litigation Management System |

---

## 2. Architecture Objective

The application will use separate modules so that file scanning, extraction, classification, evidence registration, and output management can be tested independently.

---

## 3. Processing Flow

```text
Source Evidence
      |
      v
File Scanner
      |
      v
Metadata and Hash Engine
      |
      v
Text Extractor
      |
      v
Classification Engine
      |
      v
Duplicate Detection
      |
      v
Evidence Register
      |
      v
Output and Review Queue

---
