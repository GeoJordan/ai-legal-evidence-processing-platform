from app.case_report.evidence_statistics import EvidenceStatistics
from app.case_report.evidence_statistics_calculator import (
    EvidenceStatisticsCalculator,
)

from app.evidence.email_evidence import EmailEvidence
from app.evidence.pdf_evidence import PDFEvidence
from app.evidence.image_evidence import ImageEvidence


def test_calculator_returns_statistics_object():
    calculator = EvidenceStatisticsCalculator()

    stats = calculator.calculate([])

    assert isinstance(stats, EvidenceStatistics)


def test_calculator_counts_evidence_items():
    calculator = EvidenceStatisticsCalculator()

    evidence = [
    EmailEvidence(),
    PDFEvidence(),
    ImageEvidence(),
    ]

    stats = calculator.calculate(evidence)

    assert stats.get("Evidence Items") == 3


def test_calculator_handles_empty_list():
    calculator = EvidenceStatisticsCalculator()

    stats = calculator.calculate([])

    assert stats.get("Evidence Items") == 0


def test_calculator_preserves_statistics_type():
    calculator = EvidenceStatisticsCalculator()

    stats = calculator.calculate([EmailEvidence()])

    assert type(stats) is EvidenceStatistics