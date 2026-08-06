from dataclasses import dataclass


@dataclass
class FileRecord:
    """
    Represents one physical evidence file discovered during scanning.
    """

    filename: str

    original_path: str

    extension: str

    size_bytes: int

    created_timestamp: str

    modified_timestamp: str

    sha256: str

    supported: bool

    scan_status: str

    scan_notes: str = ""