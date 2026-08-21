import csv

from app.evidence.attachment_writer import AttachmentWriter
from app.evidence.manifest_writer import ManifestWriter
from app.models.attachment import Attachment


def test_attachment_persistence_and_manifest_registration(tmp_path):

    # ---------------------------------------------------------
    # 1. Build a completely synthetic repository
    # ---------------------------------------------------------

    evidence_dir = tmp_path / "05_passports_travel" / "original" / "emails"
    evidence_dir.mkdir(parents=True)

    metadata_dir = tmp_path / "05_passports_travel" / "metadata"
    metadata_dir.mkdir(parents=True)

    manifest_path = metadata_dir / "manifest.csv"

    with manifest_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(ManifestWriter.APPROVED_HEADERS)

    # ---------------------------------------------------------
    # 2. Create synthetic evidence
    # ---------------------------------------------------------

    attachment = Attachment(
        filename="synthetic_passport_email.txt",
        content_type="text/plain",
        size=0,
        data=b"SYNTHETIC TEST EVIDENCE - NOT REAL CASE EVIDENCE",
    )

    # ---------------------------------------------------------
    # 3. Persist synthetic original
    # ---------------------------------------------------------

    attachment_writer = AttachmentWriter()

    evidence = attachment_writer.write(
        attachment,
        evidence_dir,
    )

    # ---------------------------------------------------------
    # 4. Verify physical persistence
    # ---------------------------------------------------------

    assert evidence_dir.joinpath(
        "synthetic_passport_email.txt"
    ).exists()

    assert evidence.sha256
    assert len(evidence.sha256) == 64

    # ---------------------------------------------------------
    # 5. Register synthetic evidence in manifest
    # ---------------------------------------------------------

    manifest_writer = ManifestWriter(manifest_path)

    manifest_writer.append(
        {
            "File ID": "EV-001-TEST-0001",
            "Filename": evidence.filename,
            "Evidence Type": "Email",
            "Source": "Synthetic Integration Test",
            "Date": "2026-08-20",
            "Authenticity": "Unverified",
            "Related AL": "",
            "Related RFP": "",
            "Status": "Original",
        }
    )

    # ---------------------------------------------------------
    # 6. Verify manifest registration
    # ---------------------------------------------------------

    with manifest_path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1
    assert rows[0]["File ID"] == "EV-001-TEST-0001"
    assert rows[0]["Filename"] == "synthetic_passport_email.txt"
    assert rows[0]["Status"] == "Original"