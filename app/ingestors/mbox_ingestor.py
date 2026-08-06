"""
EP-206D

MBOX Ingestor
"""
from pathlib import Path
import mailbox

from app.ingestors.base import BaseIngestor
from app.models.attachment import Attachment
from app.models.email_header import EmailHeader
from app.models.email_message import EmailMessage

class MboxIngestor(BaseIngestor):

    @property
    def name(self):
        return "MBOX Ingestor"

    def supports(self, path):

        return Path(path).suffix.lower() == ".mbox"

    def ingest(self, path, context):
        return context

class MboxIngestor(BaseIngestor):

    @property
    def name(self):
        return "MBOX Ingestor"

    def supports(self, path):
        return Path(path).suffix.lower() == ".mbox"

    def open(self, path):
        """
        Open an RFC-compliant MBOX mailbox.
        """
        return mailbox.mbox(path)

    def ingest(self, path, context):
        """
        Populate an EvidenceContext from an MBOX mailbox.
        """

        context.source_path = str(path)

        context.message_count = self.count_messages(path)

        context.headers = self.extract_headers(path)

        context.messages = self.extract_messages(path)

        context.attachments = self.extract_attachments(path)

        return context

    def count_messages(self, path):
        """
        Return the number of messages in an MBOX file.
        """
        mbox = self.open(path)

        return len(mbox)

    def extract_headers(self, path):
        """
        Extract email headers from an MBOX mailbox.

        Returns:
            list[EmailHeader]
        """
        mbox = self.open(path)

        headers = []

        for message in mbox:
            headers.append(
                EmailHeader(
                    sender=message.get("From", ""),
                    recipient=message.get("To", ""),
                    subject=message.get("Subject", ""),
                    date=message.get("Date", ""),
                    message_id=message.get("Message-ID", "")
                )
            )

        return headers

    def extract_messages(self, path):
        """
        Extract complete email messages from an MBOX mailbox.

        Returns:
            list[EmailMessage]
        """
        mbox = self.open(path)

        messages = []

        for message in mbox:

            header = EmailHeader(
                sender=message.get("From", ""),
                recipient=message.get("To", ""),
                subject=message.get("Subject", ""),
                date=message.get("Date", ""),
                message_id=message.get("Message-ID", "")
            )

            body = ""

            if message.is_multipart():
                parts = []

                for part in message.walk():
                    if part.get_content_type() == "text/plain":

                        payload = part.get_payload(decode=True)

                        if payload:
                            parts.append(
                                payload.decode(
                                    part.get_content_charset() or "utf-8",
                                    errors="replace"
                                )
                            )

                body = "\n".join(parts)

            else:
                payload = message.get_payload(decode=True)

                if payload:
                    body = payload.decode(
                        message.get_content_charset() or "utf-8",
                        errors="replace"
                    ).rstrip("\r\n")

            messages.append(
                EmailMessage(
                    header=header,
                    body=body,
                    is_html=False
                )
            )

        return messages

    def extract_attachments(self, path):
        """
        Extract all email attachments from an MBOX mailbox.

        Returns:
            list[Attachment]
        """
        mbox = self.open(path)

        attachments = []

        for message in mbox:

            if not message.is_multipart():
                continue

            for part in message.walk():

                filename = part.get_filename()

                if not filename:
                    continue

                payload = part.get_payload(decode=True) or b""

                attachments.append(
                    Attachment(
                        filename=filename,
                        content_type=part.get_content_type(),
                        size=len(payload),
                        data=payload,
                    )
                )

        return attachments