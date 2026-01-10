from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from .news_row import NewsRow


class NewsColumn(BaseModel):
    rows: list[NewsRow]
    type_label: str

    model_config = ConfigDict(alias_generator=to_camel)
