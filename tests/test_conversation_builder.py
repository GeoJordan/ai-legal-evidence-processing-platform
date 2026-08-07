from app.conversation.conversation_builder import ConversationBuilder


def test_builder_can_be_created():

    builder = ConversationBuilder()

    assert builder is not None

from app.conversation.conversation import Conversation
from app.evidence.evidence_index import EvidenceIndex
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_builder_creates_single_conversation():

    index = EvidenceIndex()

    message = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Passport Request",
            date="2026-08-01",
            message_id="<1@example.com>",
        ),
        body="Please send the passport.",
    )

    index.add_message(message)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert len(conversations) == 1

def test_builder_sets_subject():

    index = EvidenceIndex()

    message = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Passport Request",
            date="2026-08-01",
            message_id="<1@example.com>",
        ),
        body="Please send the passport.",
    )

    index.add_message(message)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert conversations[0].subject == "Passport Request"


def test_builder_sets_participants():

    index = EvidenceIndex()

    message = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Passport Request",
            date="2026-08-01",
            message_id="<1@example.com>",
        ),
        body="Please send the passport.",
    )

    index.add_message(message)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert len(conversations[0].participants) == 2