from app.workflow import Workflow


def test_workflow_can_be_created():
    workflow = Workflow()

    assert workflow is not None