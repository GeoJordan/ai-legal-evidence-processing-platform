from pathlib import Path

from app.configuration import Configuration
from app.scanner import (
    Scanner,
    calculate_sha256,
    scan_directory,
)


def test_calculate_sha256_returns_consistent_hash(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.txt"
    test_file.write_text("sample evidence", encoding="utf-8")

    first_hash = calculate_sha256(test_file)
    second_hash = calculate_sha256(test_file)

    assert first_hash == second_hash
    assert len(first_hash) == 64


def test_scan_directory_finds_nested_files(tmp_path: Path) -> None:
    nested_folder = tmp_path / "nested"
    nested_folder.mkdir()

    supported_file = nested_folder / "message.txt"
    supported_file.write_text("Christmas Break 2024", encoding="utf-8")

    unsupported_file = tmp_path / "document.pdf"
    unsupported_file.write_bytes(b"sample pdf placeholder")

    records = scan_directory(tmp_path)

    assert len(records) == 2

    records_by_name = {
        record.filename: record
        for record in records
    }

    assert records_by_name["message.txt"].supported is True
    assert records_by_name["message.txt"].scan_status == "success"

    assert records_by_name["document.pdf"].supported is False
    assert records_by_name["document.pdf"].scan_status == "success"


def test_scan_directory_raises_for_missing_folder(tmp_path: Path) -> None:
    missing_folder = tmp_path / "missing"

    try:
        scan_directory(missing_folder)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")

def test_scanner_can_be_created():
    config = Configuration("config/case.yaml")

    scanner = Scanner(config)

    assert scanner is not None


def test_scanner_receives_configuration():
    config = Configuration("config/case.yaml")

    scanner = Scanner(config)

    assert scanner.configuration.case_name == "Sample Legal Case"    