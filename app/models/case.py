class Case:

    def __init__(self, case_id, name):
        self.case_id = case_id
        self.name = name

        self.allegations = []
        self.evidence = []

    def add_allegation(self, allegation):
        self.allegations.append(allegation)

    def add_evidence(self, evidence):
        self.evidence.append(evidence)
