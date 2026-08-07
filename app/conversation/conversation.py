from dataclasses import dataclass, field


@dataclass
class Conversation:
    """
    Represents a single email conversation.
    """

    subject: str = ""

    messages: list = field(default_factory=list)

    participants: set[str] = field(default_factory=set)