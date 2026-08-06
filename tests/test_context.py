from app.configuration import Configuration
from app.context import EvidenceContext


def test_context_can_be_created():
    config = Configuration("config/case.yaml")

    context = EvidenceContext(config)

    assert context.configuration.case_name == "Sample Legal Case"
    assert context.file_records == []
    assert context.errors == []
    assert context.warnings == []