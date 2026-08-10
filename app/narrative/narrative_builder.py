from app.narrative.narrative import Narrative
from app.narrative.narrative_section import NarrativeSection

class NarrativeBuilder:
    """Builds a Narrative from a Timeline."""

    def build(self, timeline):
        return Narrative()

    def build(self, timeline):
        narrative = Narrative()

        for event in timeline.events():
            # Temporary implementation
                section = NarrativeSection(
                      heading=event.title,
                      content=event.description
                )

                narrative.add_section(section)

        return narrative