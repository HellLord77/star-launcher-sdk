from typing import Literal

from .base import Base


class Logger(Base):
    log_upload: Literal[True]
