"""
Event Source domain model.
"""

"""
Event Source domain model.

Represents a piece of evidence supporting a timeline event.
"""


class EventSource:
    """Represents supporting evidence."""

    def __init__(self, evidence_id: str):
        self.evidence_id = evidence_id

