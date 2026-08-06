from app.models.email_header import EmailHeader


def test_email_header_can_be_created():

    header = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Test",
        date="Today",
        message_id="<123>"
    )

    assert header.sender == "alice@example.com"
    assert header.subject == "Test"