from app.models.allegation import Allegation


def test_allegation_can_be_created():

    allegation = Allegation(
        allegation_id="ALG-001",
        title="Passport Withheld"
    )

    assert allegation.allegation_id == "ALG-001"
    assert allegation.title == "Passport Withheld"

from app.models.allegation import Allegation
from app.models.evidence import Evidence


def test_allegation_can_add_supporting_evidence():

    allegation = Allegation(
        allegation_id="ALG-001",
        title="Passport Withheld"
    )

    evidence = Evidence(
        evidence_id="EV-001",
        title="Passport Email"
    )

    allegation.add_evidence(evidence)

    assert len(allegation.evidence) == 1