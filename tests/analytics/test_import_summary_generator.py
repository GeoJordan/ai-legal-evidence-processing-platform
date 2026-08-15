from app.analytics.import_summary_generator import ImportSummaryGenerator


def test_empty_summary():

    summary = ImportSummaryGenerator().generate([])

    assert summary.emails_processed == 0
    assert summary.attachments_discovered == 0
    assert summary.attachments_saved == 0
    assert summary.total_attachment_size == 0
    assert summary.mime_type_counts == {}

from app.models.attachment import Attachment


def test_attachment_count():

    attachments = [
        Attachment(
            filename="a.pdf",
            content_type="application/pdf",
            size=100,
            data=b"",
        ),
        Attachment(
            filename="b.png",
            content_type="image/png",
            size=200,
            data=b"",
        ),
    ]

    summary = ImportSummaryGenerator().generate(attachments)

    assert summary.attachments_discovered == 2

from app.models.attachment import Attachment


def test_total_attachment_size():

    attachments = [
        Attachment(
            filename="contract.pdf",
            content_type="application/pdf",
            size=125,
            data=b"",
        ),
        Attachment(
            filename="photo.png",
            content_type="image/png",
            size=375,
            data=b"",
        ),
    ]

    summary = ImportSummaryGenerator().generate(attachments)

    assert summary.total_attachment_size == 500

from app.models.attachment import Attachment


def test_mime_type_counts():

    attachments = [
        Attachment(
            filename="contract1.pdf",
            content_type="application/pdf",
            size=100,
            data=b"",
        ),
        Attachment(
            filename="contract2.pdf",
            content_type="application/pdf",
            size=200,
            data=b"",
        ),
        Attachment(
            filename="photo.png",
            content_type="image/png",
            size=300,
            data=b"",
        ),
    ]

    summary = ImportSummaryGenerator().generate(attachments)

    assert summary.mime_type_counts == {
        "application/pdf": 2,
        "image/png": 1,
    }

from app.models.attachment import Attachment


def test_attachments_saved():

    attachments = [
        Attachment(
            filename="one.pdf",
            content_type="application/pdf",
            size=100,
            data=b"",
        ),
        Attachment(
            filename="two.pdf",
            content_type="application/pdf",
            size=100,
            data=b"",
        ),
    ]

    summary = ImportSummaryGenerator().generate(attachments)

    assert summary.attachments_saved == 2