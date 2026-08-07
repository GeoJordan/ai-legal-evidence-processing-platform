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

            # Add the event to the internal list
            self._events.append(event)

        # Sort after ALL events have been added
        self._events.sort(key=lambda event: event.date)

        # Return a copy of the list
        return list(self._events)

    def export(self, events):
        """
        Export timeline events as a human-readable text report.
        """

        lines = []

        for event in events:

            lines.append(f"Date: {event.date}")
            lines.append(f"From: {event.sender}")
            lines.append(f"To: {event.recipient}")
            lines.append(f"Subject: {event.subject}")
            lines.append("-" * 50)
            lines.append("")

        return "\n".join(lines)

    def filter_by_sender(self, events, sender):
        """
        Return only timeline events sent by the specified sender.
        """

        return [
            event
            for event in events
            if event.sender.lower() == sender.lower()
        ]