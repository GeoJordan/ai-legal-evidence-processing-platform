from app.pipelines.email_import_pipeline import (
    EmailImportPipeline,
)


def test_pipeline_exists():

    pipeline = EmailImportPipeline()

    assert pipeline is not None

import pytest

from pathlib import Path


def test_import_reads_mailbox():

    pipeline = EmailImportPipeline()

    messages = pipeline.import_mbox(
        Path("tests/fixtures/email/empty.mbox"),
        Path("output"),
    )

    assert messages == []

from app.ingestors.email.mbox_reader import MboxReader


def test_pipeline_has_reader():

    pipeline = EmailImportPipeline()

    assert isinstance(
        pipeline._reader,
        MboxReader,
    )

from app.processors.metadata_extractor import MetadataExtractor


def test_pipeline_has_metadata_extractor():

    pipeline = EmailImportPipeline()

    assert isinstance(
        pipeline._metadata_extractor,
        MetadataExtractor,
    )