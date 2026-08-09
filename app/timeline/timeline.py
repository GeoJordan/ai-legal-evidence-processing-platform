"""
Timeline domain model.

Represents an ordered collection of chronological events.
"""

from datetime import date

class Timeline:

    """
    Represents a single chronological event.
    """

    def __init__(self):
        self._events = []

    def events(self):
        return list(self._events)

    def add_event(self, event):
        self._events.append(event)
        self._events.sort(key=lambda e: e.date)