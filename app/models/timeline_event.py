from dataclasses import dataclass


@dataclass
class TimelineEvent:
    """
    Represents one event on the legal timeline.
    """

    date: str

    sender: str

    recipient: str

    subject: str

    message_id: str