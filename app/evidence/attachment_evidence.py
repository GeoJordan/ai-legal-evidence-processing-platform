from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class AttachmentEvidence(EvidenceItem):

    def __init__(
        self,
        filename="",
        content_type="",
        size_bytes=0,
        sha256="",
        source_path="",
        collected_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.ATTACHMENT,
            source="attachment",
            collected_at=collected_at,
        )

        self.filename = filename
        self.content_type = content_type
        self.size_bytes = size_bytes
        self.sha256 = sha256
        self.source_path = source_path

    @property
    def title(self):
        return self.filename
