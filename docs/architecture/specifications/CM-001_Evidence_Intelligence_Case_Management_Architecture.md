# 📄 CM-001_Evidence_Intelligence_Case_Management_Architecture

---

Version: 1.0
Sprint: 8
Status: Approved
Owner: George Jordan
Approved: 2026-08-08

---

## 1. Purpose

The purpose of this document is to define the architecture for the Evidence Intelligence & Case Management subsystem of the AI Legal Evidence Processing Platform.

This subsystem extends the platform beyond evidence processing by providing structured case management capabilities, enabling investigators and legal professionals to organize evidence, manage allegations, identify evidence gaps, and prepare discovery-ready evidence packages.

---

##  2. Vision

The platform evolves through the following maturity model:

```text
Evidence Sources
        │
        ▼
Evidence Processing
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
```

Each phase builds upon the previous phase while preserving backward compatibility.

---

## 3. Design Principles

The subsystem shall adhere to the following engineering principles:

### Modular Architecture

Each capability shall be implemented as an independent module.

### Test-Driven Development

Every feature begins with failing tests before implementation.

### Workspace-Oriented Design

The platform shall support multiple independent workspaces.

Each workspace may contain multiple legal cases.

### Case-Centric Organization

All evidence belongs to a specific case.

Evidence shall never exist without a parent case.

### Evidence Traceability

Every exhibit, allegation, report, and discovery package shall maintain traceability back to its originating evidence.

### Privacy by Design

The platform is designed to operate on locally stored evidence.

No assumption is made that evidence is uploaded to external services.

---

## 4. Core Domain Model

```text

Workspace
│
├── Case
│     ├── Allegations
│     ├── Evidence
│     ├── Conversations
│     ├── Timeline
│     ├── Discovery
│     ├── Reports
│     └── Exhibits
│
├── Case
│
├── Case
│
└── Dashboard
```

### Case Metadata

Each Case shall maintain core metadata including:

- Case ID
- Case Name
- Case Type
- Status
- Created Date
- Last Updated
- Case Description

---

## 5. Workspace Model

A Workspace is the highest-level organizational boundary within the AI Legal Evidence Processing Platform.

A Workspace represents a collection of one or more legal matters managed by a single user or organization.

Each Workspace owns:

- Cases
- Configuration
- Evidence repositories
- Reports
- Dashboards

Each Case is isolated from every other Case, ensuring evidence, allegations, exhibits, and reports remain independent.

Example:


```text
Workspace

├── Custody Case

├── Civil Litigation

└── Employment Dispute
```

Future versions may support collaborative workspaces and multiple users.

Sprint 8 focuses on a single-user workspace.

### Mental Model

```text

Workspace
        │
        ├──────────────┐
        │              │
      Case A        Case B
        │              │
   Allegations    Allegations
        │              │
    Evidence       Evidence
        │              │
     Reports        Reports
```

---

## 6. Case Model

Each Case represents a single legal matter.

A Case owns:

- Allegations
- Evidence
- Exhibits
- Conversations
- Timeline Events
- Discovery Packages
- Reports

A Case is the primary organizational boundary for all evidence.

---

## 7. Evidence Lifecycle

```text 

Collect
      │
      ▼
Index
      │
      ▼
Analyze
      │
      ▼
Select
      │
      ▼
Organize
      │
      ▼
Package
      │
      ▼
Report
```

---

## 8. Sprint 8 Package Structure

```text

app/
│
├── analytics/
├── conversation/
├── evidence/
├── ingestors/
├── reporting/
├── timeline/
├── models/
│    workspace.py
│    case.py
│    allegation.py
│    evidence.py
│    exhibit.py
│
├── case_management/
│      evidence_selection.py
│      evidence_gap.py
│      discovery_package.py
│      dashboard.py
│
└── utils/
```

---

## 9. Sprint 8 Roadmap

| Milestone | Description                        |
| --------- | ---------------------------------- |
| CM-801    | Workspace Domain Model             |
| CM-802    | Case Domain Model                  |
| CM-803    | Allegation Domain Model            |
| CM-804    | Evidence Domain Model              |
| CM-805    | Workspace → Case Relationship      |
| CM-806    | Case → Allegation Relationship     |
| CM-807    | Case → Evidence Relationship       |
| CM-808    | Allegation → Evidence Relationship |
| CM-809    | Evidence Selection Engine          |
| CM-810    | Evidence Gap Analysis              |
| CM-811    | Discovery Package Builder          |
| CM-812    | Case Dashboard                     |
| CM-813    | End-to-End Demonstration           |

---

## 10. Acceptance Criteria

Sprint 8 will be considered complete when:

- Workspace supports multiple cases.
- Cases manage allegations and evidence independently.
- Evidence Selection Engine identifies relevant evidence.
- Evidence Gap Analysis identifies missing support.
- Discovery Package Builder generates organized exhibit packages.
- Case Dashboard summarizes case readiness.
- A complete end-to-end demonstration showcases the Case Management workflow.
- Domain models are fully covered by automated unit tests.

---

## 11. Guiding Principle

The platform separates persistent domain models from processing services.

Domain models represent legal concepts such as Workspace, Case, Allegation, and Exhibit.

Processing services perform operations on those models, including evidence selection, gap analysis, discovery package generation, analytics, and reporting.

This separation promotes modularity, testability, and long-term maintainability.

---
