from app.case_management.evidence_gap import EvidenceGapAnalysis
from app.models.case import Case
from app.models.allegation import Allegation


def test_detect_missing_evidence():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    allegation = Allegation(
        allegation_id="ALG-001",
        title="Passport Withheld"
    )

    case.add_allegation(allegation)

    analyzer = EvidenceGapAnalysis()

    gaps = analyzer.find(case)

    assert len(gaps) == 1