from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class WhatsAppEvidence(EvidenceItem):

    def __init__(
        self,
        sender="",
        chat_name="",
        message="",
        participants=None,
        sent_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.WHATSAPP,
            source="whatsapp",
            collected_at=sent_at,
        )

        self.sender = sender
        self.chat_name = chat_name
        self.message = message
        self.participants = participants or []
        self.sent_at = sent_at

    @property
    def title(self):
        if self.message:
            return self.message[:50]
        return "WhatsApp Message"