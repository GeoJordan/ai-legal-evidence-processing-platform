from pathlib import Path


class RepositoryPathResolver:
    """
    Resolves logical evidence repository locations into filesystem paths.
    """

    def __init__(self, evidence_root: str | Path):
        self.evidence_root = Path(evidence_root)

    def resolve(
        self,
        package: str,
        stage: str,
        source: str,
    ) -> Path:
        return (
            self.evidence_root
            / package
            / stage
            / source
        )