from app.case_report.report_section_formatter import ReportSectionFormatter

class ExecutiveSummary:

    def __init__(
        self,
        title="",
        overview="",
        statistics=None,
    ):
        self.title = title
        self.overview = overview
        self.statistics = statistics or {}

    def to_text(self):
        text = self.title

        if self.overview:
            text += "\n" + self.overview

        if self.statistics:
            text += "\n\nStatistics\n----------"

            for key, value in self.statistics.items():
                text += f"\n{key}: {value}"

        return text
