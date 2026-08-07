# ADR-002 — Introduce Evidence Intelligence Layer

## Status

Accepted

## Context

The project required a dedicated subsystem for transforming raw evidence into investigator-friendly artifacts.

## Decision

Introduce an Evidence Intelligence layer consisting of:

- EvidenceIndex
- TimelineGenerator
- TimelineEvent

TimelineGenerator provides:

- build()
- export()
- filter_by_sender()
- filter_by_keyword()
- statistics()
- report()

## Consequences

Advantages

- Separation of concerns
- Easier testing
- Extensible analytics
- Supports future AI reasoning

Future extensions

- Conversation threading
- Timeline visualization
- Relationship graphs
- Case narratives