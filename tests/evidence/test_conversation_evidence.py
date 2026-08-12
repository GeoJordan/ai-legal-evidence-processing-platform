from app.evidence.conversation_evidence import ConversationEvidence
from app.evidence.email_evidence import EmailEvidence
from app.evidence.evidence_item import EvidenceItem


# store fields
def test_conversation_stores_fields():

    email = EmailEvidence(subject="Passport")

    conversation = ConversationEvidence(
        conversation_id="CONV-001",
        title="Passport Discussion",
        participants=["George", "Alice"],
        messages=[email],
        started_at="2026-08-01",
        ended_at="2026-08-02",
    )

    assert conversation.conversation_id == "CONV-001"
    assert conversation.title == "Passport Discussion"
    assert conversation.participants == ["George", "Alice"]
    assert conversation.messages == [email]
    assert conversation.started_at == "2026-08-01"
    assert conversation.ended_at == "2026-08-02"

# messages contain evidence objects
def test_conversation_messages_are_evidence_items():

    email = EmailEvidence(subject="Evidence")

    conversation = ConversationEvidence(
        messages=[email]
    )

    assert isinstance(conversation.messages[0], EvidenceItem)

# inheritance
def test_conversation_inherits_common_properties():

    conversation = ConversationEvidence()

    assert isinstance(conversation, EvidenceItem)

# defaults
def test_conversation_defaults():

    conversation = ConversationEvidence()

    assert conversation.conversation_id == ""
    assert conversation.title == ""
    assert conversation.participants == []
    assert conversation.messages == []
    assert conversation.started_at is None
    assert conversation.ended_at is None