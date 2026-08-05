# EP-201 — Configuration Engine

---

## Document Control

| Field | Value |
|--------|-------|
| **Project** | AI Legal Evidence Processing Platform |
| **Document ID** | EP-201 |
| **Document Title** | Configuration Engine |
| **Version** | 1.0 |
| **Status** | Implemented |
| **Document Type** | Module Design Specification |
| **Sprint** | Sprint 2 – Foundation & Configuration |
| **Author** | George Jordan |
| **Repository** | AI Legal Evidence Processing Platform |
| **Last Updated** | August 2026 |

---

## Revision History

| Version | Date | Author | Description |
|----------|------|--------|-------------|
| 1.0 | August 2026 | George Jordan | Initial implementation of the Configuration Engine. |

---

# 1. Purpose

The Configuration Engine provides a centralized mechanism for loading, validating, and exposing runtime configuration for the AI Legal Evidence Processing Platform.

It serves as the single source of truth for application settings and eliminates hard-coded paths throughout the codebase.

The engine enables the platform to process different legal cases without modifying application code by loading case-specific settings from an external YAML configuration file.

---

# 2. Objectives

The Configuration Engine shall:

- Load runtime configuration from a YAML file.
- Provide a single source of truth for application settings.
- Eliminate hard-coded file system paths.
- Build standardized project paths.
- Support reusable processing across multiple legal cases.
- Simplify future configuration management.

---

# 3. Architecture

```text
config/
│
└── case.yaml
        │
        ▼
Configuration
        │
        ├── Case Information
        ├── Folder Locations
        ├── Processing Settings
        └── Output Settings
```

---

# 4. Responsibilities

The Configuration Engine is responsible for:

- Loading YAML configuration files.
- Reading case metadata.
- Reading folder configuration.
- Reading processing settings.
- Providing strongly typed configuration properties.
- Constructing commonly used directory paths.
- Providing configuration to all application modules.

The Configuration Engine is **not** responsible for:

- Scanning evidence.
- Processing files.
- OCR.
- Metadata extraction.
- Classification.
- Report generation.

---

# 5. Configuration File

The platform currently uses:

```text
config/
└── case.yaml
```

The configuration file contains:

- Case information
- Repository paths
- Folder definitions
- Processing settings
- Output settings

---

# 6. Public Interface

The Configuration class exposes:

| Property | Purpose |
|----------|---------|
| `case_name` | Name of the legal case |
| `case_root` | Root case directory |
| `evidence_path` | Full evidence directory |
| `exhibits_path` | Exhibit directory |
| `timeline_path` | Timeline directory |
| `supported_extensions` | Supported evidence file types |
| `recursive_scan` | Enable recursive scanning |

---

# 7. Dependencies

External Libraries

- PyYAML

Python Standard Library

- pathlib

---

# 8. Testing

Unit Tests

```
tests/
└── test_configuration.py
```

The current test suite verifies:

- Configuration file loading.
- Property initialization.
- Supported file extensions.
- Case root path generation.

All tests are currently passing.

---

# 9. Design Principles

The Configuration Engine follows the following engineering principles:

- Single Responsibility Principle
- Configuration over hard-coded values
- Separation of concerns
- Reusability
- Test-Driven Development
- Modular architecture

---

# 10. Future Enhancements

Planned improvements include:

- Configuration validation.
- Custom exception handling.
- Environment-specific configurations.
- Multiple case profiles.
- JSON configuration support.
- Environment variable overrides.
- Configuration schema validation.

---

# 11. Sprint Deliverables

Sprint 2 delivered:

- Configuration Engine
- YAML configuration support
- Configuration class
- Unit tests
- Project-local configuration architecture

Status:

**Completed**
