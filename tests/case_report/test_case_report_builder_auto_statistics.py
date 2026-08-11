from app.case_report.case_report_builder import CaseReportBuilder
from app.case_report.executive_summary import ExecutiveSummary


def test_builder_populates_summary_statistics():

    summary = ExecutiveSummary(
        title="Executive Summary"
    )

    evidence = [
        object(),
        object(),
        object(),
    ]

    report = CaseReportBuilder().build(
        summary,
        evidence=evidence,
    )

    assert report.sections()[0].statistics is not None

def test_builder_counts_all_evidence():

    summary = ExecutiveSummary(title="Executive Summary")

    evidence = [object() for _ in range(17)]

    report = CaseReportBuilder().build(
        summary,
        evidence=evidence,
    )

    stats = report.sections()[0].statistics

    assert stats.get("Evidence Items") == 17

def test_builder_handles_empty_evidence():

    summary = ExecutiveSummary(title="Executive Summary")

    report = CaseReportBuilder().build(
        summary,
        evidence=[],
    )

    stats = report.sections()[0].statistics

    assert stats.get("Evidence Items") == 0

def test_builder_keeps_same_summary_instance():

    summary = ExecutiveSummary(title="Executive Summary")

    report = CaseReportBuilder().build(
        summary,
        evidence=[],
    )

    assert report.sections()[0] is summary