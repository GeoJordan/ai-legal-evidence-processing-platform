"""
Behavior Specification

Component:
EventSource

Purpose:
Represents one piece of evidence supporting a TimelineEvent.

EventSource shall:

- store an evidence identifier
- store a source type
- store a human-readable reference
- optionally store metadata
"""

from app.timeline.event_source import EventSource


def test_event_source_stores_evidence_id():
    source = EventSource(
        evidence_id="EV-001"
    )

    assert source.evidence_id == "EV-001"

def test_event_source_stores_source_type():
    source = EventSource(
        evidence_id="EV-001",
        source_type="Email"
    )

    assert source.source_type == "Email"

def test_event_source_stores_reference():
    source = EventSource(
        evidence_id="EV-001",
        source_type="Email",
        reference="Inbox/Passport.msg"
    )

    assert source.reference == "Inbox/Passport.msg"