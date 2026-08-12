from app.case_report.case_report_builder import CaseReportBuilder


def test_builder_creates_empty_case_report():
    builder = CaseReportBuilder()

    report = builder.build()

    assert report.sections() == []

from app.case_report.executive_summary import ExecutiveSummary


def test_builder_adds_executive_summary():
    builder = CaseReportBuilder()

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="This report summarizes the evidence."
    )

    report = builder.build(summary)

    assert len(report.sections()) == 1
    assert report.sections()[0] == summary

from app.narrative.narrative import Narrative


def test_builder_adds_multiple_sections():
    builder = CaseReportBuilder()

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="Overview"
    )

    narrative = Narrative()

    report = builder.build(summary, narrative)

    assert report.sections() == [
        summary,
        narrative,
    ]

from app.narrative.narrative import Narrative


def test_builder_adds_multiple_sections():
    builder = CaseReportBuilder()

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="Overview"
    )

    narrative = Narrative()

    report = builder.build(summary, narrative)

    assert report.sections() == [
        summary,
        narrative,
    ]

from app.evidence.email_evidence import EmailEvidence


def test_builder_populates_statistics():

    builder = CaseReportBuilder()

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="Overview",
    )

    report = builder.build(
        summary,
        evidence=[
            EmailEvidence(),
        ],
    )

    assert report.sections()[0].statistics is not None