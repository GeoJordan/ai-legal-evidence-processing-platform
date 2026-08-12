from app.evidence.email_evidence import EmailEvidence
from app.evidence.evidence_type import EvidenceType


def test_email_evidence_stores_fields():

    email = EmailEvidence(
        sender="alice@example.com",
        recipients=["bob@example.com"],
        subject="Meeting",
        body="Let's meet tomorrow."
    )

    assert email.sender == "alice@example.com"
    assert email.recipients == ["bob@example.com"]
    assert email.subject == "Meeting"
    assert email.body == "Let's meet tomorrow."


def test_email_evidence_title_returns_subject():

    email = EmailEvidence(
        subject="Quarterly Report"
    )

    assert email.title == "Quarterly Report"


def test_email_evidence_inherits_common_properties():

    email = EmailEvidence()

    assert email.evidence_type == EvidenceType.EMAIL
    assert email.source == "email"
    assert email.collected_at is not None


def test_email_evidence_default_recipients_is_empty_list():

    email = EmailEvidence()

    assert email.recipients == []
