from app.evidence.court_document_evidence import CourtDocumentEvidence
from app.evidence.evidence_item import EvidenceItem


# stores fields
def test_court_document_stores_fields():

    document = CourtDocumentEvidence(
        court_name="Delaware Family Court",
        case_number="CN24-01234",
        document_type="Petition",
        title="Petition for Sole Custody",
        filing_date="2026-08-10",
        source_path="/court/petition.pdf",
    )

    assert document.court_name == "Delaware Family Court"
    assert document.case_number == "CN24-01234"
    assert document.document_type == "Petition"
    assert document.document_title == "Petition for Sole Custody"
    assert document.filing_date == "2026-08-10"
    assert document.source_path == "/court/petition.pdf"

# title
def test_court_document_title_returns_document_title():

    document = CourtDocumentEvidence(
        title="Motion to Compel"
    )

    assert document.title == "Motion to Compel"

# inheritance
def test_court_document_inherits_common_properties():

    document = CourtDocumentEvidence()

    assert isinstance(document, EvidenceItem)

# defaults
def test_court_document_defaults_are_empty():

    document = CourtDocumentEvidence()

    assert document.court_name == ""
    assert document.case_number == ""
    assert document.document_type == ""
    assert document.document_title == ""
    assert document.filing_date is None
    assert document.source_path == ""
    assert document.title == ""

