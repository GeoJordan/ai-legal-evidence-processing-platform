"""
Narrative section domain model.
"""


class NarrativeSection:

    def __init__(self, heading: str, content: str):
        self.heading = heading
        self.content = content
        self.sources = []

    def test_section_stores_content():
        section = NarrativeSection(
            heading="Passport Request",
            content="On August 1 the petitioner requested..."
        )

        assert section.content == "On August 1 the petitioner requested..."

    def add_source(self, source):
        self.sources.append(source)
    