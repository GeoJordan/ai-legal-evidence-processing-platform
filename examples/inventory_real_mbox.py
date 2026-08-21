from pathlib import Path

from app.evidence.correspondent_selector import CorrespondentSelector
from app.evidence.date_selector import DateSelector
from app.evidence.mbox_candidate_inventory import MboxCandidateInventory


# ---------------------------------------------------------
# Configure source
# ---------------------------------------------------------

MBOX_PATH = Path(
    r"C:\PATH\TO\Inbox-003.mbox"
)

TARGET_EMAILS = [
    "person.primary@example.com",
    "person.secondary@example.com",
]

START_DATE = "2022-01-01"


# ---------------------------------------------------------
# Build read-only selectors
# ---------------------------------------------------------

correspondent_selector = CorrespondentSelector(
    TARGET_EMAILS
)

date_selector = DateSelector(
    start_date=START_DATE
)

inventory = MboxCandidateInventory(
    correspondent_selector=correspondent_selector,
    date_selector=date_selector,
)


# ---------------------------------------------------------
# Read-only inventory
# ---------------------------------------------------------

result = inventory.scan(MBOX_PATH)

print("=" * 60)
print("READ-ONLY MBOX CANDIDATE INVENTORY")
print("=" * 60)

print("Source:", MBOX_PATH)
print("Target correspondent addresses:")

for email_address in TARGET_EMAILS:
    print("  -", email_address)
print("Start date:", START_DATE)

print()
print("Total messages:", result["total_messages"])
print("Candidate messages:", result["candidate_messages"])

print()
print("READ ONLY: no evidence files were written.")