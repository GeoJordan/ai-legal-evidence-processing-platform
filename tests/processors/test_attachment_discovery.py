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

def test_attachment_size():

    message = EmailMessage()
    message.set_content("Body")

    payload = b"ABCDE"

    message.add_attachment(
        payload,
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].size == len(payload)

def test_zero_byte_attachment():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"",
        maintype="application",
        subtype="pdf",
        filename="empty.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].size == 0

def test_multiple_attachment_sizes():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"12345",
        maintype="application",
        subtype="pdf",
        filename="a.pdf",
    )

    message.add_attachment(
        b"123456789",
        maintype="image",
        subtype="png",
        filename="b.png",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].size == 5
    assert attachments[1].size == 9

def test_large_attachment_size():

    payload = b"x" * 100000

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        payload,
        maintype="application",
        subtype="zip",
        filename="archive.zip",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].size == 100000

def test_attachment_binary_data():

    payload = b"HELLO WORLD"

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        payload,
        maintype="application",
        subtype="pdf",
        filename="contract.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].data == payload

def test_empty_binary_attachment():

    message = EmailMessage()
    message.set_content("Body")

    message.add_attachment(
        b"",
        maintype="application",
        subtype="pdf",
        filename="empty.pdf",
    )

    attachments = AttachmentDiscovery().discover(message)

    assert attachments[0].data == b""


