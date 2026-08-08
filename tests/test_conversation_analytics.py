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