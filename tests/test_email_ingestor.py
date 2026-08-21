from email.message import EmailMessage as RawEmailMessage

from app.context import EvidenceContext
from app.ingestors.email.email_ingestor import EmailIngestor


def test_email_ingestor_populates_context_from_plain_text_email():

    raw_message = RawEmailMessage()

    raw_message["Message-ID"] = "<synthetic-001@example.com>"
    raw_message["From"] = "alice@example.com"
    raw_message["To"] = "bob@example.com"
    raw_message["Subject"] = "Synthetic Passport Email"

    raw_message.set_content(
        "This is synthetic test evidence."
    )

    context = EvidenceContext()
    ingestor = EmailIngestor()

    result = ingestor.ingest(
        raw_message,
        context,
    )

    assert result is context

    assert context.message_count == 1
    assert len(context.headers) == 1
    assert len(context.messages) == 1

    header = context.headers[0]
    message = context.messages[0]

    assert header.message_id == "<synthetic-001@example.com>"
    assert header.sender == "alice@example.com"
    assert header.to == ["bob@example.com"]
    assert header.subject == "Synthetic Passport Email"

    assert message.header is header
    assert "This is synthetic test evidence." in message.body
    assert not message.is_html
    assert message.attachments == []

def test_email_ingestor_normalizes_date_and_reply_metadata():

    raw_message = RawEmailMessage()

    raw_message["Message-ID"] = "<synthetic-002@example.com>"
    raw_message["From"] = "alice@example.com"
    raw_message["To"] = "bob@example.com"
    raw_message["Subject"] = "Re: Synthetic Passport Email"

    raw_message["Date"] = "Thu, 20 Aug 2026 14:30:00 -0400"
    raw_message["Reply-To"] = "reply@example.com"
    raw_message["In-Reply-To"] = "<synthetic-001@example.com>"
    raw_message["References"] = (
        "<synthetic-000@example.com> "
        "<synthetic-001@example.com>"
    )

    raw_message.set_content(
        "This is a synthetic reply message."
    )

    context = EvidenceContext()
    ingestor = EmailIngestor()

    result = ingestor.ingest(
        raw_message,
        context,
    )

    assert result is context
    assert context.message_count == 1

    header = context.headers[0]

    assert header.sent_at is not None
    assert header.sent_at.year == 2026
    assert header.sent_at.month == 8
    assert header.sent_at.day == 20
    assert header.sent_at.hour == 14
    assert header.sent_at.minute == 30

    assert header.reply_to == "reply@example.com"
    assert header.in_reply_to == "<synthetic-001@example.com>"

    assert header.references == [
        "<synthetic-000@example.com>",
        "<synthetic-001@example.com>",
    ]

def test_email_ingestor_extracts_attachment():

    raw_message = RawEmailMessage()

    raw_message["Message-ID"] = "<synthetic-003@example.com>"
    raw_message["From"] = "alice@example.com"
    raw_message["To"] = "bob@example.com"
    raw_message["Subject"] = "Synthetic Email With Attachment"

    raw_message.set_content(
        "Please see the synthetic attachment."
    )

    attachment_data = b"SYNTHETIC PDF CONTENT"

    raw_message.add_attachment(
        attachment_data,
        maintype="application",
        subtype="pdf",
        filename="synthetic_document.pdf",
    )

    context = EvidenceContext()
    ingestor = EmailIngestor()

    result = ingestor.ingest(
        raw_message,
        context,
    )

    assert result is context
    assert context.message_count == 1

    message = context.messages[0]

    assert len(message.attachments) == 1
    assert len(context.attachments) == 1

    attachment = message.attachments[0]

    assert attachment.filename == "synthetic_document.pdf"
    assert attachment.content_type == "application/pdf"
    assert attachment.size == len(attachment_data)
    assert attachment.data == attachment_data

    assert context.attachments[0] is attachment

def test_email_ingestor_handles_html_email():

    raw_message = RawEmailMessage()

    raw_message["Message-ID"] = "<synthetic-004@example.com>"
    raw_message["From"] = "alice@example.com"
    raw_message["To"] = "bob@example.com"
    raw_message["Subject"] = "Synthetic HTML Email"

    raw_message.set_content(
        "<html><body><p>Synthetic HTML evidence.</p></body></html>",
        subtype="html",
    )

    context = EvidenceContext()
    ingestor = EmailIngestor()

    result = ingestor.ingest(
        raw_message,
        context,
    )

    assert result is context
    assert context.message_count == 1
    assert len(context.messages) == 1

    message = context.messages[0]

    assert message.is_html is True
    assert "Synthetic HTML evidence." in message.body
    assert message.attachments == []