from app.case_management.case_dashboard import CaseDashboard
from app.models.case import Case


def test_dashboard_contains_case_name():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    dashboard = CaseDashboard()

    result = dashboard.generate(case)

    assert result["case"] == "Custody Case"