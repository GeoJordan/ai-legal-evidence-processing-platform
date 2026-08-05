from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class FileRecord:
    """
    Metadata collected for one source file.

    The record is immutable so later modules cannot accidentally
    alter scanner results in place.
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

    def to_dict(self) -> dict[str, object]:
        """Return the record as a dictionary."""
        return asdict(self)
    