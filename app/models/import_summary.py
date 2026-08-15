from dataclasses import dataclass, field


@dataclass
class ImportSummary:
    """
    Aggregate statistics produced during an email import.
    """

    emails_processed: int = 0

    attachments_discovered: int = 0

    attachments_saved: int = 0

    total_attachment_size: int = 0

    mime_type_counts: dict[str, int] = field(default_factory=dict)