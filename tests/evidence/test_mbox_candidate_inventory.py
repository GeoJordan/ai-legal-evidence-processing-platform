import mailbox
from email.message import EmailMessage

from app.evidence.correspondent_selector import CorrespondentSelector
from app.evidence.date_selector import DateSelector
from app.evidence.mbox_candidate_inventory import MboxCandidateInventory


def test_inventory_counts_only_matching_correspondence(tmp_path):

    mbox_path = tmp_path / "synthetic_inventory.mbox"
    mbox = mailbox.mbox(str(mbox_path))

    # Match: target is sender, after start date
    message_1 = EmailMessage()
    message_1["Message-ID"] = "<match-001@example.com>"
    message_1["From"] = "person@example.com"
    message_1["To"] = "me@example.com"
    message_1["Date"] = "Thu, 20 Aug 2026 10:00:00 -0400"
    message_1["Subject"] = "Matching incoming message"
    message_1.set_content("Synthetic evidence.")
    mbox.add(message_1)

    # Match: target is recipient, after start date
    message_2 = EmailMessage()
    message_2["Message-ID"] = "<match-002@example.com>"
    message_2["From"] = "me@example.com"
    message_2["To"] = "person@example.com"
    message_2["Date"] = "Wed, 10 Jan 2024 10:00:00 -0500"
    message_2["Subject"] = "Matching outgoing message"
    message_2.set_content("Synthetic evidence.")
    mbox.add(message_2)

    # Reject: correct correspondent but too old
    message_3 = EmailMessage()
    message_3["Message-ID"] = "<old-001@example.com>"
    message_3["From"] = "person@example.com"
    message_3["To"] = "me@example.com"
    message_3["Date"] = "Fri, 31 Dec 2021 10:00:00 -0500"
    message_3["Subject"] = "Old message"
    message_3.set_content("Synthetic evidence.")
    mbox.add(message_3)

    # Reject: correct date but unrelated correspondent
    message_4 = EmailMessage()
    message_4["Message-ID"] = "<unrelated-001@example.com>"
    message_4["From"] = "someone@example.com"
    message_4["To"] = "me@example.com"
    message_4["Date"] = "Thu, 20 Aug 2026 11:00:00 -0400"
    message_4["Subject"] = "Unrelated message"
    message_4.set_content("Synthetic evidence.")
    mbox.add(message_4)

    mbox.flush()
    mbox.close()

    correspondent_selector = CorrespondentSelector(
        "person@example.com"
    )

    date_selector = DateSelector(
        start_date="2022-01-01"
    )

    inventory = MboxCandidateInventory(
        correspondent_selector=correspondent_selector,
        date_selector=date_selector,
    )

    result = inventory.scan(mbox_path)

    assert result["total_messages"] == 4
    assert result["candidate_messages"] == 2