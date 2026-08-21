import csv
from pathlib import Path


class CandidateMetadataCsvQA:
    """
    Performs QA validation of a candidate metadata review CSV.

    This validator is read-only. It does not modify the CSV
    or write evidence into the legal workspace.
    """

    EXPECTED_HEADERS = [
        "message_id",
        "date",
        "from",
        "to",
        "subject",
        "source_mbox",
        "has_attachments",
    ]

    def validate(self, csv_path: str | Path) -> dict:

        csv_path = Path(csv_path)

        row_count = 0
        duplicate_message_ids = 0
        missing_message_ids = 0
        attachment_true = 0
        attachment_false = 0
        unexpected_attachment_values = 0

        seen_message_ids = set()

        with csv_path.open(
            "r",
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            schema_valid = reader.fieldnames == self.EXPECTED_HEADERS

            for row in reader:

                row_count += 1

                # -----------------------------------------
                # Message-ID validation
                # -----------------------------------------

                message_id = (
                    row.get("message_id") or ""
                ).strip()

                if not message_id:
                    missing_message_ids += 1
                else:
                    normalized_message_id = message_id.lower()

                    if normalized_message_id in seen_message_ids:
                        duplicate_message_ids += 1
                    else:
                        seen_message_ids.add(
                            normalized_message_id
                        )

                # -----------------------------------------
                # Attachment flag validation
                # -----------------------------------------

                attachment_value = (
                    row.get("has_attachments") or ""
                ).strip()

                if attachment_value == "True":
                    attachment_true += 1

                elif attachment_value == "False":
                    attachment_false += 1

                else:
                    unexpected_attachment_values += 1

        passed = (
            schema_valid
            and duplicate_message_ids == 0
            and missing_message_ids == 0
            and unexpected_attachment_values == 0
        )

        return {
            "row_count": row_count,
            "schema_valid": schema_valid,
            "duplicate_message_ids": duplicate_message_ids,
            "missing_message_ids": missing_message_ids,
            "attachment_true": attachment_true,
            "attachment_false": attachment_false,
            "unexpected_attachment_values": (
                unexpected_attachment_values
            ),
            "passed": passed,
        }