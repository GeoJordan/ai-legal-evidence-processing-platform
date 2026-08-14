from dataclasses import dataclass, field
from pathlib import Path

from app.models.attachment import Attachment
from app.models.email_header import EmailHeader


@dataclass
class EmailMessage:

    header: EmailHeader

    body: str = ""

    is_html: bool = False

    attachments: list[Attachment] = field(default_factory=list)

    source_path: Path | None = None

