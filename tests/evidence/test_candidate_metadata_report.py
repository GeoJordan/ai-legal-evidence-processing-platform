import mailbox
from email.message import EmailMessage

from app.evidence.correspondent_selector import CorrespondentSelector
from app.evidence.date_selector import DateSelector
from app.evidence.candidate_metadata_report import CandidateMetadataReport


def _add_message(
    mbox_path,
    *,
    message_id,
    sender,
    recipient,
    date,
    subject,
    attachment=False,
):
    message = EmailMessage()

    message["Message-ID"] = message_id
    message["From"] = sender
    message["To"] = recipient
    message["Date"] = date
    message["Subject"] = subject

    message.set_content("Synthetic test message.")

    if attachment:
        message.add_attachment(
            b"synthetic attachment",
            maintype="application",
            subtype="pdf",
            filename="synthetic.pdf",
        )

    mbox = mailbox.mbox(str(mbox_path), create=True)

    try:
        mbox.add(message)
        mbox.flush()
    finally:
        mbox.close()


def test_candidate_metadata_report_returns_unique_candidate_records(tmp_path):

    inbox_path = tmp_path / "Inbox.mbox"
    archived_path = tmp_path / "Archived.mbox"

    # Candidate appears in Inbox.
    _add_message(
        inbox_path,
        message_id="<candidate-001@example.com>",
        sender="person@example.com",
        recipient="me@example.com",
        date="Thu, 20 Aug 2026 10:00:00 -0400",
        subject="Passport Discussion",
        attachment=True,
    )

    # Same candidate deliberately duplicated in Archived.
    _add_message(
        archived_path,
        message_id="<candidate-001@example.com>",
        sender="person@example.com",
        recipient="me@example.com",
        date="Thu, 20 Aug 2026 10:00:00 -0400",
        subject="Passport Discussion",
        attachment=True,
    )

    # Second unique candidate.
    _add_message(
        inbox_path,
        message_id="<candidate-002@example.com>",
        sender="me@example.com",
        recipient="person@example.com",
        date="Wed, 10 Jan 2024 10:00:00 -0500",
        subject="Travel Discussion",
    )

    # Unrelated message — must not enter report.
    _add_message(
        inbox_path,
        message_id="<unrelated@example.com>",
        sender="someone@example.com",
        recipient="me@example.com",
        date="Thu, 20 Aug 2026 11:00:00 -0400",
        subject="Unrelated",
    )

    report = CandidateMetadataReport(
        correspondent_selector=CorrespondentSelector(
            "person@example.com"
        ),
        date_selector=DateSelector(
            start_date="2022-01-01"
        ),
    )

    records = report.collect(
        [
            inbox_path,
            archived_path,
        ]
    )

    assert len(records) == 2

    assert records[0]["message_id"] == "<candidate-001@example.com>"
    assert records[0]["subject"] == "Passport Discussion"
    assert records[0]["has_attachments"] is True
    assert records[0]["source_mbox"] == "Inbox.mbox"

    assert records[1]["message_id"] == "<candidate-002@example.com>"
    assert records[1]["subject"] == "Travel Discussion"
    assert records[1]["has_attachments"] is False