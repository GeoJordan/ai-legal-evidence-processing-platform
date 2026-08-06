from app.models.timeline_event import TimelineEvent


def test_timeline_event_can_be_created():

    event = TimelineEvent(
        date="2026-08-06",
        sender="alice@example.com",
        recipient="bob@example.com",
        subject="Meeting",
        message_id="<123@example.com>",
    )

    assert event.subject == "Meeting"