"""
EP-204 Metadata Extraction Engine
"""


class MetadataExtractor:
    """
    Metadata processing stage.
    """

    def run(self, context):
        """
        Enrich evidence records with metadata.

        Version 1 performs no enrichment yet and simply
        returns the context unchanged.
        """

        return context