from app.case_report.evidence_statistics import EvidenceStatistics


class EvidenceStatisticsCalculator:

    def calculate(self, evidence):

        statistics = {
            "Evidence Items": len(evidence),
            "Emails": 0,
            "PDF Documents": 0,
            "Images": 0,
        }

        for item in evidence:

            evidence_type = item.get("type")

            if evidence_type == "email":
                statistics["Emails"] += 1

            elif evidence_type == "pdf":
                statistics["PDF Documents"] += 1

            elif evidence_type == "image":
                statistics["Images"] += 1

        return EvidenceStatistics(statistics)