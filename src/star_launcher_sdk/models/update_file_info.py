from star_launcher_sdk.types import Base64Sha512
from star_launcher_sdk.types import RelativeExePath

from .base import Base


class UpdateFileInfo(Base):
    url: RelativeExePath
    sha512: Base64Sha512
    size: int
