"""
Timeline Event domain model.
"""

from datetime import date


class TimelineEvent:
    """Represents a single chronological event."""

    def __init__(self, date: date, title: str):
        self.date = date
        self.title = title
