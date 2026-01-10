from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import HttpUrl

from star_launcher_sdk.types import Crc64
from star_launcher_sdk.types import ImageUrl


class ClientInfo(BaseModel):
    launcher_background_img: ImageUrl
    launcher_background_img_crc64: Crc64
    config_open: bool
    user_agreement: Literal[""] | HttpUrl
    privacy_policy: Literal[""] | HttpUrl
    copyright_information: str
    notice_pop_open: Literal[False]
    notice_content: str
    exit_launcher_open: bool

    model_config = ConfigDict(arbitrary_types_allowed=True)
