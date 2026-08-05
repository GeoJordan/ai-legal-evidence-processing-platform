from pathlib import Path

from app.configuration import Configuration


def test_load_configuration():
    config_path = Path("config/case.yaml")

    config = Configuration(config_path)

    assert config.case_name == "Sample Legal Case"
    assert config.case_root.endswith("legal-case-management/case")
    assert ".pdf" in config.supported_extensions