from pathlib import Path

from app.evidence.correspondent_selector import CorrespondentSelector
from app.evidence.date_selector import DateSelector
from app.evidence.candidate_metadata_report import CandidateMetadataReport
from app.evidence.candidate_metadata_csv_writer import (
    CandidateMetadataCsvWriter,
)


# ---------------------------------------------------------
# Real source MBOX files
# ---------------------------------------------------------

MBOX_PATHS = [
    Path(r"C:\PATH\TO\Inbox-003.mbox"),
    Path(r"C:\PATH\TO\Sent.mbox"),
    Path(r"C:\PATH\TO\Archived.mbox"),
]


# ---------------------------------------------------------
# Correspondent aliases
# ---------------------------------------------------------

TARGET_EMAILS = [
    "person.primary@example.com",
    "person.secondary@example.com",
]

START_DATE = "2022-01-01"


# ---------------------------------------------------------
# Review output
#
# IMPORTANT:
# This is an AI-platform review artifact.
# It is NOT being written to legal-workspace/04_evidence.
# ---------------------------------------------------------

OUTPUT_PATH = Path(
    "exports/candidate_email_metadata_2022_present.csv"
)


# ---------------------------------------------------------
# Build read-only candidate collector
# ---------------------------------------------------------

report = CandidateMetadataReport(
    correspondent_selector=CorrespondentSelector(
        TARGET_EMAILS
    ),
    date_selector=DateSelector(
        start_date=START_DATE
    ),
)


# ---------------------------------------------------------
# Collect unique candidate metadata
# ---------------------------------------------------------

print("Scanning MBOX sources...")

print("\nDiagnostic configuration:")
print("MBOX paths:")

for path in MBOX_PATHS:
    print(
        f"  {path.name}: exists={path.exists()} "
        f"path={path}"
    )

print("Target emails:", TARGET_EMAILS)
print("Start date:", START_DATE)
print()

records = report.collect(MBOX_PATHS)

print(
    f"Unique candidate metadata records collected: {len(records)}"
)


# ---------------------------------------------------------
# Write review CSV
# ---------------------------------------------------------

writer = CandidateMetadataCsvWriter(
    OUTPUT_PATH
)

writer.write(records)


# ---------------------------------------------------------
# Report
# ---------------------------------------------------------

print()
print("=" * 65)
print("CANDIDATE EMAIL METADATA EXPORT COMPLETE")
print("=" * 65)

print("Unique candidate records:", len(records))
print("Output:", OUTPUT_PATH.resolve())

attachment_count = sum(
    1
    for record in records
    if record["has_attachments"]
)

print("Candidates with attachments:", attachment_count)
print(
    "Candidates without attachments:",
    len(records) - attachment_count,
)

print()
print("REVIEW ARTIFACT ONLY.")
print("No evidence files were written to legal-workspace.")