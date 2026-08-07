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

from datetime import date


def test_conversation_stores_start_date():

    conversation = Conversation()

    conversation.start_date = date(2026, 8, 1)

    assert conversation.start_date == date(2026, 8, 1)


def test_conversation_stores_end_date():

    conversation = Conversation()

    conversation.end_date = date(2026, 8, 5)

    assert conversation.end_date == date(2026, 8, 5)


def test_conversation_message_count():

    conversation = Conversation()

    conversation.messages.append("A")
    conversation.messages.append("B")
    conversation.messages.append("C")

    assert conversation.message_count == 3

