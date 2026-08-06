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