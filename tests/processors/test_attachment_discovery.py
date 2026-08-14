from email.message import EmailMessage

from app.processors.attachment_discovery import AttachmentDiscovery


def test_email_without_attachments():

    message = EmailMessage()

    attachments = AttachmentDiscovery().discover(message)

    assert len(attachments) == 0


def test_email_with_single_attachment():

    message = EmailMessage()

    message.set_content("Email body")

    message.add_attachment(
        b"PDF DATA",
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert len(attachments) == 1


def test_email_with_multiple_attachments():

    message = EmailMessage()

    message.set_content("Email body")

    message.add_attachment(
        b"PDF DATA",
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    message.add_attachment(
        b"IMAGE DATA",
        maintype="image",
        subtype="png",
        filename="photo.png",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert len(attachments) == 2