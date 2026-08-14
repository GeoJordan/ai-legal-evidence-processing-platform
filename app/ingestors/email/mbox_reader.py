import mailbox

from pathlib import Path
from collections.abc import Iterator
from email.message import EmailMessage



class MboxReader:
    """
    Reads raw messages from an MBOX file.

    This class is intentionally lightweight.
    Parsing and evidence conversion are handled
    by higher-level components.
    """

    def __init__(self, path: Path | None = None):
        self._path = path

    @property
    def path(self):
        return self._path
    
    @property
    def title(self) -> str:
        if self.path is None:
            return ""
        return self.path.name

    def read(self) -> Iterator[EmailMessage]:
        """
        Return an iterator over every email
        contained in the mailbox.

        Raises
        ------
        FileNotFoundError
            If the mailbox does not exist.
        """

        import mailbox

        if self.path is None:
            raise FileNotFoundError("No mailbox path was provided.")

        if not self.path.exists():
            raise FileNotFoundError(
                f"Mailbox not found: {self.path}"
            )

        mbox = mailbox.mbox(str(self.path))

        for message in mbox:
            yield message   