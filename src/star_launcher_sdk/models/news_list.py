from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from .news import News


class NewsList(BaseModel):
    code: Literal[0]
    data: News
    message: Literal["ok"]
    timestamp: datetime | None = None
