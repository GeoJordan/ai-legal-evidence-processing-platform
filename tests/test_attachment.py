from app.models.attachment import Attachment


def test_attachment_can_be_created():

    attachment = Attachment(
        filename="contract.pdf",
        content_type="application/pdf",
        size=1024,
        data=b"PDFDATA"
    )

    assert attachment.filename == "contract.pdf"
    assert attachment.content_type == "application/pdf"
    assert attachment.size == 1024
    assert attachment.data == b"PDFDATA"