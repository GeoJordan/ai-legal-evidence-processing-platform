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

def test_timeline_generator_exports_events():

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

    report = generator.export(events)

    assert "Meeting" in report
    assert "alice@example.com" in report
    assert "2026-08-06" in report

def test_timeline_generator_filters_by_sender():

    index = EvidenceIndex()

    header1 = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Meeting",
        date="2026-08-01",
        message_id="<1@example.com>",
    )

    header2 = EmailHeader(
        sender="charlie@example.com",
        recipient="bob@example.com",
        subject="Invoice",
        date="2026-08-02",
        message_id="<2@example.com>",
    )

    index.add_message(
        EmailMessage(header=header1, body="Hello")
    )

    index.add_message(
        EmailMessage(header=header2, body="Hi")
    )

    generator = TimelineGenerator()

    events = generator.build(index)

    filtered = generator.filter_by_sender(
        events,
        "alice@example.com",
    )

    assert len(filtered) == 1
    assert filtered[0].sender == "alice@example.com"

def test_timeline_generator_filters_by_keyword():

    index = EvidenceIndex()

    header1 = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Passport Request",
        date="2026-08-01",
        message_id="<1@example.com>",
    )

    header2 = EmailHeader(
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Meeting Notes",
        date="2026-08-02",
        message_id="<2@example.com>",
    )

    index.add_message(
        EmailMessage(header=header1, body="Please send the passport.")
    )

    index.add_message(
        EmailMessage(header=header2, body="Agenda for tomorrow.")
    )

    generator = TimelineGenerator()

    events = generator.build(index)

    filtered = generator.filter_by_keyword(
        events,
        "passport",
    )

    assert len(filtered) == 1
    assert filtered[0].subject == "Passport Request"