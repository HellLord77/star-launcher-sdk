from pydantic import HttpUrl

from .base import Base


class Domain(Base):
    back_up_cdn: HttpUrl
    primary_cdn: HttpUrl
