from app.conversation.conversation_report import ConversationReport


def test_conversation_report_can_be_created():

    report = ConversationReport()

    assert report is not None