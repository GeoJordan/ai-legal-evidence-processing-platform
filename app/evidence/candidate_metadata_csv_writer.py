import csv
from datetime import datetime
from pathlib import Path


class CandidateMetadataCsvWriter:
    """
    Writes candidate email metadata records to a review CSV.
    """

    HEADERS = [
        "message_id",
        "date",
        "from",
        "to",
        "subject",
        "source_mbox",
        "has_attachments",
    ]

    def __init__(self, output_path: str | Path):
        self.output_path = Path(output_path)

    def write(self, records: list[dict]) -> None:

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.output_path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=self.HEADERS,
            )

            writer.writeheader()

            for record in records:

                row = dict(record)

                if isinstance(row.get("date"), datetime):
                    row["date"] = row["date"].isoformat()

                writer.writerow(row)