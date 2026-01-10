from typing import Literal

from pydantic import BaseModel


class Logger(BaseModel):
    log_upload: Literal[True]
