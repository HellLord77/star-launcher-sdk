from pydantic import ByteSize

from star_launcher_sdk.types import AbsolutePath
from star_launcher_sdk.types import Crc64

from .base import Base


class File(Base):
    path: AbsolutePath
    hash: Crc64
    size: ByteSize
