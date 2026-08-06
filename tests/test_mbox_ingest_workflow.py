import mailbox

from app.context import EvidenceContext
from app.ingestors.mbox_ingestor import MboxIngestor


def test_ingest_populates_context(tmp_path):

    mailbox_path = tmp_path / "sample.mbox"

    mbox = mailbox.mbox(mailbox_path)

    message = mailbox.mboxMessage()

    message["From"] = "alice@example.com"
    message["To"] = "bob@example.com"
    message["Subject"] = "Test"

    message.set_payload("Hello")

    mbox.add(message)
    mbox.flush()

    context = EvidenceContext()

    ingestor = MboxIngestor()

    ingestor.ingest(mailbox_path, context)

    assert context.message_count == 1
    assert len(context.headers) == 1
    assert len(context.messages) == 1