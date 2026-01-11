import pytest
from httpx import URL

pytestmark = [pytest.mark.vcr]


@pytest.fixture(scope="module")
def launcher(config):
    from star_launcher_sdk import Launcher

    return Launcher(config)


def test_update_info(launcher):
    from star_launcher_sdk.models import UpdateInfo

    update_info = launcher.get_update_info()
    assert isinstance(update_info, UpdateInfo)


def test_hello_world(launcher):
    from star_launcher_sdk import Region
    from star_launcher_sdk.models import HelloWorld

    if launcher.config.region is Region.CHINA:
        pytest.xfail()
    hello_world = launcher.get_hello_world()
    assert isinstance(hello_world, HelloWorld)


def test_banner_and_news(launcher):
    from star_launcher_sdk.models import BannerAndNews

    banner_and_news = launcher.get_banner_and_news()
    assert isinstance(banner_and_news, BannerAndNews)


def test_client_info(launcher):
    from star_launcher_sdk.models import ClientInfo

    client_info = launcher.get_client_info()
    assert isinstance(client_info, ClientInfo)


def test_domain(launcher):
    from star_launcher_sdk.models import Domain

    domain = launcher.get_domain()
    assert isinstance(domain, Domain)


def test_game_info(launcher):
    from star_launcher_sdk.models import GameInfo

    game_info = launcher.get_game_info()
    assert isinstance(game_info, GameInfo)


def test_logger(launcher):
    from star_launcher_sdk.models import Logger

    logger = launcher.get_logger()
    assert isinstance(logger, Logger)


def test_logger_config(launcher):
    from star_launcher_sdk.models import LoggerConfig

    logger_config = launcher.get_logger_config()
    assert isinstance(logger_config, LoggerConfig)


def test_manifest_url(launcher):
    from star_launcher_sdk.models import ManifestUrl

    game_info = launcher.get_game_info()
    manifest_url = launcher.get_manifest_url(game_info.game_latest_version, game_info.game_latest_file_path)
    assert isinstance(manifest_url, ManifestUrl)


def test_manifest(launcher):
    from star_launcher_sdk.models import Manifest

    game_info = launcher.get_game_info()
    manifest_url = launcher.get_manifest_url(game_info.game_latest_version, game_info.game_latest_file_path)
    manifest = launcher.get_manifest(manifest_url)
    assert isinstance(manifest, Manifest)


def test_update_file_url(launcher):
    update_info = launcher.get_update_info()
    update_file_url = launcher.get_update_file_url(update_info)
    assert isinstance(update_file_url, URL)


def test_get_manifest_file_urls(launcher):
    domain = launcher.get_domain()
    game_info = launcher.get_game_info()
    manifest_url = launcher.get_manifest_url(game_info.game_latest_version, game_info.game_latest_file_path)
    manifest = launcher.get_manifest(manifest_url)

    manifest_file_urls = tuple(launcher.get_manifest_file_urls(domain, manifest))
    backup_manifest_file_urls = tuple(launcher.get_manifest_file_urls(domain, manifest, backup=True))

    assert len(manifest_file_urls) == len(manifest.file)
    assert len(backup_manifest_file_urls) == len(manifest.file)

    assert all(isinstance(url, URL) for url in manifest_file_urls)
    assert all(isinstance(url, URL) for url in backup_manifest_file_urls)

    source = str(manifest.source)[1:]
    assert manifest_file_urls[0] == f"{domain.primary_cdn}{source}{manifest.file[0].path}"
    assert backup_manifest_file_urls[-1] == f"{domain.back_up_cdn}{source}{manifest.file[-1].path}"
