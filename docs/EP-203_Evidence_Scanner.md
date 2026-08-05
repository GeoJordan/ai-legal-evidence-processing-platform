# EP-203 — Evidence Scanner

---

## Purpose

The Evidence Scanner discovers all supported evidence files contained within a legal case.

It provides the first processing stage after configuration loading and returns a structured inventory of evidence for downstream modules.

---

## Responsibilities

- Scan evidence directories.
- Support recursive scanning.
- Filter supported file types.
- Calculate relative paths.
- Return discovered evidence.

The scanner does **not**:

- Read metadata
- Calculate hashes
- OCR documents
- Classify evidence
- Generate reports

---

## Inputs

Configuration object

---

## Outputs

List of discovered evidence files

---

## Public Interface

```python
scanner = Scanner(configuration)

files = scanner.scan()
```

---

## Testing

test_scanner.py

---

## Future Enhancements

- Ignore hidden files
- Ignore temporary files
- Parallel directory traversal
- Progress reporting
- File count statistics