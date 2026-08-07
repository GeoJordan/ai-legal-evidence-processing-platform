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

def test_builder_creates_multiple_conversations():

    index = EvidenceIndex()

    subjects = [
        "Passport Request",
        "School Meeting",
        "Medical Appointment",
    ]

    for i, subject in enumerate(subjects):

        message = EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject=subject,
                date=f"2026-08-0{i+1}",
                message_id=f"<{i}@example.com>",
            ),
            body="Example",
        )

        index.add_message(message)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert len(conversations) == 3

def test_each_conversation_has_correct_subject():

    index = EvidenceIndex()

    subjects = [
        "Passport Request",
        "School Meeting",
        "Medical Appointment",
    ]

    for i, subject in enumerate(subjects):

        message = EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject=subject,
                date=f"2026-08-0{i+1}",
                message_id=f"<{i}@example.com>",
            ),
            body="Example",
        )

        index.add_message(message)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert conversations[0].subject == "Passport Request"
    assert conversations[1].subject == "School Meeting"
    assert conversations[2].subject == "Medical Appointment"

def test_builder_groups_reply_into_same_conversation():

    index = EvidenceIndex()

    first = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Passport Request",
            date="2026-08-01",
            message_id="<1>",
        ),
        body="Please send passport.",
    )

    reply = EmailMessage(
        header=EmailHeader(
            sender="bob@example.com",
            recipient="alice@example.com",
            subject="Re: Passport Request",
            date="2026-08-02",
            message_id="<2>",
            in_reply_to="<1>",
        ),
        body="Passport sent.",
    )

    index.add_message(first)
    index.add_message(reply)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert len(conversations) == 1
    assert conversations[0].message_count == 2

def test_builder_groups_nested_replies_into_same_conversation():

    index = EvidenceIndex()

    first = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Passport Request",
            date="2026-08-01",
            message_id="<1>",
        ),
        body="Message 1",
    )

    second = EmailMessage(
        header=EmailHeader(
            sender="bob@example.com",
            recipient="alice@example.com",
            subject="Re: Passport Request",
            date="2026-08-02",
            message_id="<2>",
            in_reply_to="<1>",
        ),
        body="Message 2",
    )

    third = EmailMessage(
        header=EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject="Re: Passport Request",
            date="2026-08-03",
            message_id="<3>",
            in_reply_to="<2>",
        ),
        body="Message 3",
    )

    index.add_message(first)
    index.add_message(second)
    index.add_message(third)

    builder = ConversationBuilder()

    conversations = builder.build(index)

    assert len(conversations) == 1
    assert conversations[0].message_count == 3