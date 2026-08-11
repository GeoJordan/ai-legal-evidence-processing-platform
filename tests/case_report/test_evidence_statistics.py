from app.case_report.evidence_statistics import EvidenceStatistics


def test_statistics_starts_empty():
    stats = EvidenceStatistics()

    assert stats.values == {}


def test_statistics_stores_values():
    stats = EvidenceStatistics(
        {
            "Evidence Items": 12,
            "Timeline Events": 8,
        }
    )

    assert stats.values == {
        "Evidence Items": 12,
        "Timeline Events": 8,
    }


def test_statistics_returns_zero_for_missing_value():
    stats = EvidenceStatistics()

    assert stats.get("Documents") == 0


def test_statistics_returns_existing_value():
    stats = EvidenceStatistics(
        {
            "Emails": 15
        }
    )

    assert stats.get("Emails") == 15