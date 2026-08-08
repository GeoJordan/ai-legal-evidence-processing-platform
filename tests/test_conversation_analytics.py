from app.conversation.conversation_analytics import ConversationAnalytics


def test_conversation_analytics_can_be_created():

    analytics = ConversationAnalytics()

    assert analytics is not None

from datetime import date

from app.conversation.conversation import Conversation
from app.conversation.conversation_analytics import ConversationAnalytics


def test_statistics_returns_basic_metrics():

    conversation = Conversation(
        subject="Passport Request",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 3),
    )

    conversation.messages.extend(["m1", "m2", "m3"])

    conversation.participants.add("alice@example.com")
    conversation.participants.add("bob@example.com")

    analytics = ConversationAnalytics()

    stats = analytics.statistics(conversation)

    assert stats["messages"] == 3
    assert stats["participants"] == 2
    assert stats["start_date"] == date(2026, 8, 1)
    assert stats["end_date"] == date(2026, 8, 3)
    assert stats["duration_days"] == 2

from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_participant_statistics():

    conversation = Conversation()

    conversation.messages.append(
        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="One",
                date="2026-08-01",
                message_id="<1>",
            ),
            body="Hello",
        )
    )

    conversation.messages.append(
        EmailMessage(
            header=EmailHeader(
                sender="bob@example.com",
                recipient="alice@example.com",
                subject="Two",
                date="2026-08-02",
                message_id="<2>",
            ),
            body="Reply",
        )
    )

    analytics = ConversationAnalytics()

    stats = analytics.participants(conversation)

    assert stats["alice@example.com"]["sent"] == 1
    assert stats["alice@example.com"]["received"] == 1

    assert stats["bob@example.com"]["sent"] == 1
    assert stats["bob@example.com"]["received"] == 1