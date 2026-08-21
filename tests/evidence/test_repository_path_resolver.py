from pathlib import Path

from app.evidence.attachment_writer import AttachmentWriter
from app.evidence.repository_path_resolver import RepositoryPathResolver
from app.models.attachment import Attachment
from app.configuration import Configuration


def test_resolver_builds_passports_email_original_path(tmp_path):

    evidence_root = tmp_path / "04_evidence"

    resolver = RepositoryPathResolver(evidence_root)

    result = resolver.resolve(
        package="05_passports_travel",
        stage="original",
        source="emails",
    )

    expected = (
        evidence_root
        / "05_passports_travel"
        / "original"
        / "emails"
    )

    assert result == expected

def test_resolver_and_writer_persist_attachment_to_resolved_path(tmp_path):

    evidence_root = tmp_path / "04_evidence"

    resolver = RepositoryPathResolver(evidence_root)

    destination = resolver.resolve(
        package="05_passports_travel",
        stage="original",
        source="emails",
    )

    attachment = Attachment(
        filename="synthetic_email_attachment.txt",
        content_type="text/plain",
        size=18,
        data=b"synthetic evidence",
    )

    writer = AttachmentWriter()

    evidence = writer.write(
        attachment,
        destination,
    )

    expected_path = (
        evidence_root
        / "05_passports_travel"
        / "original"
        / "emails"
        / "synthetic_email_attachment.txt"
    )

    assert expected_path.exists()
    assert expected_path.read_bytes() == b"synthetic evidence"

    assert Path(evidence.source_path) == expected_path.resolve()
    assert evidence.filename == "synthetic_email_attachment.txt"
    assert evidence.sha256

def test_resolver_accepts_configured_evidence_path():

    configuration = Configuration("config/case.yaml")

    resolver = RepositoryPathResolver(
        configuration.evidence_path
    )

    result = resolver.resolve(
        package="05_passports_travel",
        stage="original",
        source="emails",
    )

    expected = (
        configuration.evidence_path
        / "05_passports_travel"
        / "original"
        / "emails"
    )

    assert result == expected

def test_full_persistence_chain_with_temporary_configuration(tmp_path):

    case_root = tmp_path / "case"

    config_file = tmp_path / "case.yaml"

    config_file.write_text(
        f"""
case:
  name: "Synthetic Test Case"
  repository: "{tmp_path.as_posix()}"
  case_root: "{case_root.as_posix()}"

folders:
  evidence: "04_evidence"
  exhibits: "05_exhibits"
  timeline: "07_timeline"

processing:
  recursive_scan: true
  supported_extensions:
    - ".pdf"
    - ".txt"
""",
        encoding="utf-8",
    )

    configuration = Configuration(config_file)

    resolver = RepositoryPathResolver(
        configuration.evidence_path
    )

    destination = resolver.resolve(
        package="05_passports_travel",
        stage="original",
        source="emails",
    )

    attachment = Attachment(
        filename="synthetic_email.txt",
        content_type="text/plain",
        size=18,
        data=b"synthetic evidence",
    )

    writer = AttachmentWriter()

    evidence = writer.write(
        attachment,
        destination,
    )

    expected_path = (
        case_root
        / "04_evidence"
        / "05_passports_travel"
        / "original"
        / "emails"
        / "synthetic_email.txt"
    )

    assert expected_path.exists()
    assert expected_path.read_bytes() == b"synthetic evidence"

    assert Path(evidence.source_path) == expected_path.resolve()
    assert evidence.filename == "synthetic_email.txt"
    assert evidence.sha256