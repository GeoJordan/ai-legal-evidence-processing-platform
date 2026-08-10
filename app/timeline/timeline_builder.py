"""
Timeline Builder application service.
"""


from app.timeline.timeline import Timeline


from app.timeline.timeline import Timeline


class TimelineBuilder:
    """Constructs Timeline objects."""

    def build(self, events):
        """
        Builds a Timeline from a collection of events.
        """
        timeline = Timeline()

        for event in events:
            timeline.add_event(event)

        return timeline

