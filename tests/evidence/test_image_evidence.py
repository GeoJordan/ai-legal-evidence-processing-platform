from app.evidence.image_evidence import ImageEvidence
from app.evidence.evidence_type import EvidenceType


def test_image_evidence_stores_fields():
    image = ImageEvidence(
        filename="photo.jpg",
        width=1920,
        height=1080,
        path="/images/photo.jpg",
    )

    assert image.filename == "photo.jpg"
    assert image.width == 1920
    assert image.height == 1080
    assert image.path == "/images/photo.jpg"


def test_image_evidence_title_returns_filename():
    image = ImageEvidence(
        filename="exchange_photo.jpg"
    )

    assert image.title == "exchange_photo.jpg"


def test_image_evidence_inherits_common_properties():
    image = ImageEvidence()

    assert image.evidence_type == EvidenceType.IMAGE
    assert image.source == "image"
    assert image.collected_at is not None


def test_image_evidence_default_dimensions_are_zero():
    image = ImageEvidence()

    assert image.width == 0
    assert image.height == 0