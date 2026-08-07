from app.conversation.conversation import Conversation


def test_conversation_can_be_created():

    conversation = Conversation()

    assert conversation is not None

def test_conversation_stores_subject():

    conversation = Conversation(subject="Passport Request")

    assert conversation.subject == "Passport Request"


def test_conversation_stores_messages():

    conversation = Conversation()

    conversation.messages.append("message-1")

    assert len(conversation.messages) == 1


def test_conversation_stores_participants():

    conversation = Conversation()

    conversation.participants.add("alice@example.com")

    conversation.participants.add("bob@example.com")

    assert len(conversation.participants) == 2