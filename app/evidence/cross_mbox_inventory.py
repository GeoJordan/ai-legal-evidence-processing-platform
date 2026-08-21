from pathlib import Path

from app.ingestors.email.mbox_reader import MboxReader


class CrossMboxInventory:
    """
    Performs a read-only inventory across multiple MBOX sources.

    Candidate messages are selected using the configured correspondent
    and date selectors, then deduplicated using Message-ID.
    """

    def __init__(
        self,
        correspondent_selector,
        date_selector,
    ):
        self.correspondent_selector = correspondent_selector
        self.date_selector = date_selector

    def scan(self, mbox_paths: list[str | Path]) -> dict:

        total_messages = 0
        candidate_occurrences = 0
        duplicate_occurrences = 0
        missing_message_id = 0

        seen_message_ids = set()

        for mbox_path in mbox_paths:

            reader = MboxReader(Path(mbox_path))

            for message in reader.read():

                total_messages += 1

                if not self.correspondent_selector.matches(message):
                    continue

                if not self.date_selector.matches(message):
                    continue

                candidate_occurrences += 1

                message_id = message.get("Message-ID")

                if not message_id:
                    missing_message_id += 1
                    continue

                normalized_message_id = message_id.strip().lower()

                if normalized_message_id in seen_message_ids:
                    duplicate_occurrences += 1
                    continue

                seen_message_ids.add(normalized_message_id)

        return {
            "total_messages": total_messages,
            "candidate_occurrences": candidate_occurrences,
            "unique_candidate_messages": len(seen_message_ids),
            "duplicate_occurrences": duplicate_occurrences,
            "missing_message_id": missing_message_id,
        }