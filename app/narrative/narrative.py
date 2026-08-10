"""
Narrative domain model.
"""


class Narrative:
    """Represents an ordered collection of narrative sections."""

    def __init__(self):
        self._sections = []

    def sections(self):
        return self._sections

    def add_section(self, section):
        self._sections.append(section)