from app.evidence.whatsapp_evidence import WhatsAppEvidence
from app.evidence.evidence_item import EvidenceItem


# ----------------------------------------------------
# stores fields
# ----------------------------------------------------
def test_whatsapp_evidence_stores_fields():
    whatsapp = WhatsAppEvidence(
        sender="George",
        participants=["George", "Alice"],
        chat_name="Parenting Chat",
        message="I'll bring the passport tomorrow.",
        sent_at="2026-08-10",
    )

    assert whatsapp.sender == "George"
    assert whatsapp.participants == ["George", "Alice"]
    assert whatsapp.chat_name == "Parenting Chat"
    assert whatsapp.message == "I'll bring the passport tomorrow."
    assert whatsapp.sent_at == "2026-08-10"


# ----------------------------------------------------
# title
# ----------------------------------------------------
def test_whatsapp_evidence_title_returns_preview():
    whatsapp = WhatsAppEvidence(
        message="I'll bring the passport tomorrow."
    )

    assert whatsapp.title == "I'll bring the passport tomorrow."


# ----------------------------------------------------
# inheritance
# ----------------------------------------------------
def test_whatsapp_evidence_inherits_common_properties():
    whatsapp = WhatsAppEvidence()

    assert isinstance(whatsapp, EvidenceItem)


# ----------------------------------------------------
# defaults
# ----------------------------------------------------
def test_whatsapp_evidence_defaults_are_empty():
    whatsapp = WhatsAppEvidence()

    assert whatsapp.sender == ""
    assert whatsapp.participants == []
    assert whatsapp.chat_name == ""
    assert whatsapp.message == ""
    assert whatsapp.title == "WhatsApp Message"