from pathlib import Path

import pytest
from pydantic_yaml import parse_yaml_raw_as


@pytest.fixture
def yaml_data(request: pytest.FixtureRequest, datadir: Path) -> bytes:
    path = datadir / f"{request.node.name}.yaml"
    return path.read_bytes()


@pytest.fixture
def json_data(request: pytest.FixtureRequest, datadir: Path) -> bytes:
    path = datadir / f"{request.node.name}.json"
    return path.read_bytes()


def test_update_info(yaml_data):
    from star_launcher_sdk.models import UpdateInfo

    update_info = parse_yaml_raw_as(UpdateInfo, yaml_data)
    assert isinstance(update_info, UpdateInfo)


def test_hello_world(json_data):
    from star_launcher_sdk.models import HelloWorld

    hello_world = HelloWorld.model_validate_json(json_data)
    assert isinstance(hello_world, HelloWorld)


def test_banner_and_news(json_data):
    from star_launcher_sdk.models import BannerAndNews

    banner_and_news = BannerAndNews.model_validate_json(json_data)
    assert isinstance(banner_and_news, BannerAndNews)


def test_client_info(json_data):
    from star_launcher_sdk.models import ClientInfo

    client_info = ClientInfo.model_validate_json(json_data)
    assert isinstance(client_info, ClientInfo)


def test_domain(json_data):
    from star_launcher_sdk.models import Domain

    domain = Domain.model_validate_json(json_data)
    assert isinstance(domain, Domain)


def test_game_info(json_data):
    from star_launcher_sdk.models import GameInfo

    game_info = GameInfo.model_validate_json(json_data)
    assert isinstance(game_info, GameInfo)


def test_logger(json_data):
    from star_launcher_sdk.models import Logger

    logger = Logger.model_validate_json(json_data)
    assert isinstance(logger, Logger)


def test_logger_config(json_data):
    from star_launcher_sdk.models import LoggerConfig

    logger_config = LoggerConfig.model_validate_json(json_data)
    assert isinstance(logger_config, LoggerConfig)


def test_manifest_url(json_data):
    from star_launcher_sdk.models import ManifestUrl

    manifest_url = ManifestUrl.model_validate_json(json_data)
    assert isinstance(manifest_url, ManifestUrl)


def test_manifest(json_data):
    from star_launcher_sdk.models import Manifest

    manifest = Manifest.model_validate_json(json_data)
    assert isinstance(manifest, Manifest)
