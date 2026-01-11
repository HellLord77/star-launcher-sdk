from pydantic.alias_generators import to_camel

from .base import Base
from .news_row import NewsRow


class NewsColumn(Base, alias_generator=to_camel):
    rows: list[NewsRow]
    type_label: str
