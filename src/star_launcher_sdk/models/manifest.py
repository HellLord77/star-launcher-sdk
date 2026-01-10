from pydantic import BaseModel

from star_launcher_sdk.types import AbsolutePath

from .file import File


class Manifest(BaseModel):
    source: AbsolutePath
    file: list[File]
