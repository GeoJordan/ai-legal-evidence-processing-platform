from app.conversation.conversation import Conversation
from app.conversation.conversation_timeline import ConversationTimeline


def test_conversation_timeline_can_be_created():

    timeline = ConversationTimeline()

    assert timeline is not None