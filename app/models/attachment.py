from dataclasses import dataclass

@dataclass
class Attachment:

    filename: str = ""
    content_type: str = ""
    size: int = 0
    data: bytes = b""

