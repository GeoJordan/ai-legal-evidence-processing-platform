from app.case_management.evidence_selection import EvidenceSelection
from app.models.case import Case
from app.models.allegation import Allegation
from app.models.evidence import Evidence


def test_select_evidence_for_allegation():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    allegation = Allegation(
        allegation_id="ALG-001",
        title="Passport Withheld"
    )

    evidence = Evidence(
        evidence_id="EV-001",
        title="Passport Email"
    )

    allegation.add_evidence(evidence)
    case.add_allegation(allegation)

    selector = EvidenceSelection()

    selected = selector.select(case, allegation)

    assert len(selected) == 1