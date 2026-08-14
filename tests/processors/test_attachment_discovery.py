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

def test_attachment_filename():

    message = EmailMessage()

    message.set_content("Body")

    message.add_attachment(
        b"PDF",
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].filename == "contract.pdf"

def test_missing_filename_returns_empty_string():

    message = EmailMessage()

    message.set_content("Body")

    message.add_attachment(
        b"PDF",
        maintype="application",
        subtype="pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].filename == ""

def test_unicode_filename():

    message = EmailMessage()

    message.set_content("Body")

    message.add_attachment(
        b"PDF",
        maintype="application",
        subtype="pdf",
        filename="Résumé.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].filename == "Résumé.pdf"

def test_multiple_filenames_preserved():

    message = EmailMessage()

    message.set_content("Body")

    message.add_attachment(
        b"A",
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    message.add_attachment(
        b"B",
        maintype="image",
        subtype="png",
        filename="photo.png",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].filename == "contract.pdf"
    assert attachments[1].filename == "photo.png"

def test_pdf_content_type():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"PDF",
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].content_type == "application/pdf"

def test_png_content_type():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"IMG",
        maintype="image",
        subtype="png",
        filename="photo.png",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].content_type == "image/png"

def test_zip_content_type():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"ZIP",
        maintype="application",
        subtype="zip",
        filename="archive.zip",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].content_type == "application/zip"

def test_multiple_content_types():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"PDF",
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    message.add_attachment(
        b"PNG",
        maintype="image",
        subtype="png",
        filename="photo.png",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].content_type == "application/pdf"
    assert attachments[1].content_type == "image/png"

