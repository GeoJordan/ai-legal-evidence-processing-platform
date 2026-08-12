from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class ConversationEvidence(EvidenceItem):

    def __init__(
        self,
        conversation_id="",
        title="",
        participants=None,
        messages=None,
        started_at=None,
        ended_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.CONVERSATION,
            source="conversation",
            collected_at=started_at,
        )

        self.conversation_id = conversation_id
        self._title = title
        self.participants = participants or []
        self.messages = messages or []
        self.started_at = started_at
        self.ended_at = ended_at

    @property
    def title(self):
        return self._title

    def add(self, message):
        self.messages.append(message)

    def message_count(self):
        return len(self.messages)