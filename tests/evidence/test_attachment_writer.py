from pathlib import Path

from app.evidence.attachment_writer import AttachmentWriter
from app.models.attachment import Attachment


def test_attachment_writer_persists_attachment(tmp_path):

    attachment = Attachment(
        filename="sample.txt",
        content_type="text/plain",
        size=5,
        data=b"hello",
    )

    writer = AttachmentWriter()

    evidence = writer.write(
        attachment,
        tmp_path,
    )

    output_path = Path(evidence.source_path)

    assert output_path.exists()
    assert output_path.read_bytes() == b"hello"

    assert evidence.filename == "sample.txt"
    assert evidence.content_type == "text/plain"
    assert evidence.size_bytes == 5
    assert evidence.sha256
    assert evidence.title == "sample.txt"


def test_attachment_writer_creates_destination_directory(tmp_path):

    destination = tmp_path / "nested" / "attachments"

    attachment = Attachment(
        filename="sample.txt",
        content_type="text/plain",
        size=4,
        data=b"test",
    )

    writer = AttachmentWriter()

    evidence = writer.write(
        attachment,
        destination,
    )

    assert destination.exists()
    assert Path(evidence.source_path).exists()


def test_attachment_writer_rejects_missing_filename(tmp_path):

    attachment = Attachment(
        filename="",
        content_type="text/plain",
        size=4,
        data=b"test",
    )

    writer = AttachmentWriter()

    try:
        writer.write(
            attachment,
            tmp_path,
        )

        assert False, "Expected ValueError"

    except ValueError as error:

        assert "filename" in str(error).lower()

def test_attachment_writer_does_not_overwrite_existing_file(tmp_path):

    existing_file = tmp_path / "sample.txt"
    existing_file.write_bytes(b"original evidence")

    attachment = Attachment(
        filename="sample.txt",
        content_type="text/plain",
        size=12,
        data=b"new evidence",
    )

    writer = AttachmentWriter()

    try:
        writer.write(
            attachment,
            tmp_path,
        )

        assert False, "Expected FileExistsError"

    except FileExistsError:
        pass

    assert existing_file.read_bytes() == b"original evidence"

def test_attachment_writer_rejects_path_traversal(tmp_path):

    attachment = Attachment(
        filename="../outside.txt",
        content_type="text/plain",
        size=4,
        data=b"test",
    )

    writer = AttachmentWriter()

    try:
        writer.write(
            attachment,
            tmp_path,
        )

        assert False, "Expected ValueError"

    except ValueError as error:

        assert "filename" in str(error).lower()
        assert "path" in str(error).lower() or "traversal" in str(error).lower()

    assert not (tmp_path.parent / "outside.txt").exists()

def test_attachment_writer_rejects_windows_path_traversal(tmp_path):

    attachment = Attachment(
        filename=r"..\outside.txt",
        content_type="text/plain",
        size=4,
        data=b"test",
    )

    writer = AttachmentWriter()

    try:
        writer.write(
            attachment,
            tmp_path,
        )

        assert False, "Expected ValueError"

    except ValueError as error:

        assert "filename" in str(error).lower()

    assert not (tmp_path.parent / "outside.txt").exists()