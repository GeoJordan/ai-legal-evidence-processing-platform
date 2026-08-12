from app.evidence.evidence_index import EvidenceIndex


def test_index_starts_empty():

    index = EvidenceIndex()

    assert index.message_count() == 0
    assert index.attachment_count() == 0
    assert index.header_count() == 0

from app.evidence.email_evidence import EmailEvidence


def test_add_message():

    index = EvidenceIndex()

    email = EmailEvidence(subject="Quarterly Report")

    index.add_message(email)

    assert index.message_count() == 1
    assert index.messages[0] is email

from app.evidence.pdf_evidence import PDFEvidence


def test_add_attachment():

    index = EvidenceIndex()

    pdf = PDFEvidence(filename="contract.pdf")

    index.add_attachment(pdf)

    assert index.attachment_count() == 1
    assert index.attachments[0] is pdf

def test_add_header():

    index = EvidenceIndex()

    header = {
        "From": "George",
        "To": "Alice"
    }

    index.add_header(header)

    assert index.header_count() == 1
    assert index.headers[0] == header

from app.evidence.email_evidence import EmailEvidence
from app.evidence.pdf_evidence import PDFEvidence


def test_clear():

    index = EvidenceIndex()

    index.add_message(EmailEvidence())
    index.add_attachment(PDFEvidence())
    index.add_header({})

    index.clear()

    assert index.message_count() == 0
    assert index.attachment_count() == 0
    assert index.header_count() == 0

from app.evidence.email_evidence import EmailEvidence
from app.evidence.pdf_evidence import PDFEvidence


class FakeContext:

    def __init__(self):

        self.headers = [{"Message-ID": "1"}]

        self.messages = [
            EmailEvidence(subject="Hello")
        ]

        self.attachments = [
            PDFEvidence(filename="contract.pdf")
        ]


def test_load():

    context = FakeContext()

    index = EvidenceIndex()

    index.load(context)

    assert index.header_count() == 1
    assert index.message_count() == 1
    assert index.attachment_count() == 1