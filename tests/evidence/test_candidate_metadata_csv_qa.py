import csv

from app.evidence.candidate_metadata_csv_qa import (
    CandidateMetadataCsvQA,
)


def test_candidate_metadata_csv_qa_validates_clean_file(tmp_path):

    csv_path = tmp_path / "candidate_metadata.csv"

    with csv_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "message_id",
                "date",
                "from",
                "to",
                "subject",
                "source_mbox",
                "has_attachments",
            ],
        )

        writer.writeheader()

        writer.writerow(
            {
                "message_id": "<candidate-001@example.com>",
                "date": "2026-08-20T14:30:00-04:00",
                "from": "person@example.com",
                "to": "me@example.com",
                "subject": "Synthetic Passport Discussion",
                "source_mbox": "Inbox-003.mbox",
                "has_attachments": "True",
            }
        )

        writer.writerow(
            {
                "message_id": "<candidate-002@example.com>",
                "date": "2024-01-10T10:00:00-05:00",
                "from": "me@example.com",
                "to": "person@example.com",
                "subject": "Synthetic Travel Discussion",
                "source_mbox": "Sent.mbox",
                "has_attachments": "False",
            }
        )

    qa = CandidateMetadataCsvQA()

    result = qa.validate(csv_path)

    assert result["row_count"] == 2
    assert result["duplicate_message_ids"] == 0
    assert result["missing_message_ids"] == 0

    assert result["attachment_true"] == 1
    assert result["attachment_false"] == 1

    assert result["unexpected_attachment_values"] == 0

    assert result["schema_valid"] is True
    assert result["passed"] is True