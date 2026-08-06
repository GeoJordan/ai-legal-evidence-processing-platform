"""
EP-205 Processing Framework
"""

from abc import ABC, abstractmethod


class ProcessingStage(ABC):
    """
    Base class for every processing stage.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable stage name.
        """

    @abstractmethod
    def run(self, context):
        """
        Execute the stage.

        Returns
        -------
        EvidenceContext
        """