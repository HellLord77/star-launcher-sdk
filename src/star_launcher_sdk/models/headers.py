from star_launcher_sdk.utils import to_train

from .base import Base


class Headers(Base, populate_by_name=True, alias_generator=to_train, serialize_by_alias=True):
    authorization: str
