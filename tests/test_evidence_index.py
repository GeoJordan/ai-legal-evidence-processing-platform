from app.evidence.evidence_index import EvidenceIndex

from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_evidence_index_can_be_created():

    index = EvidenceIndex()

    assert index is not None


def test_evidence_index_can_add_message():

    index = EvidenceIndex()

    header = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Meeting",
        date="2026-08-06",
        message_id="<123@example.com>",
    )

    message = EmailMessage(
        header=header,
        body="Hello",
    )

    index.add_message(message)

    assert index.message_count() == 1

from app.models.attachment import Attachment


def test_evidence_index_can_add_attachment():

    index = EvidenceIndex()

    attachment = Attachment(
        filename="evidence.pdf",
        content_type="application/pdf",
        data=b"PDF DATA"
    )

    index.add_attachment(attachment)

    assert index.attachment_count() == 1

from app.models.attachment import Attachment


def test_evidence_index_can_add_attachment():

    index = EvidenceIndex()

    attachment = Attachment(
        filename="evidence.pdf",
        content_type="application/pdf",
        size=8,
        data=b"PDF DATA",
    )

    index.add_attachment(attachment)

    assert index.attachment_count() == 1