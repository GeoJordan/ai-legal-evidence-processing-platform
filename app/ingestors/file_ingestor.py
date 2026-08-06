"""
EP-206C File Ingestor

Concrete implementation of BaseIngestor for local evidence files.
"""

from pathlib import Path

from app.ingestors.base import BaseIngestor


class FileIngestor(BaseIngestor):
    """
    Ingests evidence from the local file system.
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".txt",
        ".jpg",
        ".jpeg",
        ".png",
    }

    @property
    def name(self) -> str:
        return "File Ingestor"

    def supports(self, path) -> bool:
        """
        Return True if the file extension is supported.
        """
        return Path(path).suffix.lower() in self.SUPPORTED_EXTENSIONS

    def ingest(self, path, context):
        """
        Version 1 placeholder.

        Future versions will populate the EvidenceContext
        with file metadata and extracted evidence.
        """
        return context