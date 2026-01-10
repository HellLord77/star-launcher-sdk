from typing import Literal

from pydantic import BaseModel
from pydantic import HttpUrl

from star_launcher_sdk.enums.social_media_channel import SocialMediaChannel


class SocialMediaResource(BaseModel):
    social_media_channel: SocialMediaChannel
    qr_img: Literal[""]
    jump_url: HttpUrl
