from app.case_report.case_report_builder import CaseReportBuilder
from app.case_report.executive_summary import ExecutiveSummary


def test_builder_can_build_summary_with_statistics():

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="Overview",
    )

    builder = CaseReportBuilder()

    report = builder.build(
        summary,
        evidence=[object(), object(), object()]
    )

    assert (
        report.sections()[0].statistics.get("Evidence Items")
        == 3
    )


def test_builder_handles_empty_evidence():

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="Overview",
    )

    builder = CaseReportBuilder()

    report = builder.build(
        summary,
        evidence=[]
    )

    assert (
        report.sections()[0].statistics.get("Evidence Items")
        == 0
    )


def test_builder_returns_case_report():

    builder = CaseReportBuilder()

    report = builder.build(
        ExecutiveSummary(),
        evidence=[]
    )

    assert report.sections()


def test_builder_preserves_summary_title():

    summary = ExecutiveSummary(
        title="Executive Summary"
    )

    builder = CaseReportBuilder()

    report = builder.build(
        summary,
        evidence=[]
    )

    assert report.sections()[0].title == "Executive Summary"