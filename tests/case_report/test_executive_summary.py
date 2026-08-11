from app.case_report.executive_summary import ExecutiveSummary


def test_executive_summary_starts_empty():
    summary = ExecutiveSummary()

    assert summary.title == ""
    assert summary.overview == ""

def test_executive_summary_stores_values():
    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="This report summarizes the evidence."
    )

    assert summary.title == "Executive Summary"
    assert summary.overview == "This report summarizes the evidence."

def test_executive_summary_stores_statistics():
    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="Summary",
        statistics={
            "Evidence Items": 12,
            "Timeline Events": 8,
        }
    )

    assert summary.statistics == {
        "Evidence Items": 12,
        "Timeline Events": 8,
    }

def test_executive_summary_to_text():
    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="This report summarizes the evidence."
    )

    assert summary.to_text() == (
        "Executive Summary\n"
        "This report summarizes the evidence."
    )

def test_executive_summary_renders_statistics():
    summary = ExecutiveSummary(
        title="Executive Summary",
        overview="This report summarizes the evidence.",
        statistics={
            "Evidence Items": 12,
            "Timeline Events": 8,
        }
    )

    assert summary.to_text() == (
        "Executive Summary\n"
        "This report summarizes the evidence.\n\n"
        "Statistics\n"
        "----------\n"
        "Evidence Items: 12\n"
        "Timeline Events: 8"
    )