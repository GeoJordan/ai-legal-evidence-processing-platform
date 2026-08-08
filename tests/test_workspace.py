from app.models.workspace import Workspace


def test_workspace_can_be_created():

    workspace = Workspace("Personal Workspace")

    assert workspace.name == "Personal Workspace"

def test_workspace_starts_with_no_cases():

    workspace = Workspace("Personal Workspace")

    assert workspace.cases == []

from app.models.workspace import Workspace
from app.models.case import Case


def test_workspace_can_add_case():

    workspace = Workspace("Personal Workspace")

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    workspace.add_case(case)

    assert len(workspace.cases) == 1