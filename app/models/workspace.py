"""
Workspace domain model.

Represents the top-level organizational boundary within the
AI Legal Evidence Processing Platform.
"""


class Workspace:
    """
    Represents a collection of one or more legal cases.
    """

    def __init__(self, name):
        self.name = name

        self.cases = []

    def add_case(self, case):
        self.cases.append(case)
