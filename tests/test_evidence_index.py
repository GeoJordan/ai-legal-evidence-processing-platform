from app.evidence.evidence_index import EvidenceIndex


def test_evidence_index_can_be_created():

    index = EvidenceIndex()

    assert index is not None