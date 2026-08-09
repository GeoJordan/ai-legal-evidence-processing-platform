# 🏗️ NI-001 — Narrative Intelligence Architecture

---

## Document Information

| Field | Value |
|-------|-------|
| Document ID | NI-001 |
| Title | Narrative Intelligence Architecture |
| Version | 1.0 (Draft) |
| Status | Draft |
| Sprint | Sprint 9 |
| Repository | AI Legal Evidence Processing Platform |
| Owner | George Jordan |

---

# 1. Purpose

This document defines the technical architecture for the Narrative Intelligence subsystem introduced during Sprint 9.

Narrative Intelligence transforms structured legal evidence into investigator-ready insights by constructing timelines, generating evidence-backed narratives, identifying potential contradictions, preparing attorney briefs, and recommending exhibits.

The architecture extends the existing Evidence Intelligence and Case Management capabilities without introducing breaking changes to the platform's domain model.

---

# 2. Scope

The Narrative Intelligence subsystem includes:

- Timeline Intelligence
- Narrative Builder
- Contradiction Detection
- Attorney Brief Generator
- Exhibit Intelligence

This specification defines:

- architecture
- data flow
- component interactions
- service boundaries
- integration points

Implementation details are intentionally excluded.

---

# 3. Architectural Vision

The platform evolves from evidence management to investigation intelligence.

```text
Evidence Sources
        │
        ▼
Evidence Intelligence
        │
        ▼
Conversation Intelligence
        │
        ▼
Case Management
        │
        ▼
Narrative Intelligence
        │
        ▼
Attorney Briefing
```

Narrative Intelligence serves as the reasoning layer between structured evidence and investigator-ready outputs.

---

# 4. Architectural Goals

The subsystem shall:

- generate evidence-backed narratives
- preserve evidence traceability
- remain explainable
- support incremental evolution
- integrate with existing services
- avoid duplicate domain models

---

# 5. Domain Integration

Narrative Intelligence operates on the existing domain model.

```text
Workspace
        │
        ▼
Case
        │
        ▼
Allegation
        │
        ▼
Evidence
```

No new root entities are introduced.

Narrative Intelligence consumes these domain objects to generate higher-level insights.

---

# 6. Service Architecture

```text
Timeline Intelligence
        │
        ▼
Narrative Builder
        │
        ▼
Contradiction Detection
        │
        ▼
Attorney Brief Generator
        │
        ▼
Exhibit Intelligence
```

Each service performs a single responsibility and communicates using existing domain objects.

---

# 7. Processing Pipeline

The Narrative Intelligence pipeline follows a deterministic workflow.

```text
Evidence
      │
      ▼
Timeline Construction
      │
      ▼
Narrative Generation
      │
      ▼
Contradiction Analysis
      │
      ▼
Attorney Brief Generation
      │
      ▼
Exhibit Recommendation
```

Each stage produces structured outputs consumed by the next stage.

---

# 8. Component Responsibilities

## Timeline Intelligence

Responsible for:

- chronological event ordering
- event normalization
- timeline generation

---

## Narrative Builder

Responsible for:

- evidence-backed narrative generation
- chronological storytelling
- narrative formatting

---

## Contradiction Detection

Responsible for:

- identifying inconsistent statements
- detecting unsupported allegations
- highlighting potential conflicts

---

## Attorney Brief Generator

Responsible for:

- executive summaries
- allegation summaries
- evidence summaries
- investigation highlights

---

## Exhibit Intelligence

Responsible for:

- exhibit recommendation
- evidence grouping
- allegation-to-exhibit mapping

---

# 9. Data Flow

```text
Evidence
      │
      ▼
Timeline Events
      │
      ▼
Narrative
      │
      ▼
Contradictions
      │
      ▼
Attorney Brief
      │
      ▼
Exhibit Package
```

Every stage enriches the previous stage without modifying the original evidence.

```text
                    LEGAL EVIDENCE

Emails ─┐
Texts ──┤
Photos ─┤
PDFs ───┤
Records ┘
     │
     ▼
Evidence Intelligence
     │
     ▼
Case Management
     │
     ▼
Timeline Intelligence
     │
     ▼
Narrative Builder
     │
     ▼
Contradiction Detection
     │
     ▼
Attorney Brief
     │
     ▼
Exhibit Package
     │
     ▼
Investigator

---

# 10. Design Principles

Narrative Intelligence follows the architectural principles established in ADR-005.

- Evidence First
- Timeline Before Narrative
- Human-in-the-Loop
- Explainability by Design
- Service-Oriented Architecture

---

# 11. Non-Goals

Narrative Intelligence shall not:

- provide legal advice
- determine liability
- replace attorney judgment
- alter original evidence
- fabricate facts
- generate unsupported conclusions

---

# 12. Testing Strategy

Each service shall include:

- unit tests
- integration tests
- deterministic outputs
- regression coverage

The platform demonstration shall integrate all Narrative Intelligence services.

---

# 13. Security Considerations

Narrative Intelligence processes potentially sensitive legal evidence.

The subsystem shall:

- preserve evidence integrity
- avoid modifying source evidence
- maintain auditability
- support future access controls
- support future chain-of-custody enhancements

---

# 14. Future Evolution

Future releases may introduce:

- AI-assisted summarization
- confidence scoring
- semantic reasoning
- witness comparison
- legal knowledge graphs
- multi-case intelligence
- retrieval-augmented generation (RAG)

without requiring architectural redesign.

---

# 15. Traceability

| Artifact | Reference |
|----------|-----------|
| Milestone | MILESTONE-003 |
| ADR | ADR-005 |
| Sprint | Sprint 9 |
| Planned Release | v0.9.0 |

---

# 16. Architecture Summary

Narrative Intelligence introduces an explainable reasoning layer that transforms structured evidence into investigator-ready narratives while preserving traceability, modularity, and auditability.

The subsystem extends the platform from Evidence Intelligence toward Investigation Intelligence without introducing breaking architectural changes.

---

**End of Document**