from app.ingestors.base import BaseIngestor


class DummyIngestor(BaseIngestor):

    @property
    def name(self):
        return "Dummy"

    def supports(self, path):
        return True

    def ingest(self, path, context):
        return context


def test_base_ingestor_can_be_subclassed():

    ingestor = DummyIngestor()

    assert ingestor.name == "Dummy"