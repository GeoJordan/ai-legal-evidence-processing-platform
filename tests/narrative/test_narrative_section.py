"""
Behavior Specification

Component:
NarrativeSection

NarrativeSection shall:

- store a heading
- store content
"""

from app.narrative.narrative_section import NarrativeSection


def test_section_stores_heading():
    section = NarrativeSection(
        heading="Passport Request",
        content=""
    )

    assert section.heading == "Passport Request"

def test_section_stores_content():
    section = NarrativeSection(
        heading="Passport Request",
        content="On August 1 the petitioner requested..."
    )

    assert section.content == "On August 1 the petitioner requested..."

def test_section_can_start_with_empty_content():
    section = NarrativeSection(
        heading="Passport Request",
        content=""
    )

    assert section.content == ""

from app.timeline.event_source import EventSource


def test_section_starts_with_no_sources():
    section = NarrativeSection(
        heading="Passport Request",
        content="Petitioner requested the child's passport."
    )

    assert section.sources == []

from app.timeline.event_source import EventSource


def test_section_adds_source():
    section = NarrativeSection(
        heading="Passport Request",
        content="Petitioner requested the child's passport."
    )

    source = EventSource(
        evidence_id="EV-001",
        source_type="Email",
        reference="Inbox/Passport.msg"
    )

    section.add_source(source)

    assert len(section.sources) == 1
    assert section.sources[0] == source

from app.timeline.event_source import EventSource


def test_section_preserves_source_order():
    section = NarrativeSection(
        heading="Passport Request",
        content="Petitioner requested the child's passport."
    )

    source1 = EventSource(
        evidence_id="EV-001",
        source_type="Email",
        reference="Inbox/Passport.msg"
    )

    source2 = EventSource(
        evidence_id="EV-002",
        source_type="Court Filing",
        reference="Petition.pdf"
    )

    section.add_source(source1)
    section.add_source(source2)

    assert section.sources[0] == source1
    assert section.sources[1] == source2