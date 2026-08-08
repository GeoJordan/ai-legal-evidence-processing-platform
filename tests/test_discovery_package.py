from app.case_management.discovery_package import DiscoveryPackageBuilder
from app.models.case import Case


def test_generate_empty_discovery_package():

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    builder = DiscoveryPackageBuilder()

    package = builder.generate(case)

    assert package["case"] == "Custody Case"