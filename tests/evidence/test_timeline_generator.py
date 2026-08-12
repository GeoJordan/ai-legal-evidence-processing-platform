from datetime import datetime

from app.evidence.timeline_generator import TimelineGenerator
from app.evidence.email_evidence import EmailEvidence

def test_returns_empty_list():

    generator = TimelineGenerator()

    timeline = generator.generate([])

    assert timeline == []

def test_returns_single_item():

    generator = TimelineGenerator()

    email = EmailEvidence(
        subject="Hello",
        sent_at=datetime(2026, 1, 10)
    )

    timeline = generator.generate([email])

    assert timeline == [email]

def test_orders_by_date():

    generator = TimelineGenerator()

    older = EmailEvidence(
        subject="Old",
        sent_at=datetime(2026, 1, 1)
    )

    newer = EmailEvidence(
        subject="New",
        sent_at=datetime(2026, 2, 1)
    )

    timeline = generator.generate([
        newer,
        older,
    ])

    assert timeline[0] is older
    assert timeline[1] is newer

def test_preserves_objects():

    generator = TimelineGenerator()

    email = EmailEvidence(
        subject="Quarterly Report"
    )

    timeline = generator.generate([email])

    assert timeline[0] is email