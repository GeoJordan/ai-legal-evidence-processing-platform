from app.models.email_header import EmailHeader


def test_email_header_can_be_created():

    header = EmailHeader(
        message_id="<123>",
        sender="alice@example.com",
        to=["bob@example.com"],
        subject="Test",
    )

    assert header.message_id == "<123>"
    assert header.sender == "alice@example.com"
    assert header.to == ["bob@example.com"]
    assert header.subject == "Test"