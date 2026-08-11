from app.case_report.evidence_statistics import EvidenceStatistics


class EvidenceStatisticsCalculator:

    def calculate(self, evidence):

        return EvidenceStatistics(
            {
                "Evidence Items": len(evidence)
            }
        )