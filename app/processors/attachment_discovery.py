from email.message import EmailMessage

from app.models.attachment import Attachment


class AttachmentDiscovery:
    """
    Discovers attachments contained in an email message.
    """

    def discover(self, message: EmailMessage) -> list[Attachment]:
        """
        Return all attachments contained in the email.
        """

        attachments: list[Attachment] = []

        for part in message.iter_attachments():

            payload = part.get_payload(decode=True) or b""

            attachments.append(
                Attachment(
                    filename=part.get_filename() or "",
                    content_type=part.get_content_type(),
                    size=len(payload),
                    data=b"",
                )
            )

        return attachments