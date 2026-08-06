"""
EP-206 Base Ingestor

Defines the common interface for all evidence ingestors.
"""

from abc import ABC, abstractmethod


class BaseIngestor(ABC):
    """
    Abstract base class for all evidence ingestors.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable ingestor name.
        """
        pass

    @abstractmethod
    def supports(self, path) -> bool:
        """
        Return True if this ingestor supports the given evidence source.
        """
        pass

    @abstractmethod
    def ingest(self, path, context):
        """
        Ingest evidence into the shared EvidenceContext.
        """
        pass