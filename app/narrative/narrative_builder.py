from app.narrative.narrative import Narrative
from app.narrative.narrative_section import NarrativeSection

class NarrativeBuilder:
    """Builds a Narrative from a Timeline."""

    def build(self, timeline):
        narrative = Narrative()

        for event in timeline.events():

            section = NarrativeSection(
                heading=event.title,
                content=event.description
            )

            for source in event.sources:
                section.add_source(source)

            narrative.add_section(section)

        return narrative
