from dataclasses import dataclass, field

from app.models.attachment import Attachment
from app.models.email_header import EmailHeader


@dataclass
class EmailMessage:
    """
    Represents a complete email message.
    """

    header: EmailHeader
    body: str
    is_html: bool = False
    attachments: list[Attachment] = field(default_factory=list)