"""
Behavior Specification

Component:
Narrative

Narrative shall:

- start empty
- allow sections to be added
- preserve insertion order
- return all sections
"""

from app.narrative.narrative import Narrative


def test_narrative_starts_empty():
    narrative = Narrative()

    assert narrative.sections() == []

def test_add_section():
    narrative = Narrative()

    narrative.add_section("First section")

    assert narrative.sections() == ["First section"]

def test_sections_are_returned_in_insertion_order():
    narrative = Narrative()

    narrative.add_section("First")
    narrative.add_section("Second")
    narrative.add_section("Third")

    assert narrative.sections() == [
        "First",
        "Second",
        "Third",
    ]