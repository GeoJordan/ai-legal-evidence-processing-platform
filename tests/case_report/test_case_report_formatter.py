from app.case_report.case_report import CaseReport
from app.case_report.case_report_formatter import CaseReportFormatter


def test_formatter_formats_empty_report():
    report = CaseReport()

    formatter = CaseReportFormatter()

    text = formatter.format(report)

    assert text == ""

from app.case_report.executive_summary import ExecutiveSummary


def test_formatter_formats_executive_summary():
    report = CaseReport()

    report.add_section(
        ExecutiveSummary(
            title="Executive Summary",
            overview="This report summarizes the evidence."
        )
    )

    formatter = CaseReportFormatter()

    text = formatter.format(report)

    assert text == (
        "AI LEGAL EVIDENCE PROCESSING PLATFORM\n"
        "CASE REPORT\n\n"
        "Executive Summary\n"
        "This report summarizes the evidence."
    )

from app.narrative.narrative import Narrative


def test_formatter_formats_multiple_sections():
    report = CaseReport()

    summary = ExecutiveSummary(
    title="Executive Summary",
    overview="This report summarizes the evidence."
    )

    narrative = Narrative()

    report.add_section(summary)
    report.add_section(narrative)

    formatter = CaseReportFormatter()

    text = formatter.format(report)

    assert text == (
        "AI LEGAL EVIDENCE PROCESSING PLATFORM\n"
        "CASE REPORT\n\n"
        "Executive Summary\n"
        "This report summarizes the evidence."
        "\n\n"
        "Narrative"
    )

def test_formatter_adds_report_header():
    report = CaseReport()

    report.add_section(
        ExecutiveSummary(
            "============================================================"
            "EXECUTIVE SUMMARY\n"
            "============================================================"
            "This report summarizes the evidence."
        )
    )

    text = CaseReportFormatter().format(report)

    assert text.startswith(
        "AI LEGAL EVIDENCE PROCESSING PLATFORM\n"
        "CASE REPORT\n"
    )

def test_formatter_formats_section_heading():
    report = CaseReport()

    report.add_section(
        ExecutiveSummary(
            title="Executive Summary",
            overview="Overview"
        )
    )

    text = CaseReportFormatter().format(report)

    assert "Executive Summary\nOverview" in text