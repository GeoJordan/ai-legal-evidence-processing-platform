from app.models.email_header import EmailHeader
from email.utils import parsedate_to_datetime


class MetadataExtractor:
    """
    Extract normalized metadata from an email message.
    """

    def extract(self, message) -> EmailHeader:

        return EmailHeader(
            message_id=message.get("Message-ID", ""),
            sender=message.get("From", ""),
            subject=message.get("Subject", ""),
            to=self._parse_addresses(message.get("To", "")),
            cc=self._parse_addresses(message.get("CC", "")),
            sent_at=self._parse_date(message.get("Date", "")),
        )

    def _parse_addresses(self, value: str) -> list[str]:
        """
        Convert a comma-separated email header into
            a list of addresses.
    """
        return [
            address.strip()
            for address in value.split(",")
            if address.strip()
        ]

    def _parse_date(self, value: str):
        """
        Convert an RFC-822 Date header into a datetime.

        Returns None if the header is missing or invalid.
        """
        if not value:
            return None

        try:
            return parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None