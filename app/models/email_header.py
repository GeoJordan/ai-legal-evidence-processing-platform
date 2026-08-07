from dataclasses import dataclass


@dataclass
class EmailHeader:
    """
    Metadata describing a single email message.
    """

    sender: str
    recipient: str
    subject: str
    date: str
    message_id: str

    in_reply_to: str | None = None

    references: list[str] | None = None