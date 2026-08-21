from email.utils import getaddresses


class CorrespondentSelector:
    """
    Matches email messages involving one or more target correspondent addresses.
    """

    def __init__(self, target_email: str | list[str]):

        if isinstance(target_email, str):
            target_emails = [target_email]
        else:
            target_emails = target_email

        self.target_emails = {
            email_address.strip().lower()
            for email_address in target_emails
            if email_address.strip()
        }

    def matches(self, message) -> bool:

        header_values = []

        for field_name in ("From", "To", "Cc", "Bcc"):
            value = message.get(field_name)

            if value:
                header_values.append(str(value))

        addresses = getaddresses(header_values)

        normalized_addresses = {
            email_address.strip().lower()
            for _, email_address in addresses
            if email_address.strip()
        }

        return bool(
            self.target_emails.intersection(normalized_addresses)
        )