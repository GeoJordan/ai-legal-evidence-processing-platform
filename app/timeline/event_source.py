"""
Event Source domain model.

Represents a piece of evidence supporting a timeline event.
"""


class EventSource:
    """Represents supporting evidence."""

    def __init__(
        self,
        evidence_id: str,
        source_type: str = "",
        reference: str = "",
    ):
        self.evidence_id = evidence_id
        self.source_type = source_type
        self.reference = reference