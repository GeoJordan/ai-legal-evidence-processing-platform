from app.conversation.conversation_analytics import ConversationAnalytics


def test_conversation_analytics_can_be_created():

    analytics = ConversationAnalytics()

    assert analytics is not None