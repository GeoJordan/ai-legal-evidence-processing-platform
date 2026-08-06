from app.models.timeline_event import TimelineEvent


class TimelineGenerator:
    """
    Generates chronological legal timelines from indexed evidence.
    """

    def __init__(self):
        self._events = []

    def build(self, evidence_index):

        self._events = []

        for message in evidence_index.messages:

            header = message.header

            event = TimelineEvent(
                date=header.date,
                sender=header.sender,
                recipient=header.recipient,
                subject=header.subject,
                message_id=header.message_id,
            )

            self._events.append(event)

        return self._events
    