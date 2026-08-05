# SRS-001 — Evidence Organizer Version 2 Requirements

---

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | SRS-001 |
| Title | Evidence Organizer Version 2 Requirements |
| Version | 1.0 |
| Status | Draft |
| Project | Litigation Management System |
| Prepared By | George Jordan |

---

## 2. Purpose

Evidence Organizer Version 2 will safely examine, classify, index, and organize litigation evidence without modifying the original source files.

---

## 3. Primary Objectives

The application shall:

1. Scan evidence folders recursively.
2. Preserve all original files without alteration.
3. Calculate a SHA-256 hash for every file.
4. detect duplicate files.
5. Extract text from supported file types.
6. Classify evidence by allegation.
7. Detect relevant years and dates where possible.
8. Record every processed file in an evidence register.
9. Record unsupported files and processing errors.
10. Support a dry-run mode before copying files.
11. Prevent accidental overwriting of files.
12. Generate a processing summary.

---

## 4. Supported File Types for Version 2.0

### Initial release

- TXT
- LOG
- EML
- PNG
- JPG
- JPEG

### Future releases

- PDF
- DOCX
- MSG
- TIFF
- Audio
- Video

---

## 5. Required Outputs

The application shall generate:

- `evidence_register.csv`
- `processing_log.txt`
- `processing_summary.txt`
- `categorized_views/`
- `review_queue/`
- `duplicates/`
- `unsupported/`

---

## 6. Evidence Register Fields

The evidence register shall contain:

- Evidence ID
- Original filename
- Original path
- File extension
- File size
- SHA-256 hash
- Created timestamp
- Modified timestamp
- Extraction status
- Matched allegations
- Matched years
- Matched keywords
- Confidence level
- Duplicate status
- Review required
- Output location
- Processing notes

---

## 7. Safety Requirements

1. Original files shall never be renamed.
2. Original files shall never be deleted.
3. Original files shall never be modified.
4. Existing output files shall not be overwritten silently.
5. Every copied file shall remain traceable to its original location.
6. Processing errors shall be recorded rather than silently ignored.
7. Dry-run mode shall perform analysis without copying files.

---

## 8. Classification Requirements

Each classification shall record:

- matched category;
- matched keyword;
- number of keyword matches;
- match source;
- confidence level.

Proposed confidence levels:

- High: three or more relevant matches
- Medium: two relevant matches
- Low: one relevant match
- None: no relevant matches

Low-confidence and conflicting classifications shall be placed in the review queue.

---

## 9. Out of Scope for Version 2.0

The following are postponed:

- automatic trial exhibit designation;
- legal conclusions;
- AI-generated case recommendations;
- automatic deletion of duplicates;
- automatic document redaction;
- court filing;
- cloud synchronization;
- dashboard development.

---

## 10. Acceptance Criteria

Version 2.0 will be accepted when it can:

1. scan a test folder recursively;
2. analyze supported files;
3. calculate reliable hashes;
4. identify duplicates;
5. classify evidence;
6. create an accurate evidence register;
7. complete a dry run without modifying or copying source evidence;
8. complete a live test without overwriting existing files;
9. log unsupported files and errors;
10. produce a processing summary.
