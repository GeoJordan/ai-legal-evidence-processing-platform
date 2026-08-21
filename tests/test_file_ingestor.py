from pathlib import Path

from app.ingestors.base import BaseIngestor
from app.scanner import scan_file
from app.ingestors.email.file_ingestor import FileIngestor
from app.context import EvidenceContext




def test_file_ingestor_can_be_created():

    ingestor = FileIngestor()

    assert ingestor.name == "File Ingestor"

def test_file_ingestor_supports_pdf():

    ingestor = FileIngestor()

    assert ingestor.supports("document.pdf")

def test_file_ingestor_rejects_unknown_extension():

    ingestor = FileIngestor()

    assert not ingestor.supports("archive.xyz")

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

def test_file_ingestor_ingests_supported_file(tmp_path):

    evidence_file = tmp_path / "sample.txt"
    evidence_file.write_text(
        "Synthetic evidence for EP-206C verification.",
        encoding="utf-8",
    )

    context = EvidenceContext()
    ingestor = FileIngestor()

    result = ingestor.ingest(evidence_file, context)

    assert result is context
    assert len(context.files) == 1

    record = context.files[0]

    assert record.filename == "sample.txt"
    assert record.extension == ".txt"
    assert record.size_bytes > 0
    assert record.sha256
    assert record.scan_status == "success"


def test_file_ingestor_warns_for_unsupported_file(tmp_path):

    unsupported_file = tmp_path / "sample.xyz"
    unsupported_file.write_text(
        "Synthetic unsupported evidence.",
        encoding="utf-8",
    )

    context = EvidenceContext()
    ingestor = FileIngestor()

    result = ingestor.ingest(unsupported_file, context)

    assert result is context
    assert len(context.files) == 0
    assert len(context.warnings) == 1
    assert "Unsupported file type" in context.warnings[0]
