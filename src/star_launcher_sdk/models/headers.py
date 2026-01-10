from pydantic import BaseModel
from pydantic import ConfigDict

from star_launcher_sdk.utils import to_train


class Headers(BaseModel):
    authorization: str
    user_agent: str

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_train, serialize_by_alias=True)
