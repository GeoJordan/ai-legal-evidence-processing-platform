from app.pipeline import Pipeline
from app.processing_stage import ProcessingStage


class DummyStage(ProcessingStage):

    @property
    def name(self):
        return "Dummy"

    def run(self, context):
        return context


def test_pipeline_can_add_stage():

    pipeline = Pipeline()

    pipeline.add_stage(DummyStage())

    assert len(pipeline.stages) == 1

from app.configuration import Configuration
from app.context import EvidenceContext


def test_pipeline_runs_all_stages():

    class CounterStage(ProcessingStage):

        @property
        def name(self):
            return "Counter"

        def run(self, context):
            context.statistics["counter"] = (
                context.statistics.get("counter", 0) + 1
            )
            return context

    config = Configuration("config/case.yaml")
    context = EvidenceContext(config)

    pipeline = Pipeline()
    pipeline.add_stage(CounterStage())
    pipeline.add_stage(CounterStage())

    result = pipeline.run(context)

    assert result.statistics["counter"] == 2