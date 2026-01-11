from .base import Base
from .news_column import NewsColumn


class News(Base):
    news: list[NewsColumn]
