from pydantic import BaseModel

from .news_column import NewsColumn


class News(BaseModel):
    news: list[NewsColumn]
