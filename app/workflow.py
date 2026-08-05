"""
EP-202 Workflow Controller

Coordinates execution of the evidence processing pipeline.
"""

from pathlib import Path

from app.configuration import Configuration


class Workflow:
    """Coordinates the execution of processing stages."""

    def __init__(self, config_path: str = "config/case.yaml"):
        self.configuration = Configuration(Path(config_path))

    def run(self):
        """Execute the workflow."""

        print("=" * 50)
        print("AI Legal Evidence Processing Platform")
        print("=" * 50)

        print("Loading configuration...")
        print(f"Case: {self.configuration.case_name}")
        print("Configuration loaded successfully.")

        return True