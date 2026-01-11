from typing import Literal

from star_launcher_sdk.types import EmptyDict

from .base import Base


class ResponseBody[T: Base](Base):
    code: Literal[200]
    data: T | EmptyDict | None
    msg: Literal["OK"]
