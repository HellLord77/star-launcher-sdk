from pydantic import BaseModel

from star_launcher_sdk.types import JsonUrl


class ManifestUrl(BaseModel):
    url: JsonUrl
