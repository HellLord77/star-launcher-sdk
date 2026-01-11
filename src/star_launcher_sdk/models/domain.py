from star_launcher_sdk.types import RootUrl

from .base import Base


class Domain(Base):
    back_up_cdn: RootUrl
    primary_cdn: RootUrl
