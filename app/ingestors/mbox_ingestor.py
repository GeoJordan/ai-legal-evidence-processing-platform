"""
EP-206D

MBOX Ingestor
"""

from pathlib import Path

import mailbox

from app.ingestors.base import BaseIngestor



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
        return context
