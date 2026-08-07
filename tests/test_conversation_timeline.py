from app.conversation.conversation import Conversation
from app.conversation.conversation_timeline import ConversationTimeline


def test_conversation_timeline_can_be_created():

    timeline = ConversationTimeline()

    assert timeline is not None

from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_conversation_timeline_returns_messages():

    conversation = Conversation(subject="Passport Request")

    conversation.messages.append(
        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="Passport Request",
                date="2026-08-01",
                message_id="<1>",
            ),
            body="Please send passport.",
        )
    )

    timeline = ConversationTimeline()

    events = timeline.build(conversation)

    assert len(events) == 1

def test_conversation_timeline_sorts_messages_by_date():

    conversation = Conversation(subject="Passport Request")

    conversation.messages.append(
        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="Third",
                date="2026-08-03",
                message_id="<3>",
            ),
            body="Third",
        )
    )

    conversation.messages.append(
        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="First",
                date="2026-08-01",
                message_id="<1>",
            ),
            body="First",
        )
    )

    conversation.messages.append(
        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="Second",
                date="2026-08-02",
                message_id="<2>",
            ),
            body="Second",
        )
    )

    timeline = ConversationTimeline()

    events = timeline.build(conversation)

    assert events[0].header.date == "2026-08-01"
    assert events[1].header.date == "2026-08-02"
    assert events[2].header.date == "2026-08-03"