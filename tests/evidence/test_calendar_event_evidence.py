from app.evidence.calendar_event_evidence import CalendarEventEvidence
from app.evidence.evidence_item import EvidenceItem


# test fields
def test_calendar_event_stores_fields():

    event = CalendarEventEvidence(
        title="Custody Exchange",
        location="Camden Police Station",
        start_time="2026-08-10 17:00",
        end_time="2026-08-10 17:30",
        description="Weekly custody exchange",
    )

    assert event.title == "Custody Exchange"
    assert event.location == "Camden Police Station"
    assert event.start_time == "2026-08-10 17:00"
    assert event.end_time == "2026-08-10 17:30"
    assert event.description == "Weekly custody exchange"

# inheritance
def test_calendar_event_inherits_common_properties():

    event = CalendarEventEvidence()

    assert isinstance(event, EvidenceItem)

# defaults
def test_calendar_event_defaults():

    event = CalendarEventEvidence()

    assert event.title == ""
    assert event.location == ""
    assert event.start_time is None
    assert event.end_time is None
    assert event.description == ""