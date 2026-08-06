"""
EP-205 Pipeline

Executes processing stages in sequence.
"""

from app.context import EvidenceContext
from app.processing_stage import ProcessingStage


class Pipeline:
    """
    Executes processing stages in order.
    """

    def __init__(self):
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        """
        Register a processing stage.

        Returns self to support fluent chaining.
        """
        self.stages.append(stage)
        return self

    def run(self, context: EvidenceContext) -> EvidenceContext:
        """
        Execute every registered stage.
        """
        for stage in self.stages:
            context = stage.run(context)

        return context