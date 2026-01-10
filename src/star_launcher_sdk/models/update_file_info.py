from pydantic import BaseModel

from star_launcher_sdk.types import Base64Sha512
from star_launcher_sdk.types import RelativeExePath


class UpdateFileInfo(BaseModel):
    url: RelativeExePath
    sha512: Base64Sha512
    size: int
