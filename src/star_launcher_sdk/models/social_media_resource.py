from typing import Literal

from pydantic import HttpUrl

from star_launcher_sdk.enums.social_media_channel import SocialMediaChannel

from .base import Base


class SocialMediaResource(Base):
    social_media_channel: SocialMediaChannel
    qr_img: Literal[""]
    jump_url: HttpUrl
