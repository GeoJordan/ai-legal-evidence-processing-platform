"""
EP-201 Configuration Engine

Loads and validates the Legal Evidence Processing Platform
configuration from config/case.yaml.
"""

from pathlib import Path

import yaml


class Configuration:
    """Loads the application configuration."""

    def __init__(self, config_path: Path):
        self.config_path = Path(config_path)

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with self.config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        # -----------------------------
        # Case
        # -----------------------------
        self.case_name = data["case"]["name"]
        self.case_root = data["case"]["case_root"]

        # -----------------------------
        # Folders
        # -----------------------------
        self.evidence_folder = data["folders"]["evidence"]
        self.exhibits_folder = data["folders"]["exhibits"]
        self.timeline_folder = data["folders"]["timeline"]

        # -----------------------------
        # Processing
        # -----------------------------
        self.supported_extensions = data["processing"][
            "supported_extensions"
        ]

        self.recursive_scan = data["processing"][
            "recursive_scan"
        ]

    @property
    def evidence_path(self) -> Path:
        """Returns the full evidence directory."""
        return Path(self.case_root) / self.evidence_folder

    @property
    def exhibits_path(self) -> Path:
        """Returns the exhibits directory."""
        return Path(self.case_root) / self.exhibits_folder

    @property
    def timeline_path(self) -> Path:
        """Returns the timeline directory."""
        return Path(self.case_root) / self.timeline_folder