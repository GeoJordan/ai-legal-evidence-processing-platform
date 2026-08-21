from pathlib import Path

from app.evidence.candidate_metadata_csv_qa import (
    CandidateMetadataCsvQA,
)


CSV_PATH = Path(
    "exports/candidate_email_metadata_2022_present.csv"
)

qa = CandidateMetadataCsvQA()

result = qa.validate(CSV_PATH)

print("=" * 60)
print("REAL CANDIDATE METADATA CSV QA")
print("=" * 60)

print("CSV:", CSV_PATH.resolve())
print("Rows:", result["row_count"])
print("Schema valid:", result["schema_valid"])
print("Duplicate Message-IDs:", result["duplicate_message_ids"])
print("Missing Message-IDs:", result["missing_message_ids"])
print("Attachments True:", result["attachment_true"])
print("Attachments False:", result["attachment_false"])
print(
    "Unexpected attachment values:",
    result["unexpected_attachment_values"],
)
print("QA passed:", result["passed"])