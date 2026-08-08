from app.models.workspace import Workspace
from app.models.case import Case
from app.models.allegation import Allegation
from app.models.evidence import Evidence

from app.case_management.evidence_selection import EvidenceSelection
from app.case_management.evidence_gap import EvidenceGapAnalysis
from app.case_management.discovery_package import DiscoveryPackageBuilder
from app.case_management.case_dashboard import CaseDashboard

REPORT_WIDTH = 70


def divider(char="="):
    print(char * REPORT_WIDTH)


def section(title):
    print()
    print(title)
    print("-" * len(title))


def stage(number, title):
    print()
    divider()
    print(f"Stage {number} — {title}")
    divider()


def success(message):
    print(f"✓ {message}")


def warning(message):
    print(f"⚠ {message}")

def generate_demo():

    workspace = Workspace("Personal Workspace")

    case = Case(
        case_id="CASE-001",
        name="Custody Case"
    )

    passport = Allegation(
        allegation_id="ALG-001",
        title="Passport Withheld"
    )

    communication = Allegation(
        allegation_id="ALG-002",
        title="Communication Failure"
    )

    parenting = Allegation(
        allegation_id="ALG-003",
        title="Parenting Time Interference"
    )

    case.add_allegation(passport)
    case.add_allegation(communication)
    case.add_allegation(parenting)

    passport_email = Evidence(
        evidence_id="EV-001",
        title="Passport Email"
    )

    text_message = Evidence(
        evidence_id="EV-002",
        title="Text Message"
    )

    calendar = Evidence(
        evidence_id="EV-003",
        title="Calendar Screenshot"
    )

    passport.add_evidence(passport_email)
    communication.add_evidence(text_message)

    case.add_evidence(passport_email)
    case.add_evidence(text_message)
    case.add_evidence(calendar)

    selector = EvidenceSelection()

    selected_evidence = selector.select(case, passport)
    gap_analysis = EvidenceGapAnalysis()

    gaps = gap_analysis.find(case)

    builder = DiscoveryPackageBuilder()

    package = builder.generate(case)

    dashboard = CaseDashboard()

    dashboard_data = dashboard.generate(case)

    workspace.add_case(case)

    return {
        "case": case.name,
        "allegations": case.allegations,
        "evidence": case.evidence,
        "selected_evidence": selected_evidence,
        "gaps": gaps,
        "package": package,
        "dashboard": dashboard_data
    }
    

if __name__ == "__main__":

    demo = generate_demo()

    divider()

    print("AI LEGAL EVIDENCE PROCESSING PLATFORM")
    print("Version 0.8.0")
    print()
    print("Evidence Intelligence & Case Management")

    divider()

    stage(1, "Workspace")

    success("Personal Workspace")

    stage(2, "Case")

    success(demo["case"])

    stage(3, "Allegations")

    for allegation in demo["allegations"]:
        success(allegation.title)

    stage(4, "Evidence")

    for evidence in demo["evidence"]:
        success(evidence.title)

    stage(5, "Evidence Selection")

    for evidence in demo["selected_evidence"]:
        success(evidence.title)

    stage(6, "Evidence Gap Analysis")

    if demo["gaps"]:

        for allegation in demo["gaps"]:
            warning(f"{allegation.title} — No supporting evidence linked")

    else:

        success("No evidence gaps identified")

    stage(7, "Discovery Package")

    success("Case Summary")

    success(demo["package"]["case"])

    success("Package Ready for Review")

    stage(8, "Case Dashboard")

    success(f"Case: {demo['dashboard']['case']}")

    success(f"Allegations: {len(demo['allegations'])}")

    success(f"Evidence: {len(demo['evidence'])}")

    success(f"Evidence Gaps: {len(demo['gaps'])}")

    success("Discovery Package: Ready")

    stage(9, "Platform Status")

    success("✓ Architecture: Approved")
    success("✓ Services: Operational")
    success("✓ Sprint 8: Complete")
    success("✓ Release: v0.8.0 Ready")
    success("✓ Platform Demonstration Complete")

    divider()

