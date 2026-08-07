from app.evidence.evidence_index import EvidenceIndex
from app.models.timeline_event import TimelineEvent


class TimelineGenerator:
    """
    Generates chronological legal timelines from indexed evidence.
    """

    REPORT_WIDTH = 60
    SECTION_DIVIDER = "=" * REPORT_WIDTH
    SUBSECTION_DIVIDER = "-" * 20

    def __init__(self):
        self._events = []

    def build(self, evidence_index: EvidenceIndex) -> list[TimelineEvent]:

        self._events = []

        for message in evidence_index.messages:

            header = message.header

            event = TimelineEvent(
                date=header.date,
                sender=header.sender,
                recipient=header.recipient,
                subject=header.subject,
                message_id=header.message_id,
                body=message.body,
        )

            # Add the event to the internal list
            self._events.append(event)

        # Sort after ALL events have been added
        self._events.sort(key=lambda event: event.date)

        # Return a copy of the list
        return list(self._events)

    def export(self, events: list[TimelineEvent]) -> str:
        """
        Export timeline events as a human-readable text report.
        """

        lines = []

        for event in events:

            lines.append(f"Date: {event.date}")
            lines.append(f"From: {event.sender}")
            lines.append(f"To: {event.recipient}")
            lines.append(f"Subject: {event.subject}")
            lines.append(self.SUBSECTION_DIVIDER)
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

    def filter_by_keyword(self, events, keyword):
        """
        Return timeline events whose subject or body contains the keyword.
        """

        keyword = keyword.lower()

        return [
            event
            for event in events
            if (
                keyword in event.subject.lower()
                or keyword in getattr(event, "body", "").lower()
            )
        ]

    def statistics(self, events):
        """
        Return summary statistics for a collection of timeline events.
        """

        senders = {event.sender for event in events}
        recipients = {event.recipient for event in events}

        return {
            "total_events": len(events),
            "unique_senders": len(senders),
            "unique_recipients": len(recipients),
            "earliest_date": min((event.date for event in events), default=None),
            "latest_date": max((event.date for event in events), default=None),
        }

    def report(self, events):
        """
        Generate a complete evidence timeline report.
        """

        stats = self.statistics(events)
        timeline = self.export(events)

        lines = [
            self.SECTION_DIVIDER,
            "Evidence Timeline Report",
            self.SECTION_DIVIDER,
            "",
            "Summary",
            self.SUBSECTION_DIVIDER,
            f"Total Events      : {stats['total_events']}",
            f"Unique Senders    : {stats['unique_senders']}",
            f"Unique Recipients : {stats['unique_recipients']}",
        ]

        if stats["earliest_date"]:
            lines.append(f"Earliest Date     : {stats['earliest_date']}")

        if stats["latest_date"]:
            lines.append(f"Latest Date       : {stats['latest_date']}")

        lines.extend([
            "",
            self.SECTION_DIVIDER,
            "Timeline",
            self.SECTION_DIVIDER,
            "",
            timeline,
        ])

        return "\n".join(lines)