from app.models.attachment import Attachment
from app.models.import_summary import ImportSummary


class ImportSummaryGenerator:
    """
    Computes aggregate statistics after an email import.
    """

    def generate(self, attachments):

        return ImportSummary(
            emails_processed=0,
            attachments_discovered=len(attachments),
            attachments_saved=len(attachments),
            total_attachment_size=sum(
                attachment.size
                for attachment in attachments
            ),
            mime_type_counts=self._mime_type_counts(
                attachments
            ),
        )

    def _mime_type_counts(self, attachments):
        counts = {}

        for attachment in attachments:
            counts[attachment.content_type] = (
                counts.get(attachment.content_type, 0) + 1
            )

        return counts