"""
Behavior Specification

Component:
TimelineEvent

Purpose:
Represents a single chronological event within a case timeline.

TimelineEvent shall:

- store a date
- store a title
- optionally store a description
- maintain supporting evidence sources
- preserve evidence insertion order
"""

from datetime import date

from app.timeline.timeline_event import TimelineEvent
from app.timeline.event_source import EventSource

def test_event_stores_date_and_title():
    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    assert event.date == date(2026, 8, 1)
    assert event.title == "Passport Email"

def test_event_stores_description():
    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email",
        description="Email requesting the child's passport."
    )

    assert event.description == (
        "Email requesting the child's passport."
    )

def test_event_starts_with_no_sources():
    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    assert event.sources == []

def test_add_source():
    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    source = EventSource(
    evidence_id="EV-001"
    )

    event.add_source(source)

    assert len(event.sources) == 1
    assert event.sources[0] == source

