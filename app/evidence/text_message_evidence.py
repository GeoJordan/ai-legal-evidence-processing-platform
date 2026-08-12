from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class TextMessageEvidence(EvidenceItem):

    def __init__(
        self,
        sender="",
        recipient="",
        message="",
        sent_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.TEXT_MESSAGE,
            source="text_message",
            collected_at=sent_at,
        )

        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.sent_at = sent_at

    @property
    def title(self):
        if self.message:
            return self.message[:50]
        return "Text Message"