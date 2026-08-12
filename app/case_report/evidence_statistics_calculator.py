from app.case_report.evidence_statistics import EvidenceStatistics
from app.evidence.evidence_type import EvidenceType


class EvidenceStatisticsCalculator:

    def calculate(self, evidence):

        statistics = {
            "Evidence Items": len(evidence),
            "Emails": 0,
            "PDF Documents": 0,
            "Images": 0,
        }

        for item in evidence:

            evidence_type = item.evidence_type

            if evidence_type == EvidenceType.EMAIL:
                statistics["Emails"] += 1

            elif evidence_type == EvidenceType.PDF:
                statistics["PDF Documents"] += 1

            elif evidence_type == EvidenceType.IMAGE:
                statistics["Images"] += 1

        return EvidenceStatistics(statistics)