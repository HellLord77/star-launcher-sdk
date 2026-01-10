from enum import Enum
from typing import Self

from pydantic import BaseModel
from pydantic_extra_types.semantic_version import SemanticVersion

from .enums import Game
from .enums import Region
from .enums.update_url import UpdateUrl


class ConfigModel(BaseModel):
    game: Game
    region: Region = Region.GLOBAL
    version: SemanticVersion = SemanticVersion(1, 0, 0)


class ConfigEnum(Enum):
    HEAVEN_BURNS_RED_GLOBAL = (
        ConfigModel(game=Game.HEAVEN_BURNS_RED, region=Region.GLOBAL),
        UpdateUrl.HEAVEN_BURNS_RED_GLOBAL,
    )

    MAHJONG_SOUL_GLOBAL = ConfigModel(game=Game.MAHJONG_SOUL, region=Region.GLOBAL), UpdateUrl.MAHJONG_SOUL_GLOBAL
    MAHJONG_SOUL_JAPAN = ConfigModel(game=Game.MAHJONG_SOUL, region=Region.JAPAN), UpdateUrl.MAHJONG_SOUL_JAPAN
    MAHJONG_SOUL_KOREA = ConfigModel(game=Game.MAHJONG_SOUL, region=Region.KOREA), UpdateUrl.MAHJONG_SOUL_KOREA

    STELLA_SORA_CHINA = ConfigModel(game=Game.STELLA_SORA, region=Region.CHINA), UpdateUrl.STELLA_SORA_CHINA
    STELLA_SORA_GLOBAL = ConfigModel(game=Game.STELLA_SORA, region=Region.GLOBAL), UpdateUrl.STELLA_SORA_GLOBAL
    STELLA_SORA_JAPAN = ConfigModel(game=Game.STELLA_SORA, region=Region.JAPAN), UpdateUrl.STELLA_SORA_JAPAN
    STELLA_SORA_KOREA = ConfigModel(game=Game.STELLA_SORA, region=Region.KOREA), UpdateUrl.STELLA_SORA_KOREA

    def __new__(cls, value: ConfigModel, update_url: UpdateUrl) -> type[Self]:
        obj = object.__new__(cls)
        obj._value_ = value
        obj.update_url = update_url
        return obj
