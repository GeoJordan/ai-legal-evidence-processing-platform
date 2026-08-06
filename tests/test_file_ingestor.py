from app.ingestors.file_ingestor import FileIngestor


def test_file_ingestor_can_be_created():

    ingestor = FileIngestor()

    assert ingestor.name == "File Ingestor"

def test_file_ingestor_supports_pdf():

    ingestor = FileIngestor()

    assert ingestor.supports("document.pdf")

def test_file_ingestor_rejects_unknown_extension():

    ingestor = FileIngestor()

    assert not ingestor.supports("archive.xyz")