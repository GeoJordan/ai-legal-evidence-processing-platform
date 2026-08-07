from dataclasses import dataclass, field
from datetime import date


@dataclass
class Conversation:
    """
    Represents a single email conversation.
    """

    subject: str = ""

    messages: list = field(default_factory=list)

    participants: set[str] = field(default_factory=set)

    start_date: date | None = None

    end_date: date | None = None

    @property
    def message_count(self) -> int:
        return len(self.messages)