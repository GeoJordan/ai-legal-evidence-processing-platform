from app.evidence.word_document_evidence import WordDocumentEvidence
from app.evidence.evidence_item import EvidenceItem


def test_word_document_stores_fields():

    doc = WordDocumentEvidence(
        filename="Discovery_Response.docx",
        title="Respondent Discovery Responses",
        author="George Jordan",
        page_count=18,
        source_path="/documents/discovery.docx",
    )

    assert doc.filename == "Discovery_Response.docx"
    assert doc.document_title == "Respondent Discovery Responses"
    assert doc.author == "George Jordan"
    assert doc.page_count == 18
    assert doc.source_path == "/documents/discovery.docx"


def test_word_document_title_returns_document_title():

    doc = WordDocumentEvidence(
        title="Custody Response"
    )

    assert doc.title == "Custody Response"


def test_word_document_inherits_common_properties():

    doc = WordDocumentEvidence()

    assert isinstance(doc, EvidenceItem)


def test_word_document_defaults_are_empty():

    doc = WordDocumentEvidence()

    assert doc.filename == ""
    assert doc.document_title == ""
    assert doc.author == ""
    assert doc.page_count == 0
    assert doc.source_path == ""
    assert doc.title == ""