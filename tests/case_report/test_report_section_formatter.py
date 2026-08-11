from app.case_report.report_section_formatter import ReportSectionFormatter


def test_formats_section_heading():
    formatter = ReportSectionFormatter()

    assert formatter.format_heading("Executive Summary") == (
        "============================================================\n"
        "EXECUTIVE SUMMARY\n"
        "============================================================"
    )