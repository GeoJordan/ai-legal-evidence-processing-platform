from pathlib import Path

from app.ingestors.email.mbox_reader import MboxReader


def test_reader_stores_path():
    path = Path("sample.mbox")

    reader = MboxReader(path)

    assert reader.path == path


def test_reader_title_returns_filename():
    reader = MboxReader(Path("emails.mbox"))

    assert reader.title == "emails.mbox"


def test_reader_defaults_to_none_path():
    reader = MboxReader()

    assert reader.path is None


def test_reader_title_defaults_to_empty():
    reader = MboxReader()

    assert reader.title == ""

import pytest

from pathlib import Path

from app.ingestors.email.mbox_reader import MboxReader


def test_read_missing_file_raises_filenotfounderror():
    reader = MboxReader(Path("does_not_exist.mbox"))

    with pytest.raises(FileNotFoundError):
        list(reader.read())

def test_read_empty_mailbox():
    reader = MboxReader(
        Path("tests/fixtures/email/empty.mbox")
    )

    messages = list(reader.read())

    assert messages == []