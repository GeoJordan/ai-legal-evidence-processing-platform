"""
Allegation domain model.
"""

class Allegation:

    def __init__(self, allegation_id, title):
        self.allegation_id = allegation_id
        self.title = title
        self.evidence = []

    def add_evidence(self, evidence):
        self.evidence.append(evidence)
