from app.evidence.attachment_evidence import AttachmentEvidence
from app.evidence.evidence_item import EvidenceItem


# ----------------------------------------------------
# stores fields
# ----------------------------------------------------
def test_attachment_evidence_stores_fields():

    attachment = AttachmentEvidence(
        filename="passport.pdf",
        content_type="application/pdf",
        size_bytes=24576,
        sha256="abc123",
        source_path="/evidence/passport.pdf",
    )

    assert attachment.filename == "passport.pdf"
    assert attachment.content_type == "application/pdf"
    assert attachment.size_bytes == 24576
    assert attachment.sha256 == "abc123"
    assert attachment.source_path == "/evidence/passport.pdf"


# ----------------------------------------------------
# title
# ----------------------------------------------------
def test_attachment_title_returns_filename():

    attachment = AttachmentEvidence(
        filename="photo.jpg"
    )

    assert attachment.title == "photo.jpg"


# ----------------------------------------------------
# inheritance
# ----------------------------------------------------
def test_attachment_inherits_common_properties():

    attachment = AttachmentEvidence()

    assert isinstance(attachment, EvidenceItem)


# ----------------------------------------------------
# defaults
# ----------------------------------------------------
def test_attachment_defaults_are_empty():

    attachment = AttachmentEvidence()

    assert attachment.filename == ""
    assert attachment.content_type == ""
    assert attachment.size_bytes == 0
    assert attachment.sha256 == ""
    assert attachment.source_path == ""
    assert attachment.title == ""