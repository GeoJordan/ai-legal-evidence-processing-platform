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