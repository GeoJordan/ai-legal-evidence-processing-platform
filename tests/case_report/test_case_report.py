from app.case_report.case_report import CaseReport


def test_case_report_starts_empty():
    report = CaseReport()

    assert report.sections() == []

def test_case_report_adds_section():
    report = CaseReport()

    report.add_section("Executive Summary")

    assert report.sections() == ["Executive Summary"]

def test_case_report_preserves_section_order():
    report = CaseReport()

    report.add_section("Executive Summary")
    report.add_section("Timeline")
    report.add_section("Narrative")

    assert report.sections() == [
        "Executive Summary",
        "Timeline",
        "Narrative",
    ]

from app.case_report.executive_summary import ExecutiveSummary


def test_case_report_to_text():
    report = CaseReport()

    report.add_section(
        ExecutiveSummary(
            title="Executive Summary",
            overview="This report summarizes the evidence."
        )
    )

    assert report.to_text() == (
        "AI LEGAL EVIDENCE PROCESSING PLATFORM\n"
        "CASE REPORT\n\n"
        "Executive Summary\n"
        "This report summarizes the evidence."
    )