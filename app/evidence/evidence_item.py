from datetime import datetime

from app.evidence.evidence_type import EvidenceType


class EvidenceItem:

    def __init__(
        self,
        evidence_type: EvidenceType,
        source="",
        collected_at=None,
    ):

        self.evidence_type = evidence_type
        self.source = source
        self.collected_at = collected_at or datetime.now()

    @property
    def title(self):
        """
        Default title for evidence.

        Specialized evidence classes override this property.
        """
        return ""