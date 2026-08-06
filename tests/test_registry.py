from app.ingestors.registry import IngestorRegistry
from app.ingestors.base import BaseIngestor


class DummyIngestor(BaseIngestor):

    @property
    def name(self):
        return "Dummy"

    def supports(self, path):
        return True

    def ingest(self, path, context):
        return context


def test_registry_can_register_ingestor():

    registry = IngestorRegistry()

    registry.register(DummyIngestor())

    assert len(registry.ingestors) == 1

def test_registry_can_find_matching_ingestor():

    registry = IngestorRegistry()

    ingestor = DummyIngestor()

    registry.register(ingestor)

    result = registry.find("sample.mbox")

    assert result is ingestor

import pytest


def test_registry_raises_when_no_ingestor_matches():

    registry = IngestorRegistry()

    with pytest.raises(LookupError):
        registry.find("unknown.xyz")