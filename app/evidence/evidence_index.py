class EvidenceIndex:
    """
    Central repository for evidence collected during processing.
    """

    def __init__(self):
        self._messages = []

    def add_message(self, message):
        self._messages.append(message)

    def message_count(self):
        return len(self._messages)
