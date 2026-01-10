import pytest

pytestmark = [pytest.mark.anyio, pytest.mark.vcr]


@pytest.fixture(scope="module")
def launcher():
    import star_launcher_sdk
    from star_launcher_sdk import AsyncLauncher

    return AsyncLauncher(star_launcher_sdk.STELLASORA_EN)


async def test_update_info(launcher):
    from star_launcher_sdk.models import UpdateInfo

    update_info = await launcher.get_update_info()
    assert isinstance(update_info, UpdateInfo)


async def test_hello_world(launcher):
    from star_launcher_sdk.models import HelloWorld

    hello_world = await launcher.get_hello_world()
    assert isinstance(hello_world, HelloWorld)


async def test_banner_and_news(launcher):
    from star_launcher_sdk.models import BannerAndNews

    banner_and_news = await launcher.get_banner_and_news()
    assert isinstance(banner_and_news, BannerAndNews)


async def test_client_info(launcher):
    from star_launcher_sdk.models import ClientInfo

    client_info = await launcher.get_client_info()
    assert isinstance(client_info, ClientInfo)


async def test_domain(launcher):
    from star_launcher_sdk.models import Domain

    domain = await launcher.get_domain()
    assert isinstance(domain, Domain)


async def test_game_info(launcher):
    from star_launcher_sdk.models import GameInfo

    game_info = await launcher.get_game_info()
    assert isinstance(game_info, GameInfo)


async def test_logger(launcher):
    from star_launcher_sdk.models import Logger

    logger = await launcher.get_logger()
    assert isinstance(logger, Logger)


async def test_logger_config(launcher):
    from star_launcher_sdk.models import LoggerConfig

    logger_config = await launcher.get_logger_config()
    assert isinstance(logger_config, LoggerConfig)


async def test_manifest_url(launcher):
    from star_launcher_sdk.models import ManifestUrl

    game_info = await launcher.get_game_info()
    manifest_url = await launcher.get_manifest_url(game_info.game_latest_version, game_info.game_latest_file_path)
    assert isinstance(manifest_url, ManifestUrl)


async def test_manifest(launcher):
    from star_launcher_sdk.models import Manifest

    game_info = await launcher.get_game_info()
    manifest_url = await launcher.get_manifest_url(game_info.game_latest_version, game_info.game_latest_file_path)
    manifest = await launcher.get_manifest(manifest_url)
    assert isinstance(manifest, Manifest)
