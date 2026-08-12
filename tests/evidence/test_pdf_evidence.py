from app.evidence.pdf_evidence import PDFEvidence
from app.evidence.evidence_type import EvidenceType


def test_pdf_evidence_stores_fields():
    pdf = PDFEvidence(
        filename="contract.pdf",
        pages=12,
        path="/documents/contract.pdf",
    )

    assert pdf.filename == "contract.pdf"
    assert pdf.pages == 12
    assert pdf.path == "/documents/contract.pdf"


def test_pdf_evidence_title_returns_filename():
    pdf = PDFEvidence(
        filename="Evidence_Report.pdf"
    )

    assert pdf.title == "Evidence_Report.pdf"


def test_pdf_evidence_inherits_common_properties():
    pdf = PDFEvidence()

    assert pdf.evidence_type == EvidenceType.PDF
    assert pdf.source == "pdf"
    assert pdf.collected_at is not None


def test_pdf_evidence_default_pages_is_zero():
    pdf = PDFEvidence()

    assert pdf.pages == 0