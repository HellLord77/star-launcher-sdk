from star_launcher_sdk.types import DomainUrl

from .base import Base


class Domain(Base):
    back_up_cdn: DomainUrl
    primary_cdn: DomainUrl
