from pathlib import Path

from app.ingestors.email.mbox_reader import MboxReader


class MboxCandidateInventory:
    """
    Performs a read-only inventory of an MBOX source and counts
    messages that satisfy the configured selection criteria.
    """

    def __init__(
        self,
        correspondent_selector,
        date_selector,
    ):
        self.correspondent_selector = correspondent_selector
        self.date_selector = date_selector

    def scan(self, mbox_path: str | Path) -> dict:

        reader = MboxReader(Path(mbox_path))

        total_messages = 0
        candidate_messages = 0

        for message in reader.read():

            total_messages += 1

            if not self.correspondent_selector.matches(message):
                continue

            if not self.date_selector.matches(message):
                continue

            candidate_messages += 1

        return {
            "total_messages": total_messages,
            "candidate_messages": candidate_messages,
        }