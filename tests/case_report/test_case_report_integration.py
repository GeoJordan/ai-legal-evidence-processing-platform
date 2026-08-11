from app.case_report.case_report_builder import CaseReportBuilder
from app.case_report.executive_summary import ExecutiveSummary


def test_build_complete_case_report():

    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="This report summarizes the evidence."
    )

    builder = CaseReportBuilder()

    report = builder.build(summary)

    assert report.to_text() == (
        "AI LEGAL EVIDENCE PROCESSING PLATFORM\n"
        "CASE REPORT\n\n"
        "Executive Summary\n"
        "This report summarizes the evidence."
    )