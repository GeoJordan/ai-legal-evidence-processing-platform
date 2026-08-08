from app.models.case import Case


def test_case_can_be_created():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    assert case.case_id == "CASE-001"
    assert case.name == "Custody Case"

from app.models.case import Case
from app.models.allegation import Allegation


def test_case_can_add_allegation():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    allegation = Allegation(
        allegation_id="ALG-001",
        title="Passport Withheld"
    )

    case.add_allegation(allegation)

    assert len(case.allegations) == 1

from app.models.case import Case
from app.models.evidence import Evidence


def test_case_can_add_evidence():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    evidence = Evidence(
        evidence_id="EV-001",
        title="Passport Email"
    )

    case.add_evidence(evidence)

    assert len(case.evidence) == 1