from app.timeline.timeline_generator import TimelineGenerator


def test_timeline_generator_can_be_created():

    generator = TimelineGenerator()

    assert generator is not None

from app.evidence.evidence_index import EvidenceIndex
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_timeline_generator_builds_events():

    index = EvidenceIndex()

    header = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Meeting",
        date="2026-08-06",
        message_id="<123@example.com>",
    )

    message = EmailMessage(
        header=header,
        body="Hello",
    )

    index.add_message(message)

    generator = TimelineGenerator()

    events = generator.build(index)

    assert len(events) == 1
    assert events[0].subject == "Meeting"

from app.evidence.evidence_index import EvidenceIndex
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


def test_timeline_generator_sorts_events():

    index = EvidenceIndex()

    dates = [
        "2026-08-05",
        "2026-08-01",
        "2026-08-03",
    ]

    for date in dates:

        header = EmailHeader(
            sender="alice@example.com",
            recipient="bob@example.com",
            subject=f"Message {date}",
            date=date,
            message_id=f"<{date}@example.com>",
        )

        message = EmailMessage(
            header=header,
            body="Hello",
        )

        index.add_message(message)

    generator = TimelineGenerator()

    events = generator.build(index)

    assert events[0].date == "2026-08-01"
    assert events[1].date == "2026-08-03"
    assert events[2].date == "2026-08-05"