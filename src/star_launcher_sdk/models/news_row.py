from datetime import datetime
from typing import Literal

from pydantic import HttpUrl
from pydantic.alias_generators import to_camel

from star_launcher_sdk.types import ImageUrl

from .base import Base


class NewsRow(Base, alias_generator=to_camel):
    description: str
    link: HttpUrl
    publish_time: datetime
    thumbnail: Literal[""] | ImageUrl
    title: str
    type_label: str
