from typing import Literal

from pydantic import BaseModel


class HelloWorld(BaseModel):
    code: Literal[200]
    data: Literal["Hello world"]
    msg: Literal["OK"]
