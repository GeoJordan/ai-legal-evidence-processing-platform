import csv
import mailbox
from email.message import EmailMessage as RawEmailMessage

from app.context import EvidenceContext
from app.evidence.attachment_writer import AttachmentWriter
from app.evidence.manifest_writer import ManifestWriter
from app.evidence.repository_path_resolver import RepositoryPathResolver
from app.ingestors.email.email_ingestor import EmailIngestor
from app.ingestors.email.mbox_reader import MboxReader


def test_mbox_email_attachment_persists_and_registers_in_manifest(tmp_path):

    # ---------------------------------------------------------
    # 1. Create synthetic source MBOX
    # ---------------------------------------------------------

    mbox_path = tmp_path / "synthetic_source.mbox"

    mbox = mailbox.mbox(str(mbox_path))

    raw_message = RawEmailMessage()
    raw_message["Message-ID"] = "<synthetic-e2e-001@example.com>"
    raw_message["From"] = "alice@example.com"
    raw_message["To"] = "bob@example.com"
    raw_message["Subject"] = "Synthetic Passport Evidence"
    raw_message["Date"] = "Thu, 20 Aug 2026 14:30:00 -0400"

    raw_message.set_content(
        "Synthetic passport communication."
    )

    attachment_data = b"SYNTHETIC PASSPORT ATTACHMENT"

    raw_message.add_attachment(
        attachment_data,
        maintype="application",
        subtype="pdf",
        filename="synthetic_passport.pdf",
    )

    mbox.add(raw_message)
    mbox.flush()
    mbox.close()

    # ---------------------------------------------------------
    # 2. Ingest MBOX into EvidenceContext
    # ---------------------------------------------------------

    context = EvidenceContext()
    reader = MboxReader(mbox_path)
    ingestor = EmailIngestor()

    for message in reader.read():
        ingestor.ingest(message, context)

    assert context.message_count == 1
    assert len(context.attachments) == 1

    # ---------------------------------------------------------
    # 3. Create synthetic governed repository
    # ---------------------------------------------------------

    evidence_root = tmp_path / "04_evidence"

    resolver = RepositoryPathResolver(evidence_root)

    destination = resolver.resolve(
        package="05_passports_travel",
        stage="original",
        source="emails",
    )

    metadata_dir = (
        evidence_root
        / "05_passports_travel"
        / "metadata"
    )

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
    # 4. Persist extracted attachment
    # ---------------------------------------------------------

    attachment = context.attachments[0]

    attachment_writer = AttachmentWriter()

    evidence = attachment_writer.write(
        attachment,
        destination,
    )

    assert evidence.filename == "synthetic_passport.pdf"
    assert evidence.sha256
    assert len(evidence.sha256) == 64

    # ---------------------------------------------------------
    # 5. Register persisted evidence
    # ---------------------------------------------------------

    manifest_writer = ManifestWriter(manifest_path)

    manifest_writer.append(
        {
            "File ID": "EV-001-TEST-0001",
            "Filename": evidence.filename,
            "Evidence Type": "Email Attachment",
            "Source": "Synthetic MBOX",
            "Date": "2026-08-20",
            "Authenticity": "Unverified",
            "Related AL": "",
            "Related RFP": "",
            "Status": "Original",
        }
    )

    # ---------------------------------------------------------
    # 6. Verify repository + manifest
    # ---------------------------------------------------------

    expected_file = (
        evidence_root
        / "05_passports_travel"
        / "original"
        / "emails"
        / "synthetic_passport.pdf"
    )

    assert expected_file.exists()
    assert expected_file.read_bytes() == attachment_data

    with manifest_path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1
    assert rows[0]["File ID"] == "EV-001-TEST-0001"
    assert rows[0]["Filename"] == "synthetic_passport.pdf"
    assert rows[0]["Status"] == "Original"