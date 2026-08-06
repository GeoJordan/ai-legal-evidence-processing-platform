class EvidenceIndex:
    """
    Central repository for evidence collected during processing.
    """

    def __init__(self):
        self._messages = []
        self._attachments = []
        self._headers = []

    # -----------------------
    # Messages
    # -----------------------

    def add_message(self, message):
        self._messages.append(message)

    def message_count(self):
        return len(self._messages)

    # -----------------------
    # Attachments
    # -----------------------

    def add_attachment(self, attachment):
        self._attachments.append(attachment)

    def attachment_count(self):
        return len(self._attachments)

    # -----------------------
    # Headers
    # -----------------------

    def add_header(self, header):
        self._headers.append(header)

    def header_count(self):
        return len(self._headers)
