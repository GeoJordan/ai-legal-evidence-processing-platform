"""
Behavior Specification

Component:
NarrativeBuilder

NarrativeBuilder shall:

- build an empty Narrative from an empty Timeline
- create one NarrativeSection per TimelineEvent
- preserve chronological order
"""

from app.narrative.narrative_builder import NarrativeBuilder
from app.timeline.timeline import Timeline


def test_builder_creates_empty_narrative():
    builder = NarrativeBuilder()

    timeline = Timeline()

    narrative = builder.build(timeline)

    assert narrative.sections() == []

from datetime import date

from app.timeline.timeline import Timeline
from app.timeline.timeline_event import TimelineEvent
from app.narrative.narrative_builder import NarrativeBuilder


def test_builder_creates_section_from_single_event():
    timeline = Timeline()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    timeline.add_event(event)

    builder = NarrativeBuilder()

    narrative = builder.build(timeline)

    sections = narrative.sections()

    assert len(sections) == 1

def test_section_heading_comes_from_event_title():
    timeline = Timeline()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email"
    )

    timeline.add_event(event)

    narrative = NarrativeBuilder().build(timeline)

    section = narrative.sections()[0]

    assert section.heading == "Passport Email"

def test_section_content_comes_from_event_description():
    timeline = Timeline()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email",
        description="Petitioner requested the child's passport."
    )

    timeline.add_event(event)

    narrative = NarrativeBuilder().build(timeline)

    section = narrative.sections()[0]

    assert section.content == "Petitioner requested the child's passport."

def test_builder_creates_sections_for_multiple_events():
    timeline = Timeline()

    event1 = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Email",
        description="Passport requested."
    )

    event2 = TimelineEvent(
        date=date(2026, 8, 5),
        title="Court Filing",
        description="Petition filed."
    )

    timeline.add_event(event1)
    timeline.add_event(event2)

    narrative = NarrativeBuilder().build(timeline)

    sections = narrative.sections()

    assert len(sections) == 2

    assert sections[0].heading == "Passport Email"
    assert sections[1].heading == "Court Filing"

    assert sections[0].content == "Passport requested."
    assert sections[1].content == "Petition filed."

def test_builder_preserves_timeline_order():
    timeline = Timeline()

    newer = TimelineEvent(
        date=date(2026, 8, 10),
        title="Later Event",
        description="Occurred later."
    )

    older = TimelineEvent(
        date=date(2026, 8, 1),
        title="Earlier Event",
        description="Occurred earlier."
    )

    # Add in reverse order
    timeline.add_event(newer)
    timeline.add_event(older)

    narrative = NarrativeBuilder().build(timeline)

    sections = narrative.sections()

    assert sections[0].heading == "Earlier Event"
    assert sections[1].heading == "Later Event"

from app.timeline.event_source import EventSource


def test_builder_copies_event_sources():
    timeline = Timeline()

    event = TimelineEvent(
        date=date(2026, 8, 1),
        title="Passport Request",
        description="Petitioner requested the child's passport."
    )

    source = EventSource(
        evidence_id="EV-001",
        source_type="Email",
        reference="Inbox/Passport.msg"
    )

    event.add_source(source)

    timeline.add_event(event)

    narrative = NarrativeBuilder().build(timeline)

    section = narrative.sections()[0]

    assert len(section.sources) == 1
    assert section.sources[0] == source