from __future__ import annotations

import hashlib
from datetime import datetime
from pathlib import Path
from typing import Iterable
from app.models import FileRecord
from app.configuration import Configuration

SUPPORTED_EXTENSIONS = {
    ".txt",
    ".log",
    ".eml",
    ".png",
    ".jpg",
    ".jpeg",
}

class Scanner:
    """
    Evidence Scanner processing stage.
    """

    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def scan(self):
        """
        Scan the configured evidence directory.
        """
        return scan_directory(self.configuration.evidence_path)

def format_timestamp(timestamp: float) -> str:
    """
    Convert a filesystem timestamp to a readable local ISO timestamp.
    """
    return datetime.fromtimestamp(timestamp).astimezone().isoformat(
        timespec="seconds"
    )

def calculate_sha256(
        file_path: Path,
        chunk_size: int = 1024 * 1024,
    ) -> str:
        """
        Calculate the SHA-256 hash of a file.

        The file is read in chunks so large files do not need to be
        loaded entirely into memory.
        """

        sha256 = hashlib.sha256()

        with file_path.open("rb") as file_handle:
            while chunk := file_handle.read(chunk_size):
                sha256.update(chunk)

        return sha256.hexdigest() 


def iter_source_files(source_dir: Path) -> Iterable[Path]:
        """
        Recursively yield files located inside the source directory.
        """

        for path in source_dir.rglob("*"):
            if path.is_file():
                yield path
    
def scan_file(file_path: Path) -> FileRecord:
        """
        Scan one file and return its metadata.

        Errors are returned inside the FileRecord instead of stopping
        the complete scan.
        """

        extension = file_path.suffix.lower()
        supported = extension in SUPPORTED_EXTENSIONS

        try:
            file_stat = file_path.stat()
            file_hash = calculate_sha256(file_path)

            return FileRecord(
                filename=file_path.name,
                original_path=str(file_path.resolve()),
                extension=extension or "[no extension]",
                size_bytes=file_stat.st_size,
                created_timestamp=format_timestamp(file_stat.st_ctime),
                modified_timestamp=format_timestamp(file_stat.st_mtime),
                sha256=file_hash,
                supported=supported,
                scan_status="success",
                scan_notes=(
                    ""
                    if supported
                    else "File type is not supported for text extraction in Version 2.0."
                ),
            )

        except (OSError, PermissionError) as error:
            return FileRecord(
                filename=file_path.name,
                original_path=str(file_path.resolve()),
                extension=extension or "[no extension]",
                size_bytes=0,
                created_timestamp="",
                modified_timestamp="",
                sha256="",
                supported=supported,
                scan_status="error",
                scan_notes=str(error),
            )

def scan_directory(source_dir: str | Path) -> list[FileRecord]:
        """
        Recursively scan a source directory.

        Returns one FileRecord for every file found.
        """

        source_path = Path(source_dir).expanduser().resolve()

        if not source_path.exists():
            raise FileNotFoundError(
                f"Source directory does not exist: {source_path}"
            )

        if not source_path.is_dir():
            raise NotADirectoryError(
                f"Source path is not a directory: {source_path}"
            )

        records: list[FileRecord] = []

        for file_path in iter_source_files(source_path):
            records.append(scan_file(file_path))

        return records    


    

    
