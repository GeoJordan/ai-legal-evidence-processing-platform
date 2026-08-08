from app.models.evidence import Evidence


def test_evidence_can_be_created():

    evidence = Evidence(
        evidence_id="EV-001",
        title="Passport Email"
    )

    assert evidence.evidence_id == "EV-001"
    assert evidence.title == "Passport Email"