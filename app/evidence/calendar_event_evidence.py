from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class CalendarEventEvidence(EvidenceItem):

    def __init__(
        self,
        title="",
        location="",
        start_time=None,
        end_time=None,
        description="",
    ):

        super().__init__(
            evidence_type=EvidenceType.CALENDAR_EVENT,
            source="calendar",
            collected_at=start_time,
        )

        self._title = title
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    @property
    def title(self):
        return self._title