# ADR-005: Evidence Domain Model

---

## Status

Accepted

---

## Context

The AI Legal Evidence Processing Platform originally represented evidence using dictionaries and generic Python objects. As the platform expanded to support emails, PDFs, images, WhatsApp conversations, court documents, timelines, and AI-generated reports, this representation became difficult to extend and maintain.

---

## Decision

### EvidenceItem

EvidenceItem is the abstract base class for all evidence types.

### EvidenceType

EvidenceType provides a strongly typed enumeration used throughout the platform.

### Specialized Evidence Classes

Each evidence source is modeled as its own domain object.

Examples:

- EmailEvidence
- PdfEvidence
- ImageEvidence
- WordDocumentEvidence
- AttachmentEvidence
- TextMessageEvidence
- WhatsAppEvidence
- CourtDocumentEvidence
- ConversationEvidence
- CalendarEventEvidence

### EvidenceIndex

EvidenceIndex is a repository responsible for organizing evidence objects.

### Common Interface

Every evidence object exposes:

- title
- evidence_type
- source
- collected_at

This enables polymorphism throughout the platform.

---

## Architecture

```text
EvidenceItem
        ▲
        │
 ┌──────┼──────────────────────────┐
 │      │      │        │          │
Email  PDF   Image   WhatsApp   CourtDocument
 │
 └──────────────┐
                ▼
         AttachmentEvidence

EvidenceIndex
        │
        ▼
EvidenceStatisticsCalculator
        │
        ▼
TimelineGenerator
        │
        ▼
ConversationBuilder
        │
        ▼
CaseReport
```

---

## Architecture Decision Records

- ADR-001 — Architecture Decisions
- ADR-005 — Evidence Domain Model

---

## Alternatives Considered

### Option 1
Use dictionaries to represent evidence.

Rejected because:
- weak typing
- difficult to extend
- poor IDE support
- no polymorphism

### Option 2
Single generic Evidence class.

Rejected because:
- mixes unrelated responsibilities
- difficult to model provider-specific metadata
- leads to many conditional statements

### Option 3 (Accepted)
Inheritance from EvidenceItem.

Chosen because:
- strong typing
- extensibility
- polymorphism
- easier testing

---

## Guiding Principles

- Every evidence source is modeled as a domain object.
- Evidence objects remain immutable after ingestion whenever practical.
- Shared behavior belongs in EvidenceItem.
- Specialized behavior belongs in subclasses.
- EvidenceIndex stores evidence but is not itself evidence.
- AI components operate on domain objects rather than raw dictionaries.

---

## Consequences

Positive outcomes:

- cleaner architecture
- polymorphism
- easier AI integration
- easier testing
- easier statistics
- easier timeline generation

Trade-offs:

- more classes
- more files
- slightly higher initial complexity

---

## Future Evolution

Document what comes next.

Examples:

- Metadata object
- Evidence relationships
- Evidence hashing
- OCR metadata
- AI annotations
- Evidence graph

---

## Related Components

- app/evidence/
- app/timeline/
- app/conversation/
- app/case_report/
