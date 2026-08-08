from examples.generate_case_demo import generate_demo


def test_demo_returns_dashboard():

    dashboard = generate_demo()

    assert dashboard["case"] == "Custody Case"