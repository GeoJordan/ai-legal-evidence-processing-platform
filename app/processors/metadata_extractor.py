from app.models.email_header import EmailHeader


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