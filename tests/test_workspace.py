from app.models.workspace import Workspace


def test_workspace_can_be_created():

    workspace = Workspace("Personal Workspace")

    assert workspace.name == "Personal Workspace"