from typing import Literal

from .base import Base


class HelloWorld(Base):
    code: Literal[200]
    data: Literal["Hello world"]
    msg: Literal["OK"]
