from app.conversation.conversation import Conversation


def test_conversation_can_be_created():

    conversation = Conversation()

    assert conversation is not None