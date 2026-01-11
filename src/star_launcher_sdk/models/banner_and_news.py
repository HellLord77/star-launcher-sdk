from typing import Literal

from .base import Base
from .news_list import NewsList
from .operations_banner import OperationsBanner


class BannerAndNews(Base):
    banner_loop: bool
    news_list: NewsList | None
    notice_list: None
    operations_banner_list: list[OperationsBanner]
    operations_resource_open: bool
    time_interval: Literal[3, 5]
