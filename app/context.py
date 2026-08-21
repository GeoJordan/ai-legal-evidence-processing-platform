from dataclasses import dataclass, field

from app.configuration import Configuration

from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage
from app.models.attachment import Attachment
from typing import Optional
from app.models import FileRecord


@dataclass
class EvidenceContext:
    """
    Shared processing context for one workflow execution.
    """

    configuration: Configuration | None = None

    source_path: str = ""

    files: list[FileRecord] = field(default_factory=list)

    message_count: int = 0

    headers: list[EmailHeader] = field(default_factory=list)

    messages: list[EmailMessage] = field(default_factory=list)

    attachments: list[Attachment] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    statistics: dict[str, int] = field(default_factory=dict)