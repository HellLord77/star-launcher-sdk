import pytest

from star_launcher_sdk import ConfigEnum
from star_launcher_sdk import Game
from star_launcher_sdk import Region
from star_launcher_sdk.config import ConfigModel

pytestmark = [pytest.mark.vcr]


@pytest.fixture(scope="module", params=Game)
def game(request: pytest.FixtureRequest):
    # noinspection PyUnresolvedReferences
    return request.param


@pytest.fixture(scope="module", params=Region)
def region(request: pytest.FixtureRequest):
    # noinspection PyUnresolvedReferences
    return request.param


@pytest.fixture(scope="module")
def launcher(game, region):
    from star_launcher_sdk import Launcher

    config = ConfigModel(game=game, region=region)
    if config in ConfigEnum:
        pytest.skip()

    return Launcher(config)


@pytest.fixture(scope="module")
def unsupported_configuration():
    return (
        ConfigModel(game=Game.HEAVEN_BURNS_RED, region=Region.CHINA),
        ConfigModel(game=Game.MAHJONG_SOUL, region=Region.CHINA),
    )


def test_update_info(launcher):
    update_info = launcher.get_update_info()
    assert update_info is None


def test_hello_world(launcher):
    from star_launcher_sdk.models import HelloWorld

    if launcher.config.region is Region.CHINA:
        pytest.xfail()

    hello_world = launcher.get_hello_world()
    assert isinstance(hello_world, HelloWorld)


def test_banner_and_news(launcher):
    banner_and_news = launcher.get_banner_and_news()
    assert banner_and_news is None


def test_client_info(launcher, unsupported_configuration):
    if launcher.config in unsupported_configuration:
        pytest.xfail()

    client_info = launcher.get_client_info()
    assert client_info is None


def test_domain(launcher):
    domain = launcher.get_domain()
    assert domain is None


def test_game_info(launcher):
    game_info = launcher.get_game_info()
    assert game_info is None


def test_logger(launcher):
    from star_launcher_sdk.models import Logger

    logger = launcher.get_logger()
    assert isinstance(logger, Logger)


def test_logger_config(launcher):
    from star_launcher_sdk.models import LoggerConfig

    logger_config = launcher.get_logger_config()
    assert isinstance(logger_config, LoggerConfig)
