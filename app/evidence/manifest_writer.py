import csv
from pathlib import Path


class ManifestWriter:
    """
    Appends evidence records to an existing manifest.csv
    using the approved repository schema.
    """

    APPROVED_HEADERS = [
        "File ID",
        "Filename",
        "Evidence Type",
        "Source",
        "Date",
        "Authenticity",
        "Related AL",
        "Related RFP",
        "Status",
    ]

    def __init__(self, manifest_path: str | Path):
        self.manifest_path = Path(manifest_path)

    def _validate_schema(self) -> None:
        """
        Verify that the existing manifest uses the approved schema.
        """

        with self.manifest_path.open(
            "r",
            newline="",
            encoding="utf-8",
        ) as file:
            reader = csv.reader(file)
            headers = next(reader, None)

        if headers != self.APPROVED_HEADERS:
            raise ValueError(
                "Manifest schema does not match the approved schema."
            )

    def append(self, record: dict) -> None:

        self._validate_schema()
        self._validate_record(record)
        self._validate_unique_file_id(record)

        with self.manifest_path.open(
            "a",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=self.APPROVED_HEADERS,
            )

            writer.writerow(record)

    def _validate_record(self, record: dict) -> None:
        """
        Verify that a manifest record contains exactly
        the fields required by the approved schema.
        """

        if set(record.keys()) != set(self.APPROVED_HEADERS):
            raise ValueError(
                "Manifest record does not match the approved schema."
            )

    def _validate_unique_file_id(self, record: dict) -> None:
        """
        Ensure the File ID does not already exist in the manifest.
        """

        with self.manifest_path.open(
            "r",
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for existing_record in reader:
                if existing_record["File ID"] == record["File ID"]:
                    raise ValueError(
                        f"Duplicate File ID: {record['File ID']}"
                    )
