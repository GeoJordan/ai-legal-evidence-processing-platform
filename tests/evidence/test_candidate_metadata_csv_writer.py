import csv
from datetime import datetime, timezone

from app.evidence.candidate_metadata_csv_writer import (
    CandidateMetadataCsvWriter,
)


def test_candidate_metadata_csv_writer_writes_approved_schema(tmp_path):

    output_path = tmp_path / "candidate_metadata.csv"

    records = [
        {
            "message_id": "<candidate-001@example.com>",
            "date": datetime(
                2026,
                8,
                20,
                14,
                30,
                tzinfo=timezone.utc,
            ),
            "from": "person@example.com",
            "to": "me@example.com",
            "subject": "Synthetic Passport Discussion",
            "source_mbox": "Inbox-003.mbox",
            "has_attachments": True,
        },
        {
            "message_id": "<candidate-002@example.com>",
            "date": datetime(
                2024,
                1,
                10,
                15,
                0,
                tzinfo=timezone.utc,
            ),
            "from": "me@example.com",
            "to": "person@example.com",
            "subject": "Synthetic Travel Discussion",
            "source_mbox": "Sent.mbox",
            "has_attachments": False,
        },
    ]

    writer = CandidateMetadataCsvWriter(output_path)

    writer.write(records)

    assert output_path.exists()

    with output_path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 2

    assert list(rows[0].keys()) == [
        "message_id",
        "date",
        "from",
        "to",
        "subject",
        "source_mbox",
        "has_attachments",
    ]

    assert rows[0]["message_id"] == "<candidate-001@example.com>"
    assert rows[0]["subject"] == "Synthetic Passport Discussion"
    assert rows[0]["source_mbox"] == "Inbox-003.mbox"
    assert rows[0]["has_attachments"] == "True"

    assert rows[1]["message_id"] == "<candidate-002@example.com>"
    assert rows[1]["source_mbox"] == "Sent.mbox"
    assert rows[1]["has_attachments"] == "False"