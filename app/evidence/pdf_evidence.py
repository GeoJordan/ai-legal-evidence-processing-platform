from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class PDFEvidence(EvidenceItem):

    def __init__(
        self,
        filename="",
        pages=0,
        path="",
        collected_at=None,
    ):
        super().__init__(
            evidence_type=EvidenceType.PDF,
            source="pdf",
            collected_at=collected_at,
        )

        self.filename = filename
        self.pages = pages
        self.path = path

    @property
    def title(self):
        return self.filename