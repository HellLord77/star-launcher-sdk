from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import SecretStr
from pydantic.alias_generators import to_pascal


class LoggerConfig(BaseModel):
    access_key_id: str
    access_key_secret: SecretStr
    expiration: datetime
    security_token: str

    model_config = ConfigDict(alias_generator=to_pascal)
