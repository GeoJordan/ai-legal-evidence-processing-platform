from dataclasses import dataclass, field

from app.configuration import Configuration
from app.models import FileRecord


@dataclass
class EvidenceContext:
    """
    Shared processing context for one workflow execution.
    """

    configuration: Configuration

    file_records: list[FileRecord] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    statistics: dict[str, int] = field(default_factory=dict)