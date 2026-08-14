from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class EmailHeader:
    """
    Normalized RFC-822 email header.

    This object contains only metadata describing
    an email message.
    """

    message_id: str

    sender: str

    to: list[str] = field(default_factory=list)

    cc: list[str] = field(default_factory=list)

    bcc: list[str] = field(default_factory=list)

    subject: str = ""

    sent_at: datetime | None = None

    reply_to: str | None = None

    in_reply_to: str | None = None

    references: list[str] = field(default_factory=list)

    @property
    def has_references(self) -> bool:
        """Return True if this email references earlier messages."""
        return bool(self.references)
