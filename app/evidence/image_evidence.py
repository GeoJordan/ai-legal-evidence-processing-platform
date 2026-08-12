from app.evidence.evidence_item import EvidenceItem
from app.evidence.evidence_type import EvidenceType


class ImageEvidence(EvidenceItem):

    def __init__(
        self,
        filename="",
        width=0,
        height=0,
        path="",
        description="",
        collected_at=None,
    ):

        super().__init__(
            evidence_type=EvidenceType.IMAGE,
            source="image",
            collected_at=collected_at,
        )

        # store the path
        self.filename = filename
        self.width = width
        self.height = height
        self.path = path
        self.description = description

    @property
    def title(self):
        return self.filename