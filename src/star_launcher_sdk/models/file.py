from pydantic import BaseModel
from pydantic import ByteSize
from pydantic import ConfigDict

from star_launcher_sdk.types import AbsolutePath
from star_launcher_sdk.types import Crc64


class File(BaseModel):
    path: AbsolutePath
    hash: Crc64
    size: ByteSize

    model_config = ConfigDict(arbitrary_types_allowed=True)
