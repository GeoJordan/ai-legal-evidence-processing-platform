from app.models.attachment import Attachment
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_email_message_can_be_created():

    header = EmailHeader(
        message_id="<123>",
        sender="alice@example.com",
        to=["bob@example.com"],
        subject="Meeting",
    )

    message = EmailMessage(
        header=header,
        body="Hello World",
        is_html=False,
    )

    assert message.header.subject == "Meeting"
    assert message.header.to == ["bob@example.com"]
    assert message.body == "Hello World"
    assert not message.is_html


def test_email_message_can_hold_attachments():

    header = EmailHeader(
        message_id="<123>",
        sender="alice@example.com",
        to=["bob@example.com"],
        subject="Report",
    )

    attachment = Attachment(
        filename="report.pdf",
        content_type="application/pdf",
        size=512,
        data=b"PDF",
    )

    message = EmailMessage(
        header=header,
        body="See attached report.",
        attachments=[attachment],
    )

    assert len(message.attachments) == 1
    assert message.attachments[0].filename == "report.pdf"