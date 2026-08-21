from pathlib import Path

from app.configuration import Configuration
from app.evidence.attachment_writer import AttachmentWriter
from app.evidence.repository_path_resolver import RepositoryPathResolver
from app.models.attachment import Attachment


configuration = Configuration(
    Path("config/case.yaml")
)

resolver = RepositoryPathResolver(
    configuration.evidence_path
)

destination = resolver.resolve(
    package="05_passports_travel",
    stage="original",
    source="emails",
)

attachment = Attachment(
    filename="SYNTHETIC_REPOSITORY_TEST_DO_NOT_USE_AS_EVIDENCE.txt",
    content_type="text/plain",
    size=36,
    data=b"SYNTHETIC TEST - NOT CASE EVIDENCE",
)

writer = AttachmentWriter()

evidence = writer.write(
    attachment,
    destination,
)

output_path = Path(evidence.source_path)

print("DRY RUN SUCCESS")
print("Case:", configuration.case_name)
print("Evidence root:", configuration.evidence_path)
print("Destination:", destination)
print("Written file:", output_path)
print("File exists:", output_path.exists())
print("SHA-256:", evidence.sha256)
print("Size:", evidence.size_bytes)