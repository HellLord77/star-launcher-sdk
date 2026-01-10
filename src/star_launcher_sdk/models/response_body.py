from typing import Literal

from pydantic import BaseModel

from star_launcher_sdk.types import EmptyDict


class ResponseBody[Data: BaseModel](BaseModel):
    code: Literal[200]
    data: Data | EmptyDict | None
    msg: Literal["OK"]
