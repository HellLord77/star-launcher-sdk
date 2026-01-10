from enum import StrEnum
from typing import Self

from .host import Host
from .salt import Salt


class Region(StrEnum):
    CHINA = "CN", Host.CHINA, Salt.CHINA
    GLOBAL = "EN", Host.GLOBAL, Salt.DEFAULT
    JAPAN = "JP", Host.JAPAN, Salt.DEFAULT
    KOREA = "KR", Host.KOREA, Salt.DEFAULT

    def __new__(cls, value: str, host: Host, salt: Salt) -> type[Self]:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.host = host
        obj.salt = salt
        return obj
