"""
EP-206B Ingestor Registry

Maintains a collection of evidence ingestors and locates
the appropriate ingestor for a given evidence source.
"""

from app.ingestors.base import BaseIngestor


class IngestorRegistry:
    """
    Registry of available evidence ingestors.
    """

    def __init__(self):
        self.ingestors: list[BaseIngestor] = []

    def register(self, ingestor: BaseIngestor):
        """
        Register a new ingestor.

        Returns:
            IngestorRegistry: self (supports fluent chaining)
        """
        self.ingestors.append(ingestor)
        return self

    def find(self, path):
        """
        Return the first ingestor that supports the given path.

        Raises:
            LookupError: if no ingestor supports the evidence source.
        """
        for ingestor in self.ingestors:
            if ingestor.supports(path):
                return ingestor

        raise LookupError(f"No ingestor registered for '{path}'")