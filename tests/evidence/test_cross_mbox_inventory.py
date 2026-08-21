import mailbox
from email.message import EmailMessage

from app.evidence.correspondent_selector import CorrespondentSelector
from app.evidence.date_selector import DateSelector
from app.evidence.cross_mbox_inventory import CrossMboxInventory


def _write_message(
    mbox_path,
    *,
    message_id,
    sender,
    recipient,
    date,
    subject,
):
    message = EmailMessage()

    message["Message-ID"] = message_id
    message["From"] = sender
    message["To"] = recipient
    message["Date"] = date
    message["Subject"] = subject

    message.set_content("Synthetic test evidence.")

    mbox = mailbox.mbox(str(mbox_path), create=True)

    try:
        mbox.add(message)
        mbox.flush()
    finally:
        mbox.close()


def test_cross_mbox_inventory_deduplicates_same_message_id(tmp_path):

    inbox_path = tmp_path / "Inbox.mbox"
    sent_path = tmp_path / "Sent.mbox"

    # Same logical email deliberately appears in both MBOX sources.
    for path in (inbox_path, sent_path):
        _write_message(
            path,
            message_id="<duplicate-001@example.com>",
            sender="person@example.com",
            recipient="me@example.com",
            date="Thu, 20 Aug 2026 14:30:00 -0400",
            subject="Synthetic Duplicate Message",
        )

    correspondent_selector = CorrespondentSelector(
        "person@example.com"
    )

    date_selector = DateSelector(
        start_date="2022-01-01"
    )

    inventory = CrossMboxInventory(
        correspondent_selector=correspondent_selector,
        date_selector=date_selector,
    )

    result = inventory.scan(
        [
            inbox_path,
            sent_path,
        ]
    )

    assert result["total_messages"] == 2
    assert result["candidate_occurrences"] == 2

    # Same Message-ID across two MBOX files must count only once.
    assert result["unique_candidate_messages"] == 1
    assert result["duplicate_occurrences"] == 1

    assert result["missing_message_id"] == 0