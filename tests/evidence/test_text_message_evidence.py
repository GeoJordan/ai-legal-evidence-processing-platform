from app.evidence.text_message_evidence import TextMessageEvidence


# store fields
def test_text_message_stores_fields():
    sms = TextMessageEvidence(
        sender="+13025551234",
        recipient="+13025555678",
        message="I'll pick her up at 5 PM.",
        sent_at="2026-08-10 17:00",
    )

    assert sms.sender == "+13025551234"
    assert sms.recipient == "+13025555678"
    assert sms.message == "I'll pick her up at 5 PM."
    assert sms.sent_at == "2026-08-10 17:00"

# title
def test_text_message_title_is_preview():
    sms = TextMessageEvidence(
        message="This is an important message."
    )

    assert sms.title == "This is an important message."

# inheritance
from app.evidence.evidence_item import EvidenceItem


def test_text_message_inherits_common_properties():
    sms = TextMessageEvidence()

    assert isinstance(sms, EvidenceItem)

# defaults
def test_text_message_defaults_are_empty():
    sms = TextMessageEvidence()

    assert sms.sender == ""
    assert sms.recipient == ""
    assert sms.message == ""

def test_text_message_defaults_are_empty():
    sms = TextMessageEvidence()

    assert sms.sender == ""
    assert sms.recipient == ""
    assert sms.message == ""
    assert sms.title == "Text Message"