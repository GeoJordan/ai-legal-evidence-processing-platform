from app.evidence.conversation_builder import ConversationBuilder

from app.evidence.conversation_evidence import ConversationEvidence

from app.evidence.email_evidence import EmailEvidence

from app.evidence.pdf_evidence import PDFEvidence


def test_builder_returns_conversation():

    builder = ConversationBuilder()

    conversation = builder.build([])

    assert isinstance(
        conversation,
        ConversationEvidence,
    )

def test_builder_stores_single_message():

    builder = ConversationBuilder()

    email = EmailEvidence(subject="Quarterly Report")

    conversation = builder.build([email])

    assert len(conversation.messages) == 1

    assert conversation.messages[0] is email

def test_builder_stores_multiple_messages():

    builder = ConversationBuilder()

    email = EmailEvidence()
    pdf = PDFEvidence()

    conversation = builder.build([email, pdf])

    assert len(conversation.messages) == 2

def test_builder_preserves_objects():

    builder = ConversationBuilder()

    email = EmailEvidence()

    conversation = builder.build([email])

    assert conversation.messages[0] is email

