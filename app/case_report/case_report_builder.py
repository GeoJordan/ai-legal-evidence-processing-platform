from app.case_report.case_report import CaseReport


class CaseReportBuilder:

    def build(self, *sections):
        report = CaseReport()

        for section in sections:
            if section is not None:
                report.add_section(section)

        return report
