from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class CourtDocumentEvidence(EvidenceItem):

    def __init__(
        self,
        court_name="",
        case_number="",
        document_type="",
        title="",
        filing_date=None,
        source_path="",
        collected_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.COURT_DOCUMENT,
            source="court_document",
            collected_at=collected_at or filing_date,
        )

        self.court_name = court_name
        self.case_number = case_number
        self.document_type = document_type
        self.document_title = title
        self.filing_date = filing_date
        self.source_path = source_path

    @property
    def title(self):
        return self.document_title