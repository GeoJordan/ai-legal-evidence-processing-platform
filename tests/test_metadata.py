from app.configuration import Configuration
from app.context import EvidenceContext
from app.metadata import MetadataExtractor


def test_metadata_extractor_can_be_created():
    config = Configuration("config/case.yaml")

    context = EvidenceContext(config)

    extractor = MetadataExtractor()

    assert extractor is not None
    assert context.message_count == 0
    assert context.headers == []
    assert context.messages == []
    assert context.attachments == []
