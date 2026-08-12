from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class EmailEvidence(EvidenceItem):

    def __init__(
        self,
        sender="",
        recipients=None,
        subject="",
        body="",
        sent_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.EMAIL,
            source="email",
            collected_at=sent_at,
        )

        self.sender = sender
        self.recipients = recipients or []
        self.subject = subject
        self.body = body
        self.sent_at = sent_at

    @property
    def title(self):
        return self.subject