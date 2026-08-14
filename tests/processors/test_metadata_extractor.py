from email.message import EmailMessage

from app.processors.metadata_extractor import MetadataExtractor


def test_extract_message_id():
    message = EmailMessage()
    message["Message-ID"] = "<123@example.com>"

    header = MetadataExtractor().extract(message)

    assert header.message_id == "<123@example.com>"


def test_extract_subject():
    message = EmailMessage()
    message["Subject"] = "Discovery Documents"

    header = MetadataExtractor().extract(message)

    assert header.subject == "Discovery Documents"


def test_extract_sender():
    message = EmailMessage()
    message["From"] = "alice@example.com"

    header = MetadataExtractor().extract(message)

    assert header.sender == "alice@example.com"


def test_missing_subject_defaults_to_empty():
    message = EmailMessage()

    header = MetadataExtractor().extract(message)

    assert header.subject == ""

def test_extract_to_recipients():

    message = EmailMessage()
    message["To"] = "alice@example.com, bob@example.com"

    header = MetadataExtractor().extract(message)

    assert header.to == [
    "alice@example.com",
        "bob@example.com",
    ]


def test_extract_cc():

    message = EmailMessage()
    message["CC"] = "manager@example.com"

    header = MetadataExtractor().extract(message)

    assert header.cc == [
        "manager@example.com"
    ]


def test_extract_empty_cc():

    message = EmailMessage()

    header = MetadataExtractor().extract(message)

    assert header.cc == []

from datetime import datetime


def test_extract_sent_date():

    message = EmailMessage()
    message["Date"] = "Tue, 11 Aug 2026 09:42:15 -0400"

    header = MetadataExtractor().extract(message)

    assert isinstance(header.sent_at, datetime)

def test_missing_date_returns_none():

    message = EmailMessage()

    header = MetadataExtractor().extract(message)

    assert header.sent_at is None

def test_timezone_is_preserved():

    message = EmailMessage()
    message["Date"] = "Tue, 11 Aug 2026 09:42:15 -0400"

    header = MetadataExtractor().extract(message)

    assert header.sent_at.utcoffset().total_seconds() == -4 * 3600

def test_invalid_date_returns_none():

    message = EmailMessage()
    message["Date"] = "Not a real date"

    header = MetadataExtractor().extract(message)

    assert header.sent_at is None

def test_extract_in_reply_to():

    message = EmailMessage()
    message["In-Reply-To"] = "<parent@example.com>"

    header = MetadataExtractor().extract(message)

    assert header.in_reply_to == "<parent@example.com>"

def test_missing_in_reply_to_returns_none():

    message = EmailMessage()

    header = MetadataExtractor().extract(message)

    assert header.in_reply_to is None

def test_extract_references():

    message = EmailMessage()

    message["References"] = (
        "<001@example.com> "
        "<002@example.com> "
        "<003@example.com>"
    )

    header = MetadataExtractor().extract(message)

    assert header.references == [
        "<001@example.com>",
        "<002@example.com>",
        "<003@example.com>",
    ]

def test_missing_references_returns_empty_list():

    message = EmailMessage()

    header = MetadataExtractor().extract(message)

    assert header.references == []

def _parse_references(self, value: str) -> list[str]:
    """
    Convert the RFC-822 References header into a list of Message-IDs.
    """
    if not value:
        return []

    return value.split()

def test_extract_bcc():

    message = EmailMessage()
    message["Bcc"] = "legal@example.com, archive@example.com"

    header = MetadataExtractor().extract(message)

    assert header.bcc == [
        "legal@example.com",
        "archive@example.com",
    ]

def test_missing_bcc_returns_empty_list():

    message = EmailMessage()

    header = MetadataExtractor().extract(message)

    assert header.bcc == []