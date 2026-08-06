from app.context import EvidenceContext


def test_context_can_be_created():

    context = EvidenceContext()

    assert context.message_count == 0
    assert context.headers == []
    assert context.messages == []
    assert context.attachments == []


def test_context_stores_email_data():

    context = EvidenceContext()

    assert context.message_count == 0
    assert context.headers == []
    assert context.messages == []
    assert context.attachments == []