import csv

from app.evidence.manifest_writer import ManifestWriter


def test_manifest_writer_appends_row_using_approved_schema(tmp_path):

    manifest_path = tmp_path / "manifest.csv"

    headers = [
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

    with manifest_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    manifest_writer = ManifestWriter(manifest_path)

    manifest_writer.append(
        {
            "File ID": "EV-001-0001",
            "Filename": "synthetic_email.pdf",
            "Evidence Type": "Email",
            "Source": "Synthetic Test",
            "Date": "2026-08-20",
            "Authenticity": "Unverified",
            "Related AL": "AL-002",
            "Related RFP": "RFP-005",
            "Status": "Original",
        }
    )

    with manifest_path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1

    assert rows[0]["File ID"] == "EV-001-0001"
    assert rows[0]["Filename"] == "synthetic_email.pdf"
    assert rows[0]["Evidence Type"] == "Email"
    assert rows[0]["Status"] == "Original"

def test_manifest_writer_rejects_invalid_schema(tmp_path):

    manifest_path = tmp_path / "manifest.csv"

    manifest_path.write_text(
        "File ID,Filename,Wrong Column\n",
        encoding="utf-8",
    )

    manifest_writer = ManifestWriter(manifest_path)

    try:
        manifest_writer.append(
            {
                "File ID": "EV-001-0001",
                "Filename": "synthetic_email.pdf",
                "Evidence Type": "Email",
                "Source": "Synthetic Test",
                "Date": "2026-08-20",
                "Authenticity": "Unverified",
                "Related AL": "AL-002",
                "Related RFP": "RFP-005",
                "Status": "Original",
            }
        )

        assert False, "Expected ValueError"

    except ValueError as error:
        assert "schema" in str(error).lower()

def test_manifest_writer_rejects_record_with_missing_field(tmp_path):

    manifest_path = tmp_path / "manifest.csv"

    headers = ManifestWriter.APPROVED_HEADERS

    with manifest_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    manifest_writer = ManifestWriter(manifest_path)

    invalid_record = {
        "File ID": "EV-001-0001",
        "Filename": "synthetic_email.pdf",
        "Evidence Type": "Email",
        "Source": "Synthetic Test",
        "Date": "2026-08-20",
        "Authenticity": "Unverified",
        "Related AL": "AL-002",
        "Related RFP": "RFP-005",
        # "Status" deliberately omitted
    }

    try:
        manifest_writer.append(invalid_record)

        assert False, "Expected ValueError"

    except ValueError as error:
        assert "record" in str(error).lower()

def test_manifest_writer_rejects_duplicate_file_id(tmp_path):

    manifest_path = tmp_path / "manifest.csv"

    headers = ManifestWriter.APPROVED_HEADERS

    with manifest_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    manifest_writer = ManifestWriter(manifest_path)

    first_record = {
        "File ID": "EV-001-0001",
        "Filename": "synthetic_email_1.pdf",
        "Evidence Type": "Email",
        "Source": "Synthetic Test",
        "Date": "2026-08-20",
        "Authenticity": "Unverified",
        "Related AL": "AL-002",
        "Related RFP": "RFP-005",
        "Status": "Original",
    }

    duplicate_record = {
        "File ID": "EV-001-0001",
        "Filename": "synthetic_email_2.pdf",
        "Evidence Type": "Email",
        "Source": "Synthetic Test",
        "Date": "2026-08-20",
        "Authenticity": "Unverified",
        "Related AL": "AL-002",
        "Related RFP": "RFP-005",
        "Status": "Original",
    }

    manifest_writer.append(first_record)

    try:
        manifest_writer.append(duplicate_record)

        assert False, "Expected ValueError"

    except ValueError as error:
        assert "duplicate" in str(error).lower()
        assert "file id" in str(error).lower()