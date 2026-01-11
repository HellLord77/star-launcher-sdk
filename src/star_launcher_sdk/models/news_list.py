from datetime import datetime
from typing import Literal

from .base import Base
from .news import News


class NewsList(Base):
    code: Literal[0]
    data: News
    message: Literal["ok"]
    timestamp: datetime | None = None
