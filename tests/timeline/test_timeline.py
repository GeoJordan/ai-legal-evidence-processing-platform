"""
Behavior Specification

Component:
Timeline

Purpose:
Represents an ordered collection of chronological events.

Timeline shall:

- start empty
- accept timeline events
- maintain chronological ordering
- allow multiple events with the same date
- preserve all events
"""

import pytest

from app.timeline.timeline import Timeline
from app.timeline.timeline_event import TimelineEvent
from datetime import date

def test_timeline_starts_empty():
    timeline = Timeline()

    assert timeline.events() == []

from datetime import date

def test_add_event():
    timeline = Timeline()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    timeline.add_event(event)

    assert len(timeline.events()) == 1

def test_events_are_returned_in_chronological_order():
    timeline = Timeline()

    older = TimelineEvent(
        date=date(2026, 8, 1),
        title="Older Event"
    )

    newer = TimelineEvent(
        date=date(2026, 8, 10),
        title="Newer Event"
    )

    timeline.add_event(newer)
    timeline.add_event(older)

    events = timeline.events()

    assert events[0] == older
    assert events[1] == newer

from datetime import date

def test_duplicate_dates_are_allowed():
    timeline = Timeline()

    first = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    second = TimelineEvent(
        date=date(2026, 8, 1),
        title="Text Message"
    )

    timeline.add_event(first)
    timeline.add_event(second)

    events = timeline.events()

    assert len(events) == 2
    assert first in events
    assert second in events