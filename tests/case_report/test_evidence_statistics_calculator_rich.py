from app.case_report.evidence_statistics_calculator import (
    EvidenceStatisticsCalculator,
)


def test_calculator_counts_multiple_types():

    evidence = [
        {"type": "email"},
        {"type": "email"},
        {"type": "pdf"},
        {"type": "image"},
        {"type": "image"},
    ]

    stats = EvidenceStatisticsCalculator().calculate(evidence)

    assert stats.get("Evidence Items") == 5
    assert stats.get("Emails") == 2
    assert stats.get("PDF Documents") == 1
    assert stats.get("Images") == 2


def test_calculator_handles_empty_list():

    stats = EvidenceStatisticsCalculator().calculate([])

    assert stats.get("Evidence Items") == 0
    assert stats.get("Emails") == 0
    assert stats.get("PDF Documents") == 0
    assert stats.get("Images") == 0


def test_calculator_handles_unknown_type():

    evidence = [
        {"type": "spreadsheet"},
    ]

    stats = EvidenceStatisticsCalculator().calculate(evidence)

    assert stats.get("Evidence Items") == 1
    assert stats.get("Emails") == 0
    assert stats.get("PDF Documents") == 0
    assert stats.get("Images") == 0


def test_calculator_handles_missing_type():

    evidence = [
        {},
    ]

    stats = EvidenceStatisticsCalculator().calculate(evidence)

    assert stats.get("Evidence Items") == 1