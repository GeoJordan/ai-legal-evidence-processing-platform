import mailbox
from email.message import EmailMessage as RawEmailMessage

from app.context import EvidenceContext
from app.ingestors.email.email_ingestor import EmailIngestor
from app.ingestors.email.mbox_reader import MboxReader


def test_mbox_reader_and_email_ingestor_populate_context(tmp_path):

    mbox_path = tmp_path / "synthetic.mbox"

    # ---------------------------------------------------------
    # 1. Build synthetic MBOX
    # ---------------------------------------------------------

    mbox = mailbox.mbox(str(mbox_path))

    first = RawEmailMessage()
    first["Message-ID"] = "<synthetic-mbox-001@example.com>"
    first["From"] = "alice@example.com"
    first["To"] = "bob@example.com"
    first["Subject"] = "Synthetic Passport Message One"
    first.set_content("First synthetic evidence message.")

    second = RawEmailMessage()
    second["Message-ID"] = "<synthetic-mbox-002@example.com>"
    second["From"] = "bob@example.com"
    second["To"] = "alice@example.com"
    second["Subject"] = "Synthetic Passport Message Two"
    second.set_content("Second synthetic evidence message.")

    mbox.add(first)
    mbox.add(second)
    mbox.flush()
    mbox.close()

    # ---------------------------------------------------------
    # 2. Read + normalize
    # ---------------------------------------------------------

    reader = MboxReader(mbox_path)
    ingestor = EmailIngestor()
    context = EvidenceContext()

    for raw_message in reader.read():
        ingestor.ingest(
            raw_message,
            context,
        )

    # ---------------------------------------------------------
    # 3. Verify normalized evidence context
    # ---------------------------------------------------------

    assert context.message_count == 2
    assert len(context.headers) == 2
    assert len(context.messages) == 2

    assert (
        context.headers[0].message_id
        == "<synthetic-mbox-001@example.com>"
    )

    assert (
        context.headers[1].message_id
        == "<synthetic-mbox-002@example.com>"
    )

    assert (
        context.messages[0].header.subject
        == "Synthetic Passport Message One"
    )

    assert (
        context.messages[1].header.subject
        == "Synthetic Passport Message Two"
    )

    assert "First synthetic evidence message." in context.messages[0].body
    assert "Second synthetic evidence message." in context.messages[1].body