from collections.abc import Iterator
from http import HTTPMethod
from typing import override

from httpx import URL
from httpx import AsyncClient
from httpx import Client
from httpx import Request
from httpx import Response
from pydantic_extra_types.semantic_version import SemanticVersion
from pydantic_yaml import parse_yaml_raw_as

from .config import ConfigEnum
from .config import ConfigModel
from .enums.path import Path
from .enums.update_url import UpdateUrl
from .models import BannerAndNews
from .models import ClientInfo
from .models import Domain
from .models import GameInfo
from .models import HelloWorld
from .models import Logger
from .models import LoggerConfig
from .models import Manifest
from .models import ManifestUrl
from .models import UpdateInfo
from .models.base import Base
from .models.headers import Headers
from .models.manifest_url_params import ManifestUrlParams
from .models.response_body import ResponseBody
from .types import RelativeZipPath
from .utils import get_auth_header


def parse_json_response_as[T: Base](model_type: type[T], response: Response) -> T | None:
    # noinspection PyTypeHints
    data = ResponseBody[model_type].model_validate_json(response.content).data
    if data == {}:
        data = None
    return data


class Launcher:
    update_url: UpdateUrl | None = None

    def __init__(self, config: ConfigModel | ConfigEnum, *, client: Client | None = None) -> None:
        if isinstance(config, ConfigEnum):
            self.update_url = config.update_url
            config = config.value
        self.config = config

        if client is None:
            client = Client()
        self.client = client

    def _get_url(self, path: Path | None = None) -> URL:
        base_url = URL(scheme="https", host=self.config.region.host)
        if path is not None:
            base_url = base_url.join(path)
        return base_url

    def _get_headers(self) -> Headers:
        data = ""
        game_id = f"{self.config.game}_{self.config.region}"
        version = str(self.config.version)
        salt = self.config.region.salt

        authorization = get_auth_header(data, game_id, version, salt)
        user_agent = f"{game_id}_GameLauncher/{version}"
        return Headers(authorization=authorization, user_agent=user_agent)

    def _get_request(self, path: Path, params: ManifestUrlParams | None = None) -> Request:
        url = self._get_url(path)
        headers = self._get_headers()

        if params is not None:
            params = params.model_dump()
        headers = headers.model_dump()

        return Request(HTTPMethod.GET, url, params=params, headers=headers)

    def _get_response(self, request: Request) -> Response:
        response = self.client.send(request)
        response.raise_for_status()
        return response

    def _get_simple_response(self, url: str | URL) -> Response:
        request = Request(HTTPMethod.GET, url)
        return self._get_response(request)

    def get_update_info(self) -> UpdateInfo | None:
        if self.update_url is None:
            return None

        url = self.update_url.join("latest.yml")
        response = self._get_simple_response(url)

        return parse_yaml_raw_as(UpdateInfo, response.content)

    def get_hello_world(self) -> HelloWorld:
        url = self._get_url()
        response = self._get_simple_response(url)

        return HelloWorld.model_validate_json(response.content)

    def _get_data[T: Base](self, path: Path, params: ManifestUrlParams | None = None, *, data: type[T]) -> T | None:
        request = self._get_request(path, params)
        response = self._get_response(request)

        return parse_json_response_as(data, response)

    def get_banner_and_news(self) -> BannerAndNews | None:
        return self._get_data(Path.BANNER_AND_NEWS, data=BannerAndNews)

    def get_client_info(self) -> ClientInfo | None:
        return self._get_data(Path.CLIENT_INFO, data=ClientInfo)

    def get_domain(self) -> Domain | None:
        return self._get_data(Path.DOMAIN, data=Domain)

    def get_game_info(self) -> GameInfo | None:
        return self._get_data(Path.GAME_INFO, data=GameInfo)

    def get_logger(self) -> Logger:
        return self._get_data(Path.LOGGER, data=Logger)

    def get_logger_config(self) -> LoggerConfig:
        return self._get_data(Path.LOGGER_CONFIG, data=LoggerConfig)

    def get_manifest_url(self, version: SemanticVersion, file_path: RelativeZipPath) -> ManifestUrl | None:
        params = ManifestUrlParams(version=version, file_path=file_path)
        return self._get_data(Path.MANIFEST_URL, params, data=ManifestUrl)

    def get_manifest(self, manifest_url: ManifestUrl) -> Manifest:
        url = str(manifest_url.url)
        response = self._get_simple_response(url)

        return Manifest.model_validate_json(response.content)

    def get_update_file_url(self, update_info: UpdateInfo) -> URL | None:
        if self.update_url is None:
            return None

        path = str(update_info.path)
        return self.update_url.join(path)

    @staticmethod
    def get_manifest_file_urls(domain: Domain, manifest: Manifest, *, backup: bool = False) -> Iterator[URL]:
        cdn = str(domain.back_up_cdn if backup else domain.primary_cdn)
        path = str(manifest.source)
        url = URL(cdn, path=path)

        for file in manifest.file:
            path = str(file.path)
            yield url.join(path)


class AsyncLauncher(Launcher):
    @override
    def __init__(self, config: ConfigModel | ConfigEnum, *, client: AsyncClient | None = None) -> None:
        if client is None:
            client = AsyncClient()

        super().__init__(config, client=client)

    async def get_update_info(self) -> UpdateInfo | None:
        if self.update_url is None:
            return None

        url = self.update_url.join("latest.yml")
        response = await self._get_simple_response(url)

        return parse_yaml_raw_as(UpdateInfo, response.content)

    async def get_hello_world(self) -> HelloWorld:
        url = self._get_url()
        response = await self._get_simple_response(url)

        return HelloWorld.model_validate_json(response.content)

    async def _get_response(self, request: Request) -> Response:
        response = await self.client.send(request)
        response.raise_for_status()
        return response

    @override
    async def _get_data[T: Base](
        self, path: Path, params: ManifestUrlParams | None = None, *, data: type[T]
    ) -> T | None:
        request = self._get_request(path, params)
        response = await self._get_response(request)

        return parse_json_response_as(data, response)

    @override
    async def get_manifest(self, manifest_url: ManifestUrl) -> Manifest:
        url = str(manifest_url.url)
        response = await self._get_simple_response(url)

        return Manifest.model_validate_json(response.content)
