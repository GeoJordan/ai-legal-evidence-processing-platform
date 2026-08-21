from app.processors.metadata_extractor import MetadataExtractor


class EmailImportPipeline:
    """
    Coordinates the complete email evidence import workflow.
    """

    def import_mbox(
        self,
        mbox_path,
        output_directory,
    ):
        raise NotImplementedError

from app.ingestors.email.mbox_reader import MboxReader


class EmailImportPipeline:
    """
    Coordinates the complete email evidence import workflow.
    """

    def __init__(self):

        self._reader = MboxReader()
        self._metadata_extractor = MetadataExtractor()

    def import_mbox(
        self,
        mbox_path,
        output_directory,
    ):

        self._reader = MboxReader(mbox_path)

        return list(self._reader.read())