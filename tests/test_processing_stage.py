from app.processing_stage import ProcessingStage


class DummyStage(ProcessingStage):

    @property
    def name(self):
        return "Dummy"

    def run(self, context):
        return context


def test_processing_stage_can_be_subclassed():

    stage = DummyStage()

    assert stage.name == "Dummy"