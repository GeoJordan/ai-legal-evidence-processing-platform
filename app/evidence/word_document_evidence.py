from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class WordDocumentEvidence(EvidenceItem):

    def __init__(
        self,
        filename="",
        title="",
        author="",
        page_count=0,
        source_path="",
        collected_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.WORD_DOCUMENT,
            source="word",
            collected_at=collected_at,
        )

        self.filename = filename
        self.document_title = title
        self.author = author
        self.page_count = page_count
        self.source_path = source_path

    @property
    def title(self):
        return self.document_title or self.filename