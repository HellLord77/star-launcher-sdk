from datetime import datetime
from typing import Literal

from pydantic import HttpUrl

from star_launcher_sdk.types import ImageUrl

from .base import Base


class OperationsBanner(Base):
    banner_img: ImageUrl
    jump_url: Literal[""] | HttpUrl
    remark: str
    start_at: Literal[0] | datetime
    end_at: Literal[0] | datetime
