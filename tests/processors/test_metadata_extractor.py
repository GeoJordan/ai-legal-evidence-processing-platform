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