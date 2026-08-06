from app.timeline.timeline_generator import TimelineGenerator


def test_timeline_generator_can_be_created():

    generator = TimelineGenerator()

    assert generator is not None