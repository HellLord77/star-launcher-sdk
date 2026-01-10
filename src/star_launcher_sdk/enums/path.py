from enum import StrEnum


class Path(StrEnum):
    BANNER_AND_NEWS = "/api/launcher/operations/resource"
    CLIENT_INFO = "/api/launcher/base/config"
    DOMAIN = "/api/launcher/advanced/game/download/cdn"
    GAME_INFO = "/api/launcher/game/config"
    LOGGER = "/api/launcher/advanced/config"
    LOGGER_CONFIG = "/api/open/api/config"
    MANIFEST_URL = "/api/launcher/game/config/json"
