from app.conversation.conversation_builder import ConversationBuilder


def test_builder_can_be_created():

    builder = ConversationBuilder()

    assert builder is not None