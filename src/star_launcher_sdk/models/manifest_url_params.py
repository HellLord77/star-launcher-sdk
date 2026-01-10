from pydantic import BaseModel
from pydantic_extra_types.semantic_version import SemanticVersion

from star_launcher_sdk.types import RelativeZipPath


class ManifestUrlParams(BaseModel):
    version: SemanticVersion
    file_path: RelativeZipPath
