from pathlib import Path

from app.evidence.candidate_metadata_inventory import (
    CandidateMetadataInventory,
)
from app.ingestors.email.mbox_reader import MboxReader


class CandidateMetadataReport:
    """
    Collects read-only metadata for unique candidate messages
    across one or more MBOX sources.
    """

    def __init__(
        self,
        correspondent_selector,
        date_selector,
    ):
        self.correspondent_selector = correspondent_selector
        self.date_selector = date_selector
        self.metadata_inventory = CandidateMetadataInventory()

    def collect(self, mbox_paths: list[str | Path]) -> list[dict]:

        records = []
        seen_message_ids = set()

        for mbox_path in mbox_paths:

            reader = MboxReader(Path(mbox_path))

            for message in reader.read():

                if not self.correspondent_selector.matches(message):
                    continue

                if not self.date_selector.matches(message):
                    continue

                message_id = str(
                    message.get("Message-ID", "")
                ).strip()

                if not message_id:
                    continue

                normalized_message_id = message_id.lower()

                if normalized_message_id in seen_message_ids:
                    continue

                seen_message_ids.add(normalized_message_id)

                record = self.metadata_inventory.extract(
                    message,
                    source_mbox=Path(mbox_path).name,
                )

                records.append(record)

        return records