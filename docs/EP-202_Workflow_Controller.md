# EP-202 — Workflow Controller

---

## Document Control

| Field | Value |
|--------|-------|
| **Project** | AI Legal Evidence Processing Platform |
| **Document ID** | EP-202 |
| **Document Title** | Workflow Controller |
| **Version** | 1.0 |
| **Status** | Design |
| **Document Type** | Module Design Specification |
| **Sprint** | Sprint 3 – Processing Framework |
| **Author** | George Jordan |
| **Repository** | AI Legal Evidence Processing Platform |
| **Last Updated** | August 2026 |

---

## 1. Purpose

The Workflow Controller orchestrates the execution of the AI Legal Evidence Processing Platform.

Rather than individual modules calling one another, the Workflow Controller coordinates processing through a series of well-defined stages. This provides a single entry point for the application, simplifies error handling, and allows new processing stages to be added without modifying existing modules.

---

## 2. Responsibilities

The Workflow Controller is responsible for:

- Loading the application configuration.
- Initializing processing modules.
- Executing each processing stage in sequence.
- Logging workflow progress.
- Reporting processing results.
- Handling recoverable processing errors.
- Providing a single entry point for the platform.

The Workflow Controller is **not** responsible for:

- Scanning evidence.
- Extracting metadata.
- Performing OCR.
- Classifying evidence.
- Generating reports.

Each of those responsibilities belongs to dedicated modules.

---

## 3. Processing Framework

The Workflow Controller manages the following processing stages.

```text
Application Start
        │
        ▼
Load Configuration
        │
        ▼
Scan Evidence
        │
        ▼
Extract Metadata
        │
        ▼
Calculate Hashes
        │
        ▼
OCR (Future)
        │
        ▼
Classification (Future)
        │
        ▼
Duplicate Detection
        │
        ▼
Evidence Register
        │
        ▼
Timeline Generation
        │
        ▼
Exhibit Generation
        │
        ▼
Reporting
        │
        ▼
Workflow Complete
```

---

## 4. Public Interface

The Workflow Controller exposes a single execution method.

```python
workflow = Workflow()
workflow.run()
```

Future versions may support:

```python
workflow.run(stage="scanner")

workflow.run(stage="metadata")

workflow.run(stage="timeline")
```

---

## 5. Processing Stages

| Stage | Module | Status |
|---------|--------|--------|
| Load Configuration | Configuration | Implemented |
| Scan Evidence | Scanner | Sprint 3 |
| Metadata Extraction | Metadata | Sprint 3 |
| Hash Verification | Hash Engine | Planned |
| OCR | OCR Engine | Planned |
| Classification | AI Classification | Planned |
| Duplicate Detection | Duplicate Detector | Planned |
| Evidence Register | Register Engine | Planned |
| Timeline | Timeline Generator | Planned |
| Exhibit Generator | Exhibit Generator | Planned |
| Reporting | Report Exporter | Planned |

---

## 6. Error Handling

The Workflow Controller shall:

- Stop processing on unrecoverable errors.
- Record processing status.
- Log failed stages.
- Return meaningful exceptions.
- Support future retry capabilities.

---

## 7. Design Principles

- Single Responsibility Principle
- Modular architecture
- Pipeline processing
- Configuration-driven execution
- Extensible stage-based design
- Test-Driven Development

---

## 8. Deliverables

Sprint 3 will deliver:

- Workflow Controller
- Workflow unit tests
- Scanner integration
- Metadata integration

Status:

**In Progress**