from star_launcher_sdk.types import AbsolutePath

from .base import Base
from .file import File


class Manifest(Base):
    source: AbsolutePath
    file: list[File]
