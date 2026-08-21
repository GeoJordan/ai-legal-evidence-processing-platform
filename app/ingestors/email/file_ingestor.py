"""
EP-206C File Ingestor

Concrete implementation of BaseIngestor for local evidence files.
"""

from pathlib import Path

from app.ingestors.base import BaseIngestor
from app.scanner import scan_file


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
        Ingest one local evidence file into the shared EvidenceContext.
        """

        file_path = Path(path)

        if not self.supports(file_path):
            context.warnings.append(
                f"Unsupported file type: {file_path}"
            )
            return context

        record = scan_file(file_path)
        context.files.append(record)

        return context
