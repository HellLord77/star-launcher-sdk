import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc: pytest.Metafunc):
    from star_launcher_sdk import ConfigEnum

    if "config" in metafunc.fixturenames:
        config = ConfigEnum if metafunc.config.getoption("--all") else (ConfigEnum.STELLA_SORA_GLOBAL,)
        metafunc.parametrize("config", config, scope="module")
