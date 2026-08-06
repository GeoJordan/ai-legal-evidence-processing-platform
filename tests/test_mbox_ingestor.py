from app.ingestors.mbox_ingestor import MboxIngestor


def test_mbox_ingestor_can_be_created():

    ingestor = MboxIngestor()

    assert ingestor.name == "MBOX Ingestor"

def test_mbox_ingestor_supports_mbox():

    ingestor = MboxIngestor()

    assert ingestor.supports("gmail_takeout.mbox")

def test_mbox_ingestor_rejects_pdf():

    ingestor = MboxIngestor()

    assert not ingestor.supports("evidence.pdf")

def test_mbox_ingestor_supports_uppercase_extension():

    ingestor = MboxIngestor()

    assert ingestor.supports("TAKEOUT.MBOX")

from pathlib import Path
import mailbox


def test_mbox_ingestor_can_open_mailbox(tmp_path):

    mailbox_path = tmp_path / "sample.mbox"

    mailbox_path.touch()

    ingestor = MboxIngestor()

    mbox = ingestor.open(mailbox_path)

    assert isinstance(mbox, mailbox.mbox)

import mailbox


def test_mbox_ingestor_counts_messages(tmp_path):

    mailbox_path = tmp_path / "sample.mbox"

    mbox = mailbox.mbox(mailbox_path)

    mbox.add(mailbox.mboxMessage("From: alice@example.com\n\nEmail One"))

    mbox.add(mailbox.mboxMessage("From: bob@example.com\n\nEmail Two"))

    mbox.flush()

    ingestor = MboxIngestor()

    assert ingestor.count_messages(mailbox_path) == 2

from app.models.email_header import EmailHeader
import mailbox


def test_mbox_ingestor_extracts_headers(tmp_path):

    mailbox_path = tmp_path / "sample.mbox"

    mbox = mailbox.mbox(mailbox_path)

    message = mailbox.mboxMessage()

    message["From"] = "alice@example.com"
    message["To"] = "bob@example.com"
    message["Subject"] = "Meeting Notes"
    message["Date"] = "Thu, 6 Aug 2026"
    message["Message-ID"] = "<123@example.com>"

    mbox.add(message)
    mbox.flush()

    ingestor = MboxIngestor()

    headers = ingestor.extract_headers(mailbox_path)

    assert len(headers) == 1
    assert isinstance(headers[0], EmailHeader)
    assert headers[0].sender == "alice@example.com"
    assert headers[0].recipient == "bob@example.com"
    assert headers[0].subject == "Meeting Notes"

from app.models.email_header import EmailHeader
import mailbox


def test_mbox_ingestor_extracts_headers(tmp_path):

    mailbox_path = tmp_path / "sample.mbox"

    mbox = mailbox.mbox(mailbox_path)

    message = mailbox.mboxMessage()
    message["From"] = "alice@example.com"
    message["To"] = "bob@example.com"
    message["Subject"] = "Meeting Notes"
    message["Date"] = "Thu, 6 Aug 2026"
    message["Message-ID"] = "<123@example.com>"

    mbox.add(message)
    mbox.flush()

    ingestor = MboxIngestor()

    headers = ingestor.extract_headers(mailbox_path)

    assert len(headers) == 1
    assert isinstance(headers[0], EmailHeader)
    assert headers[0].sender == "alice@example.com"
    assert headers[0].recipient == "bob@example.com"
    assert headers[0].subject == "Meeting Notes"

from app.models.email_message import EmailMessage


def test_mbox_ingestor_extracts_messages(tmp_path):

    mailbox_path = tmp_path / "sample.mbox"

    mbox = mailbox.mbox(mailbox_path)

    message = mailbox.mboxMessage()

    message["From"] = "alice@example.com"
    message["To"] = "bob@example.com"
    message["Subject"] = "Meeting"

    message.set_payload("This is the email body.")

    mbox.add(message)
    mbox.flush()

    ingestor = MboxIngestor()

    messages = ingestor.extract_messages(mailbox_path)

    assert len(messages) == 1
    assert isinstance(messages[0], EmailMessage)
    assert messages[0].body == "This is the email body."