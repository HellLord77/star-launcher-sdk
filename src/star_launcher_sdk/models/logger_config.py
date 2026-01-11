from datetime import datetime

from pydantic import SecretStr
from pydantic.alias_generators import to_pascal

from .base import Base


class LoggerConfig(Base, alias_generator=to_pascal):
    access_key_id: str
    access_key_secret: SecretStr
    expiration: datetime
    security_token: str
