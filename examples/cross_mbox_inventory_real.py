from pathlib import Path

from app.evidence.correspondent_selector import CorrespondentSelector
from app.evidence.date_selector import DateSelector
from app.evidence.cross_mbox_inventory import CrossMboxInventory


# ---------------------------------------------------------
# Real MBOX sources
# ---------------------------------------------------------

MBOX_PATHS = [
    Path(r"C:\PATH\TO\Inbox-003.mbox"),
    Path(r"C:\PATH\TO\Sent.mbox"),
    Path(r"C:\PATH\TO\Archived.mbox"),
]


# ---------------------------------------------------------
# Correspondent aliases
# ---------------------------------------------------------

TARGET_EMAILS = [
    "person.primary@example.com",
    "person.secondary@example.com",
]

START_DATE = "2022-01-01"


# ---------------------------------------------------------
# Build selectors
# ---------------------------------------------------------

correspondent_selector = CorrespondentSelector(
    TARGET_EMAILS
)

date_selector = DateSelector(
    start_date=START_DATE
)

inventory = CrossMboxInventory(
    correspondent_selector=correspondent_selector,
    date_selector=date_selector,
)


# ---------------------------------------------------------
# Read-only cross-MBOX inventory
# ---------------------------------------------------------

result = inventory.scan(MBOX_PATHS)


# ---------------------------------------------------------
# Report
# ---------------------------------------------------------

print("=" * 65)
print("READ-ONLY CROSS-MBOX CANDIDATE INVENTORY")
print("=" * 65)

print("\nSources:")

for path in MBOX_PATHS:
    print("  -", path)

print("\nTarget correspondent addresses:")

for email_address in TARGET_EMAILS:
    print("  -", email_address)

print("\nStart date:", START_DATE)

print()
print("Total messages:", result["total_messages"])
print("Candidate occurrences:", result["candidate_occurrences"])
print("Unique candidate messages:", result["unique_candidate_messages"])
print("Duplicate occurrences:", result["duplicate_occurrences"])
print("Missing Message-ID:", result["missing_message_id"])

print()
print("READ ONLY: no evidence files were written.")