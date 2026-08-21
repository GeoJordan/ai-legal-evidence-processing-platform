from email.message import EmailMessage

from app.evidence.correspondent_selector import CorrespondentSelector


def test_selector_matches_target_as_sender():

    message = EmailMessage()
    message["From"] = "person@example.com"
    message["To"] = "me@example.com"

    selector = CorrespondentSelector("person@example.com")

    assert selector.matches(message) is True


def test_selector_matches_target_as_recipient():

    message = EmailMessage()
    message["From"] = "me@example.com"
    message["To"] = "person@example.com"

    selector = CorrespondentSelector("person@example.com")

    assert selector.matches(message) is True


def test_selector_rejects_unrelated_message():

    message = EmailMessage()
    message["From"] = "someone@example.com"
    message["To"] = "another@example.com"

    selector = CorrespondentSelector("person@example.com")

    assert selector.matches(message) is False


def test_selector_matches_cc_and_bcc():

    cc_message = EmailMessage()
    cc_message["From"] = "me@example.com"
    cc_message["To"] = "someone@example.com"
    cc_message["Cc"] = "person@example.com"

    bcc_message = EmailMessage()
    bcc_message["From"] = "me@example.com"
    bcc_message["To"] = "someone@example.com"
    bcc_message["Bcc"] = "person@example.com"

    selector = CorrespondentSelector("person@example.com")

    assert selector.matches(cc_message) is True
    assert selector.matches(bcc_message) is True

def test_selector_matches_multiple_addresses_for_same_correspondent():

    address_1_message = EmailMessage()
    address_1_message["From"] = "person.primary@example.com"
    address_1_message["To"] = "me@example.com"

    address_2_message = EmailMessage()
    address_2_message["From"] = "me@example.com"
    address_2_message["To"] = "person.secondary@example.com"

    unrelated_message = EmailMessage()
    unrelated_message["From"] = "someone@example.com"
    unrelated_message["To"] = "me@example.com"

    selector = CorrespondentSelector(
        [
            "person.primary@example.com",
            "person.secondary@example.com",
        ]
    )

    assert selector.matches(address_1_message) is True
    assert selector.matches(address_2_message) is True
    assert selector.matches(unrelated_message) is False