from datetime import date
from email.utils import parsedate_to_datetime


class DateSelector:
    """
    Matches email messages on or after a configured start date.
    """

    def __init__(self, start_date: str):
        self.start_date = date.fromisoformat(start_date)

    def matches(self, message) -> bool:

        date_value = message.get("Date")

        if not date_value:
            return False

        try:
            message_datetime = parsedate_to_datetime(str(date_value))
        except (TypeError, ValueError, OverflowError):
            return False

        if message_datetime is None:
            return False

        return message_datetime.date() >= self.start_date