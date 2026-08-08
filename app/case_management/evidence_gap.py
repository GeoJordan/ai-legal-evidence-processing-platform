class EvidenceGapAnalysis:

    def find(self, case):

        gaps = []

        for allegation in case.allegations:
            if len(allegation.evidence) == 0:
                gaps.append(allegation)

        return gaps