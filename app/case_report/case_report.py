from app.case_report.case_report_formatter import CaseReportFormatter

class CaseReport:

    def __init__(self):
        self._sections = []

    def sections(self):
        return self._sections

    def add_section(self, section):
        self._sections.append(section)

    def to_text(self):
        formatter = CaseReportFormatter()
        return formatter.format(self)