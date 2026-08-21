from email.message import EmailMessage

from app.evidence.date_selector import DateSelector


def test_selector_accepts_message_on_start_date():

    message = EmailMessage()
    message["Date"] = "Sat, 01 Jan 2022 10:00:00 -0500"

    selector = DateSelector(start_date="2022-01-01")

    assert selector.matches(message) is True


def test_selector_accepts_message_after_start_date():

    message = EmailMessage()
    message["Date"] = "Thu, 20 Aug 2026 14:30:00 -0400"

    selector = DateSelector(start_date="2022-01-01")

    assert selector.matches(message) is True


def test_selector_rejects_message_before_start_date():

    message = EmailMessage()
    message["Date"] = "Fri, 31 Dec 2021 23:59:59 -0500"

    selector = DateSelector(start_date="2022-01-01")

    assert selector.matches(message) is False


def test_selector_rejects_message_without_date():

    message = EmailMessage()

    selector = DateSelector(start_date="2022-01-01")

    assert selector.matches(message) is False