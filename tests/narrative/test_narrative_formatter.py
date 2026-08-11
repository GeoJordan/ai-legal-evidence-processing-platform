"""
Behavior Specification

Component:
NarrativeFormatter

NarrativeFormatter shall:

- format an empty Narrative
- format a single NarrativeSection
- format multiple NarrativeSections
"""

from app.narrative.narrative_formatter import NarrativeFormatter
from app.narrative.narrative import Narrative


def test_formatter_formats_empty_narrative():
    formatter = NarrativeFormatter()

    narrative = Narrative()

    text = formatter.format(narrative)

    assert text == ""

from app.narrative.narrative import Narrative
from app.narrative.narrative_section import NarrativeSection
from app.narrative.narrative_formatter import NarrativeFormatter


def test_formatter_formats_single_section_heading():
    narrative = Narrative()

    narrative.add_section(
        NarrativeSection(
            heading="Passport Request",
            content=""
        )
    )

    formatter = NarrativeFormatter()

    text = formatter.format(narrative)

    assert text == "Passport Request"

def test_formatter_formats_single_section():
    narrative = Narrative()

    narrative.add_section(
        NarrativeSection(
            heading="Passport Request",
            content="Petitioner requested the child's passport."
        )
    )

    formatter = NarrativeFormatter()

    text = formatter.format(narrative)

    assert text == (
        "Passport Request\n"
        "Petitioner requested the child's passport."
    )

def test_formatter_formats_multiple_sections():
    narrative = Narrative()

    narrative.add_section(
        NarrativeSection(
            heading="Passport Request",
            content="Passport requested."
        )
    )

    narrative.add_section(
        NarrativeSection(
            heading="Court Filing",
            content="Petition filed."
        )
    )

    formatter = NarrativeFormatter()

    text = formatter.format(narrative)

    assert text == (
        "Passport Request\n"
        "Passport requested.\n\n"
        "Court Filing\n"
        "Petition filed."
    )

from app.timeline.event_source import EventSource


def test_formatter_formats_single_evidence_source():
    narrative = Narrative()

    section = NarrativeSection(
        heading="Passport Request",
        content="Petitioner requested the child's passport."
    )

    section.add_source(
        EventSource(
            evidence_id="EV-001",
            source_type="Email",
            reference="Inbox/Passport.msg"
        )
    )

    narrative.add_section(section)

    formatter = NarrativeFormatter()

    text = formatter.format(narrative)

    assert text == (
        "Passport Request\n"
        "Petitioner requested the child's passport.\n\n"
        "Evidence:\n"
        "- EV-001"
    )

def test_formatter_formats_multiple_evidence_sources():
    narrative = Narrative()

    section = NarrativeSection(
        heading="Passport Request",
        content="Petitioner requested the child's passport."
    )

    section.add_source(
        EventSource(
            evidence_id="EV-001",
            source_type="Email",
            reference="Inbox/Passport.msg"
        )
    )

    section.add_source(
        EventSource(
            evidence_id="EV-002",
            source_type="Court Filing",
            reference="Petition.pdf"
        )
    )

    narrative.add_section(section)

    formatter = NarrativeFormatter()

    text = formatter.format(narrative)

    assert text == (
        "Passport Request\n"
        "Petitioner requested the child's passport.\n\n"
        "Evidence:\n"
        "- EV-001\n"
        "- EV-002"
    )


