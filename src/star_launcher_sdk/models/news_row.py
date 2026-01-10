from datetime import datetime
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import HttpUrl
from pydantic.alias_generators import to_camel

from star_launcher_sdk.types import ImageUrl


class NewsRow(BaseModel):
    description: str
    link: HttpUrl
    publish_time: datetime
    thumbnail: Literal[""] | ImageUrl
    title: str
    type_label: str

    model_config = ConfigDict(alias_generator=to_camel)
