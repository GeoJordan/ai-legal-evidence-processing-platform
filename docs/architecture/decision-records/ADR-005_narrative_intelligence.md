# 📐 ADR-005 — Narrative Intelligence Architecture

---

## Document Information

| Field | Value |
|-------|-------|
| ADR ID | ADR-005 |
| Title | Narrative Intelligence |
| Status | Accepted |
| Date | 2026-08-09 |
| Sprint | Sprint 9 |
| Repository | AI Legal Evidence Processing Platform |
| Author | George Jordan |

---

# Context

The AI Legal Evidence Processing Platform has evolved through successive releases that established:

- Evidence Ingestion
- Evidence Intelligence
- Conversation Intelligence
- Case Management

While these capabilities organize and relate evidence, investigators and attorneys still spend significant time manually reconstructing events, identifying inconsistencies, and preparing narratives.

Sprint 9 introduces **Narrative Intelligence** to transform structured evidence into investigator-ready insights while maintaining strict evidence traceability and explainability.

---

# Problem Statement

Legal investigations require more than collecting evidence.

Investigators must determine:

- What happened?
- When did it happen?
- Which evidence supports each event?
- Are there inconsistencies?
- Which exhibits support each allegation?

Performing these activities manually is time-consuming and prone to oversight.

The platform requires an architectural approach that assists investigators without replacing professional judgment.

---

# Decision

The platform shall introduce a dedicated **Narrative Intelligence** subsystem composed of independent services that transform structured evidence into explainable, evidence-backed investigative narratives.

The subsystem shall operate on structured domain objects rather than raw documents whenever possible.

---

# Architectural Principles

## 1. Evidence First

Every narrative statement must be supported by one or more evidence items.

No narrative content shall be generated without traceable supporting evidence.

---

## 2. Timeline Before Narrative

Narratives shall be generated from chronological events.

The processing sequence shall be:

Evidence

↓

Timeline

↓

Narrative

rather than generating narratives directly from raw evidence.

---

## 3. Human-in-the-Loop

Narrative Intelligence shall assist investigators.

The platform shall never:

- determine guilt
- provide legal advice
- make legal conclusions
- replace attorney judgment

Instead, it shall identify:

- timelines
- evidence relationships
- potential contradictions
- evidence gaps
- recommended exhibits

---

## 4. Explainability by Design

Every generated observation shall identify the evidence supporting it.

Users must be able to trace conclusions back to the original evidence.

---

## 5. Service-Oriented Design

Narrative Intelligence shall be implemented as independent services.

Initial services include:

- Timeline Intelligence
- Narrative Builder
- Contradiction Detection
- Attorney Brief Generator
- Exhibit Intelligence

Each service shall expose a single, well-defined public interface.

---

## 6. Domain-Driven Integration

Narrative Intelligence shall integrate with the existing domain model.

Workspace

↓

Case

↓

Allegation

↓

Evidence

↓

Narrative Intelligence

No duplicate domain objects shall be introduced.

---

## 7. Incremental Evolution

Narrative Intelligence shall evolve incrementally.

Future releases may introduce:

- confidence scoring
- semantic relationships
- AI-assisted summarization
- legal knowledge graphs
- witness comparison
- multi-case analytics

without requiring architectural redesign.

---

# Rationale

This architecture provides:

- high traceability
- modular services
- simplified testing
- explainable outputs
- maintainable code
- extensibility

The service-oriented approach also aligns with the architectural patterns established in previous releases.

---

# Alternatives Considered

## Alternative 1 — Monolithic Narrative Engine

Single service responsible for timelines, narratives, contradictions, and briefs.

### Rejected

Reasons:

- difficult to test
- poor separation of concerns
- difficult to extend

---

## Alternative 2 — AI-Only Narrative Generation

Generate narratives directly from AI prompts over raw documents.

### Rejected

Reasons:

- reduced explainability
- difficult evidence traceability
- inconsistent outputs
- increased legal risk

---

## Alternative 3 — Rule-Based Narrative Generation

Generate narratives entirely from deterministic rules.

### Accepted (Initial Implementation)

Reason:

Provides deterministic, explainable outputs suitable for legal investigations.

Future AI capabilities may augment—but not replace—the rule-based foundation.

---

# Consequences

Positive:

- Evidence-backed narratives
- Improved investigator productivity
- Consistent architecture
- High testability
- Clear service boundaries
- Strong explainability

Negative:

- Additional processing stages
- More service orchestration
- Increased architectural complexity

These trade-offs are acceptable in exchange for improved maintainability and auditability.

---

# Architecture Impact

This decision extends the platform architecture from Evidence Intelligence to Investigation Intelligence.

Previous platform workflow:

Evidence
↓
Case Management

Narrative Intelligence extends the workflow to:

Evidence
↓
Timeline Intelligence
↓
Narrative Builder
↓
Contradiction Detection
↓
Attorney Brief Generator
↓
Exhibit Intelligence

This decision introduces no breaking changes to existing domain models or service interfaces.

---

# Traceability

| Artifact | Reference |
|----------|-----------|
| Milestone | MILESTONE-003 |
| Architecture Specification | NI-001 |
| Sprint | Sprint 9 |
| Planned Release | v0.9.0 |

---

# Status

**Accepted**

This Architectural Decision Record establishes the governing architectural principles for the Narrative Intelligence subsystem introduced during Sprint 9.

All Narrative Intelligence services shall conform to the principles documented in this ADR.

---

**End of Document**