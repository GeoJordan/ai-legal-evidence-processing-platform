from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


def test_evidence_item_stores_common_properties():

    item = EvidenceItem(
        evidence_type=EvidenceType.EMAIL,
        source="email",
    )

    assert item.evidence_type == EvidenceType.EMAIL
    assert item.source == "email"
    assert item.collected_at is not None

from datetime import datetime

from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


def test_evidence_item_preserves_custom_timestamp():

    timestamp = datetime(2026, 8, 12, 9, 30)

    item = EvidenceItem(
        evidence_type=EvidenceType.EMAIL,
        source="email",
        collected_at=timestamp,
    )

    assert item.collected_at == timestamp


def test_evidence_item_default_title_is_empty():

    item = EvidenceItem(
        evidence_type=EvidenceType.PDF,
        source="pdf",
    )

    assert item.title == ""


def test_evidence_item_source_is_stored():

    item = EvidenceItem(
        evidence_type=EvidenceType.IMAGE,
        source="camera",
    )

    assert item.source == "camera"