from dataclasses import dataclass


@dataclass
class Attachment:
    """
    Represents an email attachment.
    """

    filename: str
    content_type: str
    size: int
    data: bytes