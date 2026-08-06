from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_email_message_can_be_created():

    header = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Meeting",
        date="Today",
        message_id="<123>"
    )

    message = EmailMessage(
        header=header,
        body="Hello World",
        is_html=False
    )

    assert message.header.subject == "Meeting"
    assert message.body == "Hello World"
    assert not message.is_html