from dataclasses import dataclass

from app.models.email_header import EmailHeader


@dataclass
class EmailMessage:
    """
    Represents a complete email.
    """

    header: EmailHeader
    body: str
    is_html: bool