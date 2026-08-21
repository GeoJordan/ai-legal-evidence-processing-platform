from __future__ import annotations

import hashlib
from pathlib import Path

from app.evidence.attachment_evidence import AttachmentEvidence
from app.models.attachment import Attachment


class AttachmentWriter:
    """
    Persists an Attachment to the local file system and returns
    the corresponding AttachmentEvidence metadata object.
    """

    def write(
        self,
        attachment: Attachment,
        destination_directory: str | Path,
    ) -> AttachmentEvidence:

        destination = Path(destination_directory)
        destination.mkdir(parents=True, exist_ok=True)

        if not attachment.filename:
            raise ValueError("Attachment filename is required.")

        filename = Path(attachment.filename)

        if filename.name != attachment.filename or filename.is_absolute():
            raise ValueError(
                f"Attachment filename contains an invalid path: {attachment.filename}"
            )

        output_path = destination / filename.name

        if output_path.exists():
            raise FileExistsError(
                f"Evidence file already exists: {output_path}"
        )

        output_path.write_bytes(attachment.data)

        sha256 = hashlib.sha256(attachment.data).hexdigest()

        return AttachmentEvidence(
            filename=attachment.filename,
            content_type=attachment.content_type,
            size_bytes=len(attachment.data),
            sha256=sha256,
            source_path=str(output_path.resolve()),
        )