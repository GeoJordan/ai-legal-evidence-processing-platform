"""
Timeline Event domain model.
"""

from datetime import date


class TimelineEvent:
    """Represents a single chronological event."""

    def __init__(
    self,
    date,
    title,
    description=""
    ):
        self.date = date
        self.title = title
        self.description = description
        self.sources = []

    def add_source(self, source):
        """Adds a supporting evidence source."""
        self.sources.append(source)
