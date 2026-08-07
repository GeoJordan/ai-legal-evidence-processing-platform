"""
This example demonstrates the completed Sprint 6
Evidence Intelligence subsystem.

Release: v0.6.0
"""


from app.evidence.evidence_index import EvidenceIndex
from app.timeline.timeline_generator import TimelineGenerator
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def main():

    index = EvidenceIndex()

    emails = [

        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="Passport Request",
                date="2026-08-01",
                message_id="<1@example.com>",
            ),
            body="Please send the passport.",
        ),

        EmailMessage(
            header=EmailHeader(
                sender="bob@example.com",
                recipient="alice@example.com",
                subject="Passport Delivered",
                date="2026-08-03",
                message_id="<2@example.com>",
            ),
            body="The passport has been delivered.",
        ),

        EmailMessage(
            header=EmailHeader(
                sender="alice@example.com",
                recipient="bob@example.com",
                subject="Travel Confirmation",
                date="2026-08-05",
                message_id="<3@example.com>",
            ),
            body="Thank you.",
        ),

    ]

    for message in emails:
        index.add_message(message)

    generator = TimelineGenerator()

    events = generator.build(index)

    print(generator.report(events))


if __name__ == "__main__":
    main()