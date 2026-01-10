from pydantic import BaseModel
from pydantic import HttpUrl


class Domain(BaseModel):
    back_up_cdn: HttpUrl
    primary_cdn: HttpUrl
