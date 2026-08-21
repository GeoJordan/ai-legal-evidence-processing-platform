from email.message import EmailMessage

from app.evidence.candidate_metadata_inventory import (
    CandidateMetadataInventory,
)


def test_candidate_metadata_inventory_extracts_message_metadata():

    message = EmailMessage()

    message["Message-ID"] = "<candidate-001@example.com>"
    message["Date"] = "Thu, 20 Aug 2026 14:30:00 -0400"
    message["From"] = "person@example.com"
    message["To"] = "me@example.com"
    message["Subject"] = "Synthetic Passport Discussion"

    message.set_content(
        "Synthetic test evidence."
    )

    inventory = CandidateMetadataInventory()

    record = inventory.extract(
        message,
        source_mbox="Inbox-003.mbox",
    )

    assert record["message_id"] == "<candidate-001@example.com>"
    assert record["from"] == "person@example.com"
    assert record["to"] == "me@example.com"
    assert record["subject"] == "Synthetic Passport Discussion"
    assert record["source_mbox"] == "Inbox-003.mbox"

    assert record["date"] is not None
    assert record["has_attachments"] is False

def test_candidate_metadata_inventory_detects_attachment():

    message = EmailMessage()

    message["Message-ID"] = "<candidate-attachment-001@example.com>"
    message["Date"] = "Thu, 20 Aug 2026 14:30:00 -0400"
    message["From"] = "person@example.com"
    message["To"] = "me@example.com"
    message["Subject"] = "Synthetic Email With Attachment"

    message.set_content(
        "Synthetic test message containing an attachment."
    )

    message.add_attachment(
        b"synthetic attachment contents",
        maintype="application",
        subtype="pdf",
        filename="synthetic_document.pdf",
    )

    inventory = CandidateMetadataInventory()

    record = inventory.extract(
        message,
        source_mbox="Inbox-003.mbox",
    )

    assert record["message_id"] == "<candidate-attachment-001@example.com>"
    assert record["has_attachments"] is True