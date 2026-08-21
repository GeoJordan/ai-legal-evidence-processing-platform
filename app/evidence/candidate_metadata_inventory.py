from email.utils import parsedate_to_datetime


class CandidateMetadataInventory:
    """
    Extracts read-only metadata from a selected email candidate.
    """

    def extract(
        self,
        message,
        source_mbox: str,
    ) -> dict:

        date_value = message.get("Date")

        try:
            parsed_date = (
                parsedate_to_datetime(str(date_value))
                if date_value
                else None
            )
        except (TypeError, ValueError, OverflowError):
            parsed_date = None

        has_attachments = any(
            part.get_filename()
            for part in message.walk()
        )

        return {
            "message_id": str(message.get("Message-ID", "")),
            "date": parsed_date,
            "from": str(message.get("From", "")),
            "to": str(message.get("To", "")),
            "subject": str(message.get("Subject", "")),
            "source_mbox": source_mbox,
            "has_attachments": has_attachments,
        }