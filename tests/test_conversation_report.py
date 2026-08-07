from app.conversation.conversation_report import ConversationReport


def test_conversation_report_can_be_created():

    report = ConversationReport()

    assert report is not None

from app.conversation.conversation import Conversation


def test_report_contains_subject():

    conversation = Conversation(subject="Passport Request")

    report = ConversationReport()

    text = report.generate(conversation)

    assert "Passport Request" in text


def test_report_contains_message_count():

    conversation = Conversation()

    conversation.messages.extend(["A", "B", "C"])

    report = ConversationReport()

    text = report.generate(conversation)

    assert "3" in text


def test_report_contains_participant_count():

    conversation = Conversation()

    conversation.participants.add("alice@example.com")
    conversation.participants.add("bob@example.com")

    report = ConversationReport()

    text = report.generate(conversation)

    assert "2" in text