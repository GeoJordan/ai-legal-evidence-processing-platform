from email.message import Message
from email.utils import parsedate_to_datetime

from app.models.attachment import Attachment
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage


class EmailIngestor:
    """
    Converts a raw RFC-822 email message into the platform's
    normalized EmailHeader and EmailMessage models.
    """

    def ingest(self, raw_message: Message, context):

        date_value = raw_message.get("Date")

        sent_at = (
            parsedate_to_datetime(date_value)
            if date_value
            else None
        )

        references_value = raw_message.get("References", "")

        references = [
            reference.strip()
            for reference in references_value.split()
            if reference.strip()
        ]

        header = EmailHeader(
            message_id=raw_message.get("Message-ID", ""),
            sender=raw_message.get("From", ""),
            to=[
                address.strip()
                for address in raw_message.get("To", "").split(",")
                if address.strip()
            ],
            cc=[
                address.strip()
                for address in raw_message.get("Cc", "").split(",")
                if address.strip()
            ],
            bcc=[
                address.strip()
                for address in raw_message.get("Bcc", "").split(",")
                if address.strip()
            ],
            subject=raw_message.get("Subject", ""),
            sent_at=sent_at,
            reply_to=raw_message.get("Reply-To"),
            in_reply_to=raw_message.get("In-Reply-To"),
            references=references,
        )

        body = ""

        if raw_message.is_multipart():

            for part in raw_message.walk():

                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(
                        part.get_content_charset() or "utf-8",
                        errors="replace",
                    )
                    break

        else:

            payload = raw_message.get_payload(decode=True)

            if payload is not None:
                body = payload.decode(
                    raw_message.get_content_charset() or "utf-8",
                    errors="replace",
                )

        attachments = []

        if raw_message.is_multipart():
            for part in raw_message.walk():
                filename = part.get_filename()

                if not filename:
                    continue

                data = part.get_payload(decode=True) or b""

                attachment = Attachment(
                    filename=filename,
                    content_type=part.get_content_type(),
                    size=len(data),
                    data=data,
                )

                attachments.append(attachment)

        is_html = raw_message.get_content_type() == "text/html"

        message = EmailMessage(
            header=header,
            body=body,
            is_html=is_html,
            attachments=attachments,
        )

        context.headers.append(header)
        context.messages.append(message)
        context.attachments.extend(attachments)
        context.message_count += 1

        return context