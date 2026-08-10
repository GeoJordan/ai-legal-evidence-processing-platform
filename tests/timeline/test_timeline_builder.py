"""
Behavior Specification

Component:
TimelineBuilder

Purpose:
Constructs a Timeline from chronological evidence.

TimelineBuilder shall:

- build an empty timeline
- build a timeline from TimelineEvents
- preserve chronological order
- preserve evidence relationships
"""

from datetime import date

from app.timeline.timeline import Timeline
from app.timeline.timeline_builder import TimelineBuilder
from app.timeline.timeline_event import TimelineEvent
from app.timeline.event_source import EventSource


def test_builder_creates_empty_timeline():
    builder = TimelineBuilder()

    timeline = builder.build([])

    assert isinstance(timeline, Timeline)
    assert timeline.events() == []

def test_builder_adds_single_event():
    builder = TimelineBuilder()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    timeline = builder.build([event])

    assert len(timeline.events()) == 1
    assert timeline.events()[0] == event

def test_builder_preserves_event_sources():
    builder = TimelineBuilder()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    source = EventSource(
        evidence_id="EV-001",
        source_type="Email",
        reference="Inbox/Passport.msg"
    )

    event.add_source(source)

    timeline = builder.build([event])

    built_event = timeline.events()[0]

    assert len(built_event.sources) == 1
    assert built_event.sources[0] == source