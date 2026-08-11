from app.case_report.case_report import CaseReport
from app.case_report.evidence_statistics_calculator import (
    EvidenceStatisticsCalculator,
)


class CaseReportBuilder:

    def build(self, *sections, evidence=None):
        report = CaseReport()

        for section in sections:
            if section is not None:
                report.add_section(section)

            # Future support for statistics
            if evidence is not None:

                calculator = EvidenceStatisticsCalculator()

                statistics = calculator.calculate(evidence)

                for section in report.sections():

                    if hasattr(section, "statistics"):
                        section.statistics = statistics

        return report
